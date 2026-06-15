# Generation Notes

## Run

- Date: 2026-06-15
- Mode: built-in image generation
- Purpose: small sample calibration before expanding the template library

## Generated files

- `16x9/02-evidence-scale-v1.png`
- `9x16/03-validation-loop-v1.png`

## Observations

### 02-evidence-scale-v1.png

Strengths:

- Mr.Ai stayed visually consistent: cap, mustache, blue clothing, yellow accent, rounded cartoon face.
- Mr.Ai performs the action by placing cards on the scale.
- 16:9 framing leaves useful blank space.

Issues:

- The label `证据` appears twice.
- The logic reads as "more evidence cards equals pass" instead of "answer is checked against evidence".
- Exact Chinese text is good enough for a sample, but still risky for production.

Follow-up:

- Ask for fewer labels or blank label cards.
- Make the left side clearly `回答`, the right side clearly `证据`, and put `通过` outside the scale as a post overlay.

### 03-validation-loop-v1.png

Strengths:

- Mr.Ai stayed visually consistent.
- 9:16 composition is safe and readable.
- The blue thread makes the loop easy to understand.

Issues:

- `回答` was generated as `口答`.
- The layout is close to a formal flowchart.
- The concept is readable, but the exact text should be added in post-production for production use.

Follow-up:

- Prefer blank checkpoint cards for production.
- If labels are generated in-image, keep only `依据`, `检查`, `修正` or use very simple symbols.
- Push the scene toward physical checkpoint cards, not formal workflow boxes.

## Resulting documentation updates

- Strengthened prompt text policy in `agent-pack/prompt-template.md`.
- Added repeated-label and Chinese-text failure signals to `agent-pack/qa-checklist.md`.
- Synced the same changes to the Codex Skill references.

