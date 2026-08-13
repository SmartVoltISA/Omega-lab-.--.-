# Ω-Lab — Evidence & Fact Verification Protocol

## Purpose

This protocol is mandatory for experimental claims in Ω-Lab.

**No fact without evidence. No result without execution. No interpretation presented as a fact.**

The project prefers a small verified step over a large unverified conclusion.

## 1. Minimal-step rule

Every investigation must proceed as:

`minimum premise → minimum intervention → execution → verification → observation → next step`

Do not increase model complexity, n-gram order, parameter count, or theoretical scope while the current step contains an unresolved methodological uncertainty that can be tested first.

## 2. Evidence states

Every experiment and every numerical claim must have an explicit state:

- **PLANNED** — protocol exists; no execution.
- **CODED** — implementation exists; no verified execution.
- **EXECUTED** — implementation was actually run and execution evidence is archived.
- **VALIDATED** — execution result passed independent checks/tests and its provenance is recorded.
- **REPRODUCED** — an independent rerun reproduced the relevant result.
- **REJECTED** — run failed, was incomplete, or contains an unresolved methodological defect.
- **INVALIDATED** — a previously reported result was later shown not to be supported by the evidence.

Only **EXECUTED** results may be described as experimental results. Only **VALIDATED** or **REPRODUCED** results may be used as strong evidence in subsequent conclusions.

## 3. Fact gate

Before writing any sentence containing a numerical or empirical claim, verify:

1. Where did the number come from?
2. What exact code or procedure produced it?
3. Was that code actually executed?
4. Where is the raw output or execution record?
5. Were the invariants checked?
6. Were tests passed?
7. Can another run reproduce the claim?

If any required answer is unknown, the statement must be downgraded to an explicit hypothesis, expectation, or unverified claim.

Never fill a missing fact with a plausible value.

## 4. Execution evidence

Whenever technically possible, archive:

- exact source revision / commit SHA;
- execution timestamp;
- command or workflow used;
- runtime/environment information;
- seed(s);
- raw output;
- exit status;
- test output;
- generated result files.

A source file existing in GitHub is **not** evidence that it was executed.

A result file existing in GitHub is **not by itself** proof that its generating code was executed. Its provenance must be traceable.

## 5. Separation of layers

Every report must distinguish:

**FACT** — directly supported by archived evidence.

**OBSERVATION** — what the executed procedure measured.

**INTERPRETATION** — a proposed explanation.

**HYPOTHESIS** — a claim requiring further testing.

**UNKNOWN** — information not established by the current evidence.

These labels must not be collapsed into one another.

## 6. Adversarial check

After an interesting result, attempt to break it before expanding the theory.

Test at least one plausible alternative explanation where practical:

- implementation artifact;
- sampling artifact;
- metric artifact;
- seed dependence;
- data-selection artifact;
- parameter dependence;
- baseline failure;
- accidental leakage or invalid control.

If a result breaks, preserve the failed result and record the cause.

## 7. No retrospective repair

Completed experiments are immutable historical records.

If an error is found later:

- do not silently edit the old result;
- mark it as rejected/invalidated;
- create a corrected replication or new experiment;
- record the correction and reason in `HISTORY.md`.

## 8. Minimum-value discipline

Prefer the smallest claim that the evidence supports.

Example:

Bad:
> "We discovered where information is stored."

Acceptable:
> "In this finite test, sequences with the same measured local statistics produced different zlib sizes under the tested reconstruction procedure."

The second statement is deliberately narrower because it is closer to the evidence.

## 9. Stop condition

If an execution environment cannot be verified, do not simulate the missing execution mentally and do not report expected output as observed output.

State plainly:

> **Execution not verified. No experimental result claimed.**

Then either obtain a real execution path or stop at the coded/protocol stage.

## 10. Golden rule

> **Факт без проверки — не факт. Код без запуска — не результат. Результат без воспроизводимости — только предварительное наблюдение. Гипотеза никогда не становится фактом от того, что хорошо звучит.**
