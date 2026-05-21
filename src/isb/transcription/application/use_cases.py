import logging
from pathlib import Path
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.shared_kernel.events import EventBus, TranscriptionCompleted
from isb.transcription.domain.entities import Transcript
from isb.transcription.application.ports import TranscriberPort, TranscriptionManifestPort

logger = logging.getLogger(__name__)

class TranscribeAudioUseCase:
    """Orchestrates the transcription step, invoking Whisper and updating states."""

    def __init__(
        self,
        transcriber_port: TranscriberPort,
        manifest_port: TranscriptionManifestPort,
        event_bus: EventBus
    ) -> None:
        self.transcriber = transcriber_port
        self.manifest = manifest_port
        self.event_bus = event_bus

    def execute(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
        """Transcribe audio track via Whisper, mark manifest, and emit completion event."""
        logger.info("Starting transcription for content %s (audio: %s)", content_id, audio_path)
        self.manifest.mark_status(content_id, ProcessingStatus.TRANSCRIBING)

        try:
            transcript = self.transcriber.transcribe(content_id, audio_path, language_hint=language_hint)
            
            # Update manifest status to next step (SYNTHESIZING)
            self.manifest.mark_status(content_id, ProcessingStatus.SYNTHESIZING)

            # Determine a standard transcript JSON location (sibling of the audio track)
            transcript_path = audio_path.with_suffix(".json")
            
            # Emit domain event
            event = TranscriptionCompleted(
                content_id=content_id,
                transcript_path=transcript_path,
                metadata={
                    "language": transcript.language,
                    "model": transcript.model,
                    "duration_seconds": transcript.duration_seconds,
                    "word_count": transcript.word_count(),
                }
            )
            self.event_bus.publish(event)
            logger.info("Successfully transcribed content %s and published event.", content_id)
            return transcript

        except Exception as err:
            logger.exception("Failed transcription for content %s.", content_id)
            self.manifest.mark_status(content_id, ProcessingStatus.FAILED)
            raise
