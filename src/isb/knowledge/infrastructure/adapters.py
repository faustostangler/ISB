import json
import httpx
import yaml
from pathlib import Path
from datetime import datetime, timezone
from isb.shared_kernel.types import ContentId
from isb.knowledge.domain.entities import RawNote, WikiArticle
from isb.knowledge.domain.value_objects import SynthesizedArticleSchema
from isb.knowledge.application.ports import LLMPort, VaultPort

class OllamaLLMAdapter(LLMPort):
    """Infrastructure adapter implementing the LLMPort using the local Ollama HTTP API.

    This adapter manages requests to a locally hosted large language model instance
    via HTTP, requesting JSON-formatted structured outputs that represent synthesized
    wiki articles.

    Attributes:
        base_url: The base HTTP URL of the local Ollama API endpoint.
        model_name: The name/tag of the target model loaded in Ollama.
        client: The HTTP client used to perform synchronous HTTP API requests.
    """

    def __init__(self, base_url: str, model_name: str = "qwen2.5:7b") -> None:
        """Initializes the Ollama LLM adapter.

        Args:
            base_url: Base URL of the Ollama server endpoint.
            model_name: Name of the LLM to run. Defaults to "qwen2.5:7b".
        """
        self.base_url = base_url
        self.model_name = model_name
        
        # Infrastructure limit: Instantiate a synchronous HTTP client with a 60-second timeout.
        # Generating structured JSON responses from large models locally can take significant time
        # depending on GPU availability and resource saturation.
        self.client = httpx.Client(timeout=60.0)

    def synthesize_wiki(self, raw_note: RawNote, existing_articles: list[WikiArticle]) -> SynthesizedArticleSchema:
        """Analyzes a raw note and existing wiki titles to synthesize a structured wiki article.

        Formats the input context, requests the local Ollama service using JSON format constraints,
        and parses the response into a validated Pydantic schema model.

        Args:
            raw_note: The RawNote entity containing the transcription content.
            existing_articles: A list of existing WikiArticle entities used for reference and link mapping.

        Returns:
            A SynthesizedArticleSchema containing structured key takeaways, main content,
            and related topics.

        Raises:
            httpx.HTTPStatusError: If the Ollama server returns an error response.
            json.JSONDecodeError: If the server response cannot be decoded as valid JSON.
        """
        existing_titles = ", ".join(f'"{art.title}"' for art in existing_articles)
        
        # Infrastructure limit: Prompt contains strict formatting instructions to enforce the
        # Karpathy wiki style (linking to existing articles, bullet points, headers).
        prompt = (
            f"Analyze the following raw note from channel '{raw_note.metadata.channel_name}' "
            f"originally published at {raw_note.metadata.published_at.isoformat()} and source URL {raw_note.metadata.source_url}.\n"
            f"Note Title: {raw_note.title}\n"
            f"Note Content:\n{raw_note.transcript_text}\n\n"
            f"Available existing wiki article titles for cross-linking: {existing_titles}\n\n"
            f"Synthesize this note into a high-quality Wiki Article. "
            f"Provide output in strict JSON matching this schema:\n"
            f"{SynthesizedArticleSchema.model_json_schema()}"
        )
        
        # Infrastructure limit: Force Ollama to output valid JSON by specifying format="json".
        # This reduces schema violation rates and allows direct serialization into Pydantic models.
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "format": "json",
            "stream": False
        }
        
        response = self.client.post(f"{self.base_url}/api/generate", json=payload)
        response.raise_for_status()
        
        response_data = response.json()
        response_text = response_data.get("response", "")
        parsed_json = json.loads(response_text)
        
        # Ingestion Boundary: Map raw dictionary data into the strict domain-driven Pydantic schema model.
        return SynthesizedArticleSchema(**parsed_json)


class ObsidianVaultAdapter(VaultPort):
    """Infrastructure adapter implementing VaultPort for local Obsidian storage.

    Manages the filesystem layout of the Obsidian vault under structured subdirectory names:
    '00-Raw/' for raw transcript captures, and '10-Wiki/' for synthesized wiki articles.

    Attributes:
        vault_path: Path to the root directory of the target Obsidian Vault.
        raw_dir: Path to the directory where raw notes are saved.
        wiki_dir: Path to the directory where wiki articles are saved.
    """

    def __init__(self, vault_path: str | Path) -> None:
        """Initializes the Obsidian vault adapter.

        Args:
            vault_path: Local directory path representing the Obsidian vault root.
        """
        # Infrastructure limit: Separate directories are hardcoded to establish an organized structure
        # within the Obsidian vault, matching the Knowledge context boundaries.
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
        # Infrastructure limit: Sanitize or structure the filename using the note's title to avoid
        # invalid character issues on standard file systems.
        file_path = self.raw_dir / f"{note.title}.md"
        
        frontmatter = {
            "source_url": note.metadata.source_url,
            "channel_name": note.metadata.channel_name,
            "published_at": note.metadata.published_at.isoformat(),
            "processed_at": note.metadata.processed_at.isoformat(),
            "category": note.metadata.category,
            "tags": note.metadata.tags,
        }
        yaml_block = yaml.safe_dump(frontmatter, sort_keys=False)
        
        # Infrastructure limit: Frontmatter block is written at the top using standard Markdown delimiters (---)
        # to ensure metadata properties are recognized by Obsidian and other static-site generators.
        file_content = f"---\n{yaml_block}---\n\n{note.transcript_text}"
        file_path.write_text(file_content, encoding="utf-8")
        
        return file_path

    def save_wiki_article(self, article: WikiArticle) -> Path:
        """Saves a synthesized wiki article to the vault with YAML frontmatter and cross-links.

        Args:
            article: The WikiArticle entity to be persisted.

        Returns:
            The absolute Path to the newly created markdown file in the filesystem.
        """
        file_path = self.wiki_dir / f"{article.title}.md"
        
        # Infrastructure limit: Frontmatter block is written at the top using standard Markdown delimiters (---)
        # to ensure metadata properties are recognized by Obsidian and other static-site generators.
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
        
        # Infrastructure limit: Read all markdown files sequentially in the 10-Wiki folder.
        # For very large vaults, this should be paginated or indexed via SQLite.
        for file_path in self.wiki_dir.glob("*.md"):
            content = file_path.read_text(encoding="utf-8")
            if not content.startswith("---"):
                continue
            
            # Infrastructure limit: Extract frontmatter block using YAML metadata delimiters.
            parts = content.split("---")
            if len(parts) < 3:
                continue
            
            front = yaml.safe_load(parts[1])
            main_content = parts[2].strip()
            
            # Anti-Corruption Layer (ACL): Translate infrastructure-level markdown properties
            # into a pure domain-driven WikiArticle entity with ContentId and timezone-aware timestamps.
            article = WikiArticle(
                article_id=ContentId.from_str(front["article_id"]),
                title=file_path.stem,
                content=main_content,
                tags=front.get("tags") or [],
                backlinks=front.get("backlinks") or [],
                source_notes=[ContentId.from_str(nid) for nid in front.get("source_notes", [])],
                last_updated=datetime.fromisoformat(front["last_updated"])
            )
            articles.append(article)
            
        return articles

    def find_wiki_article_by_title(self, title: str) -> WikiArticle | None:
        """Finds a single synthesized wiki article matching the given title.

        Args:
            title: The title of the article to retrieve.

        Returns:
            The matched WikiArticle entity, or None if the file does not exist.
        """
        # Exception handling: Return None if the requested page is missing, allowing callers
        # to decide if a new synthesis run is required.
        file_path = self.wiki_dir / f"{title}.md"
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
            title=file_path.stem,
            content=main_content,
            tags=front.get("tags") or [],
            backlinks=front.get("backlinks") or [],
            source_notes=[ContentId.from_str(nid) for nid in front.get("source_notes", [])],
            last_updated=datetime.fromisoformat(front["last_updated"])
        )
