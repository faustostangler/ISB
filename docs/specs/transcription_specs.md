# Transcription Bounded Context Specifications

This document defines the formal behavioral specifications, boundaries, and invariants for the Transcription Bounded Context.

---

## 1. Value Object Invariants

### LanguageCode
- **Description:** ISO language code hint or detected output code.
- **Constraints:**
  - Must be a string.
  - Length must be between 2 and 5 characters (inclusive) after trimming.
- **Test Scenarios:**
  - `pt`, `en`, `es`, `pt-br` are valid.
  - Empty string, single letter (e.g. `p`), or long strings raise `ValueError`.

### ModelName
- **Description:** The size name of the loaded Whisper model.
- **Constraints:**
  - Must be a string.
  - Must be one of the standard Whisper sizes (case-insensitive check): `tiny`, `base`, `small`, `medium`, `large`, `large-v2`, `large-v3`.
- **Test Scenarios:**
  - `"base"`, `"BASE"`, `"small"` are valid.
  - `"invalid-size"` or empty string raises `ValueError`.

### TranscriptText
- **Description:** Verbatim transcribed text content.
- **Constraints:**
  - Must be a string.
  - Must not be empty or contain only whitespace.

### Segment
- **Description:** Timing and text slide extracted from the audio stream.
- **Constraints:**
  - `start_seconds` and `end_seconds` must be floats.
  - `start_seconds >= 0.0` and `end_seconds >= 0.0`.
  - `start_seconds <= end_seconds`.
  - `confidence` must be a float between `0.0` and `1.0` (inclusive).
- **Test Scenarios:**
  - Start time after end time raises `ValueError`.
  - Confidence of `1.05` or `-0.1` raises `ValueError`.

---

## 2. Entity Invariants

### Transcript
- **Rules:**
  - Enforces `content_id` is a valid ContentId.
  - Enforces `full_text` is wrapped in a `TranscriptText` Value Object.
  - Enforces `language` is a valid `LanguageCode` (defaults to `pt`).
  - Enforces `model` is a valid `ModelName` (defaults to `base`).
  - Enforces `duration_seconds` is a float greater than or equal to zero.
  - Automatic type coercion is performed using Pydantic before-validators.

---

## 3. Application Use Cases

### TranscribeAudioUseCase
- **Acceptance Criteria:**
  - Marks status as `TRANSCRIBING` at start.
  - Lazy-loads Whisper model on demand to reduce start-up memory usage.
  - Normalizes log probability outputs from Whisper to a `[0.0, 1.0]` range mapping to segment confidence scores.
  - Saves a sibling JSON file containing full text, duration, and segments inside cache directory for disaster recovery.
  - Marks status as `SYNTHESIZING` upon completion.
  - Transactionally registers `TranscriptionCompleted` event inside SQLite `outbox` table, and publishes event.
  - Reverts status to `FAILED` in manifest database upon model or disk failure.
