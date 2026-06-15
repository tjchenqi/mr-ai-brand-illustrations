# Adaptation Decisions

## Decision 1: Build a brand illustration system

This project is not a character replacement of the upstream skill. It is a dedicated Mr.Ai illustration system for AI 闲僧.

Reason:

- The user needs a reusable IP asset system for a video column.
- Mr.Ai has mandatory brand traits.
- Future samples and templates will become project assets.

## Decision 2: Use agent-pack as the source of truth

The core reusable knowledge lives in `agent-pack/`. Tool-specific wrappers such as Codex Skill and OpenClaw instructions should point back to the same core rules.

Reason:

- The project should work across agents.
- Brand rules should not drift between tools.

## Decision 3: Keep generated image text short

Generated images should contain only short labels. Long subtitles and full explanations belong to video editing, Remotion, or design overlay layers.

Reason:

- Chinese text in image models is unstable.
- Video production already has better subtitle systems.
- Short labels keep the image reusable across cuts.

## Decision 4: Treat Remotion as optional

The system may output `remotion-overlay-notes.md`, but it should not require Remotion to be useful.

Reason:

- Other agents, such as a voiceover plus image-carousel agent, should be able to use the outputs directly.
- The initial project scope is illustration planning and image prompt generation.

## Decision 5: Do not redistribute upstream example images

The project records upstream file inventory and analysis but does not include Xiaohei example images as assets.

Reason:

- Mr.Ai needs its own sample library.
- Upstream images are style calibration examples for a different IP.
- Avoid accidental visual copying.

