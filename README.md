# coolbat-skills

A personal skill library for agentic workflows — writing, design, and product development.

Skills in this repo have been tested through real projects, not just drafted as prompt ideas.

---

## Skill Bundles

### Writing — `writing-workflow`

A full content production pipeline from brief to distributed output.

**适用场景：**
- 写微信公众号长文、SEO 博客、小红书帖子
- 有模糊写作需求，需要从选题→研究→起草→润色→分发走完整流程
- 需要管理多个内容项目，跟踪项目历史和写作风格
- 需要对已有文章进行改写、去 AI 化、或多平台改编

**工作流：**

```
brief
  → 研究风险评估
  → foundation research（如需）
  → 写作方向选择
  → 纲要确认
  → outline-targeted research（如需）
  → draft → polish → humanize
  → cold-read check
  → repurpose（多平台分发）
  → image briefs（如需）
  → 项目复盘 + 历史记录
```

**包含子技能：**

| Skill | 用途 |
|-------|------|
| `writing-workflow` | 主路由，从这里开始 |
| `content-briefing` | 把模糊需求变成结构化 brief |
| `content-topic-selection` | 没有选题时生成候选题目 |
| `content-research` | 多模式研究（foundation / outline-targeted / seo-intent） |
| `content-drafting` | 方向提案、纲要、起草 |
| `content-polishing` | 事实 / 结构 / 编辑 / 平台适配四阶段审稿 |
| `content-humanizing` | 去 AI 化，放大作者声音 |
| `content-repurpose` | 适配微信 / SEO / 小红书格式 |
| `content-style-learning` | 从作者已发布文章提取风格指纹 |

**安装：**

```bash
# 一键安装（推荐）
curl -sSL https://raw.githubusercontent.com/coolbat/coolbat-skills/main/skills/writing-workflow/install.sh | bash

# 本地安装
git clone https://github.com/coolbat/coolbat-skills.git
cd coolbat-skills/skills/writing-workflow
./install.sh

# 预览会安装什么
./install.sh --dry-run
```

安装脚本会把 `writing-workflow` 及所有子技能安装到 `~/.claude/skills/`，重复执行安全（已安装的跳过）。

安装后，在 Claude 中输入 `/writing-workflow` 启动。

---

### Design — `stitch-design-brief`

把 PRD、需求文档或页面策略转化为结构化 Stitch 生成提示词。

**适用场景：**
- 有 PRD 或需求文档，需要生成 Stitch prompt 才能开始设计
- 想减少 Stitch 输出"AI 感"和通用布局
- 对已有 Stitch 页面进行迭代，需要写 edit prompt
- 产品是 AI 工具 / SaaS / 自动化产品，需要把价值主张清晰展示而不是模糊描述
- 配合 `premium-tool-page` 使用：页面策略完成后直接进入 Stitch 设计节点

**工作流：**

```
PRD / brief / page strategy
  → 提取核心输入（定位 / 受众 / 转化目标 / 品牌调性 / SEO 意图）
  → 验证必要输入（受众不明或目标不明时停下追问）
  → 填写 brief 模板
  → 输出：结构化 brief + Stitch 生成提示词 + edit prompt（迭代时）
  → Stitch 生成后用 review checklist 检查
  → 用 edit prompts 定向修改（不重写整个 brief）
```

**安装：**

```bash
git clone https://github.com/coolbat/coolbat-skills.git
cp -r coolbat-skills/skills/stitch-design-brief ~/.claude/skills/
```

安装后，在 Claude 中输入 `/stitch-design-brief` 启动，或通过 `premium-tool-page` 自动调用。

---

### Product — `premium-tool-page`

从一个关键词，构建 V2.0 精品工具页面（工具 + 落地页 + 结果展示合并为单 URL）。

**适用场景：**
- 有目标关键词，想做一个能排名的工具页面
- 需要 SEO 策略 + 页面结构 + 代码模板一体化输出
- 工具类产品需要把工具本身和营销内容合并到同一个 URL

**V2.0 页面模型：** 工具、落地页内容、结果展示合并在同一 URL，无需跳转到子域名或另一个页面。支持前后端分离展示（同 URL，登录前后看到不同内容）。

**工作流：**

```
keyword
  → Step 1: 关键词数据收集
      选择数据来源：
      A — 用户自填（输出数据模板）
      B — WebSearch（分析 SERP 结构，不提供搜索量）
      C — API（Ahrefs / SEMrush / Google Keyword Planner）
  → 长尾词建议（5-8 个变体）→ 确认目标关键词
  → Step 2: 生成页面策略
      覆盖：SEO 文案 / 布局 / 模板类型 / 前后端分离 / 内链策略 / 视觉方向
  → 用户确认策略
  → Step 3: 选择输出路径
      A — 生成模板代码（Template A 工具型 / Template B 图库型）
      B — 进入 Stitch 设计节点（调用 stitch-design-brief）
```

**模板类型选择：**
- **Template A（工具优先）**：文字输入 → 内联文字/代码输出。适合写作工具、代码生成器、转换器、分析器。
- **Template B（图库型）**：文件上传或提示词 → 网格视觉输出。适合图像生成器、音频工具、视频工具、设计工具。

**安装：**

```bash
git clone https://github.com/coolbat/coolbat-skills.git
cp -r coolbat-skills/skills/premium-tool-page ~/.claude/skills/

# 如需同时使用 Stitch 设计节点，一并安装
cp -r coolbat-skills/skills/stitch-design-brief ~/.claude/skills/
```

安装后，在 Claude 中输入 `/premium-tool-page` 启动。

---

### Product — `product-thinking-router`

面对产品问题时，快速诊断问题类型、选出最合适的思维框架，并直接应用到具体情境。

**适用场景：**
- 不知道该用哪个产品框架，需要快速匹配
- 有具体产品问题（要不要做某功能、增长停滞了、需求怎么排优先级），需要可执行的分析过程和模板
- 想避免误用框架（如把 RICE 用于理解用户动机，把 AARRR 用于 UX 分析）
- 中英双语均支持，自动识别输入语言

**支持的 12 个框架：**

| 类别 | 框架 |
|------|------|
| 方向判断 | JTBD、Kano、Lean Canvas、Assumption Tree |
| 优先级排序 | RICE、ICE、MoSCoW |
| 诊断分析 | AARRR、5 Whys、Journey Map |
| 指标设计 | North Star Metric、HEART |

**输出结构（7 段）：**

```
1. 问题诊断：这是什么类型的问题？
2. 推荐框架：1~3 个（不超过 3 个）
3. 为什么选这些：包含"为什么不选某框架"的说明
4. 套用到当前问题：直接应用，不只是解释定义
5. 可直接填写的模板：checklist / 表格 / 填空
6. 下一步建议：明确的行动
7. 误用提醒：当前场景最容易犯的错误
```

**安装：**

```bash
git clone https://github.com/coolbat/coolbat-skills.git
cp -r coolbat-skills/skills/product-thinking-router ~/.claude/skills/
```

安装后，在 Claude 中输入 `/product-thinking-router` 启动，或直接提出产品问题触发路由。

---

## 组合使用

**内容生产全流程：**
```
/writing-workflow
```

**精品工具页（代码路径）：**
```
/premium-tool-page → 选择 Path A → 生成填充模板代码
```

**精品工具页（设计路径）：**
```
/premium-tool-page → 选择 Path B → /stitch-design-brief → Stitch 生成 → review → edit → 实现
```

**单独使用 Stitch 设计节点：**
```
PRD / 需求文档 → /stitch-design-brief → Stitch 生成
```

---

## Repository Layout

```
skills/
  writing-workflow/         ← 主路由 + 安装脚本
  content-briefing/
  content-research/
  content-drafting/
  content-polishing/
  content-humanizing/
  content-repurpose/
  content-style-learning/
  content-topic-selection/
  premium-tool-page/        ← 精品工具页构建
  stitch-design-brief/      ← Stitch 设计节点
  product-thinking-router/  ← 产品思维框架路由
```

---

## License

MIT
