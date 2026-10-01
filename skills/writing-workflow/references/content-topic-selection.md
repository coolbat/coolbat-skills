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

