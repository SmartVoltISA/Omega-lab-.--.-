"""Ω-LINK-1 — matrix/reachability executor.

Fixed node set and equal edge count; only connectivity topology changes.
Primary measurements are graph-theoretic and deterministic.
"""
from collections import deque

NODES = ("A", "B", "C", "D")
GRAPHS = {
    "G1": (("A", "B"), ("B", "C"), ("C", "D"), ("A", "D")),
    "G2": (("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")),
}


def adj(edges):
    out = {n: [] for n in NODES}
    for a, b in edges:
        out[a].append(b)
    return out


def reachable(edges, start, max_steps=None):
    g = adj(edges)
    seen = {start}
    q = deque([(start, 0)])
    by_depth = {0: {start}}
    while q:
        u, d = q.popleft()
        if max_steps is not None and d >= max_steps:
            continue
        for v in g[u]:
            if v not in seen:
                seen.add(v)
                by_depth.setdefault(d + 1, set()).add(v)
                q.append((v, d + 1))
    return seen, by_depth


def remove_edge(edges, edge):
    return tuple(e for e in edges if e != edge)


def summarize(name, edges):
    result = {"edges": edges, "nodes": NODES, "reachability": {}, "edge_interventions": {}}
    for s in NODES:
        seen, depth = reachable(edges, s)
        result["reachability"][s] = {
            "reachable": sorted(seen),
            "count": len(seen),
            "by_depth": {str(k): sorted(v) for k, v in depth.items()},
            "next_count": len(adj(edges)[s]),
        }
    for e in edges:
        mod = remove_edge(edges, e)
        changed = {}
        for s in NODES:
            base = reachable(edges, s)[0]
            after = reachable(mod, s)[0]
            if base != after:
                changed[s] = {"before": sorted(base), "after": sorted(after)}
        result["edge_interventions"][str(e)] = {
            "changed_reachability": changed,
            "edge_count_after": len(mod),
        }
    return result


if __name__ == "__main__":
    for name, edges in GRAPHS.items():
        print(name)
        print(summarize(name, edges))
