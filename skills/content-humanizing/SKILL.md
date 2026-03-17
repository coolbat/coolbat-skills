---
name: content-humanizing
description: Use when polishing Chinese or English drafts that feel formulaic, overly smooth, generic, or visibly AI-written, especially before final publication or platform repurposing
---

# Content Humanizing

## Overview

This skill reduces visible AI-writing patterns while preserving meaning, facts, structure, and platform constraints.
Use it after editorial polishing, not before.

Supported modes:
- Chinese
- English
- Platform-aware humanizing for WeChat, SEO blogs, and Xiaohongshu

## Inputs

Required:
- draft file path
- language: `zh` or `en`
- platform: `wechat`, `seo-blog`, or `xiaohongshu`

Optional:
- strength: `light`, `medium`, or `aggressive`
- style notes
- banned phrases list
- phrases that must stay

## Core Rule

Humanize the expression.
Do not alter the facts.

Always preserve:
- source-backed claims
- numbers, dates, names, and quotes
- heading hierarchy where required
- keyword placement constraints for SEO drafts
- the author's core position unless explicitly changed

## Workflow

### 1. Detect the dominant failure mode

Classify the main issue before editing:
- inflated abstraction
- formulaic transitions
- repetitive contrast patterns
- fake neutrality
- bland conclusions
- Chinese AI public-account tone
- English generic LLM essay tone

### 2. Apply language-specific rules

Choose `zh` or `en` rules first.

#### Chinese priorities

- remove empty trend framing
- reduce official or promo tone
- break repetitive rhetorical symmetry
- replace abstract evaluation with concrete detail
- restore spoken rhythm where the platform allows it

Watch for phrases such as:
- "在当下这个时代"
- "值得注意的是"
- "不难发现"
- "从某种意义上说"

#### English priorities

- remove generic AI essay phrases
- reduce over-signposted transitions
- replace polished vagueness with concrete observation
- vary sentence openings and paragraph cadence

Watch for patterns such as:
- "in today's fast-paced landscape"
- "it is important to note that"
- "this highlights the importance of"
- repeated "not just X, but Y"

### 3. Apply platform-specific rules

For `wechat`:
- preserve depth
- allow stronger viewpoint
- keep readable flow

For `seo-blog`:
- preserve H1/H2/H3 structure
- preserve frontmatter and keyword strategy
- improve tone without hurting discoverability

For `xiaohongshu`:
- strengthen the opening hook
- shorten paragraphs
- increase spoken cadence
- remove lecture tone

### 4. Run a preservation pass

Check that:
- facts are unchanged
- structure is still valid
- meaning is unchanged
- SEO constraints still hold where relevant

### 5. Save the result

Write to:
- `polish/humanized-zh.md`
- `polish/humanized-en.md`

Record the pass summary with:
- `assets/templates/humanizing-report-template.md`

Always save the humanized article as its own file.
Do not treat a live-edited draft as a substitute for the saved `polish/humanized-*.md` artifact.

Do not overwrite the source draft by default.

## Strength Levels

### Light

Small cleanup only.
Use when the draft is already strong.

### Medium

Default mode.
Use when the draft is solid but visibly templated.

### Aggressive

Use only when the structure is sound but the voice still feels heavily generated.
Run an extra preservation check afterward.

## Guardrails

- Do not introduce new facts or examples.
- Do not change the article's core claim.
- Do not delete necessary SEO terms.
- Do not confuse "human" with "dramatic" or "sloppy".
- Do not skip the final saved humanized output file.

## Checklist

- [ ] Facts preserved
- [ ] Structure preserved
- [ ] Major AI patterns reduced
- [ ] Platform constraints respected
- [ ] Output saved as a new file
