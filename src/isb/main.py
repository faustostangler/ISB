import logging
from isb.config import settings
from isb.shared_kernel.events import EventBus, AudioExtracted, TranscriptionCompleted
# Import interfaces (Ports) and Use Cases
from isb.ingestion.application.use_cases import ExtractAudioUseCase
from isb.transcription.application.use_cases import TranscribeAudioUseCase
from isb.knowledge.application.use_cases import ProcessTranscriptUseCase, SynthesizeWikiUseCase
from isb.knowledge.domain.value_objects import NoteMetadata

# Logging Setup
logging.basicConfig(level=logging.INFO if not settings.DEBUG else logging.DEBUG)
logger = logging.getLogger(__name__)

def main() -> None:
    """Composition Root: Wire adapters to ports and register event-driven orchestration."""
    logger.info("Initializing Intelligent Second Brain (ISB) in %s mode...", settings.ENV)

    # 1. Instantiate Core Event Bus
    event_bus = EventBus()

    # 2. Instantiate Adapters (Stubs for now, concrete adapters will be wired here in future turns)
    # e.g.,
    # extractor_adapter = YtDlpExtractorAdapter(media_data_dir=settings.MEDIA_DATA_DIR)
    # manifest_adapter = SQLiteManifestAdapter(db_path=settings.MANIFEST_DB_PATH)
    # transcriber_adapter = WhisperTranscriberAdapter(model_name=settings.WHISPER_MODEL)
    # llm_adapter = OllamaLLMAdapter(base_url=settings.OLLAMA_BASE_URL, model_name=settings.OLLAMA_MODEL)
    # vault_adapter = ObsidianVaultAdapter(vault_root=settings.OBSIDIAN_VAULT_PATH)
    
    # 3. Instantiate Use Cases (Passing ports as constructor parameters)
    # extract_audio_use_case = ExtractAudioUseCase(
    #     extractor_port=extractor_adapter,
    #     manifest_port=manifest_adapter,
    #     event_bus=event_bus
    # )
    # transcribe_use_case = TranscribeAudioUseCase(
    #     transcriber_port=transcriber_adapter,
    #     manifest_port=manifest_adapter, # Sharing database manifest
    #     event_bus=event_bus
    # )
    # synthesize_use_case = SynthesizeWikiUseCase(
    #     llm_port=llm_adapter,
    #     vault_port=vault_adapter,
    #     manifest_port=manifest_adapter,
    #     event_bus=event_bus
    # )
    # process_transcript_use_case = ProcessTranscriptUseCase(
    #     vault_port=vault_adapter,
    #     manifest_port=manifest_adapter,
    #     synthesize_use_case=synthesize_use_case
    # )

    # 4. Wire Event-Driven Subscriptions (ACL boundaries)
    # @event_bus.subscribe(AudioExtracted)
    # def handle_audio_extracted(event: AudioExtracted) -> None:
    #     transcribe_use_case.execute(
    #         content_id=event.content_id,
    #         audio_path=event.audio_path,
    #         language_hint=settings.WHISPER_LANGUAGES[0] if settings.WHISPER_LANGUAGES else None
    #     )

    # @event_bus.subscribe(TranscriptionCompleted)
    # def handle_transcription_completed(event: TranscriptionCompleted) -> None:
    #     # Extract metadata from event or DB
    #     meta = NoteMetadata(
    #         source_url="...",
    #         channel_name="...",
    #         published_at=event.occurred_at,
    #         processed_at=event.occurred_at
    #     )
    #     process_transcript_use_case.execute(
    #         content_id=event.content_id,
    #         title=f"Note {event.content_id}",
    #         transcript_text="...", # Retrieved from transcript_path
    #         metadata=meta
    #     )

    logger.info("Composition blueprint successfully registered. System is modular-ready.")

if __name__ == "__main__":
    main()
