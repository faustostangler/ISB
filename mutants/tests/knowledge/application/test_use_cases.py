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

    def mark_status(self, content_id: ContentId, status: ProcessingStatus) -> None:
        self.statuses[content_id] = status


def test_process_transcript_and_synthesis_flow() -> None:
    """Test the complete end-to-end processing of a transcript to vault note and wiki synthesis."""
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
    
    # Setup LLM Mock response
    llm_response = {
        "title": "Large Language Models",
        "summary": "Synthesized summary about LLMs.",
        "key_takeaways": ["LMs predict next tokens"],
        "content": "# Large Language Models\n\nDetailed breakdown...",
        "tags": ["ai", "llm"],
        "related_topics": []
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
    
    # Execute Use Case
    raw_note = process_use_case.execute(
        content_id=content_id,
        title="Intro to LLMs",
        transcript_text="Verbatim transcript content.",
        metadata=meta
    )
    
    # Assert RawNote was saved
    assert raw_note.content_id == content_id
    assert vault.raw_notes[content_id] == raw_note
    
    # Assert WikiArticle was synthesized and saved
    assert len(vault.wiki_articles) == 1
    wiki = vault.find_wiki_article_by_title("Large Language Models")
    assert wiki is not None
    assert wiki.content == "# Large Language Models\n\nDetailed breakdown..."
    assert content_id in wiki.source_notes
    assert manifest.statuses[content_id] == ProcessingStatus.COMPLETED
    
    # Assert event was published
    assert len(received_events) == 1
    assert received_events[0].content_id == content_id
    assert received_events[0].raw_note_path == Path(f"/vault/raw/{content_id}.md")
    assert Path("/vault/wiki/Large Language Models.md") in received_events[0].wiki_articles_updated
