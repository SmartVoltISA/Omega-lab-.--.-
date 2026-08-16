"""Group communication for SPACE organisms.

Groups are policy containers, not trust shortcuts. Membership, message scope and
permissions remain explicit and Guardian-controlled at the transport boundary.
"""
from dataclasses import dataclass, asdict
from typing import Any

@dataclass(frozen=True)
class GroupMember:
    space_id: str
    role: str
    scope: tuple[str, ...]
    status: str = "ACTIVE"

@dataclass(frozen=True)
class GroupMessage:
    message_id: str
    group_id: str
    sender: str
    recipients: tuple[str, ...]
    topic: str
    payload: Any
    visibility: str = "MEMBERS"

class SpaceGroup:
    def __init__(self, group_id: str, purpose: str) -> None:
        self.group_id = group_id
        self.purpose = purpose
        self.members: dict[str, GroupMember] = {}
        self.messages: list[GroupMessage] = []

    def add_member(self, space_id: str, role: str, scope: tuple[str, ...] = ()) -> GroupMember:
        member = GroupMember(space_id, role, scope)
        self.members[space_id] = member
        return member

    def remove_member(self, space_id: str) -> None:
        self.members.pop(space_id, None)

    def can_send(self, space_id: str, topic: str) -> bool:
        member = self.members.get(space_id)
        return bool(member and member.status == "ACTIVE" and (not member.scope or topic in member.scope))

    def send(self, message: GroupMessage) -> GroupMessage:
        if message.sender not in self.members:
            raise PermissionError("sender is not a group member")
        if not self.can_send(message.sender, message.topic):
            raise PermissionError("sender scope does not allow topic")
        unknown = [r for r in message.recipients if r not in self.members]
        if unknown:
            raise PermissionError("recipient is not a group member")
        self.messages.append(message)
        return message

    def snapshot(self) -> dict[str, Any]:
        return {
            "group_id": self.group_id,
            "purpose": self.purpose,
            "members": [asdict(m) for m in self.members.values()],
            "messages": [asdict(m) for m in self.messages],
        }
