# QA Checklist

## Must pass

- Mr.Ai is present.
- Mr.Ai keeps cap, mustache, blue clothing, yellow accent, rounded cartoon identity.
- Mr.Ai performs the core action.
- The image explains one idea, not a whole lecture.
- The image uses only short Chinese labels.
- Repeated labels are intentional; otherwise each label appears only once.
- Production-critical Chinese text is either correct or planned for post-production overlay.
- The image is readable without long text.
- The composition works in the requested format.
- The image feels like AI 闲僧 brand content, not a random cartoon.

## Failure signals

- Mr.Ai becomes a robot, monk, child, generic presenter, or black silhouette.
- Cap, mustache, blue clothing, or yellow accent disappear.
- The image is mostly a flowchart with Mr.Ai pasted on the side.
- Too many arrows, boxes, labels, or UI panels.
- Long Chinese text appears inside the image.
- Short Chinese labels are wrong, duplicated, or visually confused.
- The image looks like PPT, stock vector, or a corporate SaaS diagram.
- The image becomes a polished flowchart instead of a small physical metaphor.
- The image is too cute, childish, glossy, or sci-fi.
- The vertical version crops out important labels or the character.

## Repair methods

- Character drift: regenerate with the character bible in the prompt and reduce other style instructions.
- Too much text: remove labels, keep only 3-5 short nouns.
- Text errors: regenerate with fewer labels, or generate blank label spaces and add exact text later.
- Repeated labels: name each object by role, or ask for unlabeled cards with post-production text.
- Too PPT-like: replace formal boxes with a physical prop or small scene.
- Mr.Ai too decorative: rewrite the composition so his action drives the metaphor.
- 9:16 unsafe: stack elements vertically and reserve top/bottom safe space.

## Delivery judgment

A strong image should feel like Mr.Ai is personally explaining one AI concept through a small memorable action.

If the image still works after removing Mr.Ai, it is not good enough.
