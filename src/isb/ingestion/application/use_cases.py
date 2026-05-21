import logging
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.shared_kernel.events import EventBus, AudioExtracted
from isb.ingestion.domain.entities import MediaSource, MediaEpisode
from isb.ingestion.application.ports import MediaExtractorPort, ManifestPort

logger = logging.getLogger(__name__)

class ExtractAudioUseCase:
    """Orchestrates the ingestion pipeline step for fetching metadata and extracting audio."""

    def __init__(
        self,
        extractor_port: MediaExtractorPort,
        manifest_port: ManifestPort,
        event_bus: EventBus
    ) -> None:
        self.extractor = extractor_port
        self.manifest = manifest_port
        self.event_bus = event_bus

    def execute(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetch and extract audio for all new/unprocessed episodes from a source."""
        processed_episodes: list[MediaEpisode] = []
        new_episodes = self.extractor.fetch_new_episodes(source)

        for episode in new_episodes:
            ext_id = episode.external_id
            
            # 1. Idempotency Check
            if self.manifest.is_processed(ext_id):
                logger.info("Episode %s already processed. Skipping.", ext_id)
                continue

            # 2. Get or Assign ContentId (UUIDv4)
            if self.manifest.has_failed_previously(ext_id):
                existing_cid = self.manifest.get_content_id(ext_id)
                if existing_cid is None:
                    # Fallback if somehow missing
                    existing_cid = ContentId.generate()
                    self.manifest.register_episode(ext_id, existing_cid)
                episode.content_id = existing_cid
                logger.info("Retrying previously failed episode %s with ContentId %s", ext_id, episode.content_id)
            else:
                # Completely new episode
                episode.content_id = ContentId.generate()
                self.manifest.register_episode(ext_id, episode.content_id)
                logger.info("Registered new episode %s with ContentId %s", ext_id, episode.content_id)

            self.manifest.mark_status(episode.content_id, ProcessingStatus.EXTRACTING)

            # 3. Audio Extraction via Port Adapter
            try:
                audio_path, file_format, size_bytes = self.extractor.extract_audio(episode)
                episode.mark_extracted(audio_path, file_format, size_bytes)
                
                # Update manifest status to next step (TRANSCRIBING)
                self.manifest.mark_status(episode.content_id, ProcessingStatus.TRANSCRIBING)
                
                # Register to tracking lists
                source.add_episode(episode)
                processed_episodes.append(episode)

                # 4. Emit domain event
                event = AudioExtracted(
                    content_id=episode.content_id,
                    audio_path=audio_path,
                    metadata={
                        "title": episode.title,
                        "external_id": episode.external_id,
                        "duration_seconds": episode.duration_seconds,
                        "published_at": episode.published_at.isoformat(),
                    }
                )
                self.event_bus.publish(event)
                logger.info("Successfully extracted audio for %s and published event.", ext_id)

            except Exception as err:
                logger.exception("Failed to extract audio for episode %s.", ext_id)
                episode.mark_failed()
                self.manifest.mark_status(episode.content_id, ProcessingStatus.FAILED)
                processed_episodes.append(episode)

        source.mark_synced()
        return processed_episodes
