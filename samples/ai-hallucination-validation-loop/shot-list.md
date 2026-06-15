# Shot List

## Overview

- Topic: AI hallucination and validation loop
- Target use: AI 闲僧 video-internal explanation images
- Default formats: 16:9 and 9:16
- Image generation status: prompts only, no images generated in this dry run

## Shots

### 01-answer-is-not-evidence

```yaml
id: 01-answer-is-not-evidence
script_position: after paragraph 2
voiceover_summary: "像答案"不等于"有依据"。
visual_purpose: Correct the false belief that fluent AI output is automatically reliable.
format: both
structure_type: Before and after
mr_ai_action: Mr.Ai holds a shiny answer card in one hand and an empty evidence folder in the other, looking calm but skeptical.
main_metaphor: A polished answer card floats above an empty evidence folder.
short_labels: ["答案", "证据", "不等于"]
prompt_status: ready
qa_status: pending image generation
```

### 02-evidence-scale

```yaml
id: 02-evidence-scale
script_position: after paragraph 4
voiceover_summary: Mr.Ai puts the answer on an evidence scale.
visual_purpose: Make verification feel like a concrete action rather than an abstract principle.
format: both
structure_type: Evidence stack
mr_ai_action: Mr.Ai places answer cards on a small scale, stacking evidence cards on the other side.
main_metaphor: The evidence scale keeps strong claims and marks weak claims with question tags.
short_labels: ["回答", "证据", "问号", "通过"]
prompt_status: ready
qa_status: pending image generation
```

### 03-validation-loop

```yaml
id: 03-validation-loop
script_position: after paragraph 5
voiceover_summary: Useful AI workflows expose uncertainty early.
visual_purpose: Show the loop: answer, evidence, check, repair.
format: both
structure_type: Workflow
mr_ai_action: Mr.Ai pulls a blue thread through four low-tech checkpoints.
main_metaphor: A validation loop made from small checkpoint boxes.
short_labels: ["回答", "依据", "检查", "修正"]
prompt_status: ready
qa_status: pending image generation
```

### 04-black-box-to-toolchain

```yaml
id: 04-black-box-to-toolchain
script_position: after final paragraph
voiceover_summary: The workflow turns AI from a talking black box into a collaborative toolchain.
visual_purpose: Close the explanation with a branded conceptual transformation.
format: both
structure_type: Black box reveal
mr_ai_action: Mr.Ai opens a dark model box and connects it to visible tool modules with a yellow cable.
main_metaphor: A black box becomes a transparent toolchain.
short_labels: ["黑盒", "工具链", "协作"]
prompt_status: ready
qa_status: pending image generation
```

