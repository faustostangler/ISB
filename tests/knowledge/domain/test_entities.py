import pytest
from datetime import datetime, timezone
from isb.shared_kernel.types import ContentId
from isb.knowledge.domain.entities import RawNote, WikiArticle
from isb.transcription.domain.value_objects import TranscriptText
from isb.knowledge.domain.value_objects import (
    NoteMetadata,
    SynthesizedArticleSchema,
    NoteTitle,
    ArticleContent,
    ArticleTag,
    ArticleBacklink,
)
from pydantic import ValidationError

def test_note_metadata_validation() -> None:
    """Test validating NoteMetadata value object."""
    meta = NoteMetadata(
        source_url="https://youtube.com/watch?v=123",
        channel_name="Karpathy",
        published_at=datetime.now(timezone.utc),
        processed_at=datetime.now(timezone.utc),
        category="AI",
        tags=["llm", "wiki"]
    )
    assert meta.channel_name == "Karpathy"
    assert "llm" in meta.tags

def test_raw_note_obsidian_markdown() -> None:
    """Test generating Obsidian markdown for a RawNote."""
    content_id = ContentId.generate()
    published = datetime(2026, 5, 21, 12, 0, 0, tzinfo=timezone.utc)
    processed = datetime(2026, 5, 21, 14, 0, 0, tzinfo=timezone.utc)
    
    meta = NoteMetadata(
        source_url="https://youtube.com/watch?v=123",
        channel_name="Karpathy",
        published_at=published,
        processed_at=processed,
        category="AI",
        tags=["llm", "wiki"]
    )
    
    raw_note = RawNote(
        content_id=content_id,
        title=NoteTitle("Intro to LLMs"),
        transcript_text=TranscriptText("This is a test transcript."),
        metadata=meta
    )
    
    markdown = raw_note.to_obsidian_markdown()
    
    # Assert YAML frontmatter exists
    assert "---" in markdown
    assert "title: Intro to LLMs" in markdown
    assert "channel_name: Karpathy" in markdown
    assert "source_url: https://youtube.com/watch?v=123" in markdown
    assert "category: AI" in markdown
    assert "tags:\n- llm\n- wiki" in markdown
    assert "This is a test transcript." in markdown

def test_wiki_article_obsidian_markdown() -> None:
    """Test generating Obsidian markdown for a WikiArticle."""
    article_id = ContentId.generate()
    source_id1 = ContentId.generate()
    
    article = WikiArticle(
        article_id=article_id,
        title=NoteTitle("Large Language Models"),
        content=ArticleContent("Comprehensive guide on LLMs."),
        tags=[ArticleTag("ai"), ArticleTag("deep-learning")],
        backlinks=[ArticleBacklink("[[Intro to LLMs]]")],
        source_notes=[source_id1],
        last_updated=datetime.now(timezone.utc)
    )
    
    markdown = article.to_obsidian_markdown()
    
    assert "---" in markdown
    assert "title: Large Language Models" in markdown
    assert "tags:\n- ai\n- deeplearning" in markdown
    assert f"source_notes:\n- {source_id1}" in markdown
    assert "Comprehensive guide on LLMs." in markdown

def test_synthesized_article_schema_validation() -> None:
    """Test Pydantic schema validation for LLM-synthesized outputs."""
    valid_data = {
        "title": "Neural Networks",
        "summary": "A guide on neural networks",
        "key_takeaways": ["Takeaway 1", "Takeaway 2"],
        "content": "# Neural Networks\n\nDeep learning fundamentals...",
        "tags": ["deep-learning", "networks"],
        "related_topics": ["Backpropagation", "Gradient Descent"]
    }
    
    schema = SynthesizedArticleSchema(**valid_data)
    assert schema.title == "Neural Networks"
    assert len(schema.key_takeaways) == 2
    
    # Test invalid data missing required fields
    invalid_data = {
        "title": "Neural Networks",
        # summary is missing
        "key_takeaways": []
    }
    
    with pytest.raises(ValidationError):
        SynthesizedArticleSchema(**invalid_data)

def test_knowledge_value_objects_validation() -> None:
    """Test validations for NoteTitle, ArticleContent, ArticleTag, and ArticleBacklink."""
    with pytest.raises(ValueError):
        NoteTitle("Invalid/Title")
    with pytest.raises(ValueError):
        NoteTitle("   ")
    with pytest.raises(TypeError):
        NoteTitle(123)  # type: ignore

    with pytest.raises(ValueError):
        ArticleContent("short")
    with pytest.raises(TypeError):
        ArticleContent(None)  # type: ignore

    with pytest.raises(ValueError):
        ArticleTag("!!!")
    with pytest.raises(TypeError):
        ArticleTag(123)  # type: ignore

    with pytest.raises(ValueError):
        ArticleBacklink("not-a-link")
    with pytest.raises(ValueError):
        ArticleBacklink("[[]]")
    with pytest.raises(TypeError):
        ArticleBacklink(123)  # type: ignore
