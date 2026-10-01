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

