# Copy Vocabulary

## Purpose

This file is the controlled vocabulary for everything that lands in the `copy:` block of a `entry_type: carousel` entry as defined in `schema-style-dna.md`. When you fill `cover_hook`, `hook_formula`, `narrative_arc`, `cta`, `voice`, or `word_counts_per_slide`, the **values** must come from the taxonomies below. Free-form descriptors are not allowed in tag fields. Use this file as the lookup table — schema defines the slots, this file defines the legal contents.

Where this doc cites engagement-rate numbers, treat them as **directional industry data**, not gospel. Carousel performance varies wildly by creator, niche, and platform mood. Patterns here are starting hypotheses, not laws.

---

## 1. Hook formula taxonomy

Six canonical archetypes, plus `hybrid` for combinations. Use the exact tag string in the `copy.hook_formula` field. For hybrids, join two tags with `+` (e.g., `listicle+regret`, `contrarian+identity-callout`) — see the `@jenny.example` reference entry for the canonical hybrid format.

### `curiosity-gap`

Open a loop the reader can only close by swiping. State that hidden knowledge exists, withhold the knowledge.

- **Example:** "The 1 thing nobody tells you about freelancing."
- **Working when:** swipe-through rate spikes between slides 1 and 2; comments ask "what is it?"
- **Overused when:** every cover starts "the 1 thing nobody tells you" — readers learn the pattern and disengage. Industry data suggests novelty erosion after a creator runs the same gap formula 4+ posts in a row (directional).

### `contrarian`

Negate a widely-accepted belief. Lead with "stop," "don't," or a direct contradiction of conventional wisdom.

- **Example:** "Stop journaling. Here's why everyone gets it wrong."
- **Working when:** comments split into two camps; saves climb because readers want the receipts mid-feed.
- **Overused when:** the contrarian claim has no payoff inside, or the creator contradicts themselves across posts. Audience reads it as bait.

### `listicle`

Promise a numbered set of items. Specificity and odd numbers (3, 5, 7, 9) outperform round numbers in directional industry data — odd-number titles tend to feel less manufactured.

- **Example:** "7 ways to write a better cold email."
- **Working when:** the cover number matches the actual count inside; each slide delivers one discrete item.
- **Overused when:** the list pads to hit the cover number, or items overlap. Readers stop saving when they sense filler.

### `identity-callout`

Name the reader's identity directly. The hook only lands if you are the named person.

- **Example:** "If you're a designer who hates writing, read this."
- **Working when:** the named identity is specific enough to feel personal but broad enough to capture the audience; replies say "this is me."
- **Overused when:** the identity is so narrow that reach collapses, or so broad ("if you're a human who breathes") that it reads as gimmick.

### `bold-claim`

Stake a measurable, often financial or outcome-based, assertion. Numbers and timeframes carry the weight.

- **Example:** "I made $42k in 30 days. Here's the playbook."
- **Working when:** the claim is unusual enough to stop the scroll and the carousel actually shows the playbook.
- **Overused when:** the number is unverifiable, the playbook is generic, or the creator runs identical claims weekly. Reads as flex rather than teaching.

### `direct-question`

Ask the reader something they want to answer for themselves. The question implies a desirable outcome.

- **Example:** "What if you could write a book in a weekend?"
- **Working when:** the question matches an active desire of the niche; the carousel answers it concretely.
- **Overused when:** the question is rhetorical and the answer is "yes obviously" — no tension, no swipe.

### `hybrid`

Two formulas stacked. Use `+` to join. Pick the dominant formula first, the modifier second.

- **Examples:** `listicle+regret` ("7 things I wish I knew at 22"), `contrarian+identity-callout` ("If you're a founder, stop hiring junior devs"), `curiosity-gap+bold-claim` ("The one habit that 10x'd my income").
- **Working when:** each component does distinct work — the listicle promises structure, the regret promises emotional payoff.
- **Overused when:** stacking three or more formulas. The hook becomes a buzzword pile and stops being legible.

---

## 2. Narrative arc taxonomy

Write the arc as `Stage → Stage → Stage` in `copy.narrative_arc`. Use `×N` for repeated stages (e.g., `Steps×5`). Use stage names from this taxonomy when possible; coin new stage names only when no existing name fits.

### Schematic templates

- `Hook → Pain → Reframe → Framework → Steps×N → Proof → CTA`
- `Hook → Promise → Listicle×N → Recap → CTA`
- `Hook → Story-open → Tension → Turn → Lesson → CTA`
- `Cover → Cliffhanger → Body → Save-prompt → Follow-CTA`

### Frame definitions

- **AIDA** — Attention → Interest → Desire → Action. Marketing-classic. Best for product or offer carousels.
- **PAS** — Problem → Agitate → Solve. Emotionally heavy; best when the audience is already aware of the pain.
- **BAB** — Before → After → Bridge. Transformation-focused. Bridge slide carries the teaching weight.
- **Hero's-Journey-micro** — Ordinary-state → Call → Trial → Return-with-lesson. Compressed into 6–10 slides; story-driven creators favor this.
- **Listicle** — Hook → Promise → Item×N → Recap → CTA. Most common arc in saves-driven niches (productivity, money, self-improvement).
- **Framework-Reveal** — Hook → Pain → Framework-name → Step-by-step → Proof → CTA. The Framework-name slide is where the audience screenshots.
- **Contrarian-Essay** — Hook (contrarian) → Common-belief → Why-it's-wrong → Real-mechanism → New-rule → CTA. Higher comment rate, lower save rate (directional).
- **Case-Study** — Hook → Subject → Starting-state → Intervention → Result → Takeaway → CTA. Works when the subject (you, a client, a known figure) carries authority.

### Stage glossary

Use these names where they fit:

| Stage name | What happens |
|---|---|
| `Hook` | The cover; opens the loop |
| `Cover` | Synonym for Hook when the visual carries equal weight |
| `Promise` | States what the reader will learn |
| `Pain` | Names the reader's current struggle |
| `Agitate` | Twists the pain to make it acute |
| `Reframe` | Reinterprets the pain as solvable |
| `Framework` | Introduces a named system |
| `Steps×N` | N stepwise instructions |
| `Listicle×N` | N parallel items |
| `Story-open` | Anecdote begins |
| `Tension` | Story-stakes raised |
| `Turn` | Story-pivot |
| `Lesson` | Generalizable takeaway from story |
| `Proof` | Receipts, screenshots, numbers |
| `Recap` | Summarizes the body |
| `Save-prompt` | Asks for save |
| `Share-prompt` | Asks for share |
| `Follow-CTA` | Asks for follow |
| `Cliffhanger` | Mid-carousel teaser pulling the next swipe |

### Notation rule

Always render arcs with spaced arrows (` → `, U+2192 with spaces around it). Use `×N` immediately after the stage name with no space (`Steps×5`, not `Steps × 5`). Cap arcs at 8 stages — longer arcs usually mean the carousel is over-scoped.

---

## 3. Slide-2 standalone test

Instagram replays carousels: a viewer who scrolls past slide 1 may see slide 2 first on a re-surface, or slide 2 may appear in the explore preview. **Slide 2 must function as a cover on its own.** If slide 1 holds the only context that makes slide 2 legible, the carousel loses retry views.

When filling `engagement_inferred.slide_2_standalone` (boolean), apply this test: cover slide 1 with your hand. Read slide 2 cold. Does it still hook?

### Three patterns that pass

1. **Restated promise** — Slide 2 repeats the cover hook in different words ("Here's exactly how I did it").
2. **First item with context** — In a listicle, slide 2 reads "1. [Item] — [why it matters]" so the structure is self-evident.
3. **Standalone question** — Slide 2 poses a question the reader can engage with even without slide 1's framing.

### Three patterns that fail

1. **Pronoun without referent** — Slide 2 says "this is why" but "this" is only defined on slide 1.
2. **Continuation without recap** — Slide 2 says "And the second reason is…" with no first reason visible.
3. **Punchline-first** — Slide 2 delivers the payoff but slide 1 carried the setup; without setup, the punchline is noise.

---

## 4. CTA patterns

Use the tag string in `copy.cta.type`. The schema currently lists `save | share | follow | comment | link-in-bio | none`; the canonical extended set below maps onto those values, with `multi` reserved for combos and added to creator_summary notes.

### `save-prompt`

- **Copy:** "save this for later," "screenshot this," "bookmark for the next time you…"
- **Works when:** the carousel is reference material — a checklist, a framework, a list the reader will return to.
- **Backfires when:** the content is opinion-driven or news-driven. Readers don't save what they won't reread.

### `share-prompt`

- **Copy:** "send this to a friend who…," "tag someone who needs this."
- **Works when:** the audience has a clear in-group (founders, designers, parents of toddlers). Identity-callout hooks pair well.
- **Backfires when:** the implied target is generic ("send to anyone"). Readers don't tag without specificity.

### `comment-prompt`

- **Copy:** "comment X for the link," "drop a 🔥 if you agree."
- **Works when:** the creator can DM in response, or the comment unlocks a resource. Strong for list-building.
- **Backfires when:** the comment is bait without payoff. Algorithm-trained audiences recognize and disengage.

### `follow-prompt`

- **Copy:** "follow @handle for more like this."
- **Works when:** the carousel is the reader's first encounter — niche-defining content.
- **Backfires when:** stacked on every post; reads as desperate. Reserve for tentpole posts.

### `link-cta`

- **Copy:** "link in bio," "DM 'guide' for the link."
- **Works when:** there is an actual destination — newsletter, product, full article.
- **Backfires when:** the link is the carousel's only purpose. Reader feels baited if the in-feed value is thin.

### `multi`

- **Copy:** combos — "Save this AND send it to one founder you know."
- **Works when:** the two asks reinforce each other (save = personal use, share = social use).
- **Backfires when:** stacking three+ asks. Reader picks none.

### `none`

- **Copy:** absent.
- **Works when:** the carousel ends on a closing line that lets the reader sit with the idea — common in poetic/editorial creators.
- **Backfires when:** the carousel is reference material. Without a save-prompt, save rate underperforms (directional industry data).

### Voice variants

- **Imperative** — "Save this." Direct, high-velocity. Works in casual and Gen-Z-internet registers.
- **Invitational** — "If this helped, you might want to save it for later." Softer, fits academic/poetic registers.
- **Question** — "Want the rest? Comment 'yes.'" Activates response bias; pairs with comment-prompt.

---

## 5. Voice and tone markers

Map values to the schema's `copy.voice` block. The schema has `tone`, `person`, `formality`; expand here with sub-markers a reader should still capture in `tags` or in body prose.

### Register

Use one of: `academic`, `professional`, `casual`, `gen-z-internet`, `poetic`.

- `academic` — citations, qualifications, hedging.
- `professional` — declarative, business-context, low-emotion.
- `casual` — contractions, conversational asides.
- `gen-z-internet` — lowercase, irony, in-group references.
- `poetic` — fragmentary, image-driven, elliptical.

### Sentence-length profile

- `short-punchy` — average <10 words/sentence.
- `medium` — 10–18 words/sentence.
- `flowing` — >18 words/sentence.

### Emoji usage

- `none` — no emoji.
- `decorative-rare` — 1–2 emoji per carousel as visual punctuation.
- `functional-frequent` — emoji as bullets, dividers, or list markers.
- `dense` — emoji woven into prose; common in gen-z-internet register.

### Casing patterns

- `title-case-headlines` — Each Major Word Capitalized.
- `sentence-case-body` — Standard prose casing.
- `all-caps-emphasis` — Selective WORDS for emphasis; never whole sentences (legibility cost).
- `all-lowercase-vibes` — full lowercase as aesthetic choice.

### Punctuation tics

- `terminal-period-skip` — display headlines drop the final period (modern editorial).
- `em-dashes-emphasis` — em-dashes set off asides — like this.
- `colons-for-setup` — colon before the payoff: like that.
- `ellipses-cliffhanger` — trailing "…" pulls the next swipe.

### Person

Match `copy.voice.person` to: `first` (I/we), `second` (you), `impersonal` (one/the reader), `mixed`.

---

## 6. Copy-density bands

Compute average words per slide as `mean(copy.word_counts_per_slide)`. Map to a band:

| Band | Words/slide avg | Notes |
|---|---|---|
| `minimal` | <8 | Display-driven; typography carries the weight |
| `light` | 8–15 | The engagement sweet spot per industry data (directional) — reads quickly, saves easily |
| `medium` | 15–25 | Story-driven and framework carousels; readers slow down |
| `dense` | 25–40 | Educational; risks losing casual scrollers |
| `wall` | >40 | Rarely earns saves; readers default to skipping |

Bands are starting hypotheses, not rules. A `wall` carousel from a known authority can outperform a `light` one from a stranger.

---

## 7. Cliffhanger devices

Used to score `engagement_inferred.swipe_cliffhangers` (`low | med | high`). Specific techniques:

- **Open-loop** — "more on this in slide 5." Names a future payoff to keep the reader swiping.
- **Partial reveal** — Slide ends mid-thought; the next slide completes it. Visual: a sentence breaks across the slide boundary.
- **Numbered tease** — "the 3rd one will surprise you." Listicle-specific; sets a target slide.
- **Question with delayed answer** — Slide poses a question, the next 2–3 slides build before answering. Highest tension when the answer is genuinely non-obvious.
- **Contrarian setup** — Slide states a common belief, next slide negates it. Works in essay arcs.
- **Framework name-drop** — Slide names the framework, the next slides decode it. Reader stays for the decode.

A carousel with zero cliffhangers across mid-slides drops swipe-through rate sharply (directional).

---

## 8. Quick-reference table

Every YAML field in the schema's `copy:` block, mapped to its definition section in this file.

| Schema field | Defined in |
|---|---|
| `copy.cover_hook` | Free text — the literal cover headline. No taxonomy; quote verbatim |
| `copy.hook_formula` | §1 Hook formula taxonomy (use exact tag, `+` for hybrids) |
| `copy.word_counts_per_slide` | §6 Copy-density bands (compute mean, map to band in `tags`) |
| `copy.narrative_arc` | §2 Narrative arc taxonomy (use ` → ` separator, `×N` for repetition) |
| `copy.cta.type` | §4 CTA patterns (use schema-allowed tag) |
| `copy.cta.placement` | Schema-defined: `final-slide | every-slide | none | inline` |
| `copy.cta.copy` | Free text — quote verbatim |
| `copy.voice.tone` | §5 Voice and tone markers (register + tone descriptors) |
| `copy.voice.person` | §5 Voice and tone markers (`first | second | impersonal | mixed`) |
| `copy.voice.formality` | §5 Voice and tone markers (register + casing patterns) |
| `engagement_inferred.slide_2_standalone` | §3 Slide-2 standalone test |
| `engagement_inferred.swipe_cliffhangers` | §7 Cliffhanger devices |
| `engagement_inferred.save_bait` | §4 CTA patterns (save-prompt section) + §6 density bands |
| `engagement_inferred.send_bait` | §4 CTA patterns (share-prompt section) |

When in doubt, prefer the canonical tag from this file over a creative one. Future Claude sessions need to aggregate across entries; novel tags break aggregation.
