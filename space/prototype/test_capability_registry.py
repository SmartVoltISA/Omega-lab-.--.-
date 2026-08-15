import unittest

from capability_registry import Capability, CapabilityRegistry


class CapabilityRegistryTests(unittest.TestCase):
    def test_register_and_read(self):
        registry = CapabilityRegistry()
        cap = Capability("vision", "camera input", organs=("camera",), provenance="env-test")
        registry.register(cap)
        self.assertEqual(registry.get("vision"), cap)
        self.assertEqual(len(registry.all()), 1)

    def test_unverified_is_not_available(self):
        registry = CapabilityRegistry()
        registry.register(Capability("vision", "camera input"))
        self.assertEqual(registry.available(), [])
        self.assertEqual(registry.missing_or_unverified(["vision"]), ["vision"])

    def test_verified_is_available(self):
        registry = CapabilityRegistry()
        registry.register(Capability("vision", "camera input", verification_state="VERIFIED"))
        self.assertEqual([x.capability_id for x in registry.available()], ["vision"])
        self.assertEqual(registry.missing_or_unverified(["vision"]), [])

    def test_duplicate_rejected(self):
        registry = CapabilityRegistry()
        registry.register(Capability("vision", "camera input"))
        with self.assertRaises(ValueError):
            registry.register(Capability("vision", "same id"))

    def test_invalid_state_rejected(self):
        registry = CapabilityRegistry()
        with self.assertRaises(ValueError):
            registry.register(Capability("vision", "camera input", verification_state="TRUST_ME"))

    def test_snapshot_is_read_only(self):
        registry = CapabilityRegistry()
        registry.register(Capability("vision", "camera input"))
        snapshot = registry.snapshot()
        self.assertEqual(snapshot[0].capability_id, "vision")
        self.assertEqual(len(registry.all()), 1)


if __name__ == "__main__":
    unittest.main()
