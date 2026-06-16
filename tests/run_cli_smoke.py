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


def run(*args: str) -> None:
    subprocess.run([str(BIN), *args], cwd=ROOT, check=True)


def load_map(path: Path) -> dict:
    return json.loads((path / "audio-visual-map.json").read_text(encoding="utf-8"))


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
