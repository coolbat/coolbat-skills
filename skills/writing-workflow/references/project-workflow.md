## Project Structure

### Storage Path Configuration

Priority order:

1. User instruction in current conversation — "Store this project in `/path/to/articles/`"
2. `.claude/settings.json` → `writing-workflow.base_path`
3. Default: `content-projects/` in current working directory

### Project Directory Structure

```text
{base_path}/{project-slug}/
├── brief/
├── research/
├── drafting/
├── polish/
├── assets/
│   ├── image-prompts/
│   ├── images/
│   └── templates/
├── distribution/
└── meta/
    └── style-library/
        ├── exemplars/
        ├── index.yaml
        └── preferences.yaml
```

## Classification

For a full writing project, classify the article before choosing its workflow.

**Content scenario**: WeChat long-form / SEO blog / WeChat adaptation / Xiaohongshu adaptation / Existing article revision / Humanizing only

**Editorial stance**: Opinion-led / Evidence-led / Narrative-led / Tutorial-led

**Task shape**: New project / Draft from source materials / Revise existing draft / Repurpose final article / Bilingual versions

**Article archetype** — identify before drafting. Each archetype has a different writing emphasis:

| Archetype | Core premise | Writing emphasis |
|-----------|-------------|-----------------|
| **Investigation / Experiment** | "I did this so you don't have to" | Process narrative, layered discoveries, first-person reactions at each step |
| **Product Experience** | "Come explore this with me" | Scene-driven demos, genuine reactions, natural comparisons to alternatives |
| **Phenomenon Analysis** | "Did you notice this? Here's what's behind it" | Observation → curiosity → research → philosophical elevation |
| **Tool / Method Share** | "I found something good" | Personal story as wrapper, reveal the tool naturally, show a jaw-dropping result |
| **Methodology / Opinion** | "Here's what I've figured out" | Every section lands on an executable action; honest about learning curve and failure points; open with humility, close by circling back to all action items |

A local revision may retain the existing classification.

## Workflow

### Step 0. Resolve storage path

Resolve once at the start. Use consistently throughout.

1. Check conversation for explicit path
2. Read `.claude/settings.json` for `writing-workflow.base_path`
3. Fall back to `content-projects/`
4. Expand `~`, convert to absolute path
5. Create project directory if it does not exist

### Step 1. Check project history (optional)

If `meta/project-history.yaml` has 5+ entries, analyze patterns before starting:
- Best-performing editorial stance + scenario combinations
- Fastest research modes
- Common bottlenecks

Share 1-2 actionable insights before proceeding.

### Step 2. Standardize the brief

If the request is incomplete, follow **Sub-skill: content-briefing**.

If no topic is specified, follow **Sub-skill: content-topic-selection**.

Minimum required fields:
- project name, content type, language mode, target audience, content goal
- topic or working title, primary subject, target length
- whether research / images / repurposing are required

Do not proceed to drafting with an incomplete brief.

### Step 3. Assess research risk

Set two flags:

**`timeliness_risk`** → `medium` or `high` if the draft includes:
- specific products, companies, models, platforms, prices, features, release dates
- timing language: "recent", "current", "this year", "latest"
- trend or market claims

**`controversy_risk`** → `medium` or `high` if the draft includes:
- category definitions still in flux
- product comparisons
- directional industry judgments
- claims likely to be challenged by informed readers

If either flag is `medium` or `high`, run **Sub-skill: content-research** in `foundation` mode before drafting.

### Step 4. Foundation research (when needed)

Follow **Sub-skill: content-research** in `foundation` mode.

Output must include: research date, source links, fact / interpretation / opinion separation, freshness notes.

Save to: `research/research-YYYY-MM-DD.md`

### Step 5. Propose directions

Follow **Sub-skill: content-drafting** — direction proposal stage only.

Generate 2-4 candidate directions. Wait for user selection before writing the full draft.

### Step 6. Outline-targeted research (when needed)

After outline is approved, follow **Sub-skill: content-research** in `outline-targeted` mode if the article includes product or trend judgments tied to specific sections.

Save to: `research/research-outline-YYYY-MM-DD.md`

### Step 7. Draft the article

Follow **Sub-skill: content-drafting** — full draft stage.

### Step 8. Polish the draft

Follow **Sub-skill: content-polishing**.

### Step 8a. Quality Gate — Four-Layer Check (required before humanizing)

Run after polishing. Do not proceed to humanizing until all four layers pass.

---

**L1 — Hard Rules (scan and fix before anything else)**

All must pass. No exceptions.

- [ ] Opening does NOT start with: "在当下这个时代" / "随着AI的发展" / "近年来" or any macro trend framing
- [ ] Article is free of filler phrases: 随着/飞速发展/改变游戏规则/颠覆/赋能/全面/深度/不难发现/值得注意的是/综上所述
- [ ] No contrast template "不是...而是..." — rewrite as plain declarative sentences
- [ ] No dash (——) insertions in body prose — rewrite with commas, colons, or split sentences. Exception: figure-caption decoration lines ("— 图源：xxx —") and quoted original text
- [ ] No dramatic/self-dramatizing rhetoric a normal person would not write. Ban and rewrite: "比X更反常的，是…" / "真正的头条是…" / "真正让我停下来的是…" / "输得清清楚楚" / "为…做担保" / "唯一的证据链". State the fact plainly; let the reader supply the drama
- [ ] No stacked epiphany parallelism ("是A，是B，是C" golden-quote triads) — at most one per article, and it must compress concrete facts, not abstractions
- [ ] No vague hedges left unfixed: "在某种程度上" / "可以说" / "相对来说" / "从某种意义上说"
- [ ] Core argument is supported by a specific example, data point, or scene — not abstract assertion
- [ ] No fabricated examples ("比如有一次...") — only real or explicitly hypothetical scenarios
- [ ] All AI tools and products named specifically (no "某AI工具" / "相关模型")

Failure → fix immediately before proceeding to L2.

---

**L2 — Style Consistency**

- [ ] Opening enters from a specific, present-tense event or scene — not a general statement
- [ ] First sentence creates "then what?" momentum
- [ ] Sentence lengths vary — no 3+ consecutive sentences of similar length
- [ ] Normal-person test (from 2026-10 Gemini 4 Argon user feedback): read each sentence and ask "would a normal person say this in a real conversation or a normal article?" — dramatic hooks, ornate metaphors, and courtroom-style rhetorical questions fail; rewrite them as plain declarative sentences and move the emphasis to structure (e.g., a standalone short paragraph), not wording
- [ ] At least one sentence stands alone as a paragraph for emphasis
- [ ] Sections that drift from the main thread are pulled back with a bridging sentence
- [ ] Knowledge is introduced as "just remembered this" — not "let me explain X"
- [ ] At least one moment of self-disclosure: uncertainty, failure, or genuine reaction

Archetype-specific checks:
- Investigation / Experiment → does the reader feel they're discovering alongside the author, step by step?
- Product Experience → is there a "wow" moment shown, not just described?
- Phenomenon Analysis → does the article move from observation → curiosity → research → elevation?
- Tool / Method Share → is the tool revealed through a story, not announced upfront?
- Methodology / Opinion → does every section end with something the reader can do today? Is the learning curve honestly described?

Pass threshold: all universal checks + relevant archetype check.

---

**L3 — Content Quality**

- [ ] Every core claim has a concrete scene, person, or data point behind it — no floating assertions
- [ ] At least one cultural, historical, or philosophical reference that elevates the specific topic to a larger frame — and it feels discovered, not inserted
- [ ] The opposing view or reader's likely objection is acknowledged before the author's position is stated
- [ ] The ending reaches a genuine conclusion — it does not just stop or summarize
- [ ] There is at least one sentence that can be screenshot and shared out of context

Platform checks:
- WeChat long-form: opens with concrete scene/problem/conflict; ends with a topic-specific engagement prompt (not generic "欢迎留言")
- Xiaohongshu: 200–500 words; closing question specific enough for readers to answer directly; title or first line creates curiosity gap
- SEO blog: heading hierarchy intact; CTA aligned with search intent

Pass threshold: all universal checks + relevant platform check.

---

**L4 — Alive-Person Final Read**

Read the full article as a reader who knows nothing about the topic. Answer:

- Does this feel like a specific person sharing something that genuinely moved them — or like an AI outputting information?
- Is there at least one moment where the author's voice is unmistakable?
- Does the author's stance come through clearly, without hedging it into mush?
- Is there any paragraph where attention drops? If yes, that paragraph needs fixing.

This layer has no checklist. It is a judgment call. If any section reads as "AI generating content," return it to content-humanizing for a targeted pass on that section only.

---

**Scoring logic:**
- L1 failure → fix before moving to L2. Do not proceed with unfixed hard rule violations.
- L2 or L3 failure → fix the specific failing item. Do not rewrite the whole article.
- L4 failure → identify the specific paragraph(s) and send back to content-humanizing for a targeted pass.
- Record all failures and fixes in `polish/review-notes.md` with specific line references.
- Re-check after fixes. Repeat until all four layers pass.

### Step 9. Humanize the draft

Follow **Sub-skill: content-humanizing** after polishing, not before.

Preserve: factual claims, source-backed details, SEO structure, core argument.

### Step 10. Cold-read check

Read as a reader who knows nothing about the topic. Verify:
- Can you clearly state what the article is about after finishing it?
- Can you identify the author's core judgment or takeaway?
- Is there a reason given for why the reader should trust that judgment?
- Does the opening match what the article actually delivers?
- WeChat: does the article end with a topic-specific engagement prompt?

Any "no" → fix before distribution.

Skip only if polishing already resolved all of these explicitly.

### Step 11. Repurpose for distribution (when requested)

Follow **Sub-skill: content-repurpose**.

**Every distribution output requires a companion metadata file. No exceptions.**

| Distribution file | Required metadata file |
|---|---|
| `distribution/wechat-article.md` | `distribution/meta-wechat.md` |
| `distribution/seo-blog-zh.md` | `distribution/meta-seo.md` |
| `distribution/seo-blog-en.md` | `distribution/meta-seo.md` |
| `distribution/xiaohongshu-post.md` | `distribution/meta-xiaohongshu.md` |

`meta-wechat.md` minimum fields:
```
title: (final title)
subtitle: (optional)
tags: (3-5 tags)
cover_image: (filename or TBD)
publish_status: draft | ready | published
target_account: (WeChat account name)
notes: (any platform-specific notes)
```

If a meta file is missing for any output that already exists in the project directory, create it before marking distribution as complete.

### Step 12. Image generation (when required)

Requires `baoyu-image-gen` and/or `baoyu-xhs-images` to be installed. Skip gracefully if not available.

#### 12a. Classify image needs

| Type | Use when |
|------|----------|
| `infographic` | Statistics, data, multi-point summaries |
| `scene` | Atmosphere, metaphor, emotional resonance |
| `flowchart` | Process, decision logic, steps |
| `comparison` | Side-by-side contrast, before/after |
| `framework` | Mental models, matrices, named systems |
| `timeline` | Chronology, history, phases |
| `cover` | Article or post cover image |
| `xhs-card` | Xiaohongshu infographic card |

Visual styles: `minimal` / `notion` / `chalkboard` / `warm` / `bold` / `infographic-flat` / `editorial`

#### 12b. Write prompt files before generating

Save every image prompt to disk before calling any image generation tool:

```text
assets/image-prompts/NN-{type}-{slug}.md
```

Each prompt file must include: image type, visual style, content to convey, aspect ratio, negative constraints.

#### 12c. Generate images

Use `baoyu-image-gen` skill. Reference image chain: generate the first image (cover/hero) without `--ref`, then pass it as `--ref` for all subsequent images to maintain visual consistency.

Cover image spec: type / palette / rendering / text / mood

Save to: `assets/images/NN-{type}-{slug}.png`

#### 12d. XHS image series

Use `baoyu-xhs-images` skill. Apply layout × style per card:

- Layout: `sparse` / `balanced` / `dense` / `list` / `flow`
- Style: `cute` / `fresh` / `minimal` / `notion`

Generate all prompts before generating any image. Use reference image chain.

### Step 13. Project retrospective

Write `meta/retrospective.md`:
- which step took the most time and why
- whether any guardrail was violated
- whether the unique angle held through drafting or drifted
- what you would change if redoing this project

Record only what was surprising or non-obvious. Skip normal flow descriptions.

Append to `meta/project-history.yaml`:

```yaml
- date: "YYYY-MM-DD"
  project_slug: "{slug}"
  content_scenario: "{scenario}"
  editorial_stance: "{stance}"
  language_mode: "{zh|en|bilingual}"
  research_mode: "{foundation|outline-targeted|seo-intent|none}"
  word_count: {number}
  bottleneck_step: "{step}"
  style_library_used: {true|false}
  dimensions:
    - "{dimension}: {selected option}"
  performance:
    views: null
    shares: null
    read_completion_rate: null
    date_measured: null
```

## Guardrails

- Do not jump to drafting when the brief is unclear.
- Do not bury the primary subject too late unless the user explicitly wants a delayed reveal.
- Do not fabricate facts, numbers, quotes, or test results.
- Do not present author interpretation as broad public consensus unless sourced.
- Do not treat humanizing as permission to change meaning.
- Do not destroy SEO structure to sound less like AI.
- Do not overwrite prior project files without checking the existing directory.
- Do not skip editorial stance classification.
- Do not skip the cold-read step unless polishing already resolved all four checks explicitly.
- Do not publish distribution outputs without their companion metadata files.

## Checklist

- [ ] Storage path resolved
- [ ] Project directory created
- [ ] Project history analyzed (if 5+ past projects)
- [ ] Project classified (scenario + editorial stance)
- [ ] Brief complete (including unique angle and competitive gap)
- [ ] Research risk assessed
- [ ] Foundation research completed if needed
- [ ] SEO intent research completed if SEO blog
- [ ] Direction selected before full drafting
- [ ] Outline-targeted research completed if needed
- [ ] Draft reviewed for facts, structure, rhythm, title-body fit, ending
- [ ] Quality Gate passed (hard rules all green, soft rules 3/4+)
- [ ] Cold-read check passed
- [ ] Humanizing applied after polishing
- [ ] Images: prompt files written before generation
- [ ] Distribution outputs created if requested
- [ ] Distribution metadata files written (one per output)
- [ ] Retrospective written
- [ ] Project history updated

---
