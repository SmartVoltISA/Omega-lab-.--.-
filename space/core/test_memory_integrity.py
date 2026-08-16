import unittest

from space.core.memory import DistributedMemory

class MemoryIntegrityTests(unittest.TestCase):
    def test_history_verifies(self):
        memory = DistributedMemory()
        memory.remember("space", "observation", {"x": 1}, "sensor", 0)
        memory.remember("space", "feedback", {"y": 2}, "tool", 1)
        self.assertTrue(memory.verify_integrity())

    def test_mutation_is_detected(self):
        memory = DistributedMemory()
        memory.remember("space", "observation", {"x": 1}, "sensor", 0)
        memory.remember("space", "feedback", {"y": 2}, "tool", 1)
        memory._traces["mem-1"] = memory._traces["mem-1"].__class__("mem-1", "space", "observation", {"x": 999}, "sensor", memory._traces["mem-1"].created_at, 0)
        self.assertFalse(memory.verify_integrity())

if __name__ == "__main__":
    unittest.main()
