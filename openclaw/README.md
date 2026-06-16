# OpenClaw Entry

Use this repository as a reusable agent pack.

## Minimal startup

Read these files in order:

1. `../agent-pack/project-positioning.md`
2. `../agent-pack/mr-ai-character-bible.md`
3. `../agent-pack/visual-style-dna.md`
4. `../agent-pack/script-to-shot-workflow.md`
5. `../agent-pack/layout-library.md`
6. `../agent-pack/prompt-template.md`
7. `../agent-pack/qa-checklist.md`
8. `../agent-pack/delivery-spec.md`
9. `../agent-pack/first-validation-protocol.md`
10. `../agent-pack/b-records-interface.md`
11. `genggui-handoff-prompt.md` when running the first real validation.

## Default task

Given an AI 闲僧 script or topic, produce:

- `source-script.md`
- `timeline-plan.md`
- `shot-list.md`
- `image-prompts.md`
- `audio-visual-map.json`
- `asset-manifest.json`
- `qa-report.md`
- `remotion-overlay-notes.md`
- `validation-notes.md`
- `16x9/`
- `9x16/`

Always run:

```bash
bin/mrai gen path/to/script.md --out samples/<topic-slug> --title "<topic>" --style auto --max-shots 5
bin/mrai validate samples/<topic-slug>
bin/mrai assets samples/<topic-slug>
```

For the first validation, generate only 2-3 images and place them in the paths declared by `asset-manifest.json`.

If B already has `records.json`, use the local job interface:

```bash
bin/mrai submit records.json --out samples/<topic-slug> --backend mmx
bin/mrai run <job_id>
bin/mrai query <job_id>
```

## Agent instruction

Do not copy the upstream Xiaohei visual identity. Use Mr.Ai only. Preserve cap, mustache, blue clothing, yellow accent, and friendly middle-aged cartoon identity.

For the first handoff, use `genggui-handoff-prompt.md` and end with the report template in `first-validation-protocol.md`.
