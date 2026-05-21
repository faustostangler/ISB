from abc import ABC, abstractmethod
from pathlib import Path
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.knowledge.domain.entities import RawNote, WikiArticle
from isb.knowledge.domain.value_objects import SynthesizedArticleSchema

class LLMPort(ABC):
    """Port interface for interacting with the Local LLM (qwen2.5:7b via Ollama)."""

    @abstractmethod
    def synthesize_wiki(self, raw_note: RawNote, existing_articles: list[WikiArticle]) -> SynthesizedArticleSchema:
        """Analyze the raw note and existing wiki articles, returning a strictly-conforming Pydantic schema."""
        pass


class VaultPort(ABC):
    """Port interface for interacting with files in the Obsidian Vault repository (Humble interface)."""

    @abstractmethod
    def save_raw_note(self, note: RawNote) -> Path:
        """Write the RawNote to the Vault under raw/ folder, returning its Path."""
        pass

    @abstractmethod
    def save_wiki_article(self, article: WikiArticle) -> Path:
        """Write the WikiArticle to the Vault under wiki/ folder, returning its Path."""
        pass

    @abstractmethod
    def list_wiki_articles(self) -> list[WikiArticle]:
        """Load and return all existing synthesized wiki articles from the vault."""
        pass

    @abstractmethod
    def find_wiki_article_by_title(self, title: str) -> WikiArticle | None:
        """Find a single synthesized wiki article matching the given title."""
        pass


class KnowledgeManifestPort(ABC):
    """Port interface for updating processing status for the knowledge context."""

    @abstractmethod
    def mark_status(self, content_id: ContentId, status: ProcessingStatus) -> None:
        """Update the processing status of the given ContentId."""
        pass
