"""Binary-tree node and traversal helpers."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class BinaryTreeNode(Generic[T]):
    value: T
    left: BinaryTreeNode[T] | None = None
    right: BinaryTreeNode[T] | None = None


def preorder(root: BinaryTreeNode[T] | None) -> list[T]:
    """Return root-left-right traversal values."""
    if root is None:
        return []
    result: list[T] = []
    pending = [root]
    while pending:
        node = pending.pop()
        result.append(node.value)
        if node.right is not None:
            pending.append(node.right)
        if node.left is not None:
            pending.append(node.left)
    return result


def inorder(root: BinaryTreeNode[T] | None) -> list[T]:
    """Return left-root-right traversal values."""
    result: list[T] = []
    pending: list[BinaryTreeNode[T]] = []
    current = root
    while current is not None or pending:
        while current is not None:
            pending.append(current)
            current = current.left
        current = pending.pop()
        result.append(current.value)
        current = current.right
    return result


def postorder(root: BinaryTreeNode[T] | None) -> list[T]:
    """Return left-right-root traversal values."""
    if root is None:
        return []
    result: list[T] = []
    pending: list[tuple[BinaryTreeNode[T], bool]] = [(root, False)]
    while pending:
        node, visited = pending.pop()
        if visited:
            result.append(node.value)
            continue
        pending.append((node, True))
        if node.right is not None:
            pending.append((node.right, False))
        if node.left is not None:
            pending.append((node.left, False))
    return result


def level_order(root: BinaryTreeNode[T] | None) -> list[T]:
    """Return breadth-first traversal values."""
    if root is None:
        return []
    result: list[T] = []
    pending = deque([root])
    while pending:
        node = pending.popleft()
        result.append(node.value)
        if node.left is not None:
            pending.append(node.left)
        if node.right is not None:
            pending.append(node.right)
    return result


def height(root: BinaryTreeNode[T] | None) -> int:
    """Return tree height measured in nodes; an empty tree has height zero."""
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))
