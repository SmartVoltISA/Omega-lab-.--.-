"""Ω-LINK-1: exhaustive minimal-horizon control for a 3-state system.

Enumerates all deterministic rules on (current_state, one-step-memory), with
3 possible values for each component. This is the next state-space-size
control after RESULT-014's exhaustive binary construction.
"""
from itertools import product

STATES = (0, 1, 2)
MAX_HORIZON = 4


def all_rules():
    # 3 x 3 input pairs, each mapped to one of 3 outputs: 3^9 rules.
    for outputs in product(STATES, repeat=9):
        yield outputs


def step(rule, state, memory):
    return rule[state * len(STATES) + memory]


def future(rule, state, memory, horizon):
    out = []
    s, m = state, memory
    for _ in range(horizon):
        n = step(rule, s, m)
        out.append(n)
        m, s = s, n
    return tuple(out)


if __name__ == "__main__":
    total_rules = 0
    pair_checks = 0
    first_horizon_counts = {h: 0 for h in range(1, MAX_HORIZON + 1)}
    no_divergence = 0
    max_observed = 0

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
                    max_observed = max(max_observed, first)

    print("exhaustive 3-state minimal-horizon experiment")
    print("total_rules", total_rules)
    print("pair_checks", pair_checks)
    print("first_horizon_counts", first_horizon_counts)
    print("no_divergence", no_divergence)
    print("max_observed_minimal_horizon", max_observed)
    print("bounded_exhaustive_check", True)
