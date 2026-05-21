from datetime import datetime, timezone
import yaml
from dataclasses import dataclass, field
from isb.shared_kernel.types import ContentId
from isb.knowledge.domain.value_objects import NoteMetadata
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore

@dataclass
class RawNote:
    """Domain Entity representing a verbatim source transcript note (Raw Layer).

    Encapsulates the raw transcript content and metadata frontmatter stored
    within the 00-Raw folder of the Obsidian Vault.
    """
    content_id: ContentId
    title: str
    transcript_text: str
    metadata: NoteMetadata

    def to_obsidian_markdown(self) -> str:
        """Serialize this raw note to an Obsidian-compatible Markdown file with YAML frontmatter.

        Returns:
            str: The fully formatted Markdown file string containing frontmatter and body.
        """
        # Step 1: Map object attributes to a standard dictionary format for frontmatter serialization
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
        
        # Step 2: Use pyyaml to dump the frontmatter block, enforcing Unicode characters
        # and preserving the logical key structure.
        yaml_str = yaml.dump(frontmatter, allow_unicode=True, sort_keys=False).strip()
        
        # Step 3: Combine YAML frontmatter with the note body content following Obsidian spec
        return f"---\n{yaml_str}\n---\n\n# {self.title}\n\n{self.transcript_text}\n"


@dataclass
class WikiArticle:
    """Domain Entity representing an LLM-synthesized second brain entry (Wiki Layer).

    Maintains links to raw source transcript notes and other related wiki topics.
    """
    article_id: ContentId
    title: str
    content: str
    tags: list[str] = field(default_factory=list)
    backlinks: list[str] = field(default_factory=list)
    source_notes: list[ContentId] = field(default_factory=list)
    last_updated: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_obsidian_markdown(self) -> str:
        """Serialize this wiki article to an Obsidian-compatible Markdown file with YAML frontmatter.

        Returns:
            str: The fully formatted Markdown file string containing frontmatter and body.
        """
        # Step 1: Map object attributes to a dictionary format for YAML frontmatter
        frontmatter = {
            "title": self.title,
            "article_id": str(self.article_id),
            "tags": self.tags,
            "backlinks": self.backlinks,
            "source_notes": [str(nid) for nid in self.source_notes],
            "last_updated": self.last_updated.isoformat()
        }
        
        # Step 2: Serialize frontmatter using YAML
        yaml_str = yaml.dump(frontmatter, allow_unicode=True, sort_keys=False).strip()
        
        # Step 3: Combine frontmatter with synthesized content
        return f"---\n{yaml_str}\n---\n\n{self.content}\n"
