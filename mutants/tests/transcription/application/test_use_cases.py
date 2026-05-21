import pytest
from pathlib import Path
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.shared_kernel.events import EventBus, TranscriptionCompleted
from isb.transcription.domain.entities import Transcript
from isb.transcription.domain.value_objects import Segment
from isb.transcription.domain.exceptions import TranscriptionError
from isb.transcription.application.ports import TranscriberPort, TranscriptionManifestPort
from isb.transcription.application.use_cases import TranscribeAudioUseCase

class MockTranscriber(TranscriberPort):
    def __init__(self, should_fail: bool = False) -> None:
        self.should_fail = should_fail
        self.transcribed_calls = []

    def transcribe(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
        if self.should_fail:
            raise TranscriptionError("Whisper failed")
        
        self.transcribed_calls.append((content_id, audio_path, language_hint))
        return Transcript(
            content_id=content_id,
            full_text="Transcrição de teste",
            segments=[Segment(0.0, 2.0, "Transcrição de teste", 0.99)],
            language="pt",
            model="base",
            duration_seconds=2.0
        )


class MockTranscriptionManifest(TranscriptionManifestPort):
    def __init__(self) -> None:
        self.statuses: dict[ContentId, ProcessingStatus] = {}
        self.status_history: list[tuple[ContentId, ProcessingStatus]] = []

    def mark_status(self, content_id: ContentId, status: ProcessingStatus) -> None:
        self.statuses[content_id] = status
        self.status_history.append((content_id, status))


def test_transcribe_audio_use_case_success(caplog: pytest.LogCaptureFixture) -> None:
    """Test transcribing audio successfully."""
    import logging
    caplog.set_level(logging.INFO)
    event_bus = EventBus()
    received_events = []
    event_bus.subscribe(TranscriptionCompleted, lambda e: received_events.append(e))
    
    content_id = ContentId.generate()
    audio_path = Path("/tmp/yt-1.wav")
    
    transcriber = MockTranscriber()
    manifest = MockTranscriptionManifest()
    use_case = TranscribeAudioUseCase(
        transcriber_port=transcriber,
        manifest_port=manifest,
        event_bus=event_bus
    )
    
    transcript = use_case.execute(content_id, audio_path, language_hint="pt")
    
    assert transcript.content_id == content_id
    assert transcript.full_text == "Transcrição de teste"
    assert manifest.statuses[content_id] == ProcessingStatus.SYNTHESIZING
    assert manifest.status_history == [
        (content_id, ProcessingStatus.TRANSCRIBING),
        (content_id, ProcessingStatus.SYNTHESIZING)
    ]
    
    assert len(received_events) == 1
    assert received_events[0].content_id == content_id
    assert received_events[0].transcript_path == Path("/tmp/yt-1.json")
    assert received_events[0].metadata == {
        "language": "pt",
        "model": "base",
        "duration_seconds": 2.0,
        "word_count": 3
    }

    # Assert calls
    assert transcriber.transcribed_calls == [(content_id, audio_path, "pt")]

    # Assert logging
    assert any(r.message == f"Starting transcription for content {content_id} (audio: {audio_path})" for r in caplog.records)
    assert any(r.message == f"Successfully transcribed content {content_id} and published event." for r in caplog.records)

def test_transcribe_audio_use_case_failure(caplog: pytest.LogCaptureFixture) -> None:
    """Test that transcription failure marks the manifest as FAILED."""
    import logging
    caplog.set_level(logging.INFO)
    event_bus = EventBus()
    content_id = ContentId.generate()
    audio_path = Path("/tmp/yt-1.wav")
    
    transcriber = MockTranscriber(should_fail=True)
    manifest = MockTranscriptionManifest()
    use_case = TranscribeAudioUseCase(
        transcriber_port=transcriber,
        manifest_port=manifest,
        event_bus=event_bus
    )
    
    with pytest.raises(TranscriptionError):
        use_case.execute(content_id, audio_path)
        
    assert manifest.statuses[content_id] == ProcessingStatus.FAILED
    assert manifest.status_history == [
        (content_id, ProcessingStatus.TRANSCRIBING),
        (content_id, ProcessingStatus.FAILED)
    ]
    
    # Assert call parameter was attempted (failed before saving log call but status set)
    assert transcriber.transcribed_calls == []

    # Assert logging
    assert any(r.message == f"Failed transcription for content {content_id}." for r in caplog.records)

def test_transcribe_audio_use_case_default_language(caplog: pytest.LogCaptureFixture) -> None:
    """Test transcribing audio without language hint, falling back to None."""
    import logging
    caplog.set_level(logging.INFO)
    event_bus = EventBus()
    received_events = []
    event_bus.subscribe(TranscriptionCompleted, lambda e: received_events.append(e))
    
    content_id = ContentId.generate()
    audio_path = Path("/tmp/yt-1.wav")
    
    transcriber = MockTranscriber()
    manifest = MockTranscriptionManifest()
    use_case = TranscribeAudioUseCase(
        transcriber_port=transcriber,
        manifest_port=manifest,
        event_bus=event_bus
    )
    
    transcript = use_case.execute(content_id, audio_path)
    
    assert transcript.content_id == content_id
    assert transcriber.transcribed_calls == [(content_id, audio_path, None)]
    
    # Assert status history
    assert manifest.status_history == [
        (content_id, ProcessingStatus.TRANSCRIBING),
        (content_id, ProcessingStatus.SYNTHESIZING)
    ]
    
    # Assert event published
    assert len(received_events) == 1
    assert received_events[0].content_id == content_id
    assert received_events[0].transcript_path == Path("/tmp/yt-1.json")
    
    # Assert logging
    assert any(r.message == f"Starting transcription for content {content_id} (audio: {audio_path})" for r in caplog.records)
    assert any(r.message == f"Successfully transcribed content {content_id} and published event." for r in caplog.records)

