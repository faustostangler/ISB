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
    """
    content_id: ContentId
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    occurred_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(frozen=True, kw_only=True)
class AudioExtracted(DomainEvent):
    """Emitted when the Ingestion context has extracted the audio for an episode."""
    audio_path: Path
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, kw_only=True)
class TranscriptionCompleted(DomainEvent):
    """Emitted when the Transcription context completes speech-to-text processing."""
    transcript_path: Path
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, kw_only=True)
class KnowledgeSynthesized(DomainEvent):
    """Emitted when the Knowledge context completes raw note extraction and wiki synthesis."""
    raw_note_path: Path
    wiki_articles_updated: list[Path] = field(default_factory=list)



T = TypeVar("T", bound=DomainEvent)
Handler = Callable[[Any], None]


class EventBus:
    """Thread-safe, in-memory publish-subscriber event bus.

    Used for decoupling contexts in the modular monolith.
    """
    def __init__(self) -> None:
        self._handlers: dict[Type[DomainEvent], list[Handler]] = {}
        self._lock = threading.Lock()

    def subscribe(self, event_type: Type[T], handler: Callable[[T], None]) -> None:
        """Subscribe a handler callback to a specific type of domain event."""
        with self._lock:
            if event_type not in self._handlers:
                self._handlers[event_type] = []
            self._handlers[event_type].append(handler)

    def publish(self, event: DomainEvent) -> None:
        """Publish a domain event to all subscribed handlers.

        Invocations are run sequentially in the caller thread to preserve ordering
        and simple transaction/worker boundaries.
        """
        event_type = type(event)
        handlers_to_call = []
        
        with self._lock:
            # Match exact event type
            if event_type in self._handlers:
                handlers_to_call.extend(self._handlers[event_type])
            # Also invoke parent class handlers if registered (polymorphism support)
            for registered_type, handlers in self._handlers.items():
                if registered_type != event_type and issubclass(event_type, registered_type):
                    handlers_to_call.extend(handlers)

        for handler in handlers_to_call:
            handler(event)
