# coolbat-skills

English-first, bilingual skill bundles for agentic writing workflows.

This repository is where I publish reusable personal skills that have been tested through real writing projects, not just drafted as prompt ideas.

## Highlights

- Structured long-form writing workflow
- English-first architecture with Chinese writing support
- Two-stage research flow: `foundation` + `outline-targeted`
- WeChat and Xiaohongshu repurposing
- Humanizing pass for Chinese and English drafts
- Bilingual image brief generation

## Why This Repo Exists

Most writing prompts break down in the same places:
- they start drafting before research is strong enough
- they blur facts and interpretation
- they skip review artifacts
- they treat platform adaptation as simple shortening

This repo packages writing skills as a real workflow system instead of a single mega-prompt.

## Current Bundle

The first published bundle is `writing-workflow`, a routed skill system for:
- WeChat long-form articles
- SEO blog drafting
- Chinese / English / bilingual writing
- platform repurposing
- image brief generation

## Workflow Overview

```text
brief
  -> research risk check
  -> foundation research
  -> direction selection
  -> outline
  -> outline-targeted research
  -> draft
  -> polish
  -> humanize
  -> repurpose
  -> image briefs
```

The goal is simple:

**make long-form writing reproducible, reviewable, and easier to reuse across platforms.**

## Included Skills

| Skill | Purpose |
| --- | --- |
| `writing-workflow` | Main router for structured writing projects |
| `content-briefing` | Turns rough requests into usable briefs |
| `content-research` | Handles current facts, sourcing, and evidence |
| `content-drafting` | Generates angles, outlines, and drafts |
| `content-polishing` | Reviews structure, facts, and platform fit |
| `content-humanizing` | Reduces visible AI-writing patterns |
| `content-repurpose` | Adapts final drafts for WeChat / Xiaohongshu / SEO |
| `image-brief-generator` | Produces image briefs with bilingual prompts |

## Repository Layout

```text
skills/
  writing-workflow/
  content-briefing/
  content-research/
  content-drafting/
  content-polishing/
  content-humanizing/
  content-repurpose/
  image-brief-generator/
```

## Install

Copy the skill directories you want into your local skills folder.

For Codex-style setups, that usually means:

```text
~/.agents/skills/
```

Keep these intact:
- `SKILL.md`
- `agents/openai.yaml`
- `assets/templates/`
- `references/` where present

## Quick Start

Start from:

```text
skills/writing-workflow/SKILL.md
```

Typical use:

1. Create a project folder under `content-projects/{project-slug}/`
2. Normalize the brief
3. Assess `timeliness_risk` and `controversy_risk`
4. Run `foundation` research if needed
5. Propose directions before full drafting
6. Approve outline
7. Run `outline-targeted` research if needed
8. Draft, polish, humanize, and repurpose

## Minimal Example

Use this bundle when you want to do things like:
- write a WeChat deep-dive article from a vague topic
- turn research notes into a structured SEO draft
- write in Chinese and later repurpose into Xiaohongshu
- generate image briefs after the article is done

## References

The main workflow includes lightweight internal references:
- `skills/writing-workflow/references/case-study.md`
- `skills/writing-workflow/references/evolution-note-2026-03.md`

They explain:
- how the workflow performed on real projects
- what broke in early versions
- why the current rules are stricter

## Roadmap

Planned next:
- more skill bundles beyond writing
- stronger README examples
- additional public case studies
- better packaging guidance for reuse across agent environments

## 中文说明

这是我个人整理和打磨的技能仓库。  
当前第一个公开 bundle 是 `writing-workflow`，它不是单个 prompt，而是一整套写作工作流：

- 先做 brief
- 再判断 research 风险
- 再做两阶段 research
- 再定大纲和初稿
- 再审校、降 AI 味、平台改写
- 最后补 image briefs

它目前最适合：
- 公众号长文
- SEO 博客
- 双语写作
- 微信 / 小红书分发

## License

MIT
