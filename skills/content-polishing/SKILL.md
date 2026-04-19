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
- whether any fact is buried inside an opinion sentence without clear attribution
- title-body consistency: does the article actually deliver what the title promises?
- ending completion: does the article reach a genuine conclusion, or does it simply stop?

### 2. Editorial review

Check:
- paragraph clarity
- sentence burden
- information density
- tone consistency
- whether examples earn their space
- whether the ending matches the argument
- prose rhythm: are sentence lengths varied, or is every sentence roughly the same weight?
- information density pacing: do high-intensity analytical sections have breathing room around them?
- whether key judgments are set up with enough short, clear sentences before and after to land with impact

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

### 4. Quality gate

Run after editorial review. All hard rules must pass before the article can proceed to humanizing or distribution. Soft rules must pass at least 3 out of 4.

**Hard rules（必须全过，否则返工对应的 review pass）**

- [ ] 开头第一句是否包含具体数字、时间或强对比？（"3周""从0到""比原来快5倍"，而非"随着AI的发展..."）
- [ ] 是否不含以下套话：随着/飞速发展/改变游戏规则/颠覆/赋能/全面/深度？
- [ ] 核心观点是否有具体例子或数据支撑？（不是"效果很好"，是"从56%提升到92%"）
- [ ] 结尾是否有读者能带走的行动或结论？（不是"希望对你有帮助"）

**Soft rules（至少过3条）**

- [ ] 文章中最难理解的概念，是否用了日常生活类比解释？
- [ ] 是否存在至少一个句子，脱离上下文单独截图也能传播？
- [ ] 是否删掉了所有"在某种程度上""可以说""相对来说"等模糊措辞？
- [ ] 正文是否避免了重复表达同一个意思的句子？

**平台补充规则（按发布平台选用）**

小红书：
- [ ] 字数是否在 200-500 字之间？
- [ ] 结尾互动问句是否具体到用户可以直接作答？（"你用过X吗" 而非 "你怎么看？"）
- [ ] 标题或第一行是否带有悬念或信息差？

微信长文：
- [ ] 文章是否以一个具体的场景、问题或冲突开头？
- [ ] 结尾是否有一个话题相关的互动引导（评论/转发）？

**未通过时的处理规则**

- Hard rules 未通过 → 定向返回对应 pass 修改，不推倒重来
- Soft rules 未通过 3 条以上 → 评估是否需要重写局部段落
- 记录扣分项到 `polish/review-notes.md`，供下次迭代参考

### 5. Save review notes

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
- **Do not fabricate hypothetical usage scenarios.** If a section would benefit from a concrete real-world example, insert a placeholder comment instead:
  ```
  <!-- 建议作者在此处插入真实使用场景。理想场景应包含：具体任务类型（如"重构一个有20个文件的模块"）、触发该操作的具体信号（如"看到 token 使用量超过 60%"）、以及实际结果（如"摘要质量明显更高"）。 -->
  ```
  Do not write the scenario yourself. Flag it and move on.

## Checklist

- [ ] Facts reviewed
- [ ] Fact / interpretation / opinion separation verified
- [ ] Title-body consistency checked
- [ ] Ending completion checked
- [ ] Structure reviewed
- [ ] Prose rhythm and pacing reviewed
- [ ] Editorial quality reviewed
- [ ] Quality gate passed (hard rules all green, soft rules 3/4+)
- [ ] Platform fit reviewed
- [ ] Review notes saved
