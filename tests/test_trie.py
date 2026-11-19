"""Tests for the trie data structure."""

import unittest

from programs.trie import Trie


class TrieTests(unittest.TestCase):
    def test_insert_search_and_prefix_lookup(self):
        trie = Trie()
        for word in ("cat", "car", "care", "dog"):
            trie.insert(word)
        self.assertTrue(trie.search("cat"))
        self.assertFalse(trie.search("ca"))
        self.assertTrue(trie.starts_with("ca"))
        self.assertFalse(trie.starts_with("z"))

    def test_duplicate_insert_does_not_increase_size(self):
        trie = Trie()
        trie.insert("hello")
        trie.insert("hello")
        self.assertEqual(len(trie), 1)

    def test_words_with_prefix_are_sorted(self):
        trie = Trie()
        for word in ("car", "cat", "care", "dog"):
            trie.insert(word)
        self.assertEqual(trie.words_with_prefix("ca"), ["car", "care", "cat"])
        self.assertEqual(trie.words_with_prefix("z"), [])

    def test_empty_word_and_empty_prefix(self):
        trie = Trie()
        trie.insert("")
        trie.insert("a")
        self.assertTrue(trie.search(""))
        self.assertEqual(trie.words_with_prefix(""), ["", "a"])

    def test_non_string_input_is_rejected(self):
        trie = Trie()
        with self.assertRaises(TypeError):
            trie.insert(12)


    def test_word_can_be_prefix_of_another_word(self):
        trie = Trie()
        trie.insert("car")
        trie.insert("carpet")
        self.assertTrue(trie.search("car"))
        self.assertTrue(trie.starts_with("carp"))
        self.assertEqual(trie.words_with_prefix("car"), ["car", "carpet"])

    def test_trie_is_case_sensitive_and_empty_prefix_matches_all(self):
        trie = Trie()
        trie.insert("Apple")
        trie.insert("apple")
        self.assertFalse(trie.search("APPLE"))
        self.assertEqual(trie.words_with_prefix(""), ["Apple", "apple"])



if __name__ == "__main__":
    unittest.main()
