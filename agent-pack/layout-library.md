# Layout Library

Use this file when choosing repeatable Mr.Ai illustration layouts for AI 闲僧 videos.

Architecture note:

- `visual-routing-rules.json` decides which layout fits a semantic intent.
- `layout-library.json` stores machine-readable actions, default labels, and avoid lists.
- This Markdown file explains the same library for humans and agents.

Each layout is a starting point, not a rigid template. Keep Mr.Ai active, keep labels blank in the bitmap by default, and avoid formal PPT diagrams.

## Core Layouts

### Label Frame

Use for: identity labels, misleading category names, external definitions, stereotypes.

Scene: Mr.Ai peels oversized labels off a small portrait or object frame.

Avoid: identity documents, many tiny tags, face close-ups.

### Third Path

Use for: false binary choices, "not A or B, but C", rejecting forced selection.

Scene: Mr.Ai stands at a fork with two blocked paths and opens a small third path.

Avoid: heroic landscape, large road signs full of text, maze scenes.

### Use vs Rewrite

Use for: using a source/tool/influence versus actively transforming it.

Scene: Mr.Ai moves one source card from a consumption basket into a rewrite workbench.

Avoid: legal ownership scenes, shopping metaphors, copy-paste UI.

### Reweaving Loom

Use for: old material, prior knowledge, inherited influence, or external assets becoming a new expression.

Scene: Mr.Ai weaves two simple source ribbons through a small hand loom into one new pattern.

Avoid: literal celebrity references, dense fabric texture, decorative poster style.

### Coexistence Stage

Use for: two origins, roles, or truths coexisting without replacement.

Scene: Mr.Ai turns on two small lamps whose light overlaps without becoming a formula.

Avoid: plus signs, equations, three-box PPT layout.

### Black Box Reveal

Use for: hidden mechanisms, model behavior, systems, role definitions, invisible process.

Scene: Mr.Ai opens a simple dark box and reveals mechanism cards inside.

Avoid: sci-fi UI, robot faces, complex circuit boards.

### Evidence Scale

Use for: weighing claims, choices, trust, verification, and interpretation.

Scene: Mr.Ai weighs a claim card against evidence cards on a small scale.

Avoid: courtroom drama, financial chart, heavy realism.

### Guardrail Pit

Use for: risk, boundaries, hallucination, safety constraints, "do not cross" moments.

Scene: Mr.Ai places a yellow guardrail before a red risk pit.

Avoid: disaster imagery, horror lighting, giant warning posters.

### Toolchain Thread

Use for: agents, tool calling, handoff, automation workflow, batch pipeline.

Scene: Mr.Ai threads a blue line through small tool blocks.

Avoid: dense software architecture, realistic UI screenshots, many app icons.

### Mini Comic Correction

Use for: misconception correction, emotional reversal, "we thought X, actually Y".

Scene: two or three tiny panels: assumption, check, correction.

Avoid: speech balloons full of text, children's book tone, too many panels.

### Before/After Desk

Use for: transformation from old to new, messy to clear, manual to automated.

Scene: Mr.Ai moves a card from an old messy desk to a clearer new workbench.

Avoid: corporate before-after slides, symmetrical posters, busy office scenes.

## Workflow Layouts

### Checkpoint Rope

Use for: loops, checkpoints, state reads, validation, stop conditions.

Scene: Mr.Ai pulls one blue rope through simple checkpoint posts.

Avoid: formal flowcharts, too many steps, tangled rope.

### Feedback Leak

Use for: bad output or state entering a loop and amplifying.

Scene: Mr.Ai plugs a leaking red pipe before it drips into a state bucket.

Avoid: industrial machinery, gross liquid, catastrophe.

### Decision Gates

Use for: deciding whether a task is suitable, verifiable, recoverable, or worth looping.

Scene: four small gates; only one is open.

Avoid: game level art, castle scenes, text-heavy gates.

### Nested Rings

Use for: layers, scopes, nested responsibilities.

Scene: Mr.Ai points at three nested hand-drawn rings.

Avoid: corporate Venn diagrams, target logos, dense architecture.

### Evidence Clamp

Use for: goals, claims, or outputs accepted only with evidence.

Scene: Mr.Ai clips a goal card and an evidence card onto one board.

Avoid: legal contracts, dashboards, tiny checklist text.

### Conveyor Split

Use for: input becoming output through a process that separates signal from noise.

Scene: Mr.Ai nudges cards along a thin conveyor that splits useful output from noise.

Avoid: factory illustrations, complex machines, PPT pipelines.

## Selection Rules

- Use `Label Frame` when a label distorts the thing itself.
- Use `Third Path` only when the segment rejects a forced binary.
- Use `Use vs Rewrite` when the key question is transformation by use.
- Use `Coexistence Stage` when the point is coexistence, not addition.
- Use `Checkpoint Rope`, `Feedback Leak`, `Decision Gates`, `Nested Rings`, `Evidence Clamp`, and `Conveyor Split` for workflow and agent-system explanations.
- If one layout appears more than twice, choose a nearby physical metaphor before generating images.
