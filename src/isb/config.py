from pathlib import Path
from typing import Any
from pydantic import BeforeValidator, Field, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource, SettingsConfigDict
from typing_extensions import Annotated

def parse_languages(v: Any) -> list[str]:
    """Parse comma-separated strings or list values into a list of language codes.

    Args:
        v: The raw input language preference from environment configurations or default values.

    Returns:
        list[str]: A list of cleaned, non-empty language identifier strings.

    Raises:
        ValueError: If the input value cannot be coerced into a comma-separated string or list.
    """
    # Step 1: Check if input is a comma-separated string
    # We do this because environment variables are loaded as strings and need splitting
    if isinstance(v, str):
        # Split language codes by comma and strip extra whitespaces from each entry
        return [lang.strip() for lang in v.split(",") if lang.strip()]
        
    # Step 2: Check if input is already a list
    # We do this to support direct python configuration object initialization (e.g. in tests)
    if isinstance(v, list):
        # Convert each element to string and strip surrounding whitespaces
        return [str(lang).strip() for lang in v if str(lang).strip()]
        
    # Step 3: Raise ValueError for unsupported types to fail early
    # Enforces strict type consistency during the configuration phase
    raise ValueError("Languages must be a comma-separated string or a list of strings")


class Settings(BaseSettings):
    """System-wide configuration settings validated via Pydantic.

    This class serves as the single source of truth for configuration validation.
    It implements the fail-fast principle, ensuring invalid environment variables
    cause the system to crash on startup rather than failing unpredictably at runtime.
    """

    # Configure Pydantic Settings behavior to read from standard .env file
    # We ignore extra environment variables to avoid crash on unrelated OS env variables
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
        """Customize configuration loading precedence and data type conversion rules.

        We intercept complex types like comma-separated lists during env reading
        to prevent Pydantic from raising JSONDecodeError when parsing string list values.

        Args:
            settings_cls: The Settings class definition.
            init_settings: Settings passed directly via constructor arguments.
            env_settings: Settings loaded from OS environment variables.
            dotenv_settings: Settings loaded from the .env file.
            file_secret_settings: Settings loaded from container secrets files.

        Returns:
            tuple[PydanticBaseSettingsSource, ...]: Customized settings sources in order of priority.
        """
        # Step 1: Define a custom decoder function to try parsing JSON arrays
        def custom_decode(field_name: str, field: Any, value: Any) -> Any:
            try:
                import json
                # Attempt to parse values as JSON list or object (e.g., list of strings)
                return json.loads(value)
            except Exception:
                # If JSON loading fails, fallback to raw string (which can be validated by parse_languages)
                return value

        # Step 2: Inject the custom decoder into env and dotenv loaders
        # This shields Pydantic from crashing on standard comma-separated env values before validation
        if hasattr(env_settings, "decode_complex_value"):
            env_settings.decode_complex_value = custom_decode  # type: ignore
        if hasattr(dotenv_settings, "decode_complex_value"):
            dotenv_settings.decode_complex_value = custom_decode  # type: ignore

        # Step 3: Return the prioritized list of configuration sources
        return init_settings, env_settings, dotenv_settings, file_secret_settings


    # --- Global Settings ---
    ENV: str = Field(
        default="development",
        description="Current execution environment (e.g., development, testing, production)",
    )
    DEBUG: bool = Field(
        default=False,
        description="Debug mode toggle for detailed logs, traces, and developer tools",
    )
    
    # --- Legacy Connections ---
    # Kept optional to maintain compatibility with decentralized sqlite and local storage
    DATABASE_URL: PostgresDsn | None = Field(
        default=None,
        description="Optional PostgreSQL database connection DSN",
    )
    REDIS_URL: RedisDsn | None = Field(
        default=None,
        description="Optional Redis connection DSN",
    )

    # --- Ingestion Bounded Context ---
    MEDIA_DATA_DIR: Path = Field(
        default=Path("./data/media"),
        description="Directory to store extracted media (audio/metadata) on disk",
    )
    MANIFEST_DB_PATH: Path = Field(
        default=Path("./data/manifest.db"),
        description="Path to the SQLite manifest DB for idempotency and status tracking",
    )

    # --- Transcription Bounded Context ---
    WHISPER_MODEL: str = Field(
        default="base",
        description="Whisper speech-to-text model size/name (e.g., base, small, medium, large-v3)",
    )
    WHISPER_LANGUAGES: Annotated[list[str], BeforeValidator(parse_languages)] = Field(
        default=["pt", "en", "es"],
        description="Prioritized list of language codes to try or use as Whisper hints",
    )

    # --- Knowledge Bounded Context ---
    OLLAMA_BASE_URL: str = Field(
        default="http://localhost:11434",
        description="Ollama API base endpoint",
    )
    OLLAMA_MODEL: str = Field(
        default="qwen2.5:7b",
        description="Local LLM model tag in Ollama for second brain note synthesis",
    )
    OBSIDIAN_VAULT_PATH: Path = Field(
        default=Path("./vault"),
        description="Root path of the target Obsidian vault repository",
    )
    SOURCES_CONFIG_PATH: Path = Field(
        default=Path("./config/sources.yaml"),
        description="Path to the channels/videos sources YAML configuration",
    )

    # --- Execution/Concurrency Control ---
    MAX_WORKERS: int = Field(
        default=1,
        description="Maximum concurrent threads for the ingestion pipeline",
    )

    # --- Telemetry & Observability ---
    SENTRY_DSN: str | None = Field(
        default=None,
        description="Sentry crash reporting DSN",
    )
    LANGFUSE_PUBLIC_KEY: str | None = Field(
        default=None,
        description="Langfuse client public key",
    )
    LANGFUSE_SECRET_KEY: str | None = Field(
        default=None,
        description="Langfuse client secret key",
    )
    LANGFUSE_HOST: str = Field(
        default="https://cloud.langfuse.com",
        description="Langfuse API host endpoint",
    )


# Trigger validation on module load to satisfy fail-fast requirements.
# If imported within tests, conftest.py overrides env variables to prevent crash.
settings = Settings()
