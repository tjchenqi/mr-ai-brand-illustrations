# Optional Remotion Notes

This project can be used without Remotion. When a video production agent uses Remotion, treat this file as optional guidance.

## Split responsibilities

Image generation should handle:

- Mr.Ai character.
- Core metaphor.
- Short labels.
- Clean composition.

Remotion or editing should handle:

- Full subtitles.
- Long Chinese titles.
- Timed callouts.
- Animated arrows.
- Highlight boxes.
- Episode chapter text.
- Final layout adjustments.

## Overlay notes per shot

For each image, optionally output:

- Subtitle safe area.
- Suggested entry animation.
- Suggested label reveal order.
- Whether to pan, zoom, or keep still.
- Any label that should be added outside the generated image.

## Render caution

This project should not trigger full video renders by itself. It only prepares still-image assets and optional overlay notes.

