from datetime import datetime
from pydantic import BaseModel, Field
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
