class KnowledgeError(Exception):
    """Base domain exception for the Knowledge bounded context.

    Comments must answer 'why': Root exception used to isolate synthesis and vault errors.
    """
    pass


class SchemaViolationError(KnowledgeError):
    """Raised when LLM-synthesized data violates structural rules defined in Pydantic."""
    pass


class SynthesisError(KnowledgeError):
    """Raised when the LLM synthesis pipeline fails (e.g. LLM unreachable or empty output)."""
    pass
