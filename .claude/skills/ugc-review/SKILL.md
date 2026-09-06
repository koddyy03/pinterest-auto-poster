---
name: ugc-review
description: >
  Analyze performance of UGC videos/ads, identify winning hooks and angles, kill
  losers, and generate the next iteration of creative. Use when the user pastes
  ad metrics (views, CTR, ROAS, CPA, watch-through), asks "which hooks won",
  "what should I test next", "review last week's batch", or wants to close the
  daily test-and-iterate loop. Reads ugc-batch output + performance data;
  feeds new directives back into ugc-hooks / ugc-batch.
---

# UGC Performance Review & Iteration

The engine only compounds if you feed results back in. Most brands treat AI
creative as a one-time experiment and quit after two ads — the winners only
emerge after weeks of daily testing. This skill closes the loop: read the data,
find what's working, kill what isn't, and write the next batch's directive.

## Inputs

- The **batch index** (`ugc-batches/<date>-<offer>/index.csv`) so findings tie
  back to specific hooks/angles/personas.
- **Performance data** — however the user has it: pasted table, CSV export, or
  screenshot. Key metrics, by platform:
  - **Top of funnel:** 3s view rate / hook rate, watch-through %.
  - **Engagement:** CTR, saves/shares.
  - **Revenue:** ROAS, CPA / cost-per-purchase, conversion rate.
- The **goal metric** (what we're optimizing — usually CPA or ROAS).

## Procedure

1. **Join data to the index** by `id`. Flag any scripts with no data (not yet
   live / not enough spend).
2. **Score each creative** against the goal metric, but read the funnel:
   - Low **hook rate** → the *hook* failed (first 1–2s). Fix the opener.
   - Good hook rate but low **CTR/ROAS** → hook worked, *body/offer/CTA* failed.
   - Use a minimum-spend / minimum-impressions threshold before judging — don't
     kill on noise.
3. **Cluster by angle and by persona** to find patterns, not just single
   winners. "Skeptic-to-convert hooks beat bold-claim 3:1" is more actionable
   than one lucky video.
4. **Classify each creative:** `winner` | `keep testing` | `kill`. Update the
   `status` column in `index.csv`.
5. **Write the review** to `ugc-reviews/<date>-<offer>.md` with:
   - Headline result (e.g. "CPA down 40% vs prior batch").
   - Winning angles/hooks and *why* you think they won.
   - Losing patterns to stop making.
   - Concrete **next-batch directive**.
6. **Generate the next iteration directive** for `ugc-batch`:
   - **Clone winners** into fresh variations (same angle, new hooks/openers) —
     this is the highest-ROI move.
   - **Double down** on winning angles in the angle mix.
   - **Drop** dead angles.
   - Propose 2–3 **new angles** to keep exploration alive (avoid overfitting to
     past winners).

## Iteration principles

- **Hook strength and volume win** — most improvement comes from better hooks on
  proven angles, delivered at volume.
- **Don't over-rotate on one winner.** Clone it *and* keep ~20–30% of the next
  batch on new exploration.
- **Warm-up matters.** New ad accounts / content styles need time; don't kill a
  whole angle on day one.
- **Compounding is the point.** Track the goal metric batch-over-batch so the
  user can see the engine improving, not just a single day's numbers.

See `references/review-template.md` for the review file structure.
