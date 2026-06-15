# Script To Shot Workflow

## Step 1: Read the script

Extract:

- Main topic.
- Audience pain or curiosity.
- Key claims.
- Cognitive turns.
- Examples, metaphors, and warnings.
- Places where an image would reduce explanation time.

Do not illustrate every paragraph. Choose moments where a visual metaphor can clarify the voiceover.

If the script uses `S` and `B` headings:

- Treat `S` as host voiceover. S is the required standard unit for口播 scripts.
- Treat `B` as optional quoted source material.
- A script with S segments and no B segments is valid.
- Use B segments as quote cards, source cards, or overlays unless the producer explicitly asks for a visual interpretation.
- Do not rewrite quoted meaning into a metaphor image.

## Step 2: Select cognitive anchors

Good anchors:

- A false belief being corrected.
- A before/after contrast.
- A black-box process becoming legible.
- A workflow with input, process, and output.
- A risk such as hallucination, bias, or overtrust.
- A toolchain handoff.
- A small principle that repeats across the episode.

Weak anchors:

- Generic intro lines.
- Pure background information.
- Long definitions.
- Sentences that already work better as subtitles.

## Step 3: Build a shot list

For each shot, write:

- `id`
- `script position`
- `voiceover summary`
- `visual purpose`
- `format`: 16:9, 9:16, or both
- `structure type`
- `Mr.Ai action`
- `main metaphor`
- `short labels`
- `overlay notes`: optional

Choose a style preset for each shot:

- Use `brand` when the shot should carry栏目识别、封面感、情绪氛围、人物温度.
- Use `explainer-sketch` when the shot must explain a mechanism quickly inside a口播视频.

For `explainer-sketch`, bias toward xiaohei-like physical metaphors:

- well: too much noise, filtering, first scoop
- conveyor: before/after, broken handoff, missing acceptance
- drawer/cabinet: sources, evidence, memory, assets
- rope/route line: loop, sequence, dependency, retry path
- gate: decision criteria, pass/fail, whether to continue
- bucket/pipe: feedback, leakage, state pollution
- clamp/scale: goal plus evidence, judgment, verification

Also create an audio/visual sync plan:

- `timeline-plan.md` for human review.
- `audio-visual-map.json` for downstream agents or video pipelines.

Each segment should state whether it gets a generated image, a quote card, subtitles only, or no image.

Default count:

- Short script: 2-4 images.
- Medium script: 4-8 images.
- Long script: 6-10 images.

## Step 4: Make the metaphor physical

Translate abstract AI ideas into visible actions:

- Hallucination: a confident answer bubble with a loose screw, checked by Mr.Ai.
- Prompt engineering: Mr.Ai tuning a small control panel with labeled knobs.
- Agent workflow: Mr.Ai pulling a thread through tools.
- RAG: Mr.Ai connecting a model box to a cabinet of evidence cards.
- Open-source model: Mr.Ai opening a transparent toolbox.
- Evaluation: Mr.Ai weighing answer cards on a small scale.
- Automation: Mr.Ai feeding a repeatable conveyor with checkpoints.

Keep props low-tech, memorable, and readable.

## Step 5: Produce prompts

Write one prompt per image. Never ask an image model to create multiple independent images in a single prompt.

For each selected shot, produce:

- 16:9 prompt.
- 9:16 prompt when needed.
- Negative constraints.
- Label list.
- QA focus.

## Step 6: QA before delivery

Check each image or prompt against:

- Character bible.
- Visual style DNA.
- One core idea per image.
- Text policy.
- Format safety.
- Delivery naming.
