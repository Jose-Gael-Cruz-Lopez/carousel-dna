# Deconstruction Protocol

## 1. Purpose

This file is the **canonical workflow** for deconstructing a carousel into a Schema A entry. It is the orchestrator: the schema (`schema-style-dna.md`) defines the slots, the vocabularies (`visual-vocabulary.md`, `copy-vocabulary.md`, `engagement-signals.md`) define the legal contents, and the template (`assets/deconstruction-template.md`) defines the literal output skeleton — this file tells you the order in which to walk a carousel so that the right values land in the right slots.

**Always run all 5 passes, in order.** Do not skip passes even if the user is impatient, and do not start filling YAML out-of-order because one slide's color jumped out at you. Order matters for output comparability: every entry in the library was produced by walking these passes in this sequence, so the cross-creator synthesis only works if new entries arrive on the same conveyor belt. If a pass yields nothing usable (e.g., a 1-slide post has no narrative arc), record `null` and a one-line note in the body — don't skip ahead.

---

## 2. Inputs

The protocol expects:

- **1 to N image attachments** representing the carousel slides, **ordered slide 1 → slide N**. If the user pastes them out of order or in a single grid image, ask once for the canonical slide order before starting Pass 1.
- **Optionally: a creator handle** (e.g., `@jenny.example`). If the handle is not provided and is not obvious from a watermark, footer, or username chyron in the slides, **ask once** before Pass 1. Without a handle the entry cannot be filed correctly (the filename pattern is `<creator-handle>/YYYY-MM-DD_<slug>.md`).
- **Optionally: performance metrics** (reach, saves, shares, comments, swipe-through rate, etc.). These only make sense for the user's own posts. If the user provides them, capture verbatim and pass them through to the `performance:` block in Pass 5. For third-party creators, leave the entire `performance:` block as `null` per Schema A.

If exactly one image is provided, treat it as a 1-slide carousel and warn in the body prose that single-image posts forfeit most carousel-specific signals (slide-2 standalone test is moot, swipe cliffhangers are moot, slide-count zone is automatically "under").

---

## 3. Pass 1 — First impression (5 seconds, 1 sentence)

Capture the gestalt **before** analysis muddles it. Once you start naming hex codes and counting words, the felt-sense of the carousel evaporates — that felt-sense is itself a data point about how a viewer in feed will react, so harvest it first.

Write **exactly one sentence** answering: *"What does this feel like?"*

- Use sensory or emotional language, not analytical language. "Feels like a Sunday-morning newsletter" is better than "warm palette with serif headline."
- Do not list features. One sentence, one impression.

Then write **one `creator_aesthetic_tag` proposal** as a lowercase-hyphenated slug. Examples:

- `editorial-finance-femme`
- `brutalist-tech`
- `soft-wellness`
- `gallery-quote`
- `productivity-corporate`

The tag is a hypothesis, not a verdict — Pass 2 may refine it. Park it for now.

**Do not start filling in the YAML yet.** No hex codes, no font guesses, no word counts. If you find yourself reaching for the template in Pass 1, stop and force the gestalt sentence first.

---

## 4. Pass 2 — Visual systems

Walk these subsections **in order**, using `visual-vocabulary.md` for terminology. The output of this pass is the filled-in `palette`, `typography`, `layout`, `imagery`, and `motifs` blocks of the deconstruction template.

### 4.1 Color

Extract **5–7 swatches** that account for ≥95% of the visible canvas across all slides combined. For each:

- Hex code (6-digit uppercase per schema).
- Role: `background`, `primary_text`, `accent`, or `signature`. Roles are functional ("what does this color *do*") not positional. See `visual-vocabulary.md` → Color → Hex extraction and role assignment.
- Harmony classification of the overall palette: pick exactly one structural type from `monochromatic | analogous | complementary | split-complementary | triadic | tetradic | achromatic | unstructured`. Combine with an emotional descriptor for `palette.harmony` (e.g., `"warm-neutral-with-gold"`).
- WCAG contrast pairs: list every text/background combination used in the carousel with `wcag_ratio` and `wcag_level` (`AAA`, `AA`, `AA Large`, or `FAIL`). See `visual-vocabulary.md` → Color → WCAG contrast.

Note in body prose if the palette is **dirty** (grain, paper texture, halftone, film grade) vs **clean** (flat solid hexes). On dirty palettes, the extracted hex is an approximation of the dominant tone, not a literal pixel — flag this.

### 4.2 Typography

Identify or **propose 2–3 candidates** per family (headline, body) using the classification tree in `visual-vocabulary.md` → Typography. For each family record:

- `family.value` plus `family.confidence` (`low`, `med`, `high` — default `med` unless you have direct evidence).
- `fallbacks` (1–3 close cousins).
- `weight` (numeric 100–900, estimated from stroke thickness).
- `size_px` as a range across slides, or single int if uniform. Use the type-scale priors in the visual vocabulary.
- `tracking_em` (negative for tight display headlines, 0 for body, +0.05 to +0.15 for small-caps labels).
- `leading_ratio` (line-height as multiple of font size).
- `casing` (one of `title-case | uppercase | lowercase | sentence-case`).

If you cannot commit to a single font name, list 2–3 candidates in `family.value` and set `confidence: low`. Over-confident font calls are this skill's most common error — when in doubt, hedge.

### 4.3 Layout

Walk the alignment, margin, grid, balance, focal placement, and slide-rhythm:

- `alignment`: one of `left | center | right | justified | mixed`.
- `margin_pct`: outer margin as percentage of canvas width (typical 6–12%).
- `grid`: short descriptor (`single-column`, `two-column`, `loose-12-col`, `strict-6-col`, `masonry`, `none`).
- `balance`: `symmetric | asymmetric | radial`.
- `focal_placement`: `upper-third | center | lower-third | rule-of-thirds-left | rule-of-thirds-right | golden-ratio | edge-anchored`.
- `rhythm`: type (`templated | evolving | variant`) plus optional modifier (`varied-density`, `crescendo`, `call-and-response`, `uniform`).

### 4.4 Spacing

Detect the base unit (4 px or 8 px is most common — see `visual-vocabulary.md` → Spacing → Base-unit detection). Compute `whitespace_ratio` (0.0–1.0) and map to a band (`minimal <0.25`, `balanced 0.25–0.50`, `breathy 0.50–0.70`, `gallery >0.70`). Note vertical rhythm (consistent baseline grid vs free-form) in body prose if it's load-bearing for the creator's signature.

### 4.5 Imagery

- `imagery.type`: schema enum `none | photo | illustration | mixed | data-viz`.
- `imagery.treatment`: null if type is none; otherwise a treatment tag or `+`-stacked combo (e.g., `"warm-grade+grain"`).
- `imagery.icon_style`: `line | filled | duotone | hand-drawn | 3D | none | null`.

Use the finer-grained type tags from `visual-vocabulary.md` → Imagery treatment in body prose where the schema enum is too coarse.

### 4.6 Motifs

List **every recurring graphic device** observed: number chips, hairline rules, thick-bar dividers, bracket pairs, pull-quote frames, sparkles, hand-drawn arrows, highlight underlines, accent underlines, pricing tags, "NEW" badges, swipe-arrow indicators, page-number glyphs, etc.

**Apply the system-motif rule:** flag any motif appearing on **≥60% of slides** as a system motif and include it in `motifs[]`. Decorative motifs (<60%) only earn a slot in `motifs[]` if they are visually load-bearing on the slide where they appear (e.g., a swipe-arrow that only shows on the cover but anchors the cover composition). Otherwise omit.

### 4.7 Output

Fill in the `palette`, `typography`, `layout`, `imagery`, and `motifs` blocks of the deconstruction template. Keep all hex codes uppercase. Wrap inferred values as `{value: ..., confidence: low|med|high}`.

---

## 5. Pass 3 — Copy systems

Walk these subsections **in order**, using `copy-vocabulary.md` for terminology. The output of this pass is the filled-in `copy:` block.

### 5.1 Cover hook

Extract the cover headline **verbatim** into `copy.cover_hook`. Preserve casing and punctuation; do not paraphrase.

Classify with the **hook-formula taxonomy** (`copy-vocabulary.md` §1):

- `curiosity-gap`
- `contrarian`
- `listicle`
- `identity-callout`
- `bold-claim`
- `direct-question`
- `hybrid` (join two with `+`, dominant first, e.g., `listicle+regret`)

The tag string goes into `copy.hook_formula`. Do not invent new formula names — if nothing fits cleanly, pick the closest match and explain in body prose.

### 5.2 Word counts per slide

Count words for **every slide**, including the cover. Report as a list: `word_counts_per_slide: [11, 28, 24, 26, 25, 30, 18]`. The list length **must** equal `slide_count` — this is a schema validation rule.

Compute the mean and map to a copy-density band (`minimal <8`, `light 8–15`, `medium 15–25`, `dense 25–40`, `wall >40`) for body prose. Flag any single slide above ~50 words as a dwell-time risk per `engagement-signals.md` §10.

### 5.3 Narrative arc

Write the schematic for `copy.narrative_arc` using stage names from `copy-vocabulary.md` §2 stage glossary. Use spaced arrows ` → ` and `×N` for repetition. Examples:

- `Hook → Pain → Reframe → Steps×4 → CTA`
- `Hook → Promise → Listicle×7 → Recap → CTA`
- `Cover → Cliffhanger → Body → Save-prompt → Follow-CTA`

Cap arcs at **8 stages** — longer arcs usually mean the carousel is over-scoped. Coin new stage names only when no existing name fits.

### 5.4 CTA

Capture all three CTA fields:

- `cta.type`: schema enum `save | share | follow | comment | link-in-bio | none`.
- `cta.placement`: `final-slide | every-slide | none | inline`.
- `cta.copy`: the exact CTA text, verbatim, or `null`.

Note the **voice variant** in body prose: imperative ("Save this."), invitational ("If this helped, you might want to save it for later."), or question ("Want the rest? Comment 'yes.'"). See `copy-vocabulary.md` §4.

### 5.5 Voice

Fill in `copy.voice`:

- `tone`: a list combining a register (`academic | professional | casual | gen-z-internet | poetic`) with descriptors (e.g., `"frank"`, `"elder-mentor"`).
- `person`: `first-person | second-person | third-person | mixed`.
- `formality`: `casual-direct | formal | playful | academic | …`.

Capture the supporting markers in body prose: sentence-length profile (`short-punchy <10`, `medium 10–18`, `flowing >18`), emoji usage (`none | decorative-rare | functional-frequent | dense`), casing patterns (`title-case-headlines`, `sentence-case-body`, `all-caps-emphasis`, `all-lowercase-vibes`), and punctuation tics (`terminal-period-skip`, `em-dashes-emphasis`, `colons-for-setup`, `ellipses-cliffhanger`).

### 5.6 Output

Fill in the `copy:` block of the deconstruction template.

---

## 6. Pass 4 — Integration

This pass captures **how text and image relate** and **how the eye moves** through each slide. Output: the `integration:` block of the template.

### 6.1 Text–image relation

`integration.text_image_relation`: one of

- `text-driven` — text is the primary unit, imagery (if any) supports.
- `image-driven` — imagery carries the message, text is caption-grade.
- `balanced` — equal weight; both are doing primary work.
- `typography-as-image` — text is set so large or expressively that it functions as the image (Migra-poster, Druk-cover style).

When there is no imagery at all (`imagery.type: none`), the relation is almost always `text-driven` or `typography-as-image` — distinguish by whether the typography itself is doing decorative work.

Body-prose: note whether overlays are used (text on top of photo), text-beside-image arrangements, text-inside-shape devices (text inside a circle/blob/banner), or true no-imagery layouts.

### 6.2 Visual hierarchy

`integration.hierarchy`: one of `headline-dominant | body-dominant | balanced | image-dominant`.

In body prose, describe the per-slide reading order — the typical pattern (e.g., **number → headline → body**, or **eyebrow → headline → divider → body → footer-handle**). If the order changes between slides, note it; if it's templated, note that too — that's a slide-rhythm signal.

### 6.3 Slide-to-slide transitions

Describe how slides relate to each other compositionally:

- **templated** — same skeleton on every slide; only the words change.
- **evolving** — the composition shifts continuously, as if the camera is panning.
- **variant** — each slide is its own composition with no shared template.

This often mirrors `layout.rhythm`, but think about it again here from the integration perspective: a carousel can have templated layouts but evolving content density, or variant layouts with a templated text/image relationship.

### 6.4 Output

Fill in the `integration:` block of the deconstruction template.

---

## 7. Pass 5 — Engagement correlation

Use `engagement-signals.md`. The output is the `engagement_inferred:` block, plus the `performance:` block if metrics were provided.

**Flag everything in this block as inferred** unless metrics are present. Use `confidence: low|med|high` markers in body prose where applicable.

### 7.1 Cover stop-power (1–5 rubric → band)

Score the cover on five axes (each 1–5) per `engagement-signals.md` §3:

- Contrast (legibility at thumbnail).
- Hook density (curiosity per word).
- Single focal element vs cluttered.
- Specificity (numbers, named entities, concrete claims).
- Visual differentiation in feed.

Sum to a 5–25 score. Map: 5–10 → `low`, 11–18 → `med`, 19–25 → `high`. Record in `engagement_inferred.cover_stop_power`. Note the per-axis scores in body prose where helpful.

### 7.2 Slide-2 standalone test

Apply the cover-your-hand test from `engagement-signals.md` §4 / `copy-vocabulary.md` §3. Slide 2 passes if it introduces or restates the central tension, is legible at thumbnail size, and makes sense without slide 1 context (no dangling pronouns).

Record `engagement_inferred.slide_2_standalone` as `true` or `false`. If neither cleanly applies, note "medium" in body prose and pick the boolean closest to the truth.

### 7.3 Save-bait

Identify save-bait slides per `engagement-signals.md` §5: framework/model/canvas, checklist/step-by-step, comparison table, stat summary/cheat sheet, resource list. Note **which slide numbers** carry save-bait shapes and **which patterns** they use.

Map to `engagement_inferred.save_bait`:

- `high` — two or more save-bait slides, including at least one in the back half.
- `med` — one save-bait slide.
- `low` — zero save-bait slides.

### 7.4 Send-bait

Per `engagement-signals.md` §6: `yes` (clear identity callout or universal truism plus explicit send/tag CTA), `no` (creator-centric or abstract, no "this is so them" trigger), or `implicit` (relatable framing exists but no explicit send/tag prompt).

Map to `engagement_inferred.send_bait`: `high | med | low`.

### 7.5 Loopability

Does slide N transition back to slide 1 visually or narratively? Per `engagement-signals.md` §8, look for:

- Final slide's color, motif, or composition mirroring slide 1.
- Final slide ending on a question slide 1 implicitly answers (or vice versa).
- A visible "back to start" cue.

Record `engagement_inferred.loopable` as boolean. Default `false` unless one of the above is unmistakable.

### 7.6 Swipe-cliffhangers

Identify which **slide pairs** carry cliffhanger transitions per `engagement-signals.md` §7 and `copy-vocabulary.md` §7: open-loop, partial reveal, numbered tease, question-with-delayed-answer, contrarian setup, framework name-drop, visual continuation.

Map to `engagement_inferred.swipe_cliffhangers`: `high` (3+ cues including at least one explicit cliffhanger transition), `med` (1–2 cues), `low` (no momentum machinery).

### 7.7 Slide-count-zone fit

Per `engagement-signals.md` §9: under (<5), sweet-spot (7–10, with tutorials stretching to 12), or over (>12). Record in body prose with the label "industry benchmark — directional only."

### 7.8 Performance (if provided)

If the user provided metrics for their own post, populate `performance:` per `engagement-signals.md` §11: `reach`, `saves`, `shares`, `comments`, `swipe_through_rate`, `completion_rate`, `save_to_reach`, `share_to_reach`, `posted_at` (ISO-8601), `pillar` (lowercase-hyphenated). Null only the fields IG Insights doesn't expose. For third-party creators, leave the entire block `null`.

### 7.9 Output

Fill in the `engagement_inferred:` block of the deconstruction template, and the `performance:` block when metrics exist.

---

## 8. Body composition

After the YAML frontmatter, write the Markdown body sections from the template, in this order:

1. **First impression** — the single sentence from Pass 1, verbatim. Do not rewrite it now that you know more; that's the point.
2. **What this carousel is doing well** — exactly **3 bullets**. Each bullet names a specific device (signature motif, hook structure, type-pairing move, etc.) and explains *why* it works.
3. **What's weaker** — **1–2 bullets**. Be honest. If nothing's weaker, name a tension or a tradeoff the design is making (e.g., "high copy density wins on save-bait but costs dwell-time on slide 4"). If you flagged any anti-patterns from `engagement-signals.md` §13, name them here.
4. **Replication notes — signature devices worth lifting** — bullet list. The question this section answers: *"If I were generating a carousel in this creator's voice, what 2–4 things would I lift?"* Be concrete (e.g., "gold underline on the key noun in each rule," not "good color usage").
5. **Slide-by-slide notes** — a Markdown table with one row per slide. Columns: `# | Role | Headline | Note`. The role names should come from the narrative-arc stage glossary (`Cover`, `Hook-restate`, `Pain`, `Framework`, `Step 1`, `CTA`, etc.). The note is one observation per row — what makes this slide do its job, or what's wrong with it.

---

## 9. Output orchestration

What happens after the deconstruction is written:

### 9.1 Write the entry file

Path: `references/style-dna/<creator>/YYYY-MM-DD_<slug>.md`. Slug derivation rules and collision policy per `schema-style-dna.md` → Filename convention. Own-account posts go in `_own/`.

### 9.2 Append to the index

Append exactly one row to `references/style-dna/_index.md`:

```
| <date> | <creator> | <relative-path> | <hook-formula> | <one-line takeaway> |
```

The takeaway is a single short sentence — the most distinctive thing this carousel teaches.

### 9.3 Synthesis trigger logic

Synthesis is **expensive**: full re-read of every entry it covers. Run it on counted milestones, not on every entry.

- **Creator summary** (`<creator>/_creator-summary.md`, `entry_type: creator_summary`): rebuild when this is the **5th, 10th, 15th, …** entry for the same creator. Below 5 entries the synthesis would over-fit on too few examples; above 5 the patterns stabilize.
- **Cross-synthesis** (`references/style-dna/_synthesis.md`, `entry_type: cross_synthesis`): rebuild when this is the **10th, 20th, 30th, …** entry overall, *and* there are ≥2 creators in the library.
- **Otherwise: skip synthesis.** Just write the entry and append the index row.

When a synthesis trigger fires, the trigger does **not** block the current task — finish writing the carousel entry first, append the index row, then run the synthesis as a separate step. If the user is in a hurry, you may defer synthesis with a one-line note ("Synthesis pending — 10th entry for @humphreytalks") rather than running it inline.

---

## 10. Honesty rules

These are non-negotiable. Skipping them produces entries that look authoritative but corrupt the library.

### 10.1 Font identification

If you are not certain, **propose 2–3 candidates with reasoning** rather than committing a single name. The schema supports this: `family: { value: ["Inter", "Helvetica Neue", "Arial"], confidence: low }` is valid. Default to `confidence: med` unless you have direct evidence (an unmistakable glyph, a watermark naming the face). Over-confident font calls are this skill's most common error.

### 10.2 Engagement claims

Everything in `engagement_inferred:` is **inferred from a static frame**, not measured, unless `performance:` is populated. Use `confidence: low|med|high` markers in body prose where applicable. Phrasing for inferred claims: "appears to," "the structure suggests," "would likely…" Phrasing for measured claims: "saved at X%," "reached Y," "completion rate Z."

When the library has <10 entries with `performance:` data, **do not** report cross-entry engagement correlations — the sample is too small. Per `engagement-signals.md` §12, the gates are n ≥ 4 per group and ≥30% relative difference in medians, *and* ≥10 own-account entries in the library.

### 10.3 Industry benchmarks

Slide-count zone, per-slide read time, save-rate norms, send-rate norms, and any other numeric threshold cited from §9–§10 of the engagement signals or §6 of the copy vocabulary must be labeled **"industry benchmark — directional only"** in body prose. They are not laws. A 4-slide carousel from a known authority can outperform a 9-slide one from a stranger.

---

## 11. Pre-flight checklist

Before running Pass 1, do these in order:

1. **Read `references/style-dna/_index.md`.** Check whether this exact carousel has already been deconstructed (same creator, same hook, similar date). If yes, ask the user whether to overwrite (with `-v2` suffix) or skip.
2. **Check whether the creator already has a `_creator-summary.md`.** If yes, read it. The new entry should explicitly note any **deviations from established patterns** ("typography breaks the creator's usual sans-serif default — first serif headline observed in N entries"). Deviations are the most useful signal a new entry can add to a mature library.
3. **Confirm the creator handle with the user if ambiguous.** Watermarks, footer chyrons, and bio handles are usually reliable, but if multiple handles appear (e.g., a co-post or a quote-card crediting another creator), ask which handle is the **author** of the design system being analyzed.
4. **Confirm slide order.** If slides arrived in a single grid image or out of order, ask once for the canonical sequence before starting.
5. **Confirm metrics scope (only for own-account posts).** If the user provides numbers, confirm which platform they came from (IG Insights, Buffer, etc.) and the date range. Note both in the `performance:` block prose.

If any of these checks fail, resolve before starting Pass 1. Don't begin analysis on shaky inputs.

---

## 12. Common failure modes

These are the patterns Claude tends to get wrong on this protocol. Read them before every run.

### 12.1 Anchoring on slide 1

The cover is the most visually striking slide and the easiest to analyze. Anchoring there means missing patterns visible **only across all slides** — a system motif that appears on slides 2, 4, and 7 but not the cover; a typography weight shift that only emerges in the body slides; a CTA voice that contradicts the cover's tone. **Always survey all slides before committing values.** If you find yourself filling out `motifs[]` after looking only at slide 1, stop.

### 12.2 Inventing exact font names

Naming a font you cannot identify is the single most expensive mistake — wrong font calls poison the cross-creator synthesis (which aggregates by font family). When uncertain, list 2–3 candidates and set `confidence: low`. The schema is designed to absorb honest uncertainty; it cannot absorb confident wrongness.

### 12.3 Conflating creator signature with industry convention

A device used by 60% of finance creators is **not** a signature of any one of them — it's a niche convention. Only `_synthesis.md` (cross-creator) can disambiguate. A new entry's `motifs[]` should reflect what's actually present in this carousel; the creator-signature claim is reserved for `_creator-summary.md` after ≥5 entries, and the niche-convention claim is reserved for `_synthesis.md` after ≥10 entries across ≥2 creators. **Do not** label something a "creator signature" in a single carousel entry — call it a motif, and let synthesis decide later whether it's a signature.

### 12.4 Missing the slide-2 standalone evaluation

This test is easy to forget because the cover is so loud. Before declaring Pass 5 complete, **literally cover slide 1 with your hand** (or scroll past it in your mental simulation) and re-read slide 2. Does it still hook? If you did not perform this test consciously, your `slide_2_standalone` value is unreliable.

### 12.5 Forgetting to count words per slide

`word_counts_per_slide` requires one count per slide, and `len(word_counts_per_slide)` must equal `slide_count` — this is a schema validation rule. Estimating the average is not enough. Count each slide. Yes, even the all-image ones (those count as `0`).

### 12.6 Finishing without checking validation

Before declaring the entry done, mentally run the eight validation rules from `schema-style-dna.md` → Validation rules: YAML parses, all required fields present and non-null, `schema_version: 1`, slide-count matches word-count-list length, all contrast pairs reference declared palette colors, hex codes match `^#[0-9A-F]{6}$`, tags match `^[a-z0-9]+(-[a-z0-9]+)*$`, filename follows the convention. The validation script (`scripts/validate-entry.py`) will catch these later, but catching them now is cheaper.

---

## 13. Quick-reference checklist

Print this in your head before starting:

1. Pre-flight: read index, read creator summary if it exists, confirm handle and slide order.
2. Pass 1 — first impression (1 sentence + aesthetic tag, no YAML).
3. Pass 2 — visual systems (palette → typography → layout → spacing → imagery → motifs).
4. Pass 3 — copy systems (cover hook → word counts → narrative arc → CTA → voice).
5. Pass 4 — integration (text–image relation, hierarchy, slide-to-slide rhythm).
6. Pass 5 — engagement correlation (cover stop-power, slide-2 standalone, save-bait, send-bait, loopability, cliffhangers, slide-count zone, performance if provided).
7. Body composition (first impression, what's working ×3, what's weaker ×1–2, replication notes, slide-by-slide table).
8. Save the file at `references/style-dna/<creator>/YYYY-MM-DD_<slug>.md`.
9. Append the index row.
10. Check synthesis triggers (5/10/15… for creator, 10/20/30… for cross).
11. Validate against the eight schema rules.

If any step feels skippable, re-read §1.
