---
name: image-brief-generator
description: Use when a finished article needs supporting image briefs, placeholder analysis, or context-aware prompts for later illustration, screenshot, or diagram generation
---

# Image Brief Generator

## Overview

This skill analyzes a finished article and produces context-aware image briefs for later visual generation or manual design work.
It does not generate images itself.

## When to Use

Use this skill when:
- the article needs screenshots, diagrams, or illustrations
- image placeholders already exist in the draft
- you want platform-specific visual notes for later production

## Inputs

Required:
- article file path

Optional:
- desired image count
- preferred visual style
- target platform
- language mode: `zh`, `en`, or `bilingual`

## Workflow

### 1. Read the article and detect image opportunities

Look for:
- existing Markdown image placeholders
- comparison sections
- workflows
- product walkthroughs
- conceptual explanations

### 2. Extract context

For each image opportunity, capture:
- section title
- surrounding paragraphs
- image purpose
- candidate filename or slug

### 3. Write the brief

Each image brief should include:
- filename
- section
- purpose
- context summary
- prompt or visual instruction
- bilingual prompt fields when language mode is `bilingual`
- style notes
- aspect ratio suggestion

Use the template at:
- `assets/templates/image-brief-template.md`

### 4. Save the briefs

Save under:

```text
assets/image-briefs/
```

Use one file per image brief unless the user prefers a combined list.

For bilingual projects:
- include both `Prompt (ZH)` and `Prompt (EN)`
- keep the two prompts semantically aligned
- do not translate awkwardly; each prompt should sound natural in its own language

## Guardrails

- Do not generate final image URLs here.
- Do not invent article meaning not supported by the surrounding text.
- Prefer specific briefs over generic "hero image" requests.
- Do not omit bilingual prompts when the project language mode is bilingual.

## Checklist

- [ ] Image opportunities detected
- [ ] Context extracted
- [ ] Briefs written
- [ ] Files saved under assets/image-briefs
