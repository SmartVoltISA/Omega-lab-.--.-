"""Ω-LINK-1 Depth Sweep.

Construct controlled deterministic processes whose next state depends on a
specified number of previous symbols, then measure conditional entropy for
history windows of increasing depth.

This is a controlled model family. It tests whether the experimental setup
can recover known minimal history depths; it is not evidence that arbitrary
real systems have finite memory depth.
"""

from collections import defaultdict, Counter
import math


def entropy(rows):
    groups = defaultdict(Counter)
    for key, nxt in rows:
        groups[key][nxt] += 1
    total = len(rows)
    if not total:
        return 0.0
    result = 0.0
    for counts in groups.values():
        n = sum(counts.values())
        local = 0.0
        for c in counts.values():
            p = c / n
            local -= p * math.log2(p)
        result += (n / total) * local
    return result


def build_sequences(depth):
    # For each binary history of length `depth`, emit a distinct next symbol.
    # Prefix with one extra symbol so all observations have a current state.
    alphabet = ["A", "C"]
    histories = []

    def gen(prefix, n):
        if n == 0:
            histories.append(tuple(prefix))
            return
        for x in alphabet:
            gen(prefix + [x], n - 1)

    gen([], depth)
    sequences = []
    for i, hist in enumerate(histories):
        nxt = alphabet[i % 2]
        sequences.append(hist + ("B", nxt))
    return sequences


def measure(depth, window):
    rows = []
    for seq in build_sequences(depth):
        # Current observation is the final pre-transition B. A window of 1
        # means B alone; larger windows include progressively more history.
        key = tuple(seq[-(window + 1):-1]) if window > 0 else ()
        rows.append((key, seq[-1]))
    return entropy(rows)


if __name__ == "__main__":
    print("depth-sweep experiment")
    for target_depth in range(1, 7):
        values = []
        for window in range(0, target_depth + 2):
            values.append((window, measure(target_depth, window)))
        print("target_depth", target_depth, "entropy_by_window", values)
