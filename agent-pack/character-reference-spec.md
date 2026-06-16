# Character Reference Spec

This spec defines the default subject reference image for Mr.Ai image-to-image generation.

## Default Asset

- Path: `assets/brand-references/MrAi_character_ref.png`
- Purpose: subject reference for MiniMax/image-01 or other image backends.
- Status: V1.1.3 candidate reference. It may be replaced without changing CLI behavior.

## Required Visual Traits

- One Mr.Ai character only.
- Plain white or transparent background.
- No `Mr.Ai` text, no logo letters, no TM mark, no watermark, no props.
- Front-facing neutral pose.
- Full body or clean half body, with generous padding.
- Compact rounded proportions, not tall and slim.
- Friendly middle-aged male feeling, not childlike.
- Baseball cap with curved brim.
- Dark or gray mustache.
- Blue collared shirt or clear blue upper-body clothing.
- Yellow brand accent on cap or clothing.
- Thick clean dark outline.
- Smooth logo-like cartoon shading.

## Avoid

- Anime styling.
- Realistic portrait styling.
- Business suit or formal presenter styling.
- Robot, monk, mascot animal, or childlike redesign.
- Any in-image text, labels, symbols, UI, badges, or decorative marks.
- Large colored background that may be interpreted as part of the character.

## QA Checklist

Use this checklist before making an asset the default reference:

- Cap, mustache, blue clothing, and yellow accent are visible at thumbnail size.
- Face shape and body proportions feel close to `MrAi_logo.png`.
- No text-like pixels are present.
- Character is centered and not cropped.
- White/transparent background dominates.
- The image can be used as `subject_reference` without asking the model to copy a logo composition.

## Replacement Rule

If a better reference image is created, replace `MrAi_character_ref.png` in place and rerun the subject-reference baseline. Cache keys include the reference-image hash, so new jobs will not collide with old reference outputs.
