# Per-carousel deconstruction template

This file is the literal copy-paste skeleton for a `entry_type: carousel` analysis. When Claude finishes deconstructing a carousel, the output is a new file at `references/style-dna/<creator-handle>/YYYY-MM-DD_<slug>.md` whose contents are this template with every `<angle-bracket-placeholder>` replaced by a real value.

## How to use

1. Read `references/schema-style-dna.md` first — Schema A is the source of truth. Field names in this template match Schema A exactly; do not invent new ones.
2. Read `references/visual-vocabulary.md`, `references/copy-vocabulary.md`, and `references/engagement-signals.md` for the legal vocabulary of every tagged value.
3. Copy everything below the `BEGIN TEMPLATE` line into the new file and replace each `<placeholder>` with a real value.
4. If a value is genuinely unknown, use literal `null` (do not delete the field). If a value is inferred rather than directly observed, wrap it as `{value: <x>, confidence: low|med|high}`.
5. Keep YAML hex codes 6-digit uppercase (`^#[0-9A-F]{6}$`). Keep tags lowercase-hyphenated.
6. After saving, append one row to `references/style-dna/_index.md` (see Section 5 below).

---

## BEGIN TEMPLATE

```markdown
---
schema_version: 1
entry_type: carousel
creator: "<@handle>"                    # IG handle including @, lowercase
creator_aesthetic_tag: "<short-slug>"   # short slug describing creator's lane, e.g. "editorial-finance"
analyzed_on: <YYYY-MM-DD>               # ISO date of this analysis
source: <platform>                      # one of: instagram | tiktok | linkedin | other
post_url: "<https://...>"               # canonical URL, or null
slide_count: <int>                      # must equal len(copy.word_counts_per_slide)
canvas:
  aspect_ratio: "<ratio>"               # one of: "1:1" | "4:5" | "9:16"
  width_px: <int>
  height_px: <int>
palette:
  background: ["<#HEX>"]                # list of background hexes
  primary_text: "<#HEX>"                # dominant ink color
  accent: ["<#HEX>"]                    # list of accent hexes (may be empty list)
  signature: "<#HEX>"                   # the single creator-identifying hex (often = accent[0])
  harmony: "<harmony-descriptor>"       # structural + emotional, e.g. "warm-neutral-with-gold"
                                        # structural component MUST map to one of:
                                        # monochromatic | analogous | complementary | split-complementary |
                                        # triadic | tetradic | achromatic | unstructured
  contrast_pairs:
    - { fg: "<#HEX>", bg: "<#HEX>", wcag_ratio: <float>, wcag_level: "<AAA|AA|AA-Large|FAIL>" }
    # repeat one entry per text/background combination used
typography:
  headline:
    family: { value: "<font-name>", confidence: <low|med|high> }
    fallbacks: ["<font-name>", "<font-name>"]
    weight: <100-900>
    size_px: [<min>, <max>]             # range across slides, or single int if uniform
    tracking_em: <float>                # negative = tighter
    leading_ratio: <float>              # line-height as multiple of font size
    casing: "<casing>"                  # one of: title-case | uppercase | lowercase | sentence-case
  body:
    family: { value: "<font-name>", confidence: <low|med|high> }
    fallbacks: ["<font-name>", "<font-name>"]
    weight: <100-900>
    size_px: [<min>, <max>]
    tracking_em: <float>
    leading_ratio: <float>
    casing: "<casing>"                  # one of: title-case | uppercase | lowercase | sentence-case
layout:
  alignment: "<alignment>"              # one of: left | center | right | justified | mixed
  margin_pct: <int>                     # outer margin as percent of canvas width (typical 6-12)
  grid: "<grid-descriptor>"             # e.g. single-column | two-column | loose-12-col | strict-6-col | masonry | none
  balance: "<balance>"                  # one of: symmetric | asymmetric | radial
  focal_placement: "<focal>"            # one of: upper-third | center | lower-third |
                                        # rule-of-thirds-left | rule-of-thirds-right | golden-ratio | edge-anchored
  rhythm: "<rhythm>"                    # type + optional modifier, e.g.
                                        # templated | evolving | variant
                                        # modifiers: varied-density | crescendo | call-and-response | uniform
  whitespace_ratio: <0.0-1.0>           # band: <0.25 minimal | 0.25-0.50 balanced | 0.50-0.70 breathy | >0.70 gallery
imagery:
  type: "<type>"                        # one of: none | photo | illustration | mixed | data-viz
  treatment: <null | "<treatment>">     # null if type is none; otherwise e.g.
                                        # ungraded | warm-grade | cool-grade | duotone | halftone |
                                        # grain | paper-texture | glassmorphism | brutalist
                                        # combine with + e.g. "warm-grade+grain"
  icon_style: <null | "<icon-style>">   # one of: line | filled | duotone | hand-drawn | 3D | none | null
motifs:
  - "<motif-slug>"                      # lowercase-hyphenated; system motifs (≥60% of slides) only,
  - "<motif-slug>"                      # plus visually load-bearing decorative motifs
  - "<motif-slug>"
copy:
  cover_hook: "<exact cover headline, verbatim>"
  hook_formula: "<formula-tag>"         # one of: curiosity-gap | contrarian | listicle | identity-callout |
                                        # bold-claim | direct-question | hybrid
                                        # for hybrid: join two with +, e.g. "listicle+regret"
  word_counts_per_slide: [<int>, <int>, <int>]   # one int per slide; len MUST equal slide_count
  narrative_arc: "<Stage> -> <Stage> -> <Stage>" # use spaced arrows; ×N for repeats; cap at 8 stages
                                                  # see copy-vocabulary §2 for stage glossary
  cta:
    type: "<cta-type>"                  # one of: save | share | follow | comment | link-in-bio | none
    placement: "<placement>"            # one of: final-slide | every-slide | none | inline
    copy: "<exact CTA text or null>"
  voice:
    tone: ["<tone>", "<tone>"]          # register + descriptors, e.g. "frank", "elder-mentor"
                                        # registers: academic | professional | casual | gen-z-internet | poetic
    person: "<person>"                  # one of: first-person | second-person | third-person | mixed
    formality: "<formality>"            # e.g. casual-direct | formal | playful | academic
integration:
  text_image_relation: "<relation>"     # one of: text-driven | image-driven | balanced | typography-as-image
  hierarchy: "<hierarchy>"              # one of: headline-dominant | body-dominant | balanced | image-dominant
engagement_inferred:
  cover_stop_power: <low|med|high>      # 5-axis rubric in engagement-signals §3 → band
  slide_2_standalone: <true|false>      # see engagement-signals §4
  save_bait: <low|med|high>             # see engagement-signals §5
  send_bait: <low|med|high>             # see engagement-signals §6
  loopable: <true|false>                # see engagement-signals §8
  swipe_cliffhangers: <low|med|high>    # see engagement-signals §7
performance:                            # null block for third-party creators; populate only for own posts
  reach: <int|null>
  saves: <int|null>
  shares: <int|null>
  comments: <int|null>
  swipe_through_rate: <0.0-1.0|null>
  completion_rate: <0.0-1.0|null>
  save_to_reach: <0.0-1.0|null>
  share_to_reach: <0.0-1.0|null>
  posted_at: <ISO-8601-timestamp|null>
  pillar: "<lowercase-hyphenated|null>"
tags:                                   # ≥3 entries, lowercase-hyphenated, ^[a-z0-9]+(-[a-z0-9]+)*$
  - "<tag>"
  - "<tag>"
  - "<tag>"
---

# Carousel: "<exact cover hook>"

## First impression
<one-sentence gestalt>

## What this carousel is doing well
- <bullet 1>
- <bullet 2>
- <bullet 3>

## What's weaker
- <bullet 1>
- <bullet 2>

## Replication notes (what I'd lift)
- <signature device 1>
- <signature device 2>

## Slide-by-slide notes
| # | Role | Headline | Note |
|---|---|---|---|
| 1 | Cover | "<text>" | <observation> |
| 2 | Hook-restate | "<text>" | <observation> |
| … | … | … | … |
```

## END TEMPLATE

---

## Section 4: Filename rule

After filling the template, save the file at:

- **Path:** `references/style-dna/<creator-handle>/YYYY-MM-DD_<3-6-word-slug>.md`
- **Creator handle directory:** lowercase, no `@`. `@humphreytalks` → `humphreytalks/`. Own-account posts go in `_own/`.
- **Slug rules:**
  - Lowercase, hyphen-separated.
  - Derived from the cover hook.
  - 3–6 words.
  - Drop stopwords (`the`, `a`, `an`, `of`, `to`, `for`, `with`) **unless** they carry meaning.
  - Strip punctuation; replace numerals-as-words with digits (`seven` → `7`).
- **Collision rule:** if the chosen filename already exists, append `-v2`, then `-v3`, etc. Never overwrite.

Example: cover "The 7 money rules I wish I knew at 22" by `@humphreytalks` analyzed on 2026-05-07 →
`references/style-dna/humphreytalks/2026-05-07_7-money-rules-22.md`.

---

## Section 5: Index-update rule

After writing the entry, append exactly one row to `references/style-dna/_index.md`:

```
| <date> | <creator> | <relative-path> | <hook-formula> | <one-line takeaway> |
```

- `<date>`: the entry's `analyzed_on` value (ISO-8601).
- `<creator>`: the entry's `creator` value (with `@`).
- `<relative-path>`: path relative to `references/style-dna/`, e.g. `humphreytalks/2026-05-07_7-money-rules-22.md`.
- `<hook-formula>`: the entry's `copy.hook_formula` value.
- `<one-line takeaway>`: a single short sentence — the most distinctive thing this carousel teaches.
