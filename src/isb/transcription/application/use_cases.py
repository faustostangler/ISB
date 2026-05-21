import logging
from pathlib import Path
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.shared_kernel.events import EventBus, TranscriptionCompleted
from isb.transcription.domain.entities import Transcript
from isb.transcription.application.ports import TranscriberPort, TranscriptionManifestPort

logger = logging.getLogger(__name__)

class TranscribeAudioUseCase:
    """Orchestrates the transcription step, invoking Whisper and updating states.

    Acts as the workflow coordinator that accepts extracted audio, queries the
    speech-to-text transcriber port, transitions manifest state processing flags,
    and publishes transcription completion events for downstream knowledge compilation.
    """

    def __init__(
        self,
        transcriber_port: TranscriberPort,
        manifest_port: TranscriptionManifestPort,
        event_bus: EventBus
    ) -> None:
        """Initialize use case dependencies via construction injection.

        Args:
            transcriber_port: Port adapter implementing TranscriberPort.
            manifest_port: Port adapter implementing TranscriptionManifestPort.
            event_bus: The core system EventBus instance.
        """
        # Step 1: Bind injected dependencies to local attributes
        self.transcriber = transcriber_port
        self.manifest = manifest_port
        self.event_bus = event_bus

    def execute(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
        """Transcribe audio track via Whisper, mark manifest, and emit completion event.

        Args:
            content_id: Unique domain content identifier.
            audio_path: Local Path reference to the source audio file.
            language_hint: Optional language identifier for speech translation mapping.

        Returns:
            Transcript: The generated Transcript domain entity.
        """
        # Step 1: Log use case initiation audit log
        logger.info("Starting transcription for content %s (audio: %s)", content_id, audio_path)
        
        # Step 2: Mark database manifest status to TRANSCRIBING
        self.manifest.mark_status(content_id, ProcessingStatus.TRANSCRIBING)

        try:
            # Step 3: Call speech-to-text service via the TranscriberPort adapter
            transcript = self.transcriber.transcribe(content_id, audio_path, language_hint=language_hint)
            
            # Step 4: Update manifest status to next step (SYNTHESIZING)
            # Informs concurrent tracking workers that raw transcription is done
            # and synthesis is about to begin.
            self.manifest.mark_status(content_id, ProcessingStatus.SYNTHESIZING)

            # Step 5: Determine standard transcript JSON output storage location
            # We save the JSON as a sibling of the audio file to keep files organized by content ID
            transcript_path = audio_path.with_suffix(".json")
            
            # Step 6: Create and publish the TranscriptionCompleted domain event
            # Broadcasts transcript details and metadata so the Knowledge context can parse it.
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
            
            # Step 7: Log final output summary and return the domain entity
            logger.info("Successfully transcribed content %s and published event.", content_id)
            return transcript

        except Exception as err:
            # Step 8: Handle transcription failures gracefully
            # Marks the manifest status as FAILED to allow clean retry configurations.
            logger.exception("Failed transcription for content %s.", content_id)
            self.manifest.mark_status(content_id, ProcessingStatus.FAILED)
            raise
