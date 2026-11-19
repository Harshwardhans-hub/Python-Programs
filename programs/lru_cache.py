"""A small least-recently-used cache backed by OrderedDict."""

from collections import OrderedDict
from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class LRUCache(Generic[K, V]):
    """Fixed-capacity cache that evicts the least recently used key."""

    def __init__(self, capacity: int) -> None:
        if isinstance(capacity, bool) or not isinstance(capacity, int):
            raise TypeError("capacity must be an integer")
        if capacity < 1:
            raise ValueError("capacity must be at least 1")
        self.capacity = capacity
        self._values: OrderedDict[K, V] = OrderedDict()

    def get(self, key: K) -> V | None:
        """Return a cached value and mark its key as most recently used."""
        if key not in self._values:
            return None
        self._values.move_to_end(key)
        return self._values[key]

    def put(self, key: K, value: V) -> None:
        """Insert or update a key, evicting the least recently used if needed."""
        if key in self._values:
            self._values.move_to_end(key)
        self._values[key] = value
        if len(self._values) > self.capacity:
            self._values.popitem(last=False)

    def __len__(self) -> int:
        return len(self._values)

    def __contains__(self, key: object) -> bool:
        return key in self._values
