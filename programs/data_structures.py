"""Small stack and queue implementations for data-structure practice."""

from collections import deque
from collections.abc import Iterable
from typing import Deque, Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """Last-in, first-out collection with constant-time end operations."""

    def __init__(self, values: Iterable[T] = ()) -> None:
        self._items = list(values)

    def push(self, value: T) -> None:
        self._items.append(value)

    def pop(self) -> T:
        """Remove and return the newest item."""
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        """Return the newest item without removing it."""
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)


class Queue(Generic[T]):
    """First-in, first-out collection backed by collections.deque."""

    def __init__(self, values: Iterable[T] = ()) -> None:
        self._items: Deque[T] = deque(values)

    def enqueue(self, value: T) -> None:
        self._items.append(value)

    def dequeue(self) -> T:
        """Remove and return the oldest item."""
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self) -> T:
        """Return the oldest item without removing it."""
        if not self._items:
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)
