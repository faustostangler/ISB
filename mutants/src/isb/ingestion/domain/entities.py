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
    """Domain Entity representing a single episode or video extracted from a source."""
    content_id: ContentId
    external_id: str  # Platform-specific ID (e.g. YouTube video ID)
    title: str
    published_at: datetime
    duration_seconds: int
    status: ProcessingStatus = ProcessingStatus.PENDING
    audio_track: AudioTrack | None = None

    def mark_extracted(self, audio_path: Path, file_format: str, size_bytes: int) -> None:
        """Mark this episode as successfully extracted by linking the AudioTrack."""
        self.audio_track = AudioTrack(
            file_path=audio_path,
            file_format=file_format,
            size_bytes=size_bytes,
            duration_seconds=self.duration_seconds
        )
        self.status = ProcessingStatus.TRANSCRIBING

    def mark_failed(self) -> None:
        """Mark this episode's ingestion stage as failed."""
        self.status = ProcessingStatus.FAILED

    def is_extracted(self) -> bool:
        """Return True if the audio file has been successfully downloaded/extracted."""
        return self.audio_track is not None


@dataclass
class MediaSource:
    """Domain Entity representing a collection of media episodes (e.g., channel, playlist)."""
    source_id: str
    url: str
    name: str
    last_synced_at: datetime | None = None
    episodes: list[MediaEpisode] = field(default_factory=list)

    def add_episode(self, episode: MediaEpisode) -> None:
        """Add an episode to this source, enforcing uniqueness check on external_id."""
        if self.has_episode(episode.external_id):
            raise DuplicateEpisodeError(f"Episode with external ID {episode.external_id} already exists in source.")
        self.episodes.append(episode)

    def has_episode(self, external_id: str) -> bool:
        """Check if an episode with the given external ID is already tracked by this source."""
        return any(ep.external_id == external_id for ep in self.episodes)

    def mark_synced(self) -> None:
        """Update last sync timestamp to current UTC time."""
        self.last_synced_at = datetime.now(timezone.utc)
