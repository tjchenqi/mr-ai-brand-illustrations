# Failure Cases

Record failed generations here. Failed images are useful because they prevent future agents from repeating the same mistakes.

Use one subfolder per failure:

```text
samples/_failure-cases/YYYYMMDD-topic/
├── prompt.txt
├── generated-image.jpg
└── notes.md
```

Minimum notes:

- Which script segment and layout?
- Which model/tool?
- What failed?
- What rule should be updated?

Common failures already observed:

- Image model renders Chinese as pseudo-text or translates it into English.
- Coexistence metaphors drift into formulas with plus signs.
- Workflow metaphors become PPT three-box diagrams.
- Mr.Ai becomes too small in 9:16.
- Baseball cap becomes a cylinder hat; mustache becomes unclear.
