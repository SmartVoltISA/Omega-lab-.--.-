import unittest

from space.core.audience_policy import AudiencePolicy, AudienceRequest, AudienceScope
from space.core.communication_gateway import CommunicationGateway

class CommunicationGatewayTests(unittest.TestCase):
    def setUp(self):
        self.policy = AudiencePolicy()
        self.policy.add_family_member("parent", "child")
        self.policy.add_trusted_contact("parent", "friend")
        self.gateway = CommunicationGateway(self.policy, lambda req: req.capability_id == "message.send")

    def test_family_is_not_trusted_contact_scope(self):
        family = AudienceRequest("parent", AudienceScope.FAMILY, ("child",), "family update", "message.send")
        friend = AudienceRequest("parent", AudienceScope.TRUSTED_CONTACTS, ("friend",), "personal update", "message.send")
        self.assertTrue(self.gateway.authorize(family).allowed)
        self.assertTrue(self.gateway.authorize(friend).allowed)

    def test_family_member_cannot_become_public_recipient(self):
        public = AudienceRequest("parent", AudienceScope.PUBLIC, ("child",), "public post", "message.send", requires_consent=True)
        self.assertFalse(self.gateway.authorize(public).allowed)

    def test_guardian_is_final_gate(self):
        gateway = CommunicationGateway(self.policy, lambda req: False)
        request = AudienceRequest("parent", AudienceScope.FAMILY, ("child",), "family update", "message.send")
        decision = gateway.authorize(request)
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason, "Guardian denied communication")

if __name__ == "__main__":
    unittest.main()
