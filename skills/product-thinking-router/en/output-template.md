# Output Template

Use this structure in every response.

## Standard 6-Section Output

### 1. Problem Diagnosis
State what kind of product problem this really is and what decision is actually required.

### 2. Framework Recommendations + Rationale

**Format**:
```
### [Framework 1]
**Why it fits**: [1-2 sentences explaining match rationale, specific to current context]
**Core purpose**: [What problem this framework solves]

### [Framework 2] (if applicable)
**Why it fits**: ...
**Core purpose**: ...

**Why not [Common Framework X]**: [Explain boundaries, 1 sentence]
```

**Requirements**:
- Maximum 3 frameworks, listed in order of use
- Recommendations and rationale in the same section, not separated
- Must explain why NOT to use a common but unsuitable framework
- Rationale must be specific to current context, not generic

### 3. Apply to Current Question
Apply the frameworks directly to the user’s case.
Do not only define the frameworks.

### 4. Practical Template
Provide a fill-in template, checklist, or simple table.

### 5. Recommended Next Action
End with a next step the user can execute immediately.

### 6. Misuse Warning
State one likely mistake or one nearby framework that should not be the main tool here.

---

## Example skeleton

### 1. Problem Diagnosis
This is a ______ problem, not just a ______ problem.

### 2. Framework Recommendations + Rationale

### [Framework 1]
**Why it fits**: [specific to this case]
**Core purpose**: [what problem it solves]

**Why not [Common Framework X]**: [1 sentence]

### 3. Apply to Current Question
To analyze your case, answer:
1. ______
2. ______
3. ______

### 4. Practical Template
- Context:
- User goal:
- Friction / opportunity:
- Priority signal:
- Next hypothesis:

### 5. Recommended Next Action
Do ______ first, then ______.

### 6. Misuse Warning
Do not ______.

---

## Quick Mode Variants

### Brief Mode

Trigger words: "quick judgment", "brief"

**Output structure**:
1. Problem Diagnosis (1 sentence)
2. Recommended Framework (1 only)
3. Simplified Template
4. Next Action (1 sentence)

---

### Template-Only Mode

Trigger words: "just the template", "template only"

**Output structure**:
Skip diagnosis and explanation, directly output:
- Framework name
- Fill-in template
- Instructions (if needed)

---

### Compare Mode

Trigger words: "compare X and Y"

**Output structure**:
```
## [Framework X] vs [Framework Y]

### When to Use Each
- X fits when: ...
- Y fits when: ...

### Key Differences
| Dimension | X | Y |
|-----------|---|---|
| Purpose   | ... | ... |
| Input     | ... | ... |
| Output    | ... | ... |

### Recommendation
If [condition 1], use X.
If [condition 2], use Y.
```

---

## Clarification Mechanism

When the following conditions are met, use clarification mode instead of direct recommendation:

**Trigger conditions**:
- Question matches 2+ decision types and cannot be determined from context
- Question is too short (< 10 words) and lacks any background
- Product stage is completely unknown and stage significantly affects framework selection

**Clarification output structure**:
```
Your question could fall into one of these scenarios:

1. If it's [Scenario A] (e.g., [specific description]) → I would recommend [Framework X]
2. If it's [Scenario B] (e.g., [specific description]) → I would recommend [Framework Y]

Please provide the following information for more precise recommendations:
- [ ] Current product stage (0→1 / Early validation / Growth / Mature optimization)
- [ ] What decision ultimately needs to be made (whether to build / which to prioritize / find root cause)
- [ ] What data or background information is currently available

Or describe your specific situation directly, and I'll help you determine.
```

**Important**: Clarification is only triggered when confidence is low. If a reasonable assumption can be made, prefer assumption + annotation rather than excessive questioning that interrupts the user.

---

## Output Quality Checklist

Before every response, verify:

- [ ] Did you diagnose the problem type first, before recommending frameworks?
- [ ] Are there ≤ 3 frameworks recommended?
- [ ] Did you explain why NOT to use a common alternative framework?
- [ ] Recommendations and rationale in the same section, not separated?
- [ ] Did you apply the frameworks directly to the user's specific case, not just define them?
- [ ] Is the template immediately fillable?
- [ ] Is the next action specific and actionable?
- [ ] Is there a misuse warning?
- [ ] When information is insufficient: triggered clarification, or clearly annotated assumptions?

---

## Example Output

### Good Example

```markdown
### 1. Problem Diagnosis
This is a "requirement validity + prioritization" problem.

The real decision required: determine whether this requirement maps to a genuine user task, and whether it's worth investing resources now.

### 2. Framework Recommendations + Rationale

### JTBD
**Why it fits**: Helps identify the real task and motivation behind the user's feature request, preventing being misled by surface-level demands.
**Core purpose**: Identify users' true goals; distinguish surface requests from underlying jobs.

### Kano
**Why it fits**: Determines whether this feature is a basic, performance, or delight need — which directly affects prioritization.
**Core purpose**: Classify requirements and understand how different types affect user satisfaction.

### RICE
**Why it fits**: When resources are limited, provides a structured method to decide whether to act now.
**Core purpose**: Rank requirements by priority through quantified scoring.

**Why not Persona**: Persona describes who the user is, but cannot directly answer "is this requirement real" or "what's the priority."

### 3. Apply to Current Question
Answer these questions first:
1. In what context did the user raise this requirement?
2. How are they solving this without the feature today?
3. Would the absence of this feature directly cause dissatisfaction?
4. How many users does it affect? What's the implementation cost?

### 4. Practical Template
| Dimension | Content |
|-----------|---------|
| Trigger context | ______ |
| Real job | ______ |
| Current workaround | ______ |
| Kano category | ______ |
| Reach | ______ |
| Impact | ______ |
| Confidence | ______ |
| Effort | ______ |
| RICE score | ______ |

### 5. Recommended Next Action
Collect 5–10 real user samples to validate whether this is a high-frequency job, then run RICE scoring — don't commit to building it before that.

### 6. Misuse Warning
⚠️ Common mistake: treating "mentioned frequently" as equivalent to "high priority."

Correct approach: High mention frequency ≠ high value. Always validate with JTBD first, then use RICE to rank.
```

---

### Bad Example

```markdown
### Problem Analysis
This problem involves requirement management and product planning.

### Recommended Methods
You can use JTBD, Kano, RICE, ICE, MoSCoW, Lean Canvas, and other methods.

### Method Explanations
JTBD stands for Jobs to be Done, used to understand user needs...
Kano model was proposed by Japanese scholar Noriaki Kano...

### Suggestion
It's recommended to do user research first, then analyze data, then make decisions.
```

**Problems**:
- No explicit problem type diagnosis
- Recommends 6 frameworks
- Only definitions, not applied to the specific case
- No fillable template
- Suggestions are too vague
- No misuse warning
