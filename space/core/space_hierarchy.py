"""Hierarchy and lineage for a family of SPACE organisms.

The hierarchy records *why* a SPACE exists and how it was derived without
making parent and child share private memory. Structural metadata is visible
through explicit queries; private organism state remains local.
"""
from dataclasses import dataclass, asdict
from typing import Any

@dataclass(frozen=True)
class SpaceModel:
    space_id: str
    model_id: str
    role: str
    purpose: str
    parent_space_id: str | None = None
    parent_model_id: str | None = None
    derived_from: str | None = None
    created_reason: str = ""
    visibility: str = "METADATA"
    version: str = "1.0"

class SpaceHierarchy:
    def __init__(self) -> None:
        self._models: dict[str, SpaceModel] = {}

    def register_root(self, space_id: str, model_id: str, purpose: str) -> SpaceModel:
        if self._models:
            raise ValueError("root SPACE already exists")
        model = SpaceModel(space_id, model_id, "ROOT", purpose, created_reason="foundation")
        self._models[space_id] = model
        return model

    def register_child(
        self,
        space_id: str,
        model_id: str,
        parent_space_id: str,
        purpose: str,
        role: str = "CHILD",
        reason: str = "",
        derived_from: str | None = None,
    ) -> SpaceModel:
        if space_id in self._models:
            raise ValueError("SPACE already registered")
        parent = self._models.get(parent_space_id)
        if parent is None:
            raise KeyError("parent SPACE not registered")
        if space_id == parent_space_id:
            raise ValueError("SPACE cannot be its own parent")
        model = SpaceModel(
            space_id, model_id, role, purpose,
            parent_space_id=parent.space_id,
            parent_model_id=parent.model_id,
            derived_from=derived_from or parent.space_id,
            created_reason=reason,
        )
        self._models[space_id] = model
        return model

    def get(self, space_id: str) -> SpaceModel:
        return self._models[space_id]

    def children(self, space_id: str) -> list[SpaceModel]:
        return [m for m in self._models.values() if m.parent_space_id == space_id]

    def ancestors(self, space_id: str) -> list[SpaceModel]:
        result: list[SpaceModel] = []
        current = self.get(space_id)
        seen: set[str] = set()
        while current.parent_space_id is not None:
            if current.space_id in seen:
                raise RuntimeError("SPACE hierarchy cycle detected")
            seen.add(current.space_id)
            current = self.get(current.parent_space_id)
            result.append(current)
        return result

    def descendants(self, space_id: str) -> list[SpaceModel]:
        result: list[SpaceModel] = []
        queue = list(self.children(space_id))
        while queue:
            current = queue.pop(0)
            result.append(current)
            queue.extend(self.children(current.space_id))
        return result

    def lineage(self, space_id: str) -> dict[str, Any]:
        model = self.get(space_id)
        return {
            "self": asdict(model),
            "ancestors": [asdict(m) for m in self.ancestors(space_id)],
            "children": [asdict(m) for m in self.children(space_id)],
            "descendants": [asdict(m) for m in self.descendants(space_id)],
        }

    def relationship(self, a: str, b: str) -> dict[str, Any]:
        if a not in self._models or b not in self._models:
            raise KeyError("unknown SPACE")
        ma, mb = self._models[a], self._models[b]
        if ma.parent_space_id == b:
            relation = "CHILD_OF"
        elif mb.parent_space_id == a:
            relation = "PARENT_OF"
        elif any(x.space_id == b for x in self.ancestors(a)):
            relation = "DESCENDANT_OF"
        elif any(x.space_id == a for x in self.ancestors(b)):
            relation = "ANCESTOR_OF"
        else:
            relation = "SIBLING_OR_PEER"
        return {"a": a, "b": b, "relation": relation, "a_model": ma.model_id, "b_model": mb.model_id}

    def visible_models(self) -> list[dict[str, Any]]:
        return [asdict(m) for m in self._models.values() if m.visibility == "METADATA"]
