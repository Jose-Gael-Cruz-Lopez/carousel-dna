# Engagement Signals

## 1. Purpose & honesty disclaimer

This file catalogues the design choices that **correlate** with Instagram carousel engagement. It is the reference the deconstruction protocol's 5th pass consults when populating the `engagement_inferred:` block in Schema A and, when metrics exist, the `performance:` block. Treat every claim here as a correlation drawn from a static frame, not a causal law. Most signals are inferred from a carousel image with no analytics attached: we are reading affordances, not outcomes. Where we cite numeric thresholds (save rates, slide counts, dwell time), label them "industry benchmark — directional only" and never present as fact. When confidence is genuinely low (e.g. inferring send-bait from a static slide without seeing comments), use `{value: ..., confidence: low}` per the schema and say so in prose.

---

## 2. The four IG carousel engagement signals (Mosseri-era)

Adam Mosseri's public statements across 2024 and 2025 collapsed the algorithm story for carousels into four signals that drive distribution, ordered roughly by reach impact:

1. **Sends per reach** — the strongest reach signal. In Mosseri's framing, a send is the highest-cost, highest-trust action a viewer can take: they are spending social capital recommending the post to a specific person. The algorithm reads this as evidence the content is unmissable. (Industry benchmark — directional only: top-performing carousels in 2025 see send rates above 1% of reach.)
2. **Saves per reach** — the second-strongest signal. A save is a self-directed promise of return: the viewer is saying "I will need this later." This is why utility-shaped carousels (frameworks, checklists, reference grids) outperform pure-entertainment carousels on reach.
3. **Comments** — third. Comments still matter but are easier to game (controversy farming) and IG appears to discount them when they look gamed.
4. **Profile visits** — fourth. A profile visit signals the carousel earned enough trust that the viewer wanted to investigate the source. Strong covers and authoritative voice drive this.

Likes are not on this list. They are noise relative to the four above.

---

## 3. Cover slide stop-power

The cover is the only slide IG guarantees a feed view of. Score it 1 (weak) to 5 (exceptional) on five axes:

- **Contrast** — text legibility at thumbnail size. Squint test: can you still read the hook when the image is 80px tall in a feed scroll? WCAG AA on the headline-to-background pair is a hard floor; AAA is the target.
- **Hook density** — curiosity per word. A 7-word hook that opens a loop beats a 14-word hook that resolves it. Measure by asking: how many words could you cut without losing the reason to swipe?
- **Single focal element vs cluttered** — one dominant visual or typographic anchor. Multiple focal points at thumbnail size read as visual mush. Score 5 = one anchor; score 1 = three or more competing anchors.
- **Specificity** — numbers, named entities, concrete claims. "7 money rules" beats "money rules"; "the email that got me a $40k raise" beats "the email that worked." Specificity raises perceived utility.
- **Visual differentiation in feed** — would this stand out in a feed of 10 covers from the same niche? Color, layout, motif, type personality. Score 5 = instantly recognizable as this creator; score 1 = could be any account in the lane.

Sum the five for a 5–25 score. Map to `engagement_inferred.cover_stop_power`: 5–10 → `low`, 11–18 → `med`, 19–25 → `high`.

---

## 4. Slide-2 standalone test

Instagram's distribution loop retries posts: viewers who scrolled past slide 1 without engaging may be re-served the post starting on slide 2. This means slide 2 has to function as a hypothetical cover too. The skill must rate slide 2 against an abbreviated cover rubric (contrast, hook density, single focal, specificity).

**Pass criteria** for `engagement_inferred.slide_2_standalone: true`:

- Slide 2 introduces or restates the central tension or promise — not pure setup.
- Slide 2 is legible at thumbnail size (contrast and word count behave like a cover, not a body slide).
- Slide 2 makes sense to a viewer who never saw slide 1 (no dangling pronouns, no "as I said above").

**Fail criteria** → `slide_2_standalone: false`:

- Slide 2 is a wall of body text with no visual anchor.
- Slide 2 begins with a connective word or pronoun that requires slide 1 context ("So...", "These are the...", "Here's why...").
- Slide 2 is a transitional/divider slide with no standalone meaning.

---

## 5. Save-bait patterns

Slides shaped to earn saves share one trait: the viewer mentally tags the post as a future-reference object. The recurring patterns:

- **Framework / model / canvas** — a visual structure (2x2, pyramid, layered diagram) the viewer can return to for orientation.
- **Checklist / step-by-step** — numbered actions with reference utility ("the 9-step pre-launch checklist").
- **Comparison table** — A vs B with criteria; functions as a decision aid.
- **Stat summary / cheat sheet** — facts, numbers, conversions, formulas the viewer would otherwise google.
- **Resource list** — links, tools, books, accounts, prompts.

**Rule:** a carousel needs **at least one** save-bait slide to earn save rates above ~3% of reach (industry benchmark — directional only). Carousels that are pure narrative without a single reference-shaped slide rarely cross that threshold no matter how strong the writing.

Map to `engagement_inferred.save_bait`:

- `high` — two or more save-bait slides, including at least one in the back half of the deck.
- `med` — one save-bait slide.
- `low` — zero save-bait slides; the carousel is pure narrative or pure opinion.

---

## 6. Send-bait patterns

Sends come from identification: the viewer recognizes themselves or a specific friend in the slide and feels compelled to forward it. Recurring patterns:

- **Strongly relatable callouts** — slides framed as "send to a friend who [specific identity]" or "show this to anyone who [recognizable behavior]."
- **Tag-someone prompts** — explicit CTAs to tag a person, especially when paired with a relatable archetype.
- **Universally relevant truisms** — the Gen-Z meme of "this is so me." Lines so on-the-nose that forwarding them is a way of saying "this is us."
- **Tactical advice for a specific identity** — "if you're a junior PM, read this" / "if you freelance, you need this." The specificity gives the sender a clear recipient.

Map to `engagement_inferred.send_bait`:

- `high` — at least one slide built around an identity callout or universal truism, plus an explicit send/tag CTA.
- `med` — relatable framing exists but no explicit send/tag prompt.
- `low` — content is creator-centric or abstract; no clear "this is so them" trigger.

---

## 7. Swipe-momentum cues

What keeps a viewer moving from slide N to slide N+1:

- **Cliffhanger transitions** — slide N ends on a question, partial reveal, or unfinished thought; slide N+1 resolves it. The strongest carousels chain three or more cliffhangers.
- **Numbered structure** — "1 of 7," "2 of 7" creates completion pressure: the viewer wants to see all seven. Visible numbering in a header or footer amplifies this.
- **Story incompleteness** — beat B is shown before beat A is resolved (a "but first…" structure). The unresolved beat pulls the swipe.
- **Visual continuation** — panoramic compositions, seamless edges, or motifs that visibly continue across slide boundaries (a line that runs off the right edge and reappears on the next slide's left edge).

Map to `engagement_inferred.swipe_cliffhangers`:

- `high` — three or more of the four cues present, including at least one explicit cliffhanger transition.
- `med` — one or two cues present.
- `low` — slides feel independent; no momentum machinery.

---

## 8. Loopability

Does the final slide visually or narratively transition back to slide 1? Loop-creators (Brian Lovin's UI tutorial style is the canonical reference) get higher view-time signals because IG counts re-views of slide 1 after slide N as continued engagement, and viewers often do re-loop when the visual cue invites it.

**Loopable indicators:**

- Final slide's color, motif, or composition mirrors slide 1's.
- Final slide ends on a question or hook that slide 1 implicitly answers (or vice versa).
- Final slide contains a visible "back to start" cue — an arrow, a callback line, a re-statement of the opening claim.

Map to `engagement_inferred.loopable`: boolean. `true` only when at least one of the above is unmistakable; default `false`.

---

## 9. Slide count zone

Industry benchmark — directional only: Buffer's 2025 carousel benchmarks and Socialinsider's 2026 report converge on **7–10 slides** as the sweet spot for save rate and completion rate combined. Tutorial / how-to carousels can stretch to **12** without penalty when the steps genuinely require it. Below **5** slides, save rates collapse — the carousel doesn't feel "worth saving" relative to a single image. Above **12**, completion rate drops faster than reach gain compensates for.

Use this as a directional guardrail when populating `slide_count`-related observations in prose, not as a hard scoring rule. A 4-slide carousel can still be excellent; flag the count as a risk, not a verdict.

---

## 10. Per-slide read time

Industry benchmark — directional only: a healthy carousel averages **4–6 seconds dwell per slide**. Below that, viewers are skimming and probably bouncing; above it (especially above 10s on a single slide), the slide is likely overloaded.

Wall-of-text slides are the standard failure mode: 60+ words on a single slide pushes dwell past 10s and breaks rhythm, and most viewers swipe out before finishing. When `copy.word_counts_per_slide` shows any slide above ~50 words, flag it in the body prose as a dwell-time risk. Conversely, slides with fewer than ~5 words can read as filler if not visually carrying weight (a strong type/image moment can justify a 2-word slide; an empty divider cannot).

---

## 11. Performance tagging schema

When the user provides their own carousel **with metrics**, populate the `performance:` block per Schema A. All fields, units, and conventions:

| Field                  | Type / unit                                  | Notes                                                    |
| ---------------------- | -------------------------------------------- | -------------------------------------------------------- |
| `reach`                | integer                                      | unique accounts that saw the post                        |
| `saves`                | integer                                      | total saves                                              |
| `shares`               | integer                                      | total sends/shares (DMs + story re-shares combined)      |
| `comments`             | integer                                      | total comments                                           |
| `swipe_through_rate`   | float in [0, 1]                              | share of viewers who reached the final slide             |
| `completion_rate`      | float in [0, 1]                              | share who watched all slides (often equals swipe-through for static carousels) |
| `save_to_reach`        | float in [0, 1]                              | `saves / reach`                                          |
| `share_to_reach`       | float in [0, 1]                              | `shares / reach`                                         |
| `posted_at`            | ISO-8601 timestamp                           | `2026-05-07T14:32:00Z`                                   |
| `pillar`               | lowercase-hyphenated tag                     | content pillar, e.g. `"money-101"`, `"design-tutorials"` |

Every field is nullable individually. For third-party creators (no analytics access), the entire `performance:` block stays `null` per the schema. For own-account posts, populate as many fields as IG Insights exposes; null only the ones genuinely unavailable.

---

## 12. Engagement-correlation analysis

When the library has **≥10 entries** with `performance:` populated (own-account posts only — third-party entries have null performance and cannot contribute), the cross-synthesis pass can derive correlations between design choices and outcomes. The basic method:

1. **Group entries** by a single design choice. Examples: `typography.headline.family` serif vs sans-serif; `imagery.type` photo vs illustration vs none; `copy.hook_formula` numbered-list vs single-question vs controversial-claim.
2. **Compute the median** of the metric of interest (usually `save_to_reach` or `share_to_reach`) within each group.
3. **Compare medians across groups.**
4. **Apply two gates before reporting a finding:**
   - Each group must have **n ≥ 4** entries. Groups smaller than that are noise.
   - The relative difference in medians must be **≥ 30%**. Smaller deltas are within sampling noise for libraries this small.
5. **Always label findings as correlations from a small sample, not laws.** Phrase: "In our library of N entries, serif-headline carousels showed a median save-to-reach of X%, vs Y% for sans-headline. Sample is small; treat as a hypothesis to test, not a rule." Populate `engagement_correlations` (Schema B) and `engagement_findings` (Schema C) using this language.

When the gates aren't met, leave correlation fields `null` and say so explicitly in the prose body. Empty is honest; fabricated is not.

---

## 13. Anti-patterns

Design choices that consistently underperform across creators and niches. When you see these in a carousel, flag them in the body prose regardless of how the rest of the entry scores:

- **All-caps body text** — legibility tanks at thumbnail size; tracking and rhythm collapse. All-caps is fine on a one-line headline, never on body copy.
- **Cover with >12 words** — viewers don't read covers, they recognize them. Past ~12 words, the cover stops being legible at thumbnail and becomes a wall.
- **Yellow/black combo** — overused since 2022 finance/productivity boom; reads as "generic IG carousel" and is feed-blind to anyone in those niches.
- **Slides that require zooming** — small body text, dense data tables that need pinch-zoom. IG users do not zoom; they swipe past.
- **1–3 slide carousels** — viewers who hunt for save-worthy content skip these on sight; the carousel format is wasted on this length.
- **Stock-photo-only** — no original visual identity. The post reads as a content-mill output and gets no creator-recognition lift.

These are not absolute prohibitions — a deliberate creator can subvert any of them — but they are the default failure modes and should be called out by name when present.

---

## 14. Quick reference table

Every field in `engagement_inferred:` (per Schema A) and where its values are defined:

| Field                                  | Allowed values            | Defined in section                               |
| -------------------------------------- | ------------------------- | ------------------------------------------------ |
| `cover_stop_power`                     | `low` / `med` / `high`    | §3 Cover slide stop-power (5-axis rubric → band) |
| `slide_2_standalone`                   | `true` / `false`          | §4 Slide-2 standalone test                       |
| `save_bait`                            | `low` / `med` / `high`    | §5 Save-bait patterns                            |
| `send_bait`                            | `low` / `med` / `high`    | §6 Send-bait patterns                            |
| `swipe_cliffhangers`                   | `low` / `med` / `high`    | §7 Swipe-momentum cues                           |
| `loopable`                             | `true` / `false`          | §8 Loopability                                   |

Adjacent observations the prose body should address (not in `engagement_inferred:` directly, but supporting it):

| Concern                | Where to reason about it |
| ---------------------- | ------------------------ |
| Slide count fit        | §9 Slide count zone      |
| Per-slide dwell risk   | §10 Per-slide read time  |
| Anti-pattern flags     | §13 Anti-patterns        |

When `performance:` is populated, the cross-synthesis correlation pass uses the method in §12.
