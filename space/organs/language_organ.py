"""Ω-Language Organ v0.1.

A small language-facing organ. It converts constrained natural-language
statements into explicit Ω semantic relations and renders those relations
back to human-readable text. Local memory is tiered and every remembered
relation may carry provenance and confidence. Global graph access is outside
this module.
"""
from dataclasses import dataclass, field
import re
from typing import Iterable


@dataclass(frozen=True)
class SemanticRelation:
    subject: str
    relation: str
    object: str
    provenance: str | None = None
    confidence: float = 1.0

    def __post_init__(self) -> None:
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")


@dataclass
class MemoryTier:
    fast: list[SemanticRelation] = field(default_factory=list)
    working: list[SemanticRelation] = field(default_factory=list)
    long_term: list[SemanticRelation] = field(default_factory=list)


class LanguageOrgan:
    """Deterministic v0.1 language organ; no graph or external authority."""

    def __init__(self) -> None:
        self.memory = MemoryTier()

    @staticmethod
    def _clean(text: str) -> str:
        return re.sub(r"\s+", " ", text.strip().strip(".!?"))

    def understand(self, text: str, provenance: str | None = None) -> list[SemanticRelation]:
        """Parse a deliberately small, auditable set of relation patterns."""
        text = self._clean(text)
        lower = text.lower()
        patterns = [
            (r"^(.+?)\s+связан(?:а|о|ы)?\s+с\s+(.+)$", "связь"),
            (r"^(.+?)\s+хранит\s+(.+)$", "хранит"),
            (r"^(.+?)\s+сохраняет\s+(.+)$", "сохраняет"),
            (r"^(.+?)\s+работает\s+с\s+(.+)$", "работает_с"),
            (r"^(.+?)\s+имеет\s+(.+)$", "имеет"),
        ]
        for pattern, relation in patterns:
            match = re.match(pattern, lower, flags=re.IGNORECASE)
            if match:
                return [SemanticRelation(match.group(1).strip(), relation, match.group(2).strip(), provenance)]
        raise ValueError("language pattern is outside the v0.1 contract")

    def remember(self, relations: Iterable[SemanticRelation], tier: str = "working") -> None:
        if tier not in {"fast", "working", "long_term"}:
            raise ValueError("unknown memory tier")
        getattr(self.memory, tier).extend(relations)

    def promote(self, relation: SemanticRelation, from_tier: str, to_tier: str) -> None:
        if from_tier not in {"fast", "working", "long_term"} or to_tier not in {"fast", "working", "long_term"}:
            raise ValueError("unknown memory tier")
        source = getattr(self.memory, from_tier)
        target = getattr(self.memory, to_tier)
        if relation not in source:
            raise KeyError("relation is not present in source memory tier")
        source.remove(relation)
        if relation not in target:
            target.append(relation)

    def render(self, relations: Iterable[SemanticRelation]) -> str:
        return " ".join(f"{r.subject} — {r.relation} → {r.object}." for r in relations)

    def answer_from_local_memory(self, subject: str) -> str:
        """Return only local-memory evidence; no global graph lookup."""
        subject = subject.strip().lower()
        found = [r for tier in (self.memory.fast, self.memory.working, self.memory.long_term)
                 for r in tier if r.subject.lower() == subject]
        if not found:
            return "Нет подтверждённой локальной записи."
        return self.render(found)
