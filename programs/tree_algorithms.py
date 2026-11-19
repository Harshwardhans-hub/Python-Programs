"""Structural checks and measurements for binary trees."""

from __future__ import annotations

from collections import deque
from programs.tree_utils import BinaryTreeNode


def is_symmetric(root: BinaryTreeNode[object] | None) -> bool:
    """Return whether a binary tree mirrors itself around its root."""
    if root is None:
        return True
    pending = deque([(root.left, root.right)])
    while pending:
        left, right = pending.popleft()
        if left is None or right is None:
            if left is not right:
                return False
            continue
        if left.value != right.value:
            return False
        pending.append((left.left, right.right))
        pending.append((left.right, right.left))
    return True


def is_balanced(root: BinaryTreeNode[object] | None) -> bool:
    """Return whether every node's child subtree heights differ by at most one."""
    def check(node: BinaryTreeNode[object] | None) -> int:
        if node is None:
            return 0
        left_height = check(node.left)
        if left_height < 0:
            return -1
        right_height = check(node.right)
        if right_height < 0 or abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)

    return check(root) >= 0


def diameter(root: BinaryTreeNode[object] | None) -> int:
    """Return the longest path between any two nodes, measured in edges."""
    longest = 0

    def height(node: BinaryTreeNode[object] | None) -> int:
        nonlocal longest
        if node is None:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        longest = max(longest, left_height + right_height)
        return 1 + max(left_height, right_height)

    height(root)
    return longest
