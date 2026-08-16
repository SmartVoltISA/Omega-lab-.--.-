import unittest

from space.organs.autonomous_organ import AutonomousOrgan


class AutonomousOrganTests(unittest.TestCase):
    def test_organ_is_self_sufficient(self):
        organ = AutonomousOrgan("vision")
        organ.state["mode"] = "local"
        organ.register_operation("observe", lambda payload: {"seen": payload})
        self.assertEqual(organ.handle_local("observe", "x"), {"seen": "x"})
        snapshot = organ.snapshot()
        self.assertEqual(snapshot["organ_id"], "vision")
        self.assertEqual(snapshot["operations"], ["observe"])
        self.assertEqual(len(snapshot["memory"]), 1)

    def test_unknown_operation_is_rejected(self):
        organ = AutonomousOrgan("audio")
        with self.assertRaises(PermissionError):
            organ.handle_local("network_send", "x")

    def test_interorgan_message_is_only_an_envelope(self):
        organ = AutonomousOrgan("vision")
        message = organ.make_message("audio", "request_transcription", "hello", "audio.read")
        self.assertEqual(message.source, "vision")
        self.assertEqual(message.target, "audio")
        self.assertEqual(message.operation, "request_transcription")
        self.assertEqual(message.capability, "audio.read")
        self.assertFalse(hasattr(message, "execute"))

    def test_self_target_is_rejected(self):
        organ = AutonomousOrgan("vision")
        with self.assertRaises(ValueError):
            organ.make_message("vision", "observe")

    def test_one_organ_failure_does_not_change_another(self):
        a = AutonomousOrgan("a")
        b = AutonomousOrgan("b")
        a.stop()
        self.assertFalse(a.running)
        self.assertTrue(b.running)
        b.register_operation("health", lambda _: "ok")
        self.assertEqual(b.handle_local("health"), "ok")

    def test_local_memory_is_not_shared_implicitly(self):
        a = AutonomousOrgan("a")
        b = AutonomousOrgan("b")
        a.memory.append({"secret": "local"})
        self.assertEqual(b.memory, [])
        self.assertIsNot(a.memory, b.memory)


if __name__ == "__main__":
    unittest.main()
