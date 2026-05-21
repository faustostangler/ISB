from datetime import datetime, timezone
import yaml
from dataclasses import dataclass, field
from isb.shared_kernel.types import ContentId
from isb.knowledge.domain.value_objects import NoteMetadata

@dataclass
class RawNote:
    """Domain Entity representing a verbatim source transcript note (Raw Layer)."""
    content_id: ContentId
    title: str
    transcript_text: str
    metadata: NoteMetadata

    def to_obsidian_markdown(self) -> str:
        """Serialize this raw note to an Obsidian-compatible Markdown file with YAML frontmatter."""
        frontmatter = {
            "title": self.title,
            "content_id": str(self.content_id),
            "source_url": self.metadata.source_url,
            "channel_name": self.metadata.channel_name,
            "published_at": self.metadata.published_at.isoformat(),
            "processed_at": self.metadata.processed_at.isoformat(),
            "category": self.metadata.category,
            "tags": self.metadata.tags
        }
        
        yaml_str = yaml.dump(frontmatter, allow_unicode=True, sort_keys=False).strip()
        return f"---\n{yaml_str}\n---\n\n# {self.title}\n\n{self.transcript_text}\n"


@dataclass
class WikiArticle:
    """Domain Entity representing an LLM-synthesized second brain entry (Wiki Layer)."""
    article_id: ContentId
    title: str
    content: str
    tags: list[str] = field(default_factory=list)
    backlinks: list[str] = field(default_factory=list)
    source_notes: list[ContentId] = field(default_factory=list)
    last_updated: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_obsidian_markdown(self) -> str:
        """Serialize this wiki article to an Obsidian-compatible Markdown file with YAML frontmatter."""
        frontmatter = {
            "title": self.title,
            "article_id": str(self.article_id),
            "tags": self.tags,
            "backlinks": self.backlinks,
            "source_notes": [str(nid) for nid in self.source_notes],
            "last_updated": self.last_updated.isoformat()
        }
        
        yaml_str = yaml.dump(frontmatter, allow_unicode=True, sort_keys=False).strip()
        return f"---\n{yaml_str}\n---\n\n{self.content}\n"
