# ADR-001: Three-Context Bounded Architecture for ISB

**Status:** Accepted
**Date:** 2026-05-21
**Decision Makers:** Lead Architect, High-Performance Implementer

## Context

The Intelligent Second Brain (ISB) compiles structured knowledge vaults from media sources. The operations required for this process span three separate domains of concern:
1. Media interaction and download (highly dependent on external network libraries and scrapers like `yt-dlp`).
2. Audio processing and speech transcription (highly compute-intensive, requiring GPU/CPU model inference via Whisper).
3. Knowledge graph compilation and markdown synthesis (highly language-model reliant, consuming token generation APIs like Ollama/qwen2.5).

Each stage operates under different throughput constraints, requires different systems dependencies, and has distinct failure modes (e.g. download rate-limiting, VRAM exhaustion during concurrent whisper/LLM runs, and schema violations by the LLM).

## Decision

We will decompose the application into three Bounded Contexts (**Ingestion**, **Transcription**, and **Knowledge**) coupled through an in-memory thread-safe **EventBus** using Domain Events (`AudioExtracted`, `TranscriptionCompleted`, `KnowledgeSynthesized`). 

- Decouple external IDs using an internal `ContentId` (UUIDv4) mapped inside the Ingestion ACL database (SQLite).
- Enforce the **Schema Layer** programmatically via Pydantic V2 schemas parsed directly from LLM structured JSON output.
- Enforce serialization of transcription and LLM inference to prevent VRAM OOM on machines with limited hardware (6GB VRAM).

## Consequences

### Positive
- **High Cohesion**: Each context is a pure hexagonal module managing its own domain models and Ports.
- **Resilience**: Failures at any stage are captured and marked as `FAILED` in the SQLite manifest, allowing clean idempotent retries without re-downloading audio tracks or re-running transcription.
- **Decoupling**: Modifying the extraction method (e.g. adding Local folder watch folders or podcast RSS support) does not affect transcription or synthesis logic.

### Negative
- Initial boilerplate is higher due to port definitions and translation mapping in adapters.
- Internal events add tracing complexity.

### Neutral
- An in-memory queue/EventBus is sufficient for version 0.1, but makes the codebase microservices-ready.

## Compliance

- [x] Hexagonal Architecture layers respected
- [x] No framework dependencies in Domain layer
- [x] Tests strategy defined (Red-Green-Refactor tests mirrored in `tests/`)
- [x] Observability plan included (status manifestation in SQLite registry)
- [x] Resource constraints (6GB VRAM) addressed by sequential pipeline configuration

## References

- Project layout guidance: `references/project_layout.md`
- Ubiquitous Language: `docs/GLOSSARY.md`
