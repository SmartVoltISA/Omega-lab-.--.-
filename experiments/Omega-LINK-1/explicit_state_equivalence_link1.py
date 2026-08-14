"""Ω-LINK-1 control: hidden memory vs explicit augmented state.

The same finite-memory process is represented in two ways:
1) as a visible current output with hidden history;
2) as an explicitly augmented state containing the memory window.

We compare future signatures and the minimal distinguishing horizon under
both representations. The purpose is to test whether delayed distinguish-
ability is a property of hidden observability rather than a new transition
mechanism.
"""
from itertools import product

BITS = (0, 1)
DEPTHS = (1, 2, 3)
MAX_H = 5


def rule_for_depth(depth):
    # deterministic shift-register rule: next bit is the oldest bit flipped
    # only for one selected configuration. This gives a concrete delayed case.
    width = 2 ** depth
    table = {bits: bits[-1] for bits in product(BITS, repeat=depth)}
    key = tuple([0] * depth)
    table[key] = 1
    return table


def step(table, hist):
    nxt = table[tuple(hist)]
    return tuple(hist[1:]) + (nxt,)


def output_future(table, hist, horizon):
    h = tuple(hist)
    out = []
    for _ in range(horizon):
        h = step(table, h)
        out.append(h[-1])
    return tuple(out)


def explicit_future(table, hist, horizon):
    h = tuple(hist)
    states = []
    for _ in range(horizon):
        h = step(table, h)
        states.append(h)
    return tuple(states)


def first_diff(signatures_a, signatures_b):
    for i, (a, b) in enumerate(zip(signatures_a, signatures_b), start=1):
        if a != b:
            return i
    return None


if __name__ == "__main__":
    print("EXPLICIT_STATE_EQUIVALENCE")
    for depth in DEPTHS:
        table = rule_for_depth(depth)
        histories = list(product(BITS, repeat=depth))
        print("DEPTH", depth)
        # choose pairs that share the immediately visible output but differ in
        # older history; search for the first output divergence.
        checked = 0
        for i, a in enumerate(histories):
            for b in histories[i + 1:]:
                if a[-1] != b[-1]:
                    continue
                checked += 1
                out_a = output_future(table, a, MAX_H)
                out_b = output_future(table, b, MAX_H)
                state_a = explicit_future(table, a, MAX_H)
                state_b = explicit_future(table, b, MAX_H)
                h_hidden = first_diff(out_a, out_b)
                h_explicit = first_diff(state_a, state_b)
                if h_hidden is not None:
                    print("PAIR", a, b)
                    print("hidden_output", out_a, out_b)
                    print("explicit_state_first_diff", h_explicit)
                    print("hidden_output_first_diff", h_hidden)
                    print("states_a", state_a)
                    print("states_b", state_b)
                    break
            else:
                continue
            break
        print("same_visible_output_pairs_checked", checked)
