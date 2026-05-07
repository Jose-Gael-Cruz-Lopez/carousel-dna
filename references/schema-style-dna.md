# Schema: Style DNA

This file is the **schema contract** for every artifact the `carousel-design-analysis` skill produces. Future Claude sessions running this skill read this file before writing any carousel entry, creator summary, or cross-creator synthesis. **Every generated entry must validate against the schema declared here.** If a field is not in the schema, it does not belong in the entry. If a field is required and missing, the entry is invalid.

This file is foundational. Vocabularies, templates, deconstruction protocols, and `SKILL.md` all reference field names defined below. Treat the schema as the single source of truth.

---

## Field conventions

Read this section before writing any entry.

- **Frontmatter for metadata, body for prose.** Put all structured fields in YAML frontmatter at the top of the file (delimited by `---`). Put rationale, narrative, and human commentary in the Markdown body below.
- **Numeric ranges use `[min, max]` lists.** A spread is `[14, 22]`. A point estimate or average is a single number. Never write `"14-22"` as a string.
- **Hex codes are 6-digit uppercase.** Write `#1A1A1A`, not `#1a1a1a` and not `#1a1`. Hex codes match `^#[0-9A-F]{6}$`.
- **Font names use the canonical PostScript name when known.** If uncertain, use a list of 2–3 candidates with the most-likely first: `[Inter, "Helvetica Neue", "Arial"]`. Keep names quoted when they contain spaces.
- **Confidence flag for inferred values.** When a value is not directly observable (e.g. font family inferred from glyph shapes, performance estimated rather than measured), wrap it as a YAML map: `{value: "Inter", confidence: med}`. Allowed values: `low`, `med`, `high`. Direct observations (count of slides, declared text) do not need a confidence flag.
- **`null` for unknown.** Use literal `null` for fields that genuinely have no value (e.g. `performance:` blocks for third-party creators where you don't have analytics access). Do not use empty strings or omit required fields.
- **Tags are lowercase-hyphenated.** `money-rules`, not `Money Rules` or `money_rules`.
- **Dates are ISO-8601.** `2026-05-07` for date-only, `2026-05-07T14:32:00Z` for timestamps.

---

## Schema A: `entry_type: carousel`

The per-carousel analysis entry. One file per analyzed carousel. Filename pattern: `<creator-handle>/YYYY-MM-DD_<slug>.md`.

```yaml
schema_version: 1                    # bump only via migration policy below
entry_type: carousel
creator: "@humphreytalks"            # IG handle including @, lowercase
creator_aesthetic_tag: "editorial-finance"   # short slug describing creator's lane
analyzed_on: 2026-05-07              # ISO date when this analysis ran
source: instagram                    # platform: instagram | tiktok | linkedin | other
post_url: "https://www.instagram.com/p/ABC123/"   # canonical post URL, null if unavailable
slide_count: 7                       # integer, must equal len(copy.word_counts_per_slide)
canvas:
  aspect_ratio: "4:5"                # string, common values: "1:1", "4:5", "9:16"
  width_px: 1080                     # integer pixel width of the source image
  height_px: 1350                    # integer pixel height of the source image
palette:                             # role-tagged colors: every hex assigned a semantic role
  background: ["#F4EFE6"]            # list of hexes used as backgrounds
  primary_text: "#1A1A1A"            # the dominant body/headline ink color
  accent: ["#C8A24B"]                # list of accent colors used for emphasis or motifs
  signature: "#C8A24B"               # the single color most identified with this creator (often = accent[0])
  harmony: "warm-neutral-with-gold"  # one-line descriptor of the palette's emotional register
  contrast_pairs:                    # every text/background combination used in the carousel
    - { fg: "#1A1A1A", bg: "#F4EFE6", wcag_ratio: 14.2, wcag_level: "AAA" }
    - { fg: "#C8A24B", bg: "#1A1A1A", wcag_ratio: 6.8,  wcag_level: "AA" }
typography:
  headline:
    family: { value: "GT Sectra", confidence: med }   # PostScript name + confidence
    fallbacks: ["Tiempos Headline", "Playfair Display"]
    weight: 700                      # numeric weight (100-900)
    size_px: [56, 72]                # range across slides, or single number if uniform
    tracking_em: -0.02               # letter-spacing in em (negative = tighter)
    leading_ratio: 1.05              # line-height as multiple of font size
    casing: "title-case"             # title-case | uppercase | lowercase | sentence-case
  body:
    family: { value: "Inter", confidence: high }
    fallbacks: ["Helvetica Neue", "Arial"]
    weight: 400
    size_px: [22, 28]
    tracking_em: 0
    leading_ratio: 1.4
    casing: "sentence-case"
layout:
  alignment: "left"                  # left | center | right | justified | mixed
  margin_pct: 8                      # outer margin as percentage of canvas width
  grid: "loose-12-col"               # short descriptor of grid system if discernible
  balance: "asymmetric"              # symmetric | asymmetric | radial
  focal_placement: "upper-third"     # upper-third | center | lower-third | rule-of-thirds-left | etc.
  rhythm: "varied-density"           # varied-density | uniform | crescendo | call-and-response
  whitespace_ratio: 0.55             # 0-1, share of canvas that is empty/breathing room
imagery:
  type: "none"                       # none | photo | illustration | mixed | data-viz
  treatment: null                    # filter/grade descriptor, null if type is none
  icon_style: null                   # line | filled | duotone | hand-drawn | null
motifs:                              # repeating visual or textual devices unique to this carousel
  - "numbered-rules"
  - "hairline-divider-between-rules"
  - "gold-underline-on-key-noun"
copy:
  cover_hook: "The 7 money rules I wish I knew at 22"
  hook_formula: "numbered-list + age-regret"   # short tag for the hook archetype
  word_counts_per_slide: [11, 28, 24, 26, 25, 30, 18]   # one int per slide; len must equal slide_count
  narrative_arc: "promise -> rules-stack -> reframe -> cta"   # 3-5 beats separated by " -> "
  cta:
    type: "save"                     # save | share | follow | comment | link-in-bio | none
    placement: "final-slide"         # final-slide | every-slide | none | inline
    copy: "Save this for the next time you get paid."
  voice:
    tone: ["frank", "elder-mentor"]
    person: "first-person"           # first-person | second-person | third-person | mixed
    formality: "casual-direct"       # casual-direct | formal | playful | academic | etc.
integration:
  text_image_relation: "text-driven" # text-driven | image-driven | balanced | typography-as-image
  hierarchy: "headline-dominant"     # headline-dominant | body-dominant | balanced | image-dominant
engagement_inferred:                 # qualitative inferences from cover/structure alone
  cover_stop_power: high             # low | med | high
  slide_2_standalone: true           # does slide 2 still hook if slide 1 is missed?
  save_bait: high                    # how much the structure invites saving
  send_bait: med                     # how much it invites sending to a friend
  loopable: false                    # does the last slide loop back to the first?
  swipe_cliffhangers: med            # do mid-slides end with tension that pulls a swipe?
performance:                         # null for third-party creators; populated only for own posts
  reach: null
  saves: null
  shares: null
  comments: null
  swipe_through_rate: null           # 0-1 share of viewers who reached final slide
  completion_rate: null              # 0-1 share who watched all slides
  save_to_reach: null                # saves / reach
  share_to_reach: null               # shares / reach
  posted_at: null                    # ISO timestamp
  pillar: null                       # content pillar tag, e.g. "money-101"
tags:                                # flat list of lowercase-hyphenated descriptors
  - "money-rules"
  - "numbered-list"
  - "editorial-finance"
  - "warm-neutral"
```

### Required fields for `entry_type: carousel`

A carousel entry is **valid** if and only if every field below is present and non-null (unless explicitly nullable):

- `schema_version`, `entry_type`, `creator`, `analyzed_on`, `source`, `slide_count`
- `canvas.aspect_ratio`, `canvas.width_px`, `canvas.height_px`
- `palette.background`, `palette.primary_text`, `palette.harmony`, `palette.contrast_pairs`
- `typography.headline.family`, `typography.headline.size_px`, `typography.headline.casing`
- `typography.body.family`, `typography.body.size_px`
- `layout.alignment`, `layout.balance`, `layout.focal_placement`
- `imagery.type`
- `copy.cover_hook`, `copy.hook_formula`, `copy.word_counts_per_slide`, `copy.narrative_arc`, `copy.cta.type`
- `engagement_inferred.cover_stop_power`, `engagement_inferred.save_bait`
- `tags` (must contain at least 3 entries)

Nullable: `post_url`, `imagery.treatment`, `imagery.icon_style`, every field in `performance` (null when not the user's own post).

### Worked example

The YAML block above is itself the canonical filled-in example for `creator: @humphreytalks` analyzing the post "The 7 money rules I wish I knew at 22". When teaching the schema to a future session, reference this example.

---

## Schema B: `entry_type: creator_summary`

The per-creator synthesis entry. One file per creator, regenerated when new carousels are added. Filename pattern: `<creator-handle>/_summary.md`.

```yaml
schema_version: 1
entry_type: creator_summary
creator: "@humphreytalks"
entries_synthesized: 7               # integer count of carousel entries this summary draws from
generated_on: 2026-05-07
palette_consensus:
  background_dominant: ["#F4EFE6", "#1A1A1A"]   # 1-3 backgrounds that appear in most carousels
  primary_text: "#1A1A1A"
  accent_signature: "#C8A24B"        # the single most-identifiable color
  variation_note: "occasional swap to ivory-on-charcoal for serious-tone posts"
typography_consensus:
  headline_family: "GT Sectra"
  body_family: "Inter"
  pairing_pattern: "editorial-serif-headline + grotesk-body"   # short label for the pairing relationship
  consistency_note: "headline family unchanged across all 7 entries; body weight varies 400-500"
layout_consensus:
  alignment: "left"
  balance: "asymmetric"
  focal_placement: "upper-third"
  rhythm: "varied-density with hairline dividers"
cover_hook_patterns:                 # frequencies expressed as "k/N" where N = entries_synthesized
  - { pattern: "numbered-list-with-age-regret", frequency: "4/7" }
  - { pattern: "controversial-claim-then-proof", frequency: "2/7" }
  - { pattern: "single-question-on-cover", frequency: "1/7" }
narrative_arc_patterns:
  - { pattern: "promise -> rules-stack -> reframe -> cta", frequency: "5/7" }
  - { pattern: "objection -> evidence -> reframe -> cta", frequency: "2/7" }
signature_motifs:
  - "numbered-rules with hairline divider"
  - "gold-underline on the key noun in each rule"
  - "final slide is always a single sentence on charcoal"
engagement_correlations:             # only populated when ≥3 entries have non-null performance data
  highest_save_pattern: null
  highest_share_pattern: null
  notes: null
```

### Body sections for creator_summary

Below the YAML, write four prose sections in this order:

1. **Rules that always hold** — patterns appearing in ≥80% of entries. State each as an imperative rule.
2. **Rules that usually hold** — patterns in 50–79%. State as defaults with noted exceptions.
3. **Experimental variations** — patterns in <50%. Describe as the creator's range of moves rather than rules.
4. **How to brief a new carousel in this style** — a 5–8 line briefing template a future Claude can adapt when the user asks "make me a carousel in @humphreytalks's voice."

### Required fields for `entry_type: creator_summary`

- `schema_version`, `entry_type`, `creator`, `entries_synthesized`, `generated_on`
- `palette_consensus.background_dominant`, `palette_consensus.primary_text`, `palette_consensus.accent_signature`
- `typography_consensus.headline_family`, `typography_consensus.body_family`
- `layout_consensus.alignment`, `layout_consensus.balance`
- `cover_hook_patterns` (list, may be empty if entries_synthesized < 3)
- `narrative_arc_patterns` (list)
- `signature_motifs` (list, must contain at least 1 if entries_synthesized ≥ 3)

`engagement_correlations` is fully nullable.

---

## Schema C: `entry_type: cross_synthesis`

The global library synthesis. One file at `references/style-dna/_cross-synthesis.md`. Regenerated when ≥2 creators or ≥10 entries are present.

```yaml
schema_version: 1
entry_type: cross_synthesis
creators_synthesized:
  - "@humphreytalks"
  - "@vexkingbooks"
  - "@theslowfactory"
entries_total: 23
generated_on: 2026-05-07
universal_patterns:                  # patterns appearing across ≥2 creators
  - { pattern: "left-aligned headline + body stack", creators: ["@humphreytalks", "@vexkingbooks"], frequency: "high" }
  - { pattern: "single-color accent for the key noun", creators: ["@humphreytalks", "@theslowfactory"], frequency: "med" }
creator_signatures:                  # patterns unique to one creator within the library
  - { creator: "@humphreytalks", signature: "gold-underline on key nouns" }
  - { creator: "@theslowfactory", signature: "ragged-edge image cards on slide 2" }
engagement_findings:                 # populated only when ≥1 own-post entry exists with performance data
  top_saves_pattern: null
  top_shares_pattern: null
  notes: null
```

### Body sections for cross_synthesis

Below the YAML, write three short prose sections:

1. **What every great carousel in this library does** — keyed off `universal_patterns`.
2. **What sets each creator apart** — keyed off `creator_signatures`.
3. **Open questions** — patterns you'd want to test next, things the library is too sparse to answer yet.

### Required fields for `entry_type: cross_synthesis`

- `schema_version`, `entry_type`, `creators_synthesized` (list of ≥2), `entries_total`, `generated_on`
- `universal_patterns` (list, may be empty if entries_total < 10)
- `creator_signatures` (list)

`engagement_findings` is fully nullable.

---

## Filename convention

Use this rule for every new carousel entry file:

- **Pattern:** `<creator-handle>/YYYY-MM-DD_<3-6-word-slug>.md`
- **Creator handle directory:** lowercase, no `@`. `@humphreytalks` → directory `humphreytalks/`. Own-account posts go in `_own/` (already scaffolded).
- **Slug rules:**
  - Lowercase, hyphenated.
  - Derived from the cover hook.
  - 3–6 words.
  - Drop stopwords (`the`, `a`, `an`, `of`, `to`, `for`, `with`) **unless** they carry meaning ("the-7-rules" is fine; "of-the-day" is not).
  - Strip punctuation; replace numerals with their digits (`seven` → `7`).
- **Collision rule:** If a file with the chosen name already exists, append `-v2`, then `-v3`, etc. Never overwrite.

Example: a carousel posted on 2026-05-07 with the hook "The 7 money rules I wish I knew at 22" by @humphreytalks becomes `humphreytalks/2026-05-07_7-money-rules-22.md`.

---

## Validation rules

An entry is valid if and only if **all** of the following hold:

1. The YAML frontmatter parses without error via `yaml.safe_load`.
2. All required fields for the entry's `entry_type` are present and non-null (see "Required fields" subsection of each schema).
3. `schema_version: 1`.
4. **For `entry_type: carousel`:** `slide_count == len(copy.word_counts_per_slide)`.
5. **For `entry_type: carousel`:** every `palette.contrast_pairs[i].fg` and `.bg` value appears somewhere in `palette.background`, `palette.primary_text`, or `palette.accent`.
6. Every hex code matches `^#[0-9A-F]{6}$`.
7. Every entry in `tags` matches `^[a-z0-9]+(-[a-z0-9]+)*$`.
8. The filename follows the pattern in the **Filename convention** section above.

A validation script lives at `scripts/validate-entry.py` (added in phase 06) and runs all eight checks.

---

## Migration policy

Schemas evolve. When they do, follow this protocol exactly:

1. **Bump `schema_version`.** New schema becomes `schema_version: 2`. Old entries remain at `1` until migrated.
2. **Document the diff.** Add a `## Schema version 2` section to the bottom of this file describing every changed, added, or removed field, with rationale.
3. **Write a migration prompt.** Add `references/migrations/v1-to-v2.md` containing a prompt the user can paste into a fresh session to rewrite all entries to the new version. The prompt must be self-contained.
4. **Never break-change a field name.** Deprecation is the only allowed path:
   - Add the new field alongside the old.
   - Mark the old field `# deprecated in v2, remove in v3` in this schema doc.
   - Run the migration to populate the new field on every entry.
   - In the next bump (v3), remove the old field.
5. **Re-run cross-synthesis after migration.** Old summaries are not automatically valid against new schemas; regenerate.

---

## Quick-reference for the busy Claude

If you only have 30 seconds before writing an entry, read this:

1. Three entry types: `carousel`, `creator_summary`, `cross_synthesis`. Pick the right one.
2. YAML frontmatter for structured fields. Markdown body for prose.
3. Hex codes: `^#[0-9A-F]{6}$`. Tags: lowercase-hyphenated. Dates: ISO-8601.
4. Inferred values get `{value: ..., confidence: low|med|high}`. Null for genuinely unknown.
5. `slide_count` must equal `len(copy.word_counts_per_slide)`.
6. Every contrast pair's fg/bg must come from the declared palette.
7. Filename: `<handle>/YYYY-MM-DD_<slug>.md`. Slug 3–6 lowercase-hyphenated words from the hook.
8. If a required field is missing, the entry is invalid — fill it or mark the entry incomplete and ask the user.
