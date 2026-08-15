import unittest

from space.integration.space_guardian_bridge import SpaceAction
from space.integration.space_memory_guardian_cycle import SpaceMemoryGuardianCycle
from space.prototype.capability_registry import Capability
from space.security.guardian_core import Decision, SecurityEvidence


class SpaceMemoryGuardianCycleTests(unittest.TestCase):
    def setUp(self):
        self.cycle = SpaceMemoryGuardianCycle()
        self.cap = Capability("read_memory", "read memory", verification_state="VERIFIED")
        self.good = SecurityEvidence("space-1", "key-1", True, True, True)

    def test_allowed_action_becomes_memory_and_clean_graph(self):
        result = self.cycle.step(
            SpaceAction("read-1", ("read_memory",)),
            [self.cap],
            self.good,
            "test:allowed-action",
        )
        self.assertEqual(result.decision, Decision.ALLOW)
        self.assertTrue(result.executed)
        self.assertEqual(len(self.cycle.events), 1)
        self.assertEqual(self.cycle.inspect_feedback_graph(), [])

    def test_blocked_action_is_recorded_without_execution(self):
        result = self.cycle.step(
            SpaceAction("read-2", ("read_memory",)),
            [self.cap],
            SecurityEvidence("space-1", "key-1", True, True, False),
            "test:replay",
        )
        self.assertEqual(result.decision, Decision.BLOCK)
        self.assertFalse(result.executed)
        self.assertEqual(self.cycle.events[0].decision, "BLOCK")
        self.assertEqual(self.cycle.inspect_feedback_graph(), [])

    def test_missing_capability_becomes_restricted_memory(self):
        result = self.cycle.step(
            SpaceAction("write-1", ("write_memory",)),
            [self.cap],
            self.good,
            "test:missing-capability",
        )
        self.assertEqual(result.decision, Decision.RESTRICT)
        self.assertFalse(result.executed)
        self.assertEqual(self.cycle.inspect_feedback_graph(), [])


if __name__ == "__main__":
    unittest.main()
