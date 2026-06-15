---
name: mr-ai-illustrations
description: Plan and generate Mr.Ai brand illustrations for the AI 闲僧 video column. Use when the user asks for AI 闲僧 or Mr.Ai IP illustration planning, script-to-image shot lists, video explanation images, 16:9 and 9:16 image prompts, brand-consistent Mr.Ai character art, optional Remotion overlay notes, or QA for generated Mr.Ai visuals.
---

# Mr.Ai Illustrations

## Core purpose

Turn AI 闲僧 scripts, topics, and explanation segments into Mr.Ai brand illustration plans and image prompts.

Prioritize video-internal explanation images that match voiceover. Do not treat this as a generic cartoon generator or a Xiaohei character replacement.

## Read references as needed

Start with:

- `references/AGENT_START_HERE.md`
- `references/project-positioning.md`
- `references/mr-ai-character-bible.md`
- `references/visual-style-dna.md`
- `references/script-to-shot-workflow.md`
- `references/layout-library.md`
- `references/prompt-template.md`
- `references/qa-checklist.md`

Read when needed:

- `references/visual-routing-rules.json` for semantic intent to layout routing.
- `references/layout-library.json` for layout actions, labels, and avoid lists.
- `references/treatment-rules.json` for S/B scoring, quote handling, and inline override syntax.
- `references/composition-patterns.md` for choosing the visual structure.
- `references/cli-usage.md` when the user wants command-line or batch workflow integration.
- `references/delivery-spec.md` for task folder layout.
- `references/first-validation-protocol.md` when preparing a handoff to another production agent.
- `references/remotion-optional-notes.md` only when the user wants video overlay or Remotion notes.
- `references/sample-themes.md` only when creating a sample pack.

## Workflow

### 1. Understand the input

Read the user's script, topic, outline, or article. Extract the main AI concept, audience pain, cognitive turns, risks, and moments that benefit from a visual metaphor.

Do not illustrate every paragraph. Choose only the strongest cognitive anchors.

### 2. Produce a shot list first

Unless the user explicitly asks to generate images immediately, first output a concise shot list.

Each shot should include:

- script position
- script segment when S/B headings are available
- segment role: host voiceover or quoted source
- voiceover summary
- visual purpose
- format: 16:9, 9:16, or both
- structure type
- style preset: brand or explainer-sketch
- image timing
- Mr.Ai action
- main metaphor
- short Chinese labels
- optional overlay notes

For S/B scripts, preserve the distinction:

- S segments are required host narration units. Every S segment should appear in `timeline-plan.md`, though not every S segment needs a generated image.
- B segments are optional quoted source material and should usually become quote cards or overlays, not metaphor images.
- Scripts with S segments and no B segments are valid.

### 3. Write image prompts

Use `references/prompt-template.md`. Write one prompt per image and per format. Do not ask an image model to create multiple independent images in one prompt.

The prompt must preserve:

- baseball cap
- mustache
- rounded middle-aged cartoon face
- blue clothing
- yellow brand accent
- friendly AI explainer personality

### 4. Generate only when asked

If the user asks to generate images and image generation is available, generate each image individually. If generation is not available, deliver final prompts and QA guidance.

Default to no rendered Chinese text inside generated bitmap images. Ask for blank label cards/signs, then add exact Chinese later with editing tools or Remotion.

### 5. QA

Check every prompt or generated image against `references/qa-checklist.md`. The most important rule: Mr.Ai must perform the core conceptual action, not decorate a finished diagram.

## Default deliverables

For a full script package, produce:

- `shot-list.md`
- `image-prompts.md`
- `timeline-plan.md`
- `audio-visual-map.json`
- `qa-report.md`
- `16x9/`
- `9x16/`
- optional `remotion-overlay-notes.md`

Use `references/delivery-spec.md` for naming and folder structure.
