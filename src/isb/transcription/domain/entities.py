from pydantic import BaseModel, ConfigDict, Field, BeforeValidator
from typing import Annotated
from isb.shared_kernel.types import ContentId
from isb.transcription.domain.value_objects import (
    Segment,
    LanguageCode,
    ModelName,
    TranscriptText,
)

class Transcript(BaseModel):
    """Domain Entity representing the parsed audio transcription result from Whisper.

    Tracks duration, language, and the individual timestamped text segments
    extracted by the speech-to-text model.
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)

    content_id: ContentId
    full_text: Annotated[TranscriptText, BeforeValidator(lambda v: TranscriptText(v) if isinstance(v, str) else v)]
    segments: list[Segment] = Field(default_factory=list)
    language: Annotated[LanguageCode, BeforeValidator(lambda v: LanguageCode(v) if isinstance(v, str) else v)] = Field(default_factory=lambda: LanguageCode("pt"))
    model: Annotated[ModelName, BeforeValidator(lambda v: ModelName(v) if isinstance(v, str) else v)] = Field(default_factory=lambda: ModelName("base"))
    duration_seconds: float = 0.0

    def word_count(self) -> int:
        """Return total number of words in this transcript.

        Returns:
            int: The calculated number of white-space separated word tokens.
        """
        cleaned = self.full_text.value.strip()
        if not cleaned:
            return 0
        return len(cleaned.split())

    def has_segments(self) -> bool:
        """Return True if transcript contains timestamped segments.

        Returns:
            bool: True if there is at least one segment entry, False otherwise.
        """
        return len(self.segments) > 0
