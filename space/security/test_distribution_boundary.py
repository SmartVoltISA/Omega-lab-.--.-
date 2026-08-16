import unittest

from space.security.distribution_boundary import Capability, DistributionBoundary, DistributionRequest


class DistributionBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.boundary = DistributionBoundary()

    def test_external_capabilities_default_deny(self):
        for capability in (
            Capability.NETWORK,
            Capability.BLUETOOTH,
            Capability.PEER_DISCOVERY,
            Capability.MEMORY_SHARING,
            Capability.CAPABILITY_DELEGATION,
            Capability.SELF_DEPLOYMENT,
        ):
            request = DistributionRequest("req-1", capability, "space-1", "external")
            self.assertFalse(self.boundary.inspect(request), capability)

    def test_lab_reproduction_allowed_only_in_sandbox(self):
        request = DistributionRequest(
            "req-lab", Capability.LAB_REPRODUCTION, "space-1", "lab", scope="sandbox"
        )
        self.assertTrue(self.boundary.inspect(request))
        self.assertTrue(self.boundary.can_lab_reproduce())

    def test_lab_reproduction_not_allowed_in_external_scope(self):
        request = DistributionRequest(
            "req-ext", Capability.LAB_REPRODUCTION, "space-1", "external", scope="external"
        )
        self.assertFalse(self.boundary.inspect(request))

    def test_no_peer_discovery(self):
        self.assertFalse(self.boundary.can_discover_peers())

    def test_no_memory_sharing(self):
        self.assertFalse(self.boundary.can_share_memory())

    def test_no_capability_delegation(self):
        self.assertFalse(self.boundary.can_delegate())

    def test_no_self_deployment(self):
        self.assertFalse(self.boundary.can_self_deploy())


if __name__ == "__main__":
    unittest.main()
