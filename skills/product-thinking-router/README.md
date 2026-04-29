# Product Thinking Router

[English](#english) | [中文](#中文)

---

## English

### What is this?

Product Thinking Router is a skill that helps you choose the right product framework for your current problem. It diagnoses your real problem type, recommends 1–3 frameworks, applies them to your situation, and gives you a practical template and clear next action.

### Supported Frameworks (12)

JTBD, Kano Model, RICE, ICE, MoSCoW, Lean Canvas, North Star Metric, AARRR, HEART, 5 Whys, User Journey Map, Assumption Tree

### How to Use

Ask your product question in English or Chinese — the skill detects language automatically:
- "Should we build this feature?"
- "Growth is slowing. Where should I look first?"
- "How do I prioritize backlog?"
- "What should our North Star Metric be?"

### Directory Structure

```
product-thinking-router/
├── SKILL.md
├── README.md
├── en/                    # English version
│   ├── router.md
│   ├── scenarios.md
│   ├── output-template.md
│   └── frameworks/        # 12 framework cards
├── zh/                    # Chinese version
│   ├── router.md
│   ├── scenarios.md
│   ├── output-template.md
│   └── frameworks/        # 12 framework cards
└── examples/
    ├── en/
    └── zh/
```

---

## 中文

> 输入一个产品问题，自动识别问题类型，匹配最合适的思维框架，并输出可执行的分析过程、模板与下一步建议。

---

## 这是什么？

Product Thinking Router 是一个产品思维路由 skill，帮助产品经理、独立开发者和创业者在面对产品问题时：

1. **快速诊断问题类型**：这是需求判断、优先级排序、增长诊断，还是指标设计？
2. **选择合适的框架**：推荐 1~3 个最适合的思维框架，而不是罗列所有方法论
3. **直接应用到具体问题**：不只是解释概念，而是给出可填写的模板和下一步行动

---

## 它不是什么？

- ❌ 不是产品框架百科全书
- ❌ 不是方法论导航站
- ❌ 不是只会解释概念的工具

它是：

- ✅ 产品问题诊断器
- ✅ 框架匹配器
- ✅ 可直接执行的产品分析助手

---

## 核心价值

### 传统方式的问题

当你遇到产品问题时，通常需要：
1. 回忆或搜索相关框架
2. 判断哪个框架适用
3. 学习框架的使用方法
4. 自己套用到具体问题

这个过程耗时、容易选错框架、容易误用。

### Product Thinking Router 的方式

1. 输入你的产品问题
2. 自动诊断问题类型
3. 推荐最合适的 1~3 个框架
4. 直接给出可填写的模板
5. 明确下一步行动

---

## 适用场景

### 高频问题类型

- 这个功能要不要做？
- 用户一直提这个需求，怎么判断？
- 增长停滞了，先查哪里？
- 一堆需求怎么排优先级？
- 怎么定北极星指标？
- 新产品方向太模糊，用什么框架？
- 竞品上了这个功能，我要不要跟？
- 上线后效果一般，怎么复盘？
- 为什么留存差？
- MVP 应该保留什么？

### 适用人群

- 产品经理
- 独立开发者
- AI 产品经理
- 创业者
- 需要经常做需求判断、增长分析、优先级排序、指标设计的人

---

## 框架库

当前支持 12 个核心框架：

### 方向判断
- **JTBD**：理解用户真实动机
- **Kano**：判断功能满意度类型
- **Lean Canvas**：0→1 方向梳理
- **Assumption Tree**：识别关键假设

### 优先级排序
- **RICE**：结构化打分排序
- **ICE**：快速粗排
- **MoSCoW**：范围收敛

### 诊断分析
- **AARRR**：增长漏斗诊断
- **5 Whys**：根因追踪
- **Journey Map**：体验摩擦定位

### 指标设计
- **North Star Metric**：价值指标对齐
- **HEART**：体验指标体系

---

## 使用示例

### 示例 1：需求判断

**输入**：
> 用户一直在反馈希望增加"深色模式"功能，要不要做？

**输出**：
1. 问题诊断：这是一个"需求真实性 + 优先级"问题
2. 推荐框架：JTBD + Kano + RICE
3. 为什么选这些：JTBD 理解真实动机，Kano 判断满意度类型，RICE 排优先级
4. 套用到当前问题：[具体分析步骤]
5. 可填写模板：[JTBD + Kano + RICE 模板]
6. 下一步建议：先做 5~10 个用户访谈，确认真实使用场景
7. 误用提醒：不要把"提及次数多"直接等同于"优先级高"

### 示例 2：增长诊断

**输入**：
> 我们的产品注册数还在涨，但活跃用户数几乎不动，问题出在哪里？

**输出**：
1. 问题诊断：这是一个"增长诊断 + 漏斗断点定位"问题
2. 推荐框架：AARRR + Journey Map + 5 Whys
3. 为什么选这些：AARRR 定位断点，Journey Map 找摩擦点，5 Whys 挖根因
4. 套用到当前问题：[具体分析步骤]
5. 可填写模板：[AARRR + Journey Map + 5 Whys 模板]
6. 下一步建议：先看激活率数据，定位具体流失环节
7. 误用提醒：不要默认问题在获客，很多产品问题在激活或留存

---

## 文件结构

```
product-thinking-router/
├── README.md                    # 本文件（双语）
├── SKILL.md                     # Skill 定义（含语言检测逻辑）
├── en/                          # 英文版本
│   ├── router.md
│   ├── scenarios.md
│   ├── output-template.md
│   └── frameworks/              # 12 个框架卡（英文）
├── zh/                          # 中文版本
│   ├── router.md
│   ├── scenarios.md
│   ├── output-template.md
│   └── frameworks/              # 12 个框架卡（中文）
└── examples/                    # 示例
    ├── en/                      # 英文示例
    └── zh/                      # 中文示例
```

---

## 核心原则

### 1. 永远先解决问题，再调用框架

不要先推荐框架，再解释它"恰好"适用。而是先诊断问题类型，再选择最合适的框架。

### 2. 最小必要框架集

- 1 个框架：问题明确且单一
- 2 个框架：需要两个互补视角
- 3 个框架：需要完整链路（诊断 → 决策 → 度量）

不要默认给 3 个，不要超过 3 个。

### 3. 直接应用，不只是解释

不要只给框架定义，要直接把框架应用到用户的具体问题，给出可填写的模板。

### 4. 明确下一步行动

每次回答都必须给出明确的下一步行动，而不是停留在概念解释。

### 5. 包含误用提醒

每次推荐框架时，必须说明当前场景最容易犯的错误，以及正确的使用边界。

---

## 输出结构

每次回答按以下 7 段结构输出：

1. **问题诊断**：这是什么类型的问题？真正需要做的决策是什么？
2. **推荐框架**：推荐 1~3 个框架
3. **为什么选这些**：逐个说明适用原因，以及为什么不选某个常见框架
4. **套用到当前问题**：直接应用到用户的具体问题
5. **可直接填写的模板**：输出 checklist / 表格 / 填空模板
6. **下一步建议**：明确用户下一步应该做什么
7. **误用提醒**：指出当前场景最容易犯的错误

---

## 快速开始

### 作为 Claude Code Skill 使用

1. 将本目录放入 Claude Code 的 skills 目录
2. 在对话中直接提问产品问题
3. Skill 会自动识别问题类型并推荐框架

### 作为参考文档使用

1. 查看 `scenarios.md` 找到你的问题类型
2. 阅读对应的框架卡（`frameworks/` 目录）
3. 参考示例（`examples/` 目录）

---

## 版本历史

| 版本 | 日期 | 变更说明 |
|------|------|---------|
| v2.0 | 2026-04-28 | 双语版本，12 个框架卡（中英文），新增 6 个框架 |
| v1.0 | 2026-04-27 | 初始版本，6 个核心框架（中文） |

---

## 贡献

欢迎贡献：
- 新的框架卡
- 新的示例
- 改进路由规则
- 补充场景映射

---

## License

MIT

---

## 联系

如有问题或建议，欢迎提 Issue。
