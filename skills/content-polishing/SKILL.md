---
name: content-polishing
description: Use when a draft exists and needs factual, structural, and editorial review before final humanizing or platform repurposing
---

# Content Polishing

## Overview

This skill performs editorial review on an existing draft.
Its job is to make the piece correct, coherent, and fit for the target platform before any humanizing pass.

## Workflow

Run these passes in order.

### 1. Factual and structural review

Check:
- factual consistency
- source alignment
- missing evidence
- contradictory statements
- weak ordering
- repetitive sections
- missing transitions that harm comprehension
- whether the main subject appears early enough for the platform and title promise
- whether any interpretation is phrased too much like sourced fact

### 2. Editorial review

Check:
- paragraph clarity
- sentence burden
- information density
- tone consistency
- whether examples earn their space
- whether the ending matches the argument

### 3. Platform fit review

For WeChat:
- readable paragraph rhythm
- enough narrative momentum

For SEO:
- heading hierarchy intact
- scannability preserved
- CTA and search intent still aligned

For Xiaohongshu adaptation drafts:
- spoken cadence
- stronger hook potential
- shorter unit length

### 4. Save review notes

Write findings to:
- `polish/review-notes.md`

Use the template at:
- `assets/templates/review-notes-template.md`

## Output Format

The review notes should be actionable and concise:
- major issues
- smaller edits
- unresolved questions
- recommended next step

## Guardrails

- Do not rewrite into a new angle here.
- Do not humanize before structural issues are fixed.
- Do not remove SEO-critical structure during review.
- Do not skip writing `polish/review-notes.md` even if fixes are discussed inline elsewhere.

## Checklist

- [ ] Facts reviewed
- [ ] Structure reviewed
- [ ] Editorial quality reviewed
- [ ] Platform fit reviewed
- [ ] Review notes saved
