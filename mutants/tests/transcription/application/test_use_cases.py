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

    def mark_status(self, content_id: ContentId, status: ProcessingStatus) -> None:
        self.statuses[content_id] = status


def test_transcribe_audio_use_case_success() -> None:
    """Test transcribing audio successfully."""
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
    assert len(received_events) == 1
    assert received_events[0].content_id == content_id
    assert received_events[0].transcript_path == Path("/tmp/yt-1.json") # We specify where use_case mock or adapter saves it

def test_transcribe_audio_use_case_failure() -> None:
    """Test that transcription failure marks the manifest as FAILED."""
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
