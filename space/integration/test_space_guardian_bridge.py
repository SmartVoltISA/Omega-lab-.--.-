import unittest

from space.integration.space_guardian_bridge import SpaceAction, SpaceGuardianBridge
from space.prototype.capability_registry import Capability
from space.security.guardian_core import Decision, SecurityEvidence


class SpaceGuardianBridgeTests(unittest.TestCase):
    def setUp(self):
        self.bridge = SpaceGuardianBridge()
        self.good = SecurityEvidence("space-1", "key-1", True, True, True)

    def test_verified_capability_and_valid_security_allows_execution(self):
        result = self.bridge.authorize(
            SpaceAction("act-1", ("read_memory",)),
            [Capability("read_memory", "read memory", verification_state="VERIFIED")],
            self.good,
        )
        self.assertEqual(result.decision, Decision.ALLOW)
        self.assertTrue(result.executed)
        self.assertEqual(result.missing_capabilities, ())

    def test_missing_capability_restricts_even_with_valid_security(self):
        result = self.bridge.authorize(
            SpaceAction("act-2", ("write_memory",)),
            [Capability("read_memory", "read memory", verification_state="VERIFIED")],
            self.good,
        )
        self.assertEqual(result.decision, Decision.RESTRICT)
        self.assertFalse(result.executed)
        self.assertEqual(result.missing_capabilities, ("write_memory",))

    def test_unverified_capability_is_missing(self):
        result = self.bridge.authorize(
            SpaceAction("act-3", ("read_memory",)),
            [Capability("read_memory", "read memory", verification_state="UNVERIFIED")],
            self.good,
        )
        self.assertEqual(result.decision, Decision.RESTRICT)
        self.assertFalse(result.executed)

    def test_guardian_block_overrides_capability(self):
        result = self.bridge.authorize(
            SpaceAction("act-4", ("read_memory",)),
            [Capability("read_memory", "read memory", verification_state="VERIFIED")],
            SecurityEvidence("space-1", "key-1", True, True, False),
        )
        self.assertEqual(result.decision, Decision.BLOCK)
        self.assertFalse(result.executed)

    def test_revoked_device_never_executes(self):
        result = self.bridge.authorize(
            SpaceAction("act-5", ()),
            [],
            SecurityEvidence("space-1", "key-1", True, True, True, revoked=True),
        )
        self.assertEqual(result.decision, Decision.BLOCK)
        self.assertFalse(result.executed)


if __name__ == "__main__":
    unittest.main()
