# DSA Module Reference

This reference complements the topic overviews in the repository's DSA guides.

| Topic | Module | Public examples |
| --- | --- | --- |
| Binary trees | `tree_utils.py` | Preorder, inorder, postorder, level order, height |
| Prefix trees | `trie.py` | Insert, search, prefix lookup, words by prefix |
| Classic sorting | `sorting_algorithms.py` | Bubble, insertion, selection, quick sort |
| Sorted searching | `search_algorithms.py` | Jump search, exponential search |
| Greedy methods | `greedy_algorithms.py` | Activity selection, fractional knapsack |
| Bit operations | `bitwise_utils.py` | Set-bit count, power of two, single-number XOR |
| Grids | `grid_algorithms.py` | Flood fill, island count |
| Combinatorics | `combinatorics_utils.py` | Pascal triangle, binomial coefficient, combinations |
| Hash maps | `hashing_utils.py` | Two-sum lookup, anagram grouping |

Run the complete suite from the repository root:

```bash
python -m unittest discover -s tests -v
```

The implementations are standalone learning examples. Their docstrings and tests define assumptions such as sorted input, non-negative weights, and valid grid shapes.
