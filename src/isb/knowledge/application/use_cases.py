import logging
from datetime import datetime, timezone
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.shared_kernel.events import EventBus, KnowledgeSynthesized
from isb.knowledge.domain.entities import RawNote, WikiArticle
from isb.knowledge.domain.value_objects import NoteMetadata
from isb.knowledge.application.ports import LLMPort, VaultPort, KnowledgeManifestPort

logger = logging.getLogger(__name__)

class SynthesizeWikiUseCase:
    """Orchestrates LLM synthesis of RawNote into the Obsidian Vault Wiki Layer."""

    def __init__(
        self,
        llm_port: LLMPort,
        vault_port: VaultPort,
        manifest_port: KnowledgeManifestPort,
        event_bus: EventBus
    ) -> None:
        self.llm = llm_port
        self.vault = vault_port
        self.manifest = manifest_port
        self.event_bus = event_bus

    def execute(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info("Synthesizing wiki articles for ContentId %s ('%s')", cid, raw_note.title)
        self.manifest.mark_status(cid, ProcessingStatus.SYNTHESIZING)

        try:
            # 1. Load existing knowledge graphs
            existing_articles = self.vault.list_wiki_articles()

            # 2. Invoke local LLM port using Pydantic structured output validation
            synthesized = self.llm.synthesize_wiki(raw_note, existing_articles)

            # 3. Check for existing article in vault to update, or create a new one
            existing_article = self.vault.find_wiki_article_by_title(synthesized.title)
            
            if existing_article:
                logger.info("Found existing WikiArticle '%s'. Merging content.", synthesized.title)
                article = existing_article
                article.content = synthesized.content
                article.tags = list(set(article.tags + synthesized.tags))
                # Add backlinks
                new_backlinks = [f"[[{topic}]]" for topic in synthesized.related_topics]
                article.backlinks = list(set(article.backlinks + new_backlinks))
                # Link source note
                if cid not in article.source_notes:
                    article.source_notes.append(cid)
                article.last_updated = datetime.now(timezone.utc)
            else:
                logger.info("Creating new WikiArticle '%s'.", synthesized.title)
                backlinks = [f"[[{topic}]]" for topic in synthesized.related_topics]
                article = WikiArticle(
                    article_id=ContentId.generate(),
                    title=synthesized.title,
                    content=synthesized.content,
                    tags=synthesized.tags,
                    backlinks=backlinks,
                    source_notes=[cid],
                    last_updated=datetime.now(timezone.utc)
                )

            # 4. Save to Obsidian Vault repository
            wiki_path = self.vault.save_wiki_article(article)
            raw_path = self.vault.save_raw_note(raw_note) # Ensure raw path is resolved

            # 5. Finalize processing status in SQLite manifest registry
            self.manifest.mark_status(cid, ProcessingStatus.COMPLETED)

            # 6. Publish domain event
            event = KnowledgeSynthesized(
                content_id=cid,
                raw_note_path=raw_path,
                wiki_articles_updated=[wiki_path]
            )
            self.event_bus.publish(event)
            logger.info("Completed synthesis for ContentId %s.", cid)
            
            return [article]

        except Exception as err:
            logger.exception("Failed synthesis for ContentId %s.", cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise


class ProcessTranscriptUseCase:
    """Saves raw transcript and triggers the synthesis use case (Obsidian pipeline entrypoint)."""

    def __init__(
        self,
        vault_port: VaultPort,
        manifest_port: KnowledgeManifestPort,
        synthesize_use_case: SynthesizeWikiUseCase
    ) -> None:
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
        """Process completed transcript: construct RawNote, write to vault, and call SynthesizeWikiUseCase."""
        logger.info("Processing completed transcript for ContentId %s ('%s')", content_id, title)
        
        raw_note = RawNote(
            content_id=content_id,
            title=title,
            transcript_text=transcript_text,
            metadata=metadata
        )
        
        # Save verbatim note to 00-Raw/ folder
        self.vault.save_raw_note(raw_note)

        # Trigger second brain compilation
        self.synthesize_use_case.execute(raw_note)
        
        return raw_note
