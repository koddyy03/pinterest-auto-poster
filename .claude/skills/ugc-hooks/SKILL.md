---
name: ugc-hooks
description: >
  Generate a large bank of short-form video hooks (the first 1–2 seconds) for
  one e-commerce offer, spread deliberately across proven angles, in the voice
  of a locked persona. Use when the user wants to "write hooks", "test hooks at
  volume", "give me 30 opening lines", "brainstorm angles for this product/ad",
  or needs hook variety before writing full scripts. Output feeds ugc-scripts.
---

# UGC Hook Generator

The hook is the single highest-leverage part of a short-form video — the first
1–2 seconds decide whether anyone watches. The winning play is **one offer,
many hooks**: generate lots of distinct openers across different angles, then let
the algorithm pick winners. This skill produces that hook bank.

## Inputs

- The **offer** (product + the specific promise/CTA). Read from `brand-brief.md`
  or ask.
- The **persona** to write in. Read from `personas/<slug>.md` (use `ugc-persona`
  first if none exists). Every hook must sound like that persona.
- **How many** hooks and across which angles (default: 30 hooks spread across
  all angle families below).

## Angle families (spread hooks across these — don't cluster on one)

Generate hooks across a deliberate mix so you're testing *angles*, not just
wording:

1. **Problem/pain call-out** — "If your X keeps doing Y, stop scrolling."
2. **Curiosity / pattern interrupt** — "Nobody talks about why this actually…"
3. **Bold claim / result** — "This replaced 3 products in my routine."
4. **Myth-bust / contrarian** — "Everything you've heard about X is wrong."
5. **Us vs them / comparison** — "X vs Y — I tested both for 30 days."
6. **Social proof / trend** — "Why is everyone suddenly buying…"
7. **Skeptic-to-convert** — "I did NOT think this would work."
8. **Question hook** — "Why does no one tell you that…"
9. **Demonstration tease** — "Watch what happens when I…"
10. **Authority / credentials** — "As someone who's tried 40 of these…"

## How to generate

1. Confirm offer + persona + count + any specific angle weighting.
2. For each angle family, write the requested share of hooks. Each hook is:
   - **≤ 12 words / ~1.5 seconds spoken.**
   - In the **persona's voice** (use their tics/energy).
   - **Specific**, not generic — reference the real product/benefit/pain.
   - A genuine *opener* — it should make the next line inevitable.
3. **Deduplicate by idea, not just wording.** Two hooks that test the same
   psychological angle count as one test; push for variety.
4. Output as a table (or CSV when feeding `ugc-batch`):

   | id | angle | hook | on-screen text |
   |----|-------|------|----------------|

   `on-screen text` is the short caption shown over the first frame (often a
   punchier version of the spoken hook).

## Quality bar

- A hook that could open *any* product's ad is too generic — rewrite it.
- Avoid corporate phrasing; sound like a real person mid-thought.
- It's fine for some hooks to be slightly polarizing — polarizing > forgettable.
- Flag any hook that makes a claim the brand can't back (the brief's proof
  points are the ceiling for claims).

See `references/hook-angles.md` for worked examples per angle.
