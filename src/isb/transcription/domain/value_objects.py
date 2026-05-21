from dataclasses import dataclass

@dataclass(frozen=True)
class Segment:
    """Immutable Value Object representing a single timestamped segment of parsed speech.

    Maintains integrity rules governing audio segment boundaries and confidence metrics.
    """
    start_seconds: float
    end_seconds: float
    text: str
    confidence: float

    def __post_init__(self) -> None:
        """Validate structural integrity constraints on initialization.

        Raises:
            ValueError: If start/end times are negative, if start occurs after end,
                        or if confidence is outside the [0.0, 1.0] range.
        """
        # Step 1: Validate timestamp negativity domain invariant
        # Timestamps representing location in audio stream cannot be negative
        if self.start_seconds < 0.0 or self.end_seconds < 0.0:
            raise ValueError("start_seconds and end_seconds cannot be negative")
            
        # Step 2: Validate chronological ordering domain invariant
        # The beginning of a speech segment cannot occur after its end
        if self.start_seconds > self.end_seconds:
            raise ValueError("start_seconds cannot be after end_seconds")
            
        # Step 3: Validate confidence value constraints
        # Model confidence percentage must fall within standard mathematical probability range
        if not (0.0 <= self.confidence <= 1.0):
            raise ValueError("confidence must be between 0.0 and 1.0")
