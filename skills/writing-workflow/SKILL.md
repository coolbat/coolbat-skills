---
name: writing-workflow
description: Use when handling long-form writing projects for WeChat articles, SEO blogs, bilingual content, or downstream repurposing into WeChat and Xiaohongshu formats. Includes all sub-skills inline — no additional installs required except optional image generation dependencies.
---

# Writing Workflow

## Overview

This skill is the router for structured writing projects. All sub-skills are embedded — install this one skill and the full workflow is available.

Supported scenarios:
- WeChat long-form
- SEO blog
- WeChat adaptation
- Xiaohongshu adaptation
- Existing article revision
- Humanizing only

## Optional Dependencies

Image generation steps require separate installation:

```bash
# For AI image generation (OpenAI, Google, DashScope, Jimeng, Seedream, Replicate)
npx skills add JimLiu/baoyu-skills@baoyu-image-gen

# For Xiaohongshu infographic card series
npx skills add JimLiu/baoyu-skills@baoyu-xhs-images
```

At least one API key must be configured for image generation to work:

| Provider | Environment Variable |
|----------|---------------------|
| OpenAI | `OPENAI_API_KEY` |
| Google | `GOOGLE_API_KEY` |
| DashScope (阿里通义万象) | `DASHSCOPE_API_KEY` |
| Jimeng / Dreamina (即梦) | Login via `dreamina login` |
| Seedream (豆包) | `ARK_API_KEY` |
| Replicate | `REPLICATE_API_TOKEN` |

Image generation steps are skipped gracefully if these dependencies are not installed.

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

Classify before doing anything else.

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

Do not skip classification.

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

## Sub-skill: content-briefing

Use when a writing request is vague, underspecified, or spread across messages.

### When to use

- Topic is clear but scope is not
- User gave goals without audience details
- User wants bilingual or multi-platform output but has not specified priorities
- Title, keyword, or CTA is still fuzzy

Do not use when a complete brief already exists.

### Required fields

- project name, content type, editorial stance, language mode
- target audience, primary goal, topic or working title, target length, desired tone
- **article archetype** (see Classification section): Investigation / Product Experience / Phenomenon Analysis / Tool Share / Methodology
- unique angle: what makes this article worth reading over existing content
- competitive gap: where existing coverage falls short
- whether research / images / repurposing are required

Optional: keywords, forbidden claims or phrases, desired CTA, reference pieces

### Workflow

1. Check for existing brief at `brief/brief.md`, `brief/requirements.md`, `meta/project.json` — reuse if complete
2. Fill missing fields from user's request or ask concise follow-up questions for essentials only
3. **Determine article archetype** — if user hasn't specified, ask: "这篇文章的切入方式更像哪种：亲自下场实验、产品体验带读者、现象分析、推荐工具/方法，还是方法论分享？" Match to the five archetypes in Classification.
4. Normalize into: objective / audience / deliverables / constraints / open risks
5. Save: `brief/brief.md`, `brief/requirements.md`, `meta/project.json`

### Guardrails

- Do not begin full drafting here
- Do not invent business goals or target readers without marking them as assumptions
- Do not overwrite a stronger existing brief with a weaker summary

---

## Sub-skill: content-topic-selection

Use when the user needs topic ideas or wants to generate topics based on current trends.

### Workflow

1. **Fetch hot topics** via WebSearch from: Weibo hot search, Toutiao, Baidu hot list, Zhihu, GitHub Trending (for Chinese); Twitter, Reddit, Hacker News, GitHub Trending (for English)
2. **Filter by relevance** to user's content focus areas — narrow to 15-20 topics
3. **Check history** — if `meta/project-history.yaml` exists, remove topics similar to recent articles
4. **Score each topic** on 3 dimensions (0-10):
   - SEO Potential: search volume, competition, long-tail opportunities
   - CTR Potential: emotional trigger, specificity, timeliness
   - User Fit: matches expertise, aligns with style, unique angle possible
   - Composite = (SEO × 0.3) + (CTR × 0.4) + (Fit × 0.3)
5. **Generate 2-3 evergreen topics** in addition to hot topics
6. **Present 10 topics**: 7-8 hot (sorted by score) + 2-3 evergreen

For each topic include: title suggestion, composite score, why trending, recommended angle, editorial stance, difficulty, SEO keywords.

### Guardrails

- Do not fabricate trending topics — all must be verifiable via WebSearch
- Do not score topics without checking actual search data
- Always check history for repetition

---

## Sub-skill: content-research

Use when the draft depends on current facts, product claims, pricing, release timelines, industry trends, or market comparisons.

Skip for purely personal essays or timeless opinion pieces.

### Modes

**`foundation`** — before drafting. Establishes: factual boundaries, concept boundaries, chronology, what is safe to state as fact vs author interpretation.

**`outline-targeted`** — after outline is approved. Maps: section → supporting sources, fact statements → safe wording, interpretation statements → author framing, claims requiring explicit uncertainty.

**`seo-intent`** — for SEO blog projects. Identifies: dominant search intent, top SERP summaries, content gaps, must-answer sub-questions, keyword variants.

### Workflow

1. Confirm: exact topic, what needs verification, publication date sensitivity, fact vs interpretation vs opinion split, which mode
2. Gather sources — prioritize: official docs, primary announcements, reputable reporting, high-signal community discussion
3. Separate fact / interpretation / opinion / open question for each major point. Note safe wording and risky wording.
4. Save findings:
   - `research/research-YYYY-MM-DD.md` (foundation)
   - `research/research-outline-YYYY-MM-DD.md` (outline-targeted)
   - `research/research-seo-intent-YYYY-MM-DD.md` (seo-intent)
   - `research/sources.md`

### Guardrails

- Do not fabricate or round up evidence
- Do not merge opinion and fact into one statement
- Do not use unsourced numbers as if verified
- Flag stale or uncertain claims explicitly

---

## Sub-skill: content-drafting

Use when a validated brief exists and any required research is complete.

### AI Role Boundaries

Clarify division of labor before drafting begins.

**AI擅长做的（放心交给AI）**
- 查找支撑论点的证据、数据、案例
- 寻找跨领域类比和比喻
- 在作者确认的角度基础上扩展细节
- 补充学术背景、历史脉络、概念解释
- 提出结构调整建议、衔接过渡

**AI做了会暴露的（必须作者来）**
- 第一视角的亲身观察和真实经历
- 核心创意角度的决策（选哪个切入点）
- 真实情绪的表达（"我当时就愣住了" vs "我当时很震撼"）
- 基于共情的人物刻画（从数据点还原真实人物）
- 文化/哲学升华的那一跳（感觉是发现，不是插入）

**理想协作流程**

```
作者提供：素材 + 核心观点 + 亲身经历 + 情绪节点
    ↓
AI补充：背景知识 + 证据 + 结构建议 + 初稿框架
    ↓
作者改写：注入自己的声音、真实细节、情绪颗粒度
    ↓
AI检查：四层质量关 (Step 8a)
```

If the author has not provided first-person material or a core angle, prompt before drafting: "在开始写之前，能分享一下你对这个话题的亲身经历或最强烈的个人判断吗？这会决定文章是否有真实的作者声音。"

### Workflow

1. **Inspect the brief** — confirm: audience, goal, language mode, platform, primary subject, target length, editorial stance, unique angle, competitive gap

2. **Propose directions first** — generate 2-4 candidate directions, each with: working title, core angle, target reader, outline, estimated effort, platform fit, opening approach, whether primary subject appears immediately or is delayed. Do not draft the full article until a direction is chosen.

3. **Build the outline** — once direction is selected. For SEO: preserve heading hierarchy, map keywords naturally. For WeChat: favor momentum and viewpoint, surface main subject early.

4. **Randomize dimensions** (to avoid article homogeneity) — activate 2-3 from:

   | Dimension | Options |
   |-----------|---------|
   | Narrative perspective | First-person / Observer analysis / Dialogue / Self-Q&A |
   | Timeline | Chronological / Reverse / Flashback / Non-linear |
   | Analogy domain | Sports / Cooking / Military / Gaming / Film / Architecture |
   | Emotional baseline | Restrained / Passionate / Satirical / Warm / Anxious |
   | Rhythm | Dense short sentences / Slow narrative / Alternating / Slow-start-fast-finish |

   Check `meta/project-history.yaml` last 3 projects' `dimensions` field — avoid exact same combination.

5. **Check style library** — if `meta/style-library/index.yaml` exists, load exemplars matching the current editorial stance, extract sample segments (opening hook, emotional peak, transition, closing), inject as style examples into the draft.

6. **Draft** — Chinese: direct and readable, avoid official tone. English: write naturally, do not mirror Chinese syntax. Bilingual: separate drafts from same brief, not sentence-by-sentence translation.

7. **Insert editorial anchors** — place 2-3 comments at: after opening hook, before core judgment, before closing summary. Format: `<!-- ✏️ 编辑建议：在这里加一句你自己的经历/看法 -->`

8. **Quick self-check** after drafting — fix immediately:
   - Forbidden phrases from brief's banned list
   - Sentence length variance (3+ consecutive same-length sentences → break up)
   - Opening hook: do first 3 sentences create suspense, conflict, or curiosity?
   - Core argument penetration: does main point appear in multiple sections?
   - Quotable moment: is there at least 1 sentence that can be screenshot and shared?

9. **Save** — archive prior version before overwriting: rename `draft-zh.md` → `draft-zh-v{N}.md`. Save to `drafting/draft-zh.md` / `drafting/draft-en.md`.

### Guardrails

- Do not skip direction proposal unless user explicitly chose a direction first
- Do not bury the article's named subject too deep when platform expects earlier framing
- Do not invent sourced facts not in the brief or research
- Do not collapse bilingual output into sentence-by-sentence translation

---

## Sub-skill: content-polishing

Use when a draft exists and needs factual, structural, and editorial review before humanizing.

### Workflow

Run these passes in order:

**Pass 1 — Factual and structural review:**
- factual consistency, source alignment, missing evidence, contradictory statements
- weak ordering, repetitive sections, missing transitions
- whether main subject appears early enough
- whether interpretation is phrased as sourced fact
- title-body consistency: does the article deliver what the title promises?
- ending completion: does the article reach a genuine conclusion or just stop?

**Pass 2 — Editorial review:**
- paragraph clarity, sentence burden, information density pacing
- tone consistency, whether examples earn their space
- prose rhythm: are sentence lengths varied?
- whether key judgments are set up with short clear sentences before and after

**Pass 3 — Platform fit:**
- WeChat: readable paragraph rhythm, narrative momentum
- SEO: heading hierarchy intact, scannability preserved, CTA aligned with search intent
- Xiaohongshu adaptation drafts: spoken cadence, stronger hook potential, shorter unit length

**Pass 4 — Quality Gate:** (see Step 8a in main workflow)

**Pass 5 — Save review notes** to `polish/review-notes.md`: major issues / smaller edits / unresolved questions / recommended next step.

### Guardrails

- Do not rewrite into a new angle here
- Do not humanize before structural issues are fixed
- Do not remove SEO-critical structure during review
- Do not skip writing `polish/review-notes.md`

---

## Sub-skill: content-humanizing

Use after editorial polishing, not before. Reduces visible AI-writing patterns and amplifies the author's distinctive voice.

### Inputs

- draft file path, language (`zh` or `en`), platform (`wechat` / `seo-blog` / `xiaohongshu`)
- optional: strength (`light` / `medium` / `aggressive`), banned phrases list

### Core rule

Humanize the expression. Do not alter the facts. Always preserve: source-backed claims, numbers/dates/names/quotes, heading hierarchy, keyword placement for SEO, the author's core position.

### Workflow

1. **Detect dominant failure mode**: inflated abstraction / formulaic transitions / repetitive contrast patterns / fake neutrality / bland conclusions / voice absence / Chinese AI public-account tone / English generic LLM essay tone

2. **Apply language-specific rules:**

   Chinese — remove: empty trend framing, official/promo tone, repetitive rhetorical symmetry, abstract evaluation. Watch for: "在当下这个时代" / "值得注意的是" / "不难发现" / "从某种意义上说"

   English — remove: generic AI essay phrases, over-signposted transitions, polished vagueness. Watch for: "in today's fast-paced landscape" / "it is important to note that" / repeated "not just X, but Y"

3. **Apply platform-specific rules:**
   - WeChat: preserve depth, allow stronger viewpoint, keep readable flow
   - SEO blog: preserve H1/H2/H3 structure, frontmatter, keyword strategy
   - Xiaohongshu: strengthen opening hook, shorten paragraphs, increase spoken cadence, remove lecture tone

4. **Voice amplification pass** — after reducing AI patterns, check: is there at least one moment where the author's analytical frame is unmistakable? Are there places where the writing is "safe" when the brief supports a stronger stance? Does the conclusion land with the author's actual view?

5. **Preservation pass** — verify: facts unchanged, structure valid, meaning unchanged, SEO constraints hold.

6. **Save** to `polish/humanized-zh.md` or `polish/humanized-en.md`. Do not overwrite the source draft.

### Strength levels

- `light`: small cleanup, draft is already strong
- `medium`: default, solid but visibly templated
- `aggressive`: structure is sound but voice still feels heavily generated — run extra preservation check afterward

### Guardrails

- Do not introduce new facts or examples
- Do not change the article's core claim
- Do not delete necessary SEO terms
- Do not confuse "human" with "dramatic" or "sloppy"

---

## Sub-skill: content-repurpose

Use when a finished article needs to be adapted into platform-specific outputs.

### Workflow

1. **Identify source type**: WeChat long-form / SEO blog / humanized final draft / bilingual pair
2. **Identify target output**: `distribution/wechat-article.md` / `distribution/seo-blog-zh.md` / `distribution/seo-blog-en.md` / `distribution/xiaohongshu-post.md`
3. **Adapt by platform:**

   **WeChat:**
   - keep article complete, preserve depth and readable pacing
   - shorter paragraphs if needed, emphasis formatting only where it improves scanability
   - make opening enter main subject quickly
   - keep key judgment lines easy to screenshot or quote
   - end with a topic-specific engagement prompt (required, not optional): e.g., "你在用 Claude Code 时踩过什么坑？欢迎在评论区分享" — not generic "欢迎留言"

   **SEO:**
   - preserve structural scanability, frontmatter, keyword-safe headings and CTA

   **Xiaohongshu:**
   - open with stronger hook, shorter sections, spoken and immediate tone
   - include: 3-5 title options (at least one keyword-optimized), cover-title suggestion, hook block, card-by-card structure, comment prompt or CTA, 3-5 hashtag suggestions, first-comment suggestion if applicable
   - do not treat as a shortened WeChat article — repackage around hooks, rhythm, and card utility

4. **Save each version separately** — do not overwrite source draft
5. **Save distribution metadata** — `distribution/meta-{platform}.md` for each output (see Step 11 in main workflow for required fields)

### Guardrails

- Do not invent new claims during adaptation
- Do not flatten the argument into generic summary bullets
- Do not break SEO requirements when adapting to SEO outputs
- Do not output WeChat and Xiaohongshu in the same pacing style
- Do not skip titles, hooks, or card structure when adapting to Xiaohongshu

---

## Sub-skill: content-style-learning

Use to build and maintain a writing style library. Can be invoked independently at any time.

Three commands:

| Command | Action |
|---------|--------|
| `import exemplar` / `导入范文` | Import a published article and extract its style fingerprint |
| `learn my edits` / `学习我的修改` | Learn from user edits to an AI draft |
| `show style library` / `查看范文库` | Display current accumulated style patterns |

### Mode 1: Import Exemplar

1. Read the article — identify type (opinion/narrative/tutorial/analysis) and language
2. Extract style fingerprint:
   - Sentence-level: average length, variance, short/long ratio, typical openings
   - Paragraph-level: average length, rhythm pattern, transition types
   - Emotional markers: intensity words, rhetorical devices (metaphor, repetition, contrast)
   - Structural patterns: opening hook style, closing style, transition phrases
   - Voice markers: first/second/third person ratio, recurring phrases, vocabulary temperature
3. Save to `meta/style-library/exemplars/{slug}.md` with frontmatter (title, category, language, date, fingerprint fields) and sample sections (opening hook, emotional peak, transition, closing)
4. Update `meta/style-library/index.yaml`

### Mode 2: Learn from Edits

1. Locate the edited draft in `drafting/` or `polish/`
2. Compare original vs edited — identify changes in: sentence structure, word choice, tone, paragraph reordering
3. Categorize edit patterns: sentence simplification / tone shift / voice injection / specificity increase / emotional amplification / structural reorganization
4. Append to `meta/style-library/edit-history.yaml`
5. Merge patterns into `meta/style-library/preferences.yaml`

Only extract patterns that appear 2+ times.

### Mode 3: Show Style Library

Read `meta/style-library/index.yaml` and display: total exemplars, breakdown by category and language, top 3-5 exemplars with fingerprint summaries.

### Integration with drafting

When `content-drafting` runs, it automatically checks for `meta/style-library/index.yaml` and injects matching exemplar samples as style examples. The more exemplars imported, the closer future drafts will match the author's voice.

### Guardrails

- Do not modify original exemplar articles
- Do not invent style patterns not present in the source material
- Do not override explicit brief requirements with learned preferences
- Respect language boundaries — do not mix zh/en style patterns
