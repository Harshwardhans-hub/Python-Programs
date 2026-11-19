# All-pairs shortest paths

Use `floyd_warshall` when distances are needed between every pair of vertices in a relatively small weighted graph.

## Contract

- Directed weighted edges are supplied as `(neighbor, weight)` pairs.
- Negative edge weights are supported.
- A negative cycle anywhere in the graph raises `ValueError`.
- Nodes mentioned only as neighbors are included.
- Unreachable pairs are represented by `math.inf`.
- Time complexity is O(V³); space complexity is O(V²).

## Choosing an algorithm

- Use BFS for unweighted shortest paths from one source.
- Use Dijkstra for one source when all edge weights are non-negative.
- Use Bellman–Ford for one source when negative edges may be present.
- Use Floyd–Warshall when all-pairs distances are needed and the graph size makes cubic time and quadratic memory reasonable.

Run focused tests:

```bash
python -m unittest tests.test_floyd_warshall -v
```
