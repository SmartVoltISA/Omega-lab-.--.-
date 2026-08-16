from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class Tool:
    tool_id: str
    description: str
    capability_id: str
    handler: Callable[..., Any]

class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        if tool.tool_id in self._tools:
            raise ValueError("duplicate tool id")
        self._tools[tool.tool_id] = tool

    def get(self, tool_id: str) -> Tool:
        return self._tools[tool_id]

    def list(self) -> list[Tool]:
        return list(self._tools.values())

    def call(self, tool_id: str, **kwargs: Any) -> Any:
        return self.get(tool_id).handler(**kwargs)
