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
        self.fetched_sources = []
        self.extract_audio_calls = []

    def fetch_new_episodes(self, source: MediaSource) -> list[MediaEpisode]:
        self.fetched_sources.append(source)
        return self.new_episodes

    def extract_audio(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        self.extract_audio_calls.append(episode)
        if self.fail_on_id == episode.external_id:
            raise DownloadError("Simulated download failure")
        self.extracted_episodes.append(episode)
        return Path(f"/tmp/{episode.external_id}.wav"), "wav", 1024


class MockManifest(ManifestPort):
    def __init__(self) -> None:
        self.registry: dict[str, ContentId] = {}
        self.statuses: dict[ContentId, ProcessingStatus] = {}
        self.status_history: list[tuple[ContentId, ProcessingStatus]] = []

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
        self.status_history.append((content_id, status))

    def has_failed_previously(self, external_id: str) -> bool:
        cid = self.registry.get(external_id)
        if cid is None:
            return False
        return self.statuses.get(cid) == ProcessingStatus.FAILED


def test_extract_audio_use_case_success(caplog: pytest.LogCaptureFixture) -> None:
    """Test extracting audio for new episodes successfully."""
    import logging
    caplog.set_level(logging.INFO)
    event_bus = EventBus()
    received_events = []
    event_bus.subscribe(AudioExtracted, lambda e: received_events.append(e))
    
    source = MediaSource(source_id="src-1", url="https://example.com", name="Channel")
    ep1_original_id = ContentId.generate()
    ep1 = MediaEpisode(
        content_id=ep1_original_id,
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
    
    assert source.last_synced_at is None
    results = use_case.execute(source)
    
    assert len(results) == 1
    episode = results[0]
    assert episode.status == ProcessingStatus.TRANSCRIBING
    assert episode.audio_track is not None
    assert episode.is_extracted() is True
    assert manifest.is_processed("yt-1") is True
    
    # Assert that a new ContentId was generated and original was overwritten
    cid = episode.content_id
    assert cid != ep1_original_id
    
    # Assert exact mock parameter inputs
    assert extractor.fetched_sources == [source]
    assert extractor.extract_audio_calls == [episode]
    
    # Assert detail fields of AudioTrack
    track = episode.audio_track
    assert track.file_path == Path("/tmp/yt-1.wav")
    assert track.file_format == "wav"
    assert track.size_bytes == 1024
    assert track.duration_seconds == 120
    
    # Assert source episodes registry
    assert len(source.episodes) == 1
    assert source.episodes[0] == episode
    
    # Assert intermediate status transitions
    assert manifest.status_history == [
        (cid, ProcessingStatus.EXTRACTING),
        (cid, ProcessingStatus.TRANSCRIBING)
    ]
    
    # Assert source sync time
    assert source.last_synced_at is not None
    
    # Assert event metadata structure and contents
    assert len(received_events) == 1
    assert received_events[0].content_id == cid
    assert received_events[0].audio_path == Path("/tmp/yt-1.wav")
    assert received_events[0].metadata == {
        "title": "Ep 1",
        "external_id": "yt-1",
        "duration_seconds": 120,
        "published_at": ep1.published_at.isoformat()
    }

    # Assert exact logging messages
    assert any(r.message == f"Registered new episode yt-1 with ContentId {cid}" for r in caplog.records)
    assert any(r.message == "Successfully extracted audio for yt-1 and published event." for r in caplog.records)

def test_extract_audio_use_case_idempotency(caplog: pytest.LogCaptureFixture) -> None:
    """Test that already processed episodes are skipped."""
    import logging
    caplog.set_level(logging.INFO)
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
    
    # Reset history to only track what happens during execution
    manifest.status_history.clear()
    
    use_case = ExtractAudioUseCase(
        extractor_port=extractor,
        manifest_port=manifest,
        event_bus=event_bus
    )
    
    results = use_case.execute(source)
    
    assert len(results) == 0  # Skipped
    assert len(extractor.extracted_episodes) == 0
    assert len(received_events) == 0
    assert len(manifest.status_history) == 0
    assert source.last_synced_at is not None

    # Assert logging
    assert any(r.message == "Episode yt-1 already processed. Skipping." for r in caplog.records)

def test_extract_audio_use_case_retry_failed(caplog: pytest.LogCaptureFixture) -> None:
    """Test that a previously failed episode is retried and succeeds."""
    import logging
    caplog.set_level(logging.INFO)
    event_bus = EventBus()
    source = MediaSource(source_id="src-1", url="https://example.com", name="Channel")
    manifest_cid = ContentId.generate()
    episode_cid = ContentId.generate()
    ep1 = MediaEpisode(
        content_id=episode_cid,
        external_id="yt-1",
        title="Ep 1",
        published_at=datetime.now(timezone.utc),
        duration_seconds=120
    )
    
    extractor = MockMediaExtractor([ep1])
    manifest = MockManifest()
    manifest.register_episode("yt-1", manifest_cid)
    manifest.mark_status(manifest_cid, ProcessingStatus.FAILED) # Previously failed
    
    manifest.status_history.clear()
    
    use_case = ExtractAudioUseCase(
        extractor_port=extractor,
        manifest_port=manifest,
        event_bus=event_bus
    )
    
    results = use_case.execute(source)
    
    assert len(results) == 1
    episode = results[0]
    assert episode.status == ProcessingStatus.TRANSCRIBING
    # The mismatched episode_cid must have been overwritten by manifest_cid
    assert episode.content_id == manifest_cid
    assert manifest.statuses[manifest_cid] == ProcessingStatus.TRANSCRIBING
    assert manifest.status_history == [
        (manifest_cid, ProcessingStatus.EXTRACTING),
        (manifest_cid, ProcessingStatus.TRANSCRIBING)
    ]
    assert source.last_synced_at is not None

    # Assert exact mock parameter inputs
    assert extractor.fetched_sources == [source]
    assert extractor.extract_audio_calls == [episode]

    # Assert logging
    assert any(r.message == f"Retrying previously failed episode yt-1 with ContentId {manifest_cid}" for r in caplog.records)

def test_extract_audio_use_case_retry_failed_missing_content_id(caplog: pytest.LogCaptureFixture) -> None:
    """Test the fallback when a failed episode is retried but its ContentId is missing."""
    import logging
    caplog.set_level(logging.INFO)
    class MockManifestMissingContentId(MockManifest):
        def has_failed_previously(self, external_id: str) -> bool:
            return True
        def get_content_id(self, external_id: str) -> ContentId | None:
            return None

    event_bus = EventBus()
    source = MediaSource(source_id="src-1", url="https://example.com", name="Channel")
    original_cid = ContentId.generate()
    ep1 = MediaEpisode(
        content_id=original_cid,  # This will be replaced by the use case
        external_id="yt-1",
        title="Ep 1",
        published_at=datetime.now(timezone.utc),
        duration_seconds=120
    )
    
    extractor = MockMediaExtractor([ep1])
    manifest = MockManifestMissingContentId()
    
    use_case = ExtractAudioUseCase(
        extractor_port=extractor,
        manifest_port=manifest,
        event_bus=event_bus
    )
    
    results = use_case.execute(source)
    
    assert len(results) == 1
    new_cid = results[0].content_id
    assert isinstance(new_cid, ContentId)
    assert new_cid != original_cid
    assert manifest.registry["yt-1"] == new_cid
    assert manifest.statuses[new_cid] == ProcessingStatus.TRANSCRIBING
    assert manifest.status_history == [
        (new_cid, ProcessingStatus.EXTRACTING),
        (new_cid, ProcessingStatus.TRANSCRIBING)
    ]
    
    # Assert exact mock parameter inputs
    assert extractor.fetched_sources == [source]
    assert extractor.extract_audio_calls == [results[0]]

    # Assert logging
    assert any(r.message == f"Retrying previously failed episode yt-1 with ContentId {new_cid}" for r in caplog.records)

def test_extract_audio_use_case_failure_handling(caplog: pytest.LogCaptureFixture) -> None:
    """Test that download failure is captured, status set to FAILED, and doesn't abort pipeline."""
    import logging
    caplog.set_level(logging.INFO)
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
    
    # Assert only succeeded episode is added to source.episodes
    assert len(source.episodes) == 1
    assert source.episodes[0].external_id == "yt-2"
    
    # Verify status history for both
    cid1 = results[0].content_id
    cid2 = results[1].content_id
    
    assert manifest.status_history == [
        (cid1, ProcessingStatus.EXTRACTING),
        (cid1, ProcessingStatus.FAILED),
        (cid2, ProcessingStatus.EXTRACTING),
        (cid2, ProcessingStatus.TRANSCRIBING)
    ]
    assert source.last_synced_at is not None

    # Assert logging
    assert any(r.message == "Failed to extract audio for episode yt-1." for r in caplog.records)

def test_extract_audio_use_case_duplicate_episode_in_source(caplog: pytest.LogCaptureFixture) -> None:
    """Test that duplicate episode in source raises DuplicateEpisodeError, is caught, and marked FAILED."""
    import logging
    caplog.set_level(logging.INFO)
    event_bus = EventBus()
    
    source = MediaSource(source_id="src-1", url="https://example.com", name="Channel")
    ep1 = MediaEpisode(
        content_id=ContentId.generate(),
        external_id="yt-1",
        title="Ep 1",
        published_at=datetime.now(timezone.utc),
        duration_seconds=120
    )
    # Pre-add ep1 to source so adding it again raises DuplicateEpisodeError
    source.add_episode(ep1)
    
    # Clean/new ep instance returned by extractor (e.g. fresh metadata check)
    ep1_dup = MediaEpisode(
        content_id=ContentId.generate(),
        external_id="yt-1",
        title="Ep 1",
        published_at=datetime.now(timezone.utc),
        duration_seconds=120
    )
    
    extractor = MockMediaExtractor([ep1_dup])
    manifest = MockManifest()
    use_case = ExtractAudioUseCase(
        extractor_port=extractor,
        manifest_port=manifest,
        event_bus=event_bus
    )
    
    results = use_case.execute(source)
    
    assert len(results) == 1
    assert results[0].status == ProcessingStatus.FAILED
    assert manifest.statuses[results[0].content_id] == ProcessingStatus.FAILED
    
    # The source should still only contain the pre-added ep1
    assert len(source.episodes) == 1
    assert source.episodes[0] == ep1
    
    assert any(r.message == "Failed to extract audio for episode yt-1." for r in caplog.records)


def test_extract_audio_use_case_empty_episodes(caplog: pytest.LogCaptureFixture) -> None:
    """Test that when there are no new episodes, the loop is skipped and an empty list is returned."""
    import logging
    caplog.set_level(logging.INFO)
    event_bus = EventBus()
    source = MediaSource(source_id="src-1", url="https://example.com", name="Channel")
    
    extractor = MockMediaExtractor([])
    manifest = MockManifest()
    use_case = ExtractAudioUseCase(
        extractor_port=extractor,
        manifest_port=manifest,
        event_bus=event_bus
    )
    
    assert source.last_synced_at is None
    results = use_case.execute(source)
    
    assert results == []
    assert isinstance(results, list)
    assert source.last_synced_at is not None
    assert extractor.fetched_sources == [source]
    assert extractor.extract_audio_calls == []


def test_extract_audio_use_case_idempotency_multiple_episodes(caplog: pytest.LogCaptureFixture) -> None:
    """Test that a processed episode followed by a new episode does not halt the pipeline (kills continue -> break mutant)."""
    import logging
    caplog.set_level(logging.INFO)
    event_bus = EventBus()
    received_events = []
    event_bus.subscribe(AudioExtracted, lambda e: received_events.append(e))
    
    source = MediaSource(source_id="src-1", url="https://example.com", name="Channel")
    cid1 = ContentId.generate()
    ep1 = MediaEpisode(
        content_id=cid1,
        external_id="yt-1",
        title="Ep 1 (processed)",
        published_at=datetime.now(timezone.utc),
        duration_seconds=120
    )
    
    ep2 = MediaEpisode(
        content_id=ContentId.generate(),
        external_id="yt-2",
        title="Ep 2 (new)",
        published_at=datetime.now(timezone.utc),
        duration_seconds=180
    )
    
    extractor = MockMediaExtractor([ep1, ep2])
    manifest = MockManifest()
    manifest.register_episode("yt-1", cid1)
    manifest.mark_status(cid1, ProcessingStatus.TRANSCRIBING) # ep1 is already processed
    
    manifest.status_history.clear()
    
    use_case = ExtractAudioUseCase(
        extractor_port=extractor,
        manifest_port=manifest,
        event_bus=event_bus
    )
    
    results = use_case.execute(source)
    
    # Assert ep1 was skipped, but ep2 was processed successfully
    assert len(results) == 1
    assert results[0].external_id == "yt-2"
    assert results[0].status == ProcessingStatus.TRANSCRIBING
    assert manifest.is_processed("yt-2") is True
    
    # Assert events for ep2 were published
    assert len(received_events) == 1
    assert received_events[0].content_id == results[0].content_id
    
    # Assert logs for both
    assert any(r.message == "Episode yt-1 already processed. Skipping." for r in caplog.records)
    assert any(r.message == f"Registered new episode yt-2 with ContentId {results[0].content_id}" for r in caplog.records)
    assert any(r.message == "Successfully extracted audio for yt-2 and published event." for r in caplog.records)

