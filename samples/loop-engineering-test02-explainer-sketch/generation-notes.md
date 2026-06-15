# Generation Notes

## Goal

Test whether the project can move closer to xiaohei-style explanatory sketches without losing Mr.Ai as the AI 闲僧 brand IP.

This round focused on code-level causes, not only visual taste.

## Code changes tested

- Added `--style explainer-sketch` to `bin/mrai`.
- Added explainer-specific layout rules:
  - `Checkpoint Rope`
  - `Feedback Leak`
  - `Decision Gates`
  - `Nested Rings`
  - `Evidence Clamp`
  - `Conveyor Split`
- Changed the prompt role from polished `brand illustration` to `whiteboard explanatory sketch`.
- Reduced Mr.Ai's intended canvas share.
- Made the physical metaphor the visual center.
- Shifted color guidance toward black marker linework with restrained blue/yellow/red accents.

## Visual comparison

Compared with the previous brand-mode `02-seven-step-loop-v1.png`, the new `02-checkpoint-rope-explainer-v1.png` is closer to the xiaohei method:

- Stronger whiteboard feeling.
- One dominant mechanism: a rope passing checkpoint signs.
- Mr.Ai is smaller and acts on the mechanism instead of becoming the main subject.
- Several blank cards remain available for post-production overlays.
- The image reads faster as a口播配图.

Remaining gap:

- Mr.Ai is still more polished and color-filled than xiaohei's black character.
- The blue rope is visually strong; useful for brand identity, but less minimal than xiaohei.
- The Chinese labels were correct in this run, but production should still prefer blank cards unless labels are essential.

`03-feedback-leak-explainer-v1.png` also moved in the right direction:

- The leak, state bucket, and magnifier make the "wrong feedback gets amplified" mechanism visible.
- It uses a single physical metaphor rather than a complex workflow diagram.
- It still draws Mr.Ai slightly large for explainer mode.

## Rule updates from this round

- In `explainer-sketch`, Mr.Ai should be about 10%-18% of a 16:9 canvas.
- Use mostly unfilled black line art.
- Avoid large filled color areas.
- Prefer blank label cards unless text accuracy is being explicitly tested.
- Keep the physical metaphor, not Mr.Ai, as the visual center.

## Candidate assets

- `16x9/02-checkpoint-rope-explainer-v1.png`: strong candidate for Loop Engineering explanation.
- `16x9/03-feedback-leak-explainer-v1.png`: useful risk/feedback metaphor, but needs a stricter small-character prompt for production.

