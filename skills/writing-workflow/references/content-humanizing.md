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

   Chinese — remove: empty trend framing, official/promo tone, repetitive rhetorical symmetry, abstract evaluation. Watch for: "在当下这个时代" / "值得注意的是" / "不难发现" / "从某种意义上说" / "不是...而是..."（rewrite as plain declarative）

   Chinese AI-flavor rewrite patterns (from 2026-10 user feedback, treat as defaults):

   | AI 味写法 | 问题 | 改法 |
   |---|---|---|
   | "比X更反常的，是…" / "更值得玩味的是…" | 悬念腔，正常人不会这么起句 | 直接说那个细节："官宣第一段有个细节容易漏掉：…" |
   | "真正让我停下来的是…" / "真正让我在意的是…" | 表演式反应 | 直接给对比和数字："和上一代相比，提升幅度很明显：" |
   | "这场发布真正的头条，我认为是X" / "X才是主角" | 哗众取宠的断言 | "跑分之外，我更在意的是X。理由放到第N节再说。" |
   | "但它输掉的那5项，输得清清楚楚" | 戏剧化动词 | "另有5项落后，CWE-bench与Astra并列。" |
   | "——没人会逐行核对——" 破折号插入语 | 正文忌破折号 | 拆句："…消失，反正没几个人会逐行核对。但…" |
   | "为「长程agent」做担保——…唯一的证据链" | 过度比喻+破折号 | "全部发生在生产环境里，与跑分无关。…这些内部数据就承担了证明的责任。" |
   | "是能力，是诚实，是态度" 三连排比金句 | 排比堆砌 | 全篇至多一处，且必须压缩具体事实；否则改写成一句平实判断 |

   配套硬规则见 project-workflow.md Step 8a 的 L1（破折号/浮夸修辞/排比）与 L2（正常人测试）。

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

