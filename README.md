# coolbat-skills

Writing workflow skills for agentic long-form content production. Tested through real projects, not just drafted as prompt ideas.

## Install

```bash
npx skills add coolbat/coolbat-skills@writing-workflow
```

That's it. All sub-skills are embedded in a single file — no additional installs required.

## Optional: Image Generation

Image generation steps are skipped gracefully if not installed. To enable:

```bash
# AI image generation (OpenAI, Google, DashScope, Jimeng, Seedream, Replicate)
npx skills add JimLiu/baoyu-skills@baoyu-image-gen

# Xiaohongshu infographic card series
npx skills add JimLiu/baoyu-skills@baoyu-xhs-images
```

Configure at least one API key:

| Provider | Environment Variable |
|----------|---------------------|
| OpenAI | `OPENAI_API_KEY` |
| Google | `GOOGLE_API_KEY` |
| DashScope (阿里通义万象) | `DASHSCOPE_API_KEY` |
| Jimeng / Dreamina (即梦) | `dreamina login` |
| Seedream (豆包) | `ARK_API_KEY` |
| Replicate | `REPLICATE_API_TOKEN` |

## What It Does

`writing-workflow` is a structured router for long-form writing projects:

- WeChat long-form articles
- SEO blog drafting (Chinese / English / bilingual)
- Platform repurposing (WeChat / Xiaohongshu / SEO)
- Style library that learns from your edits over time

The workflow enforces a quality gate before every article ships — based on the [autoresearch](https://github.com/karpathy/autoresearch) framework: fixed checklist, targeted fixes, no full rewrites.

## Workflow

```text
brief → research risk check → foundation research (if needed)
  → direction selection → outline → outline-targeted research (if needed)
  → draft → polish → quality gate → humanize → cold-read
  → repurpose → image generation (optional) → retrospective
```

## Why This Exists

Most writing prompts break down in the same places:
- they start drafting before research is strong enough
- they blur facts and interpretation
- they skip review artifacts
- they treat platform adaptation as simple shortening
- they have no quality gate — output quality varies every run

This repo packages writing as a real workflow system with a fixed quality bar.

## Included Skills

| Skill | Purpose |
|-------|---------|
| `writing-workflow` | Full workflow router with all sub-skills embedded |
| `image-brief-generator` | Produces image briefs with bilingual prompts |

Sub-skills (briefing, research, drafting, polishing, humanizing, repurposing, style learning) are all embedded inside `writing-workflow/SKILL.md`.

## Repository Layout

```text
skills/
  writing-workflow/    ← install this one
    SKILL.md           ← full workflow + all sub-skills inline
    references/
      case-study.md
      evolution-note-2026-03.md
  image-brief-generator/
```

## References

- `skills/writing-workflow/references/case-study.md` — real project run walkthrough
- `skills/writing-workflow/references/evolution-note-2026-03.md` — why the current rules are stricter

## 中文说明

这是我个人整理和打磨的写作技能仓库。

安装：

```bash
npx skills add coolbat/coolbat-skills@writing-workflow
```

所有子技能已内嵌在单个文件里，一条命令搞定。

适合：公众号长文、SEO 博客、双语写作、微信/小红书分发。

核心特点：内置基于 autoresearch 框架的质量关卡，每篇文章发布前必须通过固定 checklist，不靠感觉判断质量。

## License

MIT
