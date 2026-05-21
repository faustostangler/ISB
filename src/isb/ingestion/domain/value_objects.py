from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class AudioTrack:
    """Immutable Value Object representing an extracted audio file on disk.

    Enforces data integrity invariants post construction to ensure no corrupted
    or invalid metrics (negative duration, negative size) leak downstream.
    """
    file_path: Path
    file_format: str
    size_bytes: int
    duration_seconds: int

    def __post_init__(self) -> None:
        """Validate value object field invariants.

        Raises:
            TypeError: If the file_path is not a Path object.
            ValueError: If size_bytes or duration_seconds is negative.
        """
        # Step 1: Ensure path validation
        # We enforce type safety to prevent low-level I/O library crashes later
        if not isinstance(self.file_path, Path):
            raise TypeError("file_path must be a Path instance")
            
        # Step 2: Validate file size domain invariant
        # An audio track size cannot physically be negative
        if self.size_bytes < 0:
            raise ValueError("size_bytes cannot be negative")
            
        # Step 3: Validate duration domain invariant
        # An audio track duration cannot physically be negative
        if self.duration_seconds < 0:
            raise ValueError("duration_seconds cannot be negative")
