import json
import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch
from isb.shared_kernel.types import ContentId
from isb.transcription.domain.entities import Transcript
from isb.transcription.domain.value_objects import Segment
from isb.transcription.infrastructure.adapters import WhisperTranscriberAdapter

@pytest.fixture
def temp_cache_dir(tmp_path: Path) -> Path:
    """Fixture providing a temporary directory for transcription caching."""
    # Step 1: Combine the tmp_path with a cache subdirectory
    return tmp_path / "cache"

def test_whisper_adapter_init(temp_cache_dir: Path) -> None:
    """Verify that WhisperTranscriberAdapter initializes paths and creates cache directories."""
    # Step 1: Instantiate the adapter
    adapter = WhisperTranscriberAdapter(temp_cache_dir, model_name="tiny")
    
    # Step 2: Assert that the cache directory exists on the disk
    assert temp_cache_dir.exists()
    assert adapter.cache_dir == temp_cache_dir
    assert adapter.model_name == "tiny"

def test_whisper_adapter_transcribe(temp_cache_dir: Path) -> None:
    """Verify that transcribe calls whisper, converts segments, and writes to cache JSON."""
    # Step 1: Initialize the adapter
    adapter = WhisperTranscriberAdapter(temp_cache_dir, model_name="tiny")
    content_id = ContentId.generate()
    
    # Step 2: Create a dummy audio file path
    dummy_audio_path = temp_cache_dir / "test.mp3"
    dummy_audio_path.write_text("fake audio")

    # Step 3: Define fake whisper transcribe result
    fake_result = {
        "text": "Hello world, this is a test.",
        "language": "en",
        "segments": [
            {
                "start": 0.0,
                "end": 2.5,
                "text": "Hello world,",
                "avg_logprob": -0.1
            },
            {
                "start": 2.5,
                "end": 5.0,
                "text": "this is a test.",
                "avg_logprob": -0.2
            }
        ]
    }

    # Step 4: Mock the whisper.load_model function
    with patch("whisper.load_model") as mock_load_model:
        mock_model_instance = MagicMock()
        mock_load_model.return_value = mock_model_instance
        mock_model_instance.transcribe.return_value = fake_result

        # Step 5: Execute transcribe
        transcript = adapter.transcribe(
            content_id=content_id,
            audio_path=dummy_audio_path,
            language_hint="en"
        )

        # Step 6: Assert whisper.load_model was called with model name
        mock_load_model.assert_called_once_with("tiny")

        # Step 7: Verify transcribe called on model with correct arguments
        mock_model_instance.transcribe.assert_called_once_with(
            str(dummy_audio_path),
            language="en"
        )

        # Step 8: Verify return Transcript properties
        assert transcript.content_id == content_id
        assert transcript.full_text == "Hello world, this is a test."
        assert transcript.language == "en"
        assert transcript.model == "tiny"
        assert transcript.duration_seconds == 5.0  # From segments end

        # Step 9: Verify Segment objects mappings
        assert len(transcript.segments) == 2
        assert transcript.segments[0].start_seconds == 0.0
        assert transcript.segments[0].end_seconds == 2.5
        assert transcript.segments[0].text == "Hello world,"
        # Confidence score derived from avg_logprob: min(max(1.0 + -0.1, 0.0), 1.0) = 0.9
        assert pytest.approx(transcript.segments[0].confidence, 0.01) == 0.9

        assert transcript.segments[1].start_seconds == 2.5
        assert transcript.segments[1].end_seconds == 5.0
        assert transcript.segments[1].text == "this is a test."
        # Confidence score derived from avg_logprob: min(max(1.0 + -0.2, 0.0), 1.0) = 0.8
        assert pytest.approx(transcript.segments[1].confidence, 0.01) == 0.8

        # Step 10: Verify the transcript JSON cache file was written
        expected_cache_file = temp_cache_dir / f"{content_id}.json"
        assert expected_cache_file.exists()
        
        # Step 11: Verify cache content matches serialized transcript dict structure
        cached_data = json.loads(expected_cache_file.read_text(encoding="utf-8"))
        assert cached_data["full_text"] == "Hello world, this is a test."
        assert cached_data["language"] == "en"
        assert len(cached_data["segments"]) == 2
        assert cached_data["segments"][0]["text"] == "Hello world,"
