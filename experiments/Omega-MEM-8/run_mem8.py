import math
import collections
import numpy as np


def entropy(xs):
    c = collections.Counter(xs)
    n = len(xs)
    return -sum((v/n) * math.log2(v/n) for v in c.values())


def conditional_entropy(xs, ys):
    groups = collections.defaultdict(list)
    for x, y in zip(xs, ys):
        groups[x].append(y)
    n = len(xs)
    return sum(len(g)/n * entropy(g) for g in groups.values())


def run(seed=0, blocks=5000):
    rng = np.random.default_rng(seed)

    # Two paths converge on the same observable state S.
    # A -> S -> B -> S
    # X -> S -> Y -> S
    # At S, the next transition is generated from the path-derived
    # memory (A/X), not from a stored next-transition label.
    seq = []
    for _ in range(blocks):
        if rng.integers(2) == 0:
            seq.extend(["A", "S", "B", "S"])
        else:
            seq.extend(["X", "S", "Y", "S"])

    idx = [i for i in range(1, len(seq)-1) if seq[i] == "S"]
    current = [seq[i] for i in idx]
    nxt = [seq[i+1] for i in idx]
    path_memory = [seq[i-1] for i in idx]

    irrelevant = path_memory.copy()
    rng.shuffle(irrelevant)

    h_current = entropy(nxt)
    h_path = conditional_entropy(path_memory, nxt)
    h_irrel = conditional_entropy(irrelevant, nxt)

    return {
        "H_next_given_current": h_current,
        "H_next_given_current_path_memory": h_path,
        "I_next_memory_given_current": h_current - h_path,
        "H_next_given_current_irrelevant_memory": h_irrel,
        "I_next_irrelevant_memory_given_current": h_current - h_irrel,
        "n": len(nxt),
    }


if __name__ == "__main__":
    rows = [run(seed) for seed in range(30)]
    for key in rows[0]:
        vals = [r[key] for r in rows]
        print(key, np.mean(vals), np.std(vals))
