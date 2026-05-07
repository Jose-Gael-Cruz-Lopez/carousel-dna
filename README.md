# Carousel DNA

A Claude Code skill that **reverse-engineers Instagram carousel posts** into a structured analysis of their design and copy systems, builds a persistent style-DNA library out of those analyses, and uses that library to **brief new carousels in any captured creator's voice**.

Drop in a screenshot or paste an IG URL. Get back hex codes, font candidates, layout grids, hook formulas, narrative arcs, and engagement-signal ratings — saved as a YAML-frontmatter Markdown file you can search, filter, and synthesize across.

---

## What it does, in one diagram

```
   You drop in:                         The skill produces:
   ─────────────                        ──────────────────
   IG screenshot(s) ─────►              Deconstruction report (in chat)
        OR                ─────►        Schema A entry .md (saved to library)
   IG post URL    ───────►              Index row updated
        OR                              ───────────────────────
   "design something                    Generation brief (Figma / MJ / copy)
    in @creator's style" ─►             ───────────────────────
        OR                              Creator summary regenerated
   "re-synthesize"     ───►             Cross-creator synthesis updated
```

Three output types, all driven by which inputs you provide and what you ask for.

---

## Quick start

### 1. Install dependencies (once)

```bash
# Required: image fetcher for the IG-URL workflow
pip install gallery-dl
# or:  pipx install gallery-dl
# or:  brew install gallery-dl
```

You also need to be **logged into Instagram in a browser** (Chrome, Firefox, Safari, Edge, or Brave) — the fetcher reads your session cookies read-only so it can see public carousels behind IG's login wall.

### 2. Use it

The skill auto-triggers on phrases like:

| You say | What happens |
|---|---|
| *(attach screenshots of a carousel)* | Five-pass deconstruction → entry written to library |
| `https://www.instagram.com/p/ABC123/` | Fetcher pulls slides → deconstruction → entry |
| `analyze @creator's recent carousel` | Asks for the URL or screenshots, then deconstructs |
| `design something in @creator's style` | Reads `_creator-summary.md` → returns Figma / MJ / copy brief |
| `re-synthesize the library` | Rebuilds every creator summary + the cross-creator synthesis |
| `audit the library` | Flags outliers, vocabulary drift, missing performance data |

You don't have to say the word "skill" — Claude detects the pattern and invokes the protocol automatically.

---

## The three outputs explained

### 1. Deconstruction report

A five-pass walkthrough of one carousel. Always runs in this exact order:

| Pass | What it captures | Vocabulary file |
|---|---|---|
| **1. First impression** | One-sentence gestalt. The felt-sense before analysis muddles it. | — |
| **2. Visual systems** | Palette (5–7 hexes with WCAG ratios), typography (font candidates + weights + tracking), layout (alignment, grid, balance, focal placement, rhythm, whitespace), imagery treatment, recurring motifs. | `visual-vocabulary.md` |
| **3. Copy systems** | Cover hook (verbatim), hook formula, word counts per slide, narrative arc, CTA, voice (tone + person + formality). | `copy-vocabulary.md` |
| **4. Integration** | How text and image relate per slide; visual hierarchy; slide-to-slide rhythm. | — |
| **5. Engagement signals** | Cover stop-power (5-axis rubric → low/med/high), slide-2 standalone test, save-bait, send-bait, loopability, swipe cliffhangers, slide-count-zone fit. | `engagement-signals.md` |

You see the report inline in the chat. The skill simultaneously writes a structured **Schema A entry** to disk so the library grows.

### 2. Library entry

Every analyzed carousel becomes a Markdown file with YAML frontmatter at:

```
references/style-dna/<creator-handle>/YYYY-MM-DD_<3-6-word-slug>.md
```

The YAML carries every measurable axis (palette, typography, motifs, hook formula, engagement ratings, etc.). The Markdown body holds the narrative analysis: first impression, what's working, what's weaker, replication notes, slide-by-slide table.

A schema-validated entry looks like this (truncated):

```yaml
---
schema_version: 1
entry_type: carousel
creator: "@humphreytalks"
analyzed_on: 2026-05-07
slide_count: 7
palette:
  background: ["#F4EFE6"]
  primary_text: "#1A1A1A"
  accent: ["#C8A24B"]
  signature: "#C8A24B"
  harmony: "warm-neutral-with-gold"
  contrast_pairs:
    - { fg: "#1A1A1A", bg: "#F4EFE6", wcag_ratio: 14.2, wcag_level: "AAA" }
typography:
  headline: { family: { value: "GT Sectra", confidence: med }, ... }
copy:
  cover_hook: "The 7 money rules I wish I knew at 22"
  hook_formula: "numbered-list+age-regret"
  ...
engagement_inferred:
  cover_stop_power: high
  slide_2_standalone: true
  save_bait: high
tags: ["money-rules", "numbered-list", "editorial-finance"]
---

# Carousel: "..."
[body sections]
```

After every entry, one row is appended to `references/style-dna/_index.md` so you can scan the whole library at a glance.

### 3. Generation brief

When you ask for a carousel **in** a captured style (instead of analyzing one), you get a paste-ready brief in one of three formats:

| Format | When | Template |
|---|---|---|
| **Figma spec** | Default, or when you say "design spec" / "design tokens" | `assets/figma-spec-template.md` |
| **Midjourney prompts** | When you say "MJ" / "image AI" / "mood board" | `assets/midjourney-prompt-template.md` |
| **Copy-only brief** | When you say "just the words" / "writing brief" | inline format |

A Figma spec includes color tokens (paste into Figma variables), typography styles, components to build first, slide-by-slide layout notes, motif system to enforce, and a "what I deliberately won't replicate" section.

Briefs are inline by default. Save to `references/style-dna/_blends/` only if you say "save this brief."

---

## How the library compounds over time

The skill is designed to get smarter as you feed it more carousels. Synthesis fires on milestones:

```
1 entry        → library entry only
2-4 entries    → library entry only
5th entry      → rebuild that creator's _creator-summary.md
6-9 entries    → library entry only
10th overall   → rebuild references/style-dna/_synthesis.md (cross-creator)
15th creator   → creator summary rebuilds (and so on every 5)
20th overall   → cross-synthesis rebuilds (and so on every 10)
```

**Why milestones?** Synthesis re-reads every covered entry, which is expensive. Below 5 entries the patterns over-fit; the milestones are where signal stabilizes.

**What synthesis files contain:**

- `_creator-summary.md` — palette consensus, typography consensus, hook patterns with frequency (`4/7`), narrative-arc patterns, signature motifs, "rules that always hold / usually hold / experimental variations," and a paste-ready briefing template.
- `_synthesis.md` — universal patterns across ≥2 creators, creator signatures, and any engagement findings (only when you've added performance data to your own posts).

You can manually trigger a rebuild any time: `re-synthesize the library`.

---

## File structure

```
~/.claude/skills/carousel-design-analysis/
│
├── SKILL.md                              ← skill manifest (Claude reads this first)
├── README.md                             ← you are here
├── .gitignore                            ← excludes assets/fetched/, .DS_Store
│
├── references/                           ← protocols + vocabularies (skill machinery)
│   ├── schema-style-dna.md               ← schema contract (Schemas A/B/C)
│   ├── deconstruction-protocol.md        ← the 5-pass workflow
│   ├── generation-brief-template.md      ← brief orchestrator
│   ├── fetcher-protocol.md               ← Branch D: IG URL → local files
│   ├── visual-vocabulary.md              ← Pass 2 terminology
│   ├── copy-vocabulary.md                ← Pass 3 terminology
│   ├── engagement-signals.md             ← Pass 5 rubrics + benchmarks
│   │
│   └── style-dna/                        ← LIBRARY STATE (grows over time)
│       ├── _index.md                     ← every entry, one row
│       ├── _synthesis.md                 ← cross-creator patterns
│       ├── _own/                         ← your own posts (with performance data)
│       ├── _blends/                      ← saved generation briefs
│       └── <creator-handle>/             ← one folder per analyzed creator
│           ├── _creator-summary.md       ← regenerated on milestone
│           └── YYYY-MM-DD_<slug>.md      ← one per analyzed carousel
│
├── assets/                               ← templates the skill fills in
│   ├── deconstruction-template.md        ← Schema A skeleton
│   ├── figma-spec-template.md            ← Figma brief skeleton
│   ├── midjourney-prompt-template.md     ← MJ prompt skeleton
│   └── fetched/                          ← downloaded slides (gitignored)
│
└── scripts/
    └── fetch-carousel.py                 ← gallery-dl wrapper for IG URLs
```

**The five reference files** (`schema-style-dna.md`, `visual-vocabulary.md`, `copy-vocabulary.md`, `engagement-signals.md`, plus the two protocol files) are the actual analysis machinery. They define the legal vocabulary every entry must use, so future entries stay comparable.

---

## The four branches of the skill

The skill routes to one of four branches based on what you provide:

### Branch A — Deconstruction (manual screenshots)

You attach 1–N slide screenshots in chat. The skill walks the 5 passes in order and writes the Schema A entry. This is the canonical path; everything else feeds into it.

### Branch B — Generation brief

You ask Claude to design a carousel in a captured style. The skill reads the smallest sufficient source (one creator summary, or one specific entry, or the global synthesis), fills the chosen template, and outputs inline.

Honest constraint: **briefs cannot invent fonts or colors that aren't in the captured style.** Extending the palette requires you to ask explicitly.

### Branch C — Maintenance

Two operations:

- **`re-synthesize the library`** — regenerates every `_creator-summary.md` and the `_synthesis.md` from the current set of entries. Use after a bulk import or when you change the schema.
- **`audit the library`** — flags outliers, vocabulary inconsistencies, and missing performance data. Suggests fixes; never auto-applies destructive changes.

### Branch D — Fetch from IG URL

You paste an Instagram post URL (no screenshots). The skill calls `scripts/fetch-carousel.py`, which wraps `gallery-dl` to:

1. Extract the shortcode from the URL.
2. Reuse cookies from your logged-in browser session.
3. Download each slide as `1.jpg`, `2.jpg`, … to `assets/fetched/<shortcode>/`.
4. Print a JSON summary (creator handle, slide count, file paths).

The skill confirms creator + slide count back to you, then hands off to Branch A. The fetcher is just an input shim — it doesn't change the deconstruction.

The `assets/fetched/` directory is **gitignored** — raw images never leave your machine.

---

## What the skill is honest about

The skill enforces honesty rules so the library doesn't get poisoned by overconfident claims:

- **Font names are propositions, not verdicts.** When uncertain, the skill lists 2–3 candidates with `confidence: low`. Verify with WhatTheFont / WhatFontIs / Adobe Fonts Visual Search before trusting.
- **Engagement signals are inferred from a static frame** unless you provide actual analytics. Phrasing is "appears to" / "structure suggests," not "this will go viral."
- **Industry benchmarks** (slide-count zones, save rates, etc.) are labeled "industry benchmark — directional only." They're priors, not laws.
- **Cross-creator claims** require ≥3 entries showing the pattern. Single-entry entries can't make creator-signature claims; that's reserved for `_creator-summary.md` after 5 entries; cross-creator-convention claims wait for `_synthesis.md` after 10 entries across ≥2 creators.

---

## What the skill won't do

- Bulk-scrape feeds, hashtags, or stories (one URL = one post).
- Bypass private accounts (if you can't see the post in a browser, the fetcher can't either).
- Log in to Instagram for you (you must already be logged in to a supported browser).
- Fabricate engagement metrics (only your own posts can populate `performance:` blocks).
- Promise outcomes ("this will go viral" is out — engagement is yours to measure).

---

## Working with your own carousels

You can analyze your own posts the same way as third-party creators, with one difference: you can populate the `performance:` block with real metrics from IG Insights.

Your entries go in `references/style-dna/_own/` instead of a creator folder. The skill uses your own data to build a `_own/_creator-summary.md` over time and (once you have ≥10 entries with metrics) starts surfacing engagement correlations: which palettes save best, which hook formulas drive the highest swipe-through rate, etc.

When you ask for a brief in "my own style," the skill reads `_own/_creator-summary.md` and uses it as the basis.

---

## Common operations cheat sheet

| Goal | Say |
|---|---|
| Analyze a carousel from a URL | Paste the URL: `https://www.instagram.com/p/ABC123/` |
| Analyze a carousel from screenshots | Attach the slide images, in order |
| Design something in a creator's style | `design a carousel about <topic> in @creator's style` |
| Get a Figma spec | Add `as a Figma spec` to the brief request |
| Get Midjourney prompts | Add `as MJ prompts` |
| Get just the headlines | Add `copy only` |
| Save a brief to disk | `save this brief` after the brief is shown |
| Force a synthesis rebuild | `re-synthesize the library` |
| Find inconsistencies | `audit the library` |
| Free up disk space | Delete `assets/fetched/` — entries don't reference it |

---

## Schema validation rules

Every library entry must satisfy these rules (the skill checks them before saving):

1. YAML frontmatter parses cleanly.
2. All required fields for the entry type are present and non-null.
3. `schema_version: 1`.
4. `slide_count == len(copy.word_counts_per_slide)` for carousel entries.
5. Every contrast pair's `fg` and `bg` appears in the declared palette.
6. Hex codes match `^#[0-9A-F]{6}$` (6-digit uppercase).
7. Tags match `^[a-z0-9]+(-[a-z0-9]+)*$` (lowercase-hyphenated).
8. Filename follows `<creator-handle>/YYYY-MM-DD_<slug>.md`.

If a rule fails, the skill flags it before committing instead of silently writing a broken entry.

---

## Troubleshooting the fetcher

| Symptom | Cause | Fix |
|---|---|---|
| `gallery-dl is not installed` | Not on PATH | `pip install gallery-dl` |
| `Unable to find Firefox cookies database` | Wrong browser flag | Pass `--cookies-from-browser chrome` (or your actual browser) |
| `HTTP redirect to login page` | IG wants auth | Make sure you're logged into the named browser; pass `--cookies-from-browser` |
| `No images downloaded` | Post is private, deleted, or a Reel video | Verify the URL in a browser; if private, you need to follow the account |
| `Could not extract IG shortcode from URL` | Profile / story / tag URL, not a post | Paste a single-post URL ending in `/p/<code>/` or `/reel/<code>/` |
| `gallery-dl exited with code N` (rate limit) | Too many requests | Wait 15–30 minutes, try again |

---

## Repository

This skill lives at:

```
github.com/Jose-Gael-Cruz-Lopez/carousel-dna
```

Clone it into `~/.claude/skills/carousel-design-analysis/` to install — Claude Code auto-detects skills in that directory.

The repo contains only the skill machinery. No personal carousel data, no fetched images, no analyzed creator entries. The library state on your machine is yours alone unless you choose to commit it.

---

## License & TOS note

Instagram's terms of service restrict automated access. This skill is built for **personal research on public posts** — analyzing creators you'd manually scroll past anyway, in the same volume a normal human would. Don't run the fetcher in a loop, don't run it against accounts you can't view in a browser, and don't ship a public service that calls it.
