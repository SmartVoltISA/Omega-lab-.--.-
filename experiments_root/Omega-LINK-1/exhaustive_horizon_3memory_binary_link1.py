"""Ω-LINK-1: exhaustive minimal-horizon control with three-step memory.

Binary states, transition rule sees (x_t, x_{t-1}, x_{t-2}, x_{t-3}).
There are 2^16 deterministic rules. All 16 initial 4-tuples are compared.
The experiment tests whether the maximum minimal future-divergence horizon
continues the observed memory_depth + 1 pattern.
"""
from itertools import product

STATES = (0, 1)
MAX_HORIZON = 7


def future(rule, history, horizon):
    current, m1, m2, m3 = history
    out = []
    for _ in range(horizon):
        idx = (current << 3) | (m1 << 2) | (m2 << 1) | m3
        nxt = rule[idx]
        out.append(nxt)
        m3, m2, m1, current = m2, m1, current, nxt
    return tuple(out)


if __name__ == "__main__":
    histories = list(product(STATES, repeat=4))
    total_rules = 0
    pair_checks = 0
    first_horizon_counts = {h: 0 for h in range(1, MAX_HORIZON + 1)}
    no_divergence = 0
    max_observed = 0

    for rule in product(STATES, repeat=16):
        total_rules += 1
        signatures = [future(rule, h, MAX_HORIZON) for h in histories]
        for i in range(len(histories)):
            for j in range(i + 1, len(histories)):
                pair_checks += 1
                first = None
                a, b = signatures[i], signatures[j]
                for horizon in range(1, MAX_HORIZON + 1):
                    if a[:horizon] != b[:horizon]:
                        first = horizon
                        break
                if first is None:
                    no_divergence += 1
                else:
                    first_horizon_counts[first] += 1
                    if first > max_observed:
                        max_observed = first

    print("exhaustive 3-memory binary minimal-horizon experiment")
    print("total_rules", total_rules)
    print("pair_checks", pair_checks)
    print("first_horizon_counts", first_horizon_counts)
    print("no_divergence", no_divergence)
    print("max_observed_minimal_horizon", max_observed)
    print("bounded_exhaustive_check", True)
