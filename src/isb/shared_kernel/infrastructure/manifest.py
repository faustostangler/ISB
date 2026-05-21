import sqlite3
from pathlib import Path
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.ingestion.application.ports import ManifestPort
from isb.transcription.application.ports import TranscriptionManifestPort
from isb.knowledge.application.ports import KnowledgeManifestPort

class SQLiteManifestAdapter(ManifestPort, TranscriptionManifestPort, KnowledgeManifestPort):
    """SQLite-based implementation of idempotency registries across bounded contexts.

    Provides atomic state tracking and unique content mapping persistence.
    By inheriting from context-specific manifest ports, this class functions
    as a shared database adapter conforming to the interface segregation principle.
    """

    def __init__(self, db_path: str | Path) -> None:
        """Initialize the SQLite manifest file location and trigger schema creations.

        Args:
            db_path: Path to the SQLite manifest database file.
        """
        # Step 1: Assign and convert database path to a Path object
        # Ensures cross-platform compatibility of file system paths
        self.db_path = Path(db_path)
        # Step 2: Trigger database and tables initialization
        # Creates tables if they are not already present to guarantee zero-config startup
        self._init_db()

    def _init_db(self) -> None:
        """Create database tables if they do not exist."""
        # Step 1: Open connection to the SQLite database file
        # The 'with' context manager guarantees proper resource cleanup/closing
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Execute manifest table creation query
            # Tracks external IDs (e.g. YouTube IDs) mapped to internal Content IDs (UUIDv4) and status.
            # external_id is primary key because one external stream maps to one internal entity.
            conn.execute("""
                CREATE TABLE IF NOT EXISTS manifest (
                    external_id TEXT PRIMARY KEY,
                    content_id TEXT NOT NULL,
                    status TEXT NOT NULL
                )
            """)
            # Step 3: Execute status_history table creation query
            # Tracks historical status transitions for telemetry, observability, and audit tracking.
            conn.execute("""
                CREATE TABLE IF NOT EXISTS status_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content_id TEXT NOT NULL,
                    status TEXT NOT NULL,
                    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            # Step 4: Commit changes to save transaction state
            # Persists the schemas to the SQLite database on disk
            conn.commit()

    def is_processed(self, external_id: str) -> bool:
        """Check if an external ID has been successfully processed or is currently processing.

        Returns True for all states except FAILED or non-existent to guarantee idempotency.

        Args:
            external_id: The external stream/source identifier.

        Returns:
            bool: True if already processed or processing, False if new or failed previously.
        """
        # Step 1: Open database connection
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Create cursor to query database
            cursor = conn.cursor()
            # Step 3: Select the status of the given external ID
            cursor.execute("SELECT status FROM manifest WHERE external_id = ?", (external_id,))
            row = cursor.fetchone()
            
            # Step 4: Return False if no record exists (not processed yet)
            if not row:
                return False
                
            # Step 5: Check if the current status is not FAILED.
            # If status is FAILED, it is not successfully processed/processing (can be retried, return False).
            # Otherwise, return True (to avoid duplicate concurrent active jobs or downloads).
            return row[0] != ProcessingStatus.FAILED.value

    def get_content_id(self, external_id: str) -> ContentId | None:
        """Get the internal ContentId registered to this external ID, if it exists.

        Args:
            external_id: The external source/stream identifier.

        Returns:
            ContentId | None: The mapped ContentId object or None if unregistered/corrupt.
        """
        # Step 1: Open database connection
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Create cursor to query database
            cursor = conn.cursor()
            # Step 3: Fetch the ContentId associated with the external ID
            cursor.execute("SELECT content_id FROM manifest WHERE external_id = ?", (external_id,))
            row = cursor.fetchone()
            
            # Step 4: If no entry is found, return None
            if not row:
                return None
                
            # Step 5: Attempt to deserialize the string back to a Domain ContentId (UUIDv4 wrapper)
            try:
                return ContentId.from_str(row[0])
            except ValueError:
                # Step 6: Handle potential DB corruption gracefully by returning None
                # Rather than crashing, this allows healing by re-extracting or rebuilding
                return None

    def register_episode(self, external_id: str, content_id: ContentId) -> None:
        """Register a new external ID with an internal ContentId and status PENDING.

        Args:
            external_id: The external stream/source identifier.
            content_id: The assigned internal ContentId entity wrapper.
        """
        # Step 1: Open database connection
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Execute insertion command initializing the episode status to PENDING
            conn.execute(
                "INSERT INTO manifest (external_id, content_id, status) VALUES (?, ?, ?)",
                (external_id, str(content_id), ProcessingStatus.PENDING.value)
            )
            # Step 3: Commit the transaction
            # Enforces immediate persistence in case concurrent workers query this ID next
            conn.commit()

    def mark_status(self, content_id: ContentId, status: ProcessingStatus) -> None:
        """Update the processing status of the given ContentId and log to history.

        Args:
            content_id: The internal ContentId entity identifier.
            status: The new status enum transition state.
        """
        # Step 1: Open database connection
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Update the status of the record matching the ContentId string representation
            conn.execute(
                "UPDATE manifest SET status = ? WHERE content_id = ?",
                (status.value, str(content_id))
            )
            # Step 3: Append the state transition log in the status_history table
            # Allows tracking history of processing pipelines for latency and bottleneck telemetry
            conn.execute(
                "INSERT INTO status_history (content_id, status) VALUES (?, ?)",
                (str(content_id), status.value)
            )
            # Step 4: Commit changes to persist the update
            conn.commit()

    def has_failed_previously(self, external_id: str) -> bool:
        """Check if an external ID has previously failed processing.

        Args:
            external_id: The external stream/source identifier.

        Returns:
            bool: True if status is currently set to FAILED, False otherwise.
        """
        # Step 1: Open database connection
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Create cursor to query database
            cursor = conn.cursor()
            # Step 3: Fetch the current status of the external ID
            cursor.execute("SELECT status FROM manifest WHERE external_id = ?", (external_id,))
            row = cursor.fetchone()
            
            # Step 4: Return False if no record exists
            if not row:
                return False
                
            # Step 5: Check if the saved status string is equal to FAILED
            return row[0] == ProcessingStatus.FAILED.value
