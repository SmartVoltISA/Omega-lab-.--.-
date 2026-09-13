"""Corrected hidden-vs-explicit control for delayed distinguishability.

Select pairs with the same currently visible output and require that their
future visible outputs agree for H=1..d and first diverge at H=d+1.
Then compare the same pair in the full augmented-state representation.
The goal is to separate delayed observability from the underlying state
transition dynamics.
"""
from itertools import product

BITS = (0, 1)
DEPTHS = (1, 2, 3)
MAX_H = 6


def rule_for_depth(depth):
    # Shift-register rule with a delayed marker. It is searched explicitly
    # rather than assuming a witness exists for every depth.
    table = {bits: bits[-1] for bits in product(BITS, repeat=depth)}
    table[tuple([0] * depth)] = 1
    return table


def step(table, hist):
    nxt = table[tuple(hist)]
    return tuple(hist[1:]) + (nxt,)


def outputs(table, hist, horizon):
    h = tuple(hist)
    out = []
    for _ in range(horizon):
        h = step(table, h)
        out.append(h[-1])
    return tuple(out)


def states(table, hist, horizon):
    h = tuple(hist)
    out = []
    for _ in range(horizon):
        h = step(table, h)
        out.append(h)
    return tuple(out)


def first_diff(a, b):
    for i, (x, y) in enumerate(zip(a, b), start=1):
        if x != y:
            return i
    return None


def find_delayed_pair(table, depth):
    histories = list(product(BITS, repeat=depth))
    target = depth + 1
    for i, a in enumerate(histories):
        for b in histories[i + 1:]:
            if a[-1] != b[-1]:
                continue
            oa = outputs(table, a, target)
            ob = outputs(table, b, target)
            if oa[:depth] == ob[:depth] and oa[depth] != ob[depth]:
                return a, b, oa, ob
    return None


if __name__ == "__main__":
    print("CORRECTED_HIDDEN_EXPLICIT_CONTROL")
    for depth in DEPTHS:
        table = rule_for_depth(depth)
        witness = find_delayed_pair(table, depth)
        print("DEPTH", depth)
        if witness is None:
            print("witness_found", False)
            continue
        a, b, oa, ob = witness
        sa = states(table, a, depth + 1)
        sb = states(table, b, depth + 1)
        print("witness_found", True)
        print("pair", a, b)
        print("hidden_outputs_a", oa)
        print("hidden_outputs_b", ob)
        print("hidden_first_diff", first_diff(oa, ob))
        print("explicit_states_a", sa)
        print("explicit_states_b", sb)
        print("explicit_first_diff", first_diff(sa, sb))
        print("delayed_hidden_verified", first_diff(oa, ob) == depth + 1)
        print("explicit_state_already_distinct", sa[0] != sb[0])
