from pathlib import Path
from dataclasses import dataclass
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
