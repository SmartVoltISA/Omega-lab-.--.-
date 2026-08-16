"""Transport contract for communication between SPACE organisms."""
from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class SpaceMessage:
    message_id: str
    sender: str
    receiver: str
    capability_id: str
    payload: Any
    correlation_id: str
    freshness: int

class SpaceTransport:
    def __init__(self, authorize: Callable[[SpaceMessage], bool] | None = None) -> None:
        self.authorize = authorize or (lambda message: False)
        self.peers: dict[str, Callable[[SpaceMessage], Any]] = {}

    def register_peer(self, space_id: str, handler: Callable[[SpaceMessage], Any]) -> None:
        self.peers[space_id] = handler

    def send(self, message: SpaceMessage, authorized: bool = False) -> Any:
        if not authorized and not self.authorize(message):
            raise PermissionError("Guardian denied SPACE-to-SPACE message")
        if message.receiver not in self.peers:
            raise LookupError("SPACE peer unavailable")
        return self.peers[message.receiver](message)
