"""Ω-LINK-1 Minimal Sufficient State experiment.

Question: what is the smallest state representation that makes the next
transition deterministic in the tested history-dependent construction?

Candidate representations are compared by conditional entropy of the next
state. This is a controlled construction, not a universal claim.
"""

# Observed histories from RESULT-007.
SEQUENCES = [
    ("A", "B", "A"),
    ("C", "B", "C"),
]


def next_state(seq):
    return seq[-1]

# Representations of the current situation.
def rep_current(seq):
    return seq[-2]


def rep_last2(seq):
    return (seq[-3], seq[-2])


def rep_last3(seq):
    return tuple(seq[-3:])


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

    print("minimal-state experiment")
    print("H(next | current)", conditional_entropy(rows_current))
    print("H(next | last2)", conditional_entropy(rows_last2))
    print("H(next | last3)", conditional_entropy(rows_last3))
    print("current_rows", rows_current)
    print("last2_rows", rows_last2)
    print("last3_rows", rows_last3)
