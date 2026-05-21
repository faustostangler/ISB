import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch
from isb.shared_kernel.types import ContentId
from isb.ingestion.domain.entities import MediaSource
from isb.main import main, load_sources_from_yaml, bootstrap_composition_root, run_pipeline

def test_load_sources_from_yaml_valid(tmp_path: Path) -> None:
    """Verify that load_sources_from_yaml parses media sources from config file correctly."""
    # Step 1: Create a temporary sources.yaml file
    config_file = tmp_path / "sources.yaml"
    config_content = """
sources:
  - id: test-source-1
    name: "Test Creator"
    url: "https://www.youtube.com/playlist?list=123"
    category: "AI"
    tags:
      - ml
"""
    config_file.write_text(config_content, encoding="utf-8")

    # Step 2: Invoke parsing helper function
    sources = load_sources_from_yaml(config_file)

    # Step 3: Validate outputs mapping to MediaSource entity list
    assert len(sources) == 1
    assert sources[0].source_id == "test-source-1"
    assert sources[0].name == "Test Creator"
    assert sources[0].url == "https://www.youtube.com/playlist?list=123"


def test_main_composition_orchestration(tmp_path: Path) -> None:
    """Verify that composition wiring propagates from loading sources to execution."""
    # Step 1: Mock configuration paths and parameters
    sources_yaml = tmp_path / "sources.yaml"
    sources_yaml.write_text("sources: []", encoding="utf-8")

    # Step 2: Patch config settings to use temporary vault and DB locations
    with patch("isb.main.settings") as mock_settings:
        mock_settings.SOURCES_CONFIG_PATH = sources_yaml
        mock_settings.MANIFEST_DB_PATH = tmp_path / "manifest.db"
        mock_settings.OBSIDIAN_VAULT_PATH = tmp_path / "vault"
        mock_settings.MEDIA_DATA_DIR = tmp_path / "media"
        mock_settings.MAX_WORKERS = 2

        # Step 3: Execute main composition root
        # Under skeleton mode, this should raise NotImplementedError.
        # Once implemented (green phase), it will process mock sources successfully.
        main()
