import pytest
from isb.shared_kernel.types import ContentId
from isb.transcription.domain.entities import Transcript
from isb.transcription.domain.value_objects import (
    Segment,
    LanguageCode,
    ModelName,
    TranscriptText,
)

def test_segment_initialization() -> None:
    """Test creating a Segment value object."""
    segment = Segment(
        start_seconds=0.0,
        end_seconds=5.5,
        text="Hello world",
        confidence=0.95
    )
    assert segment.start_seconds == 0.0
    assert segment.end_seconds == 5.5
    assert segment.text == "Hello world"
    assert segment.confidence == 0.95

def test_segment_validation_negative_times() -> None:
    """Test that negative times raise ValueError."""
    with pytest.raises(ValueError, match="cannot be negative"):
        Segment(start_seconds=-1.0, end_seconds=5.0, text="Invalid start", confidence=1.0)
    with pytest.raises(ValueError, match="cannot be negative"):
        Segment(start_seconds=1.0, end_seconds=-5.0, text="Invalid end", confidence=1.0)

def test_segment_validation_start_after_end() -> None:
    """Test that end_seconds < start_seconds raises ValueError."""
    with pytest.raises(ValueError, match="start_seconds cannot be after end_seconds"):
        Segment(start_seconds=5.0, end_seconds=4.0, text="Invalid range", confidence=1.0)

def test_transcript_initialization() -> None:
    """Test creating a Transcript entity."""
    content_id = ContentId.generate()
    segment = Segment(start_seconds=0.0, end_seconds=2.0, text="Hello", confidence=0.9)
    
    transcript = Transcript(
        content_id=content_id,
        full_text=TranscriptText("Hello"),
        segments=[segment],
        language=LanguageCode("pt"),
        model=ModelName("base"),
        duration_seconds=2.0
    )
    
    assert transcript.content_id == content_id
    assert transcript.full_text.value == "Hello"
    assert transcript.segments == [segment]
    assert transcript.language == LanguageCode("pt")
    assert transcript.model == ModelName("base")
    assert transcript.duration_seconds == 2.0
    assert transcript.word_count() == 1
    assert transcript.has_segments() is True

def test_transcript_empty_word_count() -> None:
    """Test word count with empty text."""
    transcript = Transcript(
        content_id=ContentId.generate(),
        full_text=TranscriptText("   "),
        segments=[],
        language=LanguageCode("en"),
        model=ModelName("base"),
        duration_seconds=0.0
    )
    assert transcript.word_count() == 0
    assert transcript.has_segments() is False

def test_transcription_value_objects_validation() -> None:
    """Test validations for LanguageCode, ModelName, and TranscriptText."""
    with pytest.raises(ValueError):
        LanguageCode("p")
    with pytest.raises(ValueError):
        LanguageCode("longerthanfive")
    with pytest.raises(TypeError):
        LanguageCode(123)  # type: ignore

    with pytest.raises(ValueError):
        ModelName("")
    with pytest.raises(TypeError):
        ModelName(None)  # type: ignore

    with pytest.raises(ValueError):
        TranscriptText("  ")
    with pytest.raises(TypeError):
        TranscriptText(1.23)  # type: ignore
