import uuid
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Type, TypeVar
from dataclasses import dataclass, field
from isb.shared_kernel.types import ContentId
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
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁEventBusǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁEventBusǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁEventBusǁ__init____mutmut_orig(self) -> None:
        """Initialize the event handlers registry and thread lock mechanism."""
        # Step 1: Initialize in-memory dictionary mapping event types to active handlers
        self._handlers: dict[Type[DomainEvent], list[Handler]] = {}
        # Step 2: Initialize thread Lock to secure handler modification and dispatching
        # We do this because the pipeline might process multiple events concurrently
        self._lock = threading.Lock()
    def xǁEventBusǁ__init____mutmut_1(self) -> None:
        """Initialize the event handlers registry and thread lock mechanism."""
        # Step 1: Initialize in-memory dictionary mapping event types to active handlers
        self._handlers: dict[Type[DomainEvent], list[Handler]] = None
        # Step 2: Initialize thread Lock to secure handler modification and dispatching
        # We do this because the pipeline might process multiple events concurrently
        self._lock = threading.Lock()
    def xǁEventBusǁ__init____mutmut_2(self) -> None:
        """Initialize the event handlers registry and thread lock mechanism."""
        # Step 1: Initialize in-memory dictionary mapping event types to active handlers
        self._handlers: dict[Type[DomainEvent], list[Handler]] = {}
        # Step 2: Initialize thread Lock to secure handler modification and dispatching
        # We do this because the pipeline might process multiple events concurrently
        self._lock = None
    
    xǁEventBusǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁEventBusǁ__init____mutmut_1': xǁEventBusǁ__init____mutmut_1, 
        'xǁEventBusǁ__init____mutmut_2': xǁEventBusǁ__init____mutmut_2
    }
    xǁEventBusǁ__init____mutmut_orig.__name__ = 'xǁEventBusǁ__init__'

    def subscribe(self, event_type: Type[T], handler: Callable[[T], None]) -> None:
        args = [event_type, handler]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁEventBusǁsubscribe__mutmut_orig'), object.__getattribute__(self, 'xǁEventBusǁsubscribe__mutmut_mutants'), args, kwargs, self)

    def xǁEventBusǁsubscribe__mutmut_orig(self, event_type: Type[T], handler: Callable[[T], None]) -> None:
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

    def xǁEventBusǁsubscribe__mutmut_1(self, event_type: Type[T], handler: Callable[[T], None]) -> None:
        """Subscribe a handler callback to a specific type of domain event.

        Args:
            event_type: The DomainEvent subclass to listen for.
            handler: A callback function invoked when the event is published.
        """
        # Step 1: Acquire lock to ensure thread-safe modification of handlers registry
        with self._lock:
            # Step 2: Initialize handler list if it's the first subscription for this event type
            if event_type in self._handlers:
                self._handlers[event_type] = []
            # Step 3: Append handler callback to list
            self._handlers[event_type].append(handler)

    def xǁEventBusǁsubscribe__mutmut_2(self, event_type: Type[T], handler: Callable[[T], None]) -> None:
        """Subscribe a handler callback to a specific type of domain event.

        Args:
            event_type: The DomainEvent subclass to listen for.
            handler: A callback function invoked when the event is published.
        """
        # Step 1: Acquire lock to ensure thread-safe modification of handlers registry
        with self._lock:
            # Step 2: Initialize handler list if it's the first subscription for this event type
            if event_type not in self._handlers:
                self._handlers[event_type] = None
            # Step 3: Append handler callback to list
            self._handlers[event_type].append(handler)

    def xǁEventBusǁsubscribe__mutmut_3(self, event_type: Type[T], handler: Callable[[T], None]) -> None:
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
            self._handlers[event_type].append(None)
    
    xǁEventBusǁsubscribe__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁEventBusǁsubscribe__mutmut_1': xǁEventBusǁsubscribe__mutmut_1, 
        'xǁEventBusǁsubscribe__mutmut_2': xǁEventBusǁsubscribe__mutmut_2, 
        'xǁEventBusǁsubscribe__mutmut_3': xǁEventBusǁsubscribe__mutmut_3
    }
    xǁEventBusǁsubscribe__mutmut_orig.__name__ = 'xǁEventBusǁsubscribe'

    def publish(self, event: DomainEvent) -> None:
        args = [event]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁEventBusǁpublish__mutmut_orig'), object.__getattribute__(self, 'xǁEventBusǁpublish__mutmut_mutants'), args, kwargs, self)

    def xǁEventBusǁpublish__mutmut_orig(self, event: DomainEvent) -> None:
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

    def xǁEventBusǁpublish__mutmut_1(self, event: DomainEvent) -> None:
        """Publish a domain event to all subscribed handlers.

        Invocations are run sequentially in the caller thread to preserve ordering
        and simple transaction/worker boundaries.

        Args:
            event: The DomainEvent instance being dispatched.
        """
        # Step 1: Resolve the concrete type of the incoming event
        event_type = None
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

    def xǁEventBusǁpublish__mutmut_2(self, event: DomainEvent) -> None:
        """Publish a domain event to all subscribed handlers.

        Invocations are run sequentially in the caller thread to preserve ordering
        and simple transaction/worker boundaries.

        Args:
            event: The DomainEvent instance being dispatched.
        """
        # Step 1: Resolve the concrete type of the incoming event
        event_type = type(None)
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

    def xǁEventBusǁpublish__mutmut_3(self, event: DomainEvent) -> None:
        """Publish a domain event to all subscribed handlers.

        Invocations are run sequentially in the caller thread to preserve ordering
        and simple transaction/worker boundaries.

        Args:
            event: The DomainEvent instance being dispatched.
        """
        # Step 1: Resolve the concrete type of the incoming event
        event_type = type(event)
        handlers_to_call = None
        
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

    def xǁEventBusǁpublish__mutmut_4(self, event: DomainEvent) -> None:
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
            if event_type not in self._handlers:
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

    def xǁEventBusǁpublish__mutmut_5(self, event: DomainEvent) -> None:
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
                handlers_to_call.extend(None)
                
            # Step 4: Identify and include parent class handlers (polymorphic dispatching support)
            # This allows subscribing to the base DomainEvent to track system-wide events
            for registered_type, handlers in self._handlers.items():
                if registered_type != event_type and issubclass(event_type, registered_type):
                    handlers_to_call.extend(handlers)

        # Step 5: Execute handlers sequentially in the current thread context
        # We run this synchronously to avoid thread scheduling delays and to keep the pipeline simple
        for handler in handlers_to_call:
            handler(event)

    def xǁEventBusǁpublish__mutmut_6(self, event: DomainEvent) -> None:
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
                if registered_type != event_type or issubclass(event_type, registered_type):
                    handlers_to_call.extend(handlers)

        # Step 5: Execute handlers sequentially in the current thread context
        # We run this synchronously to avoid thread scheduling delays and to keep the pipeline simple
        for handler in handlers_to_call:
            handler(event)

    def xǁEventBusǁpublish__mutmut_7(self, event: DomainEvent) -> None:
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
                if registered_type == event_type and issubclass(event_type, registered_type):
                    handlers_to_call.extend(handlers)

        # Step 5: Execute handlers sequentially in the current thread context
        # We run this synchronously to avoid thread scheduling delays and to keep the pipeline simple
        for handler in handlers_to_call:
            handler(event)

    def xǁEventBusǁpublish__mutmut_8(self, event: DomainEvent) -> None:
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
                if registered_type != event_type and issubclass(None, registered_type):
                    handlers_to_call.extend(handlers)

        # Step 5: Execute handlers sequentially in the current thread context
        # We run this synchronously to avoid thread scheduling delays and to keep the pipeline simple
        for handler in handlers_to_call:
            handler(event)

    def xǁEventBusǁpublish__mutmut_9(self, event: DomainEvent) -> None:
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
                if registered_type != event_type and issubclass(event_type, None):
                    handlers_to_call.extend(handlers)

        # Step 5: Execute handlers sequentially in the current thread context
        # We run this synchronously to avoid thread scheduling delays and to keep the pipeline simple
        for handler in handlers_to_call:
            handler(event)

    def xǁEventBusǁpublish__mutmut_10(self, event: DomainEvent) -> None:
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
                if registered_type != event_type and issubclass(registered_type):
                    handlers_to_call.extend(handlers)

        # Step 5: Execute handlers sequentially in the current thread context
        # We run this synchronously to avoid thread scheduling delays and to keep the pipeline simple
        for handler in handlers_to_call:
            handler(event)

    def xǁEventBusǁpublish__mutmut_11(self, event: DomainEvent) -> None:
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
                if registered_type != event_type and issubclass(event_type, ):
                    handlers_to_call.extend(handlers)

        # Step 5: Execute handlers sequentially in the current thread context
        # We run this synchronously to avoid thread scheduling delays and to keep the pipeline simple
        for handler in handlers_to_call:
            handler(event)

    def xǁEventBusǁpublish__mutmut_12(self, event: DomainEvent) -> None:
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
                    handlers_to_call.extend(None)

        # Step 5: Execute handlers sequentially in the current thread context
        # We run this synchronously to avoid thread scheduling delays and to keep the pipeline simple
        for handler in handlers_to_call:
            handler(event)

    def xǁEventBusǁpublish__mutmut_13(self, event: DomainEvent) -> None:
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
            handler(None)
    
    xǁEventBusǁpublish__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁEventBusǁpublish__mutmut_1': xǁEventBusǁpublish__mutmut_1, 
        'xǁEventBusǁpublish__mutmut_2': xǁEventBusǁpublish__mutmut_2, 
        'xǁEventBusǁpublish__mutmut_3': xǁEventBusǁpublish__mutmut_3, 
        'xǁEventBusǁpublish__mutmut_4': xǁEventBusǁpublish__mutmut_4, 
        'xǁEventBusǁpublish__mutmut_5': xǁEventBusǁpublish__mutmut_5, 
        'xǁEventBusǁpublish__mutmut_6': xǁEventBusǁpublish__mutmut_6, 
        'xǁEventBusǁpublish__mutmut_7': xǁEventBusǁpublish__mutmut_7, 
        'xǁEventBusǁpublish__mutmut_8': xǁEventBusǁpublish__mutmut_8, 
        'xǁEventBusǁpublish__mutmut_9': xǁEventBusǁpublish__mutmut_9, 
        'xǁEventBusǁpublish__mutmut_10': xǁEventBusǁpublish__mutmut_10, 
        'xǁEventBusǁpublish__mutmut_11': xǁEventBusǁpublish__mutmut_11, 
        'xǁEventBusǁpublish__mutmut_12': xǁEventBusǁpublish__mutmut_12, 
        'xǁEventBusǁpublish__mutmut_13': xǁEventBusǁpublish__mutmut_13
    }
    xǁEventBusǁpublish__mutmut_orig.__name__ = 'xǁEventBusǁpublish'
