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

Generated three images from the package:

- `16x9/01-black-box-reveal-v1.png`: candidate usable.
- `16x9/02-toolchain-thread-v1.png`: candidate usable.
- `9x16/04-emotion-reversal-v1.png`: boundary sample, not recommended for final handoff.

Takeaways:

- Blank label cards are working better than generated Chinese labels.
- Mr.Ai character consistency is strong.
- Robot icons can appear when the prompt mentions AI toolbox; avoid robot icons/faces in production prompts.
- For 耿鬼 handoff, include selected useful images and notes, not all raw attempts.
