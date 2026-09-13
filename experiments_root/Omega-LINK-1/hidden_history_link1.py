"""Ω-LINK-1 hidden-history inference experiment.

Question: can observable sequences distinguish a history-sensitive process
from a memoryless process without being told the hidden history label?

We construct two processes that emit the same current state B but differ in
next-state statistics because one retains a hidden predecessor. The analysis
uses repeated observations of B and estimates P(next|B) versus
P(next|B,previous). This is an explicit model test, not a conclusion.
"""

from collections import Counter

SEQUENCES = [
    ("A", "B", "A"),
    ("A", "B", "A"),
    ("A", "B", "A"),
    ("C", "B", "C"),
    ("C", "B", "C"),
    ("C", "B", "C"),
    ("A", "B", "A"),
    ("C", "B", "C"),
]


def conditional_counts(sequences):
    by_current = Counter()
    by_history = Counter()
    for previous, current, nxt in sequences:
        by_current[(current, nxt)] += 1
        by_history[(previous, current, nxt)] += 1
    return by_current, by_history


def entropy_binary(count_a, count_c):
    total = count_a + count_c
    if total == 0:
        return 0.0
    import math
    out = 0.0
    for n in (count_a, count_c):
        if n:
            p = n / total
            out -= p * math.log2(p)
    return out


if __name__ == "__main__":
    by_current, by_history = conditional_counts(SEQUENCES)
    b_a = by_current[("B", "A")]
    b_c = by_current[("B", "C")]
    print("OBSERVABLE_CURRENT=B")
    print("P(next=A|B)", b_a / (b_a + b_c))
    print("P(next=C|B)", b_c / (b_a + b_c))
    print("H(next|B)", entropy_binary(b_a, b_c))
    for previous in ("A", "C"):
        a = by_history[(previous, "B", "A")]
        c = by_history[(previous, "B", "C")]
        print("history", previous, "-> B", "P(next=A)", a/(a+c), "P(next=C)", c/(a+c))
    print("NOTE: history labels are used only for evaluation; the intended test is whether observable B alone is sufficient.")
