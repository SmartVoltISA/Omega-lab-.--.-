"""Ω-LINK-1 Addition-1: test whether adding one edge creates new global reachability."""
from collections import deque

NODES = ("A", "B", "C", "D")
CASES = {
    "REDUNDANT": {
        "base": (("A", "B"), ("B", "C"), ("A", "C")),
        "add": ("A", "C"),
    },
    "NEW": {
        "base": (("A", "B"), ("B", "C")),
        "add": ("A", "D"),
    },
    "ALTERNATIVE": {
        "base": (("A", "B"), ("B", "D")),
        "add": ("A", "D"),
    },
    "PARTIAL": {
        "base": (("A", "B"), ("B", "C"), ("C", "D")),
        "add": ("A", "C"),
    },
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


def pairs(edges):
    return {(s, t) for s in NODES for t in reachable(edges, s) if t != s}


if __name__ == "__main__":
    for name, case in CASES.items():
        base = case["base"]
        edge = case["add"]
        before = pairs(base)
        after = pairs(base + (edge,))
        gained = after - before
        local_gain = 1
        print(name, {
            "edge_added": edge,
            "local_gain": local_gain,
            "global_gain": len(gained),
            "gained_pairs": sorted(gained),
        })
