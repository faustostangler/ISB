from dataclasses import dataclass

@dataclass(frozen=True)
class Segment:
    """Immutable Value Object representing a single timestamped segment of parsed speech."""
    start_seconds: float
    end_seconds: float
    text: str
    confidence: float

    def __post_init__(self) -> None:
        if self.start_seconds < 0.0 or self.end_seconds < 0.0:
            raise ValueError("start_seconds and end_seconds cannot be negative")
        if self.start_seconds > self.end_seconds:
            raise ValueError("start_seconds cannot be after end_seconds")
        if not (0.0 <= self.confidence <= 1.0):
            raise ValueError("confidence must be between 0.0 and 1.0")
