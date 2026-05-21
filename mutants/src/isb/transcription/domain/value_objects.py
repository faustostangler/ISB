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
