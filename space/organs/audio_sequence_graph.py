"""Deterministic candidate sequence graph for Ω-Audio.

This layer represents temporal acoustic/phoneme candidates as nodes and
NEXT relations. It does not promote candidates to confirmed linguistic facts.
"""
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class SoundCandidateNode:
    node_id: str
    label: str
    confidence: float
    start_s: float
    end_s: float
    confirmed: bool = False


@dataclass(frozen=True)
class SoundRelation:
    source: str
    relation: str
    target: str


@dataclass(frozen=True)
class SoundCandidateGraph:
    nodes: tuple[SoundCandidateNode, ...]
    relations: tuple[SoundRelation, ...]


class AudioSequenceGraphBuilder:
    def build(self, candidates: Iterable[SoundCandidateNode]) -> SoundCandidateGraph:
        nodes = tuple(sorted(candidates, key=lambda n: (n.start_s, n.end_s, n.node_id)))
        self._validate(nodes)
        relations = tuple(
            SoundRelation(a.node_id, "NEXT", b.node_id)
            for a, b in zip(nodes, nodes[1:])
        )
        return SoundCandidateGraph(nodes, relations)

    @staticmethod
    def _validate(nodes: tuple[SoundCandidateNode, ...]) -> None:
        ids = set()
        for node in nodes:
            if node.node_id in ids:
                raise ValueError("duplicate candidate node_id")
            ids.add(node.node_id)
            if not 0.0 <= node.confidence <= 1.0:
                raise ValueError("confidence must be in [0, 1]")
            if node.start_s < 0 or node.end_s < node.start_s:
                raise ValueError("invalid candidate time interval")
