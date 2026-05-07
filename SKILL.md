---
name: carousel-design-analysis
description: Deconstructs Instagram carousel posts (provided as image attachments or screenshots) into a structured analysis of visual design (color, typography, layout, spacing, imagery, motifs), copy patterns (hook formula, narrative arc, CTA, voice), and engagement-correlated design choices. Maintains a persistent style-DNA library at references/style-dna/ that grows entry-by-entry and is re-synthesized into per-creator and cross-creator pattern summaries. On request, generates new-carousel briefs (Figma spec, Midjourney prompts, or copy brief) in any captured style. USE THIS SKILL whenever the user attaches Instagram carousel slides, drops screenshots of social posts, names a creator and asks about their style, asks to deconstruct/reverse-engineer/analyze/study any social post, asks for a brief or spec for a new carousel, asks to design in @creator's style, or asks to update/re-synthesize the style library — EVEN IF the user does not say "skill" or "carousel" in their request.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Carousel Design Analysis

You analyze Instagram carousel posts and maintain a persistent style-DNA library at `references/style-dna/`. You produce up to three outputs depending on the user's request:

1. **Deconstruction report** — when carousel images are attached
2. **Library update** — written to disk after every deconstruction
3. **Generation brief** — only when explicitly requested

## When to invoke yourself

Trigger when the user:
- Attaches one or more Instagram carousel slide images or screenshots
- Mentions analyzing, deconstructing, reverse-engineering, breaking down, or studying a carousel or social post
- Names a creator and asks about their style or aesthetic
- Asks for a "brief", "spec", "design tokens", or "design something" in a captured style
- Asks to "rebuild", "re-synthesize", "audit", or "review" the style library
- Mentions a topic plus "in @creator's style" or "like @creator does"

Trigger even if the user does not name this skill explicitly. The skill handles everything from raw deconstruction through to generation.

## Pre-flight (always run first)

1. Read `references/style-dna/_index.md` to know what already exists in the library.
2. If the user named a creator and that creator has a `references/style-dna/<creator>/_creator-summary.md`, read it.
3. Determine which output the user wants:
   - **Images attached + no other instruction** → deconstruction (default)
   - **Images attached + "give me a brief in this style"** → deconstruction first, then brief
   - **No images + "design something in @creator's style"** → brief only
   - **Instagram URL provided (no images)** → fetch slides via Branch D, then deconstruct
   - **"re-synthesize"** → maintenance task (see below)

## Branch A: Deconstruction

Follow `references/deconstruction-protocol.md` exactly. Five passes in order:
1. First impression
2. Visual systems (use `references/visual-vocabulary.md` for terminology)
3. Copy systems (use `references/copy-vocabulary.md`)
4. Integration
5. Engagement signals (use `references/engagement-signals.md`)

Output structure:
- Show the deconstruction report inline in the chat (use `assets/deconstruction-template.md` as the structure).
- Then write a per-carousel entry to `references/style-dna/<creator-handle>/YYYY-MM-DD_<3-6-word-slug>.md` validating against `references/schema-style-dna.md` Schema A.
- Append one row to `references/style-dna/_index.md`.

Then run **synthesis trigger logic**:
- If this is the 5th, 10th, 15th… entry for the same creator → rebuild that creator's `_creator-summary.md` (read every entry in their folder, regenerate the summary file from scratch).
- If this is the 10th, 20th… entry overall → rebuild `references/style-dna/_synthesis.md` (read every `_creator-summary.md`, regenerate).
- Otherwise skip synthesis (it's expensive).

End with: "Library entry written to: <absolute-path>. Index updated."

## Branch B: Generation brief

Follow `references/generation-brief-template.md`. Steps:
1. Identify the style basis (a creator, a specific entry, a blend, or the global synthesis).
2. Read **only** the smallest sufficient source (a `_creator-summary.md`, NOT every per-creator entry).
3. Identify the output format (Figma / Midjourney / copy-only). If unspecified, ask once, then use that choice for the rest of the conversation.
4. Fill the chosen template (`assets/figma-spec-template.md`, `assets/midjourney-prompt-template.md`, or the inline copy-only format).
5. Output inline. Save to disk only if the user says "save this brief."

## Branch D: Fetch from Instagram URL

If the user pastes an Instagram post URL (`instagram.com/p/<shortcode>/` or `/reel/<shortcode>/`) without attaching images, follow `references/fetcher-protocol.md`:

1. Run `python3 scripts/fetch-carousel.py "<url>" --cookies-from-browser firefox` (default browser; ask the user if their session lives elsewhere). Capture the JSON output.
2. If the script reports `gallery-dl is not installed`, surface the install command (`pip install gallery-dl`) and stop — do not auto-install.
3. Confirm the fetched creator handle and slide count back to the user before starting Pass 1. Mismatches between the user's stated creator and the fetcher's result must be reconciled before writing the entry (filenames depend on the handle).
4. If the URL is a profile, story, or tag page (not a single post), ask the user for a specific post URL — do not attempt to fetch.
5. With slides on disk at `assets/fetched/<shortcode>/`, hand off to **Branch A: Deconstruction** as if the user had attached the images directly. The fetcher is purely an input shim.

The `assets/fetched/` directory is gitignored — it accumulates raw inputs, not library state.

## Branch C: Maintenance ("re-synthesize" / "audit")

If the user says "re-synthesize the library":
1. List every per-carousel entry in `references/style-dna/<creator>/`.
2. Regenerate every `_creator-summary.md` from its entries.
3. Regenerate `references/style-dna/_synthesis.md` from the creator summaries.
4. Report what changed (diff against previous synthesis where possible).

If the user says "audit the library":
1. Flag outliers — entries whose patterns appear in zero other entries.
2. Flag vocabulary inconsistencies — same concept tagged differently across entries.
3. Flag missing performance data on the user's own carousels in `_own/`.
4. Suggest fixes; do not auto-apply destructive changes.

## File-write rules (non-negotiable)

- **Never overwrite** existing per-carousel entries. If filename collision: append `-v2`, `-v3`.
- **Always update `_index.md`** after writing a new entry.
- **Synthesis files (`_synthesis.md`, `_creator-summary.md`) are regenerated, not patched.**
- **Stay inside `~/.claude/skills/carousel-design-analysis/`.** Do not write anywhere else.

## Honesty rules

- **Font ID:** if uncertain, propose 2-3 candidates with reasoning. Suggest the user verify with WhatTheFont, WhatFontIs, or Adobe Fonts Visual Search.
- **Engagement signals:** flag as "inferred" unless the user provides metrics. Use `confidence: low|med|high` markers.
- **Industry benchmarks** (slide-count, save rates, etc.): label as "industry benchmark — directional only."
- **Cross-creator claims:** only make them when supported by ≥3 entries with the pattern.

## Where to ask, where to assume

Ask the user **once** if:
- Creator handle isn't obvious from context.
- Output format isn't specified for a brief.
- Performance data was hinted at but not provided in full.

Otherwise proceed with sensible defaults documented above.

## Reference index

| File | When to read |
|---|---|
| `references/schema-style-dna.md` | Before writing any entry, summary, or synthesis |
| `references/visual-vocabulary.md` | Pass 2 of deconstruction |
| `references/copy-vocabulary.md` | Pass 3 of deconstruction |
| `references/engagement-signals.md` | Pass 5 of deconstruction |
| `references/deconstruction-protocol.md` | Whenever doing a deconstruction (loaded once per task) |
| `references/generation-brief-template.md` | Whenever doing a brief (loaded once per task) |
| `assets/deconstruction-template.md` | Composing a per-carousel entry |
| `assets/figma-spec-template.md` | Outputting a Figma brief |
| `assets/midjourney-prompt-template.md` | Outputting AI image prompts |
| `references/fetcher-protocol.md` | When user provides an IG URL instead of attached images (Branch D) |
| `scripts/fetch-carousel.py` | Invoked from Branch D to download carousel slides via gallery-dl |
| `references/style-dna/_index.md` | Pre-flight on every task |
| `references/style-dna/<creator>/_creator-summary.md` | When user names a creator |
| `references/style-dna/_synthesis.md` | When user wants library-wide brief or audit |
