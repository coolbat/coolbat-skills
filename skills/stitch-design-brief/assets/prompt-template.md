# Stitch Brief Template

Use this template before generating a screen in Stitch.

## 1. Product

- Name:
- One-line positioning:

## 2. Audience

- Primary audience:
- Secondary audience:
- Usage context:

## 3. Goal

- Primary conversion:
- Secondary conversion:

## 3b. AI Product Workflow

Skip this section if the page is not for an AI product.

- Core workflow:
- User input type:
- System output type:
- Demo or preview expectation:
- Trust proof for output quality:
- What makes this AI tool different from adjacent tools:

## 4. Visual Direction

- Style keywords:
- Primary colors:
- Support colors:
- Avoid colors/styles:

## 5. SEO Direction

- Primary keyword/theme:
- Secondary search intents:
- Required H1:
- Important H2 topics:

## 6. Page Structure

For AI tool pages, prefer one believable hero demo or output preview over a long abstract feature list.

- Primary device target:
- Mobile-specific layout considerations:
- Hero:
- Trust/proof:
- Core sections:
- FAQ:
- Footer CTA:

## 6b. V2.0 Premium Tool Page Structure

Skip this section if the page is NOT a premium tool page (i.e. input did not come from `premium-tool-page` skill).

- Tool input type: [text / file upload / parameters / combination]
- Results display layout: [list / grid / masonry]
- Logged-out view: full landing page content visible + tool entry with usage limit notice
- Logged-in view: landing page content hidden, immersive tool interface
- Section order: Hero → Tool Area → Results Display → Landing Content → FAQ → Internal Links
- Note for Stitch: this page is interactive — the tool must be present and usable on the page itself, not behind a CTA button that jumps to another URL

## 6b. V2.0 Premium Tool Page Structure

Skip this section if the page is NOT a premium tool page (i.e. not coming from the `premium-tool-page` skill).

The V2.0 model merges tool, landing page content, and results display into one URL. The page must be interactive — no CTA button jumping to a separate tool page.

- Tool input type: [text input / file upload / parameters / combination]
- Results display layout: [list / grid / masonry]
- Logged-out view: full landing page content visible + tool entry with usage limit notice
- Logged-in view: landing page content hidden, immersive tool interface
- Fixed section order: Hero → Tool Area → Results Display → Landing Page Content → FAQ → Internal Links

When filling the Stitch generation prompt, describe the page as an interactive tool page, not a landing page. The hero must contain the tool entry point, not just a CTA button.

## 7. Messaging

- H1:
- Support copy:
- Primary CTA:
- Secondary CTA:

## 8. Offer / Value Exchange

- Core value delivered to user:
- Access model:
- Immediate vs. delayed value:
- Key trust barriers to address:

## 9. Anti-AI Constraints

- Do not use:
- Avoid layouts like:
- Avoid copy like:
- Do not overuse:

## Stitch Generation Prompt Skeleton

```text
Design a high-fidelity [device] page for [product].

Product positioning:
[one-line positioning]

Primary audience:
[primary audience]

Secondary audience:
[secondary audience]

Primary conversion goal:
[primary conversion]

[If AI product: include workflow block]
AI product workflow:
- Core workflow: [core workflow]
- User input type: [user input type]
- System output type: [system output type]
- Demo or preview expectation: [demo or preview expectation]
- Trust proof for output quality: [trust proof]

Brand tone:
[style keywords]

Visual direction:
[visual direction details]

SEO and copy requirements:
- Primary keyword/theme: [primary keyword/theme]
- Required H1: [required H1]
- Important H2 topics: [important H2 topics]
- Use natural human English and avoid keyword stuffing.

Page structure:
[hero and section instructions]

Business / offer:
[offer / value exchange details]

Critical anti-generic constraints:
[anti-AI constraints]
```
