# Ω-Lab / Video Memory

This directory is the visual-memory layer for Ω-Lab and Life-Network.

## Purpose

Store finished videos, source manifests, visual experiments, and iteration notes so that future work can reference the actual visual language and previous results.

The archive is not merely a media folder. Each important visual experiment preserves the concept, geometry, physical behavior, camera behavior, defects, and revision logic.

## Structure

```text
media/
├── video/
│   ├── concepts/     # visual concepts and storyboards
│   ├── drafts/       # intermediate experiments
│   ├── approved/     # approved/final visualizations
│   └── archive/      # superseded versions kept for history
├── images/           # still references and generated images
├── diagrams/         # diagrams and visual schemas
└── references/       # external/reference visual material
```

## Workflow

`idea → storyboard → generation → render → review → revision → archive`

## Naming

Use:

`YYYY-MM-DD_<project>_<concept>_vNN.<ext>`

Example:

`2026-08-11_life-network_pencil_v03.mp4`

Never overwrite an approved version. New iterations receive a new version number.

## Visual memory rule

Every important video should have a companion `.md` manifest containing:

- concept;
- visual sequence;
- physical/geometric constraints;
- camera behavior;
- known defects;
- revision notes;
- source files/scripts when available.

## Life-Network visual rule

The core transformation is:

`connection → node → graph → structure → form → physical object`

The object should appear to emerge from organization of the network, not be drawn instantly on top of it.

For camera movement:

**the camera moves; the physical object does not rotate or stretch merely to create a camera effect.**

## Binary media note

The current GitHub connector available to this workspace can create/update UTF-8 text files, but does not expose a direct binary-file upload operation for MP4/PNG assets. Therefore binary assets should have text manifests here until a binary upload path is available.
