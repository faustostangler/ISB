# Ingestion Bounded Context Specifications

This document defines the formal behavioral specifications, boundaries, and invariants for the Ingestion Bounded Context.

---

## 1. Value Object Invariants

### ExternalId
- **Description:** A platform-specific media identifier.
- **Constraints:**
  - Must be a string.
  - Must not be empty or contain only whitespace characters.
  - Must contain only alphanumeric characters, hyphens, and underscores.
  - Length must be between 3 and 64 characters (inclusive).
- **Test Scenarios:**
  - Construction with `yt_123-abc` is valid.
  - Construction with empty string, only spaces, or invalid types (e.g. `123`) raises `ValueError` or `TypeError`.

### EpisodeTitle
- **Description:** The title of the scraped media episode.
- **Constraints:**
  - Must be a string.
  - Must not be empty or contain only whitespace.
  - Whitespace at start and end must be trimmed automatically.
- **Test Scenarios:**
  - Construction with `"  My Video  "` is trimmed to `"My Video"`.
  - Construction with empty string raises `ValueError`.

### DurationSeconds
- **Description:** Total length of the episode in seconds.
- **Constraints:**
  - Must be an integer.
  - Must be greater than or equal to zero.
- **Test Scenarios:**
  - Construction with `300` is valid.
  - Construction with negative integer (e.g., `-5`) or string raises `ValueError` or `TypeError`.

### PublishedAt
- **Description:** Datetime when the media was uploaded/published.
- **Constraints:**
  - Must be a `datetime` object.
  - Must be timezone-aware (specifically UTC timezone).
- **Test Scenarios:**
  - UTC datetime is accepted.
  - Naive datetime (without tz info) raises `ValueError`.

### SourceId, SourceName
- **Description:** Identifiers and human-readable names for media sources.
- **Constraints:**
  - Must be non-empty strings.

### SourceUrl
- **Description:** The extraction target URL feed.
- **Constraints:**
  - Must be a string.
  - Must start with `http://` or `https://`.

---

## 2. Entity Invariants

### MediaEpisode
- **Rules:**
  - Must contain a valid `ContentId` (wrapping UUIDv4). The domain layer must be identified strictly via system-wide UUID4. Platform-specific identifiers (such as YouTube video IDs) must never be used as domain entity IDs. They are treated strictly as external IDs mapped in the manifest registry.
  - Must enforce that `status` is a valid member of `ProcessingStatus`.
  - Can only contain an `AudioTrack` when transition is complete.
  - Construction with any primitive inputs must automatically coerce them into the corresponding Value Objects (coercion safety).

### MediaSource
- **Rules:**
  - Aggregate root tracking child episodes.
  - Adding a child episode checks external ID uniqueness across all children. If a duplicate external ID is added, raises `DuplicateEpisodeError`.

---

## 3. Application Use Cases

### ExtractAudioUseCase
- **Acceptance Criteria:**
  - Queries `ManifestPort` before executing downloads to ensure idempotency (skips if already processing or completed).
  - Marks status as `EXTRACTING` at beginning of download.
  - Marks status as `TRANSCRIBING` once files are successfully saved to disk.
  - Transactionally persists `AudioExtracted` event to `outbox` table, and publishes event to EventBus.
  - Reverts status to `FAILED` in manifest database if the scraper adapter throws a network error or extraction timeout exception.
