from dataclasses import dataclass, field
from isb.shared_kernel.types import ContentId
from isb.transcription.domain.value_objects import Segment

@dataclass
class Transcript:
    """Domain Entity representing the parsed audio transcription result from Whisper."""
    content_id: ContentId
    full_text: str
    segments: list[Segment] = field(default_factory=list)
    language: str = "pt"
    model: str = "base"
    duration_seconds: float = 0.0

    def word_count(self) -> int:
        """Return total number of words in this transcript."""
        cleaned = self.full_text.strip()
        if not cleaned:
            return 0
        return len(cleaned.split())

    def has_segments(self) -> bool:
        """Return True if transcript contains timestamped segments."""
        return len(self.segments) > 0
