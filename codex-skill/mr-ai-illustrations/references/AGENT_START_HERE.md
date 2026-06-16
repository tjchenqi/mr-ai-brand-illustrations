# Agent Start Here

This package turns an AI 闲僧 voiceover script into a reviewable Mr.Ai audio-visual plan.

Read in this order:

1. `project-positioning.md`
2. `mr-ai-character-bible.md`
3. `visual-style-dna.md`
4. `script-to-shot-workflow.md`
5. `cli-usage.md`
6. `b-records-interface.md`
7. `qa-checklist.md`

Run:

```bash
bin/mrai gen path/to/script.md --out samples/my-topic --title "My Topic" --style auto --max-shots 5
bin/mrai validate samples/my-topic
bin/mrai assets samples/my-topic
```

Review before image generation:

- `timeline-plan.md`: every S/B segment should have a timing/treatment decision.
- `shot-list.md`: selected shots only; do not generate images for every paragraph.
- `audio-visual-map.json`: machine-readable contract for Remotion, ffmpeg, or another video agent.
- `asset-manifest.json`: expected image output slots for each selected shot.
- `image-prompts.md`: prompts are drafts; tighten the best 2-3 before generating images.

B-side records image generation:

```bash
bin/mrai submit records.json --out samples/my-topic --backend mmx
bin/mrai run <job_id>
bin/mrai query <job_id>
```

Use `--backend mock` for offline validation.

Validate machine-readable output against `agent-pack/audio-visual-map.schema.json` when building automation around this package.

Override when needed:

```bash
bin/mrai gen script.md --out samples/my-topic --segments S2,S4,S7
bin/mrai gen script.md --out samples/my-topic --prefer-layout "Coexistence Stage"
```

Inline override:

```markdown
<!-- visual: style: explainer-sketch, layout: Label Frame, labels: 标签|误解|本人 -->
```

Default text policy:

- Do not render Chinese inside generated bitmap images.
- Use blank cards/signs in images.
- Add exact Chinese labels later in Remotion or editing.

The method is inherited from xiaohei-like explanatory illustration: stable character, white space, physical metaphor, arrows, sparse labels, and QA loops. The architecture is upgraded for video: S/B parsing, shot selection, audio-visual mapping, and handoff to other agents.
