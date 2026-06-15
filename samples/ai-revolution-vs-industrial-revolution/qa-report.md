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
