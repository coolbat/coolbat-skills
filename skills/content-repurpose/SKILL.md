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
- always end with an engagement prompt that invites readers to comment or share — this is required for WeChat, not optional. The prompt should be specific to the article topic (e.g., "你在用 Claude Code 时踩过什么坑？欢迎在评论区分享"), not generic ("欢迎留言").
- support container syntax for enhanced presentation:
  - `:::dialogue` for conversation blocks
  - `:::timeline` for chronological events
  - `:::callout tip|warning|info|danger` for highlighted notes
  - `:::quote` for pull quotes or key statements
- container syntax is optional — use only when it adds value to the content
- see `references/container-syntax.md` for detailed usage guidelines

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
- include title options (with at least one option optimized for search keywords)
- include a cover-title suggestion
- include a hook block
- include a card-by-card structure suggestion
- include a comment prompt or CTA
- include 3-5 hashtag suggestions with rationale (traffic vs niche balance)
- include a first-comment suggestion if the article has a link, keyword list, or detail that benefits from extra SEO surface area

Template:
- `assets/templates/xiaohongshu-post-template.md`

### 4. Save each target version separately

Do not overwrite the source final draft.

Expected defaults:
- WeChat adaptation should save to `distribution/wechat-article.md`
- Xiaohongshu adaptation should save to `distribution/xiaohongshu-post.md`

### 5. Save distribution metadata

After producing each platform output, write a companion metadata file at `distribution/meta-{platform}.md`.

For WeChat, include:
- article title
- summary (2-3 sentences for the cover description field)
- cover image direction or suggestion

For SEO blog, include:
- slug suggestion
- meta title (under 60 characters)
- meta description (under 160 characters)
- primary keyword

For Xiaohongshu, include:
- selected title
- cover text
- hashtags
- first comment draft (if applicable)

## Output Expectations

### WeChat output should usually contain
- final title
- direct opening
- clear section headings
- readable paragraph spacing
- selective bold emphasis for key lines
- engagement prompt at the end — topic-specific, invites comments or sharing (required)

### Xiaohongshu output should usually contain
- 3-5 title options (at least one keyword-optimized)
- one cover-title suggestion
- one short hook opening
- short-body version with spoken cadence
- suggested card structure
- comment prompt or CTA
- hashtag suggestions
- first comment draft if applicable

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
- [ ] Distribution metadata file written
