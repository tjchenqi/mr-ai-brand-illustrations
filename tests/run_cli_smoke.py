#!/usr/bin/env python3
"""Smoke tests for the mrai CLI contract.

These tests do not judge image beauty. They protect the production contract:
S/B parsing, machine-readable AV maps, blank-text prompt policy, and overrides.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BIN = ROOT / "bin" / "mrai"
FIXTURES = ROOT / "tests" / "fixtures"
AV_SCHEMA = ROOT / "agent-pack" / "audio-visual-map.schema.json"


def run(*args: str) -> None:
    subprocess.run([str(BIN), *args], cwd=ROOT, check=True)


def load_map(path: Path) -> dict:
    return json.loads((path / "audio-visual-map.json").read_text(encoding="utf-8"))


def load_schema() -> dict:
    return json.loads(AV_SCHEMA.read_text(encoding="utf-8"))


def assert_allowed(value, allowed, label: str) -> None:
    assert value in allowed, f"{label}: {value!r} not in {allowed!r}"


def assert_av_map_schema(data: dict, schema: dict) -> None:
    for key in schema["top_level_required"]:
        assert key in data, f"missing top-level field {key}"
    assert_allowed(data["style_preset"], schema["enums"]["top_level.style_preset"], "style_preset")

    segment_ids = set()
    selected_host_ids = set()
    for segment in data["segments"]:
        for key in schema["segment_required"]:
            assert key in segment, f"segment {segment.get('segment_id')} missing {key}"
        segment_ids.add(segment["segment_id"])
        assert_allowed(segment["role"], schema["enums"]["segment.role"], f"{segment['segment_id']}.role")
        assert_allowed(segment["visual_treatment"], schema["enums"]["segment.visual_treatment"], f"{segment['segment_id']}.visual_treatment")
        assert_allowed(segment["cognitive_role"], schema["enums"]["segment.cognitive_role"], f"{segment['segment_id']}.cognitive_role")
        assert_allowed(segment["expression_pace"], schema["enums"]["segment.expression_pace"], f"{segment['segment_id']}.expression_pace")
        assert_allowed(segment["timing"], schema["enums"]["segment.timing"], f"{segment['segment_id']}.timing")
        assert isinstance(segment["selected_for_image"], bool)
        if segment["role"] == "quoted_source":
            assert segment["cognitive_role"] == "quote_source"
            assert segment["visual_treatment"] == "quote-card-or-overlay"
        if segment["role"] == "host_voiceover" and segment["selected_for_image"]:
            selected_host_ids.add(segment["segment_id"])

    for shot in data["shots"]:
        for key in schema["shot_required"]:
            assert key in shot, f"shot {shot.get('shot_id')} missing {key}"
        assert shot["segment_id"] in selected_host_ids
        assert_allowed(shot["segment_role"], schema["enums"]["shot.segment_role"], f"{shot['shot_id']}.segment_role")
        assert shot["formats"] == schema["enums"]["shot.formats"]
        assert_allowed(shot["style_preset"], schema["enums"]["shot.style_preset"], f"{shot['shot_id']}.style_preset")
        assert_allowed(shot["expression_pace"], schema["enums"]["shot.expression_pace"], f"{shot['shot_id']}.expression_pace")
        assert_allowed(shot["timing"], schema["enums"]["shot.timing"], f"{shot['shot_id']}.timing")
        assert isinstance(shot["short_labels"], list)


def assert_prompt_policy(path: Path) -> None:
    prompts = (path / "image-prompts.md").read_text(encoding="utf-8")
    assert "Do NOT render Chinese characters" in prompts
    assert "Overlay labels for post-production only" in prompts
    assert "Short Chinese labels" not in prompts


def assert_no_b_images(data: dict) -> None:
    b_segments = {segment["segment_id"] for segment in data["segments"] if segment["role"] == "quoted_source"}
    shot_segments = {shot["segment_id"] for shot in data["shots"]}
    assert not (b_segments & shot_segments)
    assert all(segment["cognitive_role"] == "quote_source" for segment in data["segments"] if segment["role"] == "quoted_source")
    assert all(segment["visual_treatment"] == "quote-card-or-overlay" for segment in data["segments"] if segment["role"] == "quoted_source")


def main() -> int:
    schema = load_schema()
    tmp = Path(tempfile.mkdtemp(prefix="mrai-smoke-"))
    try:
        cases = [
            ("ai-technical-sb.md", "AI Technical Fixture", "4"),
            ("culture-person-sb.md", "Culture Person Fixture", "4"),
            ("quote-heavy-sb.md", "Quote Heavy Fixture", "3"),
            ("mixed-brand-explainer-sb.md", "Mixed Brand Explainer Fixture", "3"),
        ]
        for fixture, title, max_shots in cases:
            out = tmp / fixture.removesuffix(".md")
            run("gen", str(FIXTURES / fixture), "--out", str(out), "--title", title, "--style", "auto", "--max-shots", max_shots)
            data = load_map(out)
            assert_av_map_schema(data, schema)
            assert data["shots"], fixture
            assert all(shot["formats"] == ["16x9", "9x16"] for shot in data["shots"])
            assert all("cognitive_role" in segment for segment in data["segments"])
            assert all("expression_pace" in segment for segment in data["segments"])
            assert all("visual_purpose" in segment for segment in data["segments"])
            assert all("timing_hint" in segment for segment in data["segments"])
            assert all("cognitive_role" in shot for shot in data["shots"])
            assert all("expression_pace" in shot for shot in data["shots"])
            assert_no_b_images(data)
            assert_prompt_policy(out)

        mixed = tmp / "mixed-brand-explainer-sb"
        mixed_styles = [shot["style_preset"] for shot in load_map(mixed)["shots"]]
        assert "brand" in mixed_styles
        assert "explainer-sketch" in mixed_styles

        forced = tmp / "forced"
        run("gen", str(FIXTURES / "culture-person-sb.md"), "--out", str(forced), "--style", "auto", "--max-shots", "2", "--segments", "S3,S4")
        assert [shot["segment_id"] for shot in load_map(forced)["shots"]] == ["S3", "S4"]

        preferred = tmp / "preferred"
        run("gen", str(FIXTURES / "culture-person-sb.md"), "--out", str(preferred), "--style", "explainer-sketch", "--max-shots", "2", "--prefer-layout", "Evidence Clamp")
        assert all(shot["structure_type"] == "Evidence Clamp" for shot in load_map(preferred)["shots"])
    finally:
        shutil.rmtree(tmp)

    print("mrai CLI smoke tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
