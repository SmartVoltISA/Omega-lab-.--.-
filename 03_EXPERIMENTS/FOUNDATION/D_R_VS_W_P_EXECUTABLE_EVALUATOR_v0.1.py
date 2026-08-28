from dataclasses import dataclass
from typing import FrozenSet, Tuple

@dataclass(frozen=True)
class Model:
    name: str
    primitives: FrozenSet[str]
    rules: Tuple[str, ...]

CAPS = (
    "T1_distinguishable_alternatives",
    "T2_identity_boundary",
    "T3_allowed_forbidden",
    "T4_selection_action",
    "T5_state_change",
    "T6_history_feedback",
    "T7_closed_cycle",
)

# This evaluator is intentionally symbolic. It does not assert that the
# symbolic constructions are physical ontology; it tests dependency leakage.
A = Model(
    "D+R",
    frozenset({"D", "R"}),
    (
        "D(a,b)",
        "R(s,a)",
        "R(s,b)",
        "RULE: configuration = finite typed relations",
        "RULE: transition = relation between configurations",
        "RULE: retained_trace = relation from current configuration to prior record",
        "RULE: cycle = repeated transition relation with guard",
    ),
)

B = Model(
    "W+P",
    frozenset({"W", "P"}),
    (
        "W(select)",
        "P(restrict)",
        "RULE: W selects a target",
        "RULE: P restricts a target",
    ),
)

# Required hidden dependencies. A construction cannot be labelled DIRECT if
# it needs any of these without explicitly deriving them.
DEPENDENCIES = {
    "T1_distinguishable_alternatives": {"D"},
    "T2_identity_boundary": {"D", "R"},
    "T3_allowed_forbidden": {"D", "R"},
    "T4_selection_action": {"D", "R", "W"},
    "T5_state_change": {"D", "R"},
    "T6_history_feedback": {"D", "R"},
    "T7_closed_cycle": {"D", "R"},
}

def classify(model: Model, capability: str):
    need = DEPENDENCIES[capability]
    missing = need - model.primitives

    # D+R can derive the higher-level capabilities through explicit rules.
    if model.name == "D+R" and capability in CAPS:
        if capability == "T1_distinguishable_alternatives":
            return "DIRECT", frozenset()
        if capability in {"T2_identity_boundary", "T3_allowed_forbidden", "T5_state_change", "T6_history_feedback", "T7_closed_cycle"}:
            return "DERIVED", frozenset()
        if capability == "T4_selection_action":
            return "IMPORTED", frozenset({"W"})

    # W+P cannot obtain meaningful alternatives/restrictions without
    # distinguishability and a target relation. Those are counted as leakage.
    if model.name == "W+P":
        if capability == "T1_distinguishable_alternatives":
            return "IMPORTED", frozenset({"D"})
        if capability == "T2_identity_boundary":
            return "IMPORTED", frozenset({"D", "R"})
        if capability == "T3_allowed_forbidden":
            return "IMPORTED", frozenset({"D", "R"})
        if capability == "T4_selection_action":
            return "IMPORTED", frozenset({"D", "R"})
        if capability == "T5_state_change":
            return "IMPORTED", frozenset({"D", "R"})
        if capability == "T6_history_feedback":
            return "IMPORTED", frozenset({"D", "R"})
        if capability == "T7_closed_cycle":
            return "IMPORTED", frozenset({"D", "R"})

    return "UNREPRESENTABLE", frozenset(missing)

def run():
    rows = []
    for model in (A, B):
        for cap in CAPS:
            status, deps = classify(model, cap)
            rows.append((model.name, cap, status, ",".join(sorted(deps))))
    print("model,capability,status,dependencies")
    for row in rows:
        print(",".join(row))

if __name__ == "__main__":
    run()
