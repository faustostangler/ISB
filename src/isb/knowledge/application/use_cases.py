import logging
from datetime import datetime, timezone
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.shared_kernel.events import EventBus, KnowledgeSynthesized
from isb.transcription.domain.value_objects import TranscriptText
from isb.knowledge.domain.entities import RawNote, WikiArticle
from isb.knowledge.domain.value_objects import (
    NoteMetadata,
    NoteTitle,
    ArticleContent,
    ArticleTag,
    ArticleBacklink,
)
from isb.knowledge.application.ports import LLMPort, VaultPort, KnowledgeManifestPort

logger = logging.getLogger(__name__)

class SynthesizeWikiUseCase:
    """Orchestrates LLM synthesis of RawNote into the Obsidian Vault Wiki Layer.

    Loads existing vault knowledge, invokes a local LLM to generate structured summaries and
    takeaways, updates existing wiki notes or creates new ones, establishes backlinks, and emits
    synthesized knowledge events for audit tracking and sync triggers.
    """

    def __init__(
        self,
        llm_port: LLMPort,
        vault_port: VaultPort,
        manifest_port: KnowledgeManifestPort,
        event_bus: EventBus
    ) -> None:
        """Initialize use case dependencies via injection.

        Args:
            llm_port: Port adapter implementing LLMPort.
            vault_port: Port adapter implementing VaultPort.
            manifest_port: Port adapter implementing KnowledgeManifestPort.
            event_bus: System EventBus instance.
        """
        # Step 1: Bind injected dependencies to local attributes
        self.llm = llm_port
        self.vault = vault_port
        self.manifest = manifest_port
        self.event_bus = event_bus

    def execute(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event.

        Args:
            raw_note: RawNote entity containing verbatim text and source details.

        Returns:
            list[WikiArticle]: List of created/updated WikiArticle entities.
        """
        cid = raw_note.content_id
        # Step 1: Log use case entry point
        logger.info("Synthesizing wiki articles for ContentId %s ('%s')", cid, raw_note.title)
        
        # Step 2: Transition progress status to SYNTHESIZING
        self.manifest.mark_status(cid, ProcessingStatus.SYNTHESIZING)

        try:
            # Step 3: Load existing knowledge graphs
            existing_articles = self.vault.list_wiki_articles()

            # Step 4: Invoke local LLM port using Pydantic structured output validation
            synthesized = self.llm.synthesize_wiki(raw_note, existing_articles)

            # Step 5: Check for existing article in vault to update, or create a new one
            title_vo = NoteTitle(synthesized.title)
            existing_article = self.vault.find_wiki_article_by_title(title_vo)
            
            if existing_article:
                # Scenario A: Article exists. We merge content and append references.
                logger.info("Found existing WikiArticle '%s'. Merging content.", synthesized.title)
                article = existing_article
                article.content = ArticleContent(synthesized.content)
                
                # Merge tags to avoid duplicates
                new_tags = [ArticleTag(t) for t in synthesized.tags]
                existing_tag_strs = {t.value for t in article.tags}
                for nt in new_tags:
                    if nt.value not in existing_tag_strs:
                        article.tags.append(nt)
                
                # Add backlinks formatted as Obsidian wiki-links [[Topic]]
                new_backlinks = [ArticleBacklink(f"[[{topic}]]") for topic in synthesized.related_topics]
                existing_backlink_strs = {b.value for b in article.backlinks}
                for nb in new_backlinks:
                    if nb.value not in existing_backlink_strs:
                        article.backlinks.append(nb)
                
                # Append source note reference if not already tracked
                if cid not in article.source_notes:
                    article.source_notes.append(cid)
                # Update modification timestamp
                article.last_updated = datetime.now(timezone.utc)
            else:
                # Scenario B: Article is new. Instantiate a fresh WikiArticle entity.
                logger.info("Creating new WikiArticle '%s'.", synthesized.title)
                backlinks = [ArticleBacklink(f"[[{topic}]]") for topic in synthesized.related_topics]
                article = WikiArticle(
                    article_id=ContentId.generate(),
                    title=title_vo,
                    content=ArticleContent(synthesized.content),
                    tags=[ArticleTag(t) for t in synthesized.tags],
                    backlinks=backlinks,
                    source_notes=[cid],
                    last_updated=datetime.now(timezone.utc)
                )

            # Step 6: Save files to physical vault storage folders via VaultPort
            wiki_path = self.vault.save_wiki_article(article)
            raw_path = self.vault.save_raw_note(raw_note)

            # Step 7: Finalize processing status to COMPLETED in database manifest registry
            self.manifest.mark_status(cid, ProcessingStatus.COMPLETED)

            # Step 8: Construct and publish KnowledgeSynthesized domain event
            event = KnowledgeSynthesized(
                content_id=cid,
                raw_note_path=raw_path,
                wiki_articles_updated=[wiki_path]
            )
            if hasattr(self.manifest, "save_event"):
                self.manifest.save_event(event)
            self.event_bus.publish(event)
            logger.info("Completed synthesis for ContentId %s.", cid)
            
            # Step 9: Return list of modified articles
            return [article]

        except Exception as err:
            # Step 10: Fail-fast exception safety block
            logger.exception("Failed synthesis for ContentId %s.", cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise


class ProcessTranscriptUseCase:
    """Saves raw transcript and triggers the synthesis use case (Obsidian pipeline entrypoint).

    Accepts completed Whisper transcripts, instantiates the RawNote domain entity,
    saves it to the vault raw directories, and executes the synthesis workflow.
    """

    def __init__(
        self,
        vault_port: VaultPort,
        manifest_port: KnowledgeManifestPort,
        synthesize_use_case: SynthesizeWikiUseCase
    ) -> None:
        """Initialize dependencies via injection.

        Args:
            vault_port: Port adapter implementing VaultPort.
            manifest_port: Port adapter implementing KnowledgeManifestPort.
            synthesize_use_case: Injected SynthesizeWikiUseCase instance.
        """
        # Step 1: Bind injected dependencies to local attributes
        self.vault = vault_port
        self.manifest = manifest_port
        self.synthesize_use_case = synthesize_use_case

    def execute(
        self,
        content_id: ContentId,
        title: str,
        transcript_text: str,
        metadata: NoteMetadata
    ) -> RawNote:
        """Process completed transcript: construct RawNote, write to vault, and call SynthesizeWikiUseCase.

        Args:
            content_id: System ContentId identifier.
            title: Descriptive title for the raw transcript.
            transcript_text: Verbatim string transcript content.
            metadata: NoteMetadata frontmatter parameters.

        Returns:
            RawNote: The persisted RawNote entity.
        """
        # Step 1: Log transcript processing start event
        logger.info("Processing completed transcript for ContentId %s ('%s')", content_id, title)
        
        # Step 2: Instantiate the RawNote domain entity
        raw_note = RawNote(
            content_id=content_id,
            title=NoteTitle(title),
            transcript_text=TranscriptText(transcript_text),
            metadata=metadata
        )
        
        # Step 3: Write verbatim raw transcript to 00-Raw/ folder in Obsidian Vault
        self.vault.save_raw_note(raw_note)

        # Step 4: Execute second brain synthesis pipeline
        self.synthesize_use_case.execute(raw_note)
        
        # Step 5: Return raw note entity
        return raw_note
