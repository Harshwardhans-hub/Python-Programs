"""Tests for least-recently-used cache behavior."""

import unittest

from programs.lru_cache import LRUCache


class LRUCacheTests(unittest.TestCase):
    def test_put_get_and_eviction_order(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        self.assertEqual(cache.get("a"), 1)
        cache.put("c", 3)
        self.assertIn("a", cache)
        self.assertNotIn("b", cache)
        self.assertEqual(cache.get("c"), 3)

    def test_updating_existing_key_does_not_grow_cache(self):
        cache = LRUCache(1)
        cache.put("a", 1)
        cache.put("a", 2)
        self.assertEqual(cache.get("a"), 2)
        self.assertEqual(len(cache), 1)

    def test_missing_key_returns_none(self):
        self.assertIsNone(LRUCache(2).get("missing"))

    def test_capacity_validation(self):
        with self.assertRaises(ValueError):
            LRUCache(0)
        with self.assertRaises(TypeError):
            LRUCache(True)


    def test_updating_an_existing_key_refreshes_its_recency(self):
        cache = LRUCache(2)
        cache.put("first", 1)
        cache.put("second", 2)
        cache.put("first", 10)
        cache.put("third", 3)

        self.assertEqual(cache.get("first"), 10)
        self.assertIsNone(cache.get("second"))
        self.assertEqual(cache.get("third"), 3)



if __name__ == "__main__":
    unittest.main()
