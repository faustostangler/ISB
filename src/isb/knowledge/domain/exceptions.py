class KnowledgeError(Exception):
    """Base domain exception for the Knowledge bounded context.

    Comments must answer 'why': Root exception used to isolate synthesis and vault errors
    from other infrastructure or transcription failures.
    """
    pass


class SchemaViolationError(KnowledgeError):
    """Raised when LLM-synthesized data violates structural rules defined in Pydantic.

    Ensures that bad formatting or incomplete LLM response graphs do not pollute
    the structured second brain vaults.
    """
    pass


class SynthesisError(KnowledgeError):
    """Raised when the LLM synthesis pipeline fails.

    For example, raised if the local Ollama daemon is unreachable or if it returns
    an empty/corrupted payload.
    """
    pass
