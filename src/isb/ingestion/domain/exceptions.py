class IngestionError(Exception):
    """Base domain exception for the Ingestion bounded context.

    Comments must answer 'why': Root exception used to distinguish Ingestion errors from other layers.
    """
    pass


class DownloadError(IngestionError):
    """Raised when the external media extractor fails to retrieve/download media files."""
    pass


class DuplicateEpisodeError(IngestionError):
    """Raised when trying to add an episode that is already present in the source."""
    pass
