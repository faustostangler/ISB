from datetime import datetime, timezone
from pathlib import Path
from pydantic import BaseModel, ConfigDict, Field, BeforeValidator
from typing import Annotated
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.ingestion.domain.value_objects import (
    AudioTrack,
    ExternalId,
    EpisodeTitle,
    DurationSeconds,
    PublishedAt,
    SourceId,
    SourceName,
    SourceUrl,
)
from isb.ingestion.domain.exceptions import DuplicateEpisodeError


class MediaEpisode(BaseModel):
    """Domain Entity representing a single episode or video extracted from a source.

    Encapsulates lifecycle transitions and validation state checks for individual
    videos/podcasts as they are processed within the Ingestion bounded context.
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)

    content_id: ContentId
    external_id: Annotated[ExternalId, BeforeValidator(lambda v: ExternalId(v) if isinstance(v, str) else v)]
    title: Annotated[EpisodeTitle, BeforeValidator(lambda v: EpisodeTitle(v) if isinstance(v, str) else v)]
    published_at: Annotated[PublishedAt, BeforeValidator(lambda v: PublishedAt(v) if isinstance(v, datetime) else v)]
    duration_seconds: Annotated[DurationSeconds, BeforeValidator(lambda v: DurationSeconds(v) if isinstance(v, int) else v)]
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
        self.audio_track = AudioTrack(
            file_path=audio_path,
            file_format=file_format,
            size_bytes=size_bytes,
            duration_seconds=int(self.duration_seconds.value)
        )
        # Step 2: Transition the episode status to the next logical stage
        self.status = ProcessingStatus.TRANSCRIBING

    def mark_failed(self) -> None:
        """Mark this episode's ingestion stage as failed."""
        self.status = ProcessingStatus.FAILED

    def is_extracted(self) -> bool:
        """Return True if the audio file has been successfully downloaded/extracted.

        Returns:
            bool: True if an AudioTrack object is associated, False otherwise.
        """
        return self.audio_track is not None


class MediaSource(BaseModel):
    """Domain Entity representing a collection of media episodes (e.g., channel, playlist).

    Coordinates and aggregates episodes fetched from a specific external channel/URL.
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)

    source_id: Annotated[SourceId, BeforeValidator(lambda v: SourceId(v) if isinstance(v, str) else v)]
    url: Annotated[SourceUrl, BeforeValidator(lambda v: SourceUrl(v) if isinstance(v, str) else v)]
    name: Annotated[SourceName, BeforeValidator(lambda v: SourceName(v) if isinstance(v, str) else v)]
    last_synced_at: datetime | None = None
    episodes: list[MediaEpisode] = Field(default_factory=list)

    def add_episode(self, episode: MediaEpisode) -> None:
        """Add an episode to this source, enforcing uniqueness check on external_id.

        Args:
            episode: The MediaEpisode domain entity to add.

        Raises:
            DuplicateEpisodeError: If an episode with the same external_id is already present.
        """
        if self.has_episode(episode.external_id):
            raise DuplicateEpisodeError(f"Episode with external ID {episode.external_id} already exists in source.")
        self.episodes.append(episode)

    def has_episode(self, external_id: ExternalId) -> bool:
        """Check if an episode with the given external ID is already tracked by this source.

        Args:
            external_id: The platform-specific ID (e.g. YouTube video ID).

        Returns:
            bool: True if present in episodes collection, False otherwise.
        """
        return any(str(ep.external_id) == str(external_id) for ep in self.episodes)

    def mark_synced(self) -> None:
        """Update last sync timestamp to current UTC time."""
        self.last_synced_at = datetime.now(timezone.utc)
