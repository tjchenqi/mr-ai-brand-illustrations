#!/usr/bin/env python3
"""Smoke tests for the mrai CLI contract.

These tests do not judge image beauty. They protect the production contract:
S/B parsing, machine-readable AV maps, blank-text prompt policy, and overrides.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BIN = ROOT / "bin" / "mrai"
FIXTURES = ROOT / "tests" / "fixtures"


def run(*args: str, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    command_env = {**os.environ, **(env or {})}
    return subprocess.run([str(BIN), *args], cwd=ROOT, check=True, text=True, capture_output=True, env=command_env)


def run_unchecked(*args: str, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    command_env = {**os.environ, **(env or {})}
    return subprocess.run([str(BIN), *args], cwd=ROOT, check=False, text=True, capture_output=True, env=command_env)


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


def assert_safe_areas(result: dict) -> None:
    for area in result["safe_areas"]:
        for key in ["x", "y", "w", "h"]:
            assert 0 <= area[key] <= 1
        assert area["x"] + area["w"] <= 1.0001
        assert area["y"] + area["h"] <= 1.0001


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
            run("validate", str(out))
            assets_output = run("assets", str(out)).stdout
            assert "9x16:" in assets_output
            assert "missing" in assets_output
            data = load_map(out)
            assert data["shots"], fixture
            assert all(shot["formats"] == ["16x9", "9x16"] for shot in data["shots"])
            assert all(
                shot["asset_slots"] == {
                    "16x9": f"16x9/{shot['shot_id']}-16x9.png",
                    "9x16": f"9x16/{shot['shot_id']}-9x16.png",
                }
                for shot in data["shots"]
            )
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

        records_out = tmp / "records-job"
        submit = run(
            "submit",
            str(FIXTURES / "b-records-valid.json"),
            "--out",
            str(records_out),
            "--job-root",
            str(tmp),
            "--backend",
            "mock",
            "--retries",
            "1",
        )
        submitted = json.loads(submit.stdout)
        job_id = submitted["job_id"]
        pending = json.loads(run("query", job_id, "--root", str(tmp)).stdout)
        assert pending["status"] == "pending"
        assert pending["results"] == []
        assert pending["remotion_manifest"] == []

        completed = json.loads(run("run", job_id, "--root", str(tmp)).stdout)
        assert completed["status"] == "completed"
        assert completed["progress"]["total"] == 3
        assert completed["progress"]["completed"] == 2
        assert completed["progress"]["failed"] == 1
        assert completed["results"][0]["s_id"] == "S01"
        assert completed["results"][0]["beat_ref"] == "beat-001"
        assert completed["results"][0]["image_path"].endswith("S01_v1_9x16.png")
        assert completed["results"][0]["version"] == 1
        assert completed["results"][0]["cache_hit"] is False
        assert completed["results"][0]["format"] == "9x16"
        assert completed["results"][0]["usable"] is False
        assert completed["results"][0]["overlay_labels"] == ["判断", "工具", "人"]
        assert "Do NOT render any text" in completed["results"][0]["generation_meta"]["prompt"]
        assert completed["results"][0]["generation_meta"]["reference_image"].endswith("assets/brand-references/MrAi_logo.png")
        assert completed["results"][0]["generation_meta"]["subject_ref_requested"] is False
        assert completed["results"][0]["qa_status"] == "needs_human_review"
        assert completed["results"][1]["image_path"].endswith("S02_v1_16x9.png")
        assert completed["results"][2]["error_code"] == "provider_failed"
        assert_safe_areas(completed["results"][0])
        queried_completed = json.loads(run("query", job_id, "--root", str(tmp)).stdout)
        assert queried_completed["remotion_manifest"][0]["s_id"] == "S01"
        assert queried_completed["remotion_manifest"][0]["format"] == "9x16"
        assert queried_completed["remotion_manifest"][0]["usable"] is False

        submit_cached = run(
            "submit",
            str(FIXTURES / "b-records-valid.json"),
            "--out",
            str(records_out),
            "--job-root",
            str(tmp),
            "--backend",
            "mock",
        )
        cached_job_id = json.loads(submit_cached.stdout)["job_id"]
        cached = json.loads(run("run", cached_job_id, "--root", str(tmp)).stdout)
        assert cached["results"][0]["cache_hit"] is True
        assert cached["results"][0]["version"] == 1

        fake_bin = tmp / "fake-bin"
        fake_bin.mkdir()
        fake_mmx = fake_bin / "mmx"
        fake_mmx.write_text(
            """#!/bin/sh
out_dir=""
out_prefix=""
has_ref=0
while [ "$#" -gt 0 ]; do
  case "$1" in
    --out-dir) shift; out_dir="$1" ;;
    --out-prefix) shift; out_prefix="$1" ;;
    --subject-ref) has_ref=1; shift ;;
  esac
  shift
done
if [ "$has_ref" = "1" ]; then
  exit 17
fi
mkdir -p "$out_dir"
printf "fake image" > "$out_dir/${out_prefix}_001.jpg"
""",
            encoding="utf-8",
        )
        fake_mmx.chmod(0o755)
        fake_env = {"PATH": f"{fake_bin}{os.pathsep}{os.environ.get('PATH', '')}"}
        mmx_records = tmp / "mmx-records.json"
        mmx_records.write_text(
            json.dumps(
                {
                    "records": [
                        {
                            "s_id": "S09",
                            "audience_takeaway": "验证 subject-ref 失败时可以有痕迹地降级。",
                            "visual_intent": "actor_top_subtitle_bottom, Mr.Ai above a blank subtitle area",
                            "format": "9x16",
                        }
                    ]
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        submit_mmx = run(
            "submit",
            str(mmx_records),
            "--out",
            str(tmp / "records-mmx"),
            "--job-root",
            str(tmp),
            "--backend",
            "mmx",
            "--retries",
            "0",
            "--timeout-seconds",
            "5",
            env=fake_env,
        )
        mmx_job_id = json.loads(submit_mmx.stdout)["job_id"]
        mmx_completed = json.loads(run("run", mmx_job_id, "--root", str(tmp), env=fake_env).stdout)
        mmx_result = mmx_completed["results"][0]
        assert mmx_result["qa_status"] == "warning"
        assert mmx_result["usable"] is True
        assert mmx_result["composition_template_id"] == "actor_top_subtitle_bottom"
        assert mmx_result["generation_meta"]["subject_ref_requested"] is True
        assert mmx_result["generation_meta"]["subject_ref_used"] is False
        assert mmx_result["generation_meta"]["subject_ref_failed"] is True

        submit_force = run(
            "submit",
            str(FIXTURES / "b-records-valid.json"),
            "--out",
            str(records_out),
            "--job-root",
            str(tmp),
            "--backend",
            "mock",
            "--force",
        )
        force_job_id = json.loads(submit_force.stdout)["job_id"]
        forced_results = json.loads(run("run", force_job_id, "--root", str(tmp)).stdout)
        assert forced_results["results"][0]["cache_hit"] is False
        assert forced_results["results"][0]["version"] == 2

        missing = run_unchecked("submit", str(FIXTURES / "b-records-missing-required.json"), "--out", str(tmp / "bad"), "--backend", "mock")
        assert missing.returncode == 1
        assert "invalid_record" in missing.stdout
        both = run_unchecked("submit", str(FIXTURES / "b-records-format-both.json"), "--out", str(tmp / "both"), "--backend", "mock")
        assert both.returncode == 1
        assert "format=both is not supported" in both.stdout
        bad_ref = run_unchecked("submit", str(FIXTURES / "b-records-missing-reference.json"), "--out", str(tmp / "bad-ref"), "--backend", "mock")
        assert bad_ref.returncode == 1
        assert "reference_image not found" in bad_ref.stdout
    finally:
        shutil.rmtree(tmp)

    print("mrai CLI smoke tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
