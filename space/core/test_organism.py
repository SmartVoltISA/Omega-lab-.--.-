import unittest

from space.core.organism import SpaceOrganism
from space.prototype.capability_registry import Capability
from space.security.guardian_core import Decision, SecurityEvidence

class SpaceOrganismTests(unittest.TestCase):
    def setUp(self):
        self.org = SpaceOrganism("space-test")
        self.org.register_capability(Capability("compute", "bounded compute", verification_state="VERIFIED"))
        self.org.register_tool("echo", "returns input", "compute", lambda **kw: kw["value"])
        self.good = SecurityEvidence("space-test", "key-1", True, True, True)

    def test_full_cycle_updates_memory_and_graph(self):
        result = self.org.step("echo", self.good, value=7)
        self.assertEqual(result.decision, Decision.ALLOW.value)
        self.assertTrue(result.executed)
        self.assertEqual(result.output, 7)
        self.assertEqual(len(self.org.memory.snapshot()), 1)
        self.assertEqual(len(self.org.graph.nodes), 2)
        self.assertEqual(len(self.org.graph.edges), 1)

    def test_guardian_blocks_execution(self):
        stale = SecurityEvidence("space-test", "key-1", True, True, False)
        result = self.org.step("echo", stale, value=7)
        self.assertEqual(result.decision, Decision.BLOCK.value)
        self.assertFalse(result.executed)
        self.assertIsNone(result.output)

    def test_missing_capability_does_not_execute(self):
        self.org.register_tool("restricted", "restricted tool", "missing", lambda **kw: 1)
        result = self.org.step("restricted", self.good)
        self.assertEqual(result.decision, Decision.RESTRICT.value)
        self.assertFalse(result.executed)

    def test_repeated_semantic_cycle_triggers_replan(self):
        for _ in range(4):
            result = self.org.step("echo", self.good, value=1)
        self.assertEqual(result.guard_action, "STOP_REPLAN")
        self.assertEqual(self.org.state.mode, "REPLAN")

if __name__ == "__main__":
    unittest.main()
