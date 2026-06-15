# 耿鬼 Handoff Prompt

Use this prompt to hand the repository to 耿鬼 or another production agent for the first real validation.

```text
你现在要使用 Mr.Ai Brand Illustrations 项目，为 AI 闲僧视频栏目做一次真实配图验证。

项目地址：
https://github.com/tjchenqi/mr-ai-brand-illustrations

请先阅读这些文件：

1. README.md
2. agent-pack/project-positioning.md
3. agent-pack/mr-ai-character-bible.md
4. agent-pack/visual-style-dna.md
5. agent-pack/script-to-shot-workflow.md
6. agent-pack/layout-library.md
7. agent-pack/cli-usage.md
8. agent-pack/prompt-template.md
9. agent-pack/qa-checklist.md
10. agent-pack/first-validation-protocol.md

任务：
根据我提供的一篇 AI 闲僧口播稿，输出一套 Mr.Ai 配图验证包。

请生成或整理这些文件：

- source-script.md
- shot-list.md
- image-prompts.md
- qa-report.md
- 16x9/
- 9x16/
- remotion-overlay-notes.md（可选）
- validation-notes.md

要求：

- 不要复刻小黑 IP。
- Mr.Ai 必须保留棒球帽、胡子、蓝色衣服、黄色品牌色、亲切中年 AI 解读者气质。
- 每张图只解释一个概念。
- 图片内中文只放极短标签；如果文字准确性重要，请留空标签位并写入 overlay notes。
- 默认同时规划 16:9 和 9:16。
- 实际生成图片时先生成 2-3 张，不要一次生成完整大批量。
- 最后明确记录：哪些图可用、哪些要重生成、哪些规则需要修改。

如果你在本地运行仓库，可以先用：

bin/mrai gen path/to/script.md --out samples/<topic-slug> --title "<topic>" --max-shots 5

然后再人工/agent 修订生成的 shot-list 和 image-prompts。
```
