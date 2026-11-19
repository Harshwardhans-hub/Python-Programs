"""Common string algorithms for interview and practice exercises."""

from collections import Counter
from collections.abc import Sequence


def is_anagram(first: str, second: str) -> bool:
    """Compare strings while ignoring case and non-alphanumeric characters."""
    if not isinstance(first, str) or not isinstance(second, str):
        raise TypeError("both inputs must be strings")
    clean = lambda value: [char.casefold() for char in value if char.isalnum()]
    return Counter(clean(first)) == Counter(clean(second))


def first_unique_character_index(text: str) -> int | None:
    """Return the index of the first character occurring exactly once."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    counts = Counter(text)
    return next((index for index, char in enumerate(text) if counts[char] == 1), None)


def longest_common_prefix(words: Sequence[str]) -> str:
    """Return the longest common prefix shared by all supplied words."""
    if not words:
        return ""
    if any(not isinstance(word, str) for word in words):
        raise TypeError("all words must be strings")
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


def run_length_encode(text: str) -> list[tuple[str, int]]:
    """Encode consecutive repeated characters as (character, count) pairs."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not text:
        return []
    encoded: list[tuple[str, int]] = []
    current = text[0]
    count = 1
    for char in text[1:]:
        if char == current:
            count += 1
        else:
            encoded.append((current, count))
            current, count = char, 1
    encoded.append((current, count))
    return encoded


def run_length_decode(encoded: Sequence[tuple[str, int]]) -> str:
    """Decode output produced by run_length_encode."""
    parts: list[str] = []
    for item in encoded:
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("each item must be a (character, count) pair")
        char, count = item
        if not isinstance(char, str) or len(char) != 1:
            raise ValueError("character must be a single character")
        if isinstance(count, bool) or not isinstance(count, int) or count < 0:
            raise ValueError("count must be a non-negative integer")
        parts.append(char * count)
    return "".join(parts)
