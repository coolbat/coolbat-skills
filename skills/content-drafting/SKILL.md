---
name: content-drafting
description: Use when a writing project has a usable brief and any required research, and needs candidate angles, outlines, or full draft generation for WeChat, SEO, or bilingual content
---

# Content Drafting

## Overview

This skill turns a validated brief into candidate directions, outlines, and drafts.
It should not skip directly from vague request to full article.

## Inputs

Required:
- usable brief

Optional but recommended:
- research notes
- style notes
- source materials
- target keywords

## Workflow

### 1. Inspect the brief

Confirm:
- audience
- goal
- language mode
- platform
- primary subject
- target length
- whether the project is opinion-led, evidence-led, or tutorial-led

### 2. Propose directions first

Generate 2-4 candidate directions.

Each direction should include:
- working title
- core angle
- target reader
- outline
- estimated effort
- platform fit
- opening approach
- whether the primary subject appears immediately or is intentionally delayed

Use the template at:
- `assets/templates/angle-options-template.md`

Do not draft the full article until a direction is chosen.

### 3. Build the outline

Once a direction is selected, create a detailed outline.

Use the template at:
- `assets/templates/outline-template.md`

For SEO drafts:
- preserve clear heading hierarchy
- map major keyword themes naturally
- make the structure scannable

For WeChat drafts:
- favor momentum, viewpoint, and readable sections
- allow stronger narrative movement
- surface the article's main object early when the user expects topic-led writing
- if the article is about a product, event, or controversy, do not spend a long opening before naming it unless the delayed setup is intentional and justified

### 4. Draft by language mode

For Chinese:
- keep the prose direct and readable
- avoid official-copy tone

For English:
- write naturally for English readers
- do not mirror Chinese syntax

For bilingual:
- use the same brief and research
- produce separate drafts rather than literal translation

Before drafting, run a focus check:
- Is the article clearly about the promised subject?
- Does the opening enter the subject fast enough for the platform?
- Are strong judgments marked as author framing where needed?

Use the template at:
- `assets/templates/draft-template.md`

### 5. Save outputs

Common outputs:
- `drafting/outline-zh.md`
- `drafting/outline-en.md`
- `drafting/draft-zh.md`
- `drafting/draft-en.md`

Create only the files relevant to the current language mode.

## Guardrails

- Do not skip the direction proposal stage unless the user explicitly chooses a direction first.
- Do not bury the article's named subject too deep into the opening when platform expectations favor earlier framing.
- Do not invent sourced facts not present in the brief or research.
- Do not collapse bilingual output into sentence-by-sentence translation.

## Checklist

- [ ] Brief validated
- [ ] Directions proposed
- [ ] Direction selected
- [ ] Outline created
- [ ] Opening focus checked
- [ ] Draft saved to the correct file
