---
name: content-research
description: Use when a writing project includes time-sensitive facts, product claims, industry comparisons, pricing, release details, or evidence that should be researched and sourced before drafting
---

# Content Research

## Overview

This skill gathers and saves research for writing projects that need current facts, evidence, or source-backed claims.
It supports two modes:
- `foundation`
- `outline-targeted`

## When to Use

Use this skill when the draft depends on:
- current products or features
- pricing or plan details
- release timelines
- industry trends
- market comparisons
- SEO guidance
- community reactions
- real examples that need sources

Skip this skill for purely personal essays or timeless opinion pieces that do not need fresh evidence.

## Modes

### `foundation`

Use before drafting when you need to establish:
- factual boundaries
- concept boundaries
- chronology
- what is safe to state as fact
- what should remain author interpretation

### `outline-targeted`

Use after the outline is approved when you need to:
- support specific sections
- tighten product or trend comparisons
- map strong judgments to evidence
- identify which lines require softer wording

## Workflow

### 1. Confirm the research topic

Define:
- the exact topic
- what needs verification
- the publication date sensitivity
- which claims are facts vs interpretations vs opinions
- whether this run is `foundation` or `outline-targeted`

### 2. Gather sources

Prioritize:
- official docs or official product pages
- primary announcements
- reputable reporting
- high-signal community discussion

### 3. Separate fact from interpretation

For each major point, label:
- fact
- interpretation
- opinion
- open question

Also note:
- safe factual wording
- risky wording to avoid
- where the author is using a personal analytical framework

### 4. Save the findings

Write:
- `research/research-YYYY-MM-DD.md`
- `research/sources.md`

If the run is `outline-targeted`, save the main note as:
- `research/research-outline-YYYY-MM-DD.md`

Use the template at:
- `assets/templates/research-template.md`

The research note must include:
- research date
- source links
- summary of relevant findings
- freshness notes
- recommendations for rechecking later

## Output Format

`research/research-YYYY-MM-DD.md` should include:
- mode
- topic
- what was investigated
- key findings
- fact / interpretation split
- unresolved items
- freshness risk

For `outline-targeted` runs, also include:
- section-to-source mapping
- claims that require hedged wording
- claims that should remain explicit author judgment

`research/sources.md` should list:
- source name
- link
- publication date if known
- why it matters

## Guardrails

- Do not fabricate or round up evidence.
- Do not merge opinion and fact into one statement.
- Do not collapse author framing into sourced fact.
- Do not use unsourced numbers as if verified.
- Flag stale or uncertain claims explicitly.

## Checklist

- [ ] Topic and claims clarified
- [ ] Research mode selected
- [ ] Sources gathered
- [ ] Facts separated from interpretation
- [ ] Safe wording and risky wording noted
- [ ] Freshness risk noted
- [ ] Research files saved
