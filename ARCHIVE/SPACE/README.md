# SPACE ORGANISM ARCHIVE

Operational archive for the first SPACE organism.

## Current verification layers

- organism regression suite;
- graph integrity;
- memory persistence and graph memory;
- Guardian core and boundaries;
- feedback/cycle checks;
- capability/tool registry;
- stress/repetition runs;
- hardware boundary specification.

## Evidence

The latest recorded full-organism stress check is preserved in:
`01_HISTORY/ARCHITECTURE_AUDIT/2026-08-16-FULL-ORGANISM-STRESS-CHECK.md`

The architecture and hierarchy are documented in the SPACE architecture and hierarchy protocols under `space/` and `00_CORE/`.

## Capability audit rule

Every tool must eventually have four verified classes of behavior:

- normal input;
- invalid input;
- boundary input;
- recovery after rejection/failure.

A tool is not considered fully verified merely because it is registered or imported.

## External I/O rule

Network, Wi-Fi, Bluetooth, camera, microphone, sensors and other physical I/O remain `PHYSICAL_REQUIRED` until exercised on real hardware under Guardian policy.
