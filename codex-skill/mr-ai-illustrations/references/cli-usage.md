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

Validate a generated package before handoff:

```bash
bin/mrai validate samples/my-topic
```

List expected image slots and whether generated files exist:

```bash
bin/mrai assets samples/my-topic
```

B-side records image generation:

```bash
bin/mrai submit records.json --out samples/my-topic --backend mmx
bin/mrai run <job_id>
bin/mrai query <job_id>
```

Use `--backend mock` for offline validation. The records interface is documented in `agent-pack/b-records-interface.md`.

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

`auto` is deterministic and rule-based. It is useful for first-pass scaffolds, not final art direction.

The rule layer is outside Python:

- `agent-pack/visual-routing-rules.json`: semantic intent -> layout.
- `agent-pack/layout-library.json`: layout -> action, labels, avoid list.
- `agent-pack/treatment-rules.json`: S/B segment scoring, quote handling, timeline treatment.

These files should use transferable semantic patterns, not named entities from test scripts.

Useful overrides:

```bash
bin/mrai gen script.md --out samples/my-topic --style auto --segments S2,S4,S7
bin/mrai gen script.md --out samples/my-topic --prefer-layout "Third Path"
bin/mrai gen script.md --out samples/my-topic --routing agent-pack/visual-routing-rules.json
```

Inline segment override:

```markdown
### S4 · 核心判断
<!-- visual: style: explainer-sketch, layout: Third Path, labels: 模仿|拒绝|改写, cognitive_role: turning_point, pace: turn -->

这里是口播正文。
```

## Audio-visual decision fields

`audio-visual-map.json` is the downstream interface for Remotion, ffmpeg, or another video agent. Each segment includes:

- `visual_treatment`: `brand`, `explainer-sketch`, `subtitle-or-no-image`, or `quote-card-or-overlay`.
- `cognitive_role`: why this segment matters in the argument, such as `hook`, `misconception`, `turning_point`, `mechanism`, `evidence_or_boundary`, or `conclusion`.
- `expression_pace`: how the visual should behave in time, such as `hook`, `turn`, `explain`, `quote`, or `landing`.
- `timing_hint`: a human/agent-readable timing note.
- `visual_purpose`: the reason to show, skip, hold, or replace the image.

These fields are generated from `agent-pack/treatment-rules.json` and can be overridden inline when the automatic reading is too rough.

The CLI limits repeated layouts: a single style/layout pair should not appear more than twice in one package. If the first match repeats too much, the CLI falls back to a related physical metaphor. Still review `shot-list.md`; if two images feel visually redundant, rewrite one shot before image generation.

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
- `asset-manifest.json`
- `qa-report.md`
- `remotion-overlay-notes.md`
- `validation-notes.md`
- `16x9/`
- `9x16/`

## Validation

`bin/mrai validate <package>` checks that the generated folder has the required files, required image-format directories, and a valid `audio-visual-map.json` contract.

It verifies:

- required AV map fields
- allowed enum values
- `B` segments remain quote-card/overlay material
- every shot references a selected host voiceover segment
- every shot carries both `16x9` and `9x16` formats in the current MVP
- every shot has stable `asset_slots`
- `asset-manifest.json` matches `audio-visual-map.json`

Run it before handing a package to Remotion, ffmpeg, 耿鬼, OpenClaw, or another production agent.

`bin/mrai assets <package>` is a non-blocking asset inventory. It prints every expected 16:9 and 9:16 image path from `asset-manifest.json` and marks each one as `ok` or `missing`. Use it after image generation to confirm whether the image files landed in the expected slots.

## Role in the production pipeline

Use CLI for:

- Batch package creation.
- B-side records image job submission.
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

`overlay_text_candidate` is a short overlay seed, not a full subtitle. `script_summary_excerpt` carries the truncated script summary when downstream tools need a longer source excerpt.

Future versions may add:

- `--labels blank|short|overlay`
- image backend hooks
- batch input directories
- direct ffmpeg manifest output
