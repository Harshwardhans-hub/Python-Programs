"""Text processing helpers suitable for beginner Python exercises."""

from collections import Counter
import re


def normalize_whitespace(text: str) -> str:
    """Collapse all whitespace runs into single spaces and trim the ends."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return " ".join(text.split())


def is_palindrome(text: str) -> bool:
    """Check a phrase as a palindrome, ignoring case and punctuation."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    normalized = "".join(character.casefold() for character in text if character.isalnum())
    return normalized == normalized[::-1]


def word_frequency(text: str) -> dict[str, int]:
    """Count case-insensitive words while preserving first-seen key order."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    words = re.findall(r"\b[\w']+\b", text.casefold())
    return dict(Counter(words))
