# Prompt Template

Use this template for each individual image. Replace every placeholder.

Choose a preset before writing the prompt:

- `brand`: polished Mr.Ai brand illustration.
- `explainer-sketch`: sparse whiteboard explanation, closer to xiaohei's visual logic while preserving Mr.Ai.

```text
Generate one standalone Mr.Ai brand illustration for the AI 闲僧 video column.

Format:
{16:9 horizontal / 9:16 vertical}. Clean composition with safe space for later subtitles and video overlays.

Brand character:
Mr.Ai is a friendly middle-aged AI explainer with a baseball cap, gray/dark mustache, rounded cartoon face, blue shirt, thick dark outline, and yellow brand accent. He must perform the core conceptual action, not stand as decoration. Keep him warm, calm, curious, and practical. Do not make him a robot, monk, child, black silhouette, or formal business presenter.

Visual style:
Colored cartoon brand IP plus clean explanatory sketch logic. White or very light background, simple conceptual props, restrained blue/yellow brand color, dark outlines, small red warnings only when needed, sparse handwritten Chinese labels.

Theme:
{shot theme}

Core idea:
{one-sentence idea this image explains}

Structure type:
{Workflow / Black box reveal / Before and after / Risk and guardrail / Toolchain handoff / Evidence stack / Concept machine / Mini comic}

Composition:
{where Mr.Ai is, what he is doing, what physical metaphor appears, how information flows}

Short Chinese labels:
{label1} / {label2} / {label3} / {optional label4} / {optional label5}

Constraints:
One image explains only one core idea. Use at most 3-5 short Chinese labels, and do not repeat the same label on multiple objects. If exact Chinese text is important, leave clean blank label cards or label spaces so text can be added later in video editing. Do not write a long title, paragraph, subtitle, or structure type on the image. Do not make it a PPT infographic, dense architecture diagram, stock vector, generic mascot poster, realistic UI screenshot, sci-fi interface, robot icon, robot face, or children's illustration. Preserve Mr.Ai's cap, mustache, blue clothing, yellow accent, and rounded middle-aged cartoon identity.
```

## Explainer-sketch template

Use when the voiceover needs a fast, physical explanation rather than a polished brand moment.

```text
Generate one standalone Mr.Ai whiteboard explanatory sketch for the AI 闲僧 video column.

Format:
{16:9 horizontal / 9:16 vertical}. Clean white background with generous empty space for later subtitles and video overlays.

Brand character:
Mr.Ai is a friendly middle-aged AI explainer with a baseball cap, gray/dark mustache, rounded cartoon face, simple blue shirt, thick dark outline, and a tiny yellow brand accent. Draw him small, about 10-18% of the canvas in 16:9 or 12-22% in 9:16, as the person performing the explanatory action. Do not make him a robot, monk, child, black silhouette, or formal business presenter.

Visual style:
Hand-drawn whiteboard explanation, thin black marker lines, sparse props, rough human sketch feeling, no polished render, no glossy shading, no full scene background. Use mostly unfilled black line art. Use blue only for Mr.Ai's shirt or the main process line, yellow only for one small highlight, red only for warnings. Avoid large filled color areas. The image should feel closer to a simple explanatory sketch than a finished poster.

Theme:
{shot theme}

Core idea:
{one-sentence idea this image explains}

Structure type:
{Checkpoint rope / Feedback leak / Decision gates / Nested rings / Evidence clamp / Conveyor split}

Composition:
{where small Mr.Ai is, what he is doing, what physical metaphor appears, how information flows}

Short Chinese labels:
{label1} / {label2} / {label3} / {optional label4}

Constraints:
One image explains only one core idea. Prefer blank label cards when exact text is not required. If labels are used, use at most 2-4 short Chinese labels on large blank signs. No title, no paragraphs, no subtitles, no decorative background, no PPT infographic, no dense architecture diagram, no stock vector, no realistic UI screenshot, no sci-fi interface, no robot icon, no robot face, no children's-book scene. Preserve Mr.Ai's cap, mustache, blue clothing, yellow accent, and rounded middle-aged cartoon identity.
```

## 16:9 notes

Use wider left-to-right flow when explaining a process. Leave quiet space in one corner for later episode captions when useful.

## 9:16 notes

Use stacked vertical flow. Keep Mr.Ai and the main metaphor in the middle 70% of the frame. Avoid putting essential labels near the top or bottom edges.

## Text accuracy notes

Image models may distort short Chinese labels. For production-critical text, prefer one of these strategies:

- Generate blank label cards and add text in Remotion or editing.
- Use only 1-3 essential labels inside the image.
- Avoid visually similar or easily confused labels such as `回答` if the generated model tends to corrupt them.
- Put the exact overlay text in `remotion-overlay-notes.md` instead of relying on the bitmap.

## Controlled text test ladder

Use in-image Chinese only after a no-text version of the metaphor works.

1. Start with blank label cards.
2. Test 2-3 short labels on large physical signs.
3. Quote the exact labels in the prompt.
4. Say "No other words, no title, no paragraphs."
5. Keep the image only if every label is correct; otherwise use post-production text.
