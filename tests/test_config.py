import pytest
from pydantic import ValidationError
from isb.config import Settings


def test_settings_validation_success(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that valid configuration environment variables initialize settings successfully."""
    monkeypatch.setenv("ENV", "production")
    monkeypatch.setenv("DEBUG", "false")
    monkeypatch.setenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/db")
    monkeypatch.setenv("REDIS_URL", "redis://localhost:6379/0")

    settings = Settings()
    assert settings.ENV == "production"
    assert settings.DEBUG is False
    assert str(settings.DATABASE_URL) == "postgresql://user:pass@localhost:5432/db"
    assert str(settings.REDIS_URL) == "redis://localhost:6379/0"


def test_settings_validation_missing_database_url(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that missing DATABASE_URL raises ValidationError."""
    monkeypatch.setenv("ENV", "production")
    monkeypatch.setenv("DEBUG", "false")
    monkeypatch.setenv("REDIS_URL", "redis://localhost:6379/0")
    monkeypatch.delenv("DATABASE_URL", raising=False)

    with pytest.raises(ValidationError) as exc_info:
        Settings()

    assert "DATABASE_URL" in str(exc_info.value)
    assert "Field required" in str(exc_info.value)


def test_settings_validation_missing_redis_url(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that missing REDIS_URL raises ValidationError."""
    monkeypatch.setenv("ENV", "production")
    monkeypatch.setenv("DEBUG", "false")
    monkeypatch.setenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/db")
    monkeypatch.delenv("REDIS_URL", raising=False)

    with pytest.raises(ValidationError) as exc_info:
        Settings()

    assert "REDIS_URL" in str(exc_info.value)
    assert "Field required" in str(exc_info.value)


def test_settings_validation_malformed_urls(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that malformed connection DSNs raise ValidationError."""
    monkeypatch.setenv("ENV", "production")
    monkeypatch.setenv("DEBUG", "false")
    monkeypatch.setenv("DATABASE_URL", "not-a-valid-dsn")
    monkeypatch.setenv("REDIS_URL", "not-a-valid-redis-dsn")

    with pytest.raises(ValidationError) as exc_info:
        Settings()

    assert "DATABASE_URL" in str(exc_info.value)
    assert "REDIS_URL" in str(exc_info.value)
