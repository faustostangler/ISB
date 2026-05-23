from abc import ABC, abstractmethod
from pathlib import Path
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.transcription.domain.entities import Transcript
from isb.transcription.domain.value_objects import LanguageCode

class TranscriberPort(ABC):
    """Port interface for transcribing audio files using speech-to-text models.

    Decouples application use cases from concrete model implementations (e.g. Whisper).
    """

    @abstractmethod
    def transcribe(
        self,
        content_id: ContentId,
        audio_path: Path,
        language_hint: LanguageCode | None = None
    ) -> Transcript:
        """Run speech-to-text on the audio file and return the constructed Transcript.

        Args:
            content_id: Unique identifier for the media episode.
            audio_path: Local Path location of the extracted audio file.
            language_hint: Optional language preference code passed to Whisper.

        Returns:
            Transcript: The completed Transcript domain entity.
        """
        pass


class TranscriptionManifestPort(ABC):
    """Port interface for updating processing status for the transcription context.

    Abstracts status registry queries to maintain decoupled storage providers.
    """

    @abstractmethod
    def mark_status(self, content_id: ContentId, status: ProcessingStatus) -> None:
        """Update the processing status of the given ContentId.

        Args:
            content_id: System ContentId identifier.
            status: New ProcessingStatus enum value.
        """
        pass
