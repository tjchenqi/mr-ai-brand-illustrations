# Generation Notes

## Run 1

- Date: 2026-06-15
- Mode: built-in image generation
- Source: `/Users/tjboss/Desktop/AI 闲僧/test04.md`
- Format focus: 9:16 vertical
- Purpose: test a standard S0/S1/S2口播稿 format and controlled in-image Chinese text

## Generated files

- `9x16/01-reweaving-two-songs-v1.png`
- `9x16/03-third-path-text-v1.png`
- `9x16/04-use-vs-rewrite-text-v1.png`

## Results

### 01-reweaving-two-songs-v1.png

Status: strong candidate usable.

Strengths:

- Best image of this run.
- Mr.Ai stays brand-consistent in 9:16.
- Reweaving metaphor is clear without using celebrity likeness or names.
- No text, safe for post-production overlays.

Issues:

- None severe.

Action:

- Keep as a positive vertical sample for cultural/person-story scripts.

### 03-third-path-text-v1.png

Status: candidate usable and positive text test.

Strengths:

- Three exact labels rendered correctly: `模仿`, `拒绝`, `改写`.
- The metaphor matches the script: not imitation, not rejection, but rewriting.
- Mr.Ai performs the core action.

Issues:

- The side symbol for `拒绝` is generic, but acceptable.

Action:

- Keep as the first positive example for controlled in-image Chinese labels.

### 04-use-vs-rewrite-text-v1.png

Status: usable text test, weaker visual sample.

Strengths:

- Two exact labels rendered correctly: `消费`, `改写`.
- Text is large and readable.
- Mr.Ai remains stable.

Issues:

- Composition is centered and explanatory, less memorable than the loom image.
- It feels closer to a simple explainer card than a distinctive Mr.Ai metaphor.

Action:

- Keep as a text reliability sample, not as the strongest visual sample.

## Text testing conclusion

Begin text testing after the blank-label strategy is stable.

Recommended ladder:

1. Generate a no-text image with blank label space.
2. Test 2-3 short labels on large physical signs.
3. Use exact quoted labels in the prompt.
4. Allow no other words.
5. If labels render correctly, keep the image; otherwise revert to blank labels plus post-production overlays.

