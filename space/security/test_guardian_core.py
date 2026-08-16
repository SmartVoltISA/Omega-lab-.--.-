import unittest

from guardian_core import Decision, GuardianCore, SecurityEvidence


class GuardianCoreTests(unittest.TestCase):
    def setUp(self):
        self.g = GuardianCore()
        self.good = SecurityEvidence("space-1", "key-1", True, True, True)

    def test_valid_device_allowed(self):
        self.assertEqual(self.g.decide(self.good), Decision.ALLOW)

    def test_missing_identity_blocked(self):
        self.assertEqual(self.g.decide(SecurityEvidence("", "key-1", True, True, True)), Decision.BLOCK)

    def test_unattested_key_restricted(self):
        self.assertEqual(self.g.decide(SecurityEvidence("space-1", "key-1", False, True, True)), Decision.RESTRICT)

    def test_bad_integrity_restricted(self):
        self.assertEqual(self.g.decide(SecurityEvidence("space-1", "key-1", True, False, True)), Decision.RESTRICT)

    def test_replay_blocked(self):
        self.assertEqual(self.g.decide(SecurityEvidence("space-1", "key-1", True, True, False)), Decision.BLOCK)

    def test_revoked_device_blocked(self):
        self.assertEqual(self.g.decide(SecurityEvidence("space-1", "key-1", True, True, True, revoked=True)), Decision.BLOCK)

    def test_recovery_is_restricted(self):
        self.assertEqual(self.g.decide(SecurityEvidence("space-1", "key-1", True, True, True, recovery_mode=True)), Decision.RESTRICT)

    def test_foundation_mismatch_is_always_blocked(self):
        evidence = SecurityEvidence(
            "space-1", "key-1", True, True, True,
            foundation_ok=False,
        )
        self.assertEqual(self.g.decide(evidence), Decision.BLOCK)

    def test_foundation_mismatch_overrides_recovery(self):
        evidence = SecurityEvidence(
            "space-1", "key-1", True, True, True,
            recovery_mode=True,
            foundation_ok=False,
        )
        self.assertEqual(self.g.decide(evidence), Decision.BLOCK)


if __name__ == "__main__":
    unittest.main()
