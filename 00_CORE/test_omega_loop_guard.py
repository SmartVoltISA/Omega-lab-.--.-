from omega_loop_guard import OmegaLoopGuard


def test_repetition_triggers_stop_and_replan():
    guard = OmegaLoopGuard(max_repetitions=3)
    kwargs = dict(
        state="electron search unresolved",
        action="continue searching the same direction",
        output="I continue searching for the result",
        evidence_delta=False,
        strategy_delta=False,
    )
    assert guard.observe(**kwargs).action == "CONTINUE"
    assert guard.observe(**kwargs).action == "WARN"
    assert guard.observe(**kwargs).action == "WARN"
    assert guard.observe(**kwargs).action == "STOP_REPLAN"


def test_new_evidence_breaks_loop():
    guard = OmegaLoopGuard(max_repetitions=2)
    kwargs = dict(
        state="same unresolved state",
        action="same action",
        output="same output",
        evidence_delta=False,
        strategy_delta=False,
    )
    guard.observe(**kwargs)
    guard.observe(**kwargs)
    decision = guard.observe(**{**kwargs, "evidence_delta": True})
    assert decision.action == "CONTINUE"
    assert guard.repetitions == 0


def test_strategy_change_breaks_loop_even_if_wording_is_similar():
    guard = OmegaLoopGuard(max_repetitions=2)
    kwargs = dict(
        state="same unresolved state",
        action="search literature",
        output="no result yet",
        evidence_delta=False,
        strategy_delta=False,
    )
    guard.observe(**kwargs)
    guard.observe(**kwargs)
    decision = guard.observe(**{**kwargs, "action": "run simulation", "strategy_delta": True})
    assert decision.action == "CONTINUE"


def test_wording_change_alone_does_not_count_as_progress():
    guard = OmegaLoopGuard(max_repetitions=2)
    guard.observe(
        state="same state", action="same action", output="continue searching",
        evidence_delta=False, strategy_delta=False,
    )
    decision = guard.observe(
        state="same state", action="same action", output="I will keep looking for an answer",
        evidence_delta=False, strategy_delta=False,
    )
    assert decision.action in {"WARN", "STOP_REPLAN"}
