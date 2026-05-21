import pytest
from datetime import datetime, timezone
from pathlib import Path
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.shared_kernel.events import EventBus, AudioExtracted, TranscriptionCompleted
from isb.ingestion.domain.entities import MediaSource, MediaEpisode
from isb.ingestion.application.use_cases import ExtractAudioUseCase
from isb.transcription.application.use_cases import TranscribeAudioUseCase
from isb.knowledge.application.use_cases import ProcessTranscriptUseCase, SynthesizeWikiUseCase
from isb.knowledge.domain.value_objects import NoteMetadata

# Import our test-double mocks from individual unit tests or create simple pipeline stubs
from tests.ingestion.application.test_use_cases import MockMediaExtractor, MockManifest
from tests.transcription.application.test_use_cases import MockTranscriber, MockTranscriptionManifest
from tests.knowledge.application.test_use_cases import MockLLM, MockVault, MockKnowledgeManifest

def test_end_to_end_event_driven_pipeline() -> None:
    """Test that event-driven coupling propagates extraction to final wiki synthesis."""
    event_bus = EventBus()
    
    # 1. Setup shared SQLite manifest mock (we will use unified mocks or coordinate status updates)
    manifest = MockManifest()
    
    # In a real environment, different contexts might query the same DB,
    # so we wire our mock contexts to query/mark the same registry.
    class UnifiedManifestBridge(MockTranscriptionManifest, MockKnowledgeManifest):
        def __init__(self, target_manifest: MockManifest) -> None:
            self.target = target_manifest
        def mark_status(self, content_id: ContentId, status: ProcessingStatus) -> None:
            self.target.statuses[content_id] = status

    manifest_bridge = UnifiedManifestBridge(manifest)
    
    # 2. Setup adapters
    source = MediaSource(source_id="src-1", url="https://youtube.com/c/karpathy", name="Andrej Karpathy")
    ep1 = MediaEpisode(
        content_id=None,  # Will be assigned UUID by use case
        external_id="yt-karpathy-llm",
        title="Intro to Large Language Models",
        published_at=datetime.now(timezone.utc),
        duration_seconds=3600
    )
    
    extractor = MockMediaExtractor([ep1])
    transcriber = MockTranscriber()
    llm_response = {
        "title": "Andrej Karpathy LLM Guide",
        "summary": "Summary of Karpathy's LLM introduction.",
        "key_takeaways": ["LLM is a file with parameters"],
        "content": "# Andrej Karpathy LLM Guide\n\nNotes from video...",
        "tags": ["karpathy", "llm"],
        "related_topics": []
    }
    llm = MockLLM(llm_response)
    vault = MockVault()
    
    # 3. Setup Use Cases
    extract_use_case = ExtractAudioUseCase(
        extractor_port=extractor,
        manifest_port=manifest,
        event_bus=event_bus
    )
    
    transcribe_use_case = TranscribeAudioUseCase(
        transcriber_port=transcriber,
        manifest_port=manifest_bridge,
        event_bus=event_bus
    )
    
    synthesize_use_case = SynthesizeWikiUseCase(
        llm_port=llm,
        vault_port=vault,
        manifest_port=manifest_bridge,
        event_bus=event_bus
    )
    
    process_use_case = ProcessTranscriptUseCase(
        vault_port=vault,
        manifest_port=manifest_bridge,
        synthesize_use_case=synthesize_use_case
    )
    
    # 4. Wire events (Coupling logic)
    # When audio is extracted, trigger transcription
    def on_audio_extracted(event: AudioExtracted) -> None:
        transcribe_use_case.execute(
            content_id=event.content_id,
            audio_path=event.audio_path,
            language_hint="en"
        )
        
    # When transcription is completed, trigger raw note creation and wiki synthesis
    def on_transcription_completed(event: TranscriptionCompleted) -> None:
        # Load details from metadata to simulate repository load
        process_use_case.execute(
            content_id=event.content_id,
            title="Intro to Large Language Models",
            transcript_text="Transcrição de teste", # Mock text
            metadata=NoteMetadata(
                source_url=source.url,
                channel_name=source.name,
                published_at=datetime.now(timezone.utc),
                processed_at=datetime.now(timezone.utc),
                category="LLMs",
                tags=["llm"]
            )
        )
        
    event_bus.subscribe(AudioExtracted, on_audio_extracted)
    event_bus.subscribe(TranscriptionCompleted, on_transcription_completed)
    
    # 5. Trigger the pipeline!
    results = extract_use_case.execute(source)
    
    # --- Assertions ---
    # Ingestion triggered
    assert len(results) == 1
    episode = results[0]
    cid = episode.content_id
    assert cid is not None
    
    # Manifest status is completed (propagated all the way through)
    assert manifest.statuses[cid] == ProcessingStatus.COMPLETED
    
    # Vault raw note is written
    assert cid in vault.raw_notes
    assert vault.raw_notes[cid].title == "Intro to Large Language Models"
    
    # Vault wiki article is synthesized
    wiki = vault.find_wiki_article_by_title("Andrej Karpathy LLM Guide")
    assert wiki is not None
    assert cid in wiki.source_notes
    assert "karpathy" in wiki.tags
