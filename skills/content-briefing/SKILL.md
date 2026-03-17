---
name: content-briefing
description: Use when a writing request is vague, underspecified, or spread across messages and needs to be turned into a usable brief before drafting
---

# Content Briefing

## Overview

This skill turns a loose writing request into a brief that downstream writing skills can use reliably.

## When to Use

Use this skill when:
- the topic is clear but the scope is not
- the user gave goals without audience details
- the user wants bilingual or multi-platform output but has not specified priorities
- the user wants an article, but the title, keyword, or CTA is still fuzzy

Do not use this skill when a complete and consistent brief already exists.

## Required Fields

Capture these fields:
- project name
- content type
- language mode
- target audience
- primary goal
- topic or working title
- target length
- desired tone
- whether research is required
- whether images are required
- whether repurposing is required

Useful optional fields:
- keywords
- forbidden claims or phrases
- desired CTA
- examples of good reference pieces

## Workflow

### 1. Check for an existing brief

Look for:
- `brief/brief.md`
- `brief/requirements.md`
- `meta/project.json`

If they already exist and are complete, reuse them instead of rewriting.

### 2. Fill gaps

If key fields are missing, extract them from the user's request or ask concise follow-up questions only for the missing essentials.

### 3. Normalize the brief

Write a brief that separates:
- objective
- audience
- deliverables
- constraints
- open risks

Use the template at:
- `assets/templates/brief-template.md`

### 4. Save outputs

Write:
- `brief/brief.md`
- `brief/requirements.md`
- `meta/project.json`

## Brief Format

`brief/brief.md` should include:
- project summary
- target audience
- content goal
- primary deliverables
- language mode
- platforms
- tone notes
- source expectations
- image needs
- repurposing needs

`brief/requirements.md` should include:
- must-have items
- nice-to-have items
- constraints
- blocked assumptions

`meta/project.json` should include machine-friendly fields mirroring the brief.

## Guardrails

- Do not begin full drafting here.
- Do not invent business goals, product claims, or target readers without marking them as assumptions.
- Do not overwrite a stronger existing brief with a weaker summary.

## Checklist

- [ ] Existing brief checked
- [ ] Missing essentials filled
- [ ] Brief normalized
- [ ] Requirements split from summary
- [ ] Structured metadata saved
