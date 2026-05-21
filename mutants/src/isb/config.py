from pathlib import Path
from typing import Any
from pydantic import BeforeValidator, Field, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource, SettingsConfigDict
from typing_extensions import Annotated
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore

def parse_languages(v: Any) -> list[str]:
    args = [v]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_parse_languages__mutmut_orig, x_parse_languages__mutmut_mutants, args, kwargs, None)

def x_parse_languages__mutmut_orig(v: Any) -> list[str]:
    """Parse comma-separated strings or list values into a list of strings."""
    if isinstance(v, str):
        return [lang.strip() for lang in v.split(",") if lang.strip()]
    if isinstance(v, list):
        return [str(lang).strip() for lang in v if str(lang).strip()]
    raise ValueError("Languages must be a comma-separated string or a list of strings")

def x_parse_languages__mutmut_1(v: Any) -> list[str]:
    """Parse comma-separated strings or list values into a list of strings."""
    if isinstance(v, str):
        return [lang.strip() for lang in v.split(None) if lang.strip()]
    if isinstance(v, list):
        return [str(lang).strip() for lang in v if str(lang).strip()]
    raise ValueError("Languages must be a comma-separated string or a list of strings")

def x_parse_languages__mutmut_2(v: Any) -> list[str]:
    """Parse comma-separated strings or list values into a list of strings."""
    if isinstance(v, str):
        return [lang.strip() for lang in v.split("XX,XX") if lang.strip()]
    if isinstance(v, list):
        return [str(lang).strip() for lang in v if str(lang).strip()]
    raise ValueError("Languages must be a comma-separated string or a list of strings")

def x_parse_languages__mutmut_3(v: Any) -> list[str]:
    """Parse comma-separated strings or list values into a list of strings."""
    if isinstance(v, str):
        return [lang.strip() for lang in v.split(",") if lang.strip()]
    if isinstance(v, list):
        return [str(None).strip() for lang in v if str(lang).strip()]
    raise ValueError("Languages must be a comma-separated string or a list of strings")

def x_parse_languages__mutmut_4(v: Any) -> list[str]:
    """Parse comma-separated strings or list values into a list of strings."""
    if isinstance(v, str):
        return [lang.strip() for lang in v.split(",") if lang.strip()]
    if isinstance(v, list):
        return [str(lang).strip() for lang in v if str(None).strip()]
    raise ValueError("Languages must be a comma-separated string or a list of strings")

def x_parse_languages__mutmut_5(v: Any) -> list[str]:
    """Parse comma-separated strings or list values into a list of strings."""
    if isinstance(v, str):
        return [lang.strip() for lang in v.split(",") if lang.strip()]
    if isinstance(v, list):
        return [str(lang).strip() for lang in v if str(lang).strip()]
    raise ValueError(None)

def x_parse_languages__mutmut_6(v: Any) -> list[str]:
    """Parse comma-separated strings or list values into a list of strings."""
    if isinstance(v, str):
        return [lang.strip() for lang in v.split(",") if lang.strip()]
    if isinstance(v, list):
        return [str(lang).strip() for lang in v if str(lang).strip()]
    raise ValueError("XXLanguages must be a comma-separated string or a list of stringsXX")

def x_parse_languages__mutmut_7(v: Any) -> list[str]:
    """Parse comma-separated strings or list values into a list of strings."""
    if isinstance(v, str):
        return [lang.strip() for lang in v.split(",") if lang.strip()]
    if isinstance(v, list):
        return [str(lang).strip() for lang in v if str(lang).strip()]
    raise ValueError("languages must be a comma-separated string or a list of strings")

def x_parse_languages__mutmut_8(v: Any) -> list[str]:
    """Parse comma-separated strings or list values into a list of strings."""
    if isinstance(v, str):
        return [lang.strip() for lang in v.split(",") if lang.strip()]
    if isinstance(v, list):
        return [str(lang).strip() for lang in v if str(lang).strip()]
    raise ValueError("LANGUAGES MUST BE A COMMA-SEPARATED STRING OR A LIST OF STRINGS")

x_parse_languages__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_parse_languages__mutmut_1': x_parse_languages__mutmut_1, 
    'x_parse_languages__mutmut_2': x_parse_languages__mutmut_2, 
    'x_parse_languages__mutmut_3': x_parse_languages__mutmut_3, 
    'x_parse_languages__mutmut_4': x_parse_languages__mutmut_4, 
    'x_parse_languages__mutmut_5': x_parse_languages__mutmut_5, 
    'x_parse_languages__mutmut_6': x_parse_languages__mutmut_6, 
    'x_parse_languages__mutmut_7': x_parse_languages__mutmut_7, 
    'x_parse_languages__mutmut_8': x_parse_languages__mutmut_8
}
x_parse_languages__mutmut_orig.__name__ = 'x_parse_languages'

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
