import sqlite3
import pytest
from pathlib import Path
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.shared_kernel.infrastructure.manifest import SQLiteManifestAdapter

@pytest.fixture
def temp_db_path(tmp_path: Path) -> Path:
    """Fixture to provide a temporary file path for the SQLite database."""
    # Step 1: Combine the system temp directory path with a custom filename
    return tmp_path / "test_manifest.db"

def test_sqlite_manifest_db_init(temp_db_path: Path) -> None:
    """Verify that SQLiteManifestAdapter initializes tables correctly."""
    # Step 1: Instantiate the adapter, which triggers _init_db
    adapter = SQLiteManifestAdapter(temp_db_path)
    
    # Step 2: Assert that the database file was successfully created on disk
    assert temp_db_path.exists()

    # Step 3: Establish a raw sqlite connection to query schema directly
    with sqlite3.connect(temp_db_path) as conn:
        cursor = conn.cursor()
        
        # Step 4: Query sqlite master catalog to fetch all table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        
        # Step 5: Assert that both required tables were created
        assert "manifest" in tables
        assert "status_history" in tables

def test_sqlite_manifest_register_episode(temp_db_path: Path) -> None:
    """Verify that register_episode registers the episode with PENDING status."""
    # Step 1: Initialize the adapter
    adapter = SQLiteManifestAdapter(temp_db_path)
    ext_id = "yt_12345"
    content_id = ContentId.generate()

    # Step 2: Assert that the unregistered external ID does not have a content ID yet
    assert adapter.get_content_id(ext_id) is None
    
    # Step 3: Call the adapter to register the new episode
    adapter.register_episode(ext_id, content_id)
    
    # Step 4: Assert that the registered external ID retrieves the correct ContentId object
    assert adapter.get_content_id(ext_id) == content_id
    
    # Step 5: Assert that it is not considered processed (since it starts as PENDING)
    assert not adapter.is_processed(ext_id)
    
    # Step 6: Assert that it does not show up as previously failed
    assert not adapter.has_failed_previously(ext_id)

def test_sqlite_manifest_is_processed(temp_db_path: Path) -> None:
    """Verify is_processed logic for different states."""
    # Step 1: Initialize the adapter
    adapter = SQLiteManifestAdapter(temp_db_path)
    ext_id = "yt_12345"
    content_id = ContentId.generate()

    # Step 2: Assert that a non-existent external ID returns False for processed check
    assert not adapter.is_processed(ext_id)

    # Step 3: Register the episode
    adapter.register_episode(ext_id, content_id)
    
    # Step 4: Assert that PENDING (the default state) returns True for processed/processing.
    # This prevents the queue system from starting duplicate jobs for the same episode.
    assert adapter.is_processed(ext_id)

    # Step 5: Update the status to COMPLETED
    adapter.mark_status(content_id, ProcessingStatus.COMPLETED)
    
    # Step 6: Assert that COMPLETED returns True for processed check
    assert adapter.is_processed(ext_id)
    
    # Step 7: Assert that it does not register as previously failed
    assert not adapter.has_failed_previously(ext_id)

    # Step 8: Update status to FAILED
    adapter.mark_status(content_id, ProcessingStatus.FAILED)
    
    # Step 9: Assert that FAILED returns False for processed check (allowing it to be re-run)
    assert not adapter.is_processed(ext_id)
    
    # Step 10: Assert that it registers as failed previously
    assert adapter.has_failed_previously(ext_id)

def test_sqlite_manifest_mark_status_history(temp_db_path: Path) -> None:
    """Verify that mark_status updates status and logs to status_history."""
    # Step 1: Initialize adapter
    adapter = SQLiteManifestAdapter(temp_db_path)
    ext_id = "yt_123"
    content_id = ContentId.generate()

    # Step 2: Register the episode
    adapter.register_episode(ext_id, content_id)
    
    # Step 3: Update the status to EXTRACTING
    adapter.mark_status(content_id, ProcessingStatus.EXTRACTING)

    # Step 4: Establish a raw database connection to verify raw storage state
    with sqlite3.connect(temp_db_path) as conn:
        cursor = conn.cursor()
        
        # Step 5: Query the current status of the record in manifest table
        cursor.execute("SELECT status FROM manifest WHERE content_id = ?", (str(content_id),))
        assert cursor.fetchone()[0] == "EXTRACTING"

        # Step 6: Query the status history log ordered by newest entry first
        cursor.execute("SELECT status, content_id FROM status_history ORDER BY id DESC")
        history_rows = cursor.fetchall()
        
        # Step 7: Assert history has entries and the newest entry details are correct
        assert len(history_rows) >= 1
        assert history_rows[0][0] == "EXTRACTING"
        assert history_rows[0][1] == str(content_id)

def test_sqlite_manifest_get_content_id_corrupted_uuid(temp_db_path: Path) -> None:
    """Verify that get_content_id handles invalid UUID strings by returning None."""
    # Step 1: Initialize adapter
    adapter = SQLiteManifestAdapter(temp_db_path)
    ext_id = "corrupted_id"

    # Step 2: Direct-insert a raw malformed UUID string bypassing Pydantic validations
    with sqlite3.connect(temp_db_path) as conn:
        conn.execute(
            "INSERT INTO manifest (external_id, content_id, status) VALUES (?, ?, ?)",
            (ext_id, "not-a-valid-uuid", "PENDING")
        )
        conn.commit()

    # Step 3: Assert that query returns None to gracefully recover from DB corruption
    assert adapter.get_content_id(ext_id) is None
