class TranscriptionError(Exception):
    """Base domain exception for the Transcription bounded context.

    Acts as the parent exception isolating audio translation errors (such as Whisper
    model loading failures, audio file corruption, or API connection errors)
    from triggering generic system crashes.
    """
    pass
