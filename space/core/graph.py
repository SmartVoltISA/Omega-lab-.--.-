from dataclasses import dataclass, asdict
from typing import Any


PROTECTED_FOUNDATION_PREFIX = "foundation:"
PROTECTED_FOUNDATION_RELATION_PREFIX = "foundation:"


@dataclass(frozen=True)
class Node:
    node_id: str
    state: Any = None
    memory_ref: str | None = None


@dataclass(frozen=True)
class Edge:
    edge_id: str
    source: str
    target: str
    relation: str
    memory_ref: str | None = None


class GraphCore:
    """Operational graph.

    The protected Ω foundation is deliberately outside this graph. SPACE may
    operate on ordinary nodes and relations, but it can never insert a
    protected foundation node or create an edge to/from one. Foundation
    integrity is enforced by Guardian, not by graph discovery.
    """

    def __init__(self) -> None:
        self.nodes = {}
        self.edges = {}
        self._counter = 0

    @staticmethod
    def _is_protected(node_id: str) -> bool:
        return node_id.startswith(PROTECTED_FOUNDATION_PREFIX)

    @staticmethod
    def _is_protected_relation(relation: str) -> bool:
        return relation.startswith(PROTECTED_FOUNDATION_RELATION_PREFIX)

    def upsert_node(self, node_id: str, state: Any = None, memory_ref: str | None = None) -> Node:
        if self._is_protected(node_id):
            raise PermissionError("protected foundation is outside operational graph")
        node = Node(node_id, state, memory_ref)
        self.nodes[node_id] = node
        return node

    def connect(self, source: str, target: str, relation: str, memory_ref: str | None = None) -> Edge:
        if self._is_protected(source) or self._is_protected(target):
            raise PermissionError("protected foundation cannot be connected to operational graph")
        if self._is_protected_relation(relation):
            raise PermissionError("protected foundation relations are outside operational graph")
        if source not in self.nodes or target not in self.nodes:
            raise ValueError("graph endpoints must exist")
        self._counter += 1
        edge = Edge(f"edge-{self._counter}", source, target, relation, memory_ref)
        self.edges[edge.edge_id] = edge
        return edge

    def neighbors(self, node_id: str) -> list[Node]:
        if self._is_protected(node_id):
            return []
        ids = {e.target for e in self.edges.values() if e.source == node_id}
        return [self.nodes[i] for i in ids]

    def snapshot(self) -> dict[str, list[dict[str, Any]]]:
        return {"nodes": [asdict(n) for n in self.nodes.values()], "edges": [asdict(e) for e in self.edges.values()]}

    def whole_state(self) -> dict[str, Any]:
        return {"node_count": len(self.nodes), "edge_count": len(self.edges), "nodes": {n.node_id: n.state for n in self.nodes.values()}}
