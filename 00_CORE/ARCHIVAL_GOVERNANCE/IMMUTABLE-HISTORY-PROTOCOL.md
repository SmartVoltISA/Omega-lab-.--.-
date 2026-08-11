# Ω-Lab — Immutable History & Open Review Protocol

## Purpose

Ω-Lab separates the historical record from later interpretation, criticism, correction, and extension.

The historical record MUST remain recoverable exactly as recorded. A later correction MUST NOT rewrite the earlier record.

## 1. Immutable historical layer

The following are historical artifacts:
- chat archives;
- original extracted statements;
- reported experiments;
- reported numerical results;
- failed attempts;
- errors and corrections;
- historical hypotheses;
- historical interpretations.

Historical files are append-only in meaning. If an error is discovered, the original file is not silently rewritten. A new correction or review artifact is created and linked to the original.

## 2. Public reading

The repository is public. Historical artifacts are intended to be readable without write access.

## 3. Review / criticism layer

External participants must NOT edit historical archives directly.

A participant may instead submit a separate contribution containing:
- claim or archive reference;
- objection, support, replication, question, or proposed correction;
- evidence;
- code/data where applicable;
- author/date information.

Recommended contribution statuses:
- QUESTION
- COMMENT
- SUPPORT
- CHALLENGE
- REPLICATION
- CORRECTION
- EXTENSION

## 4. Identity and provenance

Every substantive contribution SHOULD identify its author/account and date.

A contribution MUST NOT be represented as an Ω-Lab conclusion merely because it was submitted.

## 5. No silent deletion

Historical information MUST NOT be deleted merely because it was later rejected, disproved, superseded, or considered mistaken.

Instead:

`original → criticism/correction → new status`

The original remains part of the historical graph.

## 6. Status separation

The project should distinguish at least:

- HISTORICAL — recorded from an archive;
- REPORTED — claimed in the source but not independently verified;
- REPRODUCED — independently reproduced;
- CONFIRMED — supported by defined validation criteria;
- REFUTED — contradicted by a valid test;
- OPEN — unresolved;
- PROPOSED — not yet tested.

## 7. Technical immutability target

For the strongest protection, the historical layer should be protected at the GitHub repository level with:
- protected `main` branch;
- no direct pushes to the historical path;
- required review for changes;
- signed tags/releases for archive snapshots;
- periodic SHA-256 manifest of historical files;
- independent backup of signed snapshots.

Repository permissions and branch-protection settings are infrastructure controls and must be configured in GitHub; this document defines the required policy, not a claim that those controls are already enabled.

## 8. Snapshot principle

At defined milestones, create a signed archival snapshot:

`ARCHIVE-SNAPSHOT-YYYY-MM-DD`

The snapshot records:
- commit SHA;
- archive manifest;
- SHA-256 for each historical file;
- date;
- specification of the snapshot procedure.

A later snapshot may add files but must not alter the meaning of an earlier snapshot.

## 9. Open scientific review

The public review space is conceptually separate from the historical archive:

`HISTORY` — what was recorded

`REVIEW` — what people say about it

`EXPERIMENTS` — what is tested

`CONCLUSIONS` — what survives verification

This prevents criticism from destroying history and prevents historical claims from being mistaken for verified conclusions.

## 10. Core rule

> **History is evidence of what happened in the project, not a document that must agree with the current theory.**

A false result, failed experiment, rejected hypothesis, or mistaken interpretation is valuable historical information and remains preserved.

# END
