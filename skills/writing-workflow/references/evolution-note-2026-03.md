# Writing Workflow Evolution Note (2026-03)

## Purpose

This note records how the writing workflow changed after running two real projects:
- an OpenClaw / Manus WeChat article
- a Naval Almanack commentary article

Use this file to understand why the current workflow has stricter rules than the original version.

## Before

The original skill system already had the right high-level decomposition:
- briefing
- research
- drafting
- polishing
- humanizing
- repurposing
- image briefs

But it was still missing several operational constraints that only became obvious during real execution.

## What Triggered The Changes

### Case 1: OpenClaw Article

The OpenClaw case exposed these issues:
- drafting started before the factual base was strong enough
- the opening buried the main subject too late
- review and humanizing happened in practice, but their saved artifacts were initially missing
- image briefs were useful, but English-only prompts were too limiting for later reuse

### Case 2: Naval Almanack Article

The Naval case exposed a different set of pressures:
- book commentary needs distinction between source material and author interpretation
- “thought leader” content easily slides into summary or quote collection
- a second research pass after outline approval is useful when the article contains strong evaluative judgments
- the workflow also needed to prove it was not only useful for product commentary

## Major Changes

### 1. Research became two-stage

The system now supports:
- `foundation` research
- `outline-targeted` research

Reason:
- some articles need a factual base before any real framing
- some articles need section-level evidence only after the outline is approved

This change lives mainly in:
- `writing-workflow/SKILL.md`
- `content-research/SKILL.md`
- `content-research/assets/templates/research-template.md`

### 2. Research risk is now explicit

The workflow now uses:
- `timeliness_risk`
- `controversy_risk`

Reason:
- not every article needs full research
- but the decision should not depend on vague intuition alone

This allows the skill to trigger research from clear conditions while still letting the user override when needed.

### 3. Primary-subject focus became a first-class rule

The workflow now requires the brief to name the article's `primary subject`.

Drafting and polishing now check:
- whether the opening reaches that subject early enough
- whether the article spends too long in abstract setup before entering the promised topic

Reason:
- the OpenClaw article opened too far away from OpenClaw in its early version
- this is especially risky for WeChat topic-led writing

This change lives mainly in:
- `writing-workflow/SKILL.md`
- `content-drafting/SKILL.md`
- `content-drafting/assets/templates/angle-options-template.md`
- `content-drafting/assets/templates/outline-template.md`
- `content-polishing/SKILL.md`

### 4. Review and humanizing artifacts became mandatory

The workflow now explicitly requires:
- `polish/review-notes.md`
- `polish/humanized-*.md`

Reason:
- conversational iteration makes it easy to fix drafts inline and forget to save the process artifacts
- those files are critical for making the workflow reproducible

This change lives mainly in:
- `content-polishing/SKILL.md`
- `content-humanizing/SKILL.md`

### 5. Image briefs became bilingual-ready

The workflow now supports:
- `language mode: zh / en / bilingual`
- `Prompt (ZH)`
- `Prompt (EN)`

Reason:
- Chinese-first projects still benefit from English prompts for image tools and later reuse
- image briefs are more reusable when they are not monolingual

This change lives mainly in:
- `image-brief-generator/SKILL.md`
- `image-brief-generator/assets/templates/image-brief-template.md`

### 6. Repurposing became more explicit

The repurpose skill now distinguishes platform outputs more concretely.

WeChat output now expects:
- early subject focus
- reader payoff
- selective emphasis
- readable long-form pacing

Xiaohongshu output now expects:
- title options
- cover title
- hook
- short spoken body
- card structure
- comment prompt

Reason:
- a platform-specific output is not just a shorter or longer version of the same text
- the earlier version of the skill was too abstract here

This change lives mainly in:
- `content-repurpose/SKILL.md`
- `content-repurpose/assets/templates/wechat-article-template.md`
- `content-repurpose/assets/templates/xiaohongshu-post-template.md`

## What Stayed The Same

Several original design decisions still held up well:
- main router + sub-skill architecture
- project-per-directory file organization
- bilingual drafting should not default to line-by-line translation
- humanizing should happen after polishing
- image generation should stay separate from image brief generation

## Practical Lessons

### 1. Writing workflows fail at the edges, not in the middle

The original architecture was already solid.
Most failures happened in edge cases:
- when to research
- how soon to enter the subject
- whether to save intermediate artifacts
- how to repurpose without flattening the text

### 2. Platform specificity matters more than expected

WeChat and Xiaohongshu are not just different lengths.
They demand different pacing, different entry points, and different packaging.

### 3. Strong commentary needs stronger distinction between fact and framing

Without an explicit split between:
- fact
- interpretation
- opinion

the system drifts into unsupported certainty too easily.

### 4. Real examples are more valuable than perfect abstractions

The workflow improved far more from two real articles than it did from initial design alone.

## Current Validation State

The workflow has now been validated against:

### Case 1
- Topic: product / agent evolution commentary
- Outputs:
  - WeChat article
  - Xiaohongshu post
  - bilingual image briefs

### Case 2
- Topic: book / idea commentary
- Outputs:
  - WeChat article
  - two-stage research
  - review notes
  - humanized output

## Next Useful Validation

The next best stress test would be a non-commentary writing task, such as:
- tutorial
- practical guide
- case-study writeup
- workflow explainer

That would confirm whether the system generalizes beyond opinion-led long-form writing.
