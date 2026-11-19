# Data Structures and Algorithms Exercises

The reusable modules in `programs/` are organized by topic. All helpers are dependency-free and have corresponding unit tests.

| Topic | Module | Examples |
| --- | --- | --- |
| Searching and sorting | `algorithms.py` | Linear search, binary search, merge sort |
| Collections | `collection_utils.py` | Chunking, stable uniqueness, rotation, flattening |
| Stack and queue | `data_structures.py` | LIFO and FIFO operations |
| Linked list | `linked_list.py` | Append, prepend, indexed insert, search, removal |
| Graphs | `graph_algorithms.py` | BFS, DFS, reachability |
| Strings | `string_algorithms.py` | Anagrams, unique characters, prefixes, run-length encoding |
| Intervals | `interval_utils.py` | Merge and insert intervals |
| Matrices | `matrix_utils.py` | Transpose, addition, multiplication, rotation |
| Number theory | `number_theory.py` | Armstrong, perfect numbers, leap years, digit sums |
| Dynamic programming | `dynamic_programming.py` | Coin change, LIS, 0/1 knapsack |
| Recursion | `recursion_utils.py` | Factorial, power, nested sums |
| Backtracking | `backtracking.py` | Subsets, permutations, N-Queens |
| Statistics | `statistics_utils.py` | Mean, median, variance, standard deviation |

## Run the tests

From the repository root:

```bash
python -m unittest discover -s tests -v
```

Examples document the expected input contracts and avoid changing the behavior of the original standalone practice scripts.
