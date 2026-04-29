# writing-workflow

A structured skill bundle for long-form content production across WeChat, SEO blogs, and Xiaohongshu.

---

## Installation

### Quick Install (Recommended)

```bash
curl -sSL https://raw.githubusercontent.com/coolbat/coolbat-skills/main/skills/writing-workflow/install.sh | bash
```

This installs `writing-workflow` and all required sub-skills into `~/.claude/skills/`.

### Manual Install

```bash
git clone https://github.com/coolbat/coolbat-skills.git
cd coolbat-skills/skills/writing-workflow
./install.sh
```

### Options

```bash
./install.sh --dry-run   # preview what would be installed
./install.sh --help      # show usage
```

### Dependencies

This skill requires the following sub-skills in `~/.claude/skills/`:

- `content-briefing`
- `content-research`
- `content-drafting`
- `content-polishing`
- `content-humanizing`
- `content-repurpose`
- `content-style-learning`
- `content-topic-selection`

The install script handles all of these automatically. Re-running is safe — already-installed skills are skipped.

This is not a single prompt. It is a routed workflow system made of 8 skills that cover the full journey from brief to distributed content.

---

## What It Does

Takes a vague writing request and produces finished, platform-adapted content through a repeatable pipeline:

```text
request
  → resolve storage path
  → normalize brief
  → assess research risk
  → foundation research (if needed)
  → propose directions
  → approve outline
  → outline-targeted research (if needed)
  → draft
  → polish
  → humanize
  → cold-read check
  → repurpose for distribution
  → generate images (if needed)
  → retrospective + history tracking
```

Supported content types: WeChat long-form, SEO blog, bilingual, Xiaohongshu, existing article revision, humanizing-only pass.

---

## Skill Architecture

`writing-workflow` is the router. It calls the right sub-skill at each stage.

```
writing-workflow          ← main router (start here)
├── content-briefing      ← standardizes vague briefs
├── content-topic-selection ← generates topic candidates when no topic given
├── content-research      ← foundation / outline-targeted / SEO-intent modes
├── content-drafting      ← directions, outlines, full drafts
├── content-polishing     ← fact / structure / editorial review
├── content-humanizing    ← removes AI patterns, amplifies author voice
├── content-repurpose     ← adapts to WeChat / SEO / Xiaohongshu
└── content-style-learning ← builds a reusable style fingerprint over time
```

Each sub-skill has its own `SKILL.md`, templates, and references. You can use them independently or through the main workflow.

---

## Storage Path Configuration

Projects are saved to a configurable base path. Priority order:

| Priority | Method | Example |
|----------|--------|---------|
| 1 (highest) | Say it in the conversation | "Store this in `~/Documents/writing/`" |
| 2 | `.claude/settings.json` | See below |
| 3 (default) | Current working directory | `content-projects/` |

**Persistent configuration via `settings.json`:**

```json
{
  "writing-workflow": {
    "base_path": "/Users/yourname/Documents/writing-projects"
  }
}
```

Paths support `~` expansion. The skill creates the project directory if it doesn't exist.

See [`references/storage-path-configuration.md`](references/storage-path-configuration.md) for full details, examples, and migration guide.

---

## Project Directory Structure

Every project follows this layout under `{base_path}/{project-slug}/`:

```text
{project-slug}/
├── brief/
│   ├── brief.md
│   └── requirements.md
├── research/
│   ├── research-YYYY-MM-DD.md
│   ├── research-outline-YYYY-MM-DD.md
│   ├── research-seo-intent-YYYY-MM-DD.md
│   └── sources.md
├── drafting/
│   ├── outline-zh.md
│   ├── outline-en.md
│   ├── draft-zh.md          ← current draft
│   ├── draft-zh-v1.md       ← archived previous version
│   └── draft-en.md
├── polish/
│   ├── review-notes.md
│   ├── humanized-zh.md
│   └── humanized-en.md
├── distribution/
│   ├── wechat-article.md
│   ├── meta-wechat.md
│   ├── seo-blog-zh.md
│   ├── seo-blog-en.md
│   ├── meta-seo.md
│   ├── xiaohongshu-post.md
│   └── meta-xiaohongshu.md
├── assets/
│   ├── images/
│   │   └── NN-{type}-{slug}.png
│   └── image-prompts/
│       ├── NN-{type}-{slug}.md
│       └── index.md
└── meta/
    ├── project.json
    ├── retrospective.md
    ├── project-history.yaml
    └── style-library/
        ├── exemplars/
        ├── index.yaml
        ├── edit-history.yaml
        └── preferences.yaml
```

---

## Sub-Skill Reference

### content-briefing

Turns a vague writing request into a usable, structured brief.

**Captures:**
- project name, content type, editorial stance, language mode
- target audience, content goal, topic / working title
- primary subject, target length, tone
- unique angle, competitive gap

**Outputs:** `brief/brief.md`, `brief/requirements.md`, `meta/project.json`

---

### content-topic-selection

Generates topic candidates when the user hasn't decided what to write.

**Sources checked:** Weibo, Toutiao, Baidu, Zhihu, GitHub, Twitter/X, Reddit, Google Trends, HN

**Scoring dimensions:** SEO potential, click potential, audience fit

**Outputs:** 10 topic candidates (7–8 trending + 2–3 evergreen), with duplicate check against `project-history.yaml`

---

### content-research

Handles all research needs across three modes:

| Mode | When to use |
|------|-------------|
| `foundation` | Before drafting — establishes factual and conceptual boundaries |
| `outline-targeted` | After outline approval — supports specific sections with evidence |
| `seo-intent` | For SEO blogs — maps search intent and keyword safety |

**Every research output separates:** fact / interpretation / opinion — with source links and freshness notes.

**Outputs:** `research/research-YYYY-MM-DD.md`, `research/sources.md`

---

### content-drafting

Produces directions, outlines, and full drafts.

**Direction proposal (before full draft):** generates 2–4 candidate angles, each with working title, target reader, core angle, outline, expected effort, platform fit, and when the primary subject surfaces.

**Draft features:**
- dimension randomization across 5 pools (prevents repetitive structure)
- style library injection (if style fingerprints exist)
- editorial anchors at 2–3 positions (prompts for author's own input)
- 5-point self-check before saving

**Version archiving:** existing draft renamed to `draft-zh-v{N}.md` before overwrite.

---

### content-polishing

Four-stage review of an existing draft:

1. **Fact and structure** — consistency, source alignment, evidence, contradiction, ordering, repetition, transitions, topic surfacing timing, title-body fit, ending completeness
2. **Editorial** — paragraph clarity, sentence load, information density, tone consistency, example quality, prose rhythm
3. **Platform fit** — WeChat / SEO / Xiaohongshu specific checks
4. **Save** — review notes written to `polish/review-notes.md` (required, not optional)

---

### content-humanizing

Reduces AI writing patterns and amplifies the author's distinctive voice.

**Detects 6 failure modes:**
- inflated abstractions
- formulaic transitions
- repetitive contrasts
- false neutrality
- flat conclusions
- missing voice

**Language-specific rules:**
- Chinese: remove empty trend framing, reduce official register
- English: remove generic AI phrases, reduce over-signposted transitions

**Three intensity levels:** `light` / `medium` / `aggressive`

**Preservation rules:** facts, source-backed details, SEO structure, core argument are never altered.

**Outputs:** `polish/humanized-zh.md`, `polish/humanized-en.md`

---

### content-repurpose

Adapts the finished humanized article to platform-specific formats.

| Platform | Key rules |
|----------|-----------|
| **WeChat** | Full article, readable rhythm, selective bolding, container syntax support |
| **SEO blog** | Header hierarchy preserved, scannable, CTA-aligned, keyword-safe |
| **Xiaohongshu** | Strong opening hook, short sections, conversational rhythm, card structure, comment bait, hashtag suggestions |

Each platform output ships with a companion metadata file (`meta-{platform}.md`).

---

### content-style-learning

Builds a reusable style fingerprint from the author's own published writing.

**Three modes:**
- `import exemplar` — extract style fingerprint from a published article
- `learn from edits` — detect patterns from user corrections during drafting
- `show style library` — display what has been learned so far

**Style fingerprint captures:** sentence rhythm, paragraph rhythm, emotional expression, transition patterns, opening hooks, closing patterns, vocabulary temperature, personal voice markers

**Integration with drafting:** when a style library exists, `content-drafting` automatically injects matching exemplar excerpts and applies stored preferences as hard constraints.

---

## Research Risk System

Before drafting, the workflow sets two flags that determine whether research is needed:

**`timeliness_risk`** — mark `medium` or `high` if the draft involves:
- specific products, companies, models, prices, features, release dates
- timing language: "recent", "current", "this year", "latest"
- trend or market claims
- SEO guidance that may have changed

**`controversy_risk`** — mark `medium` or `high` if the draft involves:
- category definitions in flux
- product comparisons
- directional industry judgments
- claims about the future of a category
- statements likely to be challenged by informed readers

If either flag is `medium` or `high`, foundation research runs before any drafting begins.

---

## Image Generation

Triggered when the brief specifies `images required: yes` or when the user requests images at any step.

**Image types:** `infographic`, `scene`, `flowchart`, `comparison`, `framework`, `timeline`, `cover`, `xhs-card`

**Visual styles:** `minimal`, `notion`, `chalkboard`, `warm`, `bold`, `infographic-flat`, `editorial`

**Discipline:** every image prompt is written to `assets/image-prompts/NN-{type}-{slug}.md` and reviewed before any generation call.

**Reference image chain:** the first image (cover or hero) is generated without a reference, then used as `--ref` for all subsequent images to maintain visual consistency across the series.

---

## Data-Driven Optimization

After each project, the workflow appends an entry to `meta/project-history.yaml`:

```yaml
- date: "2026-04-03"
  project_slug: "my-article"
  content_scenario: "WeChat long-form"
  editorial_stance: "opinion-led"
  language_mode: "zh"
  research_mode: "foundation"
  word_count: 3200
  time_spent_minutes: 90
  bottleneck_step: "direction selection"
  style_library_used: true
  editorial_anchors_count: 3
  dimensions:
    - "opening: scene-setting"
    - "ending: call-to-reflection"
  performance:
    views: null
    shares: null
    read_completion_rate: null
    date_measured: null
```

When 5+ projects exist in history, the workflow reads this file at startup and surfaces 1–2 actionable insights — which editorial stances performed best, which research modes were fastest, common bottlenecks.

---

## Guardrails

- Do not draft before the brief is clear
- Do not bury the primary subject — surface it early unless user requests a delayed reveal
- Do not fabricate facts, numbers, quotes, or test results
- Do not present author interpretation as broad public consensus
- Do not humanize before polishing
- Do not destroy SEO structure in the humanizing pass
- Do not overwrite existing project files without checking the directory first
- Do not skip editorial stance classification
- Do not skip the cold-read check unless polishing explicitly resolved all four cold-read criteria
- Do not publish distribution outputs without their companion metadata files

---

## Checklist

```
□ Storage path resolved (conversation > settings.json > default)
□ Project directory created at resolved path
□ Project history checked for insights (if 5+ entries exist)
□ Request classified: content scenario + editorial stance + task shape
□ Brief complete (unique angle and competitive gap included)
□ Research risk assessed: timeliness_risk + controversy_risk
□ Foundation research done (if risk is medium or high)
□ SEO intent research done (if SEO blog)
□ Direction selected before full drafting
□ Outline approved
□ Outline-targeted research done (if needed)
□ Draft: facts, structure, rhythm, title-body fit, ending reviewed
□ Review notes saved to polish/review-notes.md
□ Cold-read check passed
□ Humanizing applied after polishing (voice amplification verified)
□ Images: prompt files written before any generation
□ Cover image spec: type / palette / rendering / text / mood
□ Reference image chain used for series consistency
□ XHS image series: layout × style assigned per card
□ Distribution outputs created (if requested)
□ Distribution metadata files written
□ Files saved in the correct project directory
□ Retrospective written to meta/retrospective.md
□ Project history updated in meta/project-history.yaml
```

---

## References

- [`references/case-study.md`](references/case-study.md) — end-to-end walkthrough of a real WeChat article project
- [`references/evolution-note-2026-03.md`](references/evolution-note-2026-03.md) — why the workflow rules were tightened and what broke in earlier versions
- [`references/storage-path-configuration.md`](references/storage-path-configuration.md) — full storage path configuration guide

---

## Related Skills in This Repo

| Skill | Description |
|-------|-------------|
| [`content-briefing`](../content-briefing/) | Standalone brief standardization |
| [`content-research`](../content-research/) | Standalone research in any mode |
| [`content-drafting`](../content-drafting/) | Standalone drafting from brief + research |
| [`content-polishing`](../content-polishing/) | Standalone editorial review |
| [`content-humanizing`](../content-humanizing/) | Standalone humanizing pass |
| [`content-repurpose`](../content-repurpose/) | Standalone platform adaptation |
| [`image-brief-generator`](../image-brief-generator/) | Standalone image brief and prompt generation |
