# Advanced DSA Exercises

These modules extend the basic DSA examples with common interview patterns:

| Module | Main idea | Complexity notes |
| --- | --- | --- |
| `sliding_window.py` | Fixed windows, unique-character windows, prefix-sum counts | Linear time for the provided scans |
| `two_pointers.py` | Sorted two-sum, adjacent duplicate removal, text palindrome | Linear time; two-sum assumes sorted input |
| `heap_utils.py` | Top-k selection, kth-smallest, merging sorted inputs | Uses Python's heap implementation |
| `union_find.py` | Disjoint sets, path compression, union by rank | Near-constant amortized operations |
| `graph_shortest_paths.py` | Dijkstra shortest distances | Requires non-negative edge weights |

## Validation

Each algorithm has a dedicated test module under `tests/`. Run all examples with:

```bash
python -m unittest discover -s tests -v
```

These implementations are educational references. For production workloads, profile the real data distribution and consider established libraries before replacing a maintained dependency.
