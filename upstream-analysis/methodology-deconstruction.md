# Methodology Deconstruction

## What the upstream project does well

The upstream project is not only a style prompt. It is a small production system for article illustrations. Its strongest design choices are:

1. It separates planning from image generation.
2. It asks the agent to find cognitive anchors instead of illustrating every paragraph.
3. It uses a recurring IP character as an active participant, not decoration.
4. It gives composition categories that map abstract writing to visible structures.
5. It uses short labels and avoids long text in generated images.
6. It defines QA failure signals and repair moves.
7. It treats example images as calibration, not as templates to copy.

## Transferable method

These parts should be adapted for Mr.Ai:

- Script or article digestion.
- Cognitive anchor selection.
- Shot list before generation.
- One image, one idea.
- Recurring character performs the conceptual action.
- Physical metaphor before formal diagram.
- Short in-image labels.
- Explicit prompt template.
- QA checklist and repair methods.
- Example images as later calibration, not default context.

## Parts not transferred

These parts should not be transferred:

- Xiaohei as the IP character.
- Black silhouette visual identity.
- Pure black-and-white minimalist drawing as the dominant style.
- Upstream example image composition patterns.
- Upstream copywriting as project-facing documentation.
- The assumption that output is only 16:9.

## Key adaptation challenge

Mr.Ai has a much stronger brand look than Xiaohei. Xiaohei can be a simple black mark inside many diagram-like scenes. Mr.Ai is a colored character with fixed identity traits, so the image system must protect character consistency before pursuing visual metaphor complexity.

This means the Mr.Ai prompt should be character-first:

1. Lock the cap, mustache, blue clothing, yellow accent, rounded cartoon identity.
2. Keep the surrounding explanatory props simple.
3. Use text sparingly.
4. Avoid dense diagrams that make Mr.Ai decorative.

## Added requirements for AI 闲僧

Compared with the upstream project, AI 闲僧 needs:

- 16:9 and 9:16 planning.
-口播稿 position mapping.
- Video-internal explanation priority.
- Optional Remotion overlay notes.
- Delivery folders for image sequences.
- Cross-agent usage, not only Codex Skill usage.
- Stronger brand character bible.

