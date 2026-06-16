# Delivery Spec

## Folder layout per task

```text
samples/<episode-or-topic-slug>/
├── source-script.md
├── shot-list.md
├── image-prompts.md
├── timeline-plan.md
├── audio-visual-map.json
├── asset-manifest.json
├── audio-visual-map.schema.json  # project-level contract, stored in agent-pack/
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
 cognitive_role:
 expression_pace:
format:
formats:
structure_type:
mr_ai_action:
main_metaphor:
short_labels:
asset_slots:
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
 cognitive_role: hook | misconception | turning_point | mechanism | evidence_or_boundary | conclusion | explanation | quote_source
 expression_pace: hook | turn | explain | quote | landing
timing: sync_with_voiceover_anchor | hold_during_quote | keep_voiceover_primary
timing_hint:
voiceover_anchor:
script_summary_excerpt:
overlay_text_candidate:
```

`overlay_text_candidate` should be a short overlay seed, usually 1-7 Chinese characters or one compact phrase. It is not a full subtitle.

`script_summary_excerpt` carries a short source excerpt for debugging and downstream prompt review.

`audio-visual-map.json` carries the same plan in machine-readable form for other agents, Remotion, ffmpeg pipelines, or later batch tooling.

The machine-readable contract is documented in `agent-pack/audio-visual-map.schema.json`. The project test suite validates generated maps against that contract without requiring an external JSON Schema dependency.

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
  "cognitive_role": "hook | misconception | turning_point | mechanism | evidence_or_boundary | conclusion | explanation | quote_source",
  "expression_pace": "hook | turn | explain | quote | landing",
  "visual_purpose": "string",
  "timing": "sync_with_voiceover_anchor | hold_during_quote | keep_voiceover_primary",
  "timing_hint": "string",
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
  "cognitive_role": "hook | misconception | turning_point | mechanism | evidence_or_boundary | conclusion | explanation",
  "expression_pace": "hook | turn | explain | landing",
  "timing": "sync_with_voiceover_anchor",
  "timing_hint": "string",
  "voiceover_summary": "string",
  "script_summary_excerpt": "string",
  "visual_purpose": "string",
  "mr_ai_action": "string",
  "short_labels": ["string"],
  "asset_slots": {
    "16x9": "16x9/01-s2-topic-16x9.png",
    "9x16": "9x16/01-s2-topic-9x16.png"
  },
  "overlay_text_candidate": "string"
}
```

## Asset manifest fields

`asset-manifest.json` is the image-slot contract for agents that generate images or assemble video.

```json
{
  "topic": "string",
  "image_policy": "string",
  "assets": [
    {
      "shot_id": "01-s2-topic",
      "segment_id": "S2",
      "formats": ["16x9", "9x16"],
      "asset_slots": {
        "16x9": "16x9/01-s2-topic-16x9.png",
        "9x16": "9x16/01-s2-topic-9x16.png"
      },
      "style_preset": "brand | explainer-sketch",
      "structure_type": "string",
      "overlay_text_candidate": "string",
      "short_labels": ["string"],
      "status": "pending_generation | generated | accepted | rejected"
    }
  ]
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
