"""Ω-LINK-1 Future Divergence experiment.

Two history pairs share the same immediate next state when intended, then
become distinguishable at a later prediction horizon. Controlled construction.
"""

PAIRS = {
    "DIVERGE_AT_1": (("A", "B"), ("C", "B"), ("D", "E"), ("F", "G")),
    "DIVERGE_AT_2": (("A", "B"), ("C", "B"), ("D", "E", "F"), ("D", "E", "G")),
    "DIVERGE_AT_3": (("A", "B"), ("C", "B"), ("D", "E", "F", "H"), ("D", "E", "F", "I")),
}


def first_divergence(left, right):
    for i, (a, b) in enumerate(zip(left, right), start=1):
        if a != b:
            return i
    return None


if __name__ == "__main__":
    print("future-divergence experiment")
    for label, (h1, h2, f1, f2) in PAIRS.items():
        print(label)
        print("history_pair", h1, h2)
        print("future_1", f1)
        print("future_2", f2)
        print("first_divergence_horizon", first_divergence(f1, f2))
        for horizon in range(1, min(len(f1), len(f2)) + 1):
            s1, s2 = f1[:horizon], f2[:horizon]
            print("horizon", horizon, "same", s1 == s2, "signature_1", s1, "signature_2", s2)
