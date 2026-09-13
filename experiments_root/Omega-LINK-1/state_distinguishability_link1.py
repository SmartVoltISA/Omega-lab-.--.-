"""Ω-LINK-1 State Distinguishability — controlled matrix.

Question: how many distinct observable histories remain distinguishable at a
fixed history depth, and when do two histories become equivalent with respect
to their next transition?

This is a controlled structural experiment, not a claim about arbitrary real
systems.
"""
from itertools import product
from collections import defaultdict

ALPHABET = ("A", "C")


def next_state(history):
    # Controlled rule: parity of C's in the complete history.
    return ALPHABET[sum(x == "C" for x in history) % 2]


def experiment(depth):
    histories = list(product(ALPHABET, repeat=depth))
    classes = defaultdict(list)
    for h in histories:
        classes[next_state(h)].append(h)

    total = len(histories)
    distinct_next = len(classes)
    class_sizes = sorted(len(v) for v in classes.values())
    return total, distinct_next, class_sizes


if __name__ == "__main__":
    print("state-distinguishability experiment")
    print("depth,total_histories,distinct_next_states,class_sizes")
    for depth in range(1, 7):
        total, distinct_next, class_sizes = experiment(depth)
        print(depth, total, distinct_next, class_sizes)
