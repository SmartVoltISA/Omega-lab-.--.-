"""Ω-MEM-9 — indirect graph dynamics.

History does not map directly to X/Y. It changes a generic internal edge
weight through an update rule. The next transition is sampled from the
current graph using normalized edge weights. No future-state labels are
stored in memory.
"""
from collections import Counter, defaultdict
import math, random

SEEDS = range(30)
TRIALS = 20000
ALPHA = 0.35

BASE = {"X": 1.0, "Y": 1.0}


def entropy(c):
    n = sum(c.values())
    return 0.0 if n == 0 else -sum((v/n)*math.log2(v/n) for v in c.values() if v)


def softmax_weights(weights):
    total = sum(weights.values())
    return {k: v/total for k,v in weights.items()}


def update_memory(trace, incoming_edge):
    # Generic path-trace update. The memory stores a bounded trace statistic,
    # not the identity of the next transition.
    return 0.75 * trace + (1.0 if incoming_edge == "A_to_S" else -1.0)


def run(seed, history):
    rng = random.Random(seed)
    rows = []
    # A and B converge to the same observable S. Their only difference is
    # which incoming edge was traversed immediately before convergence.
    incoming = "A_to_S" if history == 0 else "B_to_S"
    trace = update_memory(0.0, incoming)

    # Memory changes a generic edge-bias parameter. It does not select a
    # future label. The graph sampler selects X/Y from the resulting weights.
    for _ in range(TRIALS):
        weights = {
            "X": BASE["X"] * math.exp(ALPHA * trace),
            "Y": BASE["Y"] * math.exp(-ALPHA * trace),
        }
        probs = softmax_weights(weights)
        nxt = "X" if rng.random() < probs["X"] else "Y"
        rows.append(("S", trace, nxt, history, probs["X"]))
        # Memory decays after each transition; future labels do not update it.
        trace *= 0.98
    return rows


def summarize(rows):
    cur = Counter(); mem = defaultdict(Counter); hist = defaultdict(Counter)
    for s,m,n,h,p in rows:
        cur[n] += 1; mem[round(m, 3)][n] += 1; hist[h][n] += 1
    return {
        "H_next_given_current": entropy(cur),
        "history_distributions": {str(k): dict(v) for k,v in hist.items()},
        "memory_bins": {str(k): dict(v) for k,v in mem.items()},
    }

if __name__ == "__main__":
    rows = run(0, 0) + run(0, 1)
    print(summarize(rows))
