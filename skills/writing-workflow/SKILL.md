---
name: writing-workflow
description: Use when handling long-form writing projects for WeChat articles, SEO blogs, bilingual content, or downstream repurposing into WeChat and Xiaohongshu formats
---

# Writing Workflow

## Overview

This skill is the router for structured writing projects.
It classifies the job, checks required inputs, routes work through the right sub-skills, and keeps the project artifacts organized.

For a concrete end-to-end example of this workflow, see:
- `references/case-study.md`

For why the workflow was tightened over time, see:
- `references/evolution-note-2026-03.md`

Supported scenarios:
- WeChat long-form
- SEO blog
- WeChat adaptation
- Xiaohongshu adaptation
- Existing article revision
- Humanizing only

## Project Structure

Store each project under:

```text
content-projects/{project-slug}/
```

Expected subdirectories:

```text
brief/
research/
drafting/
polish/
assets/
distribution/
meta/
```

If the project folder does not exist, create it before continuing.

## Classification

Classify the request before drafting anything.

### Content Scenario
- WeChat long-form
- SEO blog
- WeChat adaptation
- Xiaohongshu adaptation
- Existing article revision
- Humanizing only

### Task Shape
- New project with full brief
- New project with incomplete brief
- Draft from source materials
- Revise existing draft
- Repurpose final article
- Produce bilingual versions

Do not skip classification.

## Language Rules

Supported modes:
- Chinese only
- English only
- Bilingual

For bilingual work:
- use the same brief and research base
- produce separate audience-appropriate drafts
- do not default to sentence-by-sentence translation

## Workflow

### 1. Standardize the brief

If the request is incomplete, use `content-briefing`.

Minimum fields:
- project name
- content type
- language mode
- target audience
- content goal
- topic or working title
- primary subject or main object of discussion
- target length
- whether research is required
- whether images are required
- whether repurposing is required

### 2. Assess research risk before drafting

Set two risk flags:
- `timeliness_risk`: `low`, `medium`, or `high`
- `controversy_risk`: `low`, `medium`, or `high`

Mark `timeliness_risk` as `medium` or `high` if the draft includes any of:
- specific products, companies, models, platforms, prices, features, or release dates
- recent timing language such as "recent", "current", "this year", "right now", "next phase", or "latest"
- trend or market claims
- SEO guidance that may have changed

Mark `controversy_risk` as `medium` or `high` if the draft includes any of:
- category definitions still in flux
- product comparisons
- directional industry judgments
- claims about what represents the future of a category
- statements likely to be challenged by informed readers

If either risk is `medium` or `high`, run `content-research` in `foundation` mode before drafting.

### 3. Run foundation research when needed

Use `content-research` in `foundation` mode to establish:
- factual boundaries
- concept boundaries
- source-backed chronology
- which statements can be written as facts
- which statements must remain author interpretation

Foundation research output must include:
- research date
- source links
- fact vs interpretation vs opinion separation
- freshness or risk notes

### 4. Propose directions first

Use `content-drafting` to generate 2-4 candidate directions before full drafting.

Each option should include:
- working title
- target reader
- core angle
- outline
- expected effort
- platform fit
- how early the primary subject appears

Wait for direction selection before writing the full draft.

### 5. Run outline-targeted research when needed

After the outline is approved, run `content-research` again in `outline-targeted` mode if the article includes:
- product or trend judgments tied to specific sections
- comparisons that need tighter evidence
- strong claims about what changed, what matters, or what a product represents

Use this second pass to map:
- section -> supporting sources
- fact statements -> safe wording
- interpretation statements -> author framing
- claims requiring explicit uncertainty

### 6. Draft the article

After a direction is selected, use `content-drafting` to create the draft.

Scenario emphasis:
- WeChat: clarity, viewpoint, narrative energy, readability
- SEO blog: search intent, heading structure, keyword safety, scannability
- English: write naturally for English readers
- Bilingual: create parallel drafts from the same brief

### 7. Polish the draft

Use `content-polishing` for factual, structural, and editorial review.

### 8. Humanize the draft

Use `content-humanizing` after polishing, not before.

Preserve:
- factual claims
- source-backed details
- SEO structure where required
- the core argument

### 9. Repurpose for distribution

If requested, use `content-repurpose` to create:
- WeChat article version
- SEO blog version
- Xiaohongshu version

### 10. Optional image briefs

If the article needs illustrations, screenshots, or diagrams, use `image-brief-generator`.
Save image briefs under:

```text
assets/image-briefs/
```

## Guardrails

- Do not jump straight into a full article when the brief is unclear.
- Do not bury the primary subject too late in the article. If the piece is about a specific product, event, or controversy, surface it in the opening unless the user explicitly wants a delayed reveal.
- Do not fabricate facts, numbers, quotes, or test results.
- Do not present author interpretation as broad public consensus unless sourced.
- Do not treat humanizing as permission to change meaning.
- Do not destroy SEO structure merely to sound less like AI.
- Do not overwrite prior project files without checking the existing directory.

## Deliverables

Depending on scope, produce some or all of:
- `brief/brief.md`
- `research/research-YYYY-MM-DD.md`
- `research/research-outline-YYYY-MM-DD.md`
- `drafting/draft-zh.md`
- `drafting/draft-en.md`
- `polish/review-notes.md`
- `polish/humanized-zh.md`
- `polish/humanized-en.md`
- `distribution/wechat-article.md`
- `distribution/seo-blog-zh.md`
- `distribution/seo-blog-en.md`
- `distribution/xiaohongshu-post.md`

## Checklist

- [ ] Project classified
- [ ] Brief exists and is usable
- [ ] Research risk assessed
- [ ] Foundation research completed if needed
- [ ] Direction selected before full drafting
- [ ] Outline-targeted research completed if needed
- [ ] Draft reviewed for facts and structure
- [ ] Humanizing applied at the correct stage
- [ ] Distribution outputs created if requested
- [ ] Files saved in the correct project directory
