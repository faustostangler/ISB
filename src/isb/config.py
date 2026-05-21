from pydantic import Field, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings validated via Pydantic.

    Centralized configuration class following fail-fast principles on startup.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    ENV: str = Field(
        default="development",
        description="Current execution environment (e.g., development, testing, production)",
    )
    DEBUG: bool = Field(
        default=False,
        description="Debug mode toggle for detailed logs and traces",
    )
    DATABASE_URL: PostgresDsn = Field(
        ...,
        description="PostgreSQL database connection DSN",
    )
    REDIS_URL: RedisDsn = Field(
        ...,
        description="Redis connection DSN",
    )


# Trigger validation on module load to satisfy fail-fast requirements
settings = Settings()
