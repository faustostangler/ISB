import logging
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.shared_kernel.events import EventBus, AudioExtracted
from isb.ingestion.domain.entities import MediaSource, MediaEpisode
from isb.ingestion.application.ports import MediaExtractorPort, ManifestPort

logger = logging.getLogger(__name__)
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
        args = [extractor_port, manifest_port, event_bus]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁExtractAudioUseCaseǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁExtractAudioUseCaseǁ__init____mutmut_mutants'), args, kwargs, self)

    def xǁExtractAudioUseCaseǁ__init____mutmut_orig(
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

    def xǁExtractAudioUseCaseǁ__init____mutmut_1(
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
        self.extractor = None
        self.manifest = manifest_port
        self.event_bus = event_bus

    def xǁExtractAudioUseCaseǁ__init____mutmut_2(
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
        self.manifest = None
        self.event_bus = event_bus

    def xǁExtractAudioUseCaseǁ__init____mutmut_3(
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
        self.event_bus = None
    
    xǁExtractAudioUseCaseǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁExtractAudioUseCaseǁ__init____mutmut_1': xǁExtractAudioUseCaseǁ__init____mutmut_1, 
        'xǁExtractAudioUseCaseǁ__init____mutmut_2': xǁExtractAudioUseCaseǁ__init____mutmut_2, 
        'xǁExtractAudioUseCaseǁ__init____mutmut_3': xǁExtractAudioUseCaseǁ__init____mutmut_3
    }
    xǁExtractAudioUseCaseǁ__init____mutmut_orig.__name__ = 'xǁExtractAudioUseCaseǁ__init__'

    def execute(self, source: MediaSource) -> list[MediaEpisode]:
        args = [source]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁExtractAudioUseCaseǁexecute__mutmut_orig'), object.__getattribute__(self, 'xǁExtractAudioUseCaseǁexecute__mutmut_mutants'), args, kwargs, self)

    def xǁExtractAudioUseCaseǁexecute__mutmut_orig(self, source: MediaSource) -> list[MediaEpisode]:
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_1(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetch and extract audio for all new/unprocessed episodes from a source.

        Args:
            source: The MediaSource entity being synced.

        Returns:
            list[MediaEpisode]: List of episodes processed during this sync execution block.
        """
        # Step 1: Initialize the tracking list for episodes processed in this batch run
        processed_episodes: list[MediaEpisode] = None
        
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_2(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetch and extract audio for all new/unprocessed episodes from a source.

        Args:
            source: The MediaSource entity being synced.

        Returns:
            list[MediaEpisode]: List of episodes processed during this sync execution block.
        """
        # Step 1: Initialize the tracking list for episodes processed in this batch run
        processed_episodes: list[MediaEpisode] = []
        
        # Step 2: Query the media extractor port to identify all current/recent episodes from the source URL
        new_episodes = None

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_3(self, source: MediaSource) -> list[MediaEpisode]:
        """Fetch and extract audio for all new/unprocessed episodes from a source.

        Args:
            source: The MediaSource entity being synced.

        Returns:
            list[MediaEpisode]: List of episodes processed during this sync execution block.
        """
        # Step 1: Initialize the tracking list for episodes processed in this batch run
        processed_episodes: list[MediaEpisode] = []
        
        # Step 2: Query the media extractor port to identify all current/recent episodes from the source URL
        new_episodes = self.extractor.fetch_new_episodes(None)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_4(self, source: MediaSource) -> list[MediaEpisode]:
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
            ext_id = None
            
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_5(self, source: MediaSource) -> list[MediaEpisode]:
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
            if self.manifest.is_processed(None):
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_6(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info(None, ext_id)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_7(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("Episode %s already processed. Skipping.", None)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_8(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info(ext_id)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_9(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("Episode %s already processed. Skipping.", )
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_10(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("XXEpisode %s already processed. Skipping.XX", ext_id)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_11(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("episode %s already processed. skipping.", ext_id)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_12(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("EPISODE %S ALREADY PROCESSED. SKIPPING.", ext_id)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_13(self, source: MediaSource) -> list[MediaEpisode]:
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
                break

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_14(self, source: MediaSource) -> list[MediaEpisode]:
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
            if self.manifest.has_failed_previously(None):
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_15(self, source: MediaSource) -> list[MediaEpisode]:
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
                existing_cid = None
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_16(self, source: MediaSource) -> list[MediaEpisode]:
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
                existing_cid = self.manifest.get_content_id(None)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_17(self, source: MediaSource) -> list[MediaEpisode]:
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
                if existing_cid is not None:
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_18(self, source: MediaSource) -> list[MediaEpisode]:
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
                    existing_cid = None
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_19(self, source: MediaSource) -> list[MediaEpisode]:
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
                    self.manifest.register_episode(None, existing_cid)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_20(self, source: MediaSource) -> list[MediaEpisode]:
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
                    self.manifest.register_episode(ext_id, None)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_21(self, source: MediaSource) -> list[MediaEpisode]:
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
                    self.manifest.register_episode(existing_cid)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_22(self, source: MediaSource) -> list[MediaEpisode]:
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
                    self.manifest.register_episode(ext_id, )
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_23(self, source: MediaSource) -> list[MediaEpisode]:
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
                episode.content_id = None
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_24(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info(None, ext_id, episode.content_id)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_25(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("Retrying previously failed episode %s with ContentId %s", None, episode.content_id)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_26(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("Retrying previously failed episode %s with ContentId %s", ext_id, None)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_27(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info(ext_id, episode.content_id)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_28(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("Retrying previously failed episode %s with ContentId %s", episode.content_id)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_29(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("Retrying previously failed episode %s with ContentId %s", ext_id, )
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_30(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("XXRetrying previously failed episode %s with ContentId %sXX", ext_id, episode.content_id)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_31(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("retrying previously failed episode %s with contentid %s", ext_id, episode.content_id)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_32(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("RETRYING PREVIOUSLY FAILED EPISODE %S WITH CONTENTID %S", ext_id, episode.content_id)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_33(self, source: MediaSource) -> list[MediaEpisode]:
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
                episode.content_id = None
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_34(self, source: MediaSource) -> list[MediaEpisode]:
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
                self.manifest.register_episode(None, episode.content_id)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_35(self, source: MediaSource) -> list[MediaEpisode]:
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
                self.manifest.register_episode(ext_id, None)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_36(self, source: MediaSource) -> list[MediaEpisode]:
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
                self.manifest.register_episode(episode.content_id)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_37(self, source: MediaSource) -> list[MediaEpisode]:
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
                self.manifest.register_episode(ext_id, )
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_38(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info(None, ext_id, episode.content_id)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_39(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("Registered new episode %s with ContentId %s", None, episode.content_id)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_40(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("Registered new episode %s with ContentId %s", ext_id, None)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_41(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info(ext_id, episode.content_id)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_42(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("Registered new episode %s with ContentId %s", episode.content_id)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_43(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("Registered new episode %s with ContentId %s", ext_id, )

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_44(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("XXRegistered new episode %s with ContentId %sXX", ext_id, episode.content_id)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_45(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("registered new episode %s with contentid %s", ext_id, episode.content_id)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_46(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("REGISTERED NEW EPISODE %S WITH CONTENTID %S", ext_id, episode.content_id)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_47(self, source: MediaSource) -> list[MediaEpisode]:
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
            self.manifest.mark_status(None, ProcessingStatus.EXTRACTING)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_48(self, source: MediaSource) -> list[MediaEpisode]:
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
            self.manifest.mark_status(episode.content_id, None)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_49(self, source: MediaSource) -> list[MediaEpisode]:
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
            self.manifest.mark_status(ProcessingStatus.EXTRACTING)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_50(self, source: MediaSource) -> list[MediaEpisode]:
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
            self.manifest.mark_status(episode.content_id, )

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_51(self, source: MediaSource) -> list[MediaEpisode]:
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
                audio_path, file_format, size_bytes = None
                
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_52(self, source: MediaSource) -> list[MediaEpisode]:
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
                audio_path, file_format, size_bytes = self.extractor.extract_audio(None)
                
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_53(self, source: MediaSource) -> list[MediaEpisode]:
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
                episode.mark_extracted(None, file_format, size_bytes)
                
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_54(self, source: MediaSource) -> list[MediaEpisode]:
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
                episode.mark_extracted(audio_path, None, size_bytes)
                
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_55(self, source: MediaSource) -> list[MediaEpisode]:
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
                episode.mark_extracted(audio_path, file_format, None)
                
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_56(self, source: MediaSource) -> list[MediaEpisode]:
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
                episode.mark_extracted(file_format, size_bytes)
                
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_57(self, source: MediaSource) -> list[MediaEpisode]:
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
                episode.mark_extracted(audio_path, size_bytes)
                
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_58(self, source: MediaSource) -> list[MediaEpisode]:
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
                episode.mark_extracted(audio_path, file_format, )
                
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_59(self, source: MediaSource) -> list[MediaEpisode]:
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
                self.manifest.mark_status(None, ProcessingStatus.TRANSCRIBING)
                
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_60(self, source: MediaSource) -> list[MediaEpisode]:
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
                self.manifest.mark_status(episode.content_id, None)
                
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_61(self, source: MediaSource) -> list[MediaEpisode]:
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
                self.manifest.mark_status(ProcessingStatus.TRANSCRIBING)
                
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_62(self, source: MediaSource) -> list[MediaEpisode]:
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
                self.manifest.mark_status(episode.content_id, )
                
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_63(self, source: MediaSource) -> list[MediaEpisode]:
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
                source.add_episode(None)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_64(self, source: MediaSource) -> list[MediaEpisode]:
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
                processed_episodes.append(None)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_65(self, source: MediaSource) -> list[MediaEpisode]:
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
                event = None
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_66(self, source: MediaSource) -> list[MediaEpisode]:
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
                    content_id=None,
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_67(self, source: MediaSource) -> list[MediaEpisode]:
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
                    audio_path=None,
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_68(self, source: MediaSource) -> list[MediaEpisode]:
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
                    metadata=None
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_69(self, source: MediaSource) -> list[MediaEpisode]:
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_70(self, source: MediaSource) -> list[MediaEpisode]:
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_71(self, source: MediaSource) -> list[MediaEpisode]:
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_72(self, source: MediaSource) -> list[MediaEpisode]:
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
                        "XXtitleXX": episode.title,
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_73(self, source: MediaSource) -> list[MediaEpisode]:
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
                        "TITLE": episode.title,
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_74(self, source: MediaSource) -> list[MediaEpisode]:
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
                        "XXexternal_idXX": episode.external_id,
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_75(self, source: MediaSource) -> list[MediaEpisode]:
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
                        "EXTERNAL_ID": episode.external_id,
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_76(self, source: MediaSource) -> list[MediaEpisode]:
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
                        "XXduration_secondsXX": episode.duration_seconds,
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_77(self, source: MediaSource) -> list[MediaEpisode]:
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
                        "DURATION_SECONDS": episode.duration_seconds,
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_78(self, source: MediaSource) -> list[MediaEpisode]:
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
                        "XXpublished_atXX": episode.published_at.isoformat(),
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_79(self, source: MediaSource) -> list[MediaEpisode]:
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
                        "PUBLISHED_AT": episode.published_at.isoformat(),
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_80(self, source: MediaSource) -> list[MediaEpisode]:
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
                self.event_bus.publish(None)
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

    def xǁExtractAudioUseCaseǁexecute__mutmut_81(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info(None, ext_id)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_82(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("Successfully extracted audio for %s and published event.", None)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_83(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info(ext_id)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_84(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("Successfully extracted audio for %s and published event.", )

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_85(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("XXSuccessfully extracted audio for %s and published event.XX", ext_id)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_86(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("successfully extracted audio for %s and published event.", ext_id)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_87(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.info("SUCCESSFULLY EXTRACTED AUDIO FOR %S AND PUBLISHED EVENT.", ext_id)

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

    def xǁExtractAudioUseCaseǁexecute__mutmut_88(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.exception(None, ext_id)
                episode.mark_failed()
                self.manifest.mark_status(episode.content_id, ProcessingStatus.FAILED)
                processed_episodes.append(episode)

        # Step 11: Mark the media source aggregate sync datetime stamp
        source.mark_synced()
        
        # Step 12: Return list of processed episodes
        return processed_episodes

    def xǁExtractAudioUseCaseǁexecute__mutmut_89(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.exception("Failed to extract audio for episode %s.", None)
                episode.mark_failed()
                self.manifest.mark_status(episode.content_id, ProcessingStatus.FAILED)
                processed_episodes.append(episode)

        # Step 11: Mark the media source aggregate sync datetime stamp
        source.mark_synced()
        
        # Step 12: Return list of processed episodes
        return processed_episodes

    def xǁExtractAudioUseCaseǁexecute__mutmut_90(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.exception(ext_id)
                episode.mark_failed()
                self.manifest.mark_status(episode.content_id, ProcessingStatus.FAILED)
                processed_episodes.append(episode)

        # Step 11: Mark the media source aggregate sync datetime stamp
        source.mark_synced()
        
        # Step 12: Return list of processed episodes
        return processed_episodes

    def xǁExtractAudioUseCaseǁexecute__mutmut_91(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.exception("Failed to extract audio for episode %s.", )
                episode.mark_failed()
                self.manifest.mark_status(episode.content_id, ProcessingStatus.FAILED)
                processed_episodes.append(episode)

        # Step 11: Mark the media source aggregate sync datetime stamp
        source.mark_synced()
        
        # Step 12: Return list of processed episodes
        return processed_episodes

    def xǁExtractAudioUseCaseǁexecute__mutmut_92(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.exception("XXFailed to extract audio for episode %s.XX", ext_id)
                episode.mark_failed()
                self.manifest.mark_status(episode.content_id, ProcessingStatus.FAILED)
                processed_episodes.append(episode)

        # Step 11: Mark the media source aggregate sync datetime stamp
        source.mark_synced()
        
        # Step 12: Return list of processed episodes
        return processed_episodes

    def xǁExtractAudioUseCaseǁexecute__mutmut_93(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.exception("failed to extract audio for episode %s.", ext_id)
                episode.mark_failed()
                self.manifest.mark_status(episode.content_id, ProcessingStatus.FAILED)
                processed_episodes.append(episode)

        # Step 11: Mark the media source aggregate sync datetime stamp
        source.mark_synced()
        
        # Step 12: Return list of processed episodes
        return processed_episodes

    def xǁExtractAudioUseCaseǁexecute__mutmut_94(self, source: MediaSource) -> list[MediaEpisode]:
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
                logger.exception("FAILED TO EXTRACT AUDIO FOR EPISODE %S.", ext_id)
                episode.mark_failed()
                self.manifest.mark_status(episode.content_id, ProcessingStatus.FAILED)
                processed_episodes.append(episode)

        # Step 11: Mark the media source aggregate sync datetime stamp
        source.mark_synced()
        
        # Step 12: Return list of processed episodes
        return processed_episodes

    def xǁExtractAudioUseCaseǁexecute__mutmut_95(self, source: MediaSource) -> list[MediaEpisode]:
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
                self.manifest.mark_status(None, ProcessingStatus.FAILED)
                processed_episodes.append(episode)

        # Step 11: Mark the media source aggregate sync datetime stamp
        source.mark_synced()
        
        # Step 12: Return list of processed episodes
        return processed_episodes

    def xǁExtractAudioUseCaseǁexecute__mutmut_96(self, source: MediaSource) -> list[MediaEpisode]:
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
                self.manifest.mark_status(episode.content_id, None)
                processed_episodes.append(episode)

        # Step 11: Mark the media source aggregate sync datetime stamp
        source.mark_synced()
        
        # Step 12: Return list of processed episodes
        return processed_episodes

    def xǁExtractAudioUseCaseǁexecute__mutmut_97(self, source: MediaSource) -> list[MediaEpisode]:
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
                self.manifest.mark_status(ProcessingStatus.FAILED)
                processed_episodes.append(episode)

        # Step 11: Mark the media source aggregate sync datetime stamp
        source.mark_synced()
        
        # Step 12: Return list of processed episodes
        return processed_episodes

    def xǁExtractAudioUseCaseǁexecute__mutmut_98(self, source: MediaSource) -> list[MediaEpisode]:
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
                self.manifest.mark_status(episode.content_id, )
                processed_episodes.append(episode)

        # Step 11: Mark the media source aggregate sync datetime stamp
        source.mark_synced()
        
        # Step 12: Return list of processed episodes
        return processed_episodes

    def xǁExtractAudioUseCaseǁexecute__mutmut_99(self, source: MediaSource) -> list[MediaEpisode]:
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
                processed_episodes.append(None)

        # Step 11: Mark the media source aggregate sync datetime stamp
        source.mark_synced()
        
        # Step 12: Return list of processed episodes
        return processed_episodes
    
    xǁExtractAudioUseCaseǁexecute__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁExtractAudioUseCaseǁexecute__mutmut_1': xǁExtractAudioUseCaseǁexecute__mutmut_1, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_2': xǁExtractAudioUseCaseǁexecute__mutmut_2, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_3': xǁExtractAudioUseCaseǁexecute__mutmut_3, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_4': xǁExtractAudioUseCaseǁexecute__mutmut_4, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_5': xǁExtractAudioUseCaseǁexecute__mutmut_5, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_6': xǁExtractAudioUseCaseǁexecute__mutmut_6, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_7': xǁExtractAudioUseCaseǁexecute__mutmut_7, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_8': xǁExtractAudioUseCaseǁexecute__mutmut_8, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_9': xǁExtractAudioUseCaseǁexecute__mutmut_9, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_10': xǁExtractAudioUseCaseǁexecute__mutmut_10, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_11': xǁExtractAudioUseCaseǁexecute__mutmut_11, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_12': xǁExtractAudioUseCaseǁexecute__mutmut_12, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_13': xǁExtractAudioUseCaseǁexecute__mutmut_13, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_14': xǁExtractAudioUseCaseǁexecute__mutmut_14, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_15': xǁExtractAudioUseCaseǁexecute__mutmut_15, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_16': xǁExtractAudioUseCaseǁexecute__mutmut_16, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_17': xǁExtractAudioUseCaseǁexecute__mutmut_17, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_18': xǁExtractAudioUseCaseǁexecute__mutmut_18, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_19': xǁExtractAudioUseCaseǁexecute__mutmut_19, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_20': xǁExtractAudioUseCaseǁexecute__mutmut_20, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_21': xǁExtractAudioUseCaseǁexecute__mutmut_21, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_22': xǁExtractAudioUseCaseǁexecute__mutmut_22, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_23': xǁExtractAudioUseCaseǁexecute__mutmut_23, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_24': xǁExtractAudioUseCaseǁexecute__mutmut_24, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_25': xǁExtractAudioUseCaseǁexecute__mutmut_25, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_26': xǁExtractAudioUseCaseǁexecute__mutmut_26, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_27': xǁExtractAudioUseCaseǁexecute__mutmut_27, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_28': xǁExtractAudioUseCaseǁexecute__mutmut_28, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_29': xǁExtractAudioUseCaseǁexecute__mutmut_29, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_30': xǁExtractAudioUseCaseǁexecute__mutmut_30, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_31': xǁExtractAudioUseCaseǁexecute__mutmut_31, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_32': xǁExtractAudioUseCaseǁexecute__mutmut_32, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_33': xǁExtractAudioUseCaseǁexecute__mutmut_33, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_34': xǁExtractAudioUseCaseǁexecute__mutmut_34, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_35': xǁExtractAudioUseCaseǁexecute__mutmut_35, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_36': xǁExtractAudioUseCaseǁexecute__mutmut_36, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_37': xǁExtractAudioUseCaseǁexecute__mutmut_37, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_38': xǁExtractAudioUseCaseǁexecute__mutmut_38, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_39': xǁExtractAudioUseCaseǁexecute__mutmut_39, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_40': xǁExtractAudioUseCaseǁexecute__mutmut_40, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_41': xǁExtractAudioUseCaseǁexecute__mutmut_41, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_42': xǁExtractAudioUseCaseǁexecute__mutmut_42, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_43': xǁExtractAudioUseCaseǁexecute__mutmut_43, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_44': xǁExtractAudioUseCaseǁexecute__mutmut_44, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_45': xǁExtractAudioUseCaseǁexecute__mutmut_45, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_46': xǁExtractAudioUseCaseǁexecute__mutmut_46, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_47': xǁExtractAudioUseCaseǁexecute__mutmut_47, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_48': xǁExtractAudioUseCaseǁexecute__mutmut_48, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_49': xǁExtractAudioUseCaseǁexecute__mutmut_49, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_50': xǁExtractAudioUseCaseǁexecute__mutmut_50, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_51': xǁExtractAudioUseCaseǁexecute__mutmut_51, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_52': xǁExtractAudioUseCaseǁexecute__mutmut_52, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_53': xǁExtractAudioUseCaseǁexecute__mutmut_53, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_54': xǁExtractAudioUseCaseǁexecute__mutmut_54, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_55': xǁExtractAudioUseCaseǁexecute__mutmut_55, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_56': xǁExtractAudioUseCaseǁexecute__mutmut_56, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_57': xǁExtractAudioUseCaseǁexecute__mutmut_57, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_58': xǁExtractAudioUseCaseǁexecute__mutmut_58, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_59': xǁExtractAudioUseCaseǁexecute__mutmut_59, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_60': xǁExtractAudioUseCaseǁexecute__mutmut_60, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_61': xǁExtractAudioUseCaseǁexecute__mutmut_61, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_62': xǁExtractAudioUseCaseǁexecute__mutmut_62, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_63': xǁExtractAudioUseCaseǁexecute__mutmut_63, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_64': xǁExtractAudioUseCaseǁexecute__mutmut_64, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_65': xǁExtractAudioUseCaseǁexecute__mutmut_65, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_66': xǁExtractAudioUseCaseǁexecute__mutmut_66, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_67': xǁExtractAudioUseCaseǁexecute__mutmut_67, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_68': xǁExtractAudioUseCaseǁexecute__mutmut_68, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_69': xǁExtractAudioUseCaseǁexecute__mutmut_69, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_70': xǁExtractAudioUseCaseǁexecute__mutmut_70, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_71': xǁExtractAudioUseCaseǁexecute__mutmut_71, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_72': xǁExtractAudioUseCaseǁexecute__mutmut_72, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_73': xǁExtractAudioUseCaseǁexecute__mutmut_73, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_74': xǁExtractAudioUseCaseǁexecute__mutmut_74, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_75': xǁExtractAudioUseCaseǁexecute__mutmut_75, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_76': xǁExtractAudioUseCaseǁexecute__mutmut_76, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_77': xǁExtractAudioUseCaseǁexecute__mutmut_77, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_78': xǁExtractAudioUseCaseǁexecute__mutmut_78, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_79': xǁExtractAudioUseCaseǁexecute__mutmut_79, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_80': xǁExtractAudioUseCaseǁexecute__mutmut_80, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_81': xǁExtractAudioUseCaseǁexecute__mutmut_81, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_82': xǁExtractAudioUseCaseǁexecute__mutmut_82, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_83': xǁExtractAudioUseCaseǁexecute__mutmut_83, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_84': xǁExtractAudioUseCaseǁexecute__mutmut_84, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_85': xǁExtractAudioUseCaseǁexecute__mutmut_85, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_86': xǁExtractAudioUseCaseǁexecute__mutmut_86, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_87': xǁExtractAudioUseCaseǁexecute__mutmut_87, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_88': xǁExtractAudioUseCaseǁexecute__mutmut_88, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_89': xǁExtractAudioUseCaseǁexecute__mutmut_89, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_90': xǁExtractAudioUseCaseǁexecute__mutmut_90, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_91': xǁExtractAudioUseCaseǁexecute__mutmut_91, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_92': xǁExtractAudioUseCaseǁexecute__mutmut_92, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_93': xǁExtractAudioUseCaseǁexecute__mutmut_93, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_94': xǁExtractAudioUseCaseǁexecute__mutmut_94, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_95': xǁExtractAudioUseCaseǁexecute__mutmut_95, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_96': xǁExtractAudioUseCaseǁexecute__mutmut_96, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_97': xǁExtractAudioUseCaseǁexecute__mutmut_97, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_98': xǁExtractAudioUseCaseǁexecute__mutmut_98, 
        'xǁExtractAudioUseCaseǁexecute__mutmut_99': xǁExtractAudioUseCaseǁexecute__mutmut_99
    }
    xǁExtractAudioUseCaseǁexecute__mutmut_orig.__name__ = 'xǁExtractAudioUseCaseǁexecute'
