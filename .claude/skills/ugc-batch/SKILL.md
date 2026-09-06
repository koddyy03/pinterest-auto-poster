---
name: ugc-batch
description: >
  Produce a large daily batch of UGC video scripts in one run and organize them
  into a clean, indexed folder that maps to render jobs and back to performance
  data. Use when the user wants "a batch of N scripts", "today's content drop",
  "scale this to 50/100/550 a day", "produce a content calendar of videos", or
  to run the daily engine. Fans out ugc-hooks + ugc-scripts across one offer and
  persona; output is consumed by ugc-review.
---

# UGC Batch Production Engine

This is the daily workhorse: take one offer + one persona and produce many
distinct, on-persona scripts in a single organized drop. The whole thesis is
**volume + daily cadence** — ship fresh creative every day so winners can
compound. This skill makes that repeatable and traceable.

## Inputs

- **Offer** (`brand-brief.md`) and **persona** (`personas/<slug>.md`).
- **Batch size** N (e.g. 30, 50, 100). For very large targets see "Scaling".
- **Date** (default today) and an **offer slug** for folder naming.

## Procedure

1. **Resolve inputs.** Confirm offer, persona, N, and date. If brief or persona
   are missing, run `ugc-persona` first.
2. **Generate the hook bank** with `ugc-hooks` — produce at least N hooks spread
   across all angle families. Over-generate ~20% so you can drop weak ones.
3. **Select N hooks**, keeping the spread across angles balanced (don't let one
   angle dominate the batch — you're testing angles, not just lines).
4. **Expand each hook** into a full script with `ugc-scripts`. Vary length across
   the batch (e.g. mostly 30s, some 15s).
5. **Write the batch folder:**
   ```
   ugc-batches/<YYYY-MM-DD>-<offer-slug>/
     index.csv
     001-<hook-slug>.md
     002-<hook-slug>.md
     ...
   ```
6. **Write `index.csv`** — one row per script, the spine that connects scripts →
   renders → performance:
   ```
   id,file,angle,hook,persona,length,cta,status
   001,001-crash-at-3pm.md,problem,"If you crash every afternoon...",skeptical-sarah,30s,"Shop on TikTok",draft
   ```
7. **Summarize the drop** back to the user: count, angle distribution, persona,
   and the folder path. Note the render handoff (which avatar/voice ID to use).

## Scaling to large daily volume

For big targets (Noah's reference is ~550/day), don't write 550 files in one
serial pass — fan out:

- **Split by angle and/or sub-offer** into chunks of ~25–50 scripts.
- If the `Workflow` / `Agent` tooling is available and the user has opted into
  multi-agent runs, dispatch one agent per chunk (same persona + brief, distinct
  angle slice), then merge their `index.csv` rows and renumber ids sequentially.
- Otherwise produce in serial chunks and append to the same `index.csv`.
- **Always log the real count produced.** If you cap below the requested N, say
  so explicitly — never imply full coverage you didn't deliver.

## Organization rules (so review actually works later)

- `id` is stable and never reused. New variations get new ids.
- `status` lifecycle: `draft → rendered → live → (winner | killed)`.
- Keep one batch = one date = one offer. Don't mix offers in a folder.
- File names are `<id>-<hook-slug>.md` so they sort and grep cleanly.

The clean index is what makes `ugc-review` able to tie performance numbers back
to specific hooks and angles, closing the loop.
