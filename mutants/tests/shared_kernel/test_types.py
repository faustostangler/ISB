import pytest
import uuid
from isb.shared_kernel.types import ContentId, ProcessingStatus

def test_content_id_generation() -> None:
    """Test generating a new ContentId."""
    content_id = ContentId.generate()
    assert isinstance(content_id.value, uuid.UUID)
    # Check it's UUID version 4
    assert content_id.value.version == 4

def test_content_id_from_valid_string() -> None:
    """Test constructing ContentId from a valid UUID string."""
    raw_uuid = str(uuid.uuid4())
    content_id = ContentId.from_str(raw_uuid)
    assert str(content_id) == raw_uuid

def test_content_id_from_invalid_string() -> None:
    """Test that invalid UUID string raises ValueError."""
    with pytest.raises(ValueError, match="Invalid UUID format"):
        ContentId.from_str("not-a-uuid")

def test_content_id_equality_and_hashing() -> None:
    """Test equality and hashing of ContentId."""
    raw_uuid = uuid.uuid4()
    id1 = ContentId(raw_uuid)
    id2 = ContentId(raw_uuid)
    id3 = ContentId.generate()
    
    assert id1 == id2
    assert id1 != id3
    assert hash(id1) == hash(id2)
    assert hash(id1) != hash(id3)

def test_processing_status_values() -> None:
    """Test that all required processing statuses exist."""
    assert ProcessingStatus.PENDING.value == "PENDING"
    assert ProcessingStatus.EXTRACTING.value == "EXTRACTING"
    assert ProcessingStatus.TRANSCRIBING.value == "TRANSCRIBING"
    assert ProcessingStatus.SYNTHESIZING.value == "SYNTHESIZING"
    assert ProcessingStatus.COMPLETED.value == "COMPLETED"
    assert ProcessingStatus.FAILED.value == "FAILED"
