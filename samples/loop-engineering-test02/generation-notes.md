# Generation Notes

## Run 1

- Date: 2026-06-15
- Mode: built-in image generation
- Source: `/Users/tjboss/Desktop/AI 闲僧/test02.md`
- Purpose: test Mr.Ai illustrations on a dense abstract technical script about Loop Engineering

## CLI observation

Initial `mrai gen` exposed a long-script parsing issue:

- The source script had Chinese section markers such as `一、二、三、四、` embedded in long paragraphs.
- The first CLI pass treated pseudo-code fragments as independent shot candidates.
- The package shot list was manually revised for this test.
- CLI was then patched to recognize Chinese section markers and avoid short code-like lines in summaries.

## Generated files

- `16x9/01-three-layers-v1.png`
- `16x9/02-seven-step-loop-v1.png`
- `16x9/04-error-feedback-loop-v1.png`

## Results

### 01-three-layers-v1.png

Status: candidate usable.

Strengths:

- Mr.Ai remains visually stable.
- Nested-box metaphor explains the three-layer distinction well.
- Blank label cards worked.
- No robot icon or sci-fi drift.

Issues:

- The metaphor is clear, but overlay text will be needed to distinguish the three layers.

Action:

- Keep as a positive sample for abstract architecture concepts.

### 02-seven-step-loop-v1.png

Status: strong candidate usable.

Strengths:

- Best image of this run.
- Workbench checkpoint loop feels physical rather than like a PPT diagram.
- Mr.Ai is the action subject.
- Blank labels create excellent overlay positions.

Issues:

- The seven checkpoints are visually clear but not semantically named without overlay text.

Action:

- Keep as a likely handoff positive example.

### 04-error-feedback-loop-v1.png

Status: candidate usable for risk concepts.

Strengths:

- Red feedback pipe and state jar communicate bad feedback entering persistent state.
- Mr.Ai actively blocks the leak.
- Risk is visible but not overly scary.

Issues:

- Red is visually dominant; use this pattern sparingly.

Action:

- Keep as a risk/guardrail sample.

## Rule updates

- CLI should better support Chinese long-form scripts with inline section markers.
- Blank-label strategy remains the preferred production mode.
- For abstract technical scripts, physical workbench metaphors produce better results than direct diagrams.

