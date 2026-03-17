---
name: content-repurpose
description: Use when a finished article needs to be adapted into platform-specific outputs such as WeChat article versions, SEO blog versions, or Xiaohongshu image-text posts
---

# Content Repurpose

## Overview

This skill adapts a finished article into downstream platform formats.
It should preserve the core argument while reshaping structure, pacing, and packaging for the target channel.

## Inputs

Required:
- finished source article
- target platform

Optional:
- language mode
- style notes
- image brief requirements

## Workflow

### 1. Identify the source type

Determine whether the source is:
- WeChat long-form
- SEO blog
- humanized final draft
- bilingual pair

### 2. Identify the target output

Supported outputs:
- `distribution/wechat-article.md`
- `distribution/seo-blog-zh.md`
- `distribution/seo-blog-en.md`
- `distribution/xiaohongshu-post.md`

### 3. Adapt by platform

For WeChat:
- keep the article complete
- preserve depth and readable pacing
- use shorter paragraphs if needed
- add emphasis formatting only where it improves scanability
- favor clean subheads over excessive section nesting
- make the opening enter the main subject quickly
- keep key judgment lines easy to screenshot or quote

Template:
- `assets/templates/wechat-article-template.md`

For SEO:
- preserve structural scanability
- keep frontmatter if the project uses it
- retain keyword-safe headings and CTA

Template:
- `assets/templates/seo-blog-template.md`

For Xiaohongshu:
- open with a stronger hook
- use shorter sections
- sound more spoken and immediate
- keep concrete details
- avoid lecture tone
- include title options
- include a cover-title suggestion
- include a hook block
- include a card-by-card structure suggestion
- include a comment prompt or CTA

Template:
- `assets/templates/xiaohongshu-post-template.md`

### 4. Save each target version separately

Do not overwrite the source final draft.

Expected defaults:
- WeChat adaptation should save to `distribution/wechat-article.md`
- Xiaohongshu adaptation should save to `distribution/xiaohongshu-post.md`

## Output Expectations

### WeChat output should usually contain
- final title
- direct opening
- clear section headings
- readable paragraph spacing
- selective bold emphasis for key lines
- clean closing and CTA if needed

### Xiaohongshu output should usually contain
- 3-5 title options
- one cover-title suggestion
- one short hook opening
- short-body version with spoken cadence
- suggested card structure
- comment prompt or CTA

Do not treat Xiaohongshu as a shortened WeChat article.
Repackage it around hooks, rhythm, and card utility.

## Guardrails

- Do not invent new claims during adaptation.
- Do not flatten the argument into generic summary bullets.
- Do not break SEO requirements when adapting to SEO outputs.
- Do not erase the author's viewpoint for the sake of uniformity.
- Do not output WeChat and Xiaohongshu in the same pacing style.
- Do not skip titles, hooks, or card structure when adapting to Xiaohongshu.

## Checklist

- [ ] Source type identified
- [ ] Target platform identified
- [ ] Platform-specific adaptation applied
- [ ] Output matches the platform template shape
- [ ] Output written to the correct file
