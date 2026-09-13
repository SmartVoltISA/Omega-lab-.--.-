"""Ω-LINK-1 Minimal Horizon Validation.

For each controlled pair, find the first horizon at which future signatures differ.
Then explicitly verify that every earlier horizon is identical.
This tests minimality rather than merely observing a divergence.
"""

CASES = {
    "DIVERGE_AT_1": (("D", "E"), ("F", "G")),
    "DIVERGE_AT_2": (("D", "E", "F"), ("D", "E", "G")),
    "DIVERGE_AT_3": (("D", "E", "F", "H"), ("D", "E", "F", "I")),
    "NO_DIVERGENCE": (("D", "E", "F"), ("D", "E", "F")),
}


def first_divergence(left, right):
    for horizon, (a, b) in enumerate(zip(left, right), start=1):
        if a != b:
            return horizon
    return None


def is_minimal(left, right, divergence):
    if divergence is None:
        return all(left[:h] == right[:h] for h in range(1, min(len(left), len(right)) + 1))
    earlier_same = all(left[:h] == right[:h] for h in range(1, divergence))
    at_divergence_diff = left[:divergence] != right[:divergence]
    return earlier_same and at_divergence_diff


if __name__ == "__main__":
    print("minimal-horizon validation experiment")
    for label, (left, right) in CASES.items():
        divergence = first_divergence(left, right)
        minimal = is_minimal(left, right, divergence)
        print(label)
        print("future_1", left)
        print("future_2", right)
        print("first_divergence_horizon", divergence)
        print("minimality_verified", minimal)
        if divergence is not None:
            for h in range(1, divergence + 1):
                print("horizon", h, "same", left[:h] == right[:h])
