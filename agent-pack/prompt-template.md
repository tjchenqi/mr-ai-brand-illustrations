# Prompt Template

Use this template for each individual image. Replace every placeholder.

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
One image explains only one core idea. Use at most 3-5 short Chinese labels, and do not repeat the same label on multiple objects. If exact Chinese text is important, leave clean blank label cards or label spaces so text can be added later in video editing. Do not write a long title, paragraph, subtitle, or structure type on the image. Do not make it a PPT infographic, dense architecture diagram, stock vector, generic mascot poster, realistic UI screenshot, sci-fi interface, or children's illustration. Preserve Mr.Ai's cap, mustache, blue clothing, yellow accent, and rounded middle-aged cartoon identity.
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
