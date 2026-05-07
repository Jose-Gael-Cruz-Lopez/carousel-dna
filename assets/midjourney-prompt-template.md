# Midjourney / AI image-generation prompt template

## When to use this template

Select this template when the user mentions any of: **"Midjourney," "MJ," "image AI," "image generation," "DALL-E," "Stable Diffusion," "Flux," or "mood board."** It is the right tool when they want to generate imagery in a captured creator's style — typically for mood-boarding before opening Figma to lay out the carousel itself.

Output goes **inline** in the conversation. Do not write to a file unless the user asks. The user will paste the generated prompts directly into their image tool of choice.

---

## General prompt-engineering rules for IG-carousel-style imagery

These hold across every prompt produced from this template:

- **Aspect ratio.** Always include `--ar 4:5` (the default IG carousel canvas, per `references/visual-vocabulary.md` → Layout & grid → Canvas conventions). For 1:1 carousels, swap to `--ar 1:1`. Never produce a 16:9 image for a carousel.
- **Style locks — every prompt must include all four.** The image will drift without them:
  - `<art-direction>` — e.g. "editorial finance," "ceramic terracotta wellness," "brutalist tech."
  - `<photography style or 3D render>` — e.g. "35mm film photography," "Spline 3D render," "matte vector illustration."
  - `<color palette>` — name the harmony and 2-3 hex codes when supported.
  - `<lighting>` — e.g. "soft window light, no harsh shadows," "studio rim light, single key."
- **Negative-prompt list (carousel-killers).** Append to every prompt: `--no text, watermark, low quality, blurry`. Text in AI-generated images is almost always garbled — do the typography in Figma, not in MJ.
- **Consistency across slides.** Lock the same `--seed <N>` and `--style <reference or value>` for every prompt in a single carousel. Vary only the **subject**, never the style suffix. This is the difference between a coherent carousel and a slideshow of different aesthetics.

---

## Per-slide prompt template

Fill in the bracketed values from the creator's Schema A entry (`palette.harmony`, `palette.signature`, `imagery.treatment`, `typography.headline.casing`-derived tone, etc.). Drop the filled template into the conversation — the user copies each prompt block to their image tool.

```
Style basis: <@creator's style DNA, generated YYYY-MM-DD>

## Locked style suffix (append to every prompt)
"<art-direction phrase>, <texture/grade>, <palette description with hex codes when MJ supports them>, <lighting>, <camera/lens if photo-style>" --ar 4:5 --no text, watermark --seed <N> --style <ref>

## Slide 1 — Cover
Subject: <description>
Prompt:
"<subject>, <style suffix>"

## Slide 2 — <role, e.g. "rule one" / "the problem" / "evidence">
Subject: <description>
Prompt:
"<subject>, <style suffix>"

## Slide N — <role>
Subject: <description>
Prompt:
"<subject>, <style suffix>"

## Reroll guidance
- If MJ outputs are too saturated, append `--stylize 100` (default is 100; lower toward 50 pulls back stylization further).
- If composition wanders, add specific camera language: `eye-level, centered subject, negative space upper-third`. Mirror the carousel's `layout.focal_placement` from the Schema A entry.
- If the color palette drifts, name 2-3 hexes explicitly in the suffix (e.g. "warm-neutral palette: #F4EFE6, #1A1A1A, #C8A24B"). MJ v6+ responds reasonably to hex callouts; earlier versions ignore them — fall back to named colors ("ivory, charcoal, antique gold").
- If subjects feel generic, add a **specificity anchor**: a real-world referent ("the way light falls in a Wes Anderson interior," "Aperture-magazine print quality," "Kinfolk-issue still-life"). Use sparingly — one anchor per prompt.
```

---

## Tool-specific syntax notes

Different tools accept different flags. Translate the suffix for the user's actual tool — do not paste MJ flags into Flux.

- **Midjourney v6+**: full flag support. `--style raw` produces less-stylized, more photographic outputs — useful when the captured style is journalistic/documentary rather than editorial-glossy. Combine with `--stylize 50-100` for restraint.
- **Flux / DALL-E 3**: do **not** support `--ar` or `--no` flags. Phrase aspect ratio as a prose direction: `"vertical 4:5 composition, IG carousel format"`. Express negatives as positives: instead of `--no text`, write `"clean image with no overlaid text or watermarks."`
- **Stable Diffusion via Forge / A1111 / ComfyUI**: drop all MJ flags. Aspect ratio is set in the UI (width/height fields). The prompt body itself works as written; negative prompts go in the dedicated negative-prompt field, not the main prompt.
- **Ideogram / Recraft**: handle text moderately well, but for IG carousels still let Figma own the typography. Use the same suffix discipline as MJ.

**If the user has not specified which model they're on, ask.** Do not guess from context — getting this wrong wastes their generations. A single clarifying question ("Which image tool — MJ, Flux, DALL-E, or SD?") is the right move.

---

## When NOT to use AI imagery for a carousel

Skip this template entirely and redirect the user to the Figma template (`assets/figma-prompt-template.md`) when the captured style is one of the following:

- **Typography-only carousels.** If the Schema A entry has `imagery.type: none` across the creator's full library and `integration.text_image_relation: text-driven` or `typography-as-image`, AI imagery will only get in the way. The style *is* the type.
- **Screenshot- or mockup-driven.** If `imagery.type` is dominantly `screenshot` or `mockup-device` (per `references/visual-vocabulary.md` → Imagery treatment → Type tags), the user needs real screenshots and device frames, not AI hallucinations of UIs.
- **Data-viz carousels.** AI image tools can't draw accurate charts. Build these in Figma or a charting tool.
- **Tight motif systems** (e.g. numbered-rule editorial layouts where every slide is a numbered card on a flat field). The motifs *are* the design — AI imagery muddies them.

In any of these cases, name the reason ("This creator's style is typography-driven; AI imagery would dilute the look") and hand off to the Figma template instead.
