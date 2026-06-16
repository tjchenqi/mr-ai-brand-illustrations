# Reviewed Results Spec

This is the V1.1.3 manual QA bridge for B-side production.

The CLI keeps generated records conservative: successful provider output defaults to `qa_status=needs_human_review` and `usable=false`. B can create a separate `reviewed.json` after visual QA, without editing `results.json` directly.

## File Location

Write the file next to `results.json`:

```text
samples/<topic>/reviewed.json
```

## Schema

```json
{
  "job_id": "abc123",
  "reviewed_at": "2026-06-16T12:00:00Z",
  "reviewer": "genggui",
  "items": [
    {
      "s_id": "S01",
      "version": 1,
      "qa_status": "pass",
      "usable": true,
      "notes": "Character close enough; no bitmap text."
    }
  ]
}
```

## Review Rules

- `pass`: image can enter Remotion.
- `warning`: image can enter a prototype only, with a note.
- `failed`: image must not enter Remotion.
- `needs_human_review`: default machine state before B review.

Mark `usable=true` only when:

- Mr.Ai identity is acceptable.
- No Chinese, English, fake text, numbers, or watermark-like marks appear in the bitmap.
- Composition leaves enough room for Remotion overlays.
- The image matches the intended S segment.

Mark `usable=false` when:

- Subject reference failed.
- The image was generated through no-reference fallback.
- Mr.Ai is redesigned as a different character.
- Any in-image text appears.
- The character is pushed to an unusable edge/corner.

## Remotion Rule

B-side Remotion pipelines should prefer `reviewed.json` when present and use only `usable=true` items. If `reviewed.json` is absent, treat `results.json` as unreviewed and avoid production rendering.
