# Resource Contract Repair — 2026-08-16

## Finding
Full SPACE organism CI reduced the previous failures to one failure in the habitat resource boundary.

The failing test called `request("compact", 4)` while the ResourceManager compact contract is defined as `(resource_id, amount)`. The registered resource was `ram`.

## Repair
The regression test was corrected to use the declared compact contract: `request("ram", 4)`.

No resource-allocation semantics were weakened or bypassed. The explicit and compact forms continue to converge on the same resource state.

## Invariant
`compact(resource_id, amount)` and `explicit(claim_id, owner, resource_id, amount, unit)` must produce compatible claims against the same resource ledger.

## Verification
The repair is not VERIFIED until the next full `space-organism` CI run passes and the related graph/memory/Guardian/component checks remain green.

## Structural chain
`node → edge → graph → cycle → memory → Guardian → feedback → resource state → organism → CI`
