# Binary search tree and AVL tree

The practice collection contains both ordinary binary search tree exercises and an AVL ordered set.

## Difference

An ordinary binary search tree can become a chain when values arrive in sorted order. In that shape, search and insertion can degrade toward O(n).

An AVL tree tracks subtree heights and rotates after insertion to keep the height difference of every node within one. Search and insertion therefore remain O(log n) in the worst case.

## AVL implementation contract

- Keys must be mutually comparable.
- Duplicate keys are ignored and do not increase the tree size.
- `search(key)` and `key in tree` test membership.
- `in_order()` returns an ascending list of keys.
- `height` counts nodes on the longest root-to-leaf path; an empty tree has height zero.
- This implementation intentionally covers insertion and lookup; deletion is not included.

## Tests

```bash
python -m unittest tests.test_avl_tree -v
```

The tests exercise all four insertion rotation shapes and insert 1,000 ascending keys to check that the resulting tree remains shallow.
