# Generation brief — orchestrator

This file is the orchestrator the `carousel-design-analysis` skill loads when the user wants Claude to **generate a new carousel brief in a captured style** — the second of the skill's three outputs. It does not describe how to deconstruct an existing carousel (that's the per-carousel entry path) and it is not the cross-creator synthesis (that's the `_synthesis.md` regenerator). It tells Claude which inputs to expect, which output template to choose, which style basis files to read, and how to compose a generation-ready brief without bloating context or overstating what the captured style supports.

---

## 1. Purpose

Invoke this protocol whenever the user requests a brief, a design spec, design tokens, a writing brief, or asks Claude to "design something in @creator's style," "spec a carousel about <topic>," "give me a Midjourney mood board for <topic> in @creator's voice," or any equivalent phrasing. The deliverable is a generation-ready output — a Figma spec, an AI-image prompt set, or a copy-only brief — that a designer or writer can use immediately. It is **not** a deconstruction of an existing post; that path lives in the per-carousel entry protocol and produces a Schema A entry. If the user's request is to *analyze*, route to the deconstruction protocol instead.

---

## 2. Inputs

The protocol expects two pieces of information from the user (ask for whichever is missing):

- **Topic** for the new carousel — e.g. `"study habits for first-gen students"`, `"7 portfolio mistakes junior designers make"`, `"how to read a credit-card statement."`
- **Style basis** — exactly one of:
  - **A specific creator** (`@jenny.example`) → read that creator's `references/style-dna/<handle>/_creator-summary.md`.
  - **A specific carousel entry** → read that single Schema A entry file at `references/style-dna/<handle>/YYYY-MM-DD_<slug>.md`.
  - **A blend of two creators** (`@jenny.example + @marc.example`) → read both `_creator-summary.md` files and blend their consensus fields.
  - **"My own style"** → read `references/style-dna/_own/_creator-summary.md` if it exists; if it doesn't, tell the user the own-style summary hasn't been generated yet and ask whether they want to fall back to a single carousel entry from `_own/` or another creator.
  - **The full library synthesis** → read `references/style-dna/_synthesis.md` only.
- **Output format preference** — Figma spec / Midjourney prompts / pure copy brief. If the user does not specify, default to **Figma**.

---

## 3. Output format selection

Match on the user's phrasing, in this order:

| User says | Use |
|---|---|
| "Figma," "design spec," "design tokens," "give me a brief," "spec this out," "style guide for a new carousel" | `assets/figma-spec-template.md` |
| "Midjourney," "MJ," "image AI," "image generation," "DALL-E," "Stable Diffusion," "Flux," "mood board" | `assets/midjourney-prompt-template.md` |
| "copy," "just the words," "writing brief," "copy brief," "no design — just the headlines" | inline copy-only format (see section 6) |
| Nothing — request was format-agnostic | default to Figma; ask once which they want, then remember for the rest of the conversation |

If the user names two formats ("Figma spec **and** MJ prompts"), produce both, Figma first.

---

## 4. Style-basis loading — read the smallest sufficient source

Loading more than necessary bloats context and produces vaguer briefs. Apply this rule strictly:

- **Single-creator brief** → read **only** that creator's `_creator-summary.md`. Do not also read individual carousel entries — the summary is already the synthesis. The per-entry files are for deconstruction work, not generation.
- **Single-carousel brief** (user pinned one specific post as the basis) → read **only** that one Schema A entry file.
- **Blend** (`@a + @b`) → read **both** `_creator-summary.md` files. Do not read either creator's individual entries.
- **Library-wide brief** ("in the house style," "anything that fits the library," "blend the whole archive") → read **only** `references/style-dna/_synthesis.md`.
- **Own style** → read `references/style-dna/_own/_creator-summary.md`. Only fall back to individual `_own/` entries if the summary doesn't exist yet.

If a referenced file is missing, surface the gap to the user before composing — don't fabricate consensus fields.

---

## 5. Brief generation steps

1. **Read the style basis.** Use the rule from section 4 — smallest sufficient source.
2. **Read the chosen output template.** Either `assets/figma-spec-template.md`, `assets/midjourney-prompt-template.md`, or apply the inline copy-only format from section 6.
3. **Read schema field definitions** at `references/schema-style-dna.md` long enough to confirm token names line up (palette role names, typography style names, hook-formula tags, narrative-arc beats). Briefs that invent token names break downstream consistency.
4. **Compose.** Replace every `<placeholder>` in the chosen template with values derived from the style basis plus the topic. When the template asks for a count or range (slide count, font size range, motif count), pull the value from the captured style's typical range, not an industry default.
5. **Honesty pass.** If the topic genuinely does not fit the style — e.g. the user asks for a "soft wellness" brief in a "brutalist tech" creator's voice, or a data-heavy explainer in a typography-only style — surface the mismatch in **Notes for the designer** (Figma), in a leading paragraph (Midjourney), or in a `## Style mismatch` block (copy-only). Do not silently smooth over the conflict, and do not refuse the brief outright; describe what will and won't compose, and let the user decide.

---

## 6. Pure copy brief format

When the user wants copy only ("just the words," "writing brief"), skip the asset templates and produce this inline format. Drop sections that don't apply rather than leaving stub lines.

```markdown
# <topic> — Copy brief
Style basis: <source, generated YYYY-MM-DD>
Slide count: <N>
Voice: <tone tags from style basis, e.g. "frank, elder-mentor">
Person: <first-person | second-person | third-person | mixed>

## Cover
Hook: "<11-word max headline>"
Hook formula: <tag from style basis, e.g. "numbered-list + age-regret">

## Slide 2 (must work as cover)
Headline: "<text>"
Body: "<short>"

## Slides 3 to N-1
### Slide 3 — <role>
Headline: "<text>"
Body: "<text>"

### Slide 4 — <role>
[...]

## CTA slide
Text: "<exact CTA copy>"
Type: save-prompt | share-prompt | follow-prompt

## Notes for the writer
<Mismatches between topic and style; spots where the captured voice has to stretch.>
```

---

## 7. What the brief MUST include — regardless of format

Every brief produced by this protocol must satisfy all of the following:

- **Slide count** drawn from the captured style's typical range. If the style basis is a creator summary with `slide_count` ranging across entries, pick within that range; if it's a single-entry basis, match the entry's count or note when deviating.
- **Cover hook ≤ 11 words.** This is the industry benchmark for IG carousel hooks (cite as such — say "11-word industry benchmark," not as if it's a Claude rule).
- **Slide-2 standalone strength.** Slide 2 must read as a cover hypothetically — assume the algorithm will sometimes show slide 2 first. Validate by reading slide 2 in isolation and asking: would this stop a thumb on its own?
- **At least one save-bait slide.** A framework, checklist, comparison, or numbered rule-stack — something with reference value the reader will want to come back to.
- **Explicit CTA on the final slide.** Not "follow for more" by default — match the CTA `type` and `placement` from the style basis.
- **Motif system that mirrors the style basis.** Pull the signature motifs from `creator_summary.signature_motifs` (or the equivalent field in the chosen basis) and enforce them across slides in the brief.

---

## 8. What the brief should NOT do

- **Don't invent fonts** that don't appear in the captured style. If the basis declares `Inter + GT Sectra`, do not silently substitute `Roboto` or `Playfair`. If the user wants a font extension, ask explicitly.
- **Don't add color tokens** outside the captured palette (`palette.background`, `palette.primary_text`, `palette.accent`, `palette.signature`). Extending the palette requires the user's explicit ask.
- **Don't promise engagement outcomes.** Phrases like "this will go viral," "guaranteed to hit," or "high save rate" are out. Briefs describe design choices; performance is the user's to measure. Use `engagement_inferred` qualitatively ("structured for high save-bait") rather than as a forecast.
- **Don't output to disk by default.** Briefs are conversational artifacts unless the user says "save it" or names a target path. Inline-by-default keeps the working library uncluttered and the brief reviewable in chat.

---

## 9. Saving briefs (opt-in)

Only save when the user explicitly says "save this brief," "write it to disk," or names a path.

- **Path:** `references/style-dna/_blends/YYYY-MM-DD_<topic-slug>_brief.md`. Slug rules match the schema's filename convention: lowercase, hyphenated, 3–6 words, drop non-meaningful stopwords, replace numerals with digits, append `-v2` / `-v3` on collision.
- **YAML frontmatter** at the top of the saved file:
  ```yaml
  entry_type: brief
  basis: <source — e.g. "@humphreytalks _creator-summary.md" or "_synthesis.md">
  topic: <topic>
  generated_on: <ISO date>
  ```
- **Index update:** append a row to `references/style-dna/_index.md` with `entry_type: brief`. Match the existing column order in `_index.md`; if the index hasn't introduced a `brief` row before, add `entry_type: brief` to the type column rather than reformatting the file.

Saved briefs do not replace creator summaries or synthesis files. They are downstream artifacts and live in `_blends/` so they don't pollute per-creator folders.

---

## 10. Honesty disclaimer — append to every brief

Every brief produced by this protocol ends with the following line, with `<synthesis-date>` replaced by the `generated_on` date of the style-basis file (the `_creator-summary.md`, the entry, or `_synthesis.md`):

> This brief reflects the captured style as of `<synthesis-date>`. Update synthesis files if you've added new entries since.

If the style basis is a blend, list both source dates. If it's a single carousel entry rather than a summary, use that entry's `analyzed_on` date and add a parenthetical: "(based on a single entry, not a full creator synthesis)."
