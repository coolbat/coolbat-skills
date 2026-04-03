---
name: writing-workflow
description: Use when handling long-form writing projects for WeChat articles, SEO blogs, bilingual content, or downstream repurposing into WeChat and Xiaohongshu formats
---

# Writing Workflow

## Overview

This skill is the router for structured writing projects.
It classifies the job, checks required inputs, routes work through the right sub-skills, and keeps the project artifacts organized.

For a concrete end-to-end example of this workflow, see:
- `references/case-study.md`

For why the workflow was tightened over time, see:
- `references/evolution-note-2026-03.md`

Supported scenarios:
- WeChat long-form
- SEO blog
- WeChat adaptation
- Xiaohongshu adaptation
- Existing article revision
- Humanizing only

## Project Structure

### Storage Path Configuration

The base storage path for writing projects can be configured in three ways (in priority order):

1. **User instruction in current conversation** - highest priority
   - "Store this project in `/path/to/my/articles/`"
   - "Use `~/Documents/writing/` as the base path"

2. **Settings configuration** - persistent across sessions
   - Add to `.claude/settings.json`:
   ```json
   {
     "writing-workflow": {
       "base_path": "/Users/username/Documents/writing-projects"
     }
   }
   ```

3. **Default fallback** - when no configuration exists
   - Uses `content-projects/` in the current working directory

### Project Directory Structure

Store each project under:

```text
{base_path}/{project-slug}/
```

Expected subdirectories:

```text
brief/
research/
drafting/
polish/
assets/
distribution/
meta/
```

**Path resolution logic:**
1. Check if user specified a path in the current conversation
2. If not, read `.claude/settings.json` for `writing-workflow.base_path`
3. If not configured, use `content-projects/` as default
4. Expand `~` to user home directory
5. Convert to absolute path
6. Create the full project directory if it doesn't exist

If the project folder does not exist, create it before continuing.

## Classification

Classify the request before drafting anything.

### Content Scenario
- WeChat long-form
- SEO blog
- WeChat adaptation
- Xiaohongshu adaptation
- Existing article revision
- Humanizing only

### Editorial Stance
- Opinion-led: the author has a clear judgment and argues for it
- Evidence-led: the argument follows the research
- Narrative-led: story or case study drives the piece
- Tutorial-led: practical instruction is the core value

### Task Shape
- New project with full brief
- New project with incomplete brief
- Draft from source materials
- Revise existing draft
- Repurpose final article
- Produce bilingual versions

Do not skip classification.

## Language Rules

Supported modes:
- Chinese only
- English only
- Bilingual

For bilingual work:
- use the same brief and research base
- produce separate audience-appropriate drafts
- do not default to sentence-by-sentence translation

## Workflow

### 0. Resolve storage path (required at start)

Before any file operations, resolve the base storage path:

1. **Check conversation context** - did the user specify a path?
   - "Store in `/Users/me/articles/`"
   - "Use `~/writing/` as base"
   - Extract and use that path

2. **Check settings.json** - if no path in conversation:
   ```bash
   # Read .claude/settings.json
   # Look for: writing-workflow.base_path
   ```

3. **Use default** - if no configuration found:
   ```text
   content-projects/
   ```

4. **Normalize the path**:
   - Expand `~` to home directory
   - Convert to absolute path
   - Remove trailing slashes
   - Verify parent directory exists (create if needed)

5. **Set project path**:
   ```text
   {resolved_base_path}/{project-slug}/
   ```

**Example resolution:**
- User says: "Store in `~/Documents/writing/`"
- Resolves to: `/Users/username/Documents/writing/{project-slug}/`

- Settings has: `"base_path": "/Users/me/articles"`
- Resolves to: `/Users/me/articles/{project-slug}/`

- No configuration
- Resolves to: `{cwd}/content-projects/{project-slug}/`

**Important**: Resolve this ONCE at the start and use consistently throughout the workflow.

### 1. Check project history for insights (optional, when history exists)

If `meta/project-history.yaml` exists and has 5+ entries:
1. Analyze past projects for patterns:
   - Best-performing editorial stance + scenario combinations
   - Fastest research modes
   - Impact of style library usage
   - Common bottlenecks
2. Share 1-2 actionable insights with the user before starting
3. Adjust workflow recommendations based on data

### 1. Standardize the brief

If the request is incomplete, use `content-briefing`.

If the user has not specified a topic, use `content-topic-selection` to generate recommendations.

Minimum fields:
- project name
- content type
- language mode
- target audience
- content goal
- topic or working title
- primary subject or main object of discussion
- target length
- whether research is required
- whether images are required
- whether repurposing is required

### 2. Assess research risk before drafting

Set two risk flags:
- `timeliness_risk`: `low`, `medium`, or `high`
- `controversy_risk`: `low`, `medium`, or `high`

Mark `timeliness_risk` as `medium` or `high` if the draft includes any of:
- specific products, companies, models, platforms, prices, features, or release dates
- recent timing language such as "recent", "current", "this year", "right now", "next phase", or "latest"
- trend or market claims
- SEO guidance that may have changed

Mark `controversy_risk` as `medium` or `high` if the draft includes any of:
- category definitions still in flux
- product comparisons
- directional industry judgments
- claims about what represents the future of a category
- statements likely to be challenged by informed readers

If either risk is `medium` or `high`, run `content-research` in `foundation` mode before drafting.

### 3. Run foundation research when needed

Use `content-research` in `foundation` mode to establish:
- factual boundaries
- concept boundaries
- source-backed chronology
- which statements can be written as facts
- which statements must remain author interpretation

Foundation research output must include:
- research date
- source links
- fact vs interpretation vs opinion separation
- freshness or risk notes

### 4. Propose directions first

Use `content-drafting` to generate 2-4 candidate directions before full drafting.

Each option should include:
- working title
- target reader
- core angle
- outline
- expected effort
- platform fit
- how early the primary subject appears

Wait for direction selection before writing the full draft.

### 5. Run outline-targeted research when needed

After the outline is approved, run `content-research` again in `outline-targeted` mode if the article includes:
- product or trend judgments tied to specific sections
- comparisons that need tighter evidence
- strong claims about what changed, what matters, or what a product represents

Use this second pass to map:
- section -> supporting sources
- fact statements -> safe wording
- interpretation statements -> author framing
- claims requiring explicit uncertainty

### 6. Draft the article

After a direction is selected, use `content-drafting` to create the draft.

Scenario emphasis:
- WeChat: clarity, viewpoint, narrative energy, readability
- SEO blog: search intent, heading structure, keyword safety, scannability
- English: write naturally for English readers
- Bilingual: create parallel drafts from the same brief

### 7. Polish the draft

Use `content-polishing` for factual, structural, and editorial review.

### 8. Humanize the draft

Use `content-humanizing` after polishing, not before.

Preserve:
- factual claims
- source-backed details
- SEO structure where required
- the core argument

### 9. Cold-read check

Before repurposing or distributing, perform a cold-read pass on the humanized draft.

Read as if you are a reader who knows nothing about the topic, then verify:
- Can you clearly state what the article is about after finishing it?
- Can you identify the author's core judgment or takeaway?
- Is there a reason given for why the reader should trust that judgment?
- Does the opening match what the article actually delivers?

If the answer to any of these is no, flag it and address it before distribution.

This step is lightweight for well-executed drafts. Skip it only if the polishing step already surfaced and resolved all of these issues.

### 10. Repurpose for distribution

If requested, use `content-repurpose` to create:
- WeChat article version
- SEO blog version
- Xiaohongshu version

### 11. Image generation (when images are required)

Triggered when the brief has `whether images are required: yes`, or when the user requests images during any step.

#### 11a. Classify image needs

For each image needed, determine:

**Image Type** (what it communicates):
| Type | Use When |
|------|----------|
| `infographic` | Statistics, data, multi-point summaries |
| `scene` | Atmosphere, metaphor, emotional resonance |
| `flowchart` | Process, decision logic, steps |
| `comparison` | Side-by-side contrast, before/after |
| `framework` | Mental models, matrices, named systems |
| `timeline` | Chronology, history, phases |
| `cover` | Article or post cover image |
| `xhs-card` | Xiaohongshu infographic card |

**Visual Style** (how it looks) — pick one that matches content tone:
- `minimal` — clean, sophisticated, whitespace-heavy
- `notion` — hand-drawn line art, intellectual
- `chalkboard` — colorful chalk, educational
- `warm` — cozy, approachable
- `bold` — high impact, attention-grabbing
- `infographic-flat` — flat icon style, data-forward
- `editorial` — magazine-quality, polished

#### 11b. Write prompt files before generating

**Prompt file discipline** (required): Write every image prompt to disk BEFORE calling any image generation tool.

Save prompt files under:
```text
assets/image-prompts/
  NN-{type}-{slug}.md
```

Each prompt file must include:
- Image type and purpose
- Visual style
- Content to convey (key points, data, text elements)
- Aspect ratio (e.g. 16:9 for blog hero, 1:1 for XHS, 3:4 for cover)
- Negative constraints (what to avoid)

Do not generate any image until its prompt file is saved and reviewed.

#### 11c. Generate images with baoyu-image-gen

Use the `baoyu-image-gen` skill for actual image generation.

**Visual consistency via reference image chain**:
1. Generate the first image (typically the cover or hero) without `--ref`
2. Use that first image as `--ref` for all subsequent images in the same article — this keeps fonts, color palette, and layout consistent across a series

**Cover image** — use 5-dimension specification:
- `type`: photo / illustration / abstract / typography / collage
- `palette`: warm / cool / monochrome / vibrant / earthy
- `rendering`: realistic / flat / 3D / painterly / line-art
- `text`: large-title / subtitle / minimal / none
- `mood`: energetic / calm / serious / playful / authoritative

Save generated images under:
```text
assets/images/
  NN-{type}-{slug}.png
```

Record the mapping in `assets/image-prompts/index.md`:
```text
| # | Type | Style | Prompt file | Output file | Section used |
```

#### 11d. XHS image series (when repurposing to Xiaohongshu)

When creating Xiaohongshu content, images are not optional — they are the primary medium.

Apply the **baoyu-xhs-images** layout × style approach:

**Layout** (information structure):
- `sparse` — 1-2 points, maximum visual impact (cover card)
- `balanced` — 3-4 points (standard content card)
- `dense` — 5-8 points (knowledge card)
- `list` — ranked or enumerated (4-7 items)
- `flow` — steps or timeline (3-6 steps)

**Style** (visual aesthetic):
- `cute` — classic XHS girly aesthetic
- `fresh` — clean, natural
- `minimal` — sophisticated
- `notion` — intellectual, hand-drawn

**Outline strategies**:
- **Story-Driven** (Strategy A): Personal experience as thread — for reviews, personal shares
- **Information-Dense** (Strategy B): Value-first, efficient — for tutorials, comparisons
- **Visual-First** (Strategy C): Visual impact core, minimal text — for lifestyle, aesthetics

Generate image prompts for the full XHS series (1-10 cards) before generating any image.
Use the reference image chain: generate card 1 first, then pass it as `--ref` to all remaining cards.

## Project Retrospective

After the project is complete, write `meta/retrospective.md` with:
- which step took the most time and why
- whether any guardrail was violated during the run
- whether the unique angle held up through drafting, or drifted
- if you were to redo this project, what would you change

This file is not a summary of what happened. It is a record of what was surprising or non-obvious. Skip entries that merely describe the normal flow.

**Extended tracking** (for data-driven optimization):

Also append to `meta/project-history.yaml` (create if not exists):

```yaml
- date: "{YYYY-MM-DD}"
  project_slug: "{slug}"
  content_scenario: "{WeChat long-form|SEO blog|etc}"
  editorial_stance: "{opinion-led|evidence-led|narrative-led|tutorial-led}"
  language_mode: "{zh|en|bilingual}"
  framework_used: "{if applicable}"
  research_mode: "{foundation|outline-targeted|seo-intent|none}"
  word_count: {number}
  time_spent_minutes: {estimate}
  bottleneck_step: "{which step took longest}"
  style_library_used: {true|false}
  editorial_anchors_count: {number}
  dimensions:
    - "{dimension}: {selected option}"
    - "{dimension}: {selected option}"
  
  # Optional: performance data (if available later)
  performance:
    views: {number or null}
    shares: {number or null}
    read_completion_rate: {percentage or null}
    date_measured: "{YYYY-MM-DD or null}"
```

**Data-driven recommendations** (when history has 5+ entries):

Before starting a new project, read `meta/project-history.yaml` and analyze:
1. Which `editorial_stance` + `content_scenario` combinations performed best (if performance data exists)
2. Which `research_mode` led to faster completion without quality issues
3. Whether `style_library_used: true` projects had better outcomes
4. Common bottleneck steps across projects

Use these insights to:
- Recommend proven combinations to the user
- Suggest process improvements
- Prioritize high-impact steps

## Guardrails

- Do not jump straight into a full article when the brief is unclear.
- Do not bury the primary subject too late in the article. If the piece is about a specific product, event, or controversy, surface it in the opening unless the user explicitly wants a delayed reveal.
- Do not fabricate facts, numbers, quotes, or test results.
- Do not present author interpretation as broad public consensus unless sourced.
- Do not treat humanizing as permission to change meaning.
- Do not destroy SEO structure merely to sound less like AI.
- Do not overwrite prior project files without checking the existing directory.

## Deliverables

Depending on scope, produce some or all of:
- `brief/brief.md`
- `research/research-YYYY-MM-DD.md`
- `research/research-outline-YYYY-MM-DD.md`
- `research/research-seo-intent-YYYY-MM-DD.md`
- `drafting/draft-zh.md`
- `drafting/draft-en.md`
- `polish/review-notes.md`
- `polish/humanized-zh.md`
- `polish/humanized-en.md`
- `distribution/wechat-article.md`
- `distribution/meta-wechat.md`
- `distribution/seo-blog-zh.md`
- `distribution/seo-blog-en.md`
- `distribution/meta-seo.md`
- `distribution/xiaohongshu-post.md`
- `distribution/meta-xiaohongshu.md`
- `assets/image-prompts/NN-{type}-{slug}.md`
- `assets/image-prompts/index.md`
- `assets/images/NN-{type}-{slug}.png`
- `meta/retrospective.md`
- `meta/project-history.yaml`

## Guardrails (additions)

- Do not skip editorial stance classification — it affects tone, structure, and the type of evidence needed.
- Do not skip the cold-read step unless polishing already resolved all four cold-read checks explicitly.
- Do not publish distribution outputs without their companion metadata files.

## Checklist

- [ ] Storage path resolved (conversation > settings.json > default)
- [ ] Project directory created at resolved path
- [ ] Project history analyzed for insights (if 5+ past projects exist)
- [ ] Project classified (scenario + editorial stance)
- [ ] Brief exists and is usable (including unique angle and competitive gap)
- [ ] Research risk assessed
- [ ] Foundation research completed if needed
- [ ] SEO intent research completed if SEO blog
- [ ] Direction selected before full drafting
- [ ] Outline-targeted research completed if needed
- [ ] Draft reviewed for facts, structure, rhythm, title-body fit, and ending
- [ ] Cold-read check passed
- [ ] Humanizing applied at the correct stage (voice amplification verified)
- [ ] Images required? → prompt files written before generation
- [ ] Cover image spec: type / palette / rendering / text / mood
- [ ] Reference image chain used for series consistency (image 1 as --ref for 2..N)
- [ ] XHS image series: layout × style assigned per card
- [ ] Distribution outputs created if requested
- [ ] Distribution metadata files written
- [ ] Files saved in the correct project directory
- [ ] Retrospective written to `meta/retrospective.md`
- [ ] Project history updated in `meta/project-history.yaml`
