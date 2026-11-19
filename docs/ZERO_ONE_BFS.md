# 0-1 BFS

Use `zero_one_bfs(graph, start)` when every edge weight is exactly 0 or 1. A deque pushes zero-cost relaxations to the front and unit-cost relaxations to the back, producing shortest distances in O(V + E) time.

Do not use this function for arbitrary positive or negative weights:
- Use ordinary BFS for unweighted graphs.
- Use 0-1 BFS when all weights are 0 or 1.
- Use Dijkstra for non-negative weights of arbitrary magnitude.
- Use Bellman–Ford when negative edges are allowed.

Unreachable vertices are omitted. Invalid edge weights are rejected. Run `python -m unittest tests.test_zero_one_bfs -v` from the repository root.
