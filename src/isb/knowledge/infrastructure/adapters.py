import json
import httpx
import yaml
import logging
from pathlib import Path
from datetime import datetime, timezone
from isb.shared_kernel.types import ContentId
from isb.knowledge.domain.entities import RawNote, WikiArticle
from isb.transcription.domain.value_objects import TranscriptText
from isb.knowledge.domain.value_objects import (
    SynthesizedArticleSchema,
    NoteTitle,
    ArticleContent,
    ArticleTag,
    ArticleBacklink,
)
from isb.knowledge.application.ports import LLMPort, VaultPort

logger = logging.getLogger(__name__)

class OllamaLLMAdapter(LLMPort):
    """Infrastructure adapter implementing the LLMPort using the local Ollama HTTP API.

    This adapter manages requests to a locally hosted large language model instance
    via HTTP, requesting JSON-formatted structured outputs that represent synthesized
    wiki articles.
    """

    def __init__(
        self,
        base_url: str,
        model_name: str = "qwen2.5:7b",
        langfuse_public_key: str | None = None,
        langfuse_secret_key: str | None = None,
        langfuse_host: str = "https://cloud.langfuse.com"
    ) -> None:
        """Initializes the Ollama LLM adapter.

        Args:
            base_url: Base URL of the Ollama server endpoint.
            model_name: Name of the LLM to run. Defaults to "qwen2.5:7b".
            langfuse_public_key: Public key for Langfuse tracing.
            langfuse_secret_key: Secret key for Langfuse tracing.
            langfuse_host: Host endpoint for Langfuse API.
        """
        self.base_url = base_url
        self.model_name = model_name
        self.client = httpx.Client(timeout=60.0)
        
        # Initialize Langfuse client if API keys are provided
        if langfuse_public_key and langfuse_secret_key:
            try:
                from langfuse import Langfuse
                self.langfuse = Langfuse(
                    public_key=langfuse_public_key,
                    secret_key=langfuse_secret_key,
                    host=langfuse_host
                )
                logger.info("Langfuse LLM tracing initialized successfully.")
            except ImportError:
                logger.warning("Langfuse package is not installed. LLM tracing disabled.")
                self.langfuse = None
            except Exception as e:
                logger.exception("Failed to initialize Langfuse client: %s", e)
                self.langfuse = None
        else:
            self.langfuse = None

    def synthesize_wiki(self, raw_note: RawNote, existing_articles: list[WikiArticle]) -> SynthesizedArticleSchema:
        """Analyzes a raw note and existing wiki titles to synthesize a structured wiki article.

        Formats the input context, requests the local Ollama service using JSON format constraints,
        and parses the response into a validated Pydantic schema model.
        """
        existing_titles = ", ".join(f'"{str(art.title)}"' for art in existing_articles)
        
        # Construct LLM prompt using domain-extracted string values
        prompt = (
            f"Analyze the following raw note from channel '{raw_note.metadata.channel_name}' "
            f"originally published at {raw_note.metadata.published_at.isoformat()} and source URL {raw_note.metadata.source_url}.\n"
            f"Note Title: {str(raw_note.title)}\n"
            f"Note Content:\n{raw_note.transcript_text.value}\n\n"
            f"Available existing wiki article titles for cross-linking: {existing_titles}\n\n"
            f"Synthesize this note into a high-quality Wiki Article. "
            f"Provide output in strict JSON matching this schema:\n"
            f"{SynthesizedArticleSchema.model_json_schema()}"
        )
        
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "format": "json",
            "stream": False
        }
        
        # Start Langfuse generation span if active
        trace = None
        generation = None
        if self.langfuse:
            try:
                trace = self.langfuse.trace(
                    name="WikiSynthesis",
                    session_id=str(raw_note.content_id),
                    metadata={
                        "title": str(raw_note.title),
                        "channel_name": raw_note.metadata.channel_name,
                        "published_at": raw_note.metadata.published_at.isoformat()
                    }
                )
                generation = trace.generation(
                    name="OllamaSynthesisGeneration",
                    model=self.model_name,
                    input=prompt
                )
            except Exception as e:
                logger.warning("Failed to start Langfuse trace: %s", e)

        try:
            response = self.client.post(f"{self.base_url}/api/generate", json=payload)
            response.raise_for_status()
            
            response_data = response.json()
            response_text = response_data.get("response", "")
            
            # End Langfuse generation span successfully
            if generation:
                try:
                    generation.end(output=response_text)
                except Exception as e:
                    logger.warning("Failed to end Langfuse generation: %s", e)
            
            parsed_json = json.loads(response_text)
            return SynthesizedArticleSchema(**parsed_json)

        except Exception as err:
            # End Langfuse generation span with error status
            if generation:
                try:
                    generation.end(level="ERROR", status_message=str(err))
                except Exception as e:
                    logger.warning("Failed to log error generation in Langfuse: %s", e)
            raise
 

class ObsidianVaultAdapter(VaultPort):
    """Infrastructure adapter implementing VaultPort for local Obsidian storage.

    Manages the filesystem layout of the Obsidian vault under structured subdirectory names:
    '00-Raw/' for raw transcript captures, and '10-Wiki/' for synthesized wiki articles.
    """

    def __init__(self, vault_path: str | Path) -> None:
        """Initializes the Obsidian vault adapter.

        Args:
            vault_path: Local directory path representing the Obsidian vault root.
        """
        self.vault_path = Path(vault_path)
        self.raw_dir = self.vault_path / "00-Raw"
        self.wiki_dir = self.vault_path / "10-Wiki"
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.wiki_dir.mkdir(parents=True, exist_ok=True)

    def save_raw_note(self, note: RawNote) -> Path:
        """Saves a raw note to the vault as a markdown file with YAML frontmatter.

        Args:
            note: The RawNote entity to be persisted.

        Returns:
            The absolute Path to the newly created markdown file in the filesystem.
        """
        file_path = self.raw_dir / f"{str(note.title)}.md"
        
        frontmatter = {
            "source_url": note.metadata.source_url,
            "channel_name": note.metadata.channel_name,
            "published_at": note.metadata.published_at.isoformat(),
            "processed_at": note.metadata.processed_at.isoformat(),
            "category": note.metadata.category,
            "tags": note.metadata.tags,
        }
        yaml_block = yaml.safe_dump(frontmatter, sort_keys=False)
        
        file_content = f"---\n{yaml_block}---\n\n{note.transcript_text.value}"
        file_path.write_text(file_content, encoding="utf-8")
        
        return file_path

    def save_wiki_article(self, article: WikiArticle) -> Path:
        """Saves a synthesized wiki article to the vault with YAML frontmatter and cross-links.

        Args:
            article: The WikiArticle entity to be persisted.

        Returns:
            The absolute Path to the newly created markdown file in the filesystem.
        """
        file_path = self.wiki_dir / f"{str(article.title)}.md"
        file_content = article.to_obsidian_markdown()
        file_path.write_text(file_content, encoding="utf-8")
        
        return file_path

    def list_wiki_articles(self) -> list[WikiArticle]:
        """Loads and lists all synthesized wiki articles found in the vault.

        Iterates over markdown files, parses their frontmatter and markdown sections,
        and constructs domain-level WikiArticle entities.

        Returns:
            A list of reconstructed WikiArticle domain entities from the filesystem.
        """
        articles: list[WikiArticle] = []
        
        for file_path in self.wiki_dir.glob("*.md"):
            content = file_path.read_text(encoding="utf-8")
            if not content.startswith("---"):
                continue
            
            parts = content.split("---")
            if len(parts) < 3:
                continue
            
            front = yaml.safe_load(parts[1])
            main_content = parts[2].strip()
            
            # Anti-Corruption Layer (ACL): Translate infrastructure-level markdown properties
            # into a pure domain-driven WikiArticle entity with ContentId and timezone-aware timestamps.
            article = WikiArticle(
                article_id=ContentId.from_str(front["article_id"]),
                title=NoteTitle(file_path.stem),
                content=ArticleContent(main_content),
                tags=[ArticleTag(t) for t in front.get("tags") or []],
                backlinks=[ArticleBacklink(b) for b in front.get("backlinks") or []],
                source_notes=[ContentId.from_str(nid) for nid in front.get("source_notes", [])],
                last_updated=datetime.fromisoformat(front["last_updated"])
            )
            articles.append(article)
            
        return articles

    def find_wiki_article_by_title(self, title: NoteTitle) -> WikiArticle | None:
        """Finds a single synthesized wiki article matching the given title.

        Args:
            title: The title of the article to retrieve.

        Returns:
            The matched WikiArticle entity, or None if the file does not exist.
        """
        file_path = self.wiki_dir / f"{str(title)}.md"
        if not file_path.exists():
            return None
        
        content = file_path.read_text(encoding="utf-8")
        parts = content.split("---")
        if len(parts) < 3:
            return None
            
        front = yaml.safe_load(parts[1])
        main_content = parts[2].strip()
        
        # Anti-Corruption Layer (ACL): Translate infrastructure-level markdown properties
        # into a pure domain-driven WikiArticle entity.
        return WikiArticle(
            article_id=ContentId.from_str(front["article_id"]),
            title=NoteTitle(file_path.stem),
            content=ArticleContent(main_content),
            tags=[ArticleTag(t) for t in front.get("tags") or []],
            backlinks=[ArticleBacklink(b) for b in front.get("backlinks") or []],
            source_notes=[ContentId.from_str(nid) for nid in front.get("source_notes", [])],
            last_updated=datetime.fromisoformat(front["last_updated"])
        )
