# 耿鬼 Handoff Prompt

Use this prompt to hand the repository to 耿鬼 or another production agent for the first real validation.

```text
你现在要使用 Mr.Ai Brand Illustrations 项目，为 AI 闲僧视频栏目做一次真实配图验证。

项目地址：
https://github.com/tjchenqi/mr-ai-brand-illustrations

请先阅读这些文件：

1. README.md
2. agent-pack/AGENT_START_HERE.md
3. agent-pack/project-positioning.md
4. agent-pack/mr-ai-character-bible.md
5. agent-pack/visual-style-dna.md
6. agent-pack/script-to-shot-workflow.md
7. agent-pack/layout-library.md
8. agent-pack/cli-usage.md
9. agent-pack/delivery-spec.md
10. agent-pack/prompt-template.md
11. agent-pack/qa-checklist.md
12. agent-pack/first-validation-protocol.md

任务：
根据我提供的一篇 AI 闲僧口播稿，输出一套 Mr.Ai 配图验证包，并实际生成 2-3 张图片做第一次验证。

标准流程：

1. clone 或更新仓库，记录当前 commit。
2. 把口播稿保存为本地 `.md` 文件。
3. 运行：

   bin/mrai gen path/to/script.md --out samples/<topic-slug> --title "<topic>" --style auto --max-shots 5

4. 运行：

   bin/mrai validate samples/<topic-slug>

5. 阅读 `shot-list.md`、`image-prompts.md`、`audio-visual-map.json`、`asset-manifest.json`。
6. 只选 2-3 个 shot 生成图片，优先测试 9:16。
7. 将图片放入 `asset-manifest.json` 指定的路径。
8. 完成 QA，并报告哪些规则需要更新。

请生成或整理这些文件：

- source-script.md
- timeline-plan.md
- shot-list.md
- image-prompts.md
- audio-visual-map.json
- asset-manifest.json
- qa-report.md
- 16x9/
- 9x16/
- remotion-overlay-notes.md
- validation-notes.md

要求：

- 不要复刻小黑 IP。
- Mr.Ai 必须保留棒球帽、胡子、蓝色衣服、黄色品牌色、亲切中年 AI 解读者气质。
- 每张图只解释一个概念。
- 图片内中文只放极短标签；如果文字准确性重要，请留空标签位并写入 overlay notes。
- 默认同时规划 16:9 和 9:16。
- 实际生成图片时先生成 2-3 张，不要一次生成完整大批量。
- 图片必须尽量落到 `asset-manifest.json` 指定路径，方便 ffmpeg/Remotion 后续读取。
- 生成图片前后都要跑 `bin/mrai validate samples/<topic-slug>`；如果失败，先报告失败项。
- 最后明确记录：哪些图可用、哪些要重生成、哪些规则需要修改。

最后请按这个格式回复：

## Validation Summary

- Repo commit:
- Source script:
- Output folder:
- Command used:
- Validation result:
- Shots selected:
- Images generated:
- Usable images:
- Images needing regeneration:
- Mr.Ai trait drift:
- Chinese text handling:
- Files most useful downstream:
- Rules or docs to update:
```
