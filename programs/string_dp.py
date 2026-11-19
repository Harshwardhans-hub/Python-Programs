"""Dynamic-programming exercises for common string problems."""


def _validate_strings(first: str, second: str | None = None) -> None:
    if not isinstance(first, str) or (second is not None and not isinstance(second, str)):
        raise TypeError("inputs must be strings")


def longest_common_subsequence_length(first: str, second: str) -> int:
    """Return the length of the longest common subsequence."""
    _validate_strings(first, second)
    previous = [0] * (len(second) + 1)
    for char_first in first:
        current = [0]
        for index, char_second in enumerate(second, start=1):
            if char_first == char_second:
                current.append(previous[index - 1] + 1)
            else:
                current.append(max(previous[index], current[index - 1]))
        previous = current
    return previous[-1]


def edit_distance(first: str, second: str) -> int:
    """Return Levenshtein distance using insert, delete, and replace operations."""
    _validate_strings(first, second)
    previous = list(range(len(second) + 1))
    for row, char_first in enumerate(first, start=1):
        current = [row]
        for column, char_second in enumerate(second, start=1):
            current.append(min(
                current[column - 1] + 1,
                previous[column] + 1,
                previous[column - 1] + (char_first != char_second),
            ))
        previous = current
    return previous[-1]


def longest_palindromic_subsequence_length(text: str) -> int:
    """Return the longest palindromic subsequence length."""
    _validate_strings(text)
    size = len(text)
    if size == 0:
        return 0
    best = [[0] * size for _ in range(size)]
    for left in range(size - 1, -1, -1):
        best[left][left] = 1
        for right in range(left + 1, size):
            if text[left] == text[right]:
                best[left][right] = 2 + best[left + 1][right - 1]
            else:
                best[left][right] = max(best[left + 1][right], best[left][right - 1])
    return best[0][-1]
