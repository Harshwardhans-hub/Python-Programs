"""Hash-map patterns for common interview exercises."""

from collections import defaultdict
from collections.abc import Sequence
from numbers import Real


def two_sum(values: Sequence[Real], target: Real) -> tuple[int, int] | None:
    """Return indices of the first encountered pair that sums to target."""
    seen: dict[Real, int] = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        if value not in seen:
            seen[value] = index
    return None


def group_anagrams(words: Sequence[str]) -> list[list[str]]:
    """Group words by their sorted character signatures, preserving group order."""
    groups: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for word in words:
        if not isinstance(word, str):
            raise TypeError("all words must be strings")
        groups[tuple(sorted(word))].append(word)
    return list(groups.values())
