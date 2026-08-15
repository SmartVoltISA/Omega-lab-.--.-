"""Read-only graph-memory integrity inspector.

This module deliberately reports structural defects without changing the input.
It is a small deterministic foundation for later Space integration.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Finding:
    code: str
    message: str
    subject: str


def inspect_graph(graph: dict[str, Any]) -> list[Finding]:
    """Inspect a graph and return deterministic structural findings.

    Expected shape::
        {"nodes": [{"id": ...}], "relations": [{"source": ..., "target": ...}]}

    The function never mutates ``graph``.
    """
    findings: list[Finding] = []
    nodes = graph.get("nodes", [])
    relations = graph.get("relations", [])

    seen: set[str] = set()
    for node in nodes:
        node_id = str(node.get("id", ""))
        if not node_id:
            findings.append(Finding("MISSING_NODE_ID", "Node has no identity", "<node>"))
            continue
        if node_id in seen:
            findings.append(Finding("DUPLICATE_NODE", "Duplicate node identity", node_id))
        seen.add(node_id)
        if not node.get("provenance"):
            findings.append(Finding("MISSING_PROVENANCE", "Node has no provenance", node_id))

    node_ids = seen
    for rel in relations:
        source = str(rel.get("source", ""))
        target = str(rel.get("target", ""))
        rel_id = str(rel.get("id", f"{source}->{target}"))
        if source not in node_ids:
            findings.append(Finding("DANGLING_SOURCE", "Relation source is missing", rel_id))
        if target not in node_ids:
            findings.append(Finding("DANGLING_TARGET", "Relation target is missing", rel_id))
        if not rel.get("provenance"):
            findings.append(Finding("MISSING_PROVENANCE", "Relation has no provenance", rel_id))

    # Detect incompatible explicit states for repeated identities.
    states: dict[str, set[str]] = {}
    for node in nodes:
        node_id = str(node.get("id", ""))
        state = node.get("state")
        if node_id and state is not None:
            states.setdefault(node_id, set()).add(str(state))
    for node_id, values in sorted(states.items()):
        if len(values) > 1:
            findings.append(
                Finding("CONFLICTING_STATE", "Node has incompatible state claims", node_id)
            )

    return sorted(findings, key=lambda f: (f.code, f.subject, f.message))


def inspect_without_mutation(graph: dict[str, Any]) -> tuple[list[Finding], bool]:
    """Return findings and whether the input remained byte-for-byte equivalent."""
    before = deepcopy(graph)
    findings = inspect_graph(graph)
    return findings, graph == before
