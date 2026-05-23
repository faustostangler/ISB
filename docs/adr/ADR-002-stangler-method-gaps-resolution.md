# ADR-002: Stangler Method Gaps Resolution

**Status:** Proposed
**Date:** 2026-05-23
**Decision Makers:** Lead Architect, High-Performance Implementer

## Context

The initial implementation of the Intelligent Second Brain (ISB) codebase introduced three bounded contexts (Ingestion, Transcription, and Knowledge) as a modular monolith. However, a systematic code analysis reveals several gaps when measured against the strict requirements of the Doctor Stangler Method:

1. **Primitive Obsession (Domain Violation):** Domain Entity and Use Case signatures (such as `MediaEpisode` and `MediaSource`) consume primitive types (`str`, `int`, `datetime`) directly for attributes carrying business meaning (e.g. `external_id`, `title`, `duration_seconds`, `url`).
2. **Deferred Validation (Entity Soundness Violation):** Domain Entities (like `MediaEpisode`, `MediaSource`, `Transcript`, `RawNote`, and `WikiArticle`) are structured as plain `@dataclass` without constructor validation, allowing them to exist in invalid states (e.g. empty strings, negative durations, malformed dates).
3. **Telemetry & Observability Gaps:** The system lacks Sentry integration for error and crash tracking, and the generative AI pipeline in the Knowledge context does not trace its structured LLM synthesis runs via Langfuse telemetry (missing trace taxonomy, span hierarchy, prompt versioning, and evaluation metrics).
4. **Distributed Event Safety (Outbox Pattern):** The `SQLiteManifestAdapter` tracks status transitions in the SQLite database but does not persist domain events transactionally (failing to support the Transactional Outbox Pattern for eventual consistency).

To establish compliance with the five pillars of the Doctor Stangler Method, these design issues must be resolved at the architecture level.

## Decision

We will refactor the codebase to eliminate these architectural gaps by:
1. **Introducing Enriched Value Objects:** Defining dedicated Value Object types for all business concepts (e.g. `ExternalId`, `EpisodeTitle`, `DurationSeconds`, `SourceUrl`, `LanguageCode`, `ArticleTag`) that validate their structure upon instantiation.
2. **Converting Entities to Pydantic BaseModel:** Refactoring domain entities to inherit from Pydantic V2 `BaseModel`, enforcing strict invariants at construction time to guarantee entity soundness.
3. **Adding Observability Adapters:** Wires Sentry initialization inside the Composition Root (`main.py`) and instrumentation for Langfuse LLM tracing inside `OllamaLLMAdapter` using trace IDs, session IDs, and evaluation score metadata.
4. **Designing a SQLite-based Transactional Outbox:** Adding an `outbox` table and outbox persistence mapping to the SQLite manifest schema, laying the foundation for atomic eventual consistency event relay.

## Consequences

### Positive
- **Design-Time Safety:** Value Objects and Pydantic validation prevent any invalid domain states from propagating, ensuring strict compliance with Hexagonal and DDD layers.
- **Robust Telemetry:** Sentry and Langfuse integration will capture real-time errors, latency, and hallucination/faithfulness scores for all generative AI synthesis runs.
- **Microservices Readiness:** The Transactional Outbox Pattern ensures events are reliably tracked along with entity status modifications.

### Negative
- **Increased Boilerplate:** Added files for custom value objects and Pydantic field definitions.
- **Mappers Effort:** Adapters (e.g., `YtDlpExtractorAdapter`, `WhisperTranscriberAdapter`, `ObsidianVaultAdapter`) must map between raw database/library structures and enriched domain types.

### Neutral
- No change to the underlying core logic of yt-dlp downloading or Whisper transcription execution.

## Alternatives Considered

### Alternative A: Native Python Dataclasses with `__post_init__` Validation
- **Pros:** Avoids external framework dependency (Pydantic) in the Domain layer.
- **Cons:** Dataclasses require manually writing custom type coercion and serialization mappers for JSON/frontmatter exports.
- **Why rejected:** The project already uses Pydantic in the Domain layer for `NoteMetadata` and `SynthesizedArticleSchema`. Converting entities to Pydantic is much more cohesive with the existing code style.

### Alternative B: Direct API Observability Logs
- **Pros:** No extra telemetry dependencies (Sentry, Langfuse).
- **Cons:** Fails to provide trace hierarchies, prompt version tracking, and structured evaluation scorecard visualization.
- **Why rejected:** Telemetry and Langfuse Evals are non-negotiable observabilities under the Doctor Stangler Method for AI workflows.

## Compliance

- [ ] Hexagonal Architecture layers respected
- [ ] No framework dependencies in Domain layer (except Pydantic validation)
- [ ] Tests strategy defined (RGR unit tests checking Value Object boundaries and Entity invariants)
- [ ] Observability plan included (Sentry and Langfuse tracing)
- [ ] LGPD/Security implications assessed (Redaction of potential URLs/usernames in logs)

## References

- Standard project layout: `references/project_layout.md`
- Core Method specification: `references/37-DevOps, DDD, TDD, ADRs, Code.md`
