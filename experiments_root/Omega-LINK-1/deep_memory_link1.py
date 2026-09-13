"""Ω-LINK-1 Deep Memory experiment.

Question: can we construct a process where one previous state is NOT enough
to predict the next state, but two previous states are enough?

This is a controlled construction designed to test whether minimal sufficient
history depth can be greater than one. It is not a universal claim.
"""

# Same final current state B, but the next state depends on the state two
# positions back. The immediately previous state is deliberately identical.
SEQUENCES = [
    ("A", "C", "B", "A"),
    ("C", "C", "B", "C"),
]


def next_state(seq):
    return seq[-1]


def rep_current(seq):
    return seq[-2]


def rep_last2(seq):
    return (seq[-3], seq[-2])


def rep_last3(seq):
    return tuple(seq[-4:-1])


def conditional_entropy(rows):
    from collections import defaultdict, Counter
    import math
    groups = defaultdict(Counter)
    for state, nxt in rows:
        groups[state][nxt] += 1
    total = len(rows)
    h = 0.0
    for counts in groups.values():
        n = sum(counts.values())
        local = 0.0
        for c in counts.values():
            p = c / n
            local -= p * math.log2(p)
        h += (n / total) * local
    return h


if __name__ == "__main__":
    rows_current = [(rep_current(s), next_state(s)) for s in SEQUENCES]
    rows_last2 = [(rep_last2(s), next_state(s)) for s in SEQUENCES]
    rows_last3 = [(rep_last3(s), next_state(s)) for s in SEQUENCES]

    print("deep-memory experiment")
    print("H(next | current)", conditional_entropy(rows_current))
    print("H(next | last2)", conditional_entropy(rows_last2))
    print("H(next | last3)", conditional_entropy(rows_last3))
    print("current_rows", rows_current)
    print("last2_rows", rows_last2)
    print("last3_rows", rows_last3)
