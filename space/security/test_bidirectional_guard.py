import unittest

from space.security.bidirectional_guard import BidirectionalGuardian, BoundaryRequest, Direction
from space.security.guardian_core import Decision, SecurityEvidence

class BidirectionalGuardianTests(unittest.TestCase):
    def setUp(self):
        self.guard = BidirectionalGuardian()
        self.good = SecurityEvidence("space-a", "device-1", True, True, True)

    def test_inbound_and_outbound_are_both_allowed_when_authorized(self):
        inbound = BoundaryRequest("in-1", Direction.INBOUND, "wifi", "space-a", "network.receive", "data")
        outbound = BoundaryRequest("out-1", Direction.OUTBOUND, "space-a", "wifi", "network.send", "data")
        self.assertEqual(self.guard.inspect(inbound, self.good).decision, Decision.ALLOW)
        self.assertEqual(self.guard.inspect(outbound, self.good).decision, Decision.ALLOW)

    def test_rejected_evidence_blocks_both_directions(self):
        bad = SecurityEvidence("space-a", "device-1", True, False, True)
        req = BoundaryRequest("x", Direction.OUTBOUND, "space-a", "wifi", "network.send")
        self.assertEqual(self.guard.inspect(req, bad).decision, Decision.RESTRICT)

    def test_quarantined_scope_blocks_interaction(self):
        self.guard.block_scope("quarantine")
        req = BoundaryRequest("q", Direction.INBOUND, "wifi", "space-a", "network.receive", scope="quarantine")
        self.assertEqual(self.guard.inspect(req, self.good).decision, Decision.BLOCK)

if __name__ == "__main__":
    unittest.main()
