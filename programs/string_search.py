"""Knuth-Morris-Pratt substring search with overlapping matches."""

def _build_prefix_table(pattern: str) -> list[int]:
    prefix = [0] * len(pattern)
    matched = 0
    for index in range(1, len(pattern)):
        while matched and pattern[index] != pattern[matched]:
            matched = prefix[matched - 1]
        if pattern[index] == pattern[matched]:
            matched += 1
        prefix[index] = matched
    return prefix


def find_all_occurrences(text: str, pattern: str) -> list[int]:
    """Return all zero-based pattern start positions, including overlaps."""
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("text and pattern must be strings")
    if not pattern:
        raise ValueError("pattern cannot be empty")
    matches: list[int] = []
    prefix = _build_prefix_table(pattern)
    matched = 0
    for index, character in enumerate(text):
        while matched and character != pattern[matched]:
            matched = prefix[matched - 1]
        if character == pattern[matched]:
            matched += 1
        if matched == len(pattern):
            matches.append(index - len(pattern) + 1)
            matched = prefix[matched - 1]
    return matches
