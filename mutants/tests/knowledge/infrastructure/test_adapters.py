import json
import httpx
import pytest
import yaml
from pathlib import Path
from datetime import datetime, timezone
from unittest.mock import MagicMock, patch
from isb.shared_kernel.types import ContentId
from isb.knowledge.domain.entities import RawNote, WikiArticle
from isb.knowledge.domain.value_objects import NoteMetadata, SynthesizedArticleSchema
from isb.knowledge.infrastructure.adapters import OllamaLLMAdapter, ObsidianVaultAdapter

# =====================================================================
# OllamaLLMAdapter Tests
# =====================================================================

def test_ollama_adapter_init() -> None:
    """Verify that OllamaLLMAdapter sets URLs and initializes HTTP clients."""
    # Step 1: Instantiate adapter
    adapter = OllamaLLMAdapter(base_url="http://fake-ollama:11434", model_name="qwen2.5:7b")
    
    # Step 2: Assert attributes
    assert adapter.base_url == "http://fake-ollama:11434"
    assert adapter.model_name == "qwen2.5:7b"
    assert isinstance(adapter.client, httpx.Client)

def test_ollama_adapter_synthesize_wiki() -> None:
    """Verify that synthesize_wiki formats prompts, posts to Ollama, and parses the response."""
    # Step 1: Initialize adapter
    adapter = OllamaLLMAdapter(base_url="http://fake-ollama:11434", model_name="qwen2.5:7b")
    
    # Step 2: Construct a raw note and metadata
    metadata = NoteMetadata(
        source_url="https://youtube.com/watch?v=123",
        channel_name="Tech Channel",
        published_at=datetime(2026, 5, 20, tzinfo=timezone.utc),
        processed_at=datetime.now(timezone.utc)
    )
    raw_note = RawNote(
        content_id=ContentId.generate(),
        title="Docker Basics",
        transcript_text="This is the raw transcription content explaining Docker containers.",
        metadata=metadata
    )

    # Step 3: Define mock response dict that the LLM generates
    llm_payload = {
        "title": "Docker Basics",
        "summary": "This is a detailed summary explaining docker basics containerization.",
        "key_takeaways": [
            "Containers bundle code and dependencies.",
            "Images are immutable blueprints.",
            "Docker simplifies local developer environments."
        ],
        "content": "Detailed body content explaining Docker containers in more than fifty characters.",
        "tags": ["docker", "devops"],
        "related_topics": []
    }

    # Step 4: Mock the response from Ollama API
    fake_api_response = {
        "response": json.dumps(llm_payload)
    }

    # Step 5: Patch httpx.Client.post to return the mocked response
    with patch.object(adapter.client, "post") as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = fake_api_response
        mock_post.return_value = mock_response

        # Step 6: Execute synthesize_wiki
        schema = adapter.synthesize_wiki(raw_note, [])

        # Step 7: Assert POST request parameters
        mock_post.assert_called_once()
        post_url = mock_post.call_args[0][0]
        post_json = mock_post.call_args[1]["json"]
        
        assert post_url == "http://fake-ollama:11434/api/generate"
        assert post_json["model"] == "qwen2.5:7b"
        assert post_json["format"] == "json"
        assert post_json["stream"] is False
        assert "Docker Basics" in post_json["prompt"]

        # Step 8: Verify return schema attributes
        assert isinstance(schema, SynthesizedArticleSchema)
        assert schema.title == "Docker Basics"
        assert schema.summary == "This is a detailed summary explaining docker basics containerization."
        assert len(schema.key_takeaways) == 3


# =====================================================================
# ObsidianVaultAdapter Tests
# =====================================================================

@pytest.fixture
def temp_vault_dir(tmp_path: Path) -> Path:
    """Fixture providing a temporary directory for Obsidian vault."""
    return tmp_path / "vault"

def test_obsidian_adapter_init(temp_vault_dir: Path) -> None:
    """Verify that ObsidianVaultAdapter creates structural folders."""
    # Step 1: Instantiate adapter
    adapter = ObsidianVaultAdapter(temp_vault_dir)
    
    # Step 2: Assert directories exist
    assert temp_vault_dir.exists()
    assert (temp_vault_dir / "00-Raw").exists()
    assert (temp_vault_dir / "10-Wiki").exists()

def test_obsidian_adapter_save_raw_note(temp_vault_dir: Path) -> None:
    """Verify that save_raw_note writes Markdown note with YAML frontmatter."""
    # Step 1: Initialize adapter
    adapter = ObsidianVaultAdapter(temp_vault_dir)
    metadata = NoteMetadata(
        source_url="https://youtube.com/watch?v=123",
        channel_name="Tech Channel",
        published_at=datetime(2026, 5, 20, tzinfo=timezone.utc),
        processed_at=datetime(2026, 5, 21, tzinfo=timezone.utc)
    )
    raw_note = RawNote(
        content_id=ContentId.generate(),
        title="Docker Basics",
        transcript_text="Raw transcript data",
        metadata=metadata
    )

    # Step 2: Execute save_raw_note
    file_path = adapter.save_raw_note(raw_note)

    # Step 3: Assert file was created and matches correct path
    expected_path = temp_vault_dir / "00-Raw" / "Docker Basics.md"
    assert file_path == expected_path
    assert file_path.exists()

    # Step 4: Parse the file content to verify frontmatter structure
    content = file_path.read_text(encoding="utf-8")
    assert content.startswith("---")
    
    # Split frontmatter and body
    parts = content.split("---")
    assert len(parts) >= 3
    parsed_frontmatter = yaml.safe_load(parts[1])
    
    # Assert values in frontmatter
    assert parsed_frontmatter["source_url"] == "https://youtube.com/watch?v=123"
    assert parsed_frontmatter["channel_name"] == "Tech Channel"
    assert parsed_frontmatter["published_at"] == "2026-05-20T00:00:00+00:00"
    
    # Assert note content in body
    assert parts[2].strip() == "Raw transcript data"

def test_obsidian_adapter_save_wiki_article(temp_vault_dir: Path) -> None:
    """Verify that save_wiki_article writes structured markdown file with backlinks."""
    # Step 1: Initialize adapter
    adapter = ObsidianVaultAdapter(temp_vault_dir)
    article = WikiArticle(
        article_id=ContentId.generate(),
        title="Clean Architecture",
        content="Detailed markdown body here.",
        tags=["architecture", "ddd"],
        backlinks=["[[Hexagonal Architecture]]", "[[Domain Driven Design]]"],
        source_notes=[ContentId.generate()],
        last_updated=datetime(2026, 5, 21, tzinfo=timezone.utc)
    )

    # Step 2: Execute save_wiki_article
    file_path = adapter.save_wiki_article(article)

    # Step 3: Assert file exists at expected location
    expected_path = temp_vault_dir / "10-Wiki" / "Clean Architecture.md"
    assert file_path == expected_path
    assert file_path.exists()

    # Step 4: Parse file content
    file_content = file_path.read_text(encoding="utf-8")
    assert "title: Clean Architecture" in file_content
    assert "- [[Hexagonal Architecture]]" in file_content
    assert "- [[Domain Driven Design]]" in file_content
    assert "Detailed markdown body here." in file_content

def test_obsidian_adapter_list_and_find(temp_vault_dir: Path) -> None:
    """Verify that list_wiki_articles and find_wiki_article_by_title read files correctly."""
    # Step 1: Initialize adapter
    adapter = ObsidianVaultAdapter(temp_vault_dir)
    
    # Step 2: Create mock files directly in the filesystem
    wiki_dir = temp_vault_dir / "10-Wiki"
    
    # File 1
    file_1_content = """---
title: Topic 1
article_id: aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
tags:
- tag1
backlinks:
- [[Topic 2]]
source_notes:
- aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa
last_updated: "2026-05-21T00:00:00+00:00"
---

Main Body 1
"""
    (wiki_dir / "Topic 1.md").write_text(file_1_content, encoding="utf-8")

    # File 2
    file_2_content = """---
title: Topic 2
article_id: 11111111-2222-3333-4444-555555555555
tags:
- tag2
backlinks: []
source_notes: []
last_updated: "2026-05-21T00:00:00+00:00"
---

Main Body 2
"""
    (wiki_dir / "Topic 2.md").write_text(file_2_content, encoding="utf-8")

    # Step 3: Run list_wiki_articles and assert loaded articles list
    articles = adapter.list_wiki_articles()
    assert len(articles) == 2
    titles = [art.title for art in articles]
    assert "Topic 1" in titles
    assert "Topic 2" in titles

    # Verify attributes of File 1
    art_1 = next(art for art in articles if art.title == "Topic 1")
    assert str(art_1.article_id) == "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
    assert art_1.tags == ["tag1"]
    assert art_1.backlinks == ["[[Topic 2]]"]
    assert [str(sn) for sn in art_1.source_notes] == ["aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"]
    assert art_1.content == "Main Body 1"

    # Step 4: Run find_wiki_article_by_title
    found = adapter.find_wiki_article_by_title("Topic 2")
    assert found is not None
    assert found.title == "Topic 2"
    assert str(found.article_id) == "11111111-2222-3333-4444-555555555555"
    assert found.tags == ["tag2"]
    assert found.content == "Main Body 2"

    # Step 5: Test find with non-existent title
    assert adapter.find_wiki_article_by_title("Missing Topic") is None
