import pytest
from datetime import datetime, timezone
from pathlib import Path
from pydantic import ValidationError
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.ingestion.domain.entities import MediaSource, MediaEpisode
from isb.ingestion.domain.value_objects import (
    AudioTrack,
    ExternalId,
    EpisodeTitle,
    DurationSeconds,
    PublishedAt,
    SourceId,
    SourceName,
    SourceUrl,
)
from isb.ingestion.domain.exceptions import DuplicateEpisodeError

def test_media_episode_initialization() -> None:
    """Test creating a MediaEpisode entity with Value Objects."""
    content_id = ContentId.generate()
    published = PublishedAt(datetime.now(timezone.utc))
    episode = MediaEpisode(
        content_id=content_id,
        external_id=ExternalId("yt-12345"),
        title=EpisodeTitle("Test Title"),
        published_at=published,
        duration_seconds=DurationSeconds(300)
    )
    
    assert episode.content_id == content_id
    assert episode.external_id == ExternalId("yt-12345")
    assert str(episode.title) == "Test Title"
    assert episode.published_at == published
    assert int(episode.duration_seconds.value) == 300
    assert episode.status == ProcessingStatus.PENDING
    assert episode.audio_track is None

def test_media_episode_mark_extracted() -> None:
    """Test marking a MediaEpisode as extracted with an AudioTrack."""
    episode = MediaEpisode(
        content_id=ContentId.generate(),
        external_id=ExternalId("yt-123"),
        title=EpisodeTitle("Title"),
        published_at=PublishedAt(datetime.now(timezone.utc)),
        duration_seconds=DurationSeconds(120)
    )
    
    audio_path = Path("/tmp/yt-123.wav")
    episode.mark_extracted(audio_path=audio_path, file_format="wav", size_bytes=1024)
    
    assert episode.status == ProcessingStatus.TRANSCRIBING
    assert episode.audio_track is not None
    assert episode.audio_track.file_path == audio_path
    assert episode.audio_track.file_format == "wav"
    assert episode.audio_track.size_bytes == 1024
    assert episode.audio_track.duration_seconds == 120

def test_media_episode_mark_failed() -> None:
    """Test marking an episode as failed."""
    episode = MediaEpisode(
        content_id=ContentId.generate(),
        external_id=ExternalId("yt-123"),
        title=EpisodeTitle("Title"),
        published_at=PublishedAt(datetime.now(timezone.utc)),
        duration_seconds=DurationSeconds(120)
    )
    episode.mark_failed()
    assert episode.status == ProcessingStatus.FAILED

def test_media_source_add_episode() -> None:
    """Test adding episodes to a MediaSource."""
    source = MediaSource(
        source_id=SourceId("src-123"),
        url=SourceUrl("https://youtube.com/c/example"),
        name=SourceName("Example Channel")
    )
    
    episode = MediaEpisode(
        content_id=ContentId.generate(),
        external_id=ExternalId("yt-1"),
        title=EpisodeTitle("Episode 1"),
        published_at=PublishedAt(datetime.now(timezone.utc)),
        duration_seconds=DurationSeconds(100)
    )
    
    source.add_episode(episode)
    assert len(source.episodes) == 1
    assert source.has_episode(ExternalId("yt-1")) is True
    assert source.has_episode(ExternalId("yt-2")) is False

def test_media_source_duplicate_episode_raises_error() -> None:
    """Test that adding a duplicate episode external_id raises DuplicateEpisodeError."""
    source = MediaSource(
        source_id=SourceId("src-123"),
        url=SourceUrl("https://youtube.com/c/example"),
        name=SourceName("Example Channel")
    )
    
    ep1 = MediaEpisode(
        content_id=ContentId.generate(),
        external_id=ExternalId("yt-1"),
        title=EpisodeTitle("Episode 1"),
        published_at=PublishedAt(datetime.now(timezone.utc)),
        duration_seconds=DurationSeconds(100)
    )
    ep2 = MediaEpisode(
        content_id=ContentId.generate(),
        external_id=ExternalId("yt-1"), # Same external_id
        title=EpisodeTitle("Episode 1 Clone"),
        published_at=PublishedAt(datetime.now(timezone.utc)),
        duration_seconds=DurationSeconds(100)
    )
    
    source.add_episode(ep1)
    with pytest.raises(DuplicateEpisodeError):
        source.add_episode(ep2)

def test_value_objects_validation() -> None:
    """Test invariant and type validations on custom Value Objects."""
    with pytest.raises(ValueError):
        ExternalId("   ")
    with pytest.raises(TypeError):
        ExternalId(123)  # type: ignore
        
    with pytest.raises(ValueError):
        EpisodeTitle("")
    with pytest.raises(TypeError):
        EpisodeTitle(None)  # type: ignore
        
    with pytest.raises(ValueError):
        DurationSeconds(-5)
    with pytest.raises(TypeError):
        DurationSeconds("123")  # type: ignore
        
    with pytest.raises(ValueError):
        PublishedAt(datetime.now()) # not timezone aware
        
    with pytest.raises(ValueError):
        SourceUrl("invalid-url")
