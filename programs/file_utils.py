"""Read-only file helpers; these functions never modify input files."""

from pathlib import Path


def count_lines(path: str | Path, *, include_blank: bool = True, encoding: str = "utf-8") -> int:
    """Count lines in a text file, optionally excluding whitespace-only lines."""
    file_path = Path(path)
    total = 0
    with file_path.open("r", encoding=encoding) as source:
        for line in source:
            if include_blank or line.strip():
                total += 1
    return total


def find_in_file(
    path: str | Path,
    phrase: str,
    *,
    case_sensitive: bool = True,
    encoding: str = "utf-8",
) -> list[tuple[int, str]]:
    """Return (1-based line number, line text) pairs containing *phrase*."""
    if not isinstance(phrase, str):
        raise TypeError("phrase must be a string")
    if not phrase:
        raise ValueError("phrase cannot be empty")
    target = phrase if case_sensitive else phrase.casefold()
    matches: list[tuple[int, str]] = []
    with Path(path).open("r", encoding=encoding) as source:
        for line_number, line in enumerate(source, start=1):
            candidate = line if case_sensitive else line.casefold()
            if target in candidate:
                matches.append((line_number, line.rstrip("\\r\\n")))
    return matches
