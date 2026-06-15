# Delivery Spec

## Folder layout per task

```text
samples/<episode-or-topic-slug>/
├── source-script.md
├── shot-list.md
├── image-prompts.md
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
structure_type:
mr_ai_action:
main_metaphor:
short_labels:
prompt_status:
qa_status:
```

## QA report fields

- Character consistency.
- Concept clarity.
- Text safety.
- Format safety.
- Brand fit.
- Revision notes.

