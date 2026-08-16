import unittest

from space.integration.organ_guardian_router import OrganGuardianRouter
from space.organs.autonomous_organ import AutonomousOrgan, OrganMessage, OrganRuntime
from space.prototype.capability_registry import Capability
from space.security.guardian_core import Decision, SecurityEvidence


class OrganGuardianRouterTests(unittest.TestCase):
    def setUp(self):
        self.runtime = OrganRuntime()
        self.target = AutonomousOrgan("audio", allowed_operations={"transcribe"})
        self.target.register_operation("transcribe", lambda payload: payload.upper())
        self.runtime.register(self.target)
        self.router = OrganGuardianRouter(self.runtime)
        self.capability = Capability("audio.read", "read audio", verification_state="VERIFIED")
        self.good = SecurityEvidence("space-1", "key-1", True, True, True)

    def test_authorized_message_executes_target_local_handler(self):
        message = OrganMessage("vision", "audio", "transcribe", "hello", "audio.read")
        result = self.router.dispatch(message, [self.capability], self.good)
        self.assertEqual(result.decision, Decision.ALLOW)
        self.assertTrue(result.executed)
        self.assertEqual(self.target.memory[-1]["result"], "HELLO")

    def test_missing_capability_cannot_execute(self):
        message = OrganMessage("vision", "audio", "transcribe", "hello", "audio.read")
        result = self.router.dispatch(message, [], self.good)
        self.assertEqual(result.decision, Decision.RESTRICT)
        self.assertFalse(result.executed)
        self.assertEqual(self.target.memory, [])

    def test_guardian_block_cannot_execute(self):
        message = OrganMessage("vision", "audio", "transcribe", "hello", "audio.read")
        blocked = SecurityEvidence("space-1", "key-1", True, True, False)
        result = self.router.dispatch(message, [self.capability], blocked)
        self.assertEqual(result.decision, Decision.BLOCK)
        self.assertFalse(result.executed)
        self.assertEqual(self.target.memory, [])

    def test_unknown_target_is_rejected(self):
        message = OrganMessage("vision", "missing", "transcribe", "hello", "audio.read")
        with self.assertRaises(ValueError):
            self.router.dispatch(message, [self.capability], self.good)

    def test_stopped_target_does_not_execute(self):
        self.target.stop()
        message = OrganMessage("vision", "audio", "transcribe", "hello", "audio.read")
        result = self.router.dispatch(message, [self.capability], self.good)
        self.assertEqual(result.decision, Decision.RESTRICT)
        self.assertFalse(result.executed)


if __name__ == "__main__":
    unittest.main()
