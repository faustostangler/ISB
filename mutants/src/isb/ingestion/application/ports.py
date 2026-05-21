from abc import ABC, abstractmethod
from pathlib import Path
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.ingestion.domain.entities import MediaSource, MediaEpisode
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
