"""Ω-LINK-1: inspect the mechanism behind H_max = memory_depth + 1.

For binary finite-memory systems with d=1..3, find a concrete deterministic
rule and pair of initial histories whose first future divergence occurs at
the maximum observed horizon d+1. Print the transition table and the two
future signatures so the mechanism can be inspected rather than inferred
from counts alone.
"""
from itertools import product

STATES = (0, 1)


def future(rule, history, horizon):
    current, *memory = history
    out = []
    for _ in range(horizon):
        idx = 0
        for bit in (current, *memory):
            idx = (idx << 1) | bit
        nxt = rule[idx]
        out.append(nxt)
        memory = [current, *memory[:-1]]
        current = nxt
    return tuple(out)


def find_witness(depth):
    width = depth + 1
    histories = list(product(STATES, repeat=width))
    expected = depth + 1
    for rule in product(STATES, repeat=2 ** width):
        signatures = {h: future(rule, h, expected) for h in histories}
        for i, a in enumerate(histories):
            for b in histories[i + 1:]:
                first = None
                for h in range(1, expected + 1):
                    if signatures[a][:h] != signatures[b][:h]:
                        first = h
                        break
                if first == expected:
                    return rule, a, b, signatures[a], signatures[b]
    return None


if __name__ == "__main__":
    print("horizon mechanism witness experiment")
    for depth in (1, 2, 3):
        result = find_witness(depth)
        if result is None:
            print("depth", depth, "NO_WITNESS")
            continue
        rule, a, b, fa, fb = result
        print("depth", depth)
        print("expected_horizon", depth + 1)
        print("rule", rule)
        print("history_A", a)
        print("history_B", b)
        print("future_A", fa)
        print("future_B", fb)
        print("verified", True)
