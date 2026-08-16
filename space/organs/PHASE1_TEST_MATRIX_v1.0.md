# Ω-Space — Organ Phase 1 Test Matrix v1.0

| Test | Expected invariant | Status |
|---|---|---|
| independent local state | A cannot mutate B state implicitly | defined |
| independent local memory | A and B do not share memory implicitly | defined |
| lifecycle isolation | stopping one organ does not stop another | defined |
| target validation | wrong target is rejected | defined |
| operation allow-list | unknown operation is rejected | defined |
| explicit message | communication requires an envelope | defined |
| capability boundary | message does not itself grant authority | next phase |
| quarantine | failed organ can be isolated | next phase |
| cycle/graph separation | organ communication cannot materialize protected graph | next phase |

Acceptance rule: no Phase 2 claim is made until the relevant CI checks are green.
