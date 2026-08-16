# SPACE CAPABILITY AUDIT PROTOCOL v1.0

## Objective

Move from registry-level confidence to behavior-level verification for every executable SPACE capability.

## Test matrix

For each capability:

| Class | Required check |
|---|---|
| Normal | valid input produces the documented result |
| Invalid | malformed/unsupported input is rejected safely |
| Boundary | minimum/maximum/empty/large input behaves predictably |
| Recovery | after rejection/failure, state remains coherent and the organism continues |
| State | shared state is preserved and not silently diverged |
| Guardian | permission/trust boundary is enforced |
| Memory | consequential state/history is retained where required |
| Graph | node/edge relationships remain valid |
| Cycle | feedback can complete without uncontrolled recursion or state corruption |

## Tool lifecycle

`discover → invoke → observe → validate → record → repeat under load`.

A capability is `VERIFIED` only when all applicable rows have evidence. `REGISTERED` means only that it exists in the registry.

## External tools

For video/vision, do not mark the capability verified from documentation alone. Require an actual executable path and an image-input test. The test record must contain input provenance, preprocessing, response, errors, timing/resource observations if available, and the exact code revision.

## Hardware boundary

Wi-Fi, Bluetooth, camera, microphone, sensors, GPU-specific paths and other device I/O are tagged `PHYSICAL_REQUIRED` until tested on a real device.
