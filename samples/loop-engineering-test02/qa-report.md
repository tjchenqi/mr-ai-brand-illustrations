# QA Report

## Package-level checks

- Character consistency: pending generated images.
- Concept clarity: review every shot before generation.
- Text safety: prefer blank label cards or 1-3 short labels.
- Format safety: both 16:9 and 9:16 prompts created.
- Brand fit: pending generated images.

## Known risks

- This CLI uses deterministic heuristics; an agent should refine the shot choices.
- Chinese labels may be duplicated or corrupted by image models.
- Workflow layouts can drift toward formal PPT diagrams.

## Run 1 image calibration

Generated three images:

- `16x9/01-three-layers-v1.png`: candidate usable.
- `16x9/02-seven-step-loop-v1.png`: strong candidate usable.
- `16x9/04-error-feedback-loop-v1.png`: candidate usable for risk/guardrail concepts.

Takeaways:

- Dense technical scripts can still produce strong Mr.Ai images if prompts use physical props.
- Blank label cards are clearly better than generated Chinese text.
- The best current positive pattern is `Mr.Ai + workbench + physical loop tokens`.
- CLI-generated shot lists for long prose need agent review; the CLI is a package generator, not the final visual director.
