import uuid
from enum import Enum
from dataclasses import dataclass

class ProcessingStatus(str, Enum):
    """Execution status for media processing pipeline items."""
    PENDING = "PENDING"
    EXTRACTING = "EXTRACTING"
    TRANSCRIBING = "TRANSCRIBING"
    SYNTHESIZING = "SYNTHESIZING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


@dataclass(frozen=True)
class ContentId:
    """Globally unique domain identifier for content units (MediaEpisode, RawNote, etc.).

    Decouples domain model from platform-specific IDs (e.g. YouTube video IDs)
    by wrapping a standard UUIDv4.
    """
    value: uuid.UUID

    def __post_init__(self) -> None:
        if not isinstance(self.value, uuid.UUID):
            raise TypeError("value must be a uuid.UUID instance")

    @classmethod
    def generate(cls) -> "ContentId":
        """Generate a new random ContentId using UUIDv4."""
        return cls(uuid.uuid4())

    @classmethod
    def from_str(cls, val: str) -> "ContentId":
        """Construct a ContentId from a UUID string, raising ValueError if invalid."""
        try:
            parsed = uuid.UUID(val)
            return cls(parsed)
        except (ValueError, AttributeError, TypeError) as err:
            raise ValueError(f"Invalid UUID format: {val}") from err

    def __str__(self) -> str:
        return str(self.value)
