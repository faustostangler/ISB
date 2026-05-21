class TranscriptionError(Exception):
    """Base domain exception for the Transcription bounded context.

    Comments must answer 'why': Root exception used to distinguish transcription stage errors.
    """
    pass
