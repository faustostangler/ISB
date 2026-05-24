# Ingestion Bounded Context Glossary

This glossary contains the Ubiquitous Language terms for the Ingestion Bounded Context.

## Terms

### MediaSource
* **Definition**: A configured external resource (such as a YouTube channel URL, a playlist URL, or a local audio directory) containing media to be processed.
* **Rules**: Must be uniquely identified by a `source_id`.

### MediaEpisode
* **Definition**: A single unit of media content extracted from a `MediaSource` (such as a YouTube video or podcast episode).
* **Rules**: Tracks external identifier (`external_id`), title, duration, and publication date. Maps to a unique internal `ContentId`.

### AudioTrack
* **Definition**: The extracted audio file (`.wav`/`.mp3`) saved locally from a `MediaEpisode`.
* **Rules**: Handled as an immutable Value Object with properties defining file path, format, size, and duration.

### IngestionStatus (Local Lifecycle)
* **Definition**: The status tracked by Ingestion to coordinate the local extraction pipeline and correlate downstream progress events:
  * `PENDING`: Episode is discovered but extraction has not started.
  * `EXTRACTING`: yt-dlp is currently running to download/extract audio.
  * `EXTRACTED`: Audio has been successfully extracted and saved.
  * `TRANSCRIBING`: Downstream Transcription context has started Whisper processing (triggered by event update).
  * `TRANSCRIBED`: Downstream Transcription context has completed processing (triggered by event update).
  * `SYNTHESIZING`: Downstream Knowledge context has started Obsidian wiki compilation (triggered by event update).
  * `COMPLETED`: Downstream Knowledge context completed wiki synthesis successfully.
  * `FAILED`: Extraction or downstream pipeline stage failed.
