# EXP-C1-021 — Magic-Square Protocol / Key → Challenge → Next Node

**Status:** STRONG STRUCTURAL RESULT; endpoint mechanism beyond this stage remains UNKNOWN.
**Date:** 2026-08-28

## Verified chain

1. The 2014 portrait exposes two number columns.
2. Left column: 181, 7, 15, 16, 456, 351, 7 → sum **1033**.
3. Right column: 966, 1071, 626, 204, 434 → sum **3301**.
4. The operational OpenPuff password is **33011033**, i.e. right-column sum followed by left-column sum. The historical walkthrough explicitly records this password and the extracted file.
5. OpenPuff v4.00 extracts `magicsquares.txt`, containing exactly three squares: 5×5 with constant 3301, 7×7 with constant 1033, and 5×5 with constant 1033.
6. The 5×5 / 1033 square is reproduced in Liber Primus and in earlier OOB material.
7. The subsequent challenge asks participants to submit the three squares plus a URL to their own Tor hidden service; successful submission returns further Liber Primus pages.

## Important conclusion

3301 and 1033 are not merely coincidental numbers. They participate in an operational transition:

visible numeric columns → sums → ordered concatenation → steganographic password → hidden artifact → three magic-square constraints → participant endpoint → next pages.

The ordering **3301 || 1033** is empirically operational in this transition. Do not infer a universal `3301→1033` mathematical transformation from it.

## Graph interpretation

This is a concrete example of a typed edge sequence:

`numbers --SUM--> invariants --CONCAT/ORDER--> password --UNLOCKS--> artifact --CONTAINS--> constraints --VALIDATES--> endpoint --RETURNS--> next nodes`

The repeated 1033 matrix is therefore a cross-channel bridge, not merely a decorative square.

## What remains UNKNOWN

- Why the ordering is 3301 then 1033 beyond the observed operational rule.
- Whether the same construction is reused later in LP2.
- Whether 3301/1033 encode a domain, real-world coordinate, or cryptographic key elsewhere.
- Whether a general transition function exists across all Cicada stages.

## Next falsifiable test

Search later stages for the same pattern:
`visible numeric structures → invariant(s) → ordered concatenation → operational key/identifier → next artifact`.
A second independently verified instance would elevate the protocol from local mechanism to recurring architectural rule.
