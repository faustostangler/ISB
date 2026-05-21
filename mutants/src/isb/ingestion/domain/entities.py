from datetime import datetime, timezone
from pathlib import Path
from dataclasses import dataclass, field
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.ingestion.domain.value_objects import AudioTrack
from isb.ingestion.domain.exceptions import DuplicateEpisodeError
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore

@dataclass
class MediaEpisode:
    """Domain Entity representing a single episode or video extracted from a source.

    Encapsulates lifecycle transitions and validation state checks for individual
    videos/podcasts as they are processed within the Ingestion bounded context.
    """
    content_id: ContentId
    external_id: str  # Platform-specific ID (e.g. YouTube video ID)
    title: str
    published_at: datetime
    duration_seconds: int
    status: ProcessingStatus = ProcessingStatus.PENDING
    audio_track: AudioTrack | None = None

    def mark_extracted(self, audio_path: Path, file_format: str, size_bytes: int) -> None:
        """Mark this episode as successfully extracted by linking the AudioTrack.

        Transition status to TRANSCRIBING since downstream processes expect a local audio file.

        Args:
            audio_path: Path to the local audio file.
            file_format: File format extension string (e.g., mp3, m4a).
            size_bytes: Size of the extracted audio file in bytes.
        """
        # Step 1: Instantiate and associate the immutable AudioTrack Value Object
        # We encapsulate this data to guarantee the presence of required file system details
        self.audio_track = AudioTrack(
            file_path=audio_path,
            file_format=file_format,
            size_bytes=size_bytes,
            duration_seconds=self.duration_seconds
        )
        # Step 2: Transition the episode status to the next logical stage
        self.status = ProcessingStatus.TRANSCRIBING

    def mark_failed(self) -> None:
        """Mark this episode's ingestion stage as failed."""
        # Step 1: Transition the internal status state to FAILED
        # Signals the pipeline that this episode is eligible for retry execution on next sync
        self.status = ProcessingStatus.FAILED

    def is_extracted(self) -> bool:
        """Return True if the audio file has been successfully downloaded/extracted.

        Returns:
            bool: True if an AudioTrack object is associated, False otherwise.
        """
        # Step 1: Check presence of local AudioTrack mapping
        return self.audio_track is not None


@dataclass
class MediaSource:
    """Domain Entity representing a collection of media episodes (e.g., channel, playlist).

    Coordinates and aggregates episodes fetched from a specific external channel/URL.
    """
    source_id: str
    url: str
    name: str
    last_synced_at: datetime | None = None
    episodes: list[MediaEpisode] = field(default_factory=list)

    def add_episode(self, episode: MediaEpisode) -> None:
        """Add an episode to this source, enforcing uniqueness check on external_id.

        Args:
            episode: The MediaEpisode domain entity to add.

        Raises:
            DuplicateEpisodeError: If an episode with the same external_id is already present.
        """
        # Step 1: Perform validation check for uniqueness within this source aggregate
        # We do this to prevent duplicate downloads/transcriptions of the same video
        if self.has_episode(episode.external_id):
            raise DuplicateEpisodeError(f"Episode with external ID {episode.external_id} already exists in source.")
        # Step 2: Append the episode to the collection if unique
        self.episodes.append(episode)

    def has_episode(self, external_id: str) -> bool:
        """Check if an episode with the given external ID is already tracked by this source.

        Args:
            external_id: The platform-specific ID (e.g. YouTube video ID).

        Returns:
            bool: True if present in episodes collection, False otherwise.
        """
        # Step 1: Search through list of child entities for matching external_id
        return any(ep.external_id == external_id for ep in self.episodes)

    def mark_synced(self) -> None:
        """Update last sync timestamp to current UTC time."""
        # Step 1: Update the sync timestamp to track history of source scanning events
        self.last_synced_at = datetime.now(timezone.utc)
