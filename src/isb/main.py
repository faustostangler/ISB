"""Composition Root — Wires all bounded contexts and drives the ISB pipeline.

This module is the single entry point that connects all Hexagonal Architecture
adapters (secondary) to the application use cases (ports). It follows the
12-Factor App principle: all configuration is injected from environment variables
via Pydantic Settings, and all dependencies are wired here and only here.

Pipeline flow:
  1. Load MediaSource definitions from YAML configuration file.
  2. Instantiate concrete infrastructure adapters (SQLite, yt-dlp, Whisper, Ollama, Obsidian).
  3. Wire event subscriptions: AudioExtracted → TranscribeAudio → ProcessTranscript → SynthesizeWiki.
  4. Execute sources concurrently using ThreadPoolExecutor (bounded by MAX_WORKERS setting).
"""
import json
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml
from datetime import datetime, timezone

from isb.config import settings
from isb.ingestion.application.use_cases import ExtractAudioUseCase
from isb.ingestion.domain.entities import MediaSource
from isb.ingestion.infrastructure.adapters import YtDlpExtractorAdapter
from isb.knowledge.application.use_cases import ProcessTranscriptUseCase, SynthesizeWikiUseCase
from isb.knowledge.domain.value_objects import NoteMetadata
from isb.knowledge.infrastructure.adapters import ObsidianVaultAdapter, OllamaLLMAdapter
from isb.shared_kernel.events import AudioExtracted, EventBus, TranscriptionCompleted
from isb.shared_kernel.infrastructure.manifest import SQLiteManifestAdapter
from isb.shared_kernel.types import ContentId
from isb.transcription.application.use_cases import TranscribeAudioUseCase
from isb.transcription.infrastructure.adapters import WhisperTranscriberAdapter

# Step 1: Initialize the module-level logger.
# Why: Every step of the pipeline emits structured log records for operational
# observability (Prometheus Loki / Grafana ingestion at a later phase).
logging.basicConfig(level=logging.INFO if not settings.DEBUG else logging.DEBUG)
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Helper: YAML source loader
# ---------------------------------------------------------------------------

def load_sources_from_yaml(config_path: Path) -> list[MediaSource]:
    """Parse the sources YAML config file and return a list of MediaSource entities.

    Each entry in the ``sources`` list is mapped to a ``MediaSource`` domain
    entity using only the fields the entity cares about (id, name, url).
    Extra fields such as ``type``, ``category``, and ``tags`` are accepted but
    silently ignored by the entity — they live in the YAML for operator
    readability and future enrichment without breaking the domain boundary.

    Args:
        config_path: Absolute or relative ``Path`` to the ``sources.yaml`` file.

    Returns:
        A list of ``MediaSource`` domain entities (empty list if ``sources``
        key is absent or empty).
    """
    # Step 1: Read raw YAML bytes from the configuration file on the filesystem.
    # Why: We keep YAML parsing at the infrastructure boundary (here) so the
    # domain entities never depend on PyYAML — a classic Hexagonal ACL pattern.
    raw = yaml.safe_load(config_path.read_text(encoding="utf-8"))

    # Step 2: Extract the ``sources`` list; default to empty list if key is missing.
    # Why: A missing ``sources`` key should not crash the pipeline — it simply
    # means there is nothing to process on this run (valid operational state).
    entries: list[dict] = raw.get("sources") or []

    # Step 3: Map each YAML entry dict to a MediaSource domain entity.
    # Why: We translate at the boundary so downstream code is always typed and
    # never operates on raw dicts, preserving domain integrity.
    sources: list[MediaSource] = []
    for entry in entries:
        source = MediaSource(
            source_id=entry["id"],
            name=entry["name"],
            url=entry["url"],
        )
        sources.append(source)

    logger.info("Loaded %d media source(s) from %s", len(sources), config_path)
    return sources


# ---------------------------------------------------------------------------
# Composition Root: bootstrap_composition_root
# ---------------------------------------------------------------------------

def bootstrap_composition_root() -> tuple[EventBus, ExtractAudioUseCase]:
    """Instantiate all concrete adapters and wire them to their use cases.

    This function is the **only** place in the entire codebase that knows which
    concrete class implements which port. It wires:

      - ``SQLiteManifestAdapter`` → ``ManifestPort`` / ``TranscriptionManifestPort``
        / ``KnowledgeManifestPort``  (shared across all three contexts)
      - ``YtDlpExtractorAdapter``  → ``MediaExtractorPort``
      - ``WhisperTranscriberAdapter`` → ``TranscriberPort``
      - ``OllamaLLMAdapter``       → ``LLMPort``
      - ``ObsidianVaultAdapter``   → ``VaultPort``

    Event subscriptions follow strict ordering:
      ``AudioExtracted``          → ``TranscribeAudioUseCase.execute``
      ``TranscriptionCompleted``  → ``ProcessTranscriptUseCase.execute``

    Returns:
        A tuple of ``(EventBus, ExtractAudioUseCase)`` so the caller
        (``run_pipeline``) can drive the pipeline without knowing the internal
        wiring details.
    """
    # Step 1: Instantiate the shared EventBus.
    # Why: A single EventBus instance is shared across all contexts so that events
    # published by Ingestion are received by Transcription, and events published
    # by Transcription are received by Knowledge — without any direct import coupling.
    event_bus = EventBus()

    # Step 2: Instantiate the shared SQLite manifest adapter.
    # Why: A single adapter instance manages the processing status across all
    # three bounded contexts (Ingestion, Transcription, Knowledge).  This mirrors
    # the pattern of a shared database in a modular monolith while remaining
    # replaceable with a microservice call at a later phase.
    manifest = SQLiteManifestAdapter(db_path=settings.MANIFEST_DB_PATH)

    # Step 3: Instantiate the Ingestion infrastructure adapter (yt-dlp).
    # Why: YtDlpExtractorAdapter implements MediaExtractorPort.  Injecting it
    # here keeps the use case decoupled from yt-dlp at the domain level.
    extractor = YtDlpExtractorAdapter(download_dir=settings.MEDIA_DATA_DIR)

    # Step 4: Instantiate the Transcription infrastructure adapter (Whisper).
    # Why: WhisperTranscriberAdapter implements TranscriberPort.  The Whisper
    # model size comes from settings to allow hardware-appropriate overrides
    # without touching source code (12-Factor App, Env > Code).
    transcriber = WhisperTranscriberAdapter(
        cache_dir=settings.MEDIA_DATA_DIR,
        model_name=settings.WHISPER_MODEL,
    )

    # Step 5: Instantiate the Knowledge infrastructure adapters (Ollama + Obsidian).
    # Why: OllamaLLMAdapter implements LLMPort; ObsidianVaultAdapter implements
    # VaultPort.  Both communicate only with the outside world (HTTP + filesystem)
    # and are replaced by doubles in tests — the ports guarantee the contracts.
    llm = OllamaLLMAdapter(
        base_url=settings.OLLAMA_BASE_URL,
        model_name=settings.OLLAMA_MODEL,
    )
    vault = ObsidianVaultAdapter(vault_path=settings.OBSIDIAN_VAULT_PATH)

    # Step 6: Instantiate the three application use cases, injecting their ports.
    # Why: Constructor injection (not service locator) keeps each use case testable
    # in isolation — swap any adapter double without touching the use case class.
    synthesize_use_case = SynthesizeWikiUseCase(
        llm_port=llm,
        vault_port=vault,
        manifest_port=manifest,
        event_bus=event_bus,
    )
    process_use_case = ProcessTranscriptUseCase(
        vault_port=vault,
        manifest_port=manifest,
        synthesize_use_case=synthesize_use_case,
    )
    transcribe_use_case = TranscribeAudioUseCase(
        transcriber_port=transcriber,
        manifest_port=manifest,
        event_bus=event_bus,
    )
    extract_use_case = ExtractAudioUseCase(
        extractor_port=extractor,
        manifest_port=manifest,
        event_bus=event_bus,
    )

    # Step 7: Subscribe event handlers to bridge Ingestion → Transcription.
    # Why: The EventBus subscription is the *only* coupling between the Ingestion
    # and Transcription bounded contexts.  When Ingestion publishes AudioExtracted,
    # this handler fires and drives the transcription pipeline — no direct import
    # or method call from Ingestion into Transcription exists.
    def _on_audio_extracted(event: AudioExtracted) -> None:
        """Handle AudioExtracted event: drive Whisper transcription."""
        # Step 7a: Log the incoming event for pipeline tracing.
        logger.info(
            "AudioExtracted event received for ContentId %s — starting transcription.",
            event.content_id,
        )
        # Step 7b: Extract language hint from event metadata if provided.
        # Why: yt-dlp metadata may include a language code; passing it to Whisper
        # reduces auto-detection cost on multilingual sources.
        language_hint: str | None = event.metadata.get("language")

        # Step 7c: Execute the transcription use case with the audio file path.
        transcribe_use_case.execute(
            content_id=event.content_id,
            audio_path=event.audio_path,
            language_hint=language_hint,
        )

    # Step 8: Subscribe event handlers to bridge Transcription → Knowledge.
    # Why: Same pattern as Step 7 — TranscriptionCompleted is the only coupling
    # point between the Transcription and Knowledge bounded contexts.
    def _on_transcription_completed(event: TranscriptionCompleted) -> None:
        """Handle TranscriptionCompleted event: drive Knowledge synthesis."""
        # Step 8a: Log the incoming event for pipeline tracing.
        logger.info(
            "TranscriptionCompleted event received for ContentId %s — starting synthesis.",
            event.content_id,
        )

        # Step 8b: Load the verbatim transcript text from the JSON file on disk.
        # Why: The Transcription adapter persists the full text to a sibling JSON
        # file (audio_path.with_suffix(".json")).  We read it here at the boundary
        # so the Knowledge use case receives a plain string — not a file path.
        transcript_path: Path = event.transcript_path
        transcript_text: str = ""
        if transcript_path.exists():
            raw_json = json.loads(transcript_path.read_text(encoding="utf-8"))
            # ACL: translate the raw dict produced by the Transcription adapter into
            # the string the Knowledge use case expects.
            transcript_text = raw_json.get("text", "")

        # Step 8c: Extract episode title and source metadata from the event payload.
        # Why: AudioExtracted metadata is carried forward via the content_id correlation.
        # The Transcription event includes its own metadata; we fall back to sensible
        # defaults to keep the pipeline resilient against partial metadata.
        title: str = event.metadata.get("title", f"Untitled — {event.content_id}")
        source_url: str = event.metadata.get("source_url", "")
        channel_name: str = event.metadata.get("channel_name", "")
        category: str = event.metadata.get("category", "")
        tags: list[str] = event.metadata.get("tags", [])

        # Step 8d: Parse published_at from ISO string to timezone-aware datetime.
        published_at_str: str | None = event.metadata.get("published_at")
        if published_at_str:
            try:
                published_at = datetime.fromisoformat(published_at_str)
            except ValueError:
                # Exception recovery: fallback to now() if the string is malformed.
                published_at = datetime.now(timezone.utc)
        else:
            published_at = datetime.now(timezone.utc)

        # Step 8e: Build the NoteMetadata value object for the Knowledge context.
        metadata = NoteMetadata(
            source_url=source_url,
            channel_name=channel_name,
            published_at=published_at,
            processed_at=datetime.now(timezone.utc),
            category=category,
            tags=tags,
        )

        # Step 8f: Execute the process transcript use case.
        process_use_case.execute(
            content_id=event.content_id,
            title=title,
            transcript_text=transcript_text,
            metadata=metadata,
        )

    # Step 9: Register the handler functions on the shared EventBus.
    # Why: Subscriptions happen here — after all use cases are built — so that
    # there is no risk of an event firing before its handler is ready.
    event_bus.subscribe(AudioExtracted, _on_audio_extracted)
    event_bus.subscribe(TranscriptionCompleted, _on_transcription_completed)

    logger.info("Composition root bootstrapped successfully.")
    return event_bus, extract_use_case


# ---------------------------------------------------------------------------
# Pipeline runner
# ---------------------------------------------------------------------------

def run_pipeline() -> None:
    """Load sources and execute the extraction pipeline concurrently.

    Uses a ``ThreadPoolExecutor`` bounded by ``settings.MAX_WORKERS`` to process
    multiple media sources in parallel.  In development (``MAX_WORKERS=1``) this
    degenerates to sequential execution — safe for debugging without sacrificing
    the concurrent design that scales in production.

    Each source is processed by ``ExtractAudioUseCase.execute``.  The use case
    internally publishes ``AudioExtracted`` events that trigger transcription and
    synthesis through the EventBus subscriptions registered in
    ``bootstrap_composition_root``.
    """
    # Step 1: Load configured media sources from the YAML configuration file.
    # Why: Sources are operator-controlled; reading them at runtime (not import
    # time) means operators can change the file without restarting the process.
    sources = load_sources_from_yaml(settings.SOURCES_CONFIG_PATH)

    if not sources:
        # Step 2: Short-circuit cleanly when there are no sources to process.
        # Why: Avoids spinning up a thread pool for zero work — KISS principle.
        logger.info("No media sources configured. Pipeline run completed with nothing to do.")
        return

    # Step 3: Bootstrap the wired dependency graph once per pipeline run.
    # Why: A single bootstrap call builds all adapters and subscriptions before
    # any concurrent work starts, guaranteeing the EventBus is fully wired.
    _event_bus, extract_use_case = bootstrap_composition_root()

    # Step 4: Submit each source to the thread pool for concurrent extraction.
    # Why: ThreadPoolExecutor enforces the MAX_WORKERS ceiling so local hardware
    # is never saturated.  as_completed() drains results as they arrive rather
    # than waiting for the slowest source to finish.
    logger.info(
        "Starting pipeline for %d source(s) with max_workers=%d.",
        len(sources),
        settings.MAX_WORKERS,
    )
    with ThreadPoolExecutor(max_workers=settings.MAX_WORKERS) as pool:
        # Step 5: Map each source to a future representing its extraction work.
        future_to_source = {
            pool.submit(extract_use_case.execute, source): source
            for source in sources
        }

        # Step 6: Drain futures as they complete to log results and surface errors.
        # Why: Consuming futures via as_completed() prevents silent failures and
        # ensures that one source's exception does not block the others.
        for future in as_completed(future_to_source):
            source = future_to_source[future]
            try:
                episodes = future.result()
                logger.info(
                    "Source '%s' processed successfully: %d episode(s).",
                    source.name,
                    len(episodes),
                )
            except Exception:
                # ACL: Exceptions from adapters (network, disk, Whisper OOM) are
                # caught here so one failing source does not abort the entire run.
                logger.exception(
                    "Source '%s' failed during pipeline execution.", source.name
                )


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

def main() -> None:
    """Composition Root entry point: invokes the full pipeline run.

    Designed to be called by the CLI (``uv run isb``) or the Docker CMD.
    All configuration is resolved via Pydantic Settings before this call returns.
    """
    # Step 1: Execute the run_pipeline handler which drives end-to-end processing.
    run_pipeline()


if __name__ == "__main__":
    # Step 1: Guard allows the module to be run directly during local development.
    # In production, entry is via ``uv run isb`` defined in pyproject.toml.
    main()
