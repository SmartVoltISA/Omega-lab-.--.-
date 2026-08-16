import unittest

from space.integration.organ_guardian_router import OrganGuardianRouter
from space.organs.autonomous_organ import AutonomousOrgan, OrganRuntime
from space.organs.multi_organ_exchange import MultiOrganExchange
from space.prototype.capability_registry import Capability
from space.security.guardian_core import SecurityEvidence


class MultiOrganExchangeTests(unittest.TestCase):
    def setUp(self):
        self.a = AutonomousOrgan("a")
        self.b = AutonomousOrgan("b")
        self.a.register_operation("receive", lambda payload: payload)
        self.b.register_operation("receive", lambda payload: payload)
        self.runtime = OrganRuntime()
        self.runtime.register(self.a)
        self.runtime.register(self.b)
        self.exchange = MultiOrganExchange(OrganGuardianRouter(self.runtime))
        self.evidence = SecurityEvidence(source="test", action="organ:a:b:receive")
        self.cap = Capability(name="organ.receive", scope="b")

    def test_exchange_goes_through_router(self):
        step = self.exchange.send("a", "b", "receive", "hello", "organ.receive", [self.cap], self.evidence)
        self.assertTrue(step.executed)
        self.assertEqual(len(self.exchange.history), 1)

    def test_missing_capability_is_blocked(self):
        step = self.exchange.send("a", "b", "receive", "hello", "organ.receive", [], self.evidence)
        self.assertFalse(step.executed)

    def test_stopped_target_does_not_execute(self):
        self.b.stop()
        step = self.exchange.send("a", "b", "receive", "hello", "organ.receive", [self.cap], self.evidence)
        self.assertFalse(step.executed)

    def test_unknown_target_is_rejected(self):
        with self.assertRaises(ValueError):
            self.exchange.send("a", "missing", "receive", "hello", "organ.receive", [self.cap], self.evidence)


if __name__ == "__main__":
    unittest.main()
