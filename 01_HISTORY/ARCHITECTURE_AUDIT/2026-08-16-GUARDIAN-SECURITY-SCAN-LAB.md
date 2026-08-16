# Guardian Security Scan Lab — 2026-08-16

## Change
Added a defensive security-scan boundary for Guardian.

## Runtime
- `space/security/security_scan_lab.py`
- quarantine copy is explicit;
- SHA-256 evidence is generated;
- metadata-only mode never executes artifacts;
- optional antivirus executable is invoked only as a read-only scanner;
- no promote/execute capability is exposed by the lab object.

## CI
Added `.github/workflows/security-scan-lab.yml` with dedicated regression tests.

## Boundary
The laboratory is defensive and isolated. A clean scan is evidence only; Guardian remains the authority for promotion or rejection.

## Verification status
Implementation committed. CI/hardware verification remains a separate evidence step. Do not mark the physical antivirus engine as verified until it is exercised in the target habitat.
