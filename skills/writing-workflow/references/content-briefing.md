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

