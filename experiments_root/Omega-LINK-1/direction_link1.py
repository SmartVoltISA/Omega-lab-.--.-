"""Ω-LINK-1 Direction-1: test whether reversing one relation changes reachability."""
from collections import deque

NODES = ("A", "B", "C", "D")
CASES = {
    "DIRECT": {
        "forward": (("A", "B"),),
        "reverse": (("B", "A"),),
    },
    "CHAIN": {
        "forward": (("A", "B"), ("B", "C")),
        "reverse_one": (("B", "A"), ("B", "C")),
    },
    "BRANCH": {
        "forward": (("A", "B"), ("A", "C")),
        "reverse_one": (("B", "A"), ("A", "C")),
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
        base_key = "forward"
        variant_key = "reverse" if "reverse" in case else "reverse_one"
        before = pairs(case[base_key])
        after = pairs(case[variant_key])
        lost = before - after
        gained = after - before
        print(name, {
            "before_pairs": len(before),
            "after_pairs": len(after),
            "lost_pairs": len(lost),
            "gained_pairs": len(gained),
            "lost": sorted(lost),
            "gained": sorted(gained),
        })
