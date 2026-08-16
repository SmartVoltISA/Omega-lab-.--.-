import unittest

from space.habitat.resource_manager import ResourceManager
from space.habitat.guardian_io import GuardianIO, IORequest
from space.habitat.space_transport import SpaceMessage, SpaceTransport

class HabitatBoundaryTests(unittest.TestCase):
    def test_resource_allocation_and_release(self):
        rm = ResourceManager()
        rm.register("ram", "RAM", 16)
        self.assertTrue(rm.request("ram", 4))
        self.assertEqual(rm.available("ram"), 12)
        rm.release("ram", 2)
        self.assertEqual(rm.available("ram"), 14)
        self.assertFalse(rm.request("ram", 20))

    def test_resource_explicit_and_compact_contracts_share_state(self):
        rm = ResourceManager()
        rm.register("ram", "RAM", 16, "GB")
        # Compact contract is (resource_id, amount); both contracts must
        # address the same registered resource and therefore share state.
        self.assertTrue(rm.request("ram", 4))
        self.assertTrue(rm.request("explicit", "space", "ram", 3, "GB"))
        self.assertEqual(rm.available("ram"), 9)
        self.assertTrue(rm.release("ram", 2))
        self.assertEqual(rm.available("ram"), 11)

    def test_external_io_requires_guardian(self):
        io = GuardianIO(lambda req: req.capability_id == "wifi.send")
        sent = []
        io.register_adapter("wifi", lambda op, payload: sent.append((op, payload)) or "ok")
        allowed = io.execute(IORequest("1", "wifi", "send", "wifi.send", "hello", "out"))
        denied = io.execute(IORequest("2", "wifi", "send", "wifi.send.blocked", "no", "out"))
        self.assertTrue(allowed.allowed)
        self.assertFalse(denied.allowed)
        self.assertEqual(sent, [("send", "hello")])

    def test_space_transport_requires_authorization(self):
        transport = SpaceTransport(lambda msg: msg.receiver == "space-b")
        received = []
        transport.register_peer("space-b", lambda msg: received.append(msg.payload) or "ack")
        msg = SpaceMessage("m1", "space-a", "space-b", "peer.call", {"x": 1}, "c1", 1)
        self.assertEqual(transport.send(msg), "ack")
        self.assertEqual(received, [{"x": 1}])
        transport.authorize = lambda msg: False
        with self.assertRaises(PermissionError):
            transport.send(msg)

if __name__ == "__main__":
    unittest.main()
