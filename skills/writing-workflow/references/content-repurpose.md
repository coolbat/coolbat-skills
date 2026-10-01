## Sub-skill: content-repurpose

Use when a finished article needs to be adapted into platform-specific outputs.

### Workflow

1. **Identify source type**: WeChat long-form / SEO blog / humanized final draft / bilingual pair
2. **Identify target output**: `distribution/wechat-article.md` / `distribution/seo-blog-zh.md` / `distribution/seo-blog-en.md` / `distribution/xiaohongshu-post.md`
3. **Adapt by platform:**

   **WeChat:**
   - keep article complete, preserve depth and readable pacing
   - shorter paragraphs if needed, emphasis formatting only where it improves scanability
   - make opening enter main subject quickly
   - keep key judgment lines easy to screenshot or quote
   - end with a topic-specific engagement prompt (required, not optional): e.g., "你在用 Claude Code 时踩过什么坑？欢迎在评论区分享" — not generic "欢迎留言"

   **SEO:**
   - preserve structural scanability, frontmatter, keyword-safe headings and CTA

   **Xiaohongshu:**
   - open with stronger hook, shorter sections, spoken and immediate tone
   - include: 3-5 title options (at least one keyword-optimized), cover-title suggestion, hook block, card-by-card structure, comment prompt or CTA, 3-5 hashtag suggestions, first-comment suggestion if applicable
   - do not treat as a shortened WeChat article — repackage around hooks, rhythm, and card utility

4. **Save each version separately** — do not overwrite source draft
5. **Save distribution metadata** — `distribution/meta-{platform}.md` for each output (see Step 11 in main workflow for required fields)

### Guardrails

- Do not invent new claims during adaptation
- Do not flatten the argument into generic summary bullets
- Do not break SEO requirements when adapting to SEO outputs
- Do not output WeChat and Xiaohongshu in the same pacing style
- Do not skip titles, hooks, or card structure when adapting to Xiaohongshu

---

