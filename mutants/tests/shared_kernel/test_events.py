import pytest
from datetime import datetime, timezone
from pathlib import Path
from isb.shared_kernel.types import ContentId
from isb.shared_kernel.events import (
    EventBus,
    AudioExtracted,
    TranscriptionCompleted,
    KnowledgeSynthesized,
)

def test_audio_extracted_event_creation() -> None:
    """Test creating an AudioExtracted event with required fields."""
    content_id = ContentId.generate()
    audio_path = Path("/tmp/audio.wav")
    metadata = {"title": "Test Episode"}
    
    event = AudioExtracted(
        content_id=content_id,
        audio_path=audio_path,
        metadata=metadata
    )
    
    assert event.content_id == content_id
    assert event.audio_path == audio_path
    assert event.metadata == metadata
    assert isinstance(event.event_id, str)
    assert isinstance(event.occurred_at, datetime)
    # Check it is timezone aware or at least standard
    assert event.occurred_at.tzinfo == timezone.utc

def test_event_bus_pub_sub() -> None:
    """Test subscribing and publishing events via EventBus."""
    bus = EventBus()
    received_events = []
    
    def handler(event: AudioExtracted) -> None:
        received_events.append(event)
        
    bus.subscribe(AudioExtracted, handler)
    
    content_id = ContentId.generate()
    event = AudioExtracted(
        content_id=content_id,
        audio_path=Path("/tmp/audio.wav"),
        metadata={}
    )
    
    bus.publish(event)
    
    assert len(received_events) == 1
    assert received_events[0] == event

def test_event_bus_multiple_subscribers() -> None:
    """Test that multiple handlers can subscribe to the same event."""
    bus = EventBus()
    calls = {"h1": 0, "h2": 0}
    
    bus.subscribe(AudioExtracted, lambda e: calls.update({"h1": calls["h1"] + 1}))
    bus.subscribe(AudioExtracted, lambda e: calls.update({"h2": calls["h2"] + 1}))
    bus.subscribe(TranscriptionCompleted, lambda e: calls.update({"h1": calls["h1"] + 1}))  # Shouldn't be called
    
    event = AudioExtracted(
        content_id=ContentId.generate(),
        audio_path=Path("/tmp/audio.wav"),
        metadata={}
    )
    
    bus.publish(event)
    
    assert calls["h1"] == 1
    assert calls["h2"] == 1
