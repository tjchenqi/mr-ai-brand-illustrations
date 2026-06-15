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

Generated three 9:16 images:

- `9x16/01-reweaving-two-songs-v1.png`: strong candidate usable.
- `9x16/03-third-path-text-v1.png`: candidate usable and positive text test.
- `9x16/04-use-vs-rewrite-text-v1.png`: usable text reliability sample, weaker visual sample.

Takeaways:

- Standard S0/S1/S2口播稿 structure is easy for CLI packaging.
- Cultural/person-story scripts need manual visual direction; generic AI workflow layouts are not enough.
- Controlled Chinese text can work when limited to 2-3 short labels on clear sign plates.
- No-text metaphor images remain safer and more visually elegant.
