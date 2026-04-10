# V2.0 Premium Tool Page Structure

Source: 哥飞小课堂 — 精品工具页面思路 & 落地页版本演进

## Core Formula

```
Tool Page + Landing Page + Results Display = Premium Tool Page
Premium Tool Page + Low-Competition Keyword = Ranking & Exposure
Ranking & Exposure + Strong User Behavior Data = Top Search Results
One Keyword = One Page
Unified Front/Back End + User Behavior Data = Concentrated Engagement on One URL
```

## What Makes V2.0 Different from V1.5

V1.5: Landing page and tool page are separate pages (or separate subdomains).
V2.0: All three — tool, landing page content, and results display — are merged into one URL.

The page must be **interactive**, not just a CTA button pointing elsewhere.

## Page Sections (Fixed Structure)

### 1. Hero
- One-sentence positioning (what the tool does, who it's for)
- Tool entry point: form, upload area, or input + parameters
- No CTA button that jumps to another page — the tool IS here

### 2. Tool Area
- The functional core of the page
- Input types: text input / file upload / parameter selection / combination
- Output: displayed inline on the same page, not on a new URL

### 3. Results Display Area
- Shows curated or user-generated outputs from the tool
- Layout options: list / grid / masonry
- Default visibility: public (paid users can set private)
- Curation strategy: filter low-quality, filter policy violations, surface by engagement
- Do NOT show every result — use a selection algorithm or manual curation

### 4. Landing Page Content Area
- Written for the target keyword, backend-rendered for crawler access
- Covers: what the tool does, use cases, how it works, who it's for
- Keyword density: keep it natural; do not dilute with unrelated content
- If showing user-generated prompts alongside results, summarize them with AI rather than showing full text (avoids keyword dilution)

### 5. FAQ Section
- 5–8 questions targeting PAA and long-tail variants
- Each answer: 2–4 sentences, keyword-aware

### 6. Internal Links Section
- Link to related tool pages on the same domain
- Link to blog posts covering related topics
- Receive links from homepage and blog posts

## Front/Back End Unification

Same URL, different content based on login state:

- **Logged out**: Full landing page content visible + tool entry with usage limit notice
- **Logged in**: Landing page content hidden, immersive tool interface

Reference implementation: pollo.ai/video-effects/ai-kissing

## User Behavior Optimization Targets

```
Strong User Behavior = Low Bounce Rate + High Dwell Time + High Pages Per Session
```

Tactics:
- Tool is immediately usable without leaving the page (reduces bounce)
- Results display gives users something to browse (increases dwell time)
- Navigation and internal links encourage visiting related pages (increases pages/session)
- For tools with a processing step, show a loading/generating page — this can also carry ads

## UGC Page Strategy (for sites with user-generated content)

- Individual user-generated pages (e.g. per prompt): set `noindex`
- Create tag/category aggregation pages for keywords with search volume
- Each aggregation page: keyword-focused copy + filtered results list + tool entry
- This is the complete premium tool page pattern applied to UGC

## What to Avoid

- Launching mass pages on a new domain (new sites with mass pages will be penalized)
- Separate subdomains for tool vs. marketing site (splits user behavior data)
- Showing full user prompts in results lists (dilutes keyword density)
- CTA buttons that jump to a different URL to use the tool
- Duplicate or near-duplicate pages competing for the same keyword
