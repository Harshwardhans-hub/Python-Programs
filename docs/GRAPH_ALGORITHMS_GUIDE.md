# Graph algorithm guide

This repository includes several graph approaches. Choose based on the graph's structure and edge weights rather than treating the algorithms as interchangeable.

| Problem | Algorithm | Edge-weight assumptions | Typical complexity |
|---|---|---|---|
| Visit reachable vertices | BFS / DFS | Unweighted | O(V + E) |
| Shortest paths from one source | Dijkstra | Non-negative weights | O((V + E) log V) with a binary heap |
| Shortest paths with negative edges | Bellman–Ford | Negative weights allowed; reachable negative cycles rejected | O(VE) |
| Dependency ordering | Kahn topological sort | Directed acyclic graph | O(V + E) |\n| Detect directed / undirected cycles | DFS colors / disjoint set | Directed or undirected edge list | O(V + E) |\n| Check two-colorability | BFS coloring | Undirected graph | O(V + E) |\n| All-pairs shortest paths | Floyd–Warshall | Weighted graph; negative edges allowed without negative cycles | O(V³) |
| Minimum spanning forest | Kruskal + disjoint set | Undirected weighted graph | O(E log E) |

## Examples

Run code from the repository root:

```python
from programs.topological_sort import topological_sort

order = topological_sort({
    "compile": ["package"],
    "lint": ["package"],
    "package": [],
})
print(order)
```

```python
from programs.bellman_ford import bellman_ford

distances = bellman_ford({
    "start": [("middle", 4), ("direct", 10)],
    "middle": [("direct", -3)],
    "direct": [],
}, "start")
print(distances)
```

## Important distinctions

- Dijkstra is not valid for negative edge weights.
- Bellman–Ford detects only negative cycles reachable from the chosen source.
- A topological order exists only for directed acyclic graphs.
- Kruskal's helper returns a minimum spanning forest when the supplied graph is disconnected.
