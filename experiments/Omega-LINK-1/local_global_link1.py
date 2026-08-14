"""Ω-LINK-1 Local-vs-Global Influence control experiment."""
from collections import deque

NODES = ("A", "B", "C", "D")

GRAPHS = {
    "NO_ALTERNATIVE": (
        ("A", "B"), ("B", "C"), ("C", "D"),
    ),
    "PARTIAL_ALTERNATIVE": (
        ("A", "B"), ("A", "C"), ("B", "C"), ("C", "D"),
    ),
    "SINGLE_ALTERNATIVE": (
        ("A", "B"), ("A", "C"), ("C", "B"), ("B", "D"),
    ),
    "MULTIPLE_ALTERNATIVES": (
        ("A", "B"), ("A", "C"), ("B", "C"),
        ("B", "D"), ("C", "D"),
    ),
}


def adjacency(edges):
    g = {n: [] for n in NODES}
    for a, b in edges:
        g[a].append(b)
    return g


def reachable(edges, start):
    g = adjacency(edges)
    seen = {start}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in g[u]:
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return seen


def reachable_pairs(edges):
    return {(s, t) for s in NODES for t in reachable(edges, s) if s != t}


def measure(edges, edge):
    base = reachable_pairs(edges)
    reduced_edges = tuple(e for e in edges if e != edge)
    reduced = reachable_pairs(reduced_edges)
    lost = base - reduced

    before = len(adjacency(edges)[edge[0]])
    after = len(adjacency(reduced_edges)[edge[0]])

    return {
        "local_loss": before - after,
        "global_loss": len(lost),
        "lost_pairs": sorted(lost),
    }


if __name__ == "__main__":
    for name, edges in GRAPHS.items():
        print(f"GRAPH {name}")
        for edge in edges:
            print(edge, measure(edges, edge))
