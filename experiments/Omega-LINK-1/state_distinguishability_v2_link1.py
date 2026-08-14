"""Ω-LINK-1 State Distinguishability V2 — rule cross-check.

Question: is the observed state-class matrix specific to one transition rule,
or does it persist across qualitatively different controlled rules?

This is a controlled structural experiment, not a claim about arbitrary real systems.
"""
from itertools import product
from collections import defaultdict


def experiment(alphabet, depth, rule):
    histories = list(product(alphabet, repeat=depth))
    classes = defaultdict(list)
    for h in histories:
        classes[rule(h, alphabet)].append(h)
    return len(histories), len(classes), sorted(len(v) for v in classes.values())


def parity_binary(h, alphabet):
    return alphabet[sum(x == alphabet[1] for x in h) % 2]


def first_symbol(h, alphabet):
    return h[0]


def constant_binary(h, alphabet):
    return alphabet[0]


def sum_mod3(h, alphabet):
    return alphabet[sum(alphabet.index(x) for x in h) % 3]


if __name__ == "__main__":
    print("state-distinguishability V2 rule cross-check")
    print("rule,depth,total_histories,distinct_next_states,class_sizes")
    rules = [
        ("PARITY_BINARY", ("A", "C"), parity_binary),
        ("FIRST_BINARY", ("A", "C"), first_symbol),
        ("CONSTANT_BINARY", ("A", "C"), constant_binary),
        ("SUM_MOD3", ("A", "B", "C"), sum_mod3),
    ]
    for name, alphabet, rule in rules:
        for depth in range(1, 7):
            total, distinct, sizes = experiment(alphabet, depth, rule)
            print(name, depth, total, distinct, sizes)
