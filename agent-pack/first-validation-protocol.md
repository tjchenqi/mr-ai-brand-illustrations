# First Validation Protocol

Use this protocol before handing the project to another production agent such as 耿鬼.

## Goal

Verify that the system can turn one real AI 闲僧 script into a usable Mr.Ai visual package for a simple voiceover plus image-carousel video workflow.

The validation must test the full handoff loop:

```text
script -> mrai gen -> mrai validate -> review shot-list -> generate 2-3 images -> QA notes -> handoff report
```

## Scope

For the first validation, keep the task small:

- One short or medium script.
- 3-5 image concepts.
- Generate 2-3 actual images only.
- Include both 16:9 and 9:16 planning.
- Use optional Remotion notes, but do not require Remotion.

## Required input

The validating agent should receive:

- The GitHub repository URL.
- One source script or topic.
- The expected output folder name.
- Whether to generate images or prompts only.

## Required output

The validating agent should produce:

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

## Required commands

Run the package generator:

```bash
bin/mrai gen path/to/script.md --out samples/<topic-slug> --title "<topic>" --style auto --max-shots 5
```

Validate the package before image generation:

```bash
bin/mrai validate samples/<topic-slug>
```

If validation fails, stop and fix the package or report the failing fields before generating images.

List expected image slots:

```bash
bin/mrai assets samples/<topic-slug>
```

## Image generation step

Generate only 2-3 actual images for the first validation. Choose the shots from `shot-list.md` and `asset-manifest.json`.

For each generated image:

- Write it to the exact path in `asset-manifest.json`.
- Prefer the `9x16` version first when testing short-video use.
- Do not ask the image model to render Chinese sentences.
- Use blank cards, blank signs, roman numerals, or simple shapes inside the bitmap.
- Put exact Chinese text into `remotion-overlay-notes.md` or another post-production overlay layer.

If a tool cannot write directly to the manifest path, copy or rename the image afterward so the package still matches the manifest.

After generation, run the asset inventory again:

```bash
bin/mrai assets samples/<topic-slug>
```

The first validation may leave untested shot slots as `missing`; the generated 2-3 test images should be `ok`.

## Pass criteria

The first validation passes if:

- Mr.Ai remains recognizable in generated images.
- The shot list chooses cognitive anchors instead of illustrating every paragraph.
- Each image explains one idea.
- 16:9 and 9:16 variants are planned separately.
- Chinese text errors are noticed and handled through QA or overlay notes.
- The output could be used in a voiceover plus image-carousel video without major redesign.
- `bin/mrai validate samples/<topic-slug>` passes before the final report.
- Generated image files are placed in the `asset-manifest.json` slots or the report clearly explains why not.
- `bin/mrai assets samples/<topic-slug>` shows the generated test images as `ok`.

## Fail criteria

The validation fails if:

- Mr.Ai loses cap, mustache, blue clothing, or yellow accent.
- The images become generic AI/robot art.
- The output is mostly formal flowcharts or PPT pages.
- The agent ignores the script and makes generic AI topic images.
- The agent relies on long in-image Chinese text.
- No QA notes are produced.
- The agent generates images before reading `shot-list.md` and `asset-manifest.json`.
- The agent changes the package structure in a way that breaks `bin/mrai validate`.

## Review questions

After the validation, answer:

- Which Mr.Ai traits were stable?
- Which traits drifted?
- Which labels failed or should move to post-production?
- Which layout pattern worked best?
- Which file was most useful for the agent?
- Which instruction was missing or ambiguous?
- Did `bin/mrai validate` pass before and after image generation?
- Did the `asset-manifest.json` slots make video assembly easier or harder?
- Which `mrai assets` slots are still missing after the 2-3 image test?

## Report template

End the validation with:

```markdown
## Validation Summary

- Repo commit:
- Source script:
- Output folder:
- Command used:
- Validation result:
- Asset inventory result:
- Shots selected:
- Images generated:
- Usable images:
- Images needing regeneration:
- Mr.Ai trait drift:
- Chinese text handling:
- Files most useful downstream:
- Rules or docs to update:
```
