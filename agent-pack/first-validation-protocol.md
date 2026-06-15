# First Validation Protocol

Use this protocol before handing the project to another production agent such as 耿鬼.

## Goal

Verify that the system can turn one real AI 闲僧 script into usable Mr.Ai illustration assets for a simple voiceover plus image-carousel video workflow.

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
- `shot-list.md`
- `image-prompts.md`
- `qa-report.md`
- `16x9/`
- `9x16/`
- optional `remotion-overlay-notes.md`
- `validation-notes.md`

## Pass criteria

The first validation passes if:

- Mr.Ai remains recognizable in generated images.
- The shot list chooses cognitive anchors instead of illustrating every paragraph.
- Each image explains one idea.
- 16:9 and 9:16 variants are planned separately.
- Chinese text errors are noticed and handled through QA or overlay notes.
- The output could be used in a voiceover plus image-carousel video without major redesign.

## Fail criteria

The validation fails if:

- Mr.Ai loses cap, mustache, blue clothing, or yellow accent.
- The images become generic AI/robot art.
- The output is mostly formal flowcharts or PPT pages.
- The agent ignores the script and makes generic AI topic images.
- The agent relies on long in-image Chinese text.
- No QA notes are produced.

## Review questions

After the validation, answer:

- Which Mr.Ai traits were stable?
- Which traits drifted?
- Which labels failed or should move to post-production?
- Which layout pattern worked best?
- Which file was most useful for the agent?
- Which instruction was missing or ambiguous?

