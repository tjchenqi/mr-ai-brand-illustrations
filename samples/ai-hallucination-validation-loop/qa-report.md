# QA Report

## Package-level checks

- Character consistency: prompts repeatedly lock cap, mustache, blue clothing, yellow accent, rounded middle-aged cartoon identity.
- Concept clarity: each shot explains one idea only.
- Text safety: every image uses 3-4 short Chinese labels.
- Format safety: each shot includes separate 16:9 and 9:16 prompts.
- Brand fit: Mr.Ai is a practical AI explainer, not a monk, robot, or generic presenter.
- Remotion compatibility: prompts reserve safe space for later overlays.

## Shot checks

### 01-answer-is-not-evidence

- Strength: strong misconception correction.
- Risk: "不等于" text may render poorly.
- Repair: if text fails, replace with a simple gap/cross mark and add label in post-production.

### 02-evidence-scale

- Strength: verification becomes a physical action.
- Risk: too many small cards may create clutter.
- Repair: keep only one answer card and two evidence cards.

### 03-validation-loop

- Strength: workflow is clear and reusable.
- Risk: could become too flowchart-like.
- Repair: make checkpoint boxes hand-drawn physical blocks and keep Mr.Ai pulling the thread.

### 04-black-box-to-toolchain

- Strength: strong closing metaphor.
- Risk: "toolchain" modules could become a software architecture diagram.
- Repair: keep modules as simple physical blocks and emphasize Mr.Ai connecting a cable.

## Dry-run conclusion

The current agent-pack can produce a usable script-to-shot package without needing image generation. The next iteration should test one or two prompts with an image model and update the QA checklist with observed drift patterns.

