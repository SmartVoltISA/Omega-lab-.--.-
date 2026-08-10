"""Ω-MEM-G-1: controlled graph geometry / capacity decomposition.

Protocol: ../protocol.json
Status at registration: NOT RUN

The program constructs finite relation graphs, measures structural quantities,
and records projection-invariant quantities separately from display geometry.
It does not infer physical meaning from any geometric representation.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "raw_results"
RAW_DIR.mkdir(parents=True, exist_ok=True)

SEEDS = 30
STATE_COUNTS = [4, 8, 16, 32, 64]
EDGE_REGIMES = {
    "sparse": 1,
    "medium": 2,
    "dense": 4,
}


def ring_edges(n: int) -> List[Tuple[int, int]]:
    return [(i, (i + 1) % n) for i in range(n)]


def path_edges(n: int) -> List[Tuple[int, int]]:
    return [(i, i + 1) for i in range(n - 1)]


def random_edges(n: int, multiplier: int, seed: int) -> List[Tuple[int, int]]:
    rng = np.random.default_rng(seed)
    max_edges = n * (n - 1) // 2
    target = min(max_edges, max(n - 1, multiplier * n))
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    idx = rng.choice(len(pairs), size=target, replace=False)
    return [pairs[i] for i in idx]


def adjacency(n: int, edges: List[Tuple[int, int]]) -> np.ndarray:
    a = np.zeros((n, n), dtype=np.int8)
    for i, j in edges:
        a[i, j] = 1
        a[j, i] = 1
    return a


def graph_metrics(n: int, edges: List[Tuple[int, int]]) -> Dict[str, float]:
    a = adjacency(n, edges)
    degrees = a.sum(axis=1)
    e = len(edges)
    e_max = n * (n - 1) // 2

    # Boundary is intentionally defined here as the number of edges crossing
    # a fixed bipartition. The partition is part of the protocol, not inferred
    # from the result.
    left = set(range(n // 2))
    boundary = sum((i in left) != (j in left) for i, j in edges)

    return {
        "N_states": int(n),
        "N_edges": int(e),
        "density": float(e / e_max) if e_max else 0.0,
        "N_boundary": int(boundary),
        "connected_components": int(count_components(a)),
        "mean_degree": float(np.mean(degrees)),
        "degree_std": float(np.std(degrees)),
    }


def count_components(a: np.ndarray) -> int:
    n = len(a)
    seen = np.zeros(n, dtype=bool)
    count = 0
    for start in range(n):
        if seen[start]:
            continue
        count += 1
        stack = [start]
        seen[start] = True
        while stack:
            u = stack.pop()
            for v in np.flatnonzero(a[u]):
                if not seen[v]:
                    seen[v] = True
                    stack.append(int(v))
    return count


def projection_invariants(n: int, edges: List[Tuple[int, int]]) -> Dict[str, float]:
    a = adjacency(n, edges)
    degrees = a.sum(axis=1)
    # These are graph properties and therefore independent of drawing layout.
    return {
        "state_count": int(n),
        "edge_count": int(len(edges)),
        "degree_sum": int(degrees.sum()),
        "degree_mean": float(np.mean(degrees)),
        "component_count": int(count_components(a)),
    }


def run() -> None:
    records = []
    for n in STATE_COUNTS:
        for graph_type in ["ring", "path"]:
            edges = ring_edges(n) if graph_type == "ring" else path_edges(n)
            records.append({
                "seed": None,
                "graph_type": graph_type,
                "N": n,
                "metrics": graph_metrics(n, edges),
                "invariants": projection_invariants(n, edges),
            })

        for regime, multiplier in EDGE_REGIMES.items():
            for seed in range(SEEDS):
                edges = random_edges(n, multiplier, seed)
                records.append({
                    "seed": seed,
                    "graph_type": "random",
                    "edge_regime": regime,
                    "N": n,
                    "metrics": graph_metrics(n, edges),
                    "invariants": projection_invariants(n, edges),
                })

    output = {
        "experiment": "EXP-Ω-MEM-G-1",
        "status": "EXECUTED_BY_USER_ONLY_AFTER_PROTOCOL_FREEZE",
        "records": records,
    }
    path = RAW_DIR / "omega_mem_g1_raw.json"
    path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved raw results to {path}")


if __name__ == "__main__":
    run()
