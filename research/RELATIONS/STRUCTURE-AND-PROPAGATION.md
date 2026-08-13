# Ω — Structure and Propagation

## A. Structure

A network is represented initially as:

`G = (V, E)`

where V are distinguishable states/nodes and E are relations.

We will progressively extend this to:

`G = (V, E, W, X)`

where W are edge weights and X are additional edge states/properties only when experimentally justified.

## B. Relation as an object

The edge may itself carry state:

`e_ij(t) = [w, k, l, A, V, rho, ...]`

This notation is intentionally provisional. It does not assert that all listed variables are independent or physical.

## C. Propagation

A change at node i can affect a neighboring node j through an edge. We will measure:

- propagation delay;
- number of updates required to reach distance d;
- attenuation;
- distortion;
- branching;
- reflection / return where the model permits it;
- dependence on edge properties.

## D. Candidate propagation law

A minimal discrete update model can be written:

`G_t -> G_(t+1)`

with local rules only.

A finite causal speed would appear if a disturbance cannot affect nodes beyond a bounded graph distance per update. This would be a model result, not evidence by itself for the physical speed of light.

## E. Frame/update hypothesis

A separate hypothesis proposes that a fundamental update interval plus a fundamental spatial scale could produce an effective limiting speed:

`v_max = L_update / dt_update`

or equivalently `v_max = L_update * f_update`.

This is dimensional bookkeeping at this stage, not a derivation of c.

## F. Propagation vs information

Do not assume that propagation means information is destroyed or preserved. Track separately:

1. state change;
2. transfer/correlation;
3. irreversible loss of recoverable information;
4. energy exchange.

## G. Relation-generated structure

A hypothesis to test later:

`persistent relation patterns -> stable nodes / structures`

This must compete against models where nodes are primitive.

## H. Research sequence

`one edge -> two edges -> path -> branching -> lattice/network -> dynamic network -> propagation limit`

At each step, attempt to remove the newly introduced property and test whether the observed phenomenon survives.
