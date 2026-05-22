"""Integration tests for the Composition Root (main.py).

These tests cover the three public functions of the composition root:
  1. load_sources_from_yaml  — YAML parsing → MediaSource list
  2. bootstrap_composition_root — wires concrete adapters to use cases via ports
  3. run_pipeline — concurrent ThreadPoolExecutor loop over sources

This test file follows the Stangler RED-GREEN-REFACTOR cycle:
  RED  (now): tests are written against the known interface contracts.
  GREEN (next): main.py stubs are replaced with real implementation.

All tests use tmp_path isolation and mock the settings singleton to avoid
touching real filesystem paths or making any network calls.
"""
import json
import pytest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import MagicMock, patch

from isb.ingestion.domain.entities import MediaSource
from isb.main import bootstrap_composition_root, load_sources_from_yaml, main, run_pipeline


# ===========================================================================
# Fixtures
# ===========================================================================

@pytest.fixture
def sources_yaml_with_entries(tmp_path: Path) -> Path:
    """Write a well-formed sources.yaml with two entries and return its path."""
    # Step 1: Construct YAML content covering both required and optional fields
    config_content = """\
sources:
  - id: test-source-1
    name: "Test Creator"
    url: "https://www.youtube.com/playlist?list=123"
    category: "AI"
    tags:
      - ml
      - llm
  - id: test-source-2
    name: "Second Creator"
    url: "https://www.youtube.com/@SecondCreator"
    category: "Productivity"
    tags:
      - obsidian
"""
    config_file = tmp_path / "sources.yaml"
    config_file.write_text(config_content, encoding="utf-8")
    return config_file


@pytest.fixture
def empty_sources_yaml(tmp_path: Path) -> Path:
    """Write a sources.yaml that has an empty sources list and return its path."""
    # Step 1: Write YAML with a sources key mapping to an empty list
    config_file = tmp_path / "sources.yaml"
    config_file.write_text("sources: []", encoding="utf-8")
    return config_file


# ===========================================================================
# load_sources_from_yaml Tests
# ===========================================================================

def test_load_sources_from_yaml_valid(sources_yaml_with_entries: Path) -> None:
    """Verify that load_sources_from_yaml parses a valid YAML file into MediaSource entities."""
    # Step 1: Invoke the YAML loader with the valid config path
    sources = load_sources_from_yaml(sources_yaml_with_entries)

    # Step 2: Validate number of sources returned matches the YAML entry count
    assert len(sources) == 2

    # Step 3: Validate the first source entity fields map from YAML keys correctly
    assert sources[0].source_id == "test-source-1"
    assert sources[0].name == "Test Creator"
    assert sources[0].url == "https://www.youtube.com/playlist?list=123"

    # Step 4: Validate the second source entity
    assert sources[1].source_id == "test-source-2"
    assert sources[1].name == "Second Creator"


def test_load_sources_from_yaml_empty_returns_empty_list(empty_sources_yaml: Path) -> None:
    """Verify that load_sources_from_yaml returns an empty list when sources is empty."""
    # Step 1: Parse the empty sources file
    sources = load_sources_from_yaml(empty_sources_yaml)

    # Step 2: Assert the returned list is empty, not None or erroring
    assert sources == []


def test_load_sources_from_yaml_returns_media_source_types(sources_yaml_with_entries: Path) -> None:
    """Verify that all returned items are MediaSource domain entities, not raw dicts."""
    # Step 1: Parse the YAML file
    sources = load_sources_from_yaml(sources_yaml_with_entries)

    # Step 2: Assert each returned object is a proper domain entity instance
    for source in sources:
        assert isinstance(source, MediaSource), (
            f"Expected MediaSource instance, got {type(source)}"
        )


# ===========================================================================
# bootstrap_composition_root Tests
# ===========================================================================

def test_bootstrap_returns_event_bus_and_use_case(tmp_path: Path) -> None:
    """Verify bootstrap_composition_root returns a wired EventBus and ExtractAudioUseCase."""
    # Step 1: Patch settings to use isolated temp paths to avoid touching real filesystem
    with patch("isb.main.settings") as mock_settings:
        mock_settings.MANIFEST_DB_PATH = tmp_path / "manifest.db"
        mock_settings.OBSIDIAN_VAULT_PATH = tmp_path / "vault"
        mock_settings.MEDIA_DATA_DIR = tmp_path / "media"
        mock_settings.WHISPER_MODEL = "tiny"
        mock_settings.OLLAMA_BASE_URL = "http://localhost:11434"
        mock_settings.OLLAMA_MODEL = "qwen2.5:7b"

        # Step 2: Call the bootstrap function
        event_bus, extract_use_case = bootstrap_composition_root()

    # Step 3: Verify returned types are correct
    from isb.shared_kernel.events import EventBus
    from isb.ingestion.application.use_cases import ExtractAudioUseCase
    assert isinstance(event_bus, EventBus)
    assert isinstance(extract_use_case, ExtractAudioUseCase)


def test_bootstrap_creates_vault_directories(tmp_path: Path) -> None:
    """Verify bootstrap_composition_root creates the Obsidian vault directories on disk."""
    # Step 1: Patch settings to controlled temp directories
    vault_path = tmp_path / "vault"
    with patch("isb.main.settings") as mock_settings:
        mock_settings.MANIFEST_DB_PATH = tmp_path / "manifest.db"
        mock_settings.OBSIDIAN_VAULT_PATH = vault_path
        mock_settings.MEDIA_DATA_DIR = tmp_path / "media"
        mock_settings.WHISPER_MODEL = "tiny"
        mock_settings.OLLAMA_BASE_URL = "http://localhost:11434"
        mock_settings.OLLAMA_MODEL = "qwen2.5:7b"

        # Step 2: Call bootstrap to trigger directory creation side effects
        bootstrap_composition_root()

    # Step 3: Assert that the vault directory structure exists after bootstrapping
    assert (vault_path / "00-Raw").exists(), "Raw notes directory must be created by bootstrap"
    assert (vault_path / "10-Wiki").exists(), "Wiki directory must be created by bootstrap"


# ===========================================================================
# run_pipeline Tests
# ===========================================================================

def test_run_pipeline_with_empty_sources_does_not_crash(tmp_path: Path) -> None:
    """Verify that run_pipeline completes without error when sources list is empty."""
    # Step 1: Patch settings to use isolated paths and zero sources
    config_file = tmp_path / "sources.yaml"
    config_file.write_text("sources: []", encoding="utf-8")

    with patch("isb.main.settings") as mock_settings:
        mock_settings.SOURCES_CONFIG_PATH = config_file
        mock_settings.MANIFEST_DB_PATH = tmp_path / "manifest.db"
        mock_settings.OBSIDIAN_VAULT_PATH = tmp_path / "vault"
        mock_settings.MEDIA_DATA_DIR = tmp_path / "media"
        mock_settings.WHISPER_MODEL = "tiny"
        mock_settings.OLLAMA_BASE_URL = "http://localhost:11434"
        mock_settings.OLLAMA_MODEL = "qwen2.5:7b"
        mock_settings.MAX_WORKERS = 1

        # Step 2: Execute pipeline — must not raise any exceptions with zero sources
        run_pipeline()


def test_run_pipeline_calls_extract_use_case_per_source(tmp_path: Path) -> None:
    """Verify that run_pipeline calls ExtractAudioUseCase.execute once per loaded source."""
    # Step 1: Create a YAML with exactly one source entry
    config_file = tmp_path / "sources.yaml"
    config_file.write_text(
        "sources:\n  - id: src-1\n    name: Test\n    url: https://youtube.com/c/test\n",
        encoding="utf-8"
    )

    with patch("isb.main.settings") as mock_settings:
        mock_settings.SOURCES_CONFIG_PATH = config_file
        mock_settings.MANIFEST_DB_PATH = tmp_path / "manifest.db"
        mock_settings.OBSIDIAN_VAULT_PATH = tmp_path / "vault"
        mock_settings.MEDIA_DATA_DIR = tmp_path / "media"
        mock_settings.WHISPER_MODEL = "tiny"
        mock_settings.OLLAMA_BASE_URL = "http://localhost:11434"
        mock_settings.OLLAMA_MODEL = "qwen2.5:7b"
        mock_settings.MAX_WORKERS = 1

        # Step 2: Patch the ExtractAudioUseCase.execute to intercept calls
        # Why: We verify the pipeline submits the use case per source without real I/O
        with patch("isb.main.ExtractAudioUseCase") as MockUseCase:
            mock_instance = MagicMock()
            MockUseCase.return_value = mock_instance
            # Simulate successful extraction returning empty list (no episodes)
            mock_instance.execute.return_value = []

            # Step 3: Also patch bootstrap to return our mock
            with patch("isb.main.bootstrap_composition_root") as mock_bootstrap:
                from isb.shared_kernel.events import EventBus
                mock_bus = EventBus()
                mock_bootstrap.return_value = (mock_bus, mock_instance)

                # Step 4: Run the pipeline
                run_pipeline()

                # Step 5: Verify execute was called exactly once with the loaded MediaSource
                mock_instance.execute.assert_called_once()
                called_source = mock_instance.execute.call_args[0][0]
                assert isinstance(called_source, MediaSource)
                assert called_source.source_id == "src-1"


# ===========================================================================
# main() Integration Test
# ===========================================================================

def test_main_orchestrates_pipeline_end_to_end(tmp_path: Path) -> None:
    """Verify that main() calls run_pipeline and completes without error."""
    # Step 1: Create minimal empty config to avoid file-not-found in pipeline
    config_file = tmp_path / "sources.yaml"
    config_file.write_text("sources: []", encoding="utf-8")

    with patch("isb.main.settings") as mock_settings:
        mock_settings.SOURCES_CONFIG_PATH = config_file
        mock_settings.MANIFEST_DB_PATH = tmp_path / "manifest.db"
        mock_settings.OBSIDIAN_VAULT_PATH = tmp_path / "vault"
        mock_settings.MEDIA_DATA_DIR = tmp_path / "media"
        mock_settings.WHISPER_MODEL = "tiny"
        mock_settings.OLLAMA_BASE_URL = "http://localhost:11434"
        mock_settings.OLLAMA_MODEL = "qwen2.5:7b"
        mock_settings.MAX_WORKERS = 1

        # Step 2: Verify main() runs without raising exceptions
        main()
