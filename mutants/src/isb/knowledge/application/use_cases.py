import logging
from datetime import datetime, timezone
from isb.shared_kernel.types import ContentId, ProcessingStatus
from isb.shared_kernel.events import EventBus, KnowledgeSynthesized
from isb.knowledge.domain.entities import RawNote, WikiArticle
from isb.knowledge.domain.value_objects import NoteMetadata
from isb.knowledge.application.ports import LLMPort, VaultPort, KnowledgeManifestPort

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

class SynthesizeWikiUseCase:
    """Orchestrates LLM synthesis of RawNote into the Obsidian Vault Wiki Layer."""

    def __init__(
        self,
        llm_port: LLMPort,
        vault_port: VaultPort,
        manifest_port: KnowledgeManifestPort,
        event_bus: EventBus
    ) -> None:
        args = [llm_port, vault_port, manifest_port, event_bus]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁSynthesizeWikiUseCaseǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁSynthesizeWikiUseCaseǁ__init____mutmut_mutants'), args, kwargs, self)

    def xǁSynthesizeWikiUseCaseǁ__init____mutmut_orig(
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

    def xǁSynthesizeWikiUseCaseǁ__init____mutmut_1(
        self,
        llm_port: LLMPort,
        vault_port: VaultPort,
        manifest_port: KnowledgeManifestPort,
        event_bus: EventBus
    ) -> None:
        self.llm = None
        self.vault = vault_port
        self.manifest = manifest_port
        self.event_bus = event_bus

    def xǁSynthesizeWikiUseCaseǁ__init____mutmut_2(
        self,
        llm_port: LLMPort,
        vault_port: VaultPort,
        manifest_port: KnowledgeManifestPort,
        event_bus: EventBus
    ) -> None:
        self.llm = llm_port
        self.vault = None
        self.manifest = manifest_port
        self.event_bus = event_bus

    def xǁSynthesizeWikiUseCaseǁ__init____mutmut_3(
        self,
        llm_port: LLMPort,
        vault_port: VaultPort,
        manifest_port: KnowledgeManifestPort,
        event_bus: EventBus
    ) -> None:
        self.llm = llm_port
        self.vault = vault_port
        self.manifest = None
        self.event_bus = event_bus

    def xǁSynthesizeWikiUseCaseǁ__init____mutmut_4(
        self,
        llm_port: LLMPort,
        vault_port: VaultPort,
        manifest_port: KnowledgeManifestPort,
        event_bus: EventBus
    ) -> None:
        self.llm = llm_port
        self.vault = vault_port
        self.manifest = manifest_port
        self.event_bus = None
    
    xǁSynthesizeWikiUseCaseǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁSynthesizeWikiUseCaseǁ__init____mutmut_1': xǁSynthesizeWikiUseCaseǁ__init____mutmut_1, 
        'xǁSynthesizeWikiUseCaseǁ__init____mutmut_2': xǁSynthesizeWikiUseCaseǁ__init____mutmut_2, 
        'xǁSynthesizeWikiUseCaseǁ__init____mutmut_3': xǁSynthesizeWikiUseCaseǁ__init____mutmut_3, 
        'xǁSynthesizeWikiUseCaseǁ__init____mutmut_4': xǁSynthesizeWikiUseCaseǁ__init____mutmut_4
    }
    xǁSynthesizeWikiUseCaseǁ__init____mutmut_orig.__name__ = 'xǁSynthesizeWikiUseCaseǁ__init__'

    def execute(self, raw_note: RawNote) -> list[WikiArticle]:
        args = [raw_note]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁSynthesizeWikiUseCaseǁexecute__mutmut_orig'), object.__getattribute__(self, 'xǁSynthesizeWikiUseCaseǁexecute__mutmut_mutants'), args, kwargs, self)

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_orig(self, raw_note: RawNote) -> list[WikiArticle]:
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_1(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = None
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_2(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info(None, cid, raw_note.title)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_3(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info("Synthesizing wiki articles for ContentId %s ('%s')", None, raw_note.title)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_4(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info("Synthesizing wiki articles for ContentId %s ('%s')", cid, None)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_5(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info(cid, raw_note.title)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_6(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info("Synthesizing wiki articles for ContentId %s ('%s')", raw_note.title)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_7(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info("Synthesizing wiki articles for ContentId %s ('%s')", cid, )
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_8(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info("XXSynthesizing wiki articles for ContentId %s ('%s')XX", cid, raw_note.title)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_9(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info("synthesizing wiki articles for contentid %s ('%s')", cid, raw_note.title)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_10(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info("SYNTHESIZING WIKI ARTICLES FOR CONTENTID %S ('%S')", cid, raw_note.title)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_11(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info("Synthesizing wiki articles for ContentId %s ('%s')", cid, raw_note.title)
        self.manifest.mark_status(None, ProcessingStatus.SYNTHESIZING)

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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_12(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info("Synthesizing wiki articles for ContentId %s ('%s')", cid, raw_note.title)
        self.manifest.mark_status(cid, None)

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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_13(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info("Synthesizing wiki articles for ContentId %s ('%s')", cid, raw_note.title)
        self.manifest.mark_status(ProcessingStatus.SYNTHESIZING)

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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_14(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info("Synthesizing wiki articles for ContentId %s ('%s')", cid, raw_note.title)
        self.manifest.mark_status(cid, )

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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_15(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info("Synthesizing wiki articles for ContentId %s ('%s')", cid, raw_note.title)
        self.manifest.mark_status(cid, ProcessingStatus.SYNTHESIZING)

        try:
            # 1. Load existing knowledge graphs
            existing_articles = None

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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_16(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info("Synthesizing wiki articles for ContentId %s ('%s')", cid, raw_note.title)
        self.manifest.mark_status(cid, ProcessingStatus.SYNTHESIZING)

        try:
            # 1. Load existing knowledge graphs
            existing_articles = self.vault.list_wiki_articles()

            # 2. Invoke local LLM port using Pydantic structured output validation
            synthesized = None

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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_17(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info("Synthesizing wiki articles for ContentId %s ('%s')", cid, raw_note.title)
        self.manifest.mark_status(cid, ProcessingStatus.SYNTHESIZING)

        try:
            # 1. Load existing knowledge graphs
            existing_articles = self.vault.list_wiki_articles()

            # 2. Invoke local LLM port using Pydantic structured output validation
            synthesized = self.llm.synthesize_wiki(None, existing_articles)

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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_18(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info("Synthesizing wiki articles for ContentId %s ('%s')", cid, raw_note.title)
        self.manifest.mark_status(cid, ProcessingStatus.SYNTHESIZING)

        try:
            # 1. Load existing knowledge graphs
            existing_articles = self.vault.list_wiki_articles()

            # 2. Invoke local LLM port using Pydantic structured output validation
            synthesized = self.llm.synthesize_wiki(raw_note, None)

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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_19(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info("Synthesizing wiki articles for ContentId %s ('%s')", cid, raw_note.title)
        self.manifest.mark_status(cid, ProcessingStatus.SYNTHESIZING)

        try:
            # 1. Load existing knowledge graphs
            existing_articles = self.vault.list_wiki_articles()

            # 2. Invoke local LLM port using Pydantic structured output validation
            synthesized = self.llm.synthesize_wiki(existing_articles)

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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_20(self, raw_note: RawNote) -> list[WikiArticle]:
        """Perform synthesis, updates or creates wiki articles, and publishes completed event."""
        cid = raw_note.content_id
        logger.info("Synthesizing wiki articles for ContentId %s ('%s')", cid, raw_note.title)
        self.manifest.mark_status(cid, ProcessingStatus.SYNTHESIZING)

        try:
            # 1. Load existing knowledge graphs
            existing_articles = self.vault.list_wiki_articles()

            # 2. Invoke local LLM port using Pydantic structured output validation
            synthesized = self.llm.synthesize_wiki(raw_note, )

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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_21(self, raw_note: RawNote) -> list[WikiArticle]:
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
            existing_article = None
            
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_22(self, raw_note: RawNote) -> list[WikiArticle]:
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
            existing_article = self.vault.find_wiki_article_by_title(None)
            
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_23(self, raw_note: RawNote) -> list[WikiArticle]:
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
                logger.info(None, synthesized.title)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_24(self, raw_note: RawNote) -> list[WikiArticle]:
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
                logger.info("Found existing WikiArticle '%s'. Merging content.", None)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_25(self, raw_note: RawNote) -> list[WikiArticle]:
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
                logger.info(synthesized.title)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_26(self, raw_note: RawNote) -> list[WikiArticle]:
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
                logger.info("Found existing WikiArticle '%s'. Merging content.", )
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_27(self, raw_note: RawNote) -> list[WikiArticle]:
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
                logger.info("XXFound existing WikiArticle '%s'. Merging content.XX", synthesized.title)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_28(self, raw_note: RawNote) -> list[WikiArticle]:
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
                logger.info("found existing wikiarticle '%s'. merging content.", synthesized.title)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_29(self, raw_note: RawNote) -> list[WikiArticle]:
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
                logger.info("FOUND EXISTING WIKIARTICLE '%S'. MERGING CONTENT.", synthesized.title)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_30(self, raw_note: RawNote) -> list[WikiArticle]:
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
                article = None
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_31(self, raw_note: RawNote) -> list[WikiArticle]:
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
                article.content = None
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_32(self, raw_note: RawNote) -> list[WikiArticle]:
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
                article.tags = None
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_33(self, raw_note: RawNote) -> list[WikiArticle]:
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
                article.tags = list(None)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_34(self, raw_note: RawNote) -> list[WikiArticle]:
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
                article.tags = list(set(None))
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_35(self, raw_note: RawNote) -> list[WikiArticle]:
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
                article.tags = list(set(article.tags - synthesized.tags))
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_36(self, raw_note: RawNote) -> list[WikiArticle]:
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
                new_backlinks = None
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_37(self, raw_note: RawNote) -> list[WikiArticle]:
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
                article.backlinks = None
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_38(self, raw_note: RawNote) -> list[WikiArticle]:
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
                article.backlinks = list(None)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_39(self, raw_note: RawNote) -> list[WikiArticle]:
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
                article.backlinks = list(set(None))
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_40(self, raw_note: RawNote) -> list[WikiArticle]:
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
                article.backlinks = list(set(article.backlinks - new_backlinks))
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_41(self, raw_note: RawNote) -> list[WikiArticle]:
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
                if cid in article.source_notes:
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_42(self, raw_note: RawNote) -> list[WikiArticle]:
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
                    article.source_notes.append(None)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_43(self, raw_note: RawNote) -> list[WikiArticle]:
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
                article.last_updated = None
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_44(self, raw_note: RawNote) -> list[WikiArticle]:
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
                article.last_updated = datetime.now(None)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_45(self, raw_note: RawNote) -> list[WikiArticle]:
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
                logger.info(None, synthesized.title)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_46(self, raw_note: RawNote) -> list[WikiArticle]:
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
                logger.info("Creating new WikiArticle '%s'.", None)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_47(self, raw_note: RawNote) -> list[WikiArticle]:
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
                logger.info(synthesized.title)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_48(self, raw_note: RawNote) -> list[WikiArticle]:
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
                logger.info("Creating new WikiArticle '%s'.", )
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_49(self, raw_note: RawNote) -> list[WikiArticle]:
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
                logger.info("XXCreating new WikiArticle '%s'.XX", synthesized.title)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_50(self, raw_note: RawNote) -> list[WikiArticle]:
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
                logger.info("creating new wikiarticle '%s'.", synthesized.title)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_51(self, raw_note: RawNote) -> list[WikiArticle]:
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
                logger.info("CREATING NEW WIKIARTICLE '%S'.", synthesized.title)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_52(self, raw_note: RawNote) -> list[WikiArticle]:
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
                backlinks = None
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_53(self, raw_note: RawNote) -> list[WikiArticle]:
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
                article = None

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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_54(self, raw_note: RawNote) -> list[WikiArticle]:
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
                    article_id=None,
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_55(self, raw_note: RawNote) -> list[WikiArticle]:
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
                    title=None,
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_56(self, raw_note: RawNote) -> list[WikiArticle]:
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
                    content=None,
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_57(self, raw_note: RawNote) -> list[WikiArticle]:
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
                    tags=None,
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_58(self, raw_note: RawNote) -> list[WikiArticle]:
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
                    backlinks=None,
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_59(self, raw_note: RawNote) -> list[WikiArticle]:
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
                    source_notes=None,
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_60(self, raw_note: RawNote) -> list[WikiArticle]:
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
                    last_updated=None
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_61(self, raw_note: RawNote) -> list[WikiArticle]:
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_62(self, raw_note: RawNote) -> list[WikiArticle]:
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_63(self, raw_note: RawNote) -> list[WikiArticle]:
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_64(self, raw_note: RawNote) -> list[WikiArticle]:
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_65(self, raw_note: RawNote) -> list[WikiArticle]:
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_66(self, raw_note: RawNote) -> list[WikiArticle]:
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_67(self, raw_note: RawNote) -> list[WikiArticle]:
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_68(self, raw_note: RawNote) -> list[WikiArticle]:
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
                    last_updated=datetime.now(None)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_69(self, raw_note: RawNote) -> list[WikiArticle]:
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
            wiki_path = None
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_70(self, raw_note: RawNote) -> list[WikiArticle]:
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
            wiki_path = self.vault.save_wiki_article(None)
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_71(self, raw_note: RawNote) -> list[WikiArticle]:
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
            raw_path = None # Ensure raw path is resolved

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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_72(self, raw_note: RawNote) -> list[WikiArticle]:
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
            raw_path = self.vault.save_raw_note(None) # Ensure raw path is resolved

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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_73(self, raw_note: RawNote) -> list[WikiArticle]:
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
            self.manifest.mark_status(None, ProcessingStatus.COMPLETED)

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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_74(self, raw_note: RawNote) -> list[WikiArticle]:
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
            self.manifest.mark_status(cid, None)

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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_75(self, raw_note: RawNote) -> list[WikiArticle]:
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
            self.manifest.mark_status(ProcessingStatus.COMPLETED)

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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_76(self, raw_note: RawNote) -> list[WikiArticle]:
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
            self.manifest.mark_status(cid, )

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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_77(self, raw_note: RawNote) -> list[WikiArticle]:
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
            event = None
            self.event_bus.publish(event)
            logger.info("Completed synthesis for ContentId %s.", cid)
            
            return [article]

        except Exception as err:
            logger.exception("Failed synthesis for ContentId %s.", cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_78(self, raw_note: RawNote) -> list[WikiArticle]:
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
                content_id=None,
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_79(self, raw_note: RawNote) -> list[WikiArticle]:
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
                raw_note_path=None,
                wiki_articles_updated=[wiki_path]
            )
            self.event_bus.publish(event)
            logger.info("Completed synthesis for ContentId %s.", cid)
            
            return [article]

        except Exception as err:
            logger.exception("Failed synthesis for ContentId %s.", cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_80(self, raw_note: RawNote) -> list[WikiArticle]:
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
                wiki_articles_updated=None
            )
            self.event_bus.publish(event)
            logger.info("Completed synthesis for ContentId %s.", cid)
            
            return [article]

        except Exception as err:
            logger.exception("Failed synthesis for ContentId %s.", cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_81(self, raw_note: RawNote) -> list[WikiArticle]:
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

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_82(self, raw_note: RawNote) -> list[WikiArticle]:
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
                wiki_articles_updated=[wiki_path]
            )
            self.event_bus.publish(event)
            logger.info("Completed synthesis for ContentId %s.", cid)
            
            return [article]

        except Exception as err:
            logger.exception("Failed synthesis for ContentId %s.", cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_83(self, raw_note: RawNote) -> list[WikiArticle]:
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
                )
            self.event_bus.publish(event)
            logger.info("Completed synthesis for ContentId %s.", cid)
            
            return [article]

        except Exception as err:
            logger.exception("Failed synthesis for ContentId %s.", cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_84(self, raw_note: RawNote) -> list[WikiArticle]:
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
            self.event_bus.publish(None)
            logger.info("Completed synthesis for ContentId %s.", cid)
            
            return [article]

        except Exception as err:
            logger.exception("Failed synthesis for ContentId %s.", cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_85(self, raw_note: RawNote) -> list[WikiArticle]:
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
            logger.info(None, cid)
            
            return [article]

        except Exception as err:
            logger.exception("Failed synthesis for ContentId %s.", cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_86(self, raw_note: RawNote) -> list[WikiArticle]:
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
            logger.info("Completed synthesis for ContentId %s.", None)
            
            return [article]

        except Exception as err:
            logger.exception("Failed synthesis for ContentId %s.", cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_87(self, raw_note: RawNote) -> list[WikiArticle]:
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
            logger.info(cid)
            
            return [article]

        except Exception as err:
            logger.exception("Failed synthesis for ContentId %s.", cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_88(self, raw_note: RawNote) -> list[WikiArticle]:
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
            logger.info("Completed synthesis for ContentId %s.", )
            
            return [article]

        except Exception as err:
            logger.exception("Failed synthesis for ContentId %s.", cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_89(self, raw_note: RawNote) -> list[WikiArticle]:
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
            logger.info("XXCompleted synthesis for ContentId %s.XX", cid)
            
            return [article]

        except Exception as err:
            logger.exception("Failed synthesis for ContentId %s.", cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_90(self, raw_note: RawNote) -> list[WikiArticle]:
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
            logger.info("completed synthesis for contentid %s.", cid)
            
            return [article]

        except Exception as err:
            logger.exception("Failed synthesis for ContentId %s.", cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_91(self, raw_note: RawNote) -> list[WikiArticle]:
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
            logger.info("COMPLETED SYNTHESIS FOR CONTENTID %S.", cid)
            
            return [article]

        except Exception as err:
            logger.exception("Failed synthesis for ContentId %s.", cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_92(self, raw_note: RawNote) -> list[WikiArticle]:
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
            logger.exception(None, cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_93(self, raw_note: RawNote) -> list[WikiArticle]:
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
            logger.exception("Failed synthesis for ContentId %s.", None)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_94(self, raw_note: RawNote) -> list[WikiArticle]:
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
            logger.exception(cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_95(self, raw_note: RawNote) -> list[WikiArticle]:
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
            logger.exception("Failed synthesis for ContentId %s.", )
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_96(self, raw_note: RawNote) -> list[WikiArticle]:
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
            logger.exception("XXFailed synthesis for ContentId %s.XX", cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_97(self, raw_note: RawNote) -> list[WikiArticle]:
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
            logger.exception("failed synthesis for contentid %s.", cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_98(self, raw_note: RawNote) -> list[WikiArticle]:
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
            logger.exception("FAILED SYNTHESIS FOR CONTENTID %S.", cid)
            self.manifest.mark_status(cid, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_99(self, raw_note: RawNote) -> list[WikiArticle]:
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
            self.manifest.mark_status(None, ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_100(self, raw_note: RawNote) -> list[WikiArticle]:
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
            self.manifest.mark_status(cid, None)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_101(self, raw_note: RawNote) -> list[WikiArticle]:
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
            self.manifest.mark_status(ProcessingStatus.FAILED)
            raise

    def xǁSynthesizeWikiUseCaseǁexecute__mutmut_102(self, raw_note: RawNote) -> list[WikiArticle]:
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
            self.manifest.mark_status(cid, )
            raise
    
    xǁSynthesizeWikiUseCaseǁexecute__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁSynthesizeWikiUseCaseǁexecute__mutmut_1': xǁSynthesizeWikiUseCaseǁexecute__mutmut_1, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_2': xǁSynthesizeWikiUseCaseǁexecute__mutmut_2, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_3': xǁSynthesizeWikiUseCaseǁexecute__mutmut_3, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_4': xǁSynthesizeWikiUseCaseǁexecute__mutmut_4, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_5': xǁSynthesizeWikiUseCaseǁexecute__mutmut_5, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_6': xǁSynthesizeWikiUseCaseǁexecute__mutmut_6, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_7': xǁSynthesizeWikiUseCaseǁexecute__mutmut_7, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_8': xǁSynthesizeWikiUseCaseǁexecute__mutmut_8, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_9': xǁSynthesizeWikiUseCaseǁexecute__mutmut_9, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_10': xǁSynthesizeWikiUseCaseǁexecute__mutmut_10, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_11': xǁSynthesizeWikiUseCaseǁexecute__mutmut_11, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_12': xǁSynthesizeWikiUseCaseǁexecute__mutmut_12, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_13': xǁSynthesizeWikiUseCaseǁexecute__mutmut_13, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_14': xǁSynthesizeWikiUseCaseǁexecute__mutmut_14, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_15': xǁSynthesizeWikiUseCaseǁexecute__mutmut_15, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_16': xǁSynthesizeWikiUseCaseǁexecute__mutmut_16, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_17': xǁSynthesizeWikiUseCaseǁexecute__mutmut_17, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_18': xǁSynthesizeWikiUseCaseǁexecute__mutmut_18, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_19': xǁSynthesizeWikiUseCaseǁexecute__mutmut_19, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_20': xǁSynthesizeWikiUseCaseǁexecute__mutmut_20, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_21': xǁSynthesizeWikiUseCaseǁexecute__mutmut_21, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_22': xǁSynthesizeWikiUseCaseǁexecute__mutmut_22, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_23': xǁSynthesizeWikiUseCaseǁexecute__mutmut_23, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_24': xǁSynthesizeWikiUseCaseǁexecute__mutmut_24, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_25': xǁSynthesizeWikiUseCaseǁexecute__mutmut_25, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_26': xǁSynthesizeWikiUseCaseǁexecute__mutmut_26, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_27': xǁSynthesizeWikiUseCaseǁexecute__mutmut_27, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_28': xǁSynthesizeWikiUseCaseǁexecute__mutmut_28, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_29': xǁSynthesizeWikiUseCaseǁexecute__mutmut_29, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_30': xǁSynthesizeWikiUseCaseǁexecute__mutmut_30, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_31': xǁSynthesizeWikiUseCaseǁexecute__mutmut_31, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_32': xǁSynthesizeWikiUseCaseǁexecute__mutmut_32, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_33': xǁSynthesizeWikiUseCaseǁexecute__mutmut_33, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_34': xǁSynthesizeWikiUseCaseǁexecute__mutmut_34, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_35': xǁSynthesizeWikiUseCaseǁexecute__mutmut_35, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_36': xǁSynthesizeWikiUseCaseǁexecute__mutmut_36, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_37': xǁSynthesizeWikiUseCaseǁexecute__mutmut_37, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_38': xǁSynthesizeWikiUseCaseǁexecute__mutmut_38, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_39': xǁSynthesizeWikiUseCaseǁexecute__mutmut_39, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_40': xǁSynthesizeWikiUseCaseǁexecute__mutmut_40, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_41': xǁSynthesizeWikiUseCaseǁexecute__mutmut_41, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_42': xǁSynthesizeWikiUseCaseǁexecute__mutmut_42, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_43': xǁSynthesizeWikiUseCaseǁexecute__mutmut_43, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_44': xǁSynthesizeWikiUseCaseǁexecute__mutmut_44, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_45': xǁSynthesizeWikiUseCaseǁexecute__mutmut_45, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_46': xǁSynthesizeWikiUseCaseǁexecute__mutmut_46, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_47': xǁSynthesizeWikiUseCaseǁexecute__mutmut_47, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_48': xǁSynthesizeWikiUseCaseǁexecute__mutmut_48, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_49': xǁSynthesizeWikiUseCaseǁexecute__mutmut_49, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_50': xǁSynthesizeWikiUseCaseǁexecute__mutmut_50, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_51': xǁSynthesizeWikiUseCaseǁexecute__mutmut_51, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_52': xǁSynthesizeWikiUseCaseǁexecute__mutmut_52, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_53': xǁSynthesizeWikiUseCaseǁexecute__mutmut_53, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_54': xǁSynthesizeWikiUseCaseǁexecute__mutmut_54, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_55': xǁSynthesizeWikiUseCaseǁexecute__mutmut_55, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_56': xǁSynthesizeWikiUseCaseǁexecute__mutmut_56, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_57': xǁSynthesizeWikiUseCaseǁexecute__mutmut_57, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_58': xǁSynthesizeWikiUseCaseǁexecute__mutmut_58, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_59': xǁSynthesizeWikiUseCaseǁexecute__mutmut_59, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_60': xǁSynthesizeWikiUseCaseǁexecute__mutmut_60, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_61': xǁSynthesizeWikiUseCaseǁexecute__mutmut_61, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_62': xǁSynthesizeWikiUseCaseǁexecute__mutmut_62, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_63': xǁSynthesizeWikiUseCaseǁexecute__mutmut_63, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_64': xǁSynthesizeWikiUseCaseǁexecute__mutmut_64, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_65': xǁSynthesizeWikiUseCaseǁexecute__mutmut_65, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_66': xǁSynthesizeWikiUseCaseǁexecute__mutmut_66, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_67': xǁSynthesizeWikiUseCaseǁexecute__mutmut_67, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_68': xǁSynthesizeWikiUseCaseǁexecute__mutmut_68, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_69': xǁSynthesizeWikiUseCaseǁexecute__mutmut_69, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_70': xǁSynthesizeWikiUseCaseǁexecute__mutmut_70, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_71': xǁSynthesizeWikiUseCaseǁexecute__mutmut_71, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_72': xǁSynthesizeWikiUseCaseǁexecute__mutmut_72, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_73': xǁSynthesizeWikiUseCaseǁexecute__mutmut_73, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_74': xǁSynthesizeWikiUseCaseǁexecute__mutmut_74, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_75': xǁSynthesizeWikiUseCaseǁexecute__mutmut_75, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_76': xǁSynthesizeWikiUseCaseǁexecute__mutmut_76, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_77': xǁSynthesizeWikiUseCaseǁexecute__mutmut_77, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_78': xǁSynthesizeWikiUseCaseǁexecute__mutmut_78, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_79': xǁSynthesizeWikiUseCaseǁexecute__mutmut_79, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_80': xǁSynthesizeWikiUseCaseǁexecute__mutmut_80, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_81': xǁSynthesizeWikiUseCaseǁexecute__mutmut_81, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_82': xǁSynthesizeWikiUseCaseǁexecute__mutmut_82, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_83': xǁSynthesizeWikiUseCaseǁexecute__mutmut_83, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_84': xǁSynthesizeWikiUseCaseǁexecute__mutmut_84, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_85': xǁSynthesizeWikiUseCaseǁexecute__mutmut_85, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_86': xǁSynthesizeWikiUseCaseǁexecute__mutmut_86, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_87': xǁSynthesizeWikiUseCaseǁexecute__mutmut_87, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_88': xǁSynthesizeWikiUseCaseǁexecute__mutmut_88, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_89': xǁSynthesizeWikiUseCaseǁexecute__mutmut_89, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_90': xǁSynthesizeWikiUseCaseǁexecute__mutmut_90, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_91': xǁSynthesizeWikiUseCaseǁexecute__mutmut_91, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_92': xǁSynthesizeWikiUseCaseǁexecute__mutmut_92, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_93': xǁSynthesizeWikiUseCaseǁexecute__mutmut_93, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_94': xǁSynthesizeWikiUseCaseǁexecute__mutmut_94, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_95': xǁSynthesizeWikiUseCaseǁexecute__mutmut_95, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_96': xǁSynthesizeWikiUseCaseǁexecute__mutmut_96, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_97': xǁSynthesizeWikiUseCaseǁexecute__mutmut_97, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_98': xǁSynthesizeWikiUseCaseǁexecute__mutmut_98, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_99': xǁSynthesizeWikiUseCaseǁexecute__mutmut_99, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_100': xǁSynthesizeWikiUseCaseǁexecute__mutmut_100, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_101': xǁSynthesizeWikiUseCaseǁexecute__mutmut_101, 
        'xǁSynthesizeWikiUseCaseǁexecute__mutmut_102': xǁSynthesizeWikiUseCaseǁexecute__mutmut_102
    }
    xǁSynthesizeWikiUseCaseǁexecute__mutmut_orig.__name__ = 'xǁSynthesizeWikiUseCaseǁexecute'


class ProcessTranscriptUseCase:
    """Saves raw transcript and triggers the synthesis use case (Obsidian pipeline entrypoint)."""

    def __init__(
        self,
        vault_port: VaultPort,
        manifest_port: KnowledgeManifestPort,
        synthesize_use_case: SynthesizeWikiUseCase
    ) -> None:
        args = [vault_port, manifest_port, synthesize_use_case]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁProcessTranscriptUseCaseǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁProcessTranscriptUseCaseǁ__init____mutmut_mutants'), args, kwargs, self)

    def xǁProcessTranscriptUseCaseǁ__init____mutmut_orig(
        self,
        vault_port: VaultPort,
        manifest_port: KnowledgeManifestPort,
        synthesize_use_case: SynthesizeWikiUseCase
    ) -> None:
        self.vault = vault_port
        self.manifest = manifest_port
        self.synthesize_use_case = synthesize_use_case

    def xǁProcessTranscriptUseCaseǁ__init____mutmut_1(
        self,
        vault_port: VaultPort,
        manifest_port: KnowledgeManifestPort,
        synthesize_use_case: SynthesizeWikiUseCase
    ) -> None:
        self.vault = None
        self.manifest = manifest_port
        self.synthesize_use_case = synthesize_use_case

    def xǁProcessTranscriptUseCaseǁ__init____mutmut_2(
        self,
        vault_port: VaultPort,
        manifest_port: KnowledgeManifestPort,
        synthesize_use_case: SynthesizeWikiUseCase
    ) -> None:
        self.vault = vault_port
        self.manifest = None
        self.synthesize_use_case = synthesize_use_case

    def xǁProcessTranscriptUseCaseǁ__init____mutmut_3(
        self,
        vault_port: VaultPort,
        manifest_port: KnowledgeManifestPort,
        synthesize_use_case: SynthesizeWikiUseCase
    ) -> None:
        self.vault = vault_port
        self.manifest = manifest_port
        self.synthesize_use_case = None
    
    xǁProcessTranscriptUseCaseǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁProcessTranscriptUseCaseǁ__init____mutmut_1': xǁProcessTranscriptUseCaseǁ__init____mutmut_1, 
        'xǁProcessTranscriptUseCaseǁ__init____mutmut_2': xǁProcessTranscriptUseCaseǁ__init____mutmut_2, 
        'xǁProcessTranscriptUseCaseǁ__init____mutmut_3': xǁProcessTranscriptUseCaseǁ__init____mutmut_3
    }
    xǁProcessTranscriptUseCaseǁ__init____mutmut_orig.__name__ = 'xǁProcessTranscriptUseCaseǁ__init__'

    def execute(
        self,
        content_id: ContentId,
        title: str,
        transcript_text: str,
        metadata: NoteMetadata
    ) -> RawNote:
        args = [content_id, title, transcript_text, metadata]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁProcessTranscriptUseCaseǁexecute__mutmut_orig'), object.__getattribute__(self, 'xǁProcessTranscriptUseCaseǁexecute__mutmut_mutants'), args, kwargs, self)

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_orig(
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

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_1(
        self,
        content_id: ContentId,
        title: str,
        transcript_text: str,
        metadata: NoteMetadata
    ) -> RawNote:
        """Process completed transcript: construct RawNote, write to vault, and call SynthesizeWikiUseCase."""
        logger.info(None, content_id, title)
        
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

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_2(
        self,
        content_id: ContentId,
        title: str,
        transcript_text: str,
        metadata: NoteMetadata
    ) -> RawNote:
        """Process completed transcript: construct RawNote, write to vault, and call SynthesizeWikiUseCase."""
        logger.info("Processing completed transcript for ContentId %s ('%s')", None, title)
        
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

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_3(
        self,
        content_id: ContentId,
        title: str,
        transcript_text: str,
        metadata: NoteMetadata
    ) -> RawNote:
        """Process completed transcript: construct RawNote, write to vault, and call SynthesizeWikiUseCase."""
        logger.info("Processing completed transcript for ContentId %s ('%s')", content_id, None)
        
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

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_4(
        self,
        content_id: ContentId,
        title: str,
        transcript_text: str,
        metadata: NoteMetadata
    ) -> RawNote:
        """Process completed transcript: construct RawNote, write to vault, and call SynthesizeWikiUseCase."""
        logger.info(content_id, title)
        
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

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_5(
        self,
        content_id: ContentId,
        title: str,
        transcript_text: str,
        metadata: NoteMetadata
    ) -> RawNote:
        """Process completed transcript: construct RawNote, write to vault, and call SynthesizeWikiUseCase."""
        logger.info("Processing completed transcript for ContentId %s ('%s')", title)
        
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

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_6(
        self,
        content_id: ContentId,
        title: str,
        transcript_text: str,
        metadata: NoteMetadata
    ) -> RawNote:
        """Process completed transcript: construct RawNote, write to vault, and call SynthesizeWikiUseCase."""
        logger.info("Processing completed transcript for ContentId %s ('%s')", content_id, )
        
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

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_7(
        self,
        content_id: ContentId,
        title: str,
        transcript_text: str,
        metadata: NoteMetadata
    ) -> RawNote:
        """Process completed transcript: construct RawNote, write to vault, and call SynthesizeWikiUseCase."""
        logger.info("XXProcessing completed transcript for ContentId %s ('%s')XX", content_id, title)
        
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

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_8(
        self,
        content_id: ContentId,
        title: str,
        transcript_text: str,
        metadata: NoteMetadata
    ) -> RawNote:
        """Process completed transcript: construct RawNote, write to vault, and call SynthesizeWikiUseCase."""
        logger.info("processing completed transcript for contentid %s ('%s')", content_id, title)
        
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

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_9(
        self,
        content_id: ContentId,
        title: str,
        transcript_text: str,
        metadata: NoteMetadata
    ) -> RawNote:
        """Process completed transcript: construct RawNote, write to vault, and call SynthesizeWikiUseCase."""
        logger.info("PROCESSING COMPLETED TRANSCRIPT FOR CONTENTID %S ('%S')", content_id, title)
        
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

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_10(
        self,
        content_id: ContentId,
        title: str,
        transcript_text: str,
        metadata: NoteMetadata
    ) -> RawNote:
        """Process completed transcript: construct RawNote, write to vault, and call SynthesizeWikiUseCase."""
        logger.info("Processing completed transcript for ContentId %s ('%s')", content_id, title)
        
        raw_note = None
        
        # Save verbatim note to 00-Raw/ folder
        self.vault.save_raw_note(raw_note)

        # Trigger second brain compilation
        self.synthesize_use_case.execute(raw_note)
        
        return raw_note

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_11(
        self,
        content_id: ContentId,
        title: str,
        transcript_text: str,
        metadata: NoteMetadata
    ) -> RawNote:
        """Process completed transcript: construct RawNote, write to vault, and call SynthesizeWikiUseCase."""
        logger.info("Processing completed transcript for ContentId %s ('%s')", content_id, title)
        
        raw_note = RawNote(
            content_id=None,
            title=title,
            transcript_text=transcript_text,
            metadata=metadata
        )
        
        # Save verbatim note to 00-Raw/ folder
        self.vault.save_raw_note(raw_note)

        # Trigger second brain compilation
        self.synthesize_use_case.execute(raw_note)
        
        return raw_note

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_12(
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
            title=None,
            transcript_text=transcript_text,
            metadata=metadata
        )
        
        # Save verbatim note to 00-Raw/ folder
        self.vault.save_raw_note(raw_note)

        # Trigger second brain compilation
        self.synthesize_use_case.execute(raw_note)
        
        return raw_note

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_13(
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
            transcript_text=None,
            metadata=metadata
        )
        
        # Save verbatim note to 00-Raw/ folder
        self.vault.save_raw_note(raw_note)

        # Trigger second brain compilation
        self.synthesize_use_case.execute(raw_note)
        
        return raw_note

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_14(
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
            metadata=None
        )
        
        # Save verbatim note to 00-Raw/ folder
        self.vault.save_raw_note(raw_note)

        # Trigger second brain compilation
        self.synthesize_use_case.execute(raw_note)
        
        return raw_note

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_15(
        self,
        content_id: ContentId,
        title: str,
        transcript_text: str,
        metadata: NoteMetadata
    ) -> RawNote:
        """Process completed transcript: construct RawNote, write to vault, and call SynthesizeWikiUseCase."""
        logger.info("Processing completed transcript for ContentId %s ('%s')", content_id, title)
        
        raw_note = RawNote(
            title=title,
            transcript_text=transcript_text,
            metadata=metadata
        )
        
        # Save verbatim note to 00-Raw/ folder
        self.vault.save_raw_note(raw_note)

        # Trigger second brain compilation
        self.synthesize_use_case.execute(raw_note)
        
        return raw_note

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_16(
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
            transcript_text=transcript_text,
            metadata=metadata
        )
        
        # Save verbatim note to 00-Raw/ folder
        self.vault.save_raw_note(raw_note)

        # Trigger second brain compilation
        self.synthesize_use_case.execute(raw_note)
        
        return raw_note

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_17(
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
            metadata=metadata
        )
        
        # Save verbatim note to 00-Raw/ folder
        self.vault.save_raw_note(raw_note)

        # Trigger second brain compilation
        self.synthesize_use_case.execute(raw_note)
        
        return raw_note

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_18(
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
            )
        
        # Save verbatim note to 00-Raw/ folder
        self.vault.save_raw_note(raw_note)

        # Trigger second brain compilation
        self.synthesize_use_case.execute(raw_note)
        
        return raw_note

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_19(
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
        self.vault.save_raw_note(None)

        # Trigger second brain compilation
        self.synthesize_use_case.execute(raw_note)
        
        return raw_note

    def xǁProcessTranscriptUseCaseǁexecute__mutmut_20(
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
        self.synthesize_use_case.execute(None)
        
        return raw_note
    
    xǁProcessTranscriptUseCaseǁexecute__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁProcessTranscriptUseCaseǁexecute__mutmut_1': xǁProcessTranscriptUseCaseǁexecute__mutmut_1, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_2': xǁProcessTranscriptUseCaseǁexecute__mutmut_2, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_3': xǁProcessTranscriptUseCaseǁexecute__mutmut_3, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_4': xǁProcessTranscriptUseCaseǁexecute__mutmut_4, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_5': xǁProcessTranscriptUseCaseǁexecute__mutmut_5, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_6': xǁProcessTranscriptUseCaseǁexecute__mutmut_6, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_7': xǁProcessTranscriptUseCaseǁexecute__mutmut_7, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_8': xǁProcessTranscriptUseCaseǁexecute__mutmut_8, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_9': xǁProcessTranscriptUseCaseǁexecute__mutmut_9, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_10': xǁProcessTranscriptUseCaseǁexecute__mutmut_10, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_11': xǁProcessTranscriptUseCaseǁexecute__mutmut_11, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_12': xǁProcessTranscriptUseCaseǁexecute__mutmut_12, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_13': xǁProcessTranscriptUseCaseǁexecute__mutmut_13, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_14': xǁProcessTranscriptUseCaseǁexecute__mutmut_14, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_15': xǁProcessTranscriptUseCaseǁexecute__mutmut_15, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_16': xǁProcessTranscriptUseCaseǁexecute__mutmut_16, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_17': xǁProcessTranscriptUseCaseǁexecute__mutmut_17, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_18': xǁProcessTranscriptUseCaseǁexecute__mutmut_18, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_19': xǁProcessTranscriptUseCaseǁexecute__mutmut_19, 
        'xǁProcessTranscriptUseCaseǁexecute__mutmut_20': xǁProcessTranscriptUseCaseǁexecute__mutmut_20
    }
    xǁProcessTranscriptUseCaseǁexecute__mutmut_orig.__name__ = 'xǁProcessTranscriptUseCaseǁexecute'
