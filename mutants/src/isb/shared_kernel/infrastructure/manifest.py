import sqlite3
from pathlib import Path
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.ingestion.application.ports import ManifestPort
from isb.transcription.application.ports import TranscriptionManifestPort
from isb.knowledge.application.ports import KnowledgeManifestPort
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore

class SQLiteManifestAdapter(ManifestPort, TranscriptionManifestPort, KnowledgeManifestPort):
    """SQLite-based implementation of idempotency registries across bounded contexts.

    Provides atomic state tracking and unique content mapping persistence.
    By inheriting from context-specific manifest ports, this class functions
    as a shared database adapter conforming to the interface segregation principle.
    """

    def __init__(self, db_path: str | Path) -> None:
        args = [db_path]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁSQLiteManifestAdapterǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁSQLiteManifestAdapterǁ__init____mutmut_mutants'), args, kwargs, self)

    def xǁSQLiteManifestAdapterǁ__init____mutmut_orig(self, db_path: str | Path) -> None:
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

    def xǁSQLiteManifestAdapterǁ__init____mutmut_1(self, db_path: str | Path) -> None:
        """Initialize the SQLite manifest file location and trigger schema creations.

        Args:
            db_path: Path to the SQLite manifest database file.
        """
        # Step 1: Assign and convert database path to a Path object
        # Ensures cross-platform compatibility of file system paths
        self.db_path = None
        # Step 2: Trigger database and tables initialization
        # Creates tables if they are not already present to guarantee zero-config startup
        self._init_db()

    def xǁSQLiteManifestAdapterǁ__init____mutmut_2(self, db_path: str | Path) -> None:
        """Initialize the SQLite manifest file location and trigger schema creations.

        Args:
            db_path: Path to the SQLite manifest database file.
        """
        # Step 1: Assign and convert database path to a Path object
        # Ensures cross-platform compatibility of file system paths
        self.db_path = Path(None)
        # Step 2: Trigger database and tables initialization
        # Creates tables if they are not already present to guarantee zero-config startup
        self._init_db()
    
    xǁSQLiteManifestAdapterǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁSQLiteManifestAdapterǁ__init____mutmut_1': xǁSQLiteManifestAdapterǁ__init____mutmut_1, 
        'xǁSQLiteManifestAdapterǁ__init____mutmut_2': xǁSQLiteManifestAdapterǁ__init____mutmut_2
    }
    xǁSQLiteManifestAdapterǁ__init____mutmut_orig.__name__ = 'xǁSQLiteManifestAdapterǁ__init__'

    def _init_db(self) -> None:
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁSQLiteManifestAdapterǁ_init_db__mutmut_orig'), object.__getattribute__(self, 'xǁSQLiteManifestAdapterǁ_init_db__mutmut_mutants'), args, kwargs, self)

    def xǁSQLiteManifestAdapterǁ_init_db__mutmut_orig(self) -> None:
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

    def xǁSQLiteManifestAdapterǁ_init_db__mutmut_1(self) -> None:
        """Create database tables if they do not exist."""
        # Step 1: Open connection to the SQLite database file
        # The 'with' context manager guarantees proper resource cleanup/closing
        with sqlite3.connect(None) as conn:
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

    def xǁSQLiteManifestAdapterǁ_init_db__mutmut_2(self) -> None:
        """Create database tables if they do not exist."""
        # Step 1: Open connection to the SQLite database file
        # The 'with' context manager guarantees proper resource cleanup/closing
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Execute manifest table creation query
            # Tracks external IDs (e.g. YouTube IDs) mapped to internal Content IDs (UUIDv4) and status.
            # external_id is primary key because one external stream maps to one internal entity.
            conn.execute(None)
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

    def xǁSQLiteManifestAdapterǁ_init_db__mutmut_3(self) -> None:
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
            conn.execute(None)
            # Step 4: Commit changes to save transaction state
            # Persists the schemas to the SQLite database on disk
            conn.commit()
    
    xǁSQLiteManifestAdapterǁ_init_db__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁSQLiteManifestAdapterǁ_init_db__mutmut_1': xǁSQLiteManifestAdapterǁ_init_db__mutmut_1, 
        'xǁSQLiteManifestAdapterǁ_init_db__mutmut_2': xǁSQLiteManifestAdapterǁ_init_db__mutmut_2, 
        'xǁSQLiteManifestAdapterǁ_init_db__mutmut_3': xǁSQLiteManifestAdapterǁ_init_db__mutmut_3
    }
    xǁSQLiteManifestAdapterǁ_init_db__mutmut_orig.__name__ = 'xǁSQLiteManifestAdapterǁ_init_db'

    def is_processed(self, external_id: str) -> bool:
        args = [external_id]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁSQLiteManifestAdapterǁis_processed__mutmut_orig'), object.__getattribute__(self, 'xǁSQLiteManifestAdapterǁis_processed__mutmut_mutants'), args, kwargs, self)

    def xǁSQLiteManifestAdapterǁis_processed__mutmut_orig(self, external_id: str) -> bool:
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

    def xǁSQLiteManifestAdapterǁis_processed__mutmut_1(self, external_id: str) -> bool:
        """Check if an external ID has been successfully processed or is currently processing.

        Returns True for all states except FAILED or non-existent to guarantee idempotency.

        Args:
            external_id: The external stream/source identifier.

        Returns:
            bool: True if already processed or processing, False if new or failed previously.
        """
        # Step 1: Open database connection
        with sqlite3.connect(None) as conn:
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

    def xǁSQLiteManifestAdapterǁis_processed__mutmut_2(self, external_id: str) -> bool:
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
            cursor = None
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

    def xǁSQLiteManifestAdapterǁis_processed__mutmut_3(self, external_id: str) -> bool:
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
            cursor.execute(None, (external_id,))
            row = cursor.fetchone()
            
            # Step 4: Return False if no record exists (not processed yet)
            if not row:
                return False
                
            # Step 5: Check if the current status is not FAILED.
            # If status is FAILED, it is not successfully processed/processing (can be retried, return False).
            # Otherwise, return True (to avoid duplicate concurrent active jobs or downloads).
            return row[0] != ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁis_processed__mutmut_4(self, external_id: str) -> bool:
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
            cursor.execute("SELECT status FROM manifest WHERE external_id = ?", None)
            row = cursor.fetchone()
            
            # Step 4: Return False if no record exists (not processed yet)
            if not row:
                return False
                
            # Step 5: Check if the current status is not FAILED.
            # If status is FAILED, it is not successfully processed/processing (can be retried, return False).
            # Otherwise, return True (to avoid duplicate concurrent active jobs or downloads).
            return row[0] != ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁis_processed__mutmut_5(self, external_id: str) -> bool:
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
            cursor.execute((external_id,))
            row = cursor.fetchone()
            
            # Step 4: Return False if no record exists (not processed yet)
            if not row:
                return False
                
            # Step 5: Check if the current status is not FAILED.
            # If status is FAILED, it is not successfully processed/processing (can be retried, return False).
            # Otherwise, return True (to avoid duplicate concurrent active jobs or downloads).
            return row[0] != ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁis_processed__mutmut_6(self, external_id: str) -> bool:
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
            cursor.execute("SELECT status FROM manifest WHERE external_id = ?", )
            row = cursor.fetchone()
            
            # Step 4: Return False if no record exists (not processed yet)
            if not row:
                return False
                
            # Step 5: Check if the current status is not FAILED.
            # If status is FAILED, it is not successfully processed/processing (can be retried, return False).
            # Otherwise, return True (to avoid duplicate concurrent active jobs or downloads).
            return row[0] != ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁis_processed__mutmut_7(self, external_id: str) -> bool:
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
            cursor.execute("XXSELECT status FROM manifest WHERE external_id = ?XX", (external_id,))
            row = cursor.fetchone()
            
            # Step 4: Return False if no record exists (not processed yet)
            if not row:
                return False
                
            # Step 5: Check if the current status is not FAILED.
            # If status is FAILED, it is not successfully processed/processing (can be retried, return False).
            # Otherwise, return True (to avoid duplicate concurrent active jobs or downloads).
            return row[0] != ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁis_processed__mutmut_8(self, external_id: str) -> bool:
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
            cursor.execute("select status from manifest where external_id = ?", (external_id,))
            row = cursor.fetchone()
            
            # Step 4: Return False if no record exists (not processed yet)
            if not row:
                return False
                
            # Step 5: Check if the current status is not FAILED.
            # If status is FAILED, it is not successfully processed/processing (can be retried, return False).
            # Otherwise, return True (to avoid duplicate concurrent active jobs or downloads).
            return row[0] != ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁis_processed__mutmut_9(self, external_id: str) -> bool:
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
            cursor.execute("SELECT STATUS FROM MANIFEST WHERE EXTERNAL_ID = ?", (external_id,))
            row = cursor.fetchone()
            
            # Step 4: Return False if no record exists (not processed yet)
            if not row:
                return False
                
            # Step 5: Check if the current status is not FAILED.
            # If status is FAILED, it is not successfully processed/processing (can be retried, return False).
            # Otherwise, return True (to avoid duplicate concurrent active jobs or downloads).
            return row[0] != ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁis_processed__mutmut_10(self, external_id: str) -> bool:
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
            row = None
            
            # Step 4: Return False if no record exists (not processed yet)
            if not row:
                return False
                
            # Step 5: Check if the current status is not FAILED.
            # If status is FAILED, it is not successfully processed/processing (can be retried, return False).
            # Otherwise, return True (to avoid duplicate concurrent active jobs or downloads).
            return row[0] != ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁis_processed__mutmut_11(self, external_id: str) -> bool:
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
            if row:
                return False
                
            # Step 5: Check if the current status is not FAILED.
            # If status is FAILED, it is not successfully processed/processing (can be retried, return False).
            # Otherwise, return True (to avoid duplicate concurrent active jobs or downloads).
            return row[0] != ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁis_processed__mutmut_12(self, external_id: str) -> bool:
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
                return True
                
            # Step 5: Check if the current status is not FAILED.
            # If status is FAILED, it is not successfully processed/processing (can be retried, return False).
            # Otherwise, return True (to avoid duplicate concurrent active jobs or downloads).
            return row[0] != ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁis_processed__mutmut_13(self, external_id: str) -> bool:
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
            return row[1] != ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁis_processed__mutmut_14(self, external_id: str) -> bool:
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
            return row[0] == ProcessingStatus.FAILED.value
    
    xǁSQLiteManifestAdapterǁis_processed__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁSQLiteManifestAdapterǁis_processed__mutmut_1': xǁSQLiteManifestAdapterǁis_processed__mutmut_1, 
        'xǁSQLiteManifestAdapterǁis_processed__mutmut_2': xǁSQLiteManifestAdapterǁis_processed__mutmut_2, 
        'xǁSQLiteManifestAdapterǁis_processed__mutmut_3': xǁSQLiteManifestAdapterǁis_processed__mutmut_3, 
        'xǁSQLiteManifestAdapterǁis_processed__mutmut_4': xǁSQLiteManifestAdapterǁis_processed__mutmut_4, 
        'xǁSQLiteManifestAdapterǁis_processed__mutmut_5': xǁSQLiteManifestAdapterǁis_processed__mutmut_5, 
        'xǁSQLiteManifestAdapterǁis_processed__mutmut_6': xǁSQLiteManifestAdapterǁis_processed__mutmut_6, 
        'xǁSQLiteManifestAdapterǁis_processed__mutmut_7': xǁSQLiteManifestAdapterǁis_processed__mutmut_7, 
        'xǁSQLiteManifestAdapterǁis_processed__mutmut_8': xǁSQLiteManifestAdapterǁis_processed__mutmut_8, 
        'xǁSQLiteManifestAdapterǁis_processed__mutmut_9': xǁSQLiteManifestAdapterǁis_processed__mutmut_9, 
        'xǁSQLiteManifestAdapterǁis_processed__mutmut_10': xǁSQLiteManifestAdapterǁis_processed__mutmut_10, 
        'xǁSQLiteManifestAdapterǁis_processed__mutmut_11': xǁSQLiteManifestAdapterǁis_processed__mutmut_11, 
        'xǁSQLiteManifestAdapterǁis_processed__mutmut_12': xǁSQLiteManifestAdapterǁis_processed__mutmut_12, 
        'xǁSQLiteManifestAdapterǁis_processed__mutmut_13': xǁSQLiteManifestAdapterǁis_processed__mutmut_13, 
        'xǁSQLiteManifestAdapterǁis_processed__mutmut_14': xǁSQLiteManifestAdapterǁis_processed__mutmut_14
    }
    xǁSQLiteManifestAdapterǁis_processed__mutmut_orig.__name__ = 'xǁSQLiteManifestAdapterǁis_processed'

    def get_content_id(self, external_id: str) -> ContentId | None:
        args = [external_id]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁSQLiteManifestAdapterǁget_content_id__mutmut_orig'), object.__getattribute__(self, 'xǁSQLiteManifestAdapterǁget_content_id__mutmut_mutants'), args, kwargs, self)

    def xǁSQLiteManifestAdapterǁget_content_id__mutmut_orig(self, external_id: str) -> ContentId | None:
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

    def xǁSQLiteManifestAdapterǁget_content_id__mutmut_1(self, external_id: str) -> ContentId | None:
        """Get the internal ContentId registered to this external ID, if it exists.

        Args:
            external_id: The external source/stream identifier.

        Returns:
            ContentId | None: The mapped ContentId object or None if unregistered/corrupt.
        """
        # Step 1: Open database connection
        with sqlite3.connect(None) as conn:
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

    def xǁSQLiteManifestAdapterǁget_content_id__mutmut_2(self, external_id: str) -> ContentId | None:
        """Get the internal ContentId registered to this external ID, if it exists.

        Args:
            external_id: The external source/stream identifier.

        Returns:
            ContentId | None: The mapped ContentId object or None if unregistered/corrupt.
        """
        # Step 1: Open database connection
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Create cursor to query database
            cursor = None
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

    def xǁSQLiteManifestAdapterǁget_content_id__mutmut_3(self, external_id: str) -> ContentId | None:
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
            cursor.execute(None, (external_id,))
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

    def xǁSQLiteManifestAdapterǁget_content_id__mutmut_4(self, external_id: str) -> ContentId | None:
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
            cursor.execute("SELECT content_id FROM manifest WHERE external_id = ?", None)
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

    def xǁSQLiteManifestAdapterǁget_content_id__mutmut_5(self, external_id: str) -> ContentId | None:
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
            cursor.execute((external_id,))
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

    def xǁSQLiteManifestAdapterǁget_content_id__mutmut_6(self, external_id: str) -> ContentId | None:
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
            cursor.execute("SELECT content_id FROM manifest WHERE external_id = ?", )
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

    def xǁSQLiteManifestAdapterǁget_content_id__mutmut_7(self, external_id: str) -> ContentId | None:
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
            cursor.execute("XXSELECT content_id FROM manifest WHERE external_id = ?XX", (external_id,))
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

    def xǁSQLiteManifestAdapterǁget_content_id__mutmut_8(self, external_id: str) -> ContentId | None:
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
            cursor.execute("select content_id from manifest where external_id = ?", (external_id,))
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

    def xǁSQLiteManifestAdapterǁget_content_id__mutmut_9(self, external_id: str) -> ContentId | None:
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
            cursor.execute("SELECT CONTENT_ID FROM MANIFEST WHERE EXTERNAL_ID = ?", (external_id,))
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

    def xǁSQLiteManifestAdapterǁget_content_id__mutmut_10(self, external_id: str) -> ContentId | None:
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
            row = None
            
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

    def xǁSQLiteManifestAdapterǁget_content_id__mutmut_11(self, external_id: str) -> ContentId | None:
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
            if row:
                return None
                
            # Step 5: Attempt to deserialize the string back to a Domain ContentId (UUIDv4 wrapper)
            try:
                return ContentId.from_str(row[0])
            except ValueError:
                # Step 6: Handle potential DB corruption gracefully by returning None
                # Rather than crashing, this allows healing by re-extracting or rebuilding
                return None

    def xǁSQLiteManifestAdapterǁget_content_id__mutmut_12(self, external_id: str) -> ContentId | None:
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
                return ContentId.from_str(None)
            except ValueError:
                # Step 6: Handle potential DB corruption gracefully by returning None
                # Rather than crashing, this allows healing by re-extracting or rebuilding
                return None

    def xǁSQLiteManifestAdapterǁget_content_id__mutmut_13(self, external_id: str) -> ContentId | None:
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
                return ContentId.from_str(row[1])
            except ValueError:
                # Step 6: Handle potential DB corruption gracefully by returning None
                # Rather than crashing, this allows healing by re-extracting or rebuilding
                return None
    
    xǁSQLiteManifestAdapterǁget_content_id__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁSQLiteManifestAdapterǁget_content_id__mutmut_1': xǁSQLiteManifestAdapterǁget_content_id__mutmut_1, 
        'xǁSQLiteManifestAdapterǁget_content_id__mutmut_2': xǁSQLiteManifestAdapterǁget_content_id__mutmut_2, 
        'xǁSQLiteManifestAdapterǁget_content_id__mutmut_3': xǁSQLiteManifestAdapterǁget_content_id__mutmut_3, 
        'xǁSQLiteManifestAdapterǁget_content_id__mutmut_4': xǁSQLiteManifestAdapterǁget_content_id__mutmut_4, 
        'xǁSQLiteManifestAdapterǁget_content_id__mutmut_5': xǁSQLiteManifestAdapterǁget_content_id__mutmut_5, 
        'xǁSQLiteManifestAdapterǁget_content_id__mutmut_6': xǁSQLiteManifestAdapterǁget_content_id__mutmut_6, 
        'xǁSQLiteManifestAdapterǁget_content_id__mutmut_7': xǁSQLiteManifestAdapterǁget_content_id__mutmut_7, 
        'xǁSQLiteManifestAdapterǁget_content_id__mutmut_8': xǁSQLiteManifestAdapterǁget_content_id__mutmut_8, 
        'xǁSQLiteManifestAdapterǁget_content_id__mutmut_9': xǁSQLiteManifestAdapterǁget_content_id__mutmut_9, 
        'xǁSQLiteManifestAdapterǁget_content_id__mutmut_10': xǁSQLiteManifestAdapterǁget_content_id__mutmut_10, 
        'xǁSQLiteManifestAdapterǁget_content_id__mutmut_11': xǁSQLiteManifestAdapterǁget_content_id__mutmut_11, 
        'xǁSQLiteManifestAdapterǁget_content_id__mutmut_12': xǁSQLiteManifestAdapterǁget_content_id__mutmut_12, 
        'xǁSQLiteManifestAdapterǁget_content_id__mutmut_13': xǁSQLiteManifestAdapterǁget_content_id__mutmut_13
    }
    xǁSQLiteManifestAdapterǁget_content_id__mutmut_orig.__name__ = 'xǁSQLiteManifestAdapterǁget_content_id'

    def register_episode(self, external_id: str, content_id: ContentId) -> None:
        args = [external_id, content_id]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁSQLiteManifestAdapterǁregister_episode__mutmut_orig'), object.__getattribute__(self, 'xǁSQLiteManifestAdapterǁregister_episode__mutmut_mutants'), args, kwargs, self)

    def xǁSQLiteManifestAdapterǁregister_episode__mutmut_orig(self, external_id: str, content_id: ContentId) -> None:
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

    def xǁSQLiteManifestAdapterǁregister_episode__mutmut_1(self, external_id: str, content_id: ContentId) -> None:
        """Register a new external ID with an internal ContentId and status PENDING.

        Args:
            external_id: The external stream/source identifier.
            content_id: The assigned internal ContentId entity wrapper.
        """
        # Step 1: Open database connection
        with sqlite3.connect(None) as conn:
            # Step 2: Execute insertion command initializing the episode status to PENDING
            conn.execute(
                "INSERT INTO manifest (external_id, content_id, status) VALUES (?, ?, ?)",
                (external_id, str(content_id), ProcessingStatus.PENDING.value)
            )
            # Step 3: Commit the transaction
            # Enforces immediate persistence in case concurrent workers query this ID next
            conn.commit()

    def xǁSQLiteManifestAdapterǁregister_episode__mutmut_2(self, external_id: str, content_id: ContentId) -> None:
        """Register a new external ID with an internal ContentId and status PENDING.

        Args:
            external_id: The external stream/source identifier.
            content_id: The assigned internal ContentId entity wrapper.
        """
        # Step 1: Open database connection
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Execute insertion command initializing the episode status to PENDING
            conn.execute(
                None,
                (external_id, str(content_id), ProcessingStatus.PENDING.value)
            )
            # Step 3: Commit the transaction
            # Enforces immediate persistence in case concurrent workers query this ID next
            conn.commit()

    def xǁSQLiteManifestAdapterǁregister_episode__mutmut_3(self, external_id: str, content_id: ContentId) -> None:
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
                None
            )
            # Step 3: Commit the transaction
            # Enforces immediate persistence in case concurrent workers query this ID next
            conn.commit()

    def xǁSQLiteManifestAdapterǁregister_episode__mutmut_4(self, external_id: str, content_id: ContentId) -> None:
        """Register a new external ID with an internal ContentId and status PENDING.

        Args:
            external_id: The external stream/source identifier.
            content_id: The assigned internal ContentId entity wrapper.
        """
        # Step 1: Open database connection
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Execute insertion command initializing the episode status to PENDING
            conn.execute(
                (external_id, str(content_id), ProcessingStatus.PENDING.value)
            )
            # Step 3: Commit the transaction
            # Enforces immediate persistence in case concurrent workers query this ID next
            conn.commit()

    def xǁSQLiteManifestAdapterǁregister_episode__mutmut_5(self, external_id: str, content_id: ContentId) -> None:
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
                )
            # Step 3: Commit the transaction
            # Enforces immediate persistence in case concurrent workers query this ID next
            conn.commit()

    def xǁSQLiteManifestAdapterǁregister_episode__mutmut_6(self, external_id: str, content_id: ContentId) -> None:
        """Register a new external ID with an internal ContentId and status PENDING.

        Args:
            external_id: The external stream/source identifier.
            content_id: The assigned internal ContentId entity wrapper.
        """
        # Step 1: Open database connection
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Execute insertion command initializing the episode status to PENDING
            conn.execute(
                "XXINSERT INTO manifest (external_id, content_id, status) VALUES (?, ?, ?)XX",
                (external_id, str(content_id), ProcessingStatus.PENDING.value)
            )
            # Step 3: Commit the transaction
            # Enforces immediate persistence in case concurrent workers query this ID next
            conn.commit()

    def xǁSQLiteManifestAdapterǁregister_episode__mutmut_7(self, external_id: str, content_id: ContentId) -> None:
        """Register a new external ID with an internal ContentId and status PENDING.

        Args:
            external_id: The external stream/source identifier.
            content_id: The assigned internal ContentId entity wrapper.
        """
        # Step 1: Open database connection
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Execute insertion command initializing the episode status to PENDING
            conn.execute(
                "insert into manifest (external_id, content_id, status) values (?, ?, ?)",
                (external_id, str(content_id), ProcessingStatus.PENDING.value)
            )
            # Step 3: Commit the transaction
            # Enforces immediate persistence in case concurrent workers query this ID next
            conn.commit()

    def xǁSQLiteManifestAdapterǁregister_episode__mutmut_8(self, external_id: str, content_id: ContentId) -> None:
        """Register a new external ID with an internal ContentId and status PENDING.

        Args:
            external_id: The external stream/source identifier.
            content_id: The assigned internal ContentId entity wrapper.
        """
        # Step 1: Open database connection
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Execute insertion command initializing the episode status to PENDING
            conn.execute(
                "INSERT INTO MANIFEST (EXTERNAL_ID, CONTENT_ID, STATUS) VALUES (?, ?, ?)",
                (external_id, str(content_id), ProcessingStatus.PENDING.value)
            )
            # Step 3: Commit the transaction
            # Enforces immediate persistence in case concurrent workers query this ID next
            conn.commit()

    def xǁSQLiteManifestAdapterǁregister_episode__mutmut_9(self, external_id: str, content_id: ContentId) -> None:
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
                (external_id, str(None), ProcessingStatus.PENDING.value)
            )
            # Step 3: Commit the transaction
            # Enforces immediate persistence in case concurrent workers query this ID next
            conn.commit()
    
    xǁSQLiteManifestAdapterǁregister_episode__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁSQLiteManifestAdapterǁregister_episode__mutmut_1': xǁSQLiteManifestAdapterǁregister_episode__mutmut_1, 
        'xǁSQLiteManifestAdapterǁregister_episode__mutmut_2': xǁSQLiteManifestAdapterǁregister_episode__mutmut_2, 
        'xǁSQLiteManifestAdapterǁregister_episode__mutmut_3': xǁSQLiteManifestAdapterǁregister_episode__mutmut_3, 
        'xǁSQLiteManifestAdapterǁregister_episode__mutmut_4': xǁSQLiteManifestAdapterǁregister_episode__mutmut_4, 
        'xǁSQLiteManifestAdapterǁregister_episode__mutmut_5': xǁSQLiteManifestAdapterǁregister_episode__mutmut_5, 
        'xǁSQLiteManifestAdapterǁregister_episode__mutmut_6': xǁSQLiteManifestAdapterǁregister_episode__mutmut_6, 
        'xǁSQLiteManifestAdapterǁregister_episode__mutmut_7': xǁSQLiteManifestAdapterǁregister_episode__mutmut_7, 
        'xǁSQLiteManifestAdapterǁregister_episode__mutmut_8': xǁSQLiteManifestAdapterǁregister_episode__mutmut_8, 
        'xǁSQLiteManifestAdapterǁregister_episode__mutmut_9': xǁSQLiteManifestAdapterǁregister_episode__mutmut_9
    }
    xǁSQLiteManifestAdapterǁregister_episode__mutmut_orig.__name__ = 'xǁSQLiteManifestAdapterǁregister_episode'

    def mark_status(self, content_id: ContentId, status: ProcessingStatus) -> None:
        args = [content_id, status]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁSQLiteManifestAdapterǁmark_status__mutmut_orig'), object.__getattribute__(self, 'xǁSQLiteManifestAdapterǁmark_status__mutmut_mutants'), args, kwargs, self)

    def xǁSQLiteManifestAdapterǁmark_status__mutmut_orig(self, content_id: ContentId, status: ProcessingStatus) -> None:
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

    def xǁSQLiteManifestAdapterǁmark_status__mutmut_1(self, content_id: ContentId, status: ProcessingStatus) -> None:
        """Update the processing status of the given ContentId and log to history.

        Args:
            content_id: The internal ContentId entity identifier.
            status: The new status enum transition state.
        """
        # Step 1: Open database connection
        with sqlite3.connect(None) as conn:
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

    def xǁSQLiteManifestAdapterǁmark_status__mutmut_2(self, content_id: ContentId, status: ProcessingStatus) -> None:
        """Update the processing status of the given ContentId and log to history.

        Args:
            content_id: The internal ContentId entity identifier.
            status: The new status enum transition state.
        """
        # Step 1: Open database connection
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Update the status of the record matching the ContentId string representation
            conn.execute(
                None,
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

    def xǁSQLiteManifestAdapterǁmark_status__mutmut_3(self, content_id: ContentId, status: ProcessingStatus) -> None:
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
                None
            )
            # Step 3: Append the state transition log in the status_history table
            # Allows tracking history of processing pipelines for latency and bottleneck telemetry
            conn.execute(
                "INSERT INTO status_history (content_id, status) VALUES (?, ?)",
                (str(content_id), status.value)
            )
            # Step 4: Commit changes to persist the update
            conn.commit()

    def xǁSQLiteManifestAdapterǁmark_status__mutmut_4(self, content_id: ContentId, status: ProcessingStatus) -> None:
        """Update the processing status of the given ContentId and log to history.

        Args:
            content_id: The internal ContentId entity identifier.
            status: The new status enum transition state.
        """
        # Step 1: Open database connection
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Update the status of the record matching the ContentId string representation
            conn.execute(
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

    def xǁSQLiteManifestAdapterǁmark_status__mutmut_5(self, content_id: ContentId, status: ProcessingStatus) -> None:
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
                )
            # Step 3: Append the state transition log in the status_history table
            # Allows tracking history of processing pipelines for latency and bottleneck telemetry
            conn.execute(
                "INSERT INTO status_history (content_id, status) VALUES (?, ?)",
                (str(content_id), status.value)
            )
            # Step 4: Commit changes to persist the update
            conn.commit()

    def xǁSQLiteManifestAdapterǁmark_status__mutmut_6(self, content_id: ContentId, status: ProcessingStatus) -> None:
        """Update the processing status of the given ContentId and log to history.

        Args:
            content_id: The internal ContentId entity identifier.
            status: The new status enum transition state.
        """
        # Step 1: Open database connection
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Update the status of the record matching the ContentId string representation
            conn.execute(
                "XXUPDATE manifest SET status = ? WHERE content_id = ?XX",
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

    def xǁSQLiteManifestAdapterǁmark_status__mutmut_7(self, content_id: ContentId, status: ProcessingStatus) -> None:
        """Update the processing status of the given ContentId and log to history.

        Args:
            content_id: The internal ContentId entity identifier.
            status: The new status enum transition state.
        """
        # Step 1: Open database connection
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Update the status of the record matching the ContentId string representation
            conn.execute(
                "update manifest set status = ? where content_id = ?",
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

    def xǁSQLiteManifestAdapterǁmark_status__mutmut_8(self, content_id: ContentId, status: ProcessingStatus) -> None:
        """Update the processing status of the given ContentId and log to history.

        Args:
            content_id: The internal ContentId entity identifier.
            status: The new status enum transition state.
        """
        # Step 1: Open database connection
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Update the status of the record matching the ContentId string representation
            conn.execute(
                "UPDATE MANIFEST SET STATUS = ? WHERE CONTENT_ID = ?",
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

    def xǁSQLiteManifestAdapterǁmark_status__mutmut_9(self, content_id: ContentId, status: ProcessingStatus) -> None:
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
                (status.value, str(None))
            )
            # Step 3: Append the state transition log in the status_history table
            # Allows tracking history of processing pipelines for latency and bottleneck telemetry
            conn.execute(
                "INSERT INTO status_history (content_id, status) VALUES (?, ?)",
                (str(content_id), status.value)
            )
            # Step 4: Commit changes to persist the update
            conn.commit()

    def xǁSQLiteManifestAdapterǁmark_status__mutmut_10(self, content_id: ContentId, status: ProcessingStatus) -> None:
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
                None,
                (str(content_id), status.value)
            )
            # Step 4: Commit changes to persist the update
            conn.commit()

    def xǁSQLiteManifestAdapterǁmark_status__mutmut_11(self, content_id: ContentId, status: ProcessingStatus) -> None:
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
                None
            )
            # Step 4: Commit changes to persist the update
            conn.commit()

    def xǁSQLiteManifestAdapterǁmark_status__mutmut_12(self, content_id: ContentId, status: ProcessingStatus) -> None:
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
                (str(content_id), status.value)
            )
            # Step 4: Commit changes to persist the update
            conn.commit()

    def xǁSQLiteManifestAdapterǁmark_status__mutmut_13(self, content_id: ContentId, status: ProcessingStatus) -> None:
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
                )
            # Step 4: Commit changes to persist the update
            conn.commit()

    def xǁSQLiteManifestAdapterǁmark_status__mutmut_14(self, content_id: ContentId, status: ProcessingStatus) -> None:
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
                "XXINSERT INTO status_history (content_id, status) VALUES (?, ?)XX",
                (str(content_id), status.value)
            )
            # Step 4: Commit changes to persist the update
            conn.commit()

    def xǁSQLiteManifestAdapterǁmark_status__mutmut_15(self, content_id: ContentId, status: ProcessingStatus) -> None:
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
                "insert into status_history (content_id, status) values (?, ?)",
                (str(content_id), status.value)
            )
            # Step 4: Commit changes to persist the update
            conn.commit()

    def xǁSQLiteManifestAdapterǁmark_status__mutmut_16(self, content_id: ContentId, status: ProcessingStatus) -> None:
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
                "INSERT INTO STATUS_HISTORY (CONTENT_ID, STATUS) VALUES (?, ?)",
                (str(content_id), status.value)
            )
            # Step 4: Commit changes to persist the update
            conn.commit()

    def xǁSQLiteManifestAdapterǁmark_status__mutmut_17(self, content_id: ContentId, status: ProcessingStatus) -> None:
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
                (str(None), status.value)
            )
            # Step 4: Commit changes to persist the update
            conn.commit()
    
    xǁSQLiteManifestAdapterǁmark_status__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁSQLiteManifestAdapterǁmark_status__mutmut_1': xǁSQLiteManifestAdapterǁmark_status__mutmut_1, 
        'xǁSQLiteManifestAdapterǁmark_status__mutmut_2': xǁSQLiteManifestAdapterǁmark_status__mutmut_2, 
        'xǁSQLiteManifestAdapterǁmark_status__mutmut_3': xǁSQLiteManifestAdapterǁmark_status__mutmut_3, 
        'xǁSQLiteManifestAdapterǁmark_status__mutmut_4': xǁSQLiteManifestAdapterǁmark_status__mutmut_4, 
        'xǁSQLiteManifestAdapterǁmark_status__mutmut_5': xǁSQLiteManifestAdapterǁmark_status__mutmut_5, 
        'xǁSQLiteManifestAdapterǁmark_status__mutmut_6': xǁSQLiteManifestAdapterǁmark_status__mutmut_6, 
        'xǁSQLiteManifestAdapterǁmark_status__mutmut_7': xǁSQLiteManifestAdapterǁmark_status__mutmut_7, 
        'xǁSQLiteManifestAdapterǁmark_status__mutmut_8': xǁSQLiteManifestAdapterǁmark_status__mutmut_8, 
        'xǁSQLiteManifestAdapterǁmark_status__mutmut_9': xǁSQLiteManifestAdapterǁmark_status__mutmut_9, 
        'xǁSQLiteManifestAdapterǁmark_status__mutmut_10': xǁSQLiteManifestAdapterǁmark_status__mutmut_10, 
        'xǁSQLiteManifestAdapterǁmark_status__mutmut_11': xǁSQLiteManifestAdapterǁmark_status__mutmut_11, 
        'xǁSQLiteManifestAdapterǁmark_status__mutmut_12': xǁSQLiteManifestAdapterǁmark_status__mutmut_12, 
        'xǁSQLiteManifestAdapterǁmark_status__mutmut_13': xǁSQLiteManifestAdapterǁmark_status__mutmut_13, 
        'xǁSQLiteManifestAdapterǁmark_status__mutmut_14': xǁSQLiteManifestAdapterǁmark_status__mutmut_14, 
        'xǁSQLiteManifestAdapterǁmark_status__mutmut_15': xǁSQLiteManifestAdapterǁmark_status__mutmut_15, 
        'xǁSQLiteManifestAdapterǁmark_status__mutmut_16': xǁSQLiteManifestAdapterǁmark_status__mutmut_16, 
        'xǁSQLiteManifestAdapterǁmark_status__mutmut_17': xǁSQLiteManifestAdapterǁmark_status__mutmut_17
    }
    xǁSQLiteManifestAdapterǁmark_status__mutmut_orig.__name__ = 'xǁSQLiteManifestAdapterǁmark_status'

    def has_failed_previously(self, external_id: str) -> bool:
        args = [external_id]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_orig'), object.__getattribute__(self, 'xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_mutants'), args, kwargs, self)

    def xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_orig(self, external_id: str) -> bool:
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

    def xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_1(self, external_id: str) -> bool:
        """Check if an external ID has previously failed processing.

        Args:
            external_id: The external stream/source identifier.

        Returns:
            bool: True if status is currently set to FAILED, False otherwise.
        """
        # Step 1: Open database connection
        with sqlite3.connect(None) as conn:
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

    def xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_2(self, external_id: str) -> bool:
        """Check if an external ID has previously failed processing.

        Args:
            external_id: The external stream/source identifier.

        Returns:
            bool: True if status is currently set to FAILED, False otherwise.
        """
        # Step 1: Open database connection
        with sqlite3.connect(self.db_path) as conn:
            # Step 2: Create cursor to query database
            cursor = None
            # Step 3: Fetch the current status of the external ID
            cursor.execute("SELECT status FROM manifest WHERE external_id = ?", (external_id,))
            row = cursor.fetchone()
            
            # Step 4: Return False if no record exists
            if not row:
                return False
                
            # Step 5: Check if the saved status string is equal to FAILED
            return row[0] == ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_3(self, external_id: str) -> bool:
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
            cursor.execute(None, (external_id,))
            row = cursor.fetchone()
            
            # Step 4: Return False if no record exists
            if not row:
                return False
                
            # Step 5: Check if the saved status string is equal to FAILED
            return row[0] == ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_4(self, external_id: str) -> bool:
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
            cursor.execute("SELECT status FROM manifest WHERE external_id = ?", None)
            row = cursor.fetchone()
            
            # Step 4: Return False if no record exists
            if not row:
                return False
                
            # Step 5: Check if the saved status string is equal to FAILED
            return row[0] == ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_5(self, external_id: str) -> bool:
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
            cursor.execute((external_id,))
            row = cursor.fetchone()
            
            # Step 4: Return False if no record exists
            if not row:
                return False
                
            # Step 5: Check if the saved status string is equal to FAILED
            return row[0] == ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_6(self, external_id: str) -> bool:
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
            cursor.execute("SELECT status FROM manifest WHERE external_id = ?", )
            row = cursor.fetchone()
            
            # Step 4: Return False if no record exists
            if not row:
                return False
                
            # Step 5: Check if the saved status string is equal to FAILED
            return row[0] == ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_7(self, external_id: str) -> bool:
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
            cursor.execute("XXSELECT status FROM manifest WHERE external_id = ?XX", (external_id,))
            row = cursor.fetchone()
            
            # Step 4: Return False if no record exists
            if not row:
                return False
                
            # Step 5: Check if the saved status string is equal to FAILED
            return row[0] == ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_8(self, external_id: str) -> bool:
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
            cursor.execute("select status from manifest where external_id = ?", (external_id,))
            row = cursor.fetchone()
            
            # Step 4: Return False if no record exists
            if not row:
                return False
                
            # Step 5: Check if the saved status string is equal to FAILED
            return row[0] == ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_9(self, external_id: str) -> bool:
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
            cursor.execute("SELECT STATUS FROM MANIFEST WHERE EXTERNAL_ID = ?", (external_id,))
            row = cursor.fetchone()
            
            # Step 4: Return False if no record exists
            if not row:
                return False
                
            # Step 5: Check if the saved status string is equal to FAILED
            return row[0] == ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_10(self, external_id: str) -> bool:
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
            row = None
            
            # Step 4: Return False if no record exists
            if not row:
                return False
                
            # Step 5: Check if the saved status string is equal to FAILED
            return row[0] == ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_11(self, external_id: str) -> bool:
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
            if row:
                return False
                
            # Step 5: Check if the saved status string is equal to FAILED
            return row[0] == ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_12(self, external_id: str) -> bool:
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
                return True
                
            # Step 5: Check if the saved status string is equal to FAILED
            return row[0] == ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_13(self, external_id: str) -> bool:
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
            return row[1] == ProcessingStatus.FAILED.value

    def xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_14(self, external_id: str) -> bool:
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
            return row[0] != ProcessingStatus.FAILED.value
    
    xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_1': xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_1, 
        'xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_2': xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_2, 
        'xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_3': xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_3, 
        'xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_4': xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_4, 
        'xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_5': xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_5, 
        'xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_6': xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_6, 
        'xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_7': xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_7, 
        'xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_8': xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_8, 
        'xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_9': xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_9, 
        'xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_10': xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_10, 
        'xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_11': xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_11, 
        'xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_12': xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_12, 
        'xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_13': xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_13, 
        'xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_14': xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_14
    }
    xǁSQLiteManifestAdapterǁhas_failed_previously__mutmut_orig.__name__ = 'xǁSQLiteManifestAdapterǁhas_failed_previously'
