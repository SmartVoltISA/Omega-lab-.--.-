import unittest

from space.organs.autonomous_organ import AutonomousOrgan, OrganMessage, OrganRuntime


class TestAutonomousOrganPhase1(unittest.TestCase):
    def test_local_state_and_memory_are_independent(self):
        a = AutonomousOrgan("A", allowed_operations={"sense"})
        b = AutonomousOrgan("B", allowed_operations={"sense"})
        a.state["x"] = 1
        a.remember("a-only")
        self.assertNotIn("x", b.state)
        self.assertEqual(b.local_memory, [])

    def test_message_requires_exact_target(self):
        a = AutonomousOrgan("A", allowed_operations={"sense"})
        with self.assertRaises(ValueError):
            a.accept_message(OrganMessage("B", "C", "sense"))

    def test_unknown_operation_is_denied(self):
        a = AutonomousOrgan("A", allowed_operations={"sense"})
        with self.assertRaises(PermissionError):
            a.accept_message(OrganMessage("B", "A", "execute"))

    def test_runtime_keeps_memory_local(self):
        runtime = OrganRuntime()
        a = AutonomousOrgan("A", allowed_operations={"sense"})
        b = AutonomousOrgan("B", allowed_operations={"sense"})
        runtime.register(a)
        runtime.register(b)
        runtime.send(OrganMessage("A", "B", "sense", "hello"))
        self.assertEqual(a.local_memory, [])
        self.assertEqual(b.local_memory, [])
        self.assertIsNot(a.local_memory, b.local_memory)

    def test_one_stopped_organ_does_not_remove_other(self):
        runtime = OrganRuntime()
        good = AutonomousOrgan("GOOD", allowed_operations={"sense"})
        bad = AutonomousOrgan("BAD", allowed_operations={"sense"})
        runtime.register(good)
        runtime.register(bad)
        bad.stop()
        self.assertIn("GOOD", runtime.organs)
        self.assertIn("BAD", runtime.organs)
        self.assertEqual(runtime.send(OrganMessage("X", "GOOD", "sense", 1))["organ"], "GOOD")


if __name__ == "__main__":
    unittest.main()
