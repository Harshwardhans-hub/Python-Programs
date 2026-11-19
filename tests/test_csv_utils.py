"""Tests for CSV helper behavior."""

import tempfile
import unittest
from pathlib import Path

from programs.csv_utils import read_csv_rows, write_csv_rows


class CsvUtilsTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path = Path(self.temp_dir.name) / "records.csv"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_round_trip_preserves_commas_and_newlines(self):
        rows = [
            {"name": "Sharma, Harshwardhan", "note": "line one\nline two"},
            {"name": "Asha", "note": "Python"},
        ]
        write_csv_rows(self.path, ["name", "note"], rows)

        self.assertEqual(read_csv_rows(self.path), rows)

    def test_writer_ignores_extra_keys(self):
        write_csv_rows(self.path, ["name"], [{"name": "Asha", "private": "ignored"}])
        self.assertEqual(read_csv_rows(self.path), [{"name": "Asha"}])

    def test_writer_requires_headers(self):
        with self.assertRaises(ValueError):
            write_csv_rows(self.path, [], [])


if __name__ == "__main__":
    unittest.main()
