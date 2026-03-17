# Case Study: OpenClaw WeChat Article Workflow

## Purpose

This case study captures one full run of the writing workflow so future agents can see:
- what a successful project structure looks like
- where the workflow needed correction
- how the router and sub-skills should cooperate in practice

Read this only when you need a concrete example of the workflow, not for every invocation.

## Scenario

The user wanted a WeChat long-form article about the evolution of AI agents, centered on the impact of OpenClaw, using Manus as a key comparison point.

Requirements that emerged during the run:
- Chinese WeChat long-form first
- later repurpose into Xiaohongshu
- preserve a serious tone with some humor
- include a strong personal judgment
- avoid writing unsupported public-consensus claims
- treat Agent as a concept still converging, not as a fixed universal definition

## Final Project Path

```text
content-projects/claude-code-writing-agent-demo/
```

## Files Produced

### Briefing

- `brief/brief.md`
- `brief/requirements.md`
- `meta/project.json`
- `meta/style-notes.md`

### Research

- `research/research-2026-03-15.md`

### Drafting

- `drafting/outline-zh.md`
- `drafting/draft-zh.md`
- preserved revisions:
  - `drafting/draft-zh-v1.md`
  - `drafting/draft-zh-v2.md`
  - `drafting/draft-zh-v3.md`

### Polishing

- `polish/review-notes.md`
- `polish/humanized-zh.md`

### Distribution

- `distribution/wechat-article.md`
- `distribution/xiaohongshu-post.md`

### Image Briefs

- `assets/image-briefs/wechat-article/01-openclaw-signal.md`
- `assets/image-briefs/wechat-article/02-model-vs-agent.md`
- `assets/image-briefs/wechat-article/03-agent-discussion-shift.md`
- `assets/image-briefs/wechat-article/04-manus-execution.md`
- `assets/image-briefs/wechat-article/05-openclaw-environment.md`
- `assets/image-briefs/wechat-article/06-delivery-race.md`

## What Worked

### 1. Research before strong judgment

The article improved significantly once research happened before major framing decisions.

Useful result:
- the article stopped saying “many people think…” without evidence
- the article moved to “here is my analytical frame” with explicit distinction between fact and interpretation

### 2. Main-subject-first opening

The user wanted the article to be about OpenClaw's impact.
The first draft opened too abstractly and reached OpenClaw too late.

Useful correction:
- move OpenClaw to the opening
- explain why OpenClaw matters before broader theory
- bring Manus in as comparison, not as the opening center

### 3. Two-stage shaping worked better than one-pass drafting

The workflow improved when it followed:
- brief
- research
- outline
- draft
- revise opening focus
- polish
- humanize
- repurpose

### 4. Separate distribution outputs were worth it

The WeChat article and Xiaohongshu post needed different pacing.
Repurposing from the humanized WeChat draft worked better than trying to write both formats in one pass.

### 5. Bilingual image prompts are useful even for Chinese-first output

The image briefs became more reusable once each file included:
- `Prompt (ZH)`
- `Prompt (EN)`

This made later visual production easier across tools.

## What Broke Or Needed Adjustment

### 1. The original workflow was too loose about research timing

Problem:
- initial drafting started before a strong enough factual base

Fix now reflected in the skill:
- use `foundation` research before drafting when timeliness or controversy risk is present
- use `outline-targeted` research after outline approval when the article makes strong section-level judgments

### 2. The workflow did not explicitly enforce early subject focus

Problem:
- a topic-led WeChat article opened with too much theory before naming the main subject

Fix now reflected in the skill:
- every brief should include `primary subject`
- candidate directions should specify how early the subject appears
- drafting and polishing now check opening focus

### 3. Humanizing happened in practice but was not originally forced to save a separate artifact

Problem:
- conversational iteration can make agents edit drafts directly and skip a proper `polish/humanized-*.md`

Fix now reflected in the skill:
- humanized outputs must be saved explicitly

### 4. Review notes were initially implicit

Problem:
- feedback and fixes happened inline in conversation without a saved artifact

Fix now reflected in the skill:
- `polish/review-notes.md` is now mandatory

### 5. Image briefs originally used English-only prompts

Problem:
- Chinese-first projects still needed bilingual visual prompts later

Fix now reflected in the skill:
- bilingual image prompts are now part of the image brief workflow

## Recommended Pattern

For similar writing projects, prefer this sequence:

1. Normalize the brief
2. Assess `timeliness_risk` and `controversy_risk`
3. Run `content-research` in `foundation` mode if either risk is medium/high
4. Propose directions and check subject focus
5. Approve outline
6. Run `content-research` in `outline-targeted` mode if the article makes strong product or trend judgments
7. Draft
8. Save `polish/review-notes.md`
9. Save `polish/humanized-*.md`
10. Repurpose into platform outputs
11. Generate bilingual image briefs if visuals are needed

## Anti-Patterns Revealed By This Case

- opening too far away from the named subject
- writing trend judgments before research
- presenting interpretation as broad public consensus
- polishing inline without saving review notes
- humanizing inline without saving a separate output
- treating image briefs as monolingual by default

## Validation Use

Use this case study to validate the workflow when updating the skill.

Questions to ask:
- Would the updated workflow still force research before unsupported trend judgments?
- Would it push OpenClaw into the opening of an OpenClaw-led article?
- Would it save review notes and humanized output as files?
- Would it still produce separate WeChat and Xiaohongshu outputs?
- Would it generate bilingual image prompts?
