import re
from datetime import datetime
from pydantic import BaseModel, Field, field_validator

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

