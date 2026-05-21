import pytest
from pydantic import ValidationError
from isb.config import Settings
from pathlib import Path

def test_settings_validation_success(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that valid configuration environment variables initialize settings successfully with defaults."""
    # Setup optional legacy database envs
    monkeypatch.setenv("ENV", "production")
    monkeypatch.setenv("DEBUG", "false")
    monkeypatch.setenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/db")
    monkeypatch.setenv("REDIS_URL", "redis://localhost:6379/0")
    
    # Configure custom paths
    monkeypatch.setenv("MEDIA_DATA_DIR", "/tmp/media")
    monkeypatch.setenv("MANIFEST_DB_PATH", "/tmp/manifest.db")
    monkeypatch.setenv("WHISPER_MODEL", "small")
    monkeypatch.setenv("WHISPER_LANGUAGES", "pt,en")
    monkeypatch.setenv("OLLAMA_BASE_URL", "http://ollama-host:11434")
    monkeypatch.setenv("OLLAMA_MODEL", "qwen2.5:7b-instruct")
    monkeypatch.setenv("OBSIDIAN_VAULT_PATH", "/tmp/vault")
    monkeypatch.setenv("SOURCES_CONFIG_PATH", "/tmp/sources.yaml")
    monkeypatch.setenv("MAX_WORKERS", "4")

    settings = Settings()
    
    assert settings.ENV == "production"
    assert settings.DEBUG is False
    assert str(settings.DATABASE_URL) == "postgresql://user:pass@localhost:5432/db"
    assert str(settings.REDIS_URL) == "redis://localhost:6379/0"
    assert settings.MEDIA_DATA_DIR == Path("/tmp/media")
    assert settings.MANIFEST_DB_PATH == Path("/tmp/manifest.db")
    assert settings.WHISPER_MODEL == "small"
    assert settings.WHISPER_LANGUAGES == ["pt", "en"]
    assert settings.OLLAMA_BASE_URL == "http://ollama-host:11434"
    assert settings.OLLAMA_MODEL == "qwen2.5:7b-instruct"
    assert settings.OBSIDIAN_VAULT_PATH == Path("/tmp/vault")
    assert settings.SOURCES_CONFIG_PATH == Path("/tmp/sources.yaml")
    assert settings.MAX_WORKERS == 4

def test_settings_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test the default fallback values for non-required settings."""
    # Ensure no environment variables interfere
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.delenv("REDIS_URL", raising=False)
    monkeypatch.delenv("MEDIA_DATA_DIR", raising=False)
    monkeypatch.delenv("MANIFEST_DB_PATH", raising=False)
    monkeypatch.delenv("WHISPER_MODEL", raising=False)
    monkeypatch.delenv("WHISPER_LANGUAGES", raising=False)
    monkeypatch.delenv("OLLAMA_BASE_URL", raising=False)
    monkeypatch.delenv("OLLAMA_MODEL", raising=False)
    monkeypatch.delenv("OBSIDIAN_VAULT_PATH", raising=False)
    monkeypatch.delenv("SOURCES_CONFIG_PATH", raising=False)
    monkeypatch.delenv("MAX_WORKERS", raising=False)

    settings = Settings()
    
    assert settings.ENV == "development"
    assert settings.DEBUG is False
    assert settings.DATABASE_URL is None
    assert settings.REDIS_URL is None
    assert settings.MEDIA_DATA_DIR == Path("./data/media")
    assert settings.MANIFEST_DB_PATH == Path("./data/manifest.db")
    assert settings.WHISPER_MODEL == "base"
    assert settings.WHISPER_LANGUAGES == ["pt", "en", "es"]
    assert settings.OLLAMA_BASE_URL == "http://localhost:11434"
    assert settings.OLLAMA_MODEL == "qwen2.5:7b"
    assert settings.OBSIDIAN_VAULT_PATH == Path("./vault")
    assert settings.SOURCES_CONFIG_PATH == Path("./config/sources.yaml")
    assert settings.MAX_WORKERS == 1

def test_settings_validation_malformed_urls(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that malformed connection DSNs raise ValidationError."""
    monkeypatch.setenv("DATABASE_URL", "not-a-valid-dsn")
    monkeypatch.setenv("REDIS_URL", "not-a-valid-redis-dsn")

    with pytest.raises(ValidationError) as exc_info:
        Settings()

    assert "DATABASE_URL" in str(exc_info.value)
    assert "REDIS_URL" in str(exc_info.value)
