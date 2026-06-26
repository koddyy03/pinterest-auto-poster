---
name: ugc-engine
description: >
  Orchestrate an end-to-end AI UGC content engine for an e-commerce brand —
  produce large daily batches of short-form, creator-style video scripts ready
  to render in a tool like Arcads. Use when the user wants to "spin up a UGC
  engine", "make a batch of UGC ad scripts", "scale creative for an offer",
  "test hooks at volume", or run a daily content operation for an Amazon /
  TikTok Shop / DTC product. This is the entry point that ties together the
  ugc-persona, ugc-hooks, ugc-scripts, ugc-batch, and ugc-review skills.
---

# AI UGC E-commerce Engine

The goal of this engine is simple and is the whole thesis: most brands don't
have a marketing problem, they have a **volume + hook** problem. The platforms
(TikTok, Reels, Shorts) reward two things above everything else — **hook
strength** and **volume of fresh creative**. This engine lets one operator ship
that volume by using Claude as the brain (writes and organizes scripts at scale)
and a video studio like Arcads as the hands (turns each script into a
real-feeling creator video).

## The operating principles (do not violate these)

1. **Hook first.** The first 1–2 seconds decide everything. Every script is
   built around its hook, not the other way around.
2. **One consistent character per page.** An "authority figure" / creator
   persona is kept identical across every video so the account builds trust and
   recognition. See `ugc-persona`.
3. **Volume + daily cadence.** Ship fresh creative every single day. Two ads and
   quitting tells you nothing. The winners only compound after weeks.
4. **Test angles and offers daily.** Same offer, many hooks → let the algorithm
   pick winners. Rotate angles deliberately. See `ugc-hooks`.
5. **Review and double down.** Feed performance back in, kill losers, clone
   winners into new variations. See `ugc-review`.

## When to use which sub-skill

| You want to…                                            | Use skill      |
|---------------------------------------------------------|----------------|
| Define the brand's creator persona / authority figure   | `ugc-persona`  |
| Generate many hooks for one offer across angles         | `ugc-hooks`    |
| Turn hooks into full, render-ready UGC video scripts    | `ugc-scripts`  |
| Produce a large daily batch and organize the output     | `ugc-batch`    |
| Analyze performance and generate the next iteration     | `ugc-review`   |

## Standard workflow (a full engine run)

Follow this sequence. Each step names the sub-skill that does the heavy lifting.

1. **Intake the brand + offer.** Ask the user (or read from a brief file) for:
   product name, what it does, the core offer/CTA, target platform (Amazon /
   TikTok Shop / DTC site), audience, and any proof points (reviews, results,
   ingredients, guarantees). Capture this in `brand-brief.md` at the repo root
   or the path the user gives you.
2. **Lock the persona** with `ugc-persona` → produces `personas/<name>.md`.
   Reuse the same persona across the whole batch.
3. **Generate hooks** with `ugc-hooks` → a wide hook bank across multiple
   proven angles for the offer.
4. **Write scripts** with `ugc-scripts` → expand each chosen hook into a full
   spoken UGC script with on-screen text and shot notes.
5. **Batch + organize** with `ugc-batch` → produce N scripts in one run, named
   and indexed so they map cleanly to render jobs and back to performance data.
6. **Render** in the video studio (Arcads or similar). This step is outside
   Claude — hand off the batch folder. Note in the index which persona/voice to
   use so renders stay consistent.
7. **Review + iterate** with `ugc-review` after data comes back → kill losers,
   clone winners, re-enter at step 3 with the learnings.

## Output conventions

Keep everything as plain Markdown / CSV so it is git-trackable and diffable:

```
brand-brief.md
personas/
  <persona-name>.md
ugc-batches/
  <YYYY-MM-DD>-<offer-slug>/
    index.csv            # one row per script: id, hook, angle, persona, status
    001-<hook-slug>.md
    002-<hook-slug>.md
    ...
ugc-reviews/
  <YYYY-MM-DD>-<offer-slug>.md
```

Never hardcode brand specifics into the skill files — always read them from the
brief and persona so the engine works for any brand.

## Scaling note

Noah's reference number is ~550 videos/day at ~$0.50–$1/video. Claude's job is
only the **writing and organizing** half — generating and structuring hundreds
of distinct, on-persona scripts. Actual render volume/cost lives in the video
studio. When a user asks for "550 a day", that means produce the *scripts and
index* for that volume (see `ugc-batch` for how to fan out efficiently), not
that Claude renders video.
