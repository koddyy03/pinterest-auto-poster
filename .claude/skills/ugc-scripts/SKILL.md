---
name: ugc-scripts
description: >
  Expand a hook into a full, render-ready short-form UGC video script — spoken
  lines, on-screen text, and shot/B-roll notes — in a locked persona's voice,
  sized for a tool like Arcads. Use when the user wants to "write a UGC script",
  "turn this hook into a full ad", "script a 30-second video", or needs
  production-ready creative from hooks. Consumes ugc-hooks output; used by
  ugc-batch to produce volume.
---

# UGC Script Writer

Turns a single hook into a complete, render-ready script. The output is built to
drop straight into a UGC video studio (Arcads or similar): clean spoken lines for
the avatar to deliver, on-screen text, and lightweight shot notes.

## Inputs

- **Hook + angle** (from `ugc-hooks`, or written here on the fly).
- **Persona** from `personas/<slug>.md` — the script must sound exactly like
  them (POV, energy, tics, hard rules).
- **Offer + proof points** from `brand-brief.md` — the claim ceiling.
- **Target length** (default 30s; also support 15s and 45s).
- **CTA / destination** (Amazon listing, TikTok Shop, DTC link).

## Script structure (the proven UGC arc)

Write every script in these beats. Keep total spoken word count to ~2.2
words/second of target length (≈66 words for 30s).

1. **Hook (0–2s)** — the chosen opener, delivered in-character. Never lead with
   the brand name.
2. **Problem / relatability (2–8s)** — name the viewer's pain so they feel seen.
3. **Turn (8–14s)** — "so I tried…" / the discovery moment. Introduce the
   product naturally, as the persona would.
4. **Value / proof (14–24s)** — 1–3 concrete benefits or proof points. Specific,
   not salesy. Stay within the brief's claim ceiling.
5. **Soft objection handle (optional)** — one honest caveat or "I was skeptical
   because…" — imperfection builds trust.
6. **CTA (last 3–5s)** — clear, low-friction next step to the destination.

## Output format (one file per script)

Produce Markdown using `references/script-template.md`. It must contain:

- Frontmatter-style header: `id`, `hook`, `angle`, `persona`, `length`, `cta`.
- **Spoken script** — clean prose lines, no stage directions inline (the studio
  reads these aloud verbatim).
- **On-screen text** — timed captions/overlays.
- **Shot notes** — optional B-roll / setting cues for the editor.

Keep spoken lines and on-screen text in **separate blocks** — mixing them breaks
the render handoff.

## Quality rules

- It must sound spoken, not written. Read it out loud in your head — contractions,
  short sentences, natural rhythm.
- Respect the persona's hard rules (`Always` / `Never`).
- One idea per script. Don't cram multiple angles in — that's what volume is for.
- No claim beyond the brief's proof points. If tempted, soften to opinion
  ("for me…", "in my experience…").
- End with exactly one CTA.

See `references/script-template.md` for the exact output structure.
