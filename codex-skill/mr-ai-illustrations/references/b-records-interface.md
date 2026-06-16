# B Records Interface

This interface is for B-side production agents such as 耿鬼. It is a local CLI job flow, not an HTTP service.

The existing `mrai gen` command remains the script-to-planning-package entrypoint. The records flow starts after B has chosen visual intents for S segments.

## Commands

Submit a job:

```bash
bin/mrai submit records.json --out samples/<topic> --backend mmx
```

Run a job:

```bash
bin/mrai run <job_id>
```

Query a job:

```bash
bin/mrai query <job_id>
```

For tests or offline validation, use:

```bash
bin/mrai submit records.json --out samples/<topic> --backend mock
```

The job store defaults to `.mrai-jobs/` under the current working directory. Generated images and `results.json` are written under `--out`.

If you submit with a custom job root, use the same root when running or querying:

```bash
bin/mrai submit records.json --out samples/<topic> --job-root /path/to/workspace --backend mmx
bin/mrai run <job_id> --root /path/to/workspace
bin/mrai query <job_id> --root /path/to/workspace
```

## Input

`records.json` may be a top-level list or an object with `records`.

Required per record:

- `s_id`: S segment id from the voiceover script.
- `audience_takeaway`: the cognitive target from A/B planning.
- `visual_intent`: B-side visual translation or metaphor direction.

Optional per record:

- `mode`: `brand`, `explainer-sketch`, or another provider-specific mode hint.
- `layout`: layout or safe-area hint.
- `labels`: Chinese labels for post-production overlay. These are not rendered inside the bitmap.
- `key_elements`: elements that should appear.
- `negative_elements`: elements to avoid.
- `reference_image`: Mr.Ai reference image path.
- `format`: `9x16` or `16x9`. V1.1 does not accept `both`; submit separate records instead.
- `beat_ref`: B-side beat id. The CLI preserves it but does not calculate timing.

## Output

`mrai query <job_id>` and `<out>/results.json` return:

- `job_id`
- `status`: `pending`, `running`, `completed`, or `failed`
- `progress`: total, completed, failed, cached
- `results`

Each result includes:

- `s_id`
- `beat_ref`
- `image_path`
- `image_meta`
- `layout_used`
- `mode_used`
- `safe_areas`
- `composition_template_id`
- `qa_status`: `pass`, `warning`, `failed`, or `needs_human_review`
- `qa_checks`
- `generation_meta`
- `version`
- `cache_hit`
- `error_code`
- `error_message`
- `overlay_labels`

Single-record failures do not make the whole job fail. A job can be `completed` with failed result items. B decides which images can enter Remotion.

## Safe Areas

Safe areas use normalized 0-1 coordinates:

```json
{"x": 0.06, "y": 0.78, "w": 0.88, "h": 0.2}
```

V1.1 uses five templates:

- `left_text_safe`
- `right_text_safe`
- `top_subtitle_safe`
- `bottom_subtitle_safe`
- `center_character_safe`

## Backend Policy

V1.1 supports:

- `mock`: offline test provider that writes tiny placeholder PNG files.
- `mmx`: MiniMax/image-01 provider using `--region cn`.

The prompt policy is fixed:

- Do not render Chinese in bitmap images.
- Put Chinese labels in `overlay_labels`.
- Preserve Mr.Ai's baseball cap, mustache, blue clothing, yellow brand accent, and friendly middle-aged cartoon identity.
- Avoid formula, equation, PPT infographic, plus-sign formula, dense architecture diagram, robot face, and sci-fi UI.

## Cache And Versions

Cache key is based on the full record, reference image hash, and backend config.

Same input reuses cached images with `cache_hit=true`.

Use `--force` on submit or run to generate the next version. Versions do not overwrite old images:

```text
S03_v1_9x16.png
S03_v2_9x16.png
```
