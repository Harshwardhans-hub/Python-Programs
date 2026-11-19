"""Binary search tree operations for comparable values."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class BSTNode(Generic[T]):
    value: T
    left: BSTNode[T] | None = None
    right: BSTNode[T] | None = None


def insert(root: BSTNode[T] | None, value: T) -> BSTNode[T]:
    """Insert value; duplicate values are ignored."""
    if root is None:
        return BSTNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root


def contains(root: BSTNode[T] | None, value: T) -> bool:
    current = root
    while current is not None:
        if value == current.value:
            return True
        current = current.left if value < current.value else current.right
    return False


def inorder_values(root: BSTNode[T] | None) -> list[T]:
    result: list[T] = []
    pending: list[BSTNode[T]] = []
    current = root
    while current is not None or pending:
        while current is not None:
            pending.append(current)
            current = current.left
        current = pending.pop()
        result.append(current.value)
        current = current.right
    return result


def delete(root: BSTNode[T] | None, value: T) -> BSTNode[T] | None:
    """Delete value while preserving BST ordering."""
    if root is None:
        return None
    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        successor = root.right
        while successor.left is not None:
            successor = successor.left
        root.value = successor.value
        root.right = delete(root.right, successor.value)
    return root
