class IngestionError(Exception):
    """Base domain exception for the Ingestion bounded context.

    This exception is used to isolate all Ingestion layer errors from upstream
    application orchestration flows, serving as a boundary for exception translation.
    """
    pass


class DownloadError(IngestionError):
    """Raised when the external media extractor fails to retrieve/download media files.

    Used when network errors, format changes, or content availability issues
    prevent the local files from being successfully persisted to disk.
    """
    pass


class DuplicateEpisodeError(IngestionError):
    """Raised when trying to add an episode that is already present in the source.

    Enforces entity identity boundaries within the MediaSource domain aggregate.
    """
    pass
