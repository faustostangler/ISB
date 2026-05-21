import pytest
from datetime import datetime, timezone
from pathlib import Path
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.shared_kernel.events import EventBus, AudioExtracted
from isb.ingestion.domain.entities import MediaSource, MediaEpisode
from isb.ingestion.domain.exceptions import DownloadError
from isb.ingestion.application.ports import MediaExtractorPort, ManifestPort
from isb.ingestion.application.use_cases import ExtractAudioUseCase

class MockMediaExtractor(MediaExtractorPort):
    def __init__(self, new_episodes: list[MediaEpisode]) -> None:
        self.new_episodes = new_episodes
        self.extracted_episodes = []
        self.fail_on_id = None

    def fetch_new_episodes(self, source: MediaSource) -> list[MediaEpisode]:
        return self.new_episodes

    def extract_audio(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        if self.fail_on_id == episode.external_id:
            raise DownloadError("Simulated download failure")
        self.extracted_episodes.append(episode)
        return Path(f"/tmp/{episode.external_id}.wav"), "wav", 1024


class MockManifest(ManifestPort):
    def __init__(self) -> None:
        self.registry: dict[str, ContentId] = {}
        self.statuses: dict[ContentId, ProcessingStatus] = {}

    def is_processed(self, external_id: str) -> bool:
        cid = self.registry.get(external_id)
        if cid is None:
            return False
        return self.statuses.get(cid) == ProcessingStatus.COMPLETED or self.statuses.get(cid) == ProcessingStatus.TRANSCRIBING

    def get_content_id(self, external_id: str) -> ContentId | None:
        return self.registry.get(external_id)

    def register_episode(self, external_id: str, content_id: ContentId) -> None:
        self.registry[external_id] = content_id

    def mark_status(self, content_id: ContentId, status: ProcessingStatus) -> None:
        self.statuses[content_id] = status

    def has_failed_previously(self, external_id: str) -> bool:
        cid = self.registry.get(external_id)
        if cid is None:
            return False
        return self.statuses.get(cid) == ProcessingStatus.FAILED


def test_extract_audio_use_case_success() -> None:
    """Test extracting audio for new episodes successfully."""
    event_bus = EventBus()
    received_events = []
    event_bus.subscribe(AudioExtracted, lambda e: received_events.append(e))
    
    source = MediaSource(source_id="src-1", url="https://example.com", name="Channel")
    ep1 = MediaEpisode(
        content_id=ContentId.generate(),
        external_id="yt-1",
        title="Ep 1",
        published_at=datetime.now(timezone.utc),
        duration_seconds=120
    )
    
    extractor = MockMediaExtractor([ep1])
    manifest = MockManifest()
    use_case = ExtractAudioUseCase(
        extractor_port=extractor,
        manifest_port=manifest,
        event_bus=event_bus
    )
    
    results = use_case.execute(source)
    
    assert len(results) == 1
    assert results[0].status == ProcessingStatus.TRANSCRIBING
    assert results[0].audio_track is not None
    assert manifest.is_processed("yt-1") is True
    assert len(received_events) == 1
    assert received_events[0].content_id == results[0].content_id
    assert received_events[0].audio_path == Path("/tmp/yt-1.wav")

def test_extract_audio_use_case_idempotency() -> None:
    """Test that already processed episodes are skipped."""
    event_bus = EventBus()
    received_events = []
    event_bus.subscribe(AudioExtracted, lambda e: received_events.append(e))
    
    source = MediaSource(source_id="src-1", url="https://example.com", name="Channel")
    cid = ContentId.generate()
    ep1 = MediaEpisode(
        content_id=cid,
        external_id="yt-1",
        title="Ep 1",
        published_at=datetime.now(timezone.utc),
        duration_seconds=120
    )
    
    extractor = MockMediaExtractor([ep1])
    manifest = MockManifest()
    manifest.register_episode("yt-1", cid)
    manifest.mark_status(cid, ProcessingStatus.TRANSCRIBING) # Already processed
    
    use_case = ExtractAudioUseCase(
        extractor_port=extractor,
        manifest_port=manifest,
        event_bus=event_bus
    )
    
    results = use_case.execute(source)
    
    assert len(results) == 0  # Skipped
    assert len(extractor.extracted_episodes) == 0
    assert len(received_events) == 0

def test_extract_audio_use_case_retry_failed() -> None:
    """Test that a previously failed episode is retried and succeeds."""
    event_bus = EventBus()
    source = MediaSource(source_id="src-1", url="https://example.com", name="Channel")
    cid = ContentId.generate()
    ep1 = MediaEpisode(
        content_id=cid,
        external_id="yt-1",
        title="Ep 1",
        published_at=datetime.now(timezone.utc),
        duration_seconds=120
    )
    
    extractor = MockMediaExtractor([ep1])
    manifest = MockManifest()
    manifest.register_episode("yt-1", cid)
    manifest.mark_status(cid, ProcessingStatus.FAILED) # Previously failed
    
    use_case = ExtractAudioUseCase(
        extractor_port=extractor,
        manifest_port=manifest,
        event_bus=event_bus
    )
    
    results = use_case.execute(source)
    
    assert len(results) == 1
    assert results[0].status == ProcessingStatus.TRANSCRIBING
    assert manifest.statuses[cid] == ProcessingStatus.TRANSCRIBING

def test_extract_audio_use_case_failure_handling() -> None:
    """Test that download failure is captured, status set to FAILED, and doesn't abort pipeline."""
    event_bus = EventBus()
    source = MediaSource(source_id="src-1", url="https://example.com", name="Channel")
    
    ep1 = MediaEpisode(
        content_id=ContentId.generate(),
        external_id="yt-1",
        title="Ep 1 (fails)",
        published_at=datetime.now(timezone.utc),
        duration_seconds=120
    )
    ep2 = MediaEpisode(
        content_id=ContentId.generate(),
        external_id="yt-2",
        title="Ep 2 (succeeds)",
        published_at=datetime.now(timezone.utc),
        duration_seconds=120
    )
    
    extractor = MockMediaExtractor([ep1, ep2])
    extractor.fail_on_id = "yt-1"
    manifest = MockManifest()
    
    use_case = ExtractAudioUseCase(
        extractor_port=extractor,
        manifest_port=manifest,
        event_bus=event_bus
    )
    
    results = use_case.execute(source)
    
    # Both processed (one failed, one succeeded)
    assert len(results) == 2
    assert results[0].status == ProcessingStatus.FAILED
    assert results[1].status == ProcessingStatus.TRANSCRIBING
    assert manifest.statuses[results[0].content_id] == ProcessingStatus.FAILED
    assert manifest.statuses[results[1].content_id] == ProcessingStatus.TRANSCRIBING
