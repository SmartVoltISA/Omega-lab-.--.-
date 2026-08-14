"""Ω-LINK-1 Memory-State experiment.

Question: can two runs with the same current state produce different next
transitions solely because their prior histories differ?

The experiment compares a history-sensitive model with a memoryless control.
"""

CURRENT = "B"

HISTORIES = {
    "H1": ("A", "B"),
    "H2": ("C", "B"),
    "H3": ("A", "C", "B"),
    "H4": ("C", "A", "B"),
}


def memoryless_next(current):
    # Control: current state alone determines the next state.
    return {"B": "C"}[current]


def history_sensitive_next(history):
    # Minimal history-sensitive rule: the immediately previous state biases
    # the next transition. This is an explicit test model, not a conclusion.
    previous, current = history[-2], history[-1]
    if current != CURRENT:
        raise ValueError("history does not end in current state")
    return "A" if previous == "A" else "C"


if __name__ == "__main__":
    print("current_state", CURRENT)
    for name, history in HISTORIES.items():
        print(name, "history", history,
              "memoryless_next", memoryless_next(CURRENT),
              "history_sensitive_next", history_sensitive_next(history))
