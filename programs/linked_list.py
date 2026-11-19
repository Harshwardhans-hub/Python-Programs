"""A minimal singly linked list for data-structure practice."""

from collections.abc import Iterable, Iterator
from typing import Generic, TypeVar

T = TypeVar("T")


class _Node(Generic[T]):
    def __init__(self, value: T, next_node: "_Node[T] | None" = None) -> None:
        self.value = value
        self.next = next_node


class SinglyLinkedList(Generic[T]):
    """Linked list supporting append, prepend, indexed insert, and removal."""

    def __init__(self, values: Iterable[T] = ()) -> None:
        self._head: _Node[T] | None = None
        self._tail: _Node[T] | None = None
        self._length = 0
        for value in values:
            self.append(value)

    def append(self, value: T) -> None:
        node = _Node(value)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._length += 1

    def prepend(self, value: T) -> None:
        self._head = _Node(value, self._head)
        if self._tail is None:
            self._tail = self._head
        self._length += 1

    def insert(self, index: int, value: T) -> None:
        if isinstance(index, bool) or not isinstance(index, int):
            raise TypeError("index must be an integer")
        if index < 0 or index > self._length:
            raise IndexError("linked-list index out of range")
        if index == 0:
            self.prepend(value)
            return
        if index == self._length:
            self.append(value)
            return
        previous = self._head
        for _ in range(index - 1):
            assert previous is not None
            previous = previous.next
        assert previous is not None
        previous.next = _Node(value, previous.next)
        self._length += 1

    def remove_first(self, value: T) -> bool:
        """Remove the first matching value; return whether one was found."""
        previous: _Node[T] | None = None
        current = self._head
        while current is not None:
            if current.value == value:
                if previous is None:
                    self._head = current.next
                else:
                    previous.next = current.next
                if current is self._tail:
                    self._tail = previous
                self._length -= 1
                return True
            previous, current = current, current.next
        return False

    def search(self, value: T) -> int | None:
        for index, item in enumerate(self):
            if item == value:
                return index
        return None

    def to_list(self) -> list[T]:
        return list(self)

    def __iter__(self) -> Iterator[T]:
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._length

    def __bool__(self) -> bool:
        return self._head is not None
