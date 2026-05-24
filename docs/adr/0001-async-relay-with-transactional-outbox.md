# 0001: Async Relay with Transactional Outbox and Event-Driven Context Decoupling

**Status**: Accepted  
**Date**: 2026-05-23  

We decided to refactor the Modular Monolith's inter-context integration to guarantee strict physical boundaries and error isolation.

Specifically:
1. **Context-Owned Manifests**: We are replacing the shared SQLite database adapter with segregated context-specific SQLite databases (`ingestion.db`, `transcription.db`, `knowledge.db`).
2. **Context-Local Lifecycles**: Each context will define and manage its own localized status enum. Global status updates in Ingestion are driven strictly by event notifications.
3. **Decoupled Event Schemas (Option C & B)**: Events will carry inline payloads for data (such as serialized transcripts and segment lists) and external storage/stream references for large files (such as audio streams) rather than local filesystem path objects.
   - **Type Coercion Safety**: To prevent breaking existing Ingestion callers, `AudioExtracted` will automatically coerce `pathlib.Path` instances into `file://` URIs.
   - **ML Outlier Self-Clamping**: `SegmentPayload` will automatically clamp ML-inferred confidence scores to `[0.0, 1.0]` and timestamps to `>= 0.0` to prevent floating-point rounding errors from crashing the pipeline.
4. **Context-Encapsulated Event Adapters**: Event subscriptions are defined as incoming/primary adapters inside each context's infrastructure layer, keeping the Composition Root (`main.py`) clean.
5. **Independent Retry Lifecycle**: Each context exposes independent CLI retry commands (e.g. `isb transcribe-failed`) scanning its local database for error recovery rather than relying on a global pipeline rerun. These retries are encapsulated as Application Use Cases (`RetryFailedTranscriptionsUseCase` and `RetryFailedSynthesesUseCase`), keeping CLI presentation adapters humble.
6. **Asynchronous Thread-Pool Event Dispatching (Option B & C)**: The `EventBus` will dispatch events concurrently.
   - **Injected TaskExecutor Port**: To ensure 100% deterministic testability, the `EventBus` accepts an injected `TaskExecutor` interface. In unit tests, we inject an `InlineTaskExecutor` (synchronous execution); in production, we inject a thread-pool-backed `ThreadPoolTaskExecutor`.
   - **Error Isolation & Telemetry**: Subscriber exceptions will be caught, logged, and reported to Sentry dynamically via import guards, preventing downstream failures from bubble-crashing the upstream publishers.

## Considered Options

* **Option A (Shared Monolithic DB & Sequential Dispatch)**: High DB-level coupling and temporal execution dependency. Rejected because it violates database-per-service microservice readiness.
* **Option C (Saga Orchestration)**: Centralized workflow orchestrator managing state transitions. Rejected because it introduces accidental complexity for a simple three-step linear pipeline.

## Consequences

* **Boundary Soundness**: Zero shared database tables or filesystem paths between contexts.
* **Resilience**: Crashes in Transcription or Knowledge cannot bubble up to crash Ingestion, and failed items can be recovered independently.
* **Increased Boilerplate**: Requires mapping multiple local database schemas and writing localized status schemas.
