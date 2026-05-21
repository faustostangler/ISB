from abc import ABC, abstractmethod
from pathlib import Path
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.ingestion.domain.entities import MediaSource, MediaEpisode

class MediaExtractorPort(ABC):
    """Port interface for extracting media source metadata and extracting audio tracks."""

    @abstractmethod
    def fetch_new_episodes(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetch list of metadata episodes from the external media source URL."""
        pass

    @abstractmethod
    def extract_audio(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Extract the audio file and return the local path, file format, and size in bytes."""
        pass


class ManifestPort(ABC):
    """Port interface for storing and querying processed content status (idempotency registry)."""

    @abstractmethod
    def is_processed(self, external_id: str) -> bool:
        """Check if an external ID has been successfully processed or is currently processing."""
        pass

    @abstractmethod
    def get_content_id(self, external_id: str) -> ContentId | None:
        """Get the internal ContentId registered to this external ID, if exists."""
        pass

    @abstractmethod
    def register_episode(self, external_id: str, content_id: ContentId) -> None:
        """Register a new external ID with an internal ContentId."""
        pass

    @abstractmethod
    def mark_status(self, content_id: ContentId, status: ProcessingStatus) -> None:
        """Update the processing status of the given ContentId."""
        pass

    @abstractmethod
    def has_failed_previously(self, external_id: str) -> bool:
        """Check if an external ID has previously failed processing."""
        pass
