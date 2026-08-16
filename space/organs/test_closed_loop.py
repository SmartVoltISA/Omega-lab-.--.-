import unittest

from space.organs.autonomous_organ import AutonomousOrgan
from space.organs.causal_memory import CausalMemory
from space.organs.organ_closed_loop import OrganClosedLoop


class ClosedLoopTests(unittest.TestCase):
    def test_event_action_result_evaluation_memory_and_state_close_the_loop(self):
        organ = AutonomousOrgan("counter")
        organ.register_operation("increment", lambda payload: int(payload) + 1)
        loop = OrganClosedLoop(organ)

        result = loop.run_once(
            event="input:1",
            action="increment",
            payload=1,
            evaluate=lambda value: "good" if value == 2 else "bad",
        )

        self.assertEqual(result.result, 2)
        self.assertEqual(result.evaluation, "good")
        self.assertEqual(loop.memory.last().record_id, result.record_id)
        self.assertEqual(organ.state["last_event"], "input:1")
        self.assertEqual(organ.state["last_action"], "increment")
        self.assertEqual(organ.state["last_evaluation"], "good")

    def test_previous_result_can_influence_next_step_without_shared_memory(self):
        organ = AutonomousOrgan("adaptive")
        organ.register_operation("step", lambda payload: payload + 1)
        loop = OrganClosedLoop(organ, CausalMemory())

        first = loop.run_once("e1", "step", 1)
        next_payload = first.result
        second = loop.run_once("e2", "step", next_payload)

        self.assertEqual(first.result, 2)
        self.assertEqual(second.result, 3)
        self.assertEqual(len(loop.memory.records), 2)
        self.assertEqual(len(organ.memory), 2)

    def test_loop_has_no_graph_api(self):
        organ = AutonomousOrgan("isolated")
        organ.register_operation("noop", lambda payload: payload)
        loop = OrganClosedLoop(organ)
        loop.run_once("e", "noop", "x")
        self.assertFalse(hasattr(loop, "graph"))
        self.assertFalse(hasattr(loop, "graph_core"))

    def test_stopped_organ_breaks_execution_without_corrupting_memory(self):
        organ = AutonomousOrgan("guarded")
        organ.register_operation("noop", lambda payload: payload)
        memory = CausalMemory()
        loop = OrganClosedLoop(organ, memory)
        organ.stop()
        with self.assertRaises(RuntimeError):
            loop.run_once("e", "noop", "x")
        self.assertEqual(len(memory.records), 0)


if __name__ == "__main__":
    unittest.main()
