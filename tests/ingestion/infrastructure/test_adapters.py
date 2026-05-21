import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch
from datetime import datetime, timezone
from isb.shared_kernel.types import ContentId
from isb.ingestion.domain.entities import MediaSource, MediaEpisode
from isb.ingestion.infrastructure.adapters import YtDlpExtractorAdapter

@pytest.fixture
def temp_download_dir(tmp_path: Path) -> Path:
    """Fixture providing a temporary directory for downloads."""
    # Step 1: Combine the tmp_path with a downloads subdirectory
    return tmp_path / "downloads"

def test_ytdlp_adapter_init(temp_download_dir: Path) -> None:
    """Verify that YtDlpExtractorAdapter initializes paths and creates directories."""
    # Step 1: Instantiate the adapter
    adapter = YtDlpExtractorAdapter(temp_download_dir)
    
    # Step 2: Assert that the download directory exists on the disk
    assert temp_download_dir.exists()
    assert adapter.download_dir == temp_download_dir

def test_ytdlp_adapter_fetch_new_episodes(temp_download_dir: Path) -> None:
    """Verify that fetch_new_episodes calls yt_dlp flat extraction and maps entries."""
    # Step 1: Initialize the adapter
    adapter = YtDlpExtractorAdapter(temp_download_dir)
    source = MediaSource(
        source_id="src_1",
        url="https://www.youtube.com/playlist?list=some_playlist",
        name="Test Playlist"
    )

    # Step 2: Define fake yt-dlp extracted payload
    fake_info = {
        "_type": "playlist",
        "entries": [
            {
                "id": "video_id_1",
                "title": "Episode 1 Title",
                "duration": 600,
                "upload_date": "20260520"
            },
            {
                "id": "video_id_2",
                "title": "Episode 2 Title",
                "duration": 1200,
                "upload_date": "20260521"
            }
        ]
    }

    # Step 3: Mock the yt_dlp.YoutubeDL class and its extract_info method.
    # Why __enter__: The adapter uses YoutubeDL as a context manager (`with ... as ydl`),
    # so `ydl` is the return of `__enter__`, not the return of the constructor itself.
    with patch("isb.ingestion.infrastructure.adapters.yt_dlp.YoutubeDL") as mock_ytdl_class:
        mock_ytdl_instance = MagicMock()
        mock_ytdl_class.return_value.__enter__ = MagicMock(return_value=mock_ytdl_instance)
        mock_ytdl_class.return_value.__exit__ = MagicMock(return_value=False)
        mock_ytdl_instance.extract_info.return_value = fake_info

        # Step 4: Execute fetch_new_episodes
        episodes = adapter.fetch_new_episodes(source)

        # Step 5: Assert extract_info was called with the correct playlist URL
        mock_ytdl_instance.extract_info.assert_called_once_with(source.url, download=False)

        # Step 6: Verify options passed to YoutubeDL constructor
        ytdl_args = mock_ytdl_class.call_args[0][0]
        assert ytdl_args.get("extract_flat") is True
        assert ytdl_args.get("format") == "bestaudio/best"

        # Step 7: Verify mapped episodes list output and attributes
        assert len(episodes) == 2
        assert episodes[0].external_id == "video_id_1"
        assert episodes[0].title == "Episode 1 Title"
        assert episodes[0].duration_seconds == 600
        # Parse 20260520 to datetime timezone-aware UTC
        expected_date_1 = datetime(2026, 5, 20, tzinfo=timezone.utc)
        assert episodes[0].published_at == expected_date_1

        assert episodes[1].external_id == "video_id_2"
        assert episodes[1].title == "Episode 2 Title"
        assert episodes[1].duration_seconds == 1200
        expected_date_2 = datetime(2026, 5, 21, tzinfo=timezone.utc)
        assert episodes[1].published_at == expected_date_2

def test_ytdlp_adapter_extract_audio(temp_download_dir: Path) -> None:
    """Verify that extract_audio downloads the stream, converts to MP3, and returns details."""
    # Step 1: Initialize adapter
    adapter = YtDlpExtractorAdapter(temp_download_dir)
    episode = MediaEpisode(
        content_id=ContentId.generate(),
        external_id="vid_9876",
        title="Test Audio File",
        published_at=datetime.now(timezone.utc),
        duration_seconds=300
    )

    # Step 2: Define the expected target output path
    expected_output_path = temp_download_dir / "vid_9876.mp3"

    # Step 3: Mock the yt_dlp.YoutubeDL class and its download method.
    # Why __enter__: Same context manager boundary as fetch_new_episodes — see Step 3 above.
    with patch("isb.ingestion.infrastructure.adapters.yt_dlp.YoutubeDL") as mock_ytdl_class:
        mock_ytdl_instance = MagicMock()
        mock_ytdl_class.return_value.__enter__ = MagicMock(return_value=mock_ytdl_instance)
        mock_ytdl_class.return_value.__exit__ = MagicMock(return_value=False)

        # Step 4: Define side-effect to create the dummy file representing the downloaded file
        def fake_download(urls) -> int:
            # Create a file at the target output path with some dummy content
            expected_output_path.write_text("dummy mp3 data")
            return 0  # Success return code

        mock_ytdl_instance.download.side_effect = fake_download

        # Step 5: Execute extract_audio
        audio_path, file_format, size_bytes = adapter.extract_audio(episode)

        # Step 6: Verify YoutubeDL was instantiated with correct postprocessing parameters
        ytdl_args = mock_ytdl_class.call_args[0][0]
        assert ytdl_args.get("format") == "bestaudio/best"
        
        # Verify FFmpegExtractAudio postprocessor is defined
        pps = ytdl_args.get("postprocessors", [])
        assert len(pps) >= 1
        assert pps[0]["key"] == "FFmpegExtractAudio"
        assert pps[0]["preferredcodec"] == "mp3"
        assert pps[0]["preferredquality"] == "192"

        # Step 7: Verify YoutubeDL download was called with the correct watch URL
        mock_ytdl_instance.download.assert_called_once_with([f"https://www.youtube.com/watch?v={episode.external_id}"])

        # Step 8: Verify return parameters
        assert audio_path == expected_output_path
        assert file_format == "mp3"
        assert size_bytes == len("dummy mp3 data")
