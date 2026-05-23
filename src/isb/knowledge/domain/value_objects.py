import re
from datetime import datetime
from pydantic import BaseModel, Field, field_validator
from dataclasses import dataclass

class NoteMetadata(BaseModel):
    """Pydantic model representing immutable frontmatter metadata for RawNotes.

    Enforces validation schema layout matching target Obsidian YAML structures.
    """
    source_url: str = Field(description="URL of the original media source")
    channel_name: str = Field(description="Name of the channel or creator")
    published_at: datetime = Field(description="Original media publication datetime")
    processed_at: datetime = Field(description="Datetime when this note was processed")
    category: str = Field(default="uncategorized", description="Subject classification category")
    tags: list[str] = Field(default_factory=list, description="Associated metadata tags")


class SynthesizedArticleSchema(BaseModel):
    """Pydantic V2 schema defining the strict rules/format for LLM-synthesized WikiArticles.

    Enforces Karpathy-style structured output format for the LLM synthesis adapter,
    ensuring consistent generation of summaries, key takeaways, and cross-linking topics.
    """
    title: str = Field(..., min_length=3, description="Unique, descriptive title of the article")
    summary: str = Field(..., min_length=10, description="A concise summary of the article topic")
    key_takeaways: list[str] = Field(..., min_length=3, max_length=10, description="Key bulleted takeaways or core facts")
    content: str = Field(..., min_length=50, description="Main synthesized Markdown body, with links to related topics")
    tags: list[str] = Field(..., description="Curated tags matching taxonomy rules")
    related_topics: list[str] = Field(..., description="List of related article titles for cross-linking")

    @field_validator("title", mode="before")
    @classmethod
    def sanitize_title(cls, v: str) -> str:
        """Sanitizes the article title by replacing illegal filesystem characters with space,

        collapsing multiple whitespace characters, and trimming the ends.
        """
        # Step 1: Check type before executing string manipulations.
        if not isinstance(v, str):
            return v
        
        # Step 2: Replace illegal characters \ / : * ? " < > | with spaces.
        # This prevents invalid filename creation under ObsidianVaultAdapter.
        sanitized = re.sub(r'[\\/:*?"<>|]', " ", v)
        
        # Step 3: Collapse whitespace groups and strip padding.
        return " ".join(sanitized.split())

    @field_validator("tags", mode="before")
    @classmethod
    def normalize_tags(cls, v: list[str]) -> list[str]:
        """Normalizes tags by converting to lowercase, keeping only alphanumeric characters,

        and filtering out empty resulting tags.
        """
        # Step 1: Check type before executing list loops.
        if not isinstance(v, list):
            return v
        
        normalized = []
        for tag in v:
            # Step 2: Filter elements to ensure they are string inputs.
            if not isinstance(tag, str):
                continue
            
            # Step 3: Clean tag: extract only alphanumeric chars, lowercase it.
            cleaned = "".join(c.lower() for c in tag if c.isalnum())
            
            # Step 4: Discard empty tags resulting from blank spaces or punctuation only.
            if cleaned:
                normalized.append(cleaned)
                
        return normalized


@dataclass(frozen=True)
class NoteTitle:
    """Value Object representing a raw note's sanitized title."""
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError("NoteTitle value must be a string")
        if not self.value.strip():
            raise ValueError("NoteTitle cannot be empty or whitespace")
        # Ensure it has filesystem safe characters
        sanitized = re.sub(r'[\\/:*?"<>|]', " ", self.value)
        if not sanitized.strip():
            raise ValueError("NoteTitle contains only illegal characters")

    def __str__(self) -> str:
        sanitized = re.sub(r'[\\/:*?"<>|]', " ", self.value)
        return " ".join(sanitized.split())


@dataclass(frozen=True)
class ArticleContent:
    """Value Object representing the synthesized wiki article's markdown content."""
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError("ArticleContent value must be a string")
        if len(self.value.strip()) < 10:
            raise ValueError("ArticleContent must be at least 10 characters long")

    def __str__(self) -> str:
        return self.value.strip()


@dataclass(frozen=True)
class ArticleTag:
    """Value Object representing a normalized tag in the wiki article."""
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError("ArticleTag value must be a string")
        cleaned = "".join(c.lower() for c in self.value if c.isalnum())
        if not cleaned:
            raise ValueError("ArticleTag must contain alphanumeric characters")

    def __str__(self) -> str:
        return "".join(c.lower() for c in self.value if c.isalnum())


@dataclass(frozen=True)
class ArticleBacklink:
    """Value Object representing an Obsidian style wiki cross-link."""
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError("ArticleBacklink value must be a string")
        if not (self.value.startswith("[[") and self.value.endswith("]]")):
            raise ValueError("ArticleBacklink must start with '[[' and end with ']]'")
        # Ensure content inside link is not empty
        link_content = self.value[2:-2].strip()
        if not link_content:
            raise ValueError("ArticleBacklink target cannot be empty")

    def __str__(self) -> str:
        return self.value.strip()
