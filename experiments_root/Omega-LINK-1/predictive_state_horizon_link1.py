"""Ω-LINK-1 Predictive State Horizon experiment.

Question: how many future observations are required to distinguish the
histories that a one-step rule initially groups together?

For each controlled rule and history depth N, enumerate all possible histories,
advance the deterministic system, and record the future output sequence over
several horizons. Histories with identical future output sequences belong to
the same predictive class at that horizon.

This is a controlled methodological experiment. It does not claim that the
result is universal or that a particular physical system has this structure.
"""

from itertools import product


RULES = {
    "PARITY_BINARY": (2, lambda h: sum(h) % 2),
    "FIRST_BINARY": (2, lambda h: h[0]),
    "CONSTANT_BINARY": (2, lambda h: 0),
    "SUM_MOD3": (3, lambda h: sum(h) % 3),
}


def step(history, rule):
    return history[1:] + (rule(history),)


def future_signature(history, rule, horizon):
    cur = history
    out = []
    for _ in range(horizon):
        cur = step(cur, rule)
        out.append(cur[-1])
    return tuple(out)


def history_states(alphabet, depth):
    return list(product(range(alphabet), repeat=depth))


def class_count(histories, rule, horizon):
    signatures = [future_signature(h, rule, horizon) for h in histories]
    return len(set(signatures))


if __name__ == "__main__":
    print("predictive-state-horizon experiment")
    print("depth | horizon | histories | predictive_classes")
    print("------|---------|-----------|-------------------")

    for name, (alphabet, rule) in RULES.items():
        print(f"RULE {name}")
        for depth in range(1, 7):
            histories = history_states(alphabet, depth)
            horizons = range(1, min(7, depth + 2))
            row = []
            for horizon in horizons:
                row.append((horizon, class_count(histories, rule, horizon)))
            print({
                "depth": depth,
                "histories": len(histories),
                "classes_by_horizon": row,
                "full_history_classes": len(set(histories)),
            })
