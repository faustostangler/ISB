from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class AudioTrack:
    """Immutable Value Object representing an extracted audio file on disk."""
    file_path: Path
    file_format: str
    size_bytes: int
    duration_seconds: int

    def __post_init__(self) -> None:
        if not isinstance(self.file_path, Path):
            raise TypeError("file_path must be a Path instance")
        if self.size_bytes < 0:
            raise ValueError("size_bytes cannot be negative")
        if self.duration_seconds < 0:
            raise ValueError("duration_seconds cannot be negative")
