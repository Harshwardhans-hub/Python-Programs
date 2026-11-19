"""Breadth-first word ladder search."""

from collections import defaultdict, deque
from collections.abc import Iterable


def word_ladder_length(begin: str, end: str, words: Iterable[str]) -> int | None:
    """Return the fewest words in a one-letter transformation sequence.

    Every intermediate word must belong to words; begin need not. Return None
    if end cannot be reached. begin == end has a sequence length of one.
    """
    if not isinstance(begin, str) or not isinstance(end, str):
        raise TypeError("begin and end must be strings")
    if not begin or not end:
        raise ValueError("begin and end cannot be empty")
    if len(begin) != len(end):
        raise ValueError("begin and end must have equal lengths")
    if begin == end:
        return 1

    candidates = list(words)
    if any(not isinstance(word, str) for word in candidates):
        raise TypeError("dictionary entries must be strings")
    word_set = {word for word in candidates if len(word) == len(begin)}
    if end not in word_set:
        return None
    word_set.add(begin)

    buckets: dict[tuple[int, str, str], list[str]] = defaultdict(list)
    for word in word_set:
        for index in range(len(word)):
            pattern = (index, word[:index], word[index + 1 :])
            buckets[pattern].append(word)

    pending = deque([(begin, 1)])
    visited = {begin}
    while pending:
        word, distance = pending.popleft()
        for index in range(len(word)):
            pattern = (index, word[:index], word[index + 1 :])
            for neighbor in buckets[pattern]:
                if neighbor == end:
                    return distance + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    pending.append((neighbor, distance + 1))
            buckets[pattern].clear()
    return None
