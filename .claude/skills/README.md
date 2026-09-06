# AI UGC E-commerce Engine — Skill Set

A set of Claude Code skills that turn Claude into the **brain** of an AI UGC
content engine for e-commerce brands: it writes and organizes short-form,
creator-style video scripts at volume, ready to render in a video studio like
[Arcads](https://www.arcads.ai). The thesis: most brands don't have a marketing
problem — they have a **hook + volume** problem. Ship lots of strong-hook,
on-persona creative every day and let the algorithm find the winners.

## The skills

| Skill          | Does                                                                 |
|----------------|---------------------------------------------------------------------|
| `ugc-engine`   | Orchestrator / entry point. Ties the others into one workflow.       |
| `ugc-persona`  | Builds a consistent "authority figure" creator persona, reused everywhere. |
| `ugc-hooks`    | Generates a bank of hooks for one offer, spread across proven angles. |
| `ugc-scripts`  | Expands a hook into a full, render-ready UGC script.                  |
| `ugc-batch`    | Produces a large daily batch and organizes it into an indexed folder. |
| `ugc-review`   | Reads performance data, finds winners, writes the next iteration.    |

## How to use

Just ask Claude in natural language and the matching skill activates, e.g.:

- "Spin up a UGC engine for my matcha brand" → `ugc-engine`
- "Create an authority-figure persona for this product" → `ugc-persona`
- "Give me 40 hooks for this offer across angles" → `ugc-hooks`
- "Turn these hooks into 30-second scripts" → `ugc-scripts`
- "Make today's batch of 50 scripts" → `ugc-batch`
- "Here are last week's ad metrics — what won?" → `ugc-review`

## The loop

```
brand-brief.md ─┐
                ├─> ugc-persona ─> ugc-hooks ─> ugc-scripts ─> ugc-batch ─> [render in Arcads]
                │                       ▲                                         │
                └──────────── ugc-review ◄──────────────── performance data ◄─────┘
```

Start from `ugc-engine` for the full standard workflow and output conventions.
Templates for the brief, persona, scripts, and reviews live in each skill's
`references/` folder.
