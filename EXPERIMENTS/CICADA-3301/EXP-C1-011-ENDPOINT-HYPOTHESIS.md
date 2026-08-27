# EXP-C1-011 — Endpoint / Signed-Key Hypothesis

## Question
Could Liber Primus be an encoded algorithm whose terminal output is a signed key, domain/onion address, or real-world location rather than merely plaintext?

## Evidence

1. Page 56/57 is reported to decode to an explicit terminal instruction: a deep-web page is identified by a SHA-512 hash and the pilgrim is instructed to seek it.
2. The hash therefore behaves like an endpoint commitment, not ordinary prose.
3. The historical Cicada chain repeatedly moved from text -> cryptographic material -> hidden service / physical location.
4. Authentic Cicada communications were PGP-signed; therefore a future endpoint should be distinguished from an unsigned imitation.

## Status
**PLAUSIBLE — strong structural hypothesis, not proven.**

## Critical distinction
A SHA-512 digest does not itself encode a domain name or geographic coordinate. It is a commitment/check value. To recover an endpoint, the puzzle must provide an additional mapping, candidate object, or search space whose hash can be tested.

## Experimental plan

### E1 — Hash-space audit
Collect every endpoint-like artifact from 2012–2014 and every candidate onion/domain/address appearing in the recovered chains. Test exact SHA-512 matching against the P56/P57 digest. Do not accept prefix or fuzzy matches.

### E2 — Signed-key relation
For every candidate terminal message, verify PGP signature against the known Cicada public key. Treat unsigned matches as UNKNOWN regardless of textual quality.

### E3 — Address encoding families
Test only deterministic encodings suggested by the corpus: prime indices, Gematria values, Fibonacci/Lucas indices, book-cipher coordinates, QR payloads, and known page numbers. Avoid arbitrary brute-force wordlists.

### E4 — Real-world endpoint
Reconstruct the 2012 physical-coordinate stage and test whether later numerical structures reuse the same coordinate encoding. A geographic interpretation requires independent confirmation from a known historical coordinate.

### E5 — Negative controls
For every hash/address hypothesis generate matched random candidates. A method that produces equally good matches is rejected.

## Key research principle
The terminal plaintext may be an **instruction to obtain the key**, not the key itself. Therefore solving Liber Primus textually is not equivalent to completing Cicada.

## Current conclusion
The user's hypothesis is compatible with the strongest surviving evidence: the known end-stage text explicitly points toward a hashed deep-web endpoint. The exact endpoint and the mechanism that maps Liber Primus to it remain UNKNOWN.
