"""Executable proof for Ω-PRESENT-1."""

import unittest

from current_state import CurrentState, transition
from memory_present_link import MemoryPresentLedger


class CurrentStateTests(unittest.TestCase):
    def test_minimal_state_is_distinct_from_future_intent(self):
        state = CurrentState.create(
            cycle_id="cycle-001", status="testing",
            active_work=["present-model"], active_organs=["MEMORY", "PRESENT"],
            available_data=["state-schema"], missing_data=["verification-result"],
        )
        self.assertEqual(state.status, "testing")
        self.assertIn("verification-result", state.missing_data)
        self.assertFalse(hasattr(state, "desired_state"))
        self.assertFalse(hasattr(state, "candidate_actions"))

    def test_transition_is_append_only(self):
        state0 = CurrentState.create(cycle_id="cycle-001", status="testing", known={"version": 1})
        state1, edge = transition(state0, status="verified", known={"version": 2}, last_result={"outcome": "pass"})
        self.assertNotEqual(state0.state_id, state1.state_id)
        self.assertEqual(edge.predecessor_id, state0.state_id)
        self.assertEqual(edge.successor_id, state1.state_id)
        self.assertEqual(state0.status, "testing")
        self.assertEqual(state0.known["version"], 1)
        self.assertEqual(state1.status, "verified")
        self.assertEqual(state1.known["version"], 2)
        self.assertEqual(state1.last_result["outcome"], "pass")

    def test_memory_present_round_trip_preserves_history(self):
        state0 = CurrentState.create(cycle_id="cycle-001", status="start", known={"n": 0})
        state1, _ = transition(state0, status="middle", known={"n": 1})
        state2, _ = transition(state1, status="done", known={"n": 2})
        ledger = MemoryPresentLedger()
        for state in (state0, state1, state2):
            ledger.append(state)
        ledger.link(state0, state1)
        ledger.link(state1, state2)
        restored = ledger.reconstruct(state0.state_id, state2.state_id)
        self.assertEqual(restored.state_id, state2.state_id)
        self.assertEqual(restored.known["n"], 2)
        self.assertEqual(state0.known["n"], 0)
        self.assertEqual(len(ledger.events), 2)

    def test_ledger_rejects_overwrite(self):
        state = CurrentState.create(cycle_id="cycle-001", status="start")
        ledger = MemoryPresentLedger()
        ledger.append(state)
        with self.assertRaises(ValueError):
            ledger.append(state)

    def test_unsupported_future_field_is_rejected(self):
        state = CurrentState.create(cycle_id="cycle-001", status="idle")
        with self.assertRaises(ValueError):
            transition(state, desired_state="done")


if __name__ == "__main__":
    unittest.main()
