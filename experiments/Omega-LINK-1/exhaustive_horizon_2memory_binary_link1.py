"""Ω-LINK-1: exhaustive minimal-horizon control with two-step memory.

Binary states, but the transition rule sees (x_t, x_{t-1}, x_{t-2}).
There are 2^8 deterministic rules. All 8 initial triples are compared.
"""
from itertools import product

STATES = (0, 1)
MAX_HORIZON = 6


def all_rules():
    for outputs in product(STATES, repeat=8):
        yield outputs


def step(rule, current, memory1, memory2):
    idx = (current << 2) | (memory1 << 1) | memory2
    return rule[idx]


def future(rule, history, horizon):
    current, memory1, memory2 = history
    out = []
    for _ in range(horizon):
        nxt = step(rule, current, memory1, memory2)
        out.append(nxt)
        memory2, memory1, current = memory1, current, nxt
    return tuple(out)


if __name__ == "__main__":
    histories = list(product(STATES, repeat=3))
    total_rules = 0
    pair_checks = 0
    first_horizon_counts = {h: 0 for h in range(1, MAX_HORIZON + 1)}
    no_divergence = 0
    max_observed = 0

    for rule in all_rules():
        total_rules += 1
        for i in range(len(histories)):
            for j in range(i + 1, len(histories)):
                pair_checks += 1
                first = None
                for horizon in range(1, MAX_HORIZON + 1):
                    if future(rule, histories[i], horizon) != future(rule, histories[j], horizon):
                        first = horizon
                        break
                if first is None:
                    no_divergence += 1
                else:
                    first_horizon_counts[first] += 1
                    max_observed = max(max_observed, first)

    print("exhaustive 2-memory binary minimal-horizon experiment")
    print("total_rules", total_rules)
    print("pair_checks", pair_checks)
    print("first_horizon_counts", first_horizon_counts)
    print("no_divergence", no_divergence)
    print("max_observed_minimal_horizon", max_observed)
    print("bounded_exhaustive_check", True)
