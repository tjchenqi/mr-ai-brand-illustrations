# QA Report

## Package-level checks

- Character consistency: pending generated images.
- Concept clarity: review every shot before generation.
- Timeline fit: check `timeline-plan.md` before image generation.
- Text safety: prefer blank label cards or 1-3 short labels.
- Format safety: both 16:9 and 9:16 prompts created.
- Brand fit: pending generated images.

## Known risks

- This CLI uses deterministic routing rules; an agent should refine the shot choices.
- Production default is blank in-image labels; add exact Chinese in post-production.
- Workflow layouts can drift toward formal PPT diagrams, equations, or three-box slides.
- Explainer-sketch layouts can drift back into polished brand posters if Mr.Ai is too large or the props are too detailed.
- S/B parsing is deterministic; review whether B segments should be quote cards, overlays, or skipped.
