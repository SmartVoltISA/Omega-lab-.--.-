import unittest

from space.organs import (
    NervousSystem, CirculatorySystem, SensorySystem, MotorSystem,
    DigestiveSystem, Habitat, ImmuneSystem,
)

class TestOrgans(unittest.TestCase):
    def test_nervous_priority_and_dispatch(self):
        nervous = NervousSystem()
        seen = []
        nervous.connect("X", lambda signal: seen.append(signal.payload))
        nervous.emit("X", "test", "low", priority=50)
        nervous.emit("X", "test", "high", priority=10)
        self.assertEqual(nervous.dispatch_all(), 2)
        self.assertEqual(seen, ["high", "low"])

    def test_circulation(self):
        system = CirculatorySystem()
        system.register("cpu", 10)
        self.assertTrue(system.consume("cpu", 3))
        self.assertEqual(system.resources["cpu"].available, 7)
        self.assertFalse(system.consume("cpu", 8))

    def test_sense_and_motor_boundaries(self):
        sensory = SensorySystem()
        sensory.register("text", lambda: "hello")
        observation = sensory.read("text")
        self.assertEqual(observation.payload, "hello")

        motor = MotorSystem()
        output = []
        motor.register("display", output.append)
        self.assertFalse(motor.execute("display", "blocked").committed)
        self.assertEqual(output, [])
        self.assertTrue(motor.execute("display", "shown", authorized=True).committed)
        self.assertEqual(output, ["shown"])

    def test_digest_without_backend_is_explicit(self):
        digest = DigestiveSystem().digest("in-1", "test", [])
        self.assertFalse(digest.accepted)
        self.assertEqual(digest.interpretation["status"], "NO_LLM_BACKEND")

    def test_habitat(self):
        habitat = Habitat("host-1", "linux", "x86_64")
        habitat.expose_interface("display")
        habitat.register_device("screen-1", "monitor")
        self.assertIn("display", habitat.interfaces)
        self.assertEqual(habitat.devices["screen-1"]["kind"], "monitor")

    def test_immune_quarantine(self):
        immune = ImmuneSystem()
        immune.add_rule(lambda source, evidence: "HIGH" if evidence == "bad" else None)
        self.assertEqual(len(immune.inspect("tool", "bad")), 1)
        immune.quarantine("tool")
        self.assertTrue(immune.is_quarantined("tool"))

if __name__ == "__main__":
    unittest.main()
