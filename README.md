# Mr.Ai Brand Illustrations

AI 闲僧视频号/视频栏目的 Mr.Ai 专属 IP 配图系统。

这个项目用于把 AI 闲僧的口播稿、选题、观点和解释段落，转成一组稳定的 Mr.Ai 品牌插图规划与图片生成提示词。它不是通用插画 prompt，也不是某个开源项目的换皮版本，而是一套可给 Codex、OpenClaw、其他智能体和人工设计师共同使用的品牌插图生产规范。

## 定位

- 品牌：AI 闲僧
- IP：Mr.Ai
- 角色气质：亲切中年 AI 解读者
- 优先用途：视频内解释配图，与口播稿匹配
- 兼容用途：视频封面、公众号文章配图、短视频竖版配图
- 默认画幅：16:9 与 9:16 两套

Mr.Ai 必须稳定保留棒球帽、胡子、蓝色衣服、黄色品牌色和圆润卡通比例。画面可以吸收白底、留白、手写批注、概念隐喻和低科技解释图的方法，但主角不能变成黑白小人、机器人脸、和尚或西装商务人。

## 项目结构

```text
.
├── agent-pack/              # 通用智能体可读的核心规范
├── codex-skill/             # Codex Skill 适配层
├── openclaw/                # OpenClaw 或其他 agent 的入口说明
├── assets/
│   ├── brand-references/    # Mr.Ai 品牌参考图
│   └── examples/            # 后续样图
├── samples/                 # 后续口播稿、shot list、图片提示词、QA 报告
├── upstream-analysis/       # 上游项目拆解与改写决策
└── upstream-source/         # 上游文本快照，仅供分析
```

## 推荐使用方式

先让 agent 读：

1. `agent-pack/project-positioning.md`
2. `agent-pack/mr-ai-character-bible.md`
3. `agent-pack/script-to-shot-workflow.md`
4. `agent-pack/layout-library.md`
5. `agent-pack/prompt-template.md`
6. `agent-pack/qa-checklist.md`

然后输入口播稿或选题，要求输出：

- `shot-list.md`
- `image-prompts.md`
- `16x9/`
- `9x16/`
- `qa-report.md`
- 可选 `remotion-overlay-notes.md`

## 第一次真实验证

交付给耿鬼或其他视频生产 agent 前，先按 `agent-pack/first-validation-protocol.md` 做一次小范围验证。可直接使用 `openclaw/genggui-handoff-prompt.md` 作为任务提示词。

## 与上游项目的关系

本项目参考了 `helloianneo/ian-xiaohei-illustrations` 的方法论结构：先理解正文，再抽取认知锚点，生成 shot list，选择构图类型，设计隐喻动作，用 QA 约束图片漂移。

本项目不复用“小黑”角色、不复刻示例图、不复制其正文说明作为本项目规范。上游项目为 MIT License，详见 `NOTICE.md` 与 `upstream-analysis/`。

## 当前版本范围

当前版本只交付品牌插图系统的规范和 agent 入口。样图、模板内容生产、Remotion 视觉语言整合会作为后续专项小版本迭代。
