from pathlib import Path
from typing import Any
from pydantic import BeforeValidator, Field, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource, SettingsConfigDict
from typing_extensions import Annotated

def parse_languages(v: Any) -> list[str]:
    """Parse comma-separated strings or list values into a list of strings."""
    if isinstance(v, str):
        return [lang.strip() for lang in v.split(",") if lang.strip()]
    if isinstance(v, list):
        return [str(lang).strip() for lang in v if str(lang).strip()]
    raise ValueError("Languages must be a comma-separated string or a list of strings")

class Settings(BaseSettings):
    """Application settings validated via Pydantic.

    Centralized configuration class following fail-fast principles on startup.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        """Customize settings sources to allow fallback for complex env variables.

        Prevents JSONDecodeError when parsing comma-separated strings for lists.
        """
        def custom_decode(field_name: str, field: Any, value: Any) -> Any:
            try:
                import json
                return json.loads(value)
            except Exception:
                return value

        if hasattr(env_settings, "decode_complex_value"):
            env_settings.decode_complex_value = custom_decode  # type: ignore
        if hasattr(dotenv_settings, "decode_complex_value"):
            dotenv_settings.decode_complex_value = custom_decode  # type: ignore

        return init_settings, env_settings, dotenv_settings, file_secret_settings


    ENV: str = Field(
        default="development",
        description="Current execution environment (e.g., development, testing, production)",
    )
    DEBUG: bool = Field(
        default=False,
        description="Debug mode toggle for detailed logs and traces",
    )
    
    # Legacy connection DSNs made optional
    DATABASE_URL: PostgresDsn | None = Field(
        default=None,
        description="Optional PostgreSQL database connection DSN",
    )
    REDIS_URL: RedisDsn | None = Field(
        default=None,
        description="Optional Redis connection DSN",
    )

    # Ingestion Context
    MEDIA_DATA_DIR: Path = Field(
        default=Path("./data/media"),
        description="Directory to store extracted media (audio/metadata)",
    )
    MANIFEST_DB_PATH: Path = Field(
        default=Path("./data/manifest.db"),
        description="Path to the SQLite manifest DB for idempotency and status tracking",
    )

    # Transcription Context
    WHISPER_MODEL: str = Field(
        default="base",
        description="Whisper model size/name (e.g., base, small, medium, large-v3)",
    )
    WHISPER_LANGUAGES: Annotated[list[str], BeforeValidator(parse_languages)] = Field(
        default=["pt", "en", "es"],
        description="Prioritized list of language codes to try or use as Whisper hints",
    )

    # Knowledge Context
    OLLAMA_BASE_URL: str = Field(
        default="http://localhost:11434",
        description="Ollama API base endpoint",
    )
    OLLAMA_MODEL: str = Field(
        default="qwen2.5:7b",
        description="Local LLM model tag in Ollama",
    )
    OBSIDIAN_VAULT_PATH: Path = Field(
        default=Path("./vault"),
        description="Root path of the target Obsidian vault",
    )
    SOURCES_CONFIG_PATH: Path = Field(
        default=Path("./config/sources.yaml"),
        description="Path to the channels/videos sources YAML configuration",
    )

    # Execution/Concurrency Control
    MAX_WORKERS: int = Field(
        default=1,
        description="Maximum concurrent threads for the ingestion pipeline",
    )


# Trigger validation on module load to satisfy fail-fast requirements.
# If imported within tests, conftest.py overrides env variables to prevent crash.
settings = Settings()
