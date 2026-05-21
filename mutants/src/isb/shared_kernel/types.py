import uuid
from enum import Enum
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
