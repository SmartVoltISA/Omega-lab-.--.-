"""Human decision-support boundary for SPACE.

This organ structures evidence and alternatives without becoming the decision
maker. Consequential execution remains behind explicit authorization.
"""
from dataclasses import dataclass, asdict
from typing import Any

@dataclass(frozen=True)
class Option:
    option_id: str
    description: str
    expected_outcome: Any
    uncertainty: Any = None
    risks: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = ()

@dataclass(frozen=True)
class DecisionBrief:
    brief_id: str
    question: str
    options: tuple[Option, ...]
    evidence: tuple[str, ...]
    recommendation: str | None
    consequential: bool
    understanding_required: bool

class DecisionSupport:
    def build(self, brief_id: str, question: str, options: list[Option], evidence: list[str] | None = None, recommendation: str | None = None, consequential: bool = True) -> DecisionBrief:
        if not options:
            raise ValueError("decision support requires at least one option")
        return DecisionBrief(
            brief_id=brief_id,
            question=question,
            options=tuple(options),
            evidence=tuple(evidence or ()),
            recommendation=recommendation,
            consequential=consequential,
            understanding_required=consequential,
        )

    def record_human_decision(self, brief: DecisionBrief, option_id: str) -> dict[str, Any]:
        valid = {option.option_id for option in brief.options}
        if option_id not in valid:
            raise ValueError("human decision must select a presented option")
        return {"brief_id": brief.brief_id, "decision_owner": "HUMAN", "option_id": option_id}

    def explain(self, brief: DecisionBrief) -> dict[str, Any]:
        return asdict(brief) | {"decision_owner": "HUMAN"}
