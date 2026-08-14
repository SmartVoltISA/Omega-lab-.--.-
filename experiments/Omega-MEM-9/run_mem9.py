"""Ω-MEM-9 pilot executor.

Constructs distinct histories that converge to the same observable state S2.
Memory stores only a path trace (previous internal state), never the next label.
"""
from collections import Counter, defaultdict
import math, random

SEEDS = range(30)
N = 80000


def entropy(counts):
    n = sum(counts.values())
    if n == 0: return 0.0
    return -sum((v/n) * math.log2(v/n) for v in counts.values() if v)


def run(seed):
    rng = random.Random(seed)
    rows = []
    # Two histories converge at S2. Their hidden path trace determines the
    # branch distribution; the observable state remains exactly S2.
    for history in (0, 1):
        for _ in range(N // 2):
            # path trace is history only; it is not a future label.
            memory = history
            current = "S2"
            # Dynamics maps path trace + current state to a transition.
            # This is intentionally the minimal convergent construction.
            nxt = "X" if (memory == 0) else "Y"
            rows.append((current, memory, nxt, history))
    rng.shuffle(rows)
    return rows


def summarize(rows):
    by_current = defaultdict(Counter)
    by_mem = defaultdict(Counter)
    by_hist = defaultdict(Counter)
    for current, memory, nxt, hist in rows:
        by_current[current][nxt] += 1
        by_mem[(current, memory)][nxt] += 1
        by_hist[(current, hist)][nxt] += 1
    return {
        "H_next_given_current": entropy(by_current["S2"]),
        "H_next_given_current_memory": sum(
            entropy(c) for c in by_mem.values()
        ) / len(by_mem),
        "history_distributions": {
            str(k): dict(v) for k, v in by_hist.items()
        },
    }


if __name__ == "__main__":
    all_results = [summarize(run(seed)) for seed in SEEDS]
    print(all_results[0])
