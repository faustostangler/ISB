# SPEC-0001: Context Decoupling Test Specifications

This document defines the formal behavioral test specifications, boundary conditions, and testing strategies for the decoupled event-driven architecture established in ADR-0001.

---

## 1. Event Schema & Invariant Constraints

All domain events are messages that must remain structurally sound and valid upon instantiation.

### AudioExtracted Event
* **Description**: Emitted when Ingestion successfully extracts an audio track.
* **Invariants & Validation (Option B & Coercion)**:
  * `content_id`: Must be a valid `ContentId` UUID wrapper.
  * `audio_ref`: Must be a string representing a valid URI. The URI scheme must be one of: `file://`, `s3://`, or `https://`. Any other scheme or empty string must raise `ValueError`.
  * **Path Coercion**: If constructed with a `pathlib.Path` object instead of a string, the constructor must automatically coerce it to a local file URI (e.g. `path.as_uri()`, yielding `file:///absolute/path/to/file`).
  * `metadata`: Must be a dictionary.
* **Test Strategy (Unit)**:
  * Verify construction with a valid `file:///media/audio.wav` is accepted.
  * Assert that passing a `pathlib.Path("/media/audio.wav")` is coerced into `"file:///media/audio.wav"`.
  * Assert that constructing with a plain relative string like `"media/audio.wav"` (no schema) raises `ValueError`.

### TranscriptionCompleted Event
* **Description**: Emitted when Transcription completes speech-to-text processing.
* **Invariants & Validation (Option B & Self-Clamping)**:
  * `content_id`: Must be a valid `ContentId` UUID wrapper.
  * `transcript_payload`: Must be a Pydantic `TranscriptPayload` object containing:
    * `full_text`: Non-empty string.
    * `language`: Valid `LanguageCode` (2-5 characters, e.g. `pt`, `en`).
    * `model`: Valid `ModelName` (standard size name).
    * `duration_seconds`: Float >= 0.0.
    * `segments`: List of `SegmentPayload` models.
  * **ML Outlier Self-Clamping**:
    * `confidence` in `SegmentPayload` must be clamped to the range `[0.0, 1.0]`. If a value like `1.05` is provided, it is coerced to `1.0`. If `-0.02` is provided, it is coerced to `0.0`.
    * `start_seconds` and `end_seconds` must be clamped to `>= 0.0`.
    * `start_seconds` must be less than or equal to `end_seconds`. If `start_seconds > end_seconds`, raise `ValueError`.
* **Test Strategy (Unit)**:
  * Verify successful deserialization from a valid dictionary into `TranscriptPayload`.
  * Assert that a confidence score of `1.05` is clamped to `1.0` and `-0.01` to `0.0`.
  * Assert that timestamps are clamped to `>= 0.0`.
  * Assert that if `start_seconds > end_seconds`, it raises a `ValueError`.
  * Assert that an empty `full_text` in the payload raises a validation error.

---

## 2. Asynchronous EventBus & Executor Port

We decouple the EventBus routing logic from the execution model using an injected executor port.

### TaskExecutor Port (ABC)
* **Methods**:
  * `submit(fn: Callable[[], None]) -> None`: Submit a background task.
  * `shutdown(wait: bool = True) -> None`: Clean up execution resources.

### InlineTaskExecutor (Test Double)
* Runs all submitted tasks synchronously in the calling thread, propagating exceptions immediately.

### ThreadPoolTaskExecutor (Production Adapter)
* Runs submitted tasks in a background thread pool. Isolates thread exceptions.

### EventBus Specifications
* **Behavior 1: Subscription and Routing**:
  * Registering multiple handlers for the same event type executes all of them when published.
  * EventBus supports polymorphic dispatch (handlers subscribed to the base `DomainEvent` receive all subclass events).
* **Behavior 2: Error Isolation & Telemetry (Option A)**:
  * An exception raised by one handler must not prevent subsequent handlers from executing.
  * An exception raised in any handler must not bubble up to the publishing thread.
  * Exceptions caught in the safe-execution block are reported to Sentry dynamically via an `ImportError` guard block (checking if `sentry_sdk` is available).
* **Test Strategy (Unit)**:
  * Use `InlineTaskExecutor` to assert routing, subscriber matching, and polymorphic dispatch.
  * Assert that when a handler raises `RuntimeError`, the exception is logged but does not propagate out of `EventBus.publish()`.
* **Test Strategy (Integration)**:
  * Use `ThreadPoolTaskExecutor` to assert concurrent dispatching (verify `publish()` returns immediately while handlers run concurrently).
  * Assert that calling `shutdown()` on the executor waits for running handlers to complete.

---

## 3. Context-Owned Manifest Databases

Each context maintains its own local manifest DB file (`ingestion.db`, `transcription.db`, `knowledge.db`).

### Ingestion Manifest
* Schema: `manifest` (external_id [PK], content_id [NotNull], status [NotNull])
* Statuses: `IngestionStatus` enum values.
* Constraint: Unique `external_id`.

### Transcription Manifest
* Schema: `transcription` (content_id [PK], status [NotNull], language [NotNull], model [NotNull])
* Statuses: `TranscriptionStatus` enum values.

### Knowledge Manifest
* Schema: `knowledge` (content_id [PK], status [NotNull], raw_note_path [Null/Text], wiki_article_path [Null/Text])
* Statuses: `KnowledgeStatus` enum values.

### Test Strategy (Unit & Mocks - Option C)
* In Use Case unit tests, the manifest ports are replaced with mock objects. We verify that:
  * The Use Case invokes the manifest's save/status update methods.
  * The Use Case passes the status and events to the ports together.
  * The concrete transaction handling is validated in integration tests against `:memory:` SQLite instances.

---

## 4. Application Retry Use Cases

Retry flows are encapsulated inside application use cases, keeping CLI scripts humble.

### RetryFailedTranscriptionsUseCase
* **Behavior**:
  * Scans `TranscriptionManifestPort` for tasks with status `FAILED`.
  * For each failed item, invokes the transcriber port.
  * On success, updates status to `TRANSCRIBED` and publishes `TranscriptionCompleted`.
  * On failure, logs the error and updates status to `FAILED`.
* **Test Strategy (Unit)**:
  * Mock the manifest port to return a list of failed tasks.
  * Mock the transcriber port to simulate success for task A and failure for task B.
  * Assert that task A transitions to `TRANSCRIBED` and emits event.
  * Assert that task B remains `FAILED` and does not crash the loop.

### RetryFailedSynthesesUseCase
* **Behavior**:
  * Scans `KnowledgeManifestPort` for tasks with status `FAILED`.
  * For each failed item, runs the LLM synthesis pipeline.
  * On success, updates status to `COMPLETED` and publishes `KnowledgeSynthesized`.
  * On failure, updates status to `FAILED`.
* **Test Strategy (Unit)**:
  * Mock the ports and assert that the synthesis loop executes only on failed items.
  * Verify that successful synthesis updates the local database status correctly.
