---
name: premium-tool-page
description: Use when the user provides a keyword and wants to build a V2.0 premium tool page (tool + landing page + results display merged into one URL). Outputs keyword analysis, page strategy, and either filled template code or a Stitch design brief.
---

# Premium Tool Page

Build a V2.0 premium tool page from a single keyword.

The V2.0 model merges tool, landing page content, and results display into one URL — no separate app subdomain, no CTA button jumping to another page. Read [references/v2-page-structure.md](references/v2-page-structure.md) before starting.

## Trigger

Use this skill when the user provides a keyword and wants to:
- Build a tool page that ranks for that keyword
- Create a single-page tool site
- Follow the 精品工具页面 (premium tool page) SEO strategy

## Workflow

```
Step 1: Collect keyword data
Step 2: Generate page strategy
Step 3: User chooses output path (template code or Stitch)
```

---

## Step 1: Collect Keyword Data

Ask the user which data sources to use. This is a **multi-select** — they can choose one or more.

Present the options:

> Which data sources do you want to use for keyword analysis? (choose one or more)
>
> **A — I'll provide the data myself**
> Output the template from [assets/keyword-data-template.md](assets/keyword-data-template.md) and ask the user to fill it in.
>
> **B — Use WebSearch**
> Search the keyword. Analyze SERP structure: top 10 page types, whether a Featured Snippet or PAA box exists, competitor H1 patterns, and what the dominant page format is (tool / blog / product page / directory).
> Note clearly: WebSearch cannot provide accurate search volume or CPC. It provides SERP structure only.
>
> **C — API (user provides key)**
> Ask which service: Ahrefs, SEMrush, or Google Keyword Planner.
> Ask for the API key.
> Fetch: monthly search volume, competition level, CPC, and top related keywords.

If the user selects multiple sources, merge the data. API data takes precedence over WebSearch estimates. User-provided data takes precedence over everything.

Once data is collected, output a **long-tail keyword suggestions list** (5–8 variants) based on the data. Ask the user to confirm the final target keyword before proceeding.

---

## Step 2: Generate Page Strategy

Fill [assets/page-strategy-template.md](assets/page-strategy-template.md) using the confirmed keyword and collected data.

Do not invent data. If a field has no data source, mark it as `[not available]`.

The strategy covers:
- SEO copy: H1 variants, meta title, meta description, section headings, FAQ questions
- Layout: template type recommendation (A or B), tool input type, results display layout
- Front/back split: what logged-out vs logged-in users see
- Internal link strategy: outbound and inbound recommendations
- Style direction: recommended style and color direction

**Template type selection guide:**
- **Template A (tool-first)**: text input → inline text/code output. Use for writing tools, code generators, converters, analyzers.
- **Template B (gallery)**: file upload or prompt → visual output in a grid. Use for image generators, audio tools, video tools, design tools.

Present the completed strategy to the user and ask for confirmation before proceeding to Step 3.

---

## Step 3: Choose Output Path

Ask the user:

> How do you want to proceed?
>
> **A — Generate template code**
> Fill the chosen HTML template with the page strategy content. Output ready-to-use code.
>
> **B — Enter Stitch design**
> Pass the page strategy to `stitch-design-brief` as input. Generate a Stitch brief and generation prompt.

### Path A: Generate Template Code

1. Confirm which template the user wants: A (tool-first) or B (gallery).
2. Ask if they have a custom `theme.css`. If yes, ask them to paste it. If no, use the default theme from the template.
3. Read the chosen template from `assets/template-a/index.html` or `assets/template-b/index.html`.
4. Replace every `{{PLACEHOLDER}}` with the corresponding value from the page strategy.
   - Use the confirmed keyword, H1, meta title, meta description, section headings, FAQ questions and answers, internal link targets, and example content from the strategy.
   - For tool-specific placeholders (`{{TOOL_INPUT_LABEL}}`, `{{SUBMIT_BUTTON_LABEL}}`, etc.), infer sensible values from the keyword and tool type.
   - Leave `{{CANONICAL_URL}}`, `{{YEAR}}`, and `{{SITE_NAME}}` as clearly marked TODOs if the user has not provided them.
5. If the user provided a custom `theme.css`, output it separately with instructions to replace the default file.
6. Output the complete filled HTML. Add a short note at the top listing the TODOs that still need the user's input (API integration, auth check, canonical URL, site name).

### Path B: Stitch Design

Invoke the `stitch-design-brief` skill. Pass the completed page strategy document as the source material input.

---

## Rules

- Never invent keyword data. If data is missing, say so.
- WebSearch is for SERP structure analysis only — never present WebSearch results as search volume figures.
- The page structure is fixed (V2.0 model). Do not propose alternative structures.
- Always recommend the front/back split pattern (same URL, different content by login state).
- Do not skip the strategy confirmation step before generating code.
- Keep one target keyword per page. If the user provides multiple keywords, ask them to pick one for this page and note the others as candidates for future pages.
