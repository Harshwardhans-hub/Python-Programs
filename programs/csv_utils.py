"""Convenience wrappers for reading and writing dictionary-based CSV files."""

import csv
from pathlib import Path
from collections.abc import Iterable, Mapping


def read_csv_rows(path: str | Path, *, encoding: str = "utf-8") -> list[dict[str, str]]:
    """Read a CSV file as dictionaries keyed by its header row."""
    with Path(path).open("r", encoding=encoding, newline="") as source:
        return list(csv.DictReader(source))


def write_csv_rows(
    path: str | Path,
    fieldnames: list[str],
    rows: Iterable[Mapping[str, object]],
    *,
    encoding: str = "utf-8",
) -> None:
    """Write mapping rows with a header; extra mapping keys are ignored."""
    if not fieldnames:
        raise ValueError("fieldnames cannot be empty")
    with Path(path).open("w", encoding=encoding, newline="") as destination:
        writer = csv.DictWriter(destination, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
