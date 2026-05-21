import pytest
from pydantic import ValidationError
from isb.knowledge.domain.value_objects import SynthesizedArticleSchema

def test_synthesized_article_schema_valid() -> None:
    """Verify that a valid payload passes Pydantic schema validation."""
    # Step 1: Define a valid dictionary payload
    payload = {
        "title": "Clean Architecture Guide",
        "summary": "This article explains clean architecture in modern projects.",
        "key_takeaways": [
            "Use ports and adapters to decouple domains.",
            "Domain layer has zero dependencies.",
            "Write adapters for database queries."
        ],
        "content": "This is a detailed article explaining Clean Architecture. " * 3,
        "tags": ["Architecture", "DDD"],
        "related_topics": ["Hexagonal Architecture"]
    }
    
    # Step 2: Validate payload through schema constructor
    schema = SynthesizedArticleSchema(**payload)
    
    # Step 3: Assert parsed attributes are mapped correctly
    assert schema.title == "Clean Architecture Guide"
    assert schema.tags == ["architecture", "ddd"]  # Check lowercase normalization

def test_synthesized_article_schema_invalid_lengths() -> None:
    """Verify that short fields trigger ValidationError."""
    # Step 1: Try too short title
    with pytest.raises(ValidationError) as exc:
        SynthesizedArticleSchema(
            title="Ab",  # < 3 chars
            summary="This article explains clean architecture.",
            key_takeaways=["Takeaway 1", "Takeaway 2", "Takeaway 3"],
            content="Too short",  # < 50 chars
            tags=["tech"],
            related_topics=[]
        )
    assert "title" in str(exc.value)
    assert "content" in str(exc.value)

def test_synthesized_article_schema_takeaway_count_limits() -> None:
    """Verify that too few or too many takeaways trigger ValidationError."""
    # Step 1: Validate with only 2 takeaways (min is 3)
    with pytest.raises(ValidationError) as exc_few:
        SynthesizedArticleSchema(
            title="Valid Title",
            summary="This is a valid long summary for testing purposes.",
            key_takeaways=["Only 1", "Only 2"],
            content="This is a very long text to satisfy the minimum length constraint of 50 characters.",
            tags=["tech"],
            related_topics=[]
        )
    assert "key_takeaways" in str(exc_few.value)

    # Step 2: Validate with 11 takeaways (max is 10)
    with pytest.raises(ValidationError) as exc_many:
        SynthesizedArticleSchema(
            title="Valid Title",
            summary="This is a valid long summary for testing purposes.",
            key_takeaways=[f"Takeaway {i}" for i in range(11)],
            content="This is a very long text to satisfy the minimum length constraint of 50 characters.",
            tags=["tech"],
            related_topics=[]
        )
    assert "key_takeaways" in str(exc_many.value)

def test_synthesized_article_schema_title_sanitization() -> None:
    """Verify that illegal file characters in titles are replaced/sanitized."""
    # Step 1: Define a payload with illegal title characters: \ / : * ? " < > |
    payload = {
        "title": "Docker\\Compose: A Guide?",
        "summary": "This is a valid long summary for testing purposes.",
        "key_takeaways": ["Takeaway 1", "Takeaway 2", "Takeaway 3"],
        "content": "This is a very long text to satisfy the minimum length constraint of 50 characters.",
        "tags": ["tech"],
        "related_topics": []
    }
    
    # Step 2: Validate the payload
    schema = SynthesizedArticleSchema(**payload)
    
    # Step 3: Assert the title was successfully sanitized into a valid filename format
    # "Docker\Compose: A Guide?" -> "Docker Compose A Guide"
    assert schema.title == "Docker Compose A Guide"

def test_synthesized_article_schema_tag_normalization() -> None:
    """Verify that tags are filtered to keep only lowercase alphanumeric characters."""
    # Step 1: Define payload with tags containing punctuation, uppercase characters, and whitespace
    payload = {
        "title": "Valid Title",
        "summary": "This is a valid long summary for testing purposes.",
        "key_takeaways": ["Takeaway 1", "Takeaway 2", "Takeaway 3"],
        "content": "This is a very long text to satisfy the minimum length constraint of 50 characters.",
        "tags": ["Docker-Compose", "   ", "whisper!"],
        "related_topics": []
    }
    
    # Step 2: Validate the payload
    schema = SynthesizedArticleSchema(**payload)
    
    # Step 3: Assert tags normalized correctly: "Docker-Compose" -> "dockercompose", "   " is discarded, "whisper!" -> "whisper"
    assert schema.tags == ["dockercompose", "whisper"]
