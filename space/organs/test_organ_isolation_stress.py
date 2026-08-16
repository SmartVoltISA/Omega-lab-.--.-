import unittest

from space.organs.autonomous_organ import AutonomousOrgan


class OrganIsolationStressTests(unittest.TestCase):
    def test_repeated_local_work_does_not_cross_memory(self):
        organs = [AutonomousOrgan(f"organ-{i}") for i in range(8)]
        for organ in organs:
            organ.register_operation("tick", lambda payload: payload + 1)

        for round_no in range(100):
            for organ in organs:
                self.assertEqual(organ.handle_local("tick", round_no), round_no + 1)

        self.assertEqual([len(o.memory) for o in organs], [100] * 8)
        for i, organ in enumerate(organs):
            for other in organs[:i] + organs[i + 1:]:
                self.assertIsNot(organ.memory, other.memory)

    def test_stopping_one_organ_does_not_stop_the_pool(self):
        organs = [AutonomousOrgan(f"organ-{i}") for i in range(16)]
        organs[7].stop()
        active = [o for o in organs if o.running]
        self.assertEqual(len(active), 15)
        for organ in active:
            organ.register_operation("health", lambda _: "ok")
            self.assertEqual(organ.handle_local("health"), "ok")

    def test_messages_do_not_execute_without_a_dispatcher(self):
        source = AutonomousOrgan("source")
        message = source.make_message("target", "run", "payload")
        self.assertEqual(message.target, "target")
        self.assertFalse(hasattr(message, "execute"))


if __name__ == "__main__":
    unittest.main()
