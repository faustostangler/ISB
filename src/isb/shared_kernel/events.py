import uuid
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Type, TypeVar
from dataclasses import dataclass, field
from isb.shared_kernel.types import ContentId

@dataclass(frozen=True, kw_only=True)
class DomainEvent:
    """Base record for all domain events emitted by the system contexts.

    All subclasses inherit these properties to preserve auditability and tracing.
    Domain events represent significant state transitions within a Bounded Context.
    """
    content_id: ContentId
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    occurred_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(frozen=True, kw_only=True)
class AudioExtracted(DomainEvent):
    """Emitted when the Ingestion context has extracted the audio for an episode.

    Signals to downstream listeners (such as the Transcription context) that
    a local audio file is ready for speech-to-text processing.
    """
    audio_path: Path
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, kw_only=True)
class TranscriptionCompleted(DomainEvent):
    """Emitted when the Transcription context completes speech-to-text processing.

    Signals to downstream listeners (such as the Knowledge context) that
    the verbatim transcription JSON is available for second brain note synthesis.
    """
    transcript_path: Path
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, kw_only=True)
class KnowledgeSynthesized(DomainEvent):
    """Emitted when the Knowledge context completes raw note extraction and wiki synthesis.

    Indicates the final step of the pipeline where both raw transcription notes
    and synthesized wiki articles have been committed to the Obsidian Vault.
    """
    raw_note_path: Path
    wiki_articles_updated: list[Path] = field(default_factory=list)



T = TypeVar("T", bound=DomainEvent)
Handler = Callable[[Any], None]


class EventBus:
    """Thread-safe, in-memory publish-subscriber event bus.

    Used for decoupling contexts in the modular monolith. It coordinates workflow
    flows across context boundaries without introducing tight physical coupling.
    """
    def __init__(self) -> None:
        """Initialize the event handlers registry and thread lock mechanism."""
        # Step 1: Initialize in-memory dictionary mapping event types to active handlers
        self._handlers: dict[Type[DomainEvent], list[Handler]] = {}
        # Step 2: Initialize thread Lock to secure handler modification and dispatching
        # We do this because the pipeline might process multiple events concurrently
        self._lock = threading.Lock()

    def subscribe(self, event_type: Type[T], handler: Callable[[T], None]) -> None:
        """Subscribe a handler callback to a specific type of domain event.

        Args:
            event_type: The DomainEvent subclass to listen for.
            handler: A callback function invoked when the event is published.
        """
        # Step 1: Acquire lock to ensure thread-safe modification of handlers registry
        with self._lock:
            # Step 2: Initialize handler list if it's the first subscription for this event type
            if event_type not in self._handlers:
                self._handlers[event_type] = []
            # Step 3: Append handler callback to list
            self._handlers[event_type].append(handler)

    def publish(self, event: DomainEvent) -> None:
        """Publish a domain event to all subscribed handlers.

        Invocations are run sequentially in the caller thread to preserve ordering
        and simple transaction/worker boundaries.

        Args:
            event: The DomainEvent instance being dispatched.
        """
        # Step 1: Resolve the concrete type of the incoming event
        event_type = type(event)
        handlers_to_call = []
        
        # Step 2: Lock registry to safely extract handlers without concurrent modification conflicts
        with self._lock:
            # Step 3: Match exact event type subscribers and add them to execution queue
            if event_type in self._handlers:
                handlers_to_call.extend(self._handlers[event_type])
                
            # Step 4: Identify and include parent class handlers (polymorphic dispatching support)
            # This allows subscribing to the base DomainEvent to track system-wide events
            for registered_type, handlers in self._handlers.items():
                if registered_type != event_type and issubclass(event_type, registered_type):
                    handlers_to_call.extend(handlers)

        # Step 5: Execute handlers sequentially in the current thread context
        # We run this synchronously to avoid thread scheduling delays and to keep the pipeline simple
        for handler in handlers_to_call:
            handler(event)
