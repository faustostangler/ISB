import logging
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.shared_kernel.events import EventBus, AudioExtracted
from isb.ingestion.domain.entities import MediaSource, MediaEpisode
from isb.ingestion.application.ports import MediaExtractorPort, ManifestPort

logger = logging.getLogger(__name__)

class ExtractAudioUseCase:
    """Orchestrates the ingestion pipeline step for fetching metadata and extracting audio.

    Fetches episodes metadata from the target URL, executes downloads/extraction of the audio files
    for new/previously-failed items, registers their unique system identifiers, and raises domain
    events to coordinate transcription asynchronously.
    """

    def __init__(
        self,
        extractor_port: MediaExtractorPort,
        manifest_port: ManifestPort,
        event_bus: EventBus
    ) -> None:
        """Initialize the use case with required infrastructure ports and event dispatcher.

        Args:
            extractor_port: Adapter implementing MediaExtractorPort to fetch and download media.
            manifest_port: Adapter implementing ManifestPort to track idempotency state history.
            event_bus: EventBus instance to broadcast events.
        """
        # Step 1: Wire infrastructure ports and registries via constructor injection
        # This keeps the application logic decoupled from specific library or DB implementations
        self.extractor = extractor_port
        self.manifest = manifest_port
        self.event_bus = event_bus

    def execute(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetch and extract audio for all new/unprocessed episodes from a source.

        Args:
            source: The MediaSource entity being synced.

        Returns:
            list[MediaEpisode]: List of episodes processed during this sync execution block.
        """
        # Step 1: Initialize the tracking list for episodes processed in this batch run
        processed_episodes: list[MediaEpisode] = []
        
        # Step 2: Query the media extractor port to identify all current/recent episodes from the source URL
        new_episodes = self.extractor.fetch_new_episodes(source)

        # Step 3: Iterate through each identified episode to process it
        for episode in new_episodes:
            ext_id = episode.external_id
            
            # Step 4: Perform the Idempotency Check
            # We skip downloading if the manifest registry reports that this external ID
            # is currently active or has been completed, avoiding duplicate bandwidth usage.
            if self.manifest.is_processed(ext_id):
                logger.info("Episode %s already processed. Skipping.", ext_id)
                continue

            # Step 5: Assign or recover the internal globally unique ContentId
            if self.manifest.has_failed_previously(ext_id):
                # Retry scenario: Retrieve the pre-existing system-wide ContentId from the database
                # to maintain trace history and avoid generating disconnected records.
                existing_cid = self.manifest.get_content_id(ext_id)
                if existing_cid is None:
                    # Fallback boundary: If somehow the ID is lost, generate a new one and register
                    existing_cid = ContentId.generate()
                    self.manifest.register_episode(ext_id, existing_cid)
                episode.content_id = existing_cid
                logger.info("Retrying previously failed episode %s with ContentId %s", ext_id, episode.content_id)
            else:
                # Fresh scenario: Generate a new UUID content token and register it in the manifest registry
                episode.content_id = ContentId.generate()
                self.manifest.register_episode(ext_id, episode.content_id)
                logger.info("Registered new episode %s with ContentId %s", ext_id, episode.content_id)

            # Step 6: Mark progress status as EXTRACTING
            # Informs concurrent query workers that this content ID is actively being downloaded.
            self.manifest.mark_status(episode.content_id, ProcessingStatus.EXTRACTING)

            # Step 7: Perform file extraction wrapped in exception safety blocks
            try:
                # Retrieve local file path, file format, and size in bytes from the extractor adapter
                audio_path, file_format, size_bytes = self.extractor.extract_audio(episode)
                
                # Update domain entity state to bind the extracted AudioTrack VO
                episode.mark_extracted(audio_path, file_format, size_bytes)
                
                # Step 8: Update manifest status to next step (TRANSCRIBING) in SQLite registry
                self.manifest.mark_status(episode.content_id, ProcessingStatus.TRANSCRIBING)
                
                # Append to source aggregate tracking list and batch result list
                source.add_episode(episode)
                processed_episodes.append(episode)

                # Step 9: Construct and publish the AudioExtracted domain event
                # This decouples the ingestion use case from the transcription use case,
                # triggering speech-to-text processing asynchronously via the event bus.
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
                # Step 10: Graceful failure handling
                # Mark entity as failed, record FAILED status in database registry, and continue batch.
                # This prevents a single network/extractor timeout from halting the entire sync pipeline.
                logger.exception("Failed to extract audio for episode %s.", ext_id)
                episode.mark_failed()
                self.manifest.mark_status(episode.content_id, ProcessingStatus.FAILED)
                processed_episodes.append(episode)

        # Step 11: Mark the media source aggregate sync datetime stamp
        source.mark_synced()
        
        # Step 12: Return list of processed episodes
        return processed_episodes
