"""Ω-LINK-1 Influence-1: quantify reachability change after one-edge removal."""
from collections import deque

NODES = ("A", "B", "C", "D")
GRAPHS = {
    "G1": (("A", "B"), ("B", "C"), ("C", "D"), ("A", "D")),
    "G2": (("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")),
}


def adj(edges):
    g = {n: [] for n in NODES}
    for a, b in edges:
        g[a].append(b)
    return g


def reachable(edges, start):
    g = adj(edges)
    seen = {start}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in g[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)
    return seen


def metrics(edges):
    pairs = {(s, t) for s in NODES for t in reachable(edges, s) if t != s}
    return pairs


def score(edges, edge):
    base = metrics(edges)
    reduced = metrics(tuple(e for e in edges if e != edge))
    lost_pairs = base - reduced
    changed_sources = {s for s, _ in lost_pairs}
    next_before = len(adj(edges)[edge[0]])
    next_after = len(adj(tuple(e for e in edges if e != edge))[edge[0]])
    return {
        "influence_pairs": len(lost_pairs),
        "changed_sources": len(changed_sources),
        "next_choice_loss": next_before - next_after,
        "lost_pairs": sorted(lost_pairs),
    }


if __name__ == "__main__":
    for name, edges in GRAPHS.items():
        print(name)
        for edge in edges:
            print(edge, score(edges, edge))
