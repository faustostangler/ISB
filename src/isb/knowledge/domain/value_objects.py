from datetime import datetime
from pydantic import BaseModel, Field

class NoteMetadata(BaseModel):
    """Pydantic model representing immutable frontmatter metadata for RawNotes."""
    source_url: str = Field(description="URL of the original media source")
    channel_name: str = Field(description="Name of the channel or creator")
    published_at: datetime = Field(description="Original media publication datetime")
    processed_at: datetime = Field(description="Datetime when this note was parsed")
    category: str = Field(default="uncategorized", description="Subject classification category")
    tags: list[str] = Field(default_factory=list, description="Associated metadata tags")


class SynthesizedArticleSchema(BaseModel):
    """Pydantic V2 schema defining the strict rules/format for LLM-synthesized WikiArticles.

    Enforces Karpathy LLM Wiki structure in the Schema Layer.
    """
    title: str = Field(..., description="Unique, descriptive title of the article")
    summary: str = Field(..., description="A concise summary of the article topic")
    key_takeaways: list[str] = Field(..., description="Key bulleted takeaways or core facts")
    content: str = Field(..., description="Main synthesized Markdown body, with links to related topics")
    tags: list[str] = Field(..., description="Curated tags matching taxonomy rules")
    related_topics: list[str] = Field(..., description="List of related article titles for cross-linking")
