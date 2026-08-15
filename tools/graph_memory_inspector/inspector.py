"""Read-only graph-memory integrity inspector.

Nodes and edges are first-class records. The inspector observes both and never
changes the supplied graph.
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
    """Inspect nodes and first-class edges for deterministic structural defects.

    Expected shape::
        {
            "nodes": [{"id": ..., "state": ..., "provenance": ...}],
            "relations": [{
                "id": ..., "source": ..., "target": ..., "type": ...,
                "provenance": ...
            }]
        }

    The function never mutates ``graph``.
    """
    findings: list[Finding] = []
    nodes = graph.get("nodes", [])
    relations = graph.get("relations", [])

    seen_nodes: set[str] = set()
    for node in nodes:
        node_id = str(node.get("id", ""))
        if not node_id:
            findings.append(Finding("MISSING_NODE_ID", "Node has no identity", "<node>"))
            continue
        if node_id in seen_nodes:
            findings.append(Finding("DUPLICATE_NODE", "Duplicate node identity", node_id))
        seen_nodes.add(node_id)
        if not node.get("provenance"):
            findings.append(Finding("MISSING_PROVENANCE", "Node has no provenance", node_id))

    # Edges/relations are first-class objects: identity, endpoints, type and provenance.
    seen_edges: set[str] = set()
    edge_signatures: set[tuple[str, str, str]] = set()
    for index, rel in enumerate(relations):
        rel_id = str(rel.get("id", ""))
        source = str(rel.get("source", ""))
        target = str(rel.get("target", ""))
        rel_type = str(rel.get("type", ""))
        subject = rel_id or f"relation[{index}]"

        if not rel_id:
            findings.append(Finding("MISSING_RELATION_ID", "Relation has no identity", subject))
        elif rel_id in seen_edges:
            findings.append(Finding("DUPLICATE_RELATION", "Duplicate relation identity", rel_id))
        seen_edges.add(rel_id)

        if source not in seen_nodes:
            findings.append(Finding("DANGLING_SOURCE", "Relation source is missing", subject))
        if target not in seen_nodes:
            findings.append(Finding("DANGLING_TARGET", "Relation target is missing", subject))
        if not rel_type:
            findings.append(Finding("MISSING_RELATION_TYPE", "Relation has no semantic type", subject))
        if not rel.get("provenance"):
            findings.append(Finding("MISSING_PROVENANCE", "Relation has no provenance", subject))

        signature = (source, target, rel_type)
        if rel_type and signature in edge_signatures:
            findings.append(Finding("DUPLICATE_EDGE_SIGNATURE", "Duplicate source-target-type edge", subject))
        edge_signatures.add(signature)

    # Detect incompatible explicit states for repeated identities.
    states: dict[str, set[str]] = {}
    for node in nodes:
        node_id = str(node.get("id", ""))
        state = node.get("state")
        if node_id and state is not None:
            states.setdefault(node_id, set()).add(str(state))
    for node_id, values in sorted(states.items()):
        if len(values) > 1:
            findings.append(Finding("CONFLICTING_STATE", "Node has incompatible state claims", node_id))

    return sorted(findings, key=lambda f: (f.code, f.subject, f.message))


def inspect_without_mutation(graph: dict[str, Any]) -> tuple[list[Finding], bool]:
    """Return findings and whether the input remained equivalent."""
    before = deepcopy(graph)
    findings = inspect_graph(graph)
    return findings, graph == before
