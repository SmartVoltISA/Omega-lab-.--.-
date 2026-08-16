import unittest

from space.security.distribution_boundary import Capability, DistributionBoundary, DistributionRequest


class DistributionBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.boundary = DistributionBoundary()

    def test_all_external_and_distributed_capabilities_default_deny(self):
        for capability in Capability:
            request = DistributionRequest("req-1", capability, "space-1", "external")
            self.assertFalse(self.boundary.inspect(request), capability)

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
