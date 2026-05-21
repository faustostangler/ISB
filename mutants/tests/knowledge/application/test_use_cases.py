import pytest
from datetime import datetime, timezone
from pathlib import Path
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.shared_kernel.events import EventBus, KnowledgeSynthesized
from isb.knowledge.domain.entities import RawNote, WikiArticle
from isb.knowledge.domain.value_objects import NoteMetadata, SynthesizedArticleSchema
from isb.knowledge.application.ports import LLMPort, VaultPort, KnowledgeManifestPort
from isb.knowledge.application.use_cases import ProcessTranscriptUseCase, SynthesizeWikiUseCase

class MockLLM(LLMPort):
    def __init__(self, response_data: dict) -> None:
        self.response_data = response_data
        self.calls = []

    def synthesize_wiki(self, raw_note: RawNote, existing_articles: list[WikiArticle]) -> SynthesizedArticleSchema:
        self.calls.append((raw_note, existing_articles))
        return SynthesizedArticleSchema(**self.response_data)


class MockVault(VaultPort):
    def __init__(self) -> None:
        self.raw_notes: dict[ContentId, RawNote] = {}
        self.wiki_articles: dict[str, WikiArticle] = {}

    def save_raw_note(self, note: RawNote) -> Path:
        self.raw_notes[note.content_id] = note
        return Path(f"/vault/raw/{note.content_id}.md")

    def save_wiki_article(self, article: WikiArticle) -> Path:
        self.wiki_articles[article.title.lower()] = article
        return Path(f"/vault/wiki/{article.title}.md")

    def list_wiki_articles(self) -> list[WikiArticle]:
        return list(self.wiki_articles.values())

    def find_wiki_article_by_title(self, title: str) -> WikiArticle | None:
        return self.wiki_articles.get(title.lower())


class MockKnowledgeManifest(KnowledgeManifestPort):
    def __init__(self) -> None:
        self.statuses: dict[ContentId, ProcessingStatus] = {}
        self.status_history: list[tuple[ContentId, ProcessingStatus]] = []

    def mark_status(self, content_id: ContentId, status: ProcessingStatus) -> None:
        self.statuses[content_id] = status
        self.status_history.append((content_id, status))


def test_process_transcript_and_synthesis_flow(caplog: pytest.LogCaptureFixture, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test the complete end-to-end processing of a transcript to vault note and wiki synthesis."""
    import logging
    caplog.set_level(logging.INFO)
    
    fixed_time = datetime(2023, 5, 21, 10, 0, 0, tzinfo=timezone.utc)
    class MockDatetime(datetime):
        @classmethod
        def now(cls, tz=None):
            return fixed_time.replace(tzinfo=tz)
    monkeypatch.setattr("isb.knowledge.application.use_cases.datetime", MockDatetime)
    event_bus = EventBus()
    received_events = []
    event_bus.subscribe(KnowledgeSynthesized, lambda e: received_events.append(e))
    
    content_id = ContentId.generate()
    published = datetime.now(timezone.utc)
    meta = NoteMetadata(
        source_url="https://youtube.com/watch?v=123",
        channel_name="Karpathy",
        published_at=published,
        processed_at=published,
        category="AI",
        tags=["llm"]
    )
    
    # Setup LLM Mock response (with duplicates to test de-duplication)
    llm_response = {
        "title": "Large Language Models",
        "summary": "Synthesized summary about LLMs.",
        "key_takeaways": ["LMs predict next tokens"],
        "content": "# Large Language Models\n\nDetailed breakdown...",
        "tags": ["ai", "llm", "ai"],
        "related_topics": ["Deep Learning", "Deep Learning"]
    }
    
    llm = MockLLM(llm_response)
    vault = MockVault()
    manifest = MockKnowledgeManifest()
    
    synthesize_use_case = SynthesizeWikiUseCase(
        llm_port=llm,
        vault_port=vault,
        manifest_port=manifest,
        event_bus=event_bus
    )
    
    process_use_case = ProcessTranscriptUseCase(
        vault_port=vault,
        manifest_port=manifest,
        synthesize_use_case=synthesize_use_case
    )
    
    # Assert constructor dependency assignments
    assert process_use_case.vault is vault
    assert process_use_case.manifest is manifest
    assert process_use_case.synthesize_use_case is synthesize_use_case
    
    # Execute Use Case
    raw_note = process_use_case.execute(
        content_id=content_id,
        title="Intro to LLMs",
        transcript_text="Verbatim transcript content.",
        metadata=meta
    )
    
    # Assert RawNote was saved with correct constructor properties (kills constructor mutants)
    assert raw_note.content_id == content_id
    assert raw_note.title == "Intro to LLMs"
    assert raw_note.transcript_text == "Verbatim transcript content."
    assert raw_note.metadata == meta
    assert vault.raw_notes[content_id] == raw_note
    
    # Assert WikiArticle was synthesized and saved
    assert len(vault.wiki_articles) == 1
    wiki = vault.find_wiki_article_by_title("Large Language Models")
    assert wiki is not None
    assert isinstance(wiki.article_id, ContentId)
    # The article_id must be a newly generated ID, distinct from the source raw_note's content_id
    assert wiki.article_id != content_id
    # The last_updated time must match the mocked time exactly
    assert wiki.last_updated == fixed_time
    assert wiki.last_updated.tzinfo == timezone.utc
    assert wiki.content == "# Large Language Models\n\nDetailed breakdown..."
    assert content_id in wiki.source_notes
    assert manifest.statuses[content_id] == ProcessingStatus.COMPLETED
    assert manifest.status_history == [
        (content_id, ProcessingStatus.SYNTHESIZING),
        (content_id, ProcessingStatus.COMPLETED)
    ]
    
    # Assert LLM calls (parameter validation)
    assert len(llm.calls) == 1
    assert llm.calls[0][0] == raw_note
    assert llm.calls[0][1] == []  # no existing articles yet
    
    # Assert tags and backlinks de-duplication
    assert set(wiki.tags) == {"ai", "llm"}
    assert set(wiki.backlinks) == {"[[Deep Learning]]"}
    
    # Assert event was published
    assert len(received_events) == 1
    assert received_events[0].content_id == content_id
    assert received_events[0].raw_note_path == Path(f"/vault/raw/{content_id}.md")
    assert Path("/vault/wiki/Large Language Models.md") in received_events[0].wiki_articles_updated
    
    # Assert exact logging messages
    assert any(r.message == f"Processing completed transcript for ContentId {content_id} ('Intro to LLMs')" for r in caplog.records)
    assert any(r.message == f"Synthesizing wiki articles for ContentId {content_id} ('Intro to LLMs')" for r in caplog.records)
    assert any(r.message == "Creating new WikiArticle 'Large Language Models'." for r in caplog.records)
    assert any(r.message == f"Completed synthesis for ContentId {content_id}." for r in caplog.records)

def test_synthesize_wiki_use_case_existing_article_merge(caplog: pytest.LogCaptureFixture, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test SynthesizeWikiUseCase when the wiki article already exists in vault, merging content and tags."""
    import logging
    caplog.set_level(logging.INFO)
    
    fixed_time = datetime(2023, 5, 21, 10, 0, 0, tzinfo=timezone.utc)
    class MockDatetime(datetime):
        @classmethod
        def now(cls, tz=None):
            return fixed_time.replace(tzinfo=tz)
    monkeypatch.setattr("isb.knowledge.application.use_cases.datetime", MockDatetime)
    event_bus = EventBus()
    received_events = []
    event_bus.subscribe(KnowledgeSynthesized, lambda e: received_events.append(e))
    
    llm_response = {
        "title": "Large Language Models",
        "summary": "Updated summary.",
        "key_takeaways": ["LMs predict next tokens"],
        "content": "# Large Language Models\n\nUpdated breakdown...",
        "tags": ["ai", "neural-networks"],
        "related_topics": ["Deep Learning"]
    }
    
    llm = MockLLM(llm_response)
    vault = MockVault()
    manifest = MockKnowledgeManifest()
    
    # Pre-populate vault with existing article
    old_cid = ContentId.generate()
    old_time = datetime(2020, 1, 1, tzinfo=timezone.utc)
    existing = WikiArticle(
        article_id=ContentId.generate(),
        title="Large Language Models",
        content="# Large Language Models\n\nOld content",
        tags=["ai", "llm"],
        backlinks=["[[Old Topic]]"],
        source_notes=[old_cid],
        last_updated=old_time
    )
    vault.save_wiki_article(existing)
    
    synthesize_use_case = SynthesizeWikiUseCase(
        llm_port=llm,
        vault_port=vault,
        manifest_port=manifest,
        event_bus=event_bus
    )
    
    new_cid = ContentId.generate()
    published = datetime.now(timezone.utc)
    raw_note = RawNote(
        content_id=new_cid,
        title="Intro to LLMs",
        transcript_text="Verbatim transcript content.",
        metadata=NoteMetadata(
            source_url="https://youtube.com/watch?v=123",
            channel_name="Karpathy",
            published_at=published,
            processed_at=published,
            category="AI",
            tags=["llm"]
        )
    )
    
    results = synthesize_use_case.execute(raw_note)
    
    assert len(results) == 1
    updated = results[0]
    assert updated.title == "Large Language Models"
    assert updated.content == "# Large Language Models\n\nUpdated breakdown..."
    
    # Tags should be merged: old ("ai", "llm") + new ("ai", "neural-networks") -> set -> sorted list
    assert set(updated.tags) == {"ai", "llm", "neural-networks"}
    
    # Backlinks should be merged: old ("[[Old Topic]]") + new ("[[Deep Learning]]") -> set
    assert set(updated.backlinks) == {"[[Old Topic]]", "[[Deep Learning]]"}
    
    # Source notes should have both
    assert set(updated.source_notes) == {old_cid, new_cid}
    
    # Verify manifest statuses and full status history
    assert manifest.statuses[new_cid] == ProcessingStatus.COMPLETED
    assert manifest.status_history == [
        (new_cid, ProcessingStatus.SYNTHESIZING),
        (new_cid, ProcessingStatus.COMPLETED)
    ]

    # Verify vault contains the updated article and raw note
    assert vault.raw_notes[new_cid] == raw_note
    assert vault.find_wiki_article_by_title("Large Language Models") == updated

    # Assert LLM calls (existing article passed correctly)
    assert len(llm.calls) == 1
    assert llm.calls[0][0] == raw_note
    assert llm.calls[0][1] == [existing]
    
    # Assert timezone awareness and last_updated is actually updated to mocked time
    assert updated.last_updated == fixed_time
    assert updated.last_updated.tzinfo == timezone.utc

    # Assert event published with exact details
    assert len(received_events) == 1
    assert received_events[0].content_id == new_cid
    assert received_events[0].raw_note_path == Path(f"/vault/raw/{new_cid}.md")
    assert Path("/vault/wiki/Large Language Models.md") in received_events[0].wiki_articles_updated

    # Assert logging
    assert any(r.message == f"Synthesizing wiki articles for ContentId {new_cid} ('Intro to LLMs')" for r in caplog.records)
    assert any(r.message == "Found existing WikiArticle 'Large Language Models'. Merging content." for r in caplog.records)
    assert any(r.message == f"Completed synthesis for ContentId {new_cid}." for r in caplog.records)

def test_synthesize_wiki_use_case_failure(caplog: pytest.LogCaptureFixture) -> None:
    """Test SynthesizeWikiUseCase when synthesis fails, marking manifest as FAILED and logging exact exception."""
    class FailLLM(LLMPort):
        def synthesize_wiki(self, raw_note: RawNote, existing_articles: list[WikiArticle]) -> SynthesizedArticleSchema:
            raise RuntimeError("LLM synthesis error")
            
    import logging
    caplog.set_level(logging.INFO)
    event_bus = EventBus()
    llm = FailLLM()
    vault = MockVault()
    manifest = MockKnowledgeManifest()
    
    use_case = SynthesizeWikiUseCase(
        llm_port=llm,
        vault_port=vault,
        manifest_port=manifest,
        event_bus=event_bus
    )
    
    cid = ContentId.generate()
    published = datetime.now(timezone.utc)
    raw_note = RawNote(
        content_id=cid,
        title="Intro to LLMs",
        transcript_text="Verbatim transcript content.",
        metadata=NoteMetadata(
            source_url="https://youtube.com/watch?v=123",
            channel_name="Karpathy",
            published_at=published,
            processed_at=published,
            category="AI",
            tags=["llm"]
        )
    )
    
    with pytest.raises(RuntimeError, match="LLM synthesis error"):
        use_case.execute(raw_note)
        
    assert manifest.statuses[cid] == ProcessingStatus.FAILED
    assert manifest.status_history == [
        (cid, ProcessingStatus.SYNTHESIZING),
        (cid, ProcessingStatus.FAILED)
    ]

    # Assert exact logging messages
    assert any(r.message == f"Synthesizing wiki articles for ContentId {cid} ('Intro to LLMs')" for r in caplog.records)
    assert any(r.message == f"Failed synthesis for ContentId {cid}." for r in caplog.records)

def test_synthesize_wiki_use_case_retry_same_source(caplog: pytest.LogCaptureFixture, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that retrying synthesis for the already linked ContentId does not create duplicate source_notes."""
    import logging
    caplog.set_level(logging.INFO)
    
    fixed_time = datetime(2023, 5, 21, 10, 0, 0, tzinfo=timezone.utc)
    class MockDatetime(datetime):
        @classmethod
        def now(cls, tz=None):
            return fixed_time.replace(tzinfo=tz)
    monkeypatch.setattr("isb.knowledge.application.use_cases.datetime", MockDatetime)
    event_bus = EventBus()
    received_events = []
    event_bus.subscribe(KnowledgeSynthesized, lambda e: received_events.append(e))

    llm_response = {
        "title": "Large Language Models",
        "summary": "Updated summary.",
        "key_takeaways": ["LMs predict next tokens"],
        "content": "# Large Language Models\n\nUpdated breakdown...",
        "tags": ["ai"],
        "related_topics": []
    }
    
    llm = MockLLM(llm_response)
    vault = MockVault()
    manifest = MockKnowledgeManifest()
    
    cid = ContentId.generate()
    old_time = datetime(2020, 1, 1, tzinfo=timezone.utc)
    # Pre-populate vault with existing article that already lists cid
    existing = WikiArticle(
        article_id=ContentId.generate(),
        title="Large Language Models",
        content="# Large Language Models\n\nOld content",
        tags=["ai"],
        backlinks=[],
        source_notes=[cid],
        last_updated=old_time
    )
    vault.save_wiki_article(existing)
    
    synthesize_use_case = SynthesizeWikiUseCase(
        llm_port=llm,
        vault_port=vault,
        manifest_port=manifest,
        event_bus=event_bus
    )
    
    raw_note = RawNote(
        content_id=cid,
        title="Intro to LLMs",
        transcript_text="Verbatim transcript content.",
        metadata=NoteMetadata(
            source_url="https://youtube.com/watch?v=123",
            channel_name="Karpathy",
            published_at=datetime.now(timezone.utc),
            processed_at=datetime.now(timezone.utc),
            category="AI",
            tags=["llm"]
        )
    )
    
    results = synthesize_use_case.execute(raw_note)
    assert len(results) == 1
    updated = results[0]
    # source_notes must not contain duplicate cid values
    assert updated.source_notes == [cid]

    # Verify manifest statuses and full status history
    assert manifest.statuses[cid] == ProcessingStatus.COMPLETED
    assert manifest.status_history == [
        (cid, ProcessingStatus.SYNTHESIZING),
        (cid, ProcessingStatus.COMPLETED)
    ]

    # Verify LLM calls parameters
    assert len(llm.calls) == 1
    assert llm.calls[0][0] == raw_note
    assert llm.calls[0][1] == [existing]

    # Assert timezone awareness and last_updated is updated to mocked time
    assert updated.last_updated == fixed_time
    assert updated.last_updated.tzinfo == timezone.utc

    # Assert event published
    assert len(received_events) == 1
    assert received_events[0].content_id == cid

    # Assert logging
    assert any(r.message == f"Synthesizing wiki articles for ContentId {cid} ('Intro to LLMs')" for r in caplog.records)
    assert any(r.message == "Found existing WikiArticle 'Large Language Models'. Merging content." for r in caplog.records)
    assert any(r.message == f"Completed synthesis for ContentId {cid}." for r in caplog.records)


def test_process_transcript_use_case_isolation() -> None:
    """Test ProcessTranscriptUseCase in isolation, verifying save_raw_note is called and synthesis is triggered."""
    class MockSynthesizeOnlyCalls:
        def __init__(self) -> None:
            self.calls = []
        def execute(self, raw_note: RawNote) -> list[WikiArticle]:
            self.calls.append(raw_note)
            return []
            
    vault = MockVault()
    manifest = MockKnowledgeManifest()
    mock_synth = MockSynthesizeOnlyCalls()
    
    use_case = ProcessTranscriptUseCase(
        vault_port=vault,
        manifest_port=manifest,
        synthesize_use_case=mock_synth  # type: ignore
    )
    
    content_id = ContentId.generate()
    published = datetime.now(timezone.utc)
    meta = NoteMetadata(
        source_url="https://youtube.com/watch?v=123",
        channel_name="Karpathy",
        published_at=published,
        processed_at=published,
        category="AI",
        tags=["llm"]
    )
    
    raw_note = use_case.execute(
        content_id=content_id,
        title="Intro to LLMs",
        transcript_text="Verbatim transcript content.",
        metadata=meta
    )
    
    # Assert RawNote was saved in the vault exactly once
    assert content_id in vault.raw_notes
    assert vault.raw_notes[content_id] == raw_note
    
    # Assert the mock synthesize use case was called with the exact raw_note object
    assert mock_synth.calls == [raw_note]


