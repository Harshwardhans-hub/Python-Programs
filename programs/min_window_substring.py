"""Minimum window substring using a frequency-aware sliding window."""

from collections import Counter


def minimum_window_substring(text: str, target: str) -> str:
    """Return the shortest substring containing every target character.

    Character multiplicity matters. Return an empty string when target is empty
    or no valid window exists.
    """
    if not isinstance(text, str) or not isinstance(target, str):
        raise TypeError("text and target must be strings")
    if not target or len(target) > len(text):
        return ""

    required = Counter(target)
    window: Counter[str] = Counter()
    formed = 0
    required_kinds = len(required)
    left = 0
    best_start = 0
    best_length = len(text) + 1

    for right, character in enumerate(text):
        if character in required:
            window[character] += 1
            if window[character] == required[character]:
                formed += 1

        while formed == required_kinds:
            current_length = right - left + 1
            if current_length < best_length:
                best_start = left
                best_length = current_length

            outgoing = text[left]
            if outgoing in required:
                if window[outgoing] == required[outgoing]:
                    formed -= 1
                window[outgoing] -= 1
            left += 1

    if best_length > len(text):
        return ""
    return text[best_start : best_start + best_length]
