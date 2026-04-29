---
name: content-topic-selection
description: Use when the user needs topic ideas for articles, or wants to generate topics based on current trends. Supports hot topic fetching, SEO scoring, and topic recommendation.
---

# Content Topic Selection

## Overview

This skill helps generate article topics by:
1. Fetching current hot topics from multiple platforms
2. Scoring topics by SEO potential and click-through rate
3. Filtering against recent article history to avoid repetition
4. Recommending 7-10 hot topics + 2-3 evergreen topics

## When to Use

Use this skill when:
- User says "give me topic ideas" / "帮我选题" / "有什么可以写的"
- User wants to write about current trends
- Starting a new writing project without a specific topic
- User asks "what's trending" / "今天有什么热点"

## Inputs

Required:
- User's content focus areas (from brief or direct input)

Optional:
- Target platform (WeChat / SEO blog / Xiaohongshu)
- Language mode (zh / en)
- Recent article history (to avoid repetition)

## Workflow

### 1. Fetch hot topics

Use `WebSearch` to gather trending topics from multiple sources:

**For Chinese content**:
- Weibo hot search: `site:s.weibo.com 热搜`
- Toutiao trends: `site:toutiao.com 热点`
- Baidu hot list: `百度热榜 今日`
- Zhihu hot questions: `site:zhihu.com 热门问题`
- GitHub Trending (Chinese): `site:github.com/trending 中文`

**For English content**:
- Twitter trending: `site:twitter.com trending`
- Reddit hot posts: `site:reddit.com hot`
- Google Trends: `google trends today`
- Hacker News: `site:news.ycombinator.com`
- GitHub Trending: `site:github.com/trending`

**For tech/developer content** (additional source):
- GitHub Trending by language: `site:github.com/trending/{language}` where language = python, javascript, go, rust, etc.
- GitHub Trending repositories: Extract repository names, descriptions, and star counts
- Focus on repos with rapid star growth (trending this week/month)

Collect 20-30 raw topics.

### 2. Filter by relevance

Match topics against user's content focus areas:
- Keep topics that overlap with user's domains
- Remove topics completely outside user's expertise
- Prioritize topics where user can add unique perspective

Narrow down to 15-20 relevant topics.

### 3. Check against history

If `meta/project-history.yaml` exists:
- Extract topics from the last 7 days
- Remove topics that are too similar to recent articles
- Deprioritize keywords already covered

This prevents repetitive content.

### 4. Score each topic

Evaluate on 3 dimensions (0-10 scale):

**A. SEO Potential** (for SEO blog / WeChat SEO):
- Search volume estimate (use `WebSearch` for "{topic} 搜索量" or check Google Trends)
- Keyword competition level
- Long-tail keyword opportunities
- Score: 0 (no search interest) to 10 (high volume, low competition)

**B. Click-Through Rate Potential**:
- Emotional trigger (curiosity, controversy, urgency, benefit)
- Specificity (vague vs concrete)
- Timeliness (breaking news vs evergreen)
- Score: 0 (boring) to 10 (irresistible)

**C. User Fit**:
- Matches user's expertise level
- Aligns with user's content style
- User can add unique angle
- Score: 0 (poor fit) to 10 (perfect fit)

**Composite Score** = (SEO × 0.3) + (CTR × 0.4) + (Fit × 0.3)

### 5. Generate evergreen topics

In addition to hot topics, generate 2-3 evergreen topics:
- Tutorial: "How to {solve common problem}"
- Comparison: "{Tool A} vs {Tool B}: Which is better?"
- List: "Top 10 {resources} for {audience}"
- Method: "The {framework} approach to {goal}"

Mark these as "Evergreen" to distinguish from hot topics.

### 6. Present recommendations

Output 10 topics total:
- 7-8 hot topics (sorted by composite score, highest first)
- 2-3 evergreen topics

For each topic, include:
- **Title suggestion** (20-28 characters)
- **Composite score** (0-10)
- **Why it's trending** (1 sentence for hot topics)
- **Recommended angle** (unique perspective user can take)
- **Recommended editorial stance** (opinion/evidence/narrative/tutorial)
- **Estimated difficulty** (easy/medium/hard)
- **SEO keywords** (3-5 keywords)

### 7. User selection

- **Auto mode**: Select the highest-scoring topic
- **Interactive mode**: Display all 10, let user choose

## Output Format

```markdown
# Topic Recommendations ({date})

## Hot Topics (7-8)

### 1. {Title Suggestion} [Score: 8.5/10]

**Why trending**: {1 sentence explanation}

**Recommended angle**: {unique perspective}

**Editorial stance**: Opinion-led

**Difficulty**: Medium

**SEO keywords**: keyword1, keyword2, keyword3

---

### 2. {Title Suggestion} [Score: 8.2/10]

...

## Evergreen Topics (2-3)

### 9. {Title Suggestion} [Evergreen]

**Why valuable**: {long-term relevance}

**Recommended angle**: {approach}

**Editorial stance**: Tutorial-led

**Difficulty**: Easy

**SEO keywords**: keyword1, keyword2, keyword3

---
```

## Integration with Writing Workflow

When `writing-workflow` Step 1 completes and no topic is specified:
1. Automatically invoke `content-topic-selection`
2. Present recommendations
3. User selects topic
4. Continue to Step 2 (research)

## Guardrails

- Do not fabricate trending topics — all must be verifiable via WebSearch
- Do not recommend topics completely outside user's expertise
- Do not ignore recent history — always check for repetition
- Do not score topics without checking actual search data
- Mark evergreen topics clearly to distinguish from time-sensitive hot topics

## Checklist

- [ ] Hot topics fetched from multiple sources
- [ ] Topics filtered by relevance to user's focus areas
- [ ] History checked for repetition (if exists)
- [ ] Each topic scored on 3 dimensions
- [ ] Evergreen topics generated
- [ ] Recommendations formatted and presented
- [ ] User selection captured (if interactive mode)

