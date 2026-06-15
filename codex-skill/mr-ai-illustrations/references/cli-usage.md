# CLI Usage

`mrai` is a lightweight command-line helper for repeatable Mr.Ai illustration production.

It does not replace the agent skill. It creates the standard package structure, copies the script, proposes first-pass shots, and writes prompt scaffolds that an agent or image model can refine.

## Basic command

```bash
bin/mrai gen path/to/script.md --out samples/my-topic --title "My Topic" --max-shots 5
```

Inline text is also accepted:

```bash
bin/mrai gen "这里是一段口播稿..." --out ./imgs --title "临时验证"
```

## Style presets

Choose the visual mode explicitly:

```bash
bin/mrai gen script.md --out samples/my-topic --style brand
bin/mrai gen script.md --out samples/my-topic --style explainer-sketch
bin/mrai gen script.md --out samples/my-topic --style auto
```

- `brand`: polished Mr.Ai brand illustration. Use for opening, ending, emotional moments, culture/person stories, and cover-like assets.
- `explainer-sketch`: sparse whiteboard explanation. Use for mechanisms, workflows, risks, verification, loops, decision criteria, and xiaohei-like video inserts.
- `auto`: choose `brand` or `explainer-sketch` per selected S segment. Review before production.

## S/B script handling

The CLI recognizes standard video script headings such as:

```markdown
### S1 · 主播解释
### B1 · 原文引用
```

- `S` means host voiceover. S segments are required for the standard script format. Every S segment should appear in `timeline-plan.md`, though not every S segment needs a generated image.
- `B` means quoted source. B segments are optional. When present, they should preserve quoted meaning and normally become quote cards or overlays, not metaphor images.
- Scripts with S segments and no B segments are valid.
- Later editorial sections such as `主要改动说明` and `口播节奏检查` are ignored when parsing S/B scripts.

## Output

The command writes:

- `source-script.md`
- `shot-list.md`
- `image-prompts.md`
- `timeline-plan.md`
- `audio-visual-map.json`
- `qa-report.md`
- `remotion-overlay-notes.md`
- `validation-notes.md`
- `16x9/`
- `9x16/`

## Role in the production pipeline

Use CLI for:

- Batch package creation.
- Stable folder naming.
- ffmpeg or video pipeline integration.
- First-pass audio/visual alignment through `timeline-plan.md`.
- Machine-readable image timing and segment mapping through `audio-visual-map.json`.
- Re-running the same script after prompt changes.
- Giving 耿鬼 a predictable input/output contract.

Use agent reasoning for:

- Choosing better cognitive anchors.
- Rewriting rough shot choices.
- Tightening prompts before image generation.
- Reviewing images and updating QA rules.

Use image generation tools for:

- Producing actual PNG/JPG images.
- Editing or regenerating failed images.

## Current limitation

The CLI uses deterministic heuristics. Treat its shot list as a first draft. For production, the agent should review and revise at least the best 2-3 prompts before generating images.

Future versions may add:

- `--labels blank|short|overlay`
- image backend hooks
- batch input directories
- direct ffmpeg manifest output
