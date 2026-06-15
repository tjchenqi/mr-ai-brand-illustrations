# Validation Notes

## Verdict

`explainer-sketch` is a useful second preset.

It moves Mr.Ai images closer to the xiaohei method by changing the generation mechanism, not only by adding style adjectives:

- CLI layout selection now chooses small physical metaphors.
- Prompt role now says whiteboard explanatory sketch instead of brand illustration.
- Mr.Ai is intentionally smaller.
- The physical mechanism is the visual center.
- Color is constrained to black marker linework plus limited blue/yellow/red.

## Image review

### `16x9/02-checkpoint-rope-explainer-v1.png`

Status: usable positive sample.

Works because:

- The loop is visible as a rope passing checkpoint signs.
- Mr.Ai is acting on the system instead of posing beside it.
- Blank signs allow later overlay text.
- White space is video-friendly.

Improve next:

- Make Mr.Ai even more line-art-like.
- Reduce the visual weight of the blue rope.
- Use blank signs by default unless testing text.

### `16x9/03-feedback-leak-explainer-v1.png`

Status: usable boundary sample.

Works because:

- Leak, state bucket, and magnifier make the risk easy to read.
- The metaphor is simpler than the previous brand-mode feedback-loop image.

Improve next:

- Mr.Ai is still slightly too large for explainer mode.
- Keep only one or two labels if text is not essential.

## Reusable rule

Use `brand` for IP identity and polished moments.

Use `explainer-sketch` for口播解释图, especially when the script includes:

- loop
- feedback
- verification
- state
- risk
- before/after process
- decision criteria

For delivery to another agent, ask it to start with:

```bash
bin/mrai gen <script.md> --out <sample-dir> --title "<topic>" --max-shots 5 --style explainer-sketch
```

