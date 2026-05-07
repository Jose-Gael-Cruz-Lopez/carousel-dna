# Visual vocabulary

## Purpose

This file is the language the deconstruction protocol uses for visual fields. When you fill in a `palette`, `typography`, `layout`, `imagery`, or `motifs` value in a Schema A carousel entry, the value should come from the taxonomies defined below. Use this vocabulary to keep entries comparable across creators: two analysts looking at the same carousel should land on the same descriptors, and the cross-creator synthesis (Schema C) only works if the underlying entries speak the same dialect. If a phenomenon you observe does not fit any term here, prefer an existing close match plus a short prose note in the body, rather than inventing a new tag in the YAML.

## Color

### Hex extraction and role assignment

Read every hex code as 6-digit uppercase (`#1A1A1A`, never `#1a1a1a`) per schema convention. When tagging hexes into `palette.background`, `palette.primary_text`, `palette.accent`, and `palette.signature`, assign roles **functionally, not positionally**. The role is "what does this color *do* on the slide," not "where on the canvas does it sit."

- `background`: the field a slide reads against. Usually the largest area; on photo-led slides it may be the dominant graded tone of the photo, not the literal canvas color.
- `primary_text`: the dominant ink color used for headline and body. If headline and body use different inks (e.g. gold headline on charcoal body), pick the body color as `primary_text` and put the headline color in `accent`.
- `accent`: colors that exist to draw the eye — used on key nouns, dividers, number chips, signature underlines, swipe arrows. A color that appears once decoratively still counts.
- `signature`: the single hex most identified with this creator across their feed, not just this carousel. Often equals `accent[0]`. If unsure, leave it equal to the strongest accent and flag with `confidence: low` in body prose.

If a color appears as both background (slide 1) and accent (slide 4), list it under whichever role it serves on the slide where it most carries meaning. Do not list a hex in two roles.

### Harmony types

Pick exactly one for the `palette.harmony` descriptor's structural component (the descriptor itself can include emotional adjectives, e.g. `"warm-neutral-with-gold"`, but the structure should map to one of these):

- **monochromatic**: single hue, multiple tints/shades/tones.
- **analogous**: 2-3 hues adjacent on the color wheel (≤30° apart).
- **complementary**: two hues opposite on the wheel (180°).
- **split-complementary**: a base hue plus the two neighbors of its complement.
- **triadic**: three hues evenly spaced (120° apart).
- **tetradic**: four hues forming a rectangle on the wheel (two complementary pairs).
- **achromatic**: black, white, and grays only, no chromatic content.
- **unstructured**: more than four hues with no discernible relationship; common in screenshot-heavy or meme carousels.

### Temperature and saturation profiles

Cross temperature × saturation to produce the descriptor. One-line vibes:

|             | high-sat                       | desaturated                      | muted                          |
|-------------|--------------------------------|----------------------------------|--------------------------------|
| **warm**    | hot, urgent, retail-energy     | sun-faded, californian, lived-in | terracotta-editorial, ceramic  |
| **cool**    | tech-launch, fluorescent, sport| corporate-clinical, fintech-blue | sea-glass, scandi-calm         |
| **neutral** | rare; often a single brand pop | newsprint, archival, document-y  | linen, oat, gallery-default    |

### WCAG contrast

For each entry in `palette.contrast_pairs`, compute `wcag_ratio` as the standard relative-luminance contrast ratio (1.0 to 21.0). Compute via `wcag-contrast-ratio` (npm) or any implementation of WCAG 2.1's relative luminance formula; Claude can also estimate from hex values when no script is available, but flag low confidence in the body if so. Levels:

- **AAA** (≥7:1): required for body text smaller than 18pt regular / 14pt bold.
- **AA** (≥4.5:1): required for normal-size body text.
- **AA Large** (≥3:1): acceptable only for text ≥24pt regular or ≥18.5pt bold.
- Below 3:1: fail — do not label as any AA level. Note the failure in body prose.

### Dirty vs clean palettes

- **Clean palette**: flat solid hexes, no grain, no patina, no overlay. Vector-true. Common in fintech, productivity, and modernist editorial carousels.
- **Dirty palette**: the same hex carries grain, paper-texture, halftone, slight grade, or a film-emulation curve. The hex you extract is an approximation of the dominant tone, not the literal pixel. When a palette is dirty, note this in body prose and consider tagging `imagery.treatment` accordingly even on text-only slides.

## Typography

### Classification tree

Identify each face down to a leaf. Examples are non-exhaustive; the leaf label is the load-bearing part.

- **serif**
  - **old-style** (humanist serifs, low contrast, slanted axis): Garamond, Caslon, Sabon.
  - **transitional** (sharper, more vertical axis): Baskerville, Times, Georgia.
  - **modern / didone** (extreme thick-thin, vertical stress): Bodoni, Didot, GT Sectra Display.
  - **slab** (thick rectangular serifs): Roboto Slab, Tiempos, Sentinel.
- **sans-serif**
  - **humanist** (calligraphic skeleton, open apertures): Gill Sans, Frutiger, Source Sans.
  - **grotesque** (early sans, slight contrast, sturdier): Akzidenz-Grotesk, Founders Grotesk.
  - **neo-grotesque** (refined geometry, closed apertures): Helvetica, Inter, ABC Diatype.
  - **geometric** (drawn on circles/squares): Futura, Avenir, Circular.
- **display**: faces designed for large sizes only; high personality, often poor at body size. Druk, GT Sectra Display, Migra.
- **script**: handwriting/calligraphy. Caveat, Allura, Tangerine.
- **monospace**: fixed-width. JetBrains Mono, IBM Plex Mono, Berkeley Mono.

### Pairing patterns

When you can identify the headline/body relationship, tag it as one of these pairing patterns in `typography_consensus.pairing_pattern` (Schema B) or in body prose (Schema A):

- **editorial** (`serif-display + sans-body`): magazine archetype. Tiempos + Inter, GT Sectra + Söhne.
- **modernist** (single-family weight contrast): one family, dramatic weight jump (e.g. Inter Black headline + Inter Regular body).
- **minimalist** (all-one-weight): one family, one weight, hierarchy from size and color only.
- **technical** (mono-everything): a monospace face for both headline and body, often with all-caps headlines.
- **mixed-script** (sans + script accent): rare, vibe-driven creator carousels using a script font for one decorative word.

### Type scale on 1080×1350

These are conventions, not laws. Use them as priors when estimating `size_px` ranges:

- **cover headline**: 64-96pt equivalent (roughly 96-144 px at 1× rendering on a 1080-wide canvas).
- **subhead / slide title**: 32-48pt (48-72 px).
- **body**: 22-32pt (32-48 px). Modern sans body on IG typically lands 24-28pt.
- **caption / footnote / handle**: 14-18pt (20-28 px).

For square 1080×1080 slides, scale all bands down ~10%. For 9:16 stories (1080×1920), scale headline up ~15%.

### Tracking conventions

- **Tight display headlines**: `tracking_em` between -0.01 and -0.03 (i.e. -1% to -3%). Common on serif-display headlines and bold sans display.
- **Body**: `tracking_em` 0 (default). Anything other than 0 on body text deserves a note.
- **Small caps and labels**: `tracking_em` +0.05 to +0.15 (+5% to +15%). Required for legibility when casing is uppercase at small sizes.

### Casing semantics

Match Schema A's `casing` enum (`title-case` | `uppercase` | `lowercase` | `sentence-case`) and use these rules to read intent:

- **title-case**: editorial headlines, "polished" tone.
- **sentence-case**: body copy, conversational headlines, modern-software defaults.
- **uppercase**: emphasis, labels, eyebrows, dividers; signals authority or category.
- **lowercase**: vibe-driven creator-y carousels (poetry/wellness), intentional casualness, anti-corporate signal.

### Identification confidence

When committing a font name to `typography.headline.family.value` or `.body.family.value`:

- **high** confidence (no list needed): the face has unmistakable glyphs (e.g. GT Sectra's leg of the `R`, Druk's compressed weight, Migra's `g`, Söhne's `a`). Commit a single name.
- **med** confidence: glyphs are consistent with 1-2 close cousins. Commit the most-likely name in `value` and put alternates in `fallbacks`.
- **low** confidence: you can name the genus (e.g. "geometric sans") but not the species. Use a 2-3 candidate list in `value` (e.g. `["Circular", "Avenir Next", "Gotham"]`) and set `confidence: low`.

Default to `med` unless you have direct evidence — over-confident font calls are the most common error in this skill.

## Layout & grid

### Canvas conventions

- **1080×1350** (4:5): IG carousel default; the assumed canvas unless stated otherwise.
- **1080×1080** (1:1): square fallback, common in older accounts and in cross-posted LinkedIn carousels.
- **1080×1920** (9:16): Stories/Reels covers, occasionally repurposed as carousel.

Outer margin defaults: **64-128 px** on a 1080-wide canvas (≈6-12% of width). Margins narrower than 48 px feel poster-like or aggressive; wider than 144 px feel breathy or gallery-grade. Record the margin as `layout.margin_pct` (percentage of canvas width).

### Alignment families

Match Schema A's `layout.alignment` enum: `left | center | right | justified | mixed`. Editorial signals:

- **left**: default for editorial and information-dense carousels; signals "read me like an article."
- **center**: signals announcement, manifesto, quote-card; gives every line equal weight; risks monotony over 7+ slides.
- **right**: rare; signals deliberate, often paired with right-anchored imagery on the left.
- **justified**: signals print-newspaper or formal document; common in book-quote carousels.
- **mixed**: tag this when alignment changes across slides as a deliberate device, not as drift.

### Balance

Match `layout.balance` enum: `symmetric | asymmetric | radial`.

- **symmetric**: mirror-image around vertical or horizontal axis; static, formal.
- **asymmetric**: weighted off-center; dynamic, modern editorial default.
- **radial**: elements arrange around a center point; rare, often on a single hero slide.

### Focal placement

Match `layout.focal_placement`. Standard values:

- **rule-of-thirds-left / rule-of-thirds-right**: focal point at a thirds-grid intersection.
- **golden-ratio**: focal at φ ≈ 0.618 of width or height.
- **center**: dead-center; manifesto, quote, announcement.
- **upper-third / lower-third**: focal anchored high or low; "upper-third" is the editorial-headline default.
- **edge-anchored**: focal hugs left, right, top, or bottom edge — bleeding off; signals motion or boldness.

### Grid families

Record in `layout.grid` as a short descriptor. Families:

- **single-column**: one stacked column of text/image blocks; default for text-driven carousels.
- **two-column**: side-by-side columns; common for compare/contrast or label+value structures.
- **modular** (e.g. `loose-12-col`, `strict-6-col`): repeating modules across slides, often a 6 or 12-column underlying grid.
- **masonry**: variable-height tiles, rare in carousels.
- **none**: free composition with no detectable grid; common in handcrafted, illustration-heavy work.

### Slide-rhythm types

Record in `layout.rhythm`. Three primary patterns plus modifiers:

- **templated**: every slide uses the same structural template (same headline position, same body block); maximum consistency, minimum surprise.
- **evolving / panoramic**: composition shifts continuously from slide to slide as if the camera is panning; cinematic.
- **variant**: each slide is its own composition with no shared template; portfolio-grade or experimental.
- Modifiers (combine with the above): `varied-density`, `crescendo` (intensity climbs to a peak), `call-and-response` (alternating slide types), `uniform`.

## Spacing

### Base-unit detection

Most modern carousels are built on a **4 px** or **8 px** base unit (rarely 6 px). Spot it by looking for consistent multiples in:

- outer margins (e.g. 96 = 8×12, 64 = 8×8),
- gaps between text blocks (e.g. 24, 32, 48 — all multiples of 8),
- the height of single-line text blocks (font size + leading often resolves to a multiple).

If margins are 64 / 96 / 128 px and gaps are 16 / 24 / 32 / 48 px, the base is almost certainly 8. If you also see 4, 12, 20, 28, the base is 4. If multiples are inconsistent across slides, note "no detectable base unit" rather than forcing one.

### Whitespace ratio bands

Record in `layout.whitespace_ratio` (0-1). Bands:

- **minimal** (<0.25): dense, information-packed; common in step-by-step tutorials.
- **balanced** (0.25-0.50): editorial default; readable without feeling sparse.
- **breathy** (0.50-0.70): premium-feeling, gallery-adjacent; common in wellness and finance-luxury.
- **gallery** (>0.70): poster-like; one short headline floating in space.

### Vertical rhythm

- **consistent baseline grid**: line heights and inter-block gaps resolve to multiples of a single baseline unit. Signals print-design literacy.
- **free-form**: vertical spacing varies per slide based on composition needs. Most common; not a defect.

Note which one applies in body prose if it's load-bearing for the creator's signature.

## Imagery treatment

### Type tags

For `imagery.type`. The Schema A enum is short (`none | photo | illustration | mixed | data-viz`); when filling that field, pick from the schema's enum, but in body prose use these finer tags:

- **photo**: photographic imagery, as-is or graded.
- **illustration-vector**: clean vector illustration; flat or with simple shading.
- **illustration-organic**: hand-drawn, watercolor, brush, or painterly illustration.
- **3D-render**: rendered 3D objects or scenes (Spline, Blender, C4D look).
- **screenshot**: literal app/web screenshots; common in tech/productivity creators.
- **mockup-device**: imagery placed inside a phone/laptop/tablet frame.
- **mockup-paper**: imagery placed on a paper, magazine, or book mockup.
- **abstract-geometric**: purely geometric shapes/patterns, no representation.
- **no-imagery**: text-only slides; map to schema enum `none`.

### Treatment tags

For `imagery.treatment` and body prose. Pick whichever applies; combine with `+` if multiple (e.g. `warm-grade+grain`):

- **ungraded**: no detectable color treatment.
- **warm-grade**: pushed toward yellow/orange/red.
- **cool-grade**: pushed toward blue/cyan/green.
- **duotone**: image mapped to two colors only.
- **halftone**: dot-pattern reproduction, print-process aesthetic.
- **grain**: visible film-grain or noise overlay.
- **paper-texture**: paper, kraft, or newsprint texture overlay.
- **glassmorphism**: frosted-glass blur effects on translucent layers.
- **brutalist**: harsh, low-fidelity, intentionally crude treatment (raw screenshots, jpeg-artifact, photocopy).

### Icon-style tags

For `imagery.icon_style`. Match Schema A's hint enum (`line | filled | duotone | hand-drawn | null`) and extend with:

- **outline / line**: stroked icons, no fill.
- **filled**: solid-shape icons.
- **duotone**: two-color icons (commonly accent + neutral).
- **3D**: rendered 3D icons (Apple-emoji-like, Spline-like).
- **hand-drawn**: sketched icons, intentional irregularity.
- **none**: no icons used.

## Motifs

### Catalog of common recurring devices

These populate the `motifs` array in Schema A. Tag each as a lowercase-hyphenated slug (e.g. `numbered-rules`, `hairline-divider-between-rules`). Common entries:

- **number chips / numbered rules**: numerals (often in a pill or circle) leading each rule.
- **hairline rules**: 1-2 px dividers separating sections.
- **thick-bar dividers**: 4-12 px horizontal bars used as section breaks.
- **brackets `[ ]`**: bracket pairs framing a word or phrase.
- **pull-quote frames**: a quote slide with prominent quotation marks or a framing rule.
- **sparkles ✦**: ornament glyphs as decoration.
- **hand-drawn arrows**: scribbled arrows pointing at a word or chart element.
- **highlight underlines (Notion-style)**: a colored block behind a key word, often pastel.
- **gold-underline / accent-underline**: a thin colored rule under a key noun.
- **pricing tags**: tag-shape graphics with a price or label.
- **"NEW" badges**: small badge graphics calling out a tag word.
- **swipe-arrow indicators on slide 1**: an arrow or "swipe →" cue on the cover.
- **page-number / slide-counter** (e.g. `2/7`): pagination glyphs.

### System-motif rule

If a motif appears on **≥60% of slides** in a single carousel, treat it as a *system motif* — it is part of the design system and worth replicating when generating in this style. Include it in `motifs` and call it out in the body prose.

If a motif appears on <60% of slides, it is *decorative* — list it in `motifs` only if it is visually load-bearing on the slide where it appears (e.g. the swipe-arrow on the cover slide). Otherwise omit.

When promoting motifs to `signature_motifs` in a creator_summary (Schema B), require the motif to be a system motif in **≥50%** of the synthesized carousels.

## Quick reference table

Map every Schema A YAML field defined in `schema-style-dna.md` to the section above where its allowed values are defined.

| Schema A field                       | Vocabulary section                          | Notes                                                          |
|--------------------------------------|---------------------------------------------|----------------------------------------------------------------|
| `palette.background`                 | Color → Hex extraction and role assignment  | List of hexes; role = "what reads as the field on the slide".  |
| `palette.primary_text`               | Color → Hex extraction and role assignment  | Single hex; the dominant ink.                                  |
| `palette.accent`                     | Color → Hex extraction and role assignment  | List of hexes; emphasis colors.                                |
| `palette.signature`                  | Color → Hex extraction and role assignment  | Single hex; creator-identifying.                               |
| `palette.harmony`                    | Color → Harmony types; Temperature/saturation | One-line descriptor; combine structural + emotional terms.    |
| `palette.contrast_pairs[].wcag_ratio`| Color → WCAG contrast                       | Numeric 1.0-21.0.                                              |
| `palette.contrast_pairs[].wcag_level`| Color → WCAG contrast                       | `AAA` / `AA` / `AA Large` / fail.                              |
| `typography.headline.family`         | Typography → Classification tree; Identification confidence | Use confidence map for inferred values.        |
| `typography.headline.weight`         | Typography → Classification tree            | Numeric 100-900.                                               |
| `typography.headline.size_px`        | Typography → Type scale on 1080×1350        | Range or single int.                                           |
| `typography.headline.tracking_em`    | Typography → Tracking conventions           | Negative for tight headlines.                                  |
| `typography.headline.casing`         | Typography → Casing semantics               | One of the four enum values.                                   |
| `typography.body.*`                  | Typography → Classification tree, Type scale, Tracking, Casing | Same rules as headline, defaults differ.    |
| `layout.alignment`                   | Layout & grid → Alignment families          | Schema enum; pick "mixed" only when intentional.               |
| `layout.margin_pct`                  | Layout & grid → Canvas conventions          | 6-12% is the default band.                                     |
| `layout.grid`                        | Layout & grid → Grid families               | Short descriptor.                                              |
| `layout.balance`                     | Layout & grid → Balance                     | Schema enum.                                                   |
| `layout.focal_placement`             | Layout & grid → Focal placement             | Schema enum + extensions allowed.                              |
| `layout.rhythm`                      | Layout & grid → Slide-rhythm types          | Combine type + modifier where useful.                          |
| `layout.whitespace_ratio`            | Spacing → Whitespace ratio bands            | 0-1 numeric; band names go in body prose.                      |
| `imagery.type`                       | Imagery treatment → Type tags               | Schema enum is short; finer tags belong in body prose.         |
| `imagery.treatment`                  | Imagery treatment → Treatment tags          | Combine with `+` for stacked treatments.                       |
| `imagery.icon_style`                 | Imagery treatment → Icon-style tags         | Schema hint enum + extensions.                                 |
| `motifs[]`                           | Motifs → Catalog; System-motif rule         | Lowercase-hyphenated; apply ≥60% rule before tagging.          |

When a vocabulary item here doesn't fit the slide cleanly, prefer the closest existing tag and explain in body prose. False precision is worse than honest fuzziness — flag uncertainty rather than inventing new YAML enum values mid-entry.
