import yt_dlp
from pathlib import Path
from datetime import datetime, timezone
from isb.shared_kernel.types import ContentId
from isb.ingestion.domain.entities import MediaSource, MediaEpisode
from isb.ingestion.application.ports import MediaExtractorPort
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

class YtDlpExtractorAdapter(MediaExtractorPort):
    """Infrastructure adapter that implements the MediaExtractorPort using yt-dlp.

    This adapter manages the communication boundary between the Ingestion context
    and external media streams (e.g., YouTube), scraping and downloading raw audio
    material for subsequent downstream processing.

    Attributes:
        download_dir: The directory path where raw audio files will be persisted.
    """

    def __init__(self, download_dir: str | Path) -> None:
        args = [download_dir]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁYtDlpExtractorAdapterǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁYtDlpExtractorAdapterǁ__init____mutmut_mutants'), args, kwargs, self)

    def xǁYtDlpExtractorAdapterǁ__init____mutmut_orig(self, download_dir: str | Path) -> None:
        """Initializes the yt-dlp media extraction adapter.

        Args:
            download_dir: Directory path on the local filesystem where media should
                be downloaded and stored.
        """
        # Infrastructure limit: Direct filesystem I/O is required because raw audio extraction
        # must store the temporal payload locally before the transcription worker reads it.
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(parents=True, exist_ok=True)

    def xǁYtDlpExtractorAdapterǁ__init____mutmut_1(self, download_dir: str | Path) -> None:
        """Initializes the yt-dlp media extraction adapter.

        Args:
            download_dir: Directory path on the local filesystem where media should
                be downloaded and stored.
        """
        # Infrastructure limit: Direct filesystem I/O is required because raw audio extraction
        # must store the temporal payload locally before the transcription worker reads it.
        self.download_dir = None
        self.download_dir.mkdir(parents=True, exist_ok=True)

    def xǁYtDlpExtractorAdapterǁ__init____mutmut_2(self, download_dir: str | Path) -> None:
        """Initializes the yt-dlp media extraction adapter.

        Args:
            download_dir: Directory path on the local filesystem where media should
                be downloaded and stored.
        """
        # Infrastructure limit: Direct filesystem I/O is required because raw audio extraction
        # must store the temporal payload locally before the transcription worker reads it.
        self.download_dir = Path(None)
        self.download_dir.mkdir(parents=True, exist_ok=True)

    def xǁYtDlpExtractorAdapterǁ__init____mutmut_3(self, download_dir: str | Path) -> None:
        """Initializes the yt-dlp media extraction adapter.

        Args:
            download_dir: Directory path on the local filesystem where media should
                be downloaded and stored.
        """
        # Infrastructure limit: Direct filesystem I/O is required because raw audio extraction
        # must store the temporal payload locally before the transcription worker reads it.
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(parents=None, exist_ok=True)

    def xǁYtDlpExtractorAdapterǁ__init____mutmut_4(self, download_dir: str | Path) -> None:
        """Initializes the yt-dlp media extraction adapter.

        Args:
            download_dir: Directory path on the local filesystem where media should
                be downloaded and stored.
        """
        # Infrastructure limit: Direct filesystem I/O is required because raw audio extraction
        # must store the temporal payload locally before the transcription worker reads it.
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(parents=True, exist_ok=None)

    def xǁYtDlpExtractorAdapterǁ__init____mutmut_5(self, download_dir: str | Path) -> None:
        """Initializes the yt-dlp media extraction adapter.

        Args:
            download_dir: Directory path on the local filesystem where media should
                be downloaded and stored.
        """
        # Infrastructure limit: Direct filesystem I/O is required because raw audio extraction
        # must store the temporal payload locally before the transcription worker reads it.
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(exist_ok=True)

    def xǁYtDlpExtractorAdapterǁ__init____mutmut_6(self, download_dir: str | Path) -> None:
        """Initializes the yt-dlp media extraction adapter.

        Args:
            download_dir: Directory path on the local filesystem where media should
                be downloaded and stored.
        """
        # Infrastructure limit: Direct filesystem I/O is required because raw audio extraction
        # must store the temporal payload locally before the transcription worker reads it.
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(parents=True, )

    def xǁYtDlpExtractorAdapterǁ__init____mutmut_7(self, download_dir: str | Path) -> None:
        """Initializes the yt-dlp media extraction adapter.

        Args:
            download_dir: Directory path on the local filesystem where media should
                be downloaded and stored.
        """
        # Infrastructure limit: Direct filesystem I/O is required because raw audio extraction
        # must store the temporal payload locally before the transcription worker reads it.
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(parents=False, exist_ok=True)

    def xǁYtDlpExtractorAdapterǁ__init____mutmut_8(self, download_dir: str | Path) -> None:
        """Initializes the yt-dlp media extraction adapter.

        Args:
            download_dir: Directory path on the local filesystem where media should
                be downloaded and stored.
        """
        # Infrastructure limit: Direct filesystem I/O is required because raw audio extraction
        # must store the temporal payload locally before the transcription worker reads it.
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(parents=True, exist_ok=False)
    
    xǁYtDlpExtractorAdapterǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁYtDlpExtractorAdapterǁ__init____mutmut_1': xǁYtDlpExtractorAdapterǁ__init____mutmut_1, 
        'xǁYtDlpExtractorAdapterǁ__init____mutmut_2': xǁYtDlpExtractorAdapterǁ__init____mutmut_2, 
        'xǁYtDlpExtractorAdapterǁ__init____mutmut_3': xǁYtDlpExtractorAdapterǁ__init____mutmut_3, 
        'xǁYtDlpExtractorAdapterǁ__init____mutmut_4': xǁYtDlpExtractorAdapterǁ__init____mutmut_4, 
        'xǁYtDlpExtractorAdapterǁ__init____mutmut_5': xǁYtDlpExtractorAdapterǁ__init____mutmut_5, 
        'xǁYtDlpExtractorAdapterǁ__init____mutmut_6': xǁYtDlpExtractorAdapterǁ__init____mutmut_6, 
        'xǁYtDlpExtractorAdapterǁ__init____mutmut_7': xǁYtDlpExtractorAdapterǁ__init____mutmut_7, 
        'xǁYtDlpExtractorAdapterǁ__init____mutmut_8': xǁYtDlpExtractorAdapterǁ__init____mutmut_8
    }
    xǁYtDlpExtractorAdapterǁ__init____mutmut_orig.__name__ = 'xǁYtDlpExtractorAdapterǁ__init__'

    def fetch_new_episodes(self, source: MediaSource) -> list[MediaEpisode]:
        args = [source]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_orig'), object.__getattribute__(self, 'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_mutants'), args, kwargs, self)

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_orig(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_1(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = None
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_2(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "XXextract_flatXX": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_3(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "EXTRACT_FLAT": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_4(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": False,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_5(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "XXformatXX": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_6(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "FORMAT": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_7(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "XXbestaudio/bestXX",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_8(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "BESTAUDIO/BEST",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_9(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "XXplaylistendXX": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_10(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "PLAYLISTEND": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_11(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 6,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_12(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "XXquietXX": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_13(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "QUIET": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_14(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": False,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_15(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(None) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_16(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = None
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_17(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(None, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_18(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=None)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_19(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_20(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, )
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_21(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=True)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_22(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_23(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = None
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_24(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") and []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_25(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get(None) or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_26(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("XXentriesXX") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_27(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("ENTRIES") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_28(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = None
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_29(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = None
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_30(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get(None)
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_31(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("XXidXX")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_32(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("ID")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_33(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_34(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    break
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_35(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = None
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_36(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") and "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_37(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get(None) or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_38(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("XXtitleXX") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_39(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("TITLE") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_40(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "XXUnknown TitleXX"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_41(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "unknown title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_42(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "UNKNOWN TITLE"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_43(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = None
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_44(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get(None)
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_45(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("XXupload_dateXX")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_46(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("UPLOAD_DATE")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_47(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = None
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_48(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=None)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_49(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(None, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_50(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, None).replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_51(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime("%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_52(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, ).replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_53(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "XX%Y%m%dXX").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_54(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_55(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%M%D").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_56(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = None
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_57(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(None)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_58(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = None
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_59(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(None)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_60(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = None
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_61(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get(None)
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_62(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("XXdurationXX")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_63(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("DURATION")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_64(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = None
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_65(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(None) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_66(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 1
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_67(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    None
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_68(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=None,
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_69(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=None,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_70(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=None,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_71(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=None,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_72(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=None
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_73(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_74(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        title=title,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_75(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        published_at=published_at,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_76(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        duration_seconds=duration_seconds
                    )
                )
            
            return episodes

    def xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_77(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetches the latest metadata episodes from the external media source URL.

        Iterates through the external source's feed without downloading any media files,
        creating a collection of MediaEpisode domain entities representing ingestion candidates.

        Args:
            source: The MediaSource entity containing the target URL and metadata constraints.

        Returns:
            A list of MediaEpisode entities found at the source URL, limited by the
            ingestion window constraint (latest 5 episodes).
        """
        # Infrastructure limit: Flat extraction is used to optimize network traffic by retrieving metadata only,
        # and restricting the feed inspection to the last 5 episodes prevents API throttling and reduces bandwidth.
        ydl_opts = {
            "extract_flat": True,
            "format": "bestaudio/best",
            "playlistend": 5,
            "quiet": True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # External I/O boundary: Perform flat network lookup against the source provider URL.
            info = ydl.extract_info(source.url, download=False)
            if not info:
                return []
            
            entries = info.get("entries") or []
            episodes: list[MediaEpisode] = []
            
            for entry in entries:
                external_id = entry.get("id")
                if not external_id:
                    continue
                
                title = entry.get("title") or "Unknown Title"
                
                # Exception recovery: Fallback to the current system UTC time in case the external source feed publishes
                # malformed, missing, or unparseable date strings, ensuring downstream scheduling does not fail.
                upload_date_str = entry.get("upload_date")
                if upload_date_str:
                    try:
                        published_at = datetime.strptime(upload_date_str, "%Y%m%d").replace(tzinfo=timezone.utc)
                    except Exception:
                        published_at = datetime.now(timezone.utc)
                else:
                    published_at = datetime.now(timezone.utc)
                
                duration = entry.get("duration")
                duration_seconds = int(duration) if duration else 0
                
                episodes.append(
                    MediaEpisode(
                        content_id=ContentId.generate(),
                        external_id=external_id,
                        title=title,
                        published_at=published_at,
                        )
                )
            
            return episodes
    
    xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_1': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_1, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_2': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_2, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_3': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_3, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_4': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_4, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_5': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_5, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_6': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_6, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_7': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_7, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_8': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_8, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_9': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_9, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_10': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_10, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_11': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_11, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_12': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_12, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_13': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_13, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_14': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_14, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_15': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_15, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_16': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_16, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_17': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_17, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_18': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_18, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_19': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_19, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_20': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_20, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_21': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_21, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_22': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_22, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_23': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_23, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_24': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_24, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_25': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_25, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_26': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_26, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_27': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_27, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_28': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_28, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_29': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_29, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_30': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_30, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_31': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_31, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_32': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_32, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_33': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_33, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_34': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_34, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_35': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_35, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_36': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_36, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_37': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_37, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_38': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_38, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_39': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_39, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_40': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_40, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_41': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_41, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_42': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_42, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_43': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_43, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_44': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_44, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_45': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_45, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_46': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_46, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_47': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_47, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_48': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_48, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_49': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_49, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_50': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_50, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_51': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_51, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_52': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_52, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_53': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_53, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_54': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_54, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_55': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_55, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_56': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_56, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_57': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_57, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_58': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_58, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_59': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_59, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_60': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_60, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_61': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_61, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_62': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_62, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_63': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_63, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_64': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_64, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_65': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_65, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_66': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_66, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_67': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_67, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_68': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_68, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_69': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_69, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_70': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_70, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_71': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_71, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_72': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_72, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_73': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_73, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_74': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_74, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_75': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_75, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_76': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_76, 
        'xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_77': xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_77
    }
    xǁYtDlpExtractorAdapterǁfetch_new_episodes__mutmut_orig.__name__ = 'xǁYtDlpExtractorAdapterǁfetch_new_episodes'

    def extract_audio(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        args = [episode]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_orig'), object.__getattribute__(self, 'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_mutants'), args, kwargs, self)

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_orig(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_1(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = None
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_2(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(None)
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_3(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir * f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_4(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = None
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_5(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "XXformatXX": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_6(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "FORMAT": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_7(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "XXbestaudio/bestXX",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_8(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "BESTAUDIO/BEST",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_9(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "XXouttmplXX": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_10(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "OUTTMPL": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_11(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "XXquietXX": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_12(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "QUIET": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_13(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": False,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_14(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "XXpostprocessorsXX": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_15(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "POSTPROCESSORS": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_16(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "XXkeyXX": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_17(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "KEY": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_18(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "XXFFmpegExtractAudioXX",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_19(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "ffmpegextractaudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_20(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFMPEGEXTRACTAUDIO",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_21(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "XXpreferredcodecXX": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_22(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "PREFERREDCODEC": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_23(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "XXmp3XX",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_24(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "MP3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_25(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "XXpreferredqualityXX": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_26(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "PREFERREDQUALITY": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_27(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "XX192XX",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_28(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(None) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_29(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = None
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_30(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download(None)
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_31(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = None
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_32(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir * f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_33(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_34(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(None)
        
        size_bytes = target_path.stat().st_size
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_35(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = None
        return target_path, "mp3", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_36(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "XXmp3XX", size_bytes

    def xǁYtDlpExtractorAdapterǁextract_audio__mutmut_37(self, episode: MediaEpisode) -> tuple[Path, str, int]:
        """Downloads and extracts the audio channel from the target media episode.

        Fetches the raw media from the external source, post-processes it into the
        standard internal audio format (MP3) at a constant bitrate, and tracks file metrics.

        Args:
            episode: The MediaEpisode entity containing the external ID of the target content.

        Returns:
            A tuple containing:
                - Path: The absolute local Path to the extracted audio file.
                - str: The encoding format identifier (always "mp3").
                - int: The size of the extracted file in bytes.

        Raises:
            FileNotFoundError: If the downloaded file is missing on the filesystem after
                yt-dlp execution completes.
        """
        # Infrastructure limit: Save raw media files using a predictable name template bound to the
        # unique external ID to ensure download idempotency and avoid duplicate file downloads.
        output_template = str(self.download_dir / f"{episode.external_id}.%(ext)s")
        
        # Infrastructure limit: FFmpeg is forced to extract audio and transcode it to MP3 at 192kbps.
        # This standardizes input codecs for downstream Whisper transcription while managing local disk saturation.
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            watch_url = f"https://www.youtube.com/watch?v={episode.external_id}"
            ydl.download([watch_url])
        
        # Exception handling: Ensure the file was generated and is accessible on disk.
        # Downstream Whisper transcription depends on the local existence of the audio artifact.
        target_path = self.download_dir / f"{episode.external_id}.mp3"
        if not target_path.exists():
            raise FileNotFoundError(f"Extracted audio file not found at {target_path}")
        
        size_bytes = target_path.stat().st_size
        return target_path, "MP3", size_bytes
    
    xǁYtDlpExtractorAdapterǁextract_audio__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_1': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_1, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_2': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_2, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_3': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_3, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_4': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_4, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_5': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_5, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_6': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_6, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_7': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_7, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_8': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_8, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_9': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_9, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_10': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_10, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_11': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_11, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_12': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_12, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_13': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_13, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_14': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_14, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_15': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_15, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_16': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_16, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_17': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_17, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_18': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_18, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_19': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_19, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_20': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_20, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_21': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_21, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_22': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_22, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_23': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_23, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_24': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_24, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_25': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_25, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_26': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_26, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_27': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_27, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_28': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_28, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_29': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_29, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_30': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_30, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_31': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_31, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_32': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_32, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_33': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_33, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_34': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_34, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_35': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_35, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_36': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_36, 
        'xǁYtDlpExtractorAdapterǁextract_audio__mutmut_37': xǁYtDlpExtractorAdapterǁextract_audio__mutmut_37
    }
    xǁYtDlpExtractorAdapterǁextract_audio__mutmut_orig.__name__ = 'xǁYtDlpExtractorAdapterǁextract_audio'
