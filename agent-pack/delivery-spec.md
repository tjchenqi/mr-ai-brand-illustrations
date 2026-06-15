# Delivery Spec

## Folder layout per task

```text
samples/<episode-or-topic-slug>/
├── source-script.md
├── shot-list.md
├── image-prompts.md
├── timeline-plan.md
├── audio-visual-map.json
├── qa-report.md
├── remotion-overlay-notes.md
├── 16x9/
└── 9x16/
```

## File naming

Use numbered filenames:

```text
01-black-box-reveal.png
02-prompt-control-panel.png
03-evidence-stack.png
```

Use the same base name for 16:9 and 9:16 variants when they represent the same idea.

## Shot list fields

```yaml
id:
script_position:
voiceover_summary:
visual_purpose:
format:
formats:
structure_type:
mr_ai_action:
main_metaphor:
short_labels:
prompt_status:
qa_status:
```

## Timeline fields

`timeline-plan.md` is the human-readable audio/visual sync plan.

Each segment should include:

```yaml
segment_id:
role: host_voiceover | quoted_source
visual_treatment: brand | explainer-sketch | quote-card-or-overlay | subtitle-or-no-image
timing: sync_with_voiceover_anchor | hold_during_quote | keep_voiceover_primary
voiceover_anchor:
script_summary_excerpt:
overlay_text_candidate:
```

`overlay_text_candidate` should be a short overlay seed, usually 1-7 Chinese characters or one compact phrase. It is not a full subtitle.

`script_summary_excerpt` carries a short source excerpt for debugging and downstream prompt review.

`audio-visual-map.json` carries the same plan in machine-readable form for other agents, Remotion, ffmpeg pipelines, or later batch tooling.

## Audio/visual map fields

Top-level:

```json
{
  "topic": "string",
  "style_preset": "brand | explainer-sketch | auto",
  "segments": [],
  "shots": []
}
```

Each segment:

```json
{
  "segment_id": "S2",
  "role": "host_voiceover | quoted_source",
  "title": "string",
  "voiceover_summary": "string",
  "script_summary_excerpt": "string",
  "selected_for_image": true,
  "visual_treatment": "brand | explainer-sketch | quote-card-or-overlay | subtitle-or-no-image",
  "timing": "sync_with_voiceover_anchor | hold_during_quote | keep_voiceover_primary",
  "overlay_text_candidate": "string"
}
```

Each shot:

```json
{
  "shot_id": "01-s2-topic",
  "segment_id": "S2",
  "segment_role": "host_voiceover",
  "formats": ["16x9", "9x16"],
  "style_preset": "brand | explainer-sketch",
  "structure_type": "string",
  "timing": "sync_with_voiceover_anchor",
  "voiceover_summary": "string",
  "script_summary_excerpt": "string",
  "visual_purpose": "string",
  "mr_ai_action": "string",
  "short_labels": ["string"],
  "overlay_text_candidate": "string"
}
```

## S/B handling

- `S` segments are required host narration units. Every S segment should appear in `timeline-plan.md`.
- `B` segments are optional quoted source material and should usually become quote cards or overlays.
- Scripts with S segments and no B segments are valid.
- Do not turn a B quote into a new metaphor image unless the producer explicitly asks for that interpretation.

## QA report fields

- Character consistency.
- Concept clarity.
- Text safety.
- Format safety.
- Brand fit.
- Revision notes.
