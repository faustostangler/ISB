from pathlib import Path
from dataclasses import dataclass
from datetime import datetime

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


@dataclass(frozen=True)
class ExternalId:
    """Value Object representing a platform-specific external identifier."""
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError("ExternalId value must be a string")
        if not self.value.strip():
            raise ValueError("ExternalId value cannot be empty or whitespace")

    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True)
class EpisodeTitle:
    """Value Object representing a media episode's title."""
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError("EpisodeTitle value must be a string")
        if not self.value.strip():
            raise ValueError("EpisodeTitle value cannot be empty or whitespace")

    def __str__(self) -> str:
        return self.value.strip()


@dataclass(frozen=True)
class DurationSeconds:
    """Value Object representing a duration in seconds."""
    value: int

    def __post_init__(self) -> None:
        if not isinstance(self.value, int):
            raise TypeError("DurationSeconds value must be an integer")
        if self.value < 0:
            raise ValueError("DurationSeconds value cannot be negative")

    def __int__(self) -> int:
        return self.value


@dataclass(frozen=True)
class PublishedAt:
    """Value Object representing a timezone-aware UTC publication datetime."""
    value: datetime

    def __post_init__(self) -> None:
        if not isinstance(self.value, datetime):
            raise TypeError("PublishedAt value must be a datetime instance")
        if self.value.tzinfo is None or self.value.tzinfo.utcoffset(self.value) is None:
            raise ValueError("PublishedAt value must be timezone-aware UTC datetime")

    def to_iso(self) -> str:
        return self.value.isoformat()


@dataclass(frozen=True)
class SourceId:
    """Value Object representing a media source's unique identifier."""
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError("SourceId value must be a string")
        if not self.value.strip():
            raise ValueError("SourceId value cannot be empty or whitespace")

    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True)
class SourceName:
    """Value Object representing a media source's name."""
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError("SourceName value must be a string")
        if not self.value.strip():
            raise ValueError("SourceName value cannot be empty or whitespace")

    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True)
class SourceUrl:
    """Value Object representing a media source's extraction URL."""
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError("SourceUrl value must be a string")
        if not (self.value.startswith("http://") or self.value.startswith("https://")):
            raise ValueError("SourceUrl value must start with http:// or https://")

    def __str__(self) -> str:
        return self.value
