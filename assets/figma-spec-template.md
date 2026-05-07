# Figma spec template

## When to use

This is the default output format when the user asks Claude to design a carousel in a captured style — they want a "Figma spec," "design brief," "design tokens," or simply "give me a brief." It is the generation brief that turns a Schema B `creator_summary` (or a Schema A `carousel` entry) into something a designer can paste straight into Figma. **Output goes inline in the chat, not to a file**, unless the user explicitly says "save it" or names a target path. Inline-by-default keeps the brief reviewable in the conversation; saving on demand keeps the working library uncluttered.

## Template body

Fill placeholders in `<angle brackets>`. Drop sections that do not apply rather than leaving stub lines. Date format is ISO-8601.

```markdown
# Carousel Spec: <topic>
Style basis: <@creator's style DNA, generated YYYY-MM-DD>
Slide count: <N>

## Canvas
1080 × 1350 px (4:5). Outer margin <Npx>.

## Color tokens (paste into Figma variables)
| Token | Hex | Use |
|---|---|---|
| bg/primary | <#HEX> | <use> |
| surface | <#HEX> | <use> |
| text/primary | <#HEX> | <use> |
| accent/cta | <#HEX> | <use> |
| accent/2 | <#HEX> | <use> |

## Typography styles
| Style | Family | Weight | Size/Leading | Tracking | Color |
|---|---|---|---|---|---|
| Headline/XL | <family> | <weight> | <size>/<leading> | <tracking>% | text/primary |
| Body/Regular | <family> | Regular | <size>/<leading> | 0% | text/primary |
| Number-chip | <family> | <weight> | <size> | 0% | accent/cta |

## Components to build first
1. <component 1 — e.g. "Number chip"> — <description>
2. <component 2> — <description>
3. <component 3> — <description>

## Slide-by-slide

### Slide 1 — Cover
- **Headline (≤ 11 words):** "<exact copy>"
- **Subhead (optional):** "<exact copy>"
- **Layout:** <description>
- **Motif:** <if any>
- **Color emphasis:** <which token does the heavy lifting>

### Slide 2 — Hook restate / standalone-cover test
- **Must work as cover if shown first.**
- **Headline:** "<exact copy>"
- **Layout:** <description>

### Slide N — <role>
[...]

### Slide <last> — CTA
- **CTA text:** "<exact copy>"
- **CTA type:** save | share | follow | comment | link-in-bio | none  <!-- Schema A `cta.type` enum; pick one -->
- **Visual treatment:** <description>

## Motif system to enforce across slides
- <motif 1, e.g. "Hairline rule under every headline (1px, accent/2)">
- <motif 2>

## What I deliberately won't replicate
<If the captured style has elements that are too creator-specific or risky to copy, name them.>

## Notes for the designer
<Open issues, decisions to make in Figma, places to deviate from the captured style.>
```

## Brevity rule

The spec must fit on one screen of Figma's "guidelines" panel — aim for **1.5 pages of Markdown maximum**. If the source style has 15 components, do not list all 15; pick the 3–5 most important (the ones that carry the system motif and the cover/CTA treatments). Same rule for color tokens (5 is the cap), motifs (3–5), and slide-by-slide notes (one bullet per axis, not a paragraph). The deliverable's job is to be paste-ready, not exhaustive — the underlying creator summary already carries the long-form analysis. If the user wants the full background, point them to the Schema B summary file rather than expanding the spec.

## How SKILL.md selects this template

`SKILL.md` routes to this template when the user asks for a "Figma spec," "design brief," "design tokens," "style guide for a new carousel," or by default any time they say "give me a brief" / "spec this out" in a captured style. If they instead ask to *analyze* an existing carousel (deconstruct, score, describe), that's the Schema A entry path, not this template. When in doubt — the user wants something to hand to a designer or paste into Figma → use this template; the user wants something to add to the library → use Schema A.
