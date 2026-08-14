"""Ω-MEM-7 execution: controlled branching with fixed memory capacity.

Design: current observable state is constant. A latent memory state determines
which of B possible next transitions occurs. Memory capacity is fixed at 8
slots for every B in {1,2,4,8}. Relevant memory stores the latent next-transition
class; irrelevant memory is an independent random 8-state variable.

The branching generator is intentionally non-uniform for B>1 so that resetting
memory to a uniform B-state distribution changes the marginal transition
statistics while preserving the current observable state.
"""
from collections import Counter, defaultdict
from math import log2
import random

N = 80_000
SEEDS = range(30)
BRANCHING = (1, 2, 4, 8)
MEM_CAPACITY = 8


def entropy(xs):
    c = Counter(xs); n = len(xs)
    return -sum((v/n) * log2(v/n) for v in c.values()) if n else 0.0


def conditional_entropy(keys, ys):
    groups = defaultdict(list)
    for k, y in zip(keys, ys): groups[k].append(y)
    n = len(ys)
    out = 0.0
    for g in groups.values():
        out += len(g)/n * entropy(g)
    return out


def generator(B):
    weights = [1] if B == 1 else [7] + [1] * (B - 1)
    cycle = []
    for symbol, weight in enumerate(weights):
        cycle.extend([symbol] * weight)
    seq = (cycle * (N // len(cycle) + 1))[:N]
    return [0] * N, seq


def run(B, seed):
    rng = random.Random(seed)
    current, nxt = generator(B)
    relevant_memory = list(nxt)  # causal latent state needed for next transition
    irrelevant_memory = [rng.randrange(MEM_CAPACITY) for _ in nxt]

    h_current = conditional_entropy(current, nxt)
    h_relevant = conditional_entropy(list(zip(current, relevant_memory)), nxt)
    h_random = conditional_entropy(list(zip(current, irrelevant_memory)), nxt)
    mi = h_current - h_relevant

    empirical_branching = len(set(nxt))

    # Intervention: hold current observable state fixed, replace memory by
    # an independent uniform B-state memory.
    reset_memory = [rng.randrange(B) for _ in nxt]
    p = Counter(nxt); q = Counter(reset_memory)
    n = len(nxt)
    tv = 0.5 * sum(abs(p[k]/n - q[k]/n) for k in set(p) | set(q))
    changed = sum(a != b for a, b in zip(nxt, reset_memory)) / n

    return {
        "B": B, "seed": seed, "H_current": h_current,
        "H_relevant": h_relevant, "H_random": h_random,
        "MI_next_memory_given_current": mi,
        "empirical_branching": empirical_branching,
        "TV_reset": tv, "fraction_changed_after_reset": changed,
    }


if __name__ == "__main__":
    for B in BRANCHING:
        for seed in SEEDS:
            print(run(B, seed))
