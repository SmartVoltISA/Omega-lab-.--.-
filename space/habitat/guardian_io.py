"""All external habitat I/O must cross Guardian before execution."""
from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class IORequest:
    request_id: str
    interface: str
    operation: str
    capability_id: str
    payload: Any
    direction: str

@dataclass(frozen=True)
class IODecision:
    allowed: bool
    reason: str
    result: Any = None

class GuardianIO:
    def __init__(self, authorizer: Callable[[IORequest], bool] | None = None) -> None:
        self.authorizer = authorizer or (lambda request: False)
        self.adapters: dict[str, Callable[[str, Any], Any]] = {}

    def register_adapter(self, interface: str, handler: Callable[[str, Any], Any]) -> None:
        self.adapters[interface] = handler

    def execute(self, request: IORequest, authorized: bool = False) -> IODecision:
        if not authorized and not self.authorizer(request):
            return IODecision(False, "guardian denied external I/O")
        if request.interface not in self.adapters:
            return IODecision(False, "interface adapter unavailable")
        result = self.adapters[request.interface](request.operation, request.payload)
        return IODecision(True, "guardian authorized", result)
