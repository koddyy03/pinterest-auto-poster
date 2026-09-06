---
name: ugc-persona
description: >
  Define and lock a consistent "authority figure" / creator persona for an
  e-commerce brand's UGC content, so the same believable character appears
  across every video. Use when the user wants to "create an AI creator", "build
  a brand spokesperson / authority figure", "define the avatar", or needs a
  reusable persona spec before generating hooks or scripts. Produces a single
  reusable persona file consumed by ugc-hooks, ugc-scripts, and ugc-batch.
---

# UGC Persona / Authority Figure Builder

The hardest part of an AI UGC engine is not making content — it's building a
**believable character that stays consistent**. Creator-style accounts win when
the same avatar shows up across all videos: viewers learn the face, the voice,
and the energy, and that recognition becomes trust, and trust drives revenue.

This skill produces one reusable persona spec. Lock it once per page/brand and
reuse it for the entire content engine.

## How to build a persona

1. **Read the brand brief** (`brand-brief.md` or the path given). If it's
   missing, ask the user for: product, audience, platform, and tone.
2. **Pick an archetype that fits the niche and the buyer's trust triggers.**
   Common high-trust archetypes:
   - *The expert* (dermatologist-type, nutritionist-type, "I've tested 50 of
     these") — authority through credentials/experience.
   - *The relatable peer* ("girl next door", "regular guy") — authority through
     sameness and honesty.
   - *The convert* ("I was skeptical, then…") — authority through transformation.
   - *The founder* — authority through mission and behind-the-scenes access.
   - *The enthusiast / obsessive* ("I'm obsessed with X") — authority through
     passion and depth.
3. **Fill in every field of the persona template** (see
   `references/persona-template.md`). Be specific and concrete — vague personas
   produce inconsistent scripts.
4. **Write it to** `personas/<persona-name>.md`. Use a short kebab-case slug for
   the filename (e.g. `personas/skeptical-sarah.md`).

## Consistency rules (these are what make it work)

- **One persona per page/account.** Don't mix archetypes on the same page.
- **Lock voice + look notes** so the video studio (Arcads) renders the same
  avatar and voice every time. Record the exact avatar/voice ID if known.
- **Catchphrases and verbal tics** stay constant — they're recognition anchors.
- **The persona's POV is fixed** (e.g. always first-person, always casual).
  ugc-scripts must respect this.

## Output

A complete `personas/<slug>.md` following the template. Confirm back to the user
the persona name, archetype, and the one-line "who they are" so they can approve
before the engine scales on it.

See `references/persona-template.md` for the exact structure to produce.
