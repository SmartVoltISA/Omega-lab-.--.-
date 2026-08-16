import unittest

from space.organs.autonomous_organ import AutonomousOrgan, OrganRuntime
from space.organs.causal_memory import CausalMemory
from space.organs.closed_loop import OrganClosedLoop
from space.organs.quarantine import OrganQuarantine


class ClosedLoopQuarantineTests(unittest.TestCase):
    def make_organs(self):
        a = AutonomousOrgan("a")
        b = AutonomousOrgan("b")
        a.register_operation("increment", lambda value: value + 1)
        b.register_operation("echo", lambda value: value)
        runtime = OrganRuntime()
        runtime.register(a)
        runtime.register(b)
        return a, b, runtime

    def test_closed_causal_loop(self):
        a, _, _ = self.make_organs()
        loop = OrganClosedLoop(a, CausalMemory())
        first = loop.step("input", "increment", 1, lambda result: "good" if result == 2 else "bad")
        self.assertEqual(first.result, 2)
        self.assertEqual(first.evaluation, "good")
        self.assertEqual(loop.snapshot()["causal_memory"][0]["action"], "increment")
        self.assertEqual(a.state["last_evaluation"], "good")

    def test_local_memory_does_not_become_graph(self):
        a, _, _ = self.make_organs()
        loop = OrganClosedLoop(a)
        loop.step("input", "increment", 4)
        self.assertNotIn("graph", loop.snapshot())

    def test_quarantine_isolates_only_target(self):
        a, b, runtime = self.make_organs()
        quarantine = OrganQuarantine(runtime)
        quarantine.isolate("a", "health failure")
        self.assertTrue(quarantine.is_isolated("a"))
        self.assertFalse(a.running)
        self.assertTrue(b.running)
        self.assertEqual(quarantine.available_organs(), ["b"])
        quarantine.release("a")
        self.assertTrue(a.running)

    def test_quarantine_unknown_organ_fails_closed(self):
        _, _, runtime = self.make_organs()
        with self.assertRaises(ValueError):
            OrganQuarantine(runtime).isolate("missing", "unknown")


if __name__ == "__main__":
    unittest.main()
