# Shot List

- Topic: Loop Engineering
- Status: manually revised after `mrai gen` exposed long-text splitting issues
- Test goal: verify Mr.Ai can explain abstract agent-loop engineering concepts without becoming PPT diagrams

## 01-three-layers

```yaml
id: 01-three-layers
script_position: "Agent loop / harness / Loop Engineering 三层关系"
voiceover_summary: "Agent loop 负责这一轮如何行动，harness 负责环境与约束，Loop Engineering 决定为什么进入下一轮以及何时结束。"
visual_purpose: Show the three-layer distinction as a physical nested system.
format: both
structure_type: Black Box Reveal
mr_ai_action: "Mr.Ai opens a nested box: inner loop, outer harness, and a top-level route board."
main_metaphor: "nested boxes with a route board"
short_labels: []
prompt_status: ready
qa_status: pending image generation
```

## 02-seven-step-loop

```yaml
id: 02-seven-step-loop
script_position: "目标 → 读取状态 → 选择工作 → 执行 → 验证 → 写回 → 路由或停止"
voiceover_summary: "一个可靠的任务级 Loop 不是简单重复调用 Agent，而是有目标、状态、选择、执行、验证、写回和退出。"
visual_purpose: Make the loop closure concrete without generating a formal flowchart.
format: both
structure_type: Validation Loop
mr_ai_action: "Mr.Ai pulls a blue cable through seven physical checkpoint tokens on a workbench."
main_metaphor: "workbench checkpoint loop"
short_labels: []
prompt_status: ready
qa_status: pending image generation
```

## 03-verification-contract

```yaml
id: 03-verification-contract
script_position: "目标与验证形成可执行的验收契约"
voiceover_summary: "目标不是一句意图，而是一份可以被环境证据检查的验收契约。"
visual_purpose: Explain why goals and verification must pair together.
format: both
structure_type: Evidence Scale
mr_ai_action: "Mr.Ai clips a goal card and a test-evidence card onto the two sides of one contract board."
main_metaphor: "contract board with evidence clips"
short_labels: []
prompt_status: ready
qa_status: pending image generation
```

## 04-error-feedback-loop

```yaml
id: 04-error-feedback-loop
script_position: "闭环之后，错误也会闭环"
voiceover_summary: "如果验证标准错了，错误结果会被写入状态，并在下一轮继续放大。"
visual_purpose: Show the danger of bad feedback being persisted.
format: both
structure_type: Guardrail Pit
mr_ai_action: "Mr.Ai blocks a red leaking feedback loop before it flows into a state jar."
main_metaphor: "leaking red feedback loop and state jar"
short_labels: []
prompt_status: ready
qa_status: pending image generation
```

## 05-four-gates

```yaml
id: 05-four-gates
script_position: "不是所有任务都值得闭环"
voiceover_summary: "任务是否适合 Loop，要看结果是否可验证、状态是否可保存、失败是否可恢复、建设成本是否值得。"
visual_purpose: Give the audience a decision framework.
format: both
structure_type: Guardrail Pit
mr_ai_action: "Mr.Ai stands before four small gates and opens only the gates that pass inspection."
main_metaphor: "four decision gates"
short_labels: []
prompt_status: ready
qa_status: pending image generation
```

