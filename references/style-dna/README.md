# Style DNA Library

This folder is the persistent memory of the carousel-design-analysis skill. Every carousel ever analyzed lives here as a YAML+Markdown entry. Per-creator and cross-creator pattern summaries are derived from those entries.

## Layout

```
style-dna/
├── README.md                    ← you are here
├── _index.md                    ← table of every entry, append-only
├── _synthesis.md                ← cross-creator patterns (regenerated on demand)
├── <creator-handle>/            ← one folder per creator/aesthetic target
│   ├── YYYY-MM-DD_<slug>.md     ← one per analyzed carousel, append-only
│   ├── YYYY-MM-DD_<slug>.md
│   └── _creator-summary.md      ← per-creator synthesis (regenerated)
├── _own/                        ← Jose's own carousels (with performance: data)
└── _blends/                     ← derivative briefs that mix multiple styles
```

## Rules for writing here

1. **New analyses are NEW FILES.** Never overwrite. On filename collision, append `-v2`, `-v3`.
2. **Always append to `_index.md`** after writing a new entry.
3. **Synthesis files (`_synthesis.md`, `_creator-summary.md`) are regenerated, not patched.** Read all entries in scope, rewrite the file from scratch.
4. **Synthesis schedule:**
   - Per-creator summary regenerates on the 5th, 10th, 15th… entry for that creator.
   - Cross-creator synthesis regenerates on the 10th, 20th… entry overall.
   - User can request manual re-synthesis at any time.
5. **All entries validate against `../schema-style-dna.md`.** Schema version is in the YAML frontmatter.
6. **Outliers stay in the library.** Tag them `outlier` in `tags:` so they're excluded from synthesis but preserved as data.

## Filename conventions

- Per-carousel entry: `<creator-handle>/YYYY-MM-DD_<3-6-word-slug>.md`
- Slug: lowercase, hyphenated, derived from cover hook, no stopwords.
- Brief output (saved on request): `_blends/YYYY-MM-DD_<topic-slug>_brief.md`

## Folder semantics

- `_own/` — only the user's own carousels. These should always have `performance:` data populated, which feeds engagement-correlation analysis.
- `_blends/` — saved generation briefs that combine multiple style sources, OR briefs that don't belong to a single creator.
- `<creator-handle>/` — one folder per creator. Use the IG handle including `@` (e.g., `@jenny.example/`) or a clean tag if you don't want a real handle (e.g., `inspo-finance-1/`).

## How to query the library

For a quick overview: read `_index.md`. It's a single Markdown table — one row per entry.

To answer "what's @jenny.example's style?": read `<@jenny.example>/_creator-summary.md` only. Don't read every entry — the summary already synthesizes them.

To answer "what's universal across creators?": read `_synthesis.md` only.

To answer "what specific carousel did Jose say he loved?": grep `_index.md` for the headline keyword, then read just that entry file.
