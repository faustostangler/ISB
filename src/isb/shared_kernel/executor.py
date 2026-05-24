from abc import ABC, abstractmethod
from typing import Callable

class TaskExecutor(ABC):
    """Port interface defining task execution concurrency behaviors.
    
    Provides an abstraction layer over execution environments to enable
    deterministic testing and flexible runtime threading policies.
    """

    @abstractmethod
    def submit(self, fn: Callable[[], None]) -> None:
        """Submit a callable task for execution.
        
        Args:
            fn: A zero-argument function returning None.
        """
        pass

    @abstractmethod
    def shutdown(self, wait: bool = True) -> None:
        """Shutdown the executor resources and cleanup background workers.
        
        Args:
            wait: If True, blocks until all pending tasks finish executing.
        """
        pass


class InlineTaskExecutor(TaskExecutor):
    """Synchronous executor for deterministic unit testing.
    
    Executes all tasks sequentially in the calling thread, propagating
    any raised exceptions immediately back to the caller.
    """

    def submit(self, fn: Callable[[], None]) -> None:
        # Step 1: Run the callable task synchronously
        # In unit tests, we want immediate synchronous execution to verify results.
        raise NotImplementedError("InlineTaskExecutor.submit skeleton stub")

    def shutdown(self, wait: bool = True) -> None:
        # Step 2: No-op for synchronous executor
        # There are no background threads or resources to clean up.
        raise NotImplementedError("InlineTaskExecutor.shutdown skeleton stub")


class ThreadPoolTaskExecutor(TaskExecutor):
    """Concurrent executor backed by a thread pool.
    
    Offloads tasks to a ThreadPoolExecutor, isolating execution context
    and isolating main execution threads from worker-level failures.
    """

    def __init__(self, max_workers: int = 4) -> None:
        """Initialize the thread pool executor.
        
        Args:
            max_workers: Maximum number of background worker threads to allocate.
        """
        # Step 1: Initialize the ThreadPoolExecutor
        # The constructor sets up the worker pool boundaries.
        raise NotImplementedError("ThreadPoolTaskExecutor.__init__ skeleton stub")

    def submit(self, fn: Callable[[], None]) -> None:
        # Step 2: Submit the callable task to the internal thread pool
        # This executes the callable asynchronously in a worker thread.
        raise NotImplementedError("ThreadPoolTaskExecutor.submit skeleton stub")

    def shutdown(self, wait: bool = True) -> None:
        # Step 3: Call shutdown on the underlying ThreadPoolExecutor
        # This cleans up OS threads and blocks if wait is True.
        raise NotImplementedError("ThreadPoolTaskExecutor.shutdown skeleton stub")
