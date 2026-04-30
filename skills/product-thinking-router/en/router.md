# Router Rules

## Purpose
Convert ambiguous product questions into the right analytical path.

## Rule 1: Identify the user’s actual decision
Do not respond to the surface wording only.
Translate the request into the real decision.

Examples:
- “Should we build X?” → discovery + prioritization
- “Growth is slowing” → funnel diagnosis
- “What metric should we use?” → value definition + measurement design
- “Competitor launched this” → competitive reaction + real user need check

## Rule 2: Categorize the problem

### A. Strategy
Typical prompts:
- Is this product direction valid?
- How do I structure a new product idea?
- Where should we start?

Recommended frameworks:
- Lean Canvas
- Assumption Tree
- JTBD

### B. Discovery
Typical prompts:
- Why do users want this?
- What problem are they actually trying to solve?
- Is this a real need or surface request?

Recommended frameworks:
- JTBD
- User Journey Map
- 5 Whys

### C. Prioritization
Typical prompts:
- Which feature should we do first?
- How do I rank these initiatives?
- How do I scope MVP or roadmap?

Recommended frameworks:
- RICE
- ICE
- MoSCoW
- Kano

### D. Growth
Typical prompts:
- Growth is slowing.
- Conversion is weak.
- Retention is dropping.

Recommended frameworks:
- AARRR
- User Journey Map
- 5 Whys

### E. Metrics
Typical prompts:
- What should our North Star Metric be?
- What should we measure?
- The team has too many goals; how do we simplify?

Recommended frameworks:
- North Star Metric
- HEART

### F. Experience
Typical prompts:
- Users say it feels hard to use.
- Onboarding is confusing.
- Why is activation weak even with traffic?

Recommended frameworks:
- User Journey Map
- HEART
- 5 Whys

### G. Review / Diagnosis
Typical prompts:
- We shipped it, but it underperformed.
- Why didn’t adoption happen?
- What’s the root cause?

Recommended frameworks:
- 5 Whys
- HEART
- AARRR
- User Journey Map

### H. Hypothesis Validation

Typical prompts:
- How do I quickly validate this idea?
- What should the MVP test?
- Which assumption is most dangerous?
- How do I design a small experiment?

Recommended frameworks:
- Lean Canvas (identify highest-risk assumption)
- Assumption Tree (structure and rank assumptions)

Typical combinations:
- Early MVP validation: Lean Canvas + Assumption Tree
- Quick experiment design: Assumption Tree + ICE

When to use:
- 0→1 stage with high uncertainty
- Have an idea but unsure which assumption to test first
- Need to design minimum experiments to validate core assumptions

## Rule 3: Consider product stage

### 0→1
Prefer:
- Lean Canvas
- Assumption Tree
- JTBD
- ICE

### Early Traction
Prefer:
- JTBD
- AARRR
- RICE
- User Journey Map

### Growth Stage
Prefer:
- AARRR
- North Star Metric
- RICE
- HEART

### Mature Optimization
Prefer:
- HEART
- North Star Metric
- Kano
- User Journey Map
- 5 Whys

## Rule 4: Recommend the minimum viable framework set
- 1 framework if the problem is narrow and obvious
- 2 frameworks if two lenses are enough
- 3 frameworks only if the user clearly needs a sequence

Never recommend more than 3 frameworks by default.

## Rule 5: Always include one misuse warning
Explain one nearby framework that should not be the main tool here, or one common mistake.

Examples:
- Use JTBD, not Persona, when the core issue is motivation.
- Use RICE, not Kano alone, when the core issue is prioritization.
- Use North Star Metric, not OKR alone, when the core issue is product-value focus.

---

## Quick Reference Card

| User question | First framework | Optional add-on | Avoid |
|--------------|-----------------|-----------------|-------|
| Should we build this? | JTBD | Kano + RICE | Jumping straight to scope |
| Which feature first? | RICE | MoSCoW | Kano alone |
| Growth is stuck | AARRR | Journey Map + 5 Whys | Looking only at acquisition |
| How to set North Star? | North Star Metric | HEART | Choosing vanity metrics |
| Experience feels bad | Journey Map | HEART + 5 Whys | Single-point fixes |
| Post-launch underperformed | 5 Whys | HEART + AARRR | Staying at surface symptoms |
| Validate an idea fast | Lean Canvas | Assumption Tree | Building without testing |
| Competitive positioning | JTBD | Kano + Lean Canvas | Feature-by-feature comparison |
