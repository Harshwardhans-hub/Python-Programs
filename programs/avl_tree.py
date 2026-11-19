"""AVL binary search tree with unique keys and automatic rebalancing."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class _Node(Generic[T]):
    key: T
    height: int = 1
    left: _Node[T] | None = None
    right: _Node[T] | None = None


def _height(node: _Node[T] | None) -> int:
    return node.height if node else 0


def _refresh(node: _Node[T]) -> None:
    node.height = 1 + max(_height(node.left), _height(node.right))


def _balance(node: _Node[T]) -> int:
    return _height(node.left) - _height(node.right)


def _rotate_right(root: _Node[T]) -> _Node[T]:
    pivot = root.left
    assert pivot is not None
    transfer = pivot.right
    pivot.right = root
    root.left = transfer
    _refresh(root)
    _refresh(pivot)
    return pivot


def _rotate_left(root: _Node[T]) -> _Node[T]:
    pivot = root.right
    assert pivot is not None
    transfer = pivot.left
    pivot.left = root
    root.right = transfer
    _refresh(root)
    _refresh(pivot)
    return pivot


def _rebalance(node: _Node[T]) -> _Node[T]:
    _refresh(node)
    balance = _balance(node)
    if balance > 1:
        if node.left is not None and _balance(node.left) < 0:
            node.left = _rotate_left(node.left)
        return _rotate_right(node)
    if balance < -1:
        if node.right is not None and _balance(node.right) > 0:
            node.right = _rotate_right(node.right)
        return _rotate_left(node)
    return node


class AVLTree(Generic[T]):
    """Ordered set backed by an AVL tree; duplicate keys are ignored."""

    def __init__(self, values=()) -> None:
        self._root: _Node[T] | None = None
        self._size = 0
        for value in values:
            self.insert(value)

    def insert(self, key: T) -> bool:
        """Insert key; return False when it already exists."""
        inserted = False

        def place(node: _Node[T] | None) -> _Node[T]:
            nonlocal inserted
            if node is None:
                inserted = True
                return _Node(key)
            if key < node.key:
                node.left = place(node.left)
            elif key > node.key:
                node.right = place(node.right)
            else:
                return node
            return _rebalance(node)

        self._root = place(self._root)
        if inserted:
            self._size += 1
        return inserted

    def search(self, key: T) -> bool:
        """Return whether key is present."""
        node = self._root
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return True
        return False

    def in_order(self) -> list[T]:
        """Return keys in ascending sorted order."""
        result: list[T] = []

        def visit(node: _Node[T] | None) -> None:
            if node is None:
                return
            visit(node.left)
            result.append(node.key)
            visit(node.right)

        visit(self._root)
        return result

    @property
    def height(self) -> int:
        """Return tree height measured in nodes; an empty tree has height zero."""
        return _height(self._root)

    def __len__(self) -> int:
        return self._size

    def __contains__(self, key: object) -> bool:
        return self.search(key)  # type: ignore[arg-type]

    def __iter__(self):
        return iter(self.in_order())
