# Ω-Lab — External Read-Only Archive Policy

## Purpose

The Ω-Lab historical archive is public for reading and research, but the historical source itself is not a public editing surface.

## External access

External visitors may:
- read the archive;
- download and copy it;
- fork or mirror it;
- analyse it;
- quote and cite it;
- build independent graphs and interpretations;
- reproduce experiments;
- submit criticism, support, questions, corrections, and refutations through the designated review layer.

External visitors may not:
- modify historical archive files;
- rewrite an archived conversation;
- silently replace an archived result;
- delete historical records;
- alter the historical record through review material.

## Corrections

A discovered error is recorded as a new document linked to the original archive. The original archive is retained unchanged as historical evidence.

Pattern:

`HISTORY/023` → `REVIEW/023/CORRECTION-001`

The review/correction layer may change as new evidence arrives; the historical source does not.

## Review model

The archive is read-only; scientific participation happens beside it:

- QUESTIONS
- CRITICISM
- SUPPORT
- REPLICATIONS
- REFUTATIONS
- CORRECTIONS

A disagreement does not overwrite the source. It creates a new trace connected to the source.

## Integrity principle

> The archive cannot be corrected by rewriting history. It can only be challenged, supported, reproduced, or contextualized by new records.

## Current implementation note

GitHub repository permissions and branch protection are implementation mechanisms, not part of the scientific content. The desired operational state is public read access with no write access for external participants to the historical archive path/branch.

Where stronger immutability is required, signed releases/tags and independent hash manifests should be added so historical snapshots can be verified outside the live repository.

# END
