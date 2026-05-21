from dataclasses import dataclass, field
from isb.shared_kernel.types import ContentId
from isb.transcription.domain.value_objects import Segment
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

@dataclass
class Transcript:
    """Domain Entity representing the parsed audio transcription result from Whisper.

    Tracks duration, language, and the individual timestamped text segments
    extracted by the speech-to-text model.
    """
    content_id: ContentId
    full_text: str
    segments: list[Segment] = field(default_factory=list)
    language: str = "pt"
    model: str = "base"
    duration_seconds: float = 0.0

    def word_count(self) -> int:
        """Return total number of words in this transcript.

        Returns:
            int: The calculated number of white-space separated word tokens.
        """
        # Step 1: Clean surrounding whitespaces from full text
        cleaned = self.full_text.strip()
        # Step 2: Return 0 if transcript is empty
        if not cleaned:
            return 0
        # Step 3: Split cleaned string by whitespace and calculate length
        return len(cleaned.split())

    def has_segments(self) -> bool:
        """Return True if transcript contains timestamped segments.

        Returns:
            bool: True if there is at least one segment entry, False otherwise.
        """
        # Step 1: Evaluate the size of the segment list collection
        return len(self.segments) > 0
