from abc import ABC, abstractmethod
from pathlib import Path
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.knowledge.domain.entities import RawNote, WikiArticle
from isb.knowledge.domain.value_objects import SynthesizedArticleSchema, NoteTitle

class LLMPort(ABC):
    """Port interface for interacting with the Local LLM (qwen2.5:7b via Ollama).

    Decouples application synthesis logic from Ollama API or external network client libraries.
    """

    @abstractmethod
    def synthesize_wiki(self, raw_note: RawNote, existing_articles: list[WikiArticle]) -> SynthesizedArticleSchema:
        """Analyze the raw note and existing wiki articles, returning a strictly-conforming Pydantic schema.

        Args:
            raw_note: The raw transcript note to be synthesized.
            existing_articles: List of current articles in the vault to support context/cross-linking.

        Returns:
            SynthesizedArticleSchema: Structured Pydantic representation of the synthesized article.
        """
        pass


class VaultPort(ABC):
    """Port interface for interacting with files in the Obsidian Vault repository (Humble interface).

    Provides database/file-system abstraction for writing and reading markdown notes.
    """

    @abstractmethod
    def save_raw_note(self, note: RawNote) -> Path:
        """Write the RawNote to the Vault under raw/ folder, returning its Path.

        Args:
            note: The RawNote entity to save.

        Returns:
            Path: Absolute/relative file system Path to the saved raw note.
        """
        pass

    @abstractmethod
    def save_wiki_article(self, article: WikiArticle) -> Path:
        """Write the WikiArticle to the Vault under wiki/ folder, returning its Path.

        Args:
            article: The WikiArticle entity to save.

        Returns:
            Path: Absolute/relative file system Path to the saved wiki article.
        """
        pass

    @abstractmethod
    def list_wiki_articles(self) -> list[WikiArticle]:
        """Load and return all existing synthesized wiki articles from the vault.

        Returns:
            list[WikiArticle]: List of existing WikiArticle entities.
        """
        pass

    @abstractmethod
    def find_wiki_article_by_title(self, title: NoteTitle) -> WikiArticle | None:
        """Find a single synthesized wiki article matching the given title.

        Args:
            title: The title name of the target article.

        Returns:
            WikiArticle | None: The found WikiArticle entity or None.
        """
        pass


class KnowledgeManifestPort(ABC):
    """Port interface for updating processing status for the knowledge context.

    Abstracts status tracking storage dependencies from synthesis orchestrations.
    """

    @abstractmethod
    def mark_status(self, content_id: ContentId, status: ProcessingStatus) -> None:
        """Update the processing status of the given ContentId.

        Args:
            content_id: Unique system ContentId.
            status: ProcessingStatus transition state.
        """
        pass
