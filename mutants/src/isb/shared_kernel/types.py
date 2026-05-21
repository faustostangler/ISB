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
    """Execution status for media processing pipeline items.

    Tracks the business lifecycle of a media episode through its lifecycle states:
    PENDING -> EXTRACTING -> TRANSCRIBING -> SYNTHESIZING -> COMPLETED/FAILED.
    """
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
    by wrapping a standard UUIDv4. This prevents external system modifications or ID
    formats from leaking into the core system domains.
    """
    value: uuid.UUID

    def __post_init__(self) -> None:
        """Validate input type parameters post dataclass initialization.

        Raises:
            TypeError: If the input value is not an instance of uuid.UUID.
        """
        # Step 1: Enforce strict type validation
        # We do this to ensure that only a valid UUID class can initialize ContentId,
        # protecting domain objects from downstream parsing crashes.
        if not isinstance(self.value, uuid.UUID):
            raise TypeError("value must be a uuid.UUID instance")

    @classmethod
    def generate(cls) -> "ContentId":
        """Generate a new random ContentId using UUIDv4.

        Returns:
            ContentId: A new ContentId instance wrapping a randomly generated UUIDv4.
        """
        # Step 1: Instantiate ContentId wrapping a freshly generated UUIDv4
        # We use UUIDv4 because it is statistically guaranteed to be unique globally.
        return cls(uuid.uuid4())

    @classmethod
    def from_str(cls, val: str) -> "ContentId":
        """Construct a ContentId from a UUID string representation.

        Args:
            val: The raw string representation of a UUID.

        Returns:
            ContentId: A constructed ContentId instance.

        Raises:
            ValueError: If the string is not a valid representation of a UUIDv4.
        """
        # Step 1: Attempt parsing the input string using standard uuid.UUID deserialization
        try:
            parsed = uuid.UUID(val)
            # Step 2: Return a new ContentId wrapping the parsed UUID
            return cls(parsed)
        except (ValueError, AttributeError, TypeError) as err:
            # Step 3: Wrap exceptions into a clear ValueError to protect caller domain layers
            # from leakage of low-level uuid parsing errors.
            raise ValueError(f"Invalid UUID format: {val}") from err

    def __str__(self) -> str:
        """Return the canonical string representation of the wrapped UUID.

        Returns:
            str: Standard 36-character hyphenated UUID string.
        """
        # Step 1: Stringify the internal UUID value for serialization / database writes
        return str(self.value)
