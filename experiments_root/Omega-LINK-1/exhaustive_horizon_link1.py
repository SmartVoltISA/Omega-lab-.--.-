"""Omega-LINK-1 exhaustive minimal-horizon check on small finite systems.

Enumerates deterministic binary transition rules for 2-state systems and
compares all distinct histories up to a bounded length. For each pair it
finds the first prediction horizon at which their future signatures differ.
The experiment is intentionally small and exhaustive: it is a control for
whether minimal future horizon is an artifact of hand-built examples.
"""
from itertools import product

STATES = (0, 1)
MAX_HORIZON = 4


def all_rules():
    for outputs in product(STATES, repeat=4):
        yield outputs


def step(rule, state, memory):
    # deterministic rule on current state and one-bit memory
    return rule[state * 2 + memory]


def future(rule, state, memory, horizon):
    out = []
    s, m = state, memory
    for _ in range(horizon):
        n = step(rule, s, m)
        out.append(n)
        m, s = s, n
    return tuple(out)


if __name__ == "__main__":
    print("exhaustive minimal-horizon experiment")
    total_rules = 0
    pair_checks = 0
    first_horizon_counts = {h: 0 for h in range(1, MAX_HORIZON + 1)}
    no_divergence = 0

    for rule in all_rules():
        total_rules += 1
        histories = [(s, m) for s in STATES for m in STATES]
        for i in range(len(histories)):
            for j in range(i + 1, len(histories)):
                pair_checks += 1
                h1, h2 = histories[i], histories[j]
                first = None
                for horizon in range(1, MAX_HORIZON + 1):
                    if future(rule, *h1, horizon) != future(rule, *h2, horizon):
                        first = horizon
                        break
                if first is None:
                    no_divergence += 1
                else:
                    first_horizon_counts[first] += 1

    print("total_rules", total_rules)
    print("pair_checks", pair_checks)
    print("first_horizon_counts", first_horizon_counts)
    print("no_divergence", no_divergence)
    print("bounded_exhaustive_check", True)
