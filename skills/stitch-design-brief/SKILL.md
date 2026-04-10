---
name: stitch-design-brief
description: Use when a user wants to generate or iterate a UI page in Stitch from a PRD, requirements doc, marketing brief, homepage brief, landing page brief, SEO page brief, or website brief, especially when they need a structured Stitch prompt, clearer design direction, or stronger anti-generic AI design constraints before generating or editing screens
---

# Stitch Design Brief

## Overview

This skill standardizes the design handoff into Stitch.

Use it to convert messy requirements into a repeatable brief, generation prompt, edit prompt, and review pass instead of improvising prompts from scratch.

## When to Use

Use this skill before Stitch work when:
- the input is a completed page strategy document from the `premium-tool-page` skill — in this case skip Steps 1 and 2 entirely and go straight to Step 3 (fill the brief template), using the strategy doc as the source of truth
- the user provides a PRD, requirements doc, homepage brief, landing page request, or SEO page brief
- the task is to design a website, landing page, template hub, resource page, or matrix page in Stitch
- the user wants to improve prompt quality or reduce generic "AI-looking" output
- the user wants to edit an existing Stitch screen with clearer direction
- the user wants to generate or iterate a UI page using Stitch
- the user provides product, marketing, or SEO requirements that need to become visual design direction
- the page is for an AI tool, AI SaaS, AI app, AI feature, model-driven workflow, prompt product, or automation product and the value proposition needs to be shown clearly rather than described vaguely

Examples:
- "根据这个 PRD 生成 Stitch prompt"
- "先走 Stitch 设计节点"
- "给这个页面产出 Stitch brief"
- "把需求整理成 Stitch prompt"
- "优化一下 Stitch 的 prompt"
- "给现有 Stitch 页面写 edit prompt"

Do not use this skill when:
- the task is implementation-only and the design is already approved
- the user only wants code refactoring with no design generation step

## Workflow

1. Extract the core inputs from the source material:
   - product positioning
   - target audience
   - primary conversion goal
   - brand tone
   - SEO intent
   - required sections
   - for AI products: core workflow, input type, output type, demo expectation, and trust proof

2. Validate the minimum inputs.
   - If primary audience is missing or ambiguous, stop and ask.
   - If primary conversion goal is missing or ambiguous, stop and ask.
   - If the page type or main device target cannot be inferred, stop and ask.

3. Fill the brief template in [assets/prompt-template.md](assets/prompt-template.md).
   - If the page is for an AI tool and the positioning still feels generic, read [references/ai-tool-examples.md](references/ai-tool-examples.md) for concrete framing patterns before writing the final prompt.

4. Produce three outputs:
   - a structured brief
   - a Stitch generation prompt
   - if revising existing work, a Stitch edit prompt

5. After Stitch generates a screen, review it with [assets/review-checklist.md](assets/review-checklist.md).

6. If the output misses the mark, choose or adapt a targeted follow-up from [assets/edit-prompts.md](assets/edit-prompts.md) instead of rewriting the entire brief.

## Core Rules

- Treat the brief as the source of truth. Do not jump straight from PRD to freeform prompt writing.
- Keep one clear primary conversion goal.
- Add explicit anti-generic constraints. Stitch defaults drift toward repetitive layouts and vague copy.
- For websites, always add an SEO section to the brief even if the original requirements did not.
- Keep the prompt concrete: name audiences, scenarios, sections, headings, and forbidden patterns.
- For AI products, never stop at "AI-powered" positioning. State what the user inputs, what the system returns, how fast it works, and what proof makes the output believable.

## Output Shape

The final handoff should usually contain:
- `Structured brief`
- `Generation prompt`
- `Review focus`
- `Edit prompt` if iterating

## Default Design Node In Workflow

Use this node in the flow:

`PRD / brief -> stitch-design-brief -> Stitch generate -> review checklist -> Stitch edit -> implementation`

If the user has not asked for code yet, stop after the design prompt or the Stitch pass.
