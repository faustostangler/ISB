import yt_dlp
from pathlib import Path
from datetime import datetime, timezone
from isb.shared_kernel.types import ContentId
from isb.ingestion.domain.entities import MediaSource, MediaEpisode
from isb.ingestion.application.ports import MediaExtractorPort

class YtDlpExtractorAdapter(MediaExtractorPort):
    """Infrastructure adapter that implements the MediaExtractorPort using yt-dlp.

    This adapter manages the communication boundary between the Ingestion context
    and external media streams (e.g., YouTube), scraping and downloading raw audio
    material for subsequent downstream processing.

    Attributes:
        download_dir: The directory path where raw audio files will be persisted.
    """

    def __init__(self, download_dir: str | Path) -> None:
        """Initializes the yt-dlp media extraction adapter.

        Args:
            download_dir: Directory path on the local filesystem where media should
                be downloaded and stored.
        """
        # Infrastructure limit: Direct filesystem I/O is required because raw audio extraction
        # must store the temporal payload locally before the transcription worker reads it.
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(parents=True, exist_ok=True)

    def fetch_new_episodes(self, source: MediaSource) -> list[MediaEpisode]:
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

    def extract_audio(self, episode: MediaEpisode) -> tuple[Path, str, int]:
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
