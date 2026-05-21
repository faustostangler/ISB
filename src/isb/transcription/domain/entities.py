from dataclasses import dataclass, field
from isb.shared_kernel.types import ContentId
from isb.transcription.domain.value_objects import Segment

@dataclass
class Transcript:
    """Domain Entity representing the parsed audio transcription result from Whisper.

    Tracks duration, language, and the individual timestamped text segments
    extracted by the speech-to-text model.
    """
    content_id: ContentId
    full_text: str
    segments: list[Segment] = field(default_factory=list)
    language: str = "pt"
    model: str = "base"
    duration_seconds: float = 0.0

    def word_count(self) -> int:
        """Return total number of words in this transcript.

        Returns:
            int: The calculated number of white-space separated word tokens.
        """
        # Step 1: Clean surrounding whitespaces from full text
        cleaned = self.full_text.strip()
        # Step 2: Return 0 if transcript is empty
        if not cleaned:
            return 0
        # Step 3: Split cleaned string by whitespace and calculate length
        return len(cleaned.split())

    def has_segments(self) -> bool:
        """Return True if transcript contains timestamped segments.

        Returns:
            bool: True if there is at least one segment entry, False otherwise.
        """
        # Step 1: Evaluate the size of the segment list collection
        return len(self.segments) > 0
