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

## Output

The command writes:

- `source-script.md`
- `shot-list.md`
- `image-prompts.md`
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

- `--style strict|loose`
- `--labels blank|short|overlay`
- image backend hooks
- batch input directories
- direct ffmpeg manifest output

