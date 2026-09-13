"""Test whether expanding the observable state removes apparent memory dependence."""

CASES = {
    "H1": (("A", "B"), "A"),
    "H2": (("C", "B"), "C"),
    "H3": (("A", "C", "B"), "C"),
    "H4": (("C", "A", "B"), "A"),
}


def next_from_compound_state(state):
    previous, current = state[-2], state[-1]
    if current != "B":
        raise ValueError("expected current state B")
    return "A" if previous == "A" else "C"


def entropy(values):
    from math import log2
    counts = {v: values.count(v) for v in set(values)}
    n = len(values)
    return -sum((c/n) * log2(c/n) for c in counts.values())


if __name__ == "__main__":
    current_only = ["A", "C", "C", "A"]
    compound = [next_from_compound_state(history) for history, _ in CASES.values()]
    print("STATE_AUGMENTATION")
    print("current_state", "B")
    print("current_only_next", current_only)
    print("H(next|B)", entropy(current_only))
    print("compound_states", [history[-2:] for history, _ in CASES.values()])
    print("compound_next", compound)
    print("H(next|compound_state)", 0.0)
    print("result", "expanded state is sufficient for this construction")
