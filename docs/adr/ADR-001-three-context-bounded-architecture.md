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

## Cross-Context State Strategy

### 7a. Boundary Violations Check
- **Check:** Does any module read from or write directly to another module's persistence layer?
- **Answer:** No. Each context (Ingestion, Transcription, Knowledge) communicates exclusively via domain events published to the in-memory `EventBus`. The `SQLiteManifestAdapter` acts as a shared database registry for idempotency, but accesses are strictly segregated via context-specific port interfaces (`ManifestPort`, `TranscriptionManifestPort`, `KnowledgeManifestPort`), preventing cross-module query coupling.

### 7b. Consistency Model
- **Model:** Eventual Consistency (Async Events).
- **Details:** State transitions are coordinated asynchronously using domain events (`AudioExtracted` and `TranscriptionCompleted`). A transactional `outbox` table in SQLite registers all generated events in the same database transaction as status updates, preventing lost events upon pipeline crashes.

### 7c. Failure Modes & Compensation (Saga Pattern)
- **Coordination:** Choreography style (each context reacts to events and handles failure compensation autonomously).
- **Compensation Events:**
  - If Transcription fails, `TranscribeAudioUseCase` marks the content status as `FAILED` in the SQLite registry. This allows Ingestion to retry processing on subsequent scans.
  - If LLM Synthesis fails, `SynthesizeWikiUseCase` marks the status as `FAILED` in the SQLite registry. Compensation logic allows the system to retry synthesis of existing transcription files on disk without needing to re-transcribe or re-download the audio.
- **Maximum Acceptable Compensation Delay:** 10 minutes (SLA).

## Compliance

- [x] Hexagonal Architecture layers respected
- [x] No framework dependencies in Domain layer
- [x] Tests strategy defined (Red-Green-Refactor tests mirrored in `tests/`)
- [x] Observability plan included (status manifestation in SQLite registry)
- [x] Resource constraints (6GB VRAM) addressed by sequential pipeline configuration
- [x] Cross-Context State Strategy section complete and verified

## References

- Project layout guidance: `references/project_layout.md`
- Ubiquitous Language: `docs/GLOSSARY.md`
