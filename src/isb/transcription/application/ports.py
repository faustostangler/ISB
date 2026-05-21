from abc import ABC, abstractmethod
from pathlib import Path
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.transcription.domain.entities import Transcript

class TranscriberPort(ABC):
    """Port interface for transcribing audio files using speech-to-text models."""

    @abstractmethod
    def transcribe(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
        """Run speech-to-text on the audio file and return the constructed Transcript."""
        pass


class TranscriptionManifestPort(ABC):
    """Port interface for updating processing status for the transcription context."""

    @abstractmethod
    def mark_status(self, content_id: ContentId, status: ProcessingStatus) -> None:
        """Update the processing status of the given ContentId."""
        pass
