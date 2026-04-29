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
- style library (from `content-style-learning`)

## Workflow

### 1. Inspect the brief

Confirm:
- audience
- goal
- language mode
- platform
- primary subject
- target length
- editorial stance: opinion-led, evidence-led, narrative-led, or tutorial-led
- unique angle and competitive gap if present in the brief

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

**Dimension randomization** (to avoid article homogeneity):

Before drafting, randomly activate 2-3 dimensions from the following pools to vary expression style:

| Dimension | Options |
|-----------|---------|
| Narrative perspective | First-person experiential / Observer analysis / Dialogue format / Self-Q&A |
| Timeline | Chronological / Reverse chronological / Flashback / Non-linear |
| Analogy domain | Sports / Cooking / Military / Romance / Gaming / Film / Architecture / Medicine |
| Emotional baseline | Restrained calm / Passionate energetic / Satirical critical / Warm healing / Anxious warning |
| Rhythm | Dense short sentences / Slow long narrative / Alternating long-short / Slow start fast finish |

If `meta/project-history.yaml` exists, check the last 3 projects' `dimensions` field and avoid using the exact same combination.

Record the activated dimensions in `meta/project-history.yaml` for future reference.

**Check for style library** (before drafting):

If `meta/style-library/index.yaml` exists:
1. Load exemplars matching the current editorial stance:
   - Opinion-led → `opinion` category
   - Narrative-led → `narrative` category
   - Tutorial-led → `tutorial` category
   - Evidence-led → `analysis` category
2. Extract top 2-3 exemplars by relevance
3. Read their sample segments (opening hook, emotional peak, transition, closing)
4. Inject into drafting prompt as style examples:
   ```
   The following are authentic writing samples from this author's published work.
   Emulate the sentence rhythm, emotional intensity, and voice patterns:
   
   [Opening Hook Style]
   {exemplar opening sample}
   
   [Emotional Expression Style]
   {exemplar emotional peak sample}
   
   [Transition Style]
   {exemplar transition sample}
   
   [Closing Style]
   {exemplar closing sample}
   ```
5. Apply preferences from `meta/style-library/preferences.yaml` as constraints

If no style library exists:
- Use generic writing guidelines only
- After drafting, suggest: "To make future drafts match your style better, you can import published articles with 'import exemplar' or teach me by editing this draft and saying 'learn my edits'."

**Language-specific drafting**:

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

**Insert editorial anchors**:
- Place 2-3 editorial anchor comments at key positions in the draft
- Format: `<!-- ✏️ 编辑建议：在这里加一句你自己的经历/看法 -->` (Chinese) or `<!-- ✏️ Editorial note: Add your own experience/perspective here -->` (English)
- Recommended positions:
  - After the opening hook (before entering the main argument)
  - Before the core judgment or main point
  - Before the closing summary
- Purpose: Transform AI draft into "your work" by prompting personal input at critical moments

Use the template at:
- `assets/templates/draft-template.md`

### 5. Quick self-check after drafting

Immediately after completing the draft, run a 5-item scan and fix issues on the spot to reduce the need for rewrites in the polishing stage.

**Writing quality checks** (fix immediately):
1. **Forbidden phrases**: Check against the brief's `forbidden claims or phrases` list. Replace any matches.
2. **Sentence length variance**: Scan for 3+ consecutive sentences with similar length (within 5 characters). Break up or add short sentences to create rhythm.

**Content quality checks** (fix immediately):
3. **Opening hook**: Do the first 3 sentences create suspense, conflict, or curiosity? If they're just background exposition, rewrite the opening.
4. **Core argument penetration**: Does the main point appear in multiple sections, or only once? If only once, reinforce it in at least one other H2 section.
5. **Quotable moment**: Is there at least 1 sentence that could be screenshot and shared independently? If not, add one at an emotional peak.

This is a lightweight pass done by the agent itself — no external scripts needed. Fix issues inline before saving the draft.

### 6. Save outputs

Before saving a revised draft, archive the current version first:
- rename `drafting/draft-zh.md` to `drafting/draft-zh-v{N}.md` before overwriting
- rename `drafting/draft-en.md` to `drafting/draft-en-v{N}.md` before overwriting

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
- [ ] Unique angle and competitive gap noted
- [ ] Dimensions randomized (2-3 selected, avoiding recent combinations)
- [ ] Style library checked and loaded (if exists)
- [ ] Directions proposed
- [ ] Direction selected
- [ ] Outline created
- [ ] Opening focus checked
- [ ] Style examples injected (if style library exists)
- [ ] Editorial anchors inserted (2-3 positions)
- [ ] Quick self-check completed (5 items)
- [ ] Prior draft version archived before overwrite
- [ ] Draft saved to the correct file
