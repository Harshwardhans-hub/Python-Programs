"""Tests for read-only text file helpers."""

import tempfile
import unittest
from pathlib import Path

from programs.file_utils import count_lines, find_in_file


class FileUtilsTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path = Path(self.temp_dir.name) / "sample.txt"
        self.path.write_text("Alpha\n\nBeta beta\nGamma\n", encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_count_lines_including_and_excluding_blank_lines(self):
        self.assertEqual(count_lines(self.path), 4)
        self.assertEqual(count_lines(self.path, include_blank=False), 3)

    def test_find_in_file_is_case_sensitive_by_default(self):
        self.assertEqual(find_in_file(self.path, "Beta"), [(3, "Beta beta")])

    def test_find_in_file_can_ignore_case(self):
        self.assertEqual(find_in_file(self.path, "beta", case_sensitive=False), [(3, "Beta beta")])

    def test_find_in_file_rejects_empty_phrase(self):
        with self.assertRaises(ValueError):
            find_in_file(self.path, "")


if __name__ == "__main__":
    unittest.main()
