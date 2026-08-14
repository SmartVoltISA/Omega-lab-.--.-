"""Ω-LINK-1 Depth Sweep — corrected construction.

For target depth N, the next symbol is a deterministic function of the full
N-symbol history. Every shorter window is deliberately insufficient: for each
shorter suffix there are histories with the same suffix but opposite next
symbols. At window N, the full history is sufficient.

This validates the measurement method on controlled model families. It is not
evidence that arbitrary real systems have finite memory depth.
"""

from collections import defaultdict, Counter
import math

ALPHABET = ("A", "C")


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


def all_histories(depth):
    if depth == 0:
        return [()]
    histories = [()]
    for _ in range(depth):
        histories = [h + (x,) for h in histories for x in ALPHABET]
    return histories


def next_from_history(history):
    # Encode A=0, C=1 and emit the parity of the complete history.
    parity = sum(1 for x in history if x == "C") % 2
    return ALPHABET[parity]


def build_sequences(depth):
    # Every complete depth-N history reaches the same current observation B.
    # The next state depends on the entire N-symbol history.
    return [history + ("B", next_from_history(history))
            for history in all_histories(depth)]


def measure(depth, window):
    rows = []
    for seq in build_sequences(depth):
        history = seq[:-2]  # symbols before the current B
        if window == 0:
            key = ()
        else:
            key = history[-window:]
        rows.append((key, seq[-1]))
    return entropy(rows)


if __name__ == "__main__":
    print("depth-sweep experiment — corrected")
    for target_depth in range(1, 7):
        values = []
        for window in range(0, target_depth + 2):
            values.append((window, measure(target_depth, window)))
        print("target_depth", target_depth, "entropy_by_window", values)
