# Container Syntax for WeChat Articles

## Overview

Container syntax provides enhanced visual presentation for specific content types in WeChat articles. Use these sparingly — only when they genuinely improve readability or comprehension.

## Supported Containers

### 1. Dialogue Container

**Use when**: Presenting conversations, Q&A exchanges, or contrasting viewpoints

**Syntax**:
```markdown
:::dialogue
Question or first speaker's text
> Response or second speaker's text
Another question
> Another response
:::
```

**Example**:
```markdown
:::dialogue
How do I use this feature?
> It's simple — just click the button in the top right corner.
What if it doesn't work?
> Check your network connection first, then try restarting the app.
:::
```

**When NOT to use**: Single quotes or statements (use regular blockquote instead)

---

### 2. Timeline Container

**Use when**: Showing chronological events, project milestones, or historical progression

**Syntax**:
```markdown
:::timeline
**Date/Period** Event description
**Date/Period** Event description
**Date/Period** Event description
:::
```

**Example**:
```markdown
:::timeline
**2024 Q1** Project kickoff and initial research
**2024 Q2** MVP development completed
**2024 Q3** Beta testing with 100 users
**2024 Q4** Public launch
:::
```

**When NOT to use**: Unordered events or non-chronological lists

---

### 3. Callout Container

**Use when**: Highlighting important notes, warnings, tips, or critical information

**Syntax**:
```markdown
:::callout tip
Your tip content here
:::

:::callout warning
Your warning content here
:::

:::callout info
Your info content here
:::

:::callout danger
Your danger/critical content here
:::
```

**Types**:
- `tip`: Helpful suggestions or best practices (green/positive tone)
- `warning`: Cautions or things to watch out for (yellow/alert tone)
- `info`: Neutral informational notes (blue/neutral tone)
- `danger`: Critical warnings or errors to avoid (red/urgent tone)

**Example**:
```markdown
:::callout tip
Pro tip: Save your work frequently to avoid losing progress.
:::

:::callout warning
This feature is still in beta. Use with caution in production environments.
:::

:::callout danger
Never share your API keys publicly. This can lead to security breaches.
:::
```

**When NOT to use**: Regular paragraph content that doesn't need special emphasis

---

### 4. Quote Container

**Use when**: Highlighting pull quotes, key statements, or memorable phrases

**Syntax**:
```markdown
:::quote
Your quotable statement or key insight here.
:::
```

**Example**:
```markdown
:::quote
Good design is not about making things look pretty. It's about making things work better.
:::
```

**When NOT to use**: Citations or attributed quotes (use regular blockquote with attribution instead)

---

## Usage Guidelines

### When to Use Containers

✅ **Good use cases**:
- Dialogue: Actual conversations, Q&A sections, contrasting viewpoints
- Timeline: Product roadmaps, historical events, project phases
- Callout: Critical warnings, pro tips, important notes
- Quote: Key takeaways, memorable insights, pull quotes

❌ **Avoid using containers for**:
- Regular paragraphs that don't need special treatment
- Content that works fine with standard markdown
- Decorative purposes without functional value
- Every other paragraph (overuse reduces impact)

### Best Practices

1. **Use sparingly**: 1-3 containers per article maximum
2. **Choose the right type**: Match container to content purpose
3. **Keep content concise**: Containers work best with 1-3 sentences
4. **Don't nest containers**: Avoid putting containers inside containers
5. **Test readability**: Ensure containers enhance, not distract from, the reading flow

### Conversion Notes

When converting to WeChat HTML:
- Containers are transformed into styled `<section>` elements
- Each type has distinct visual styling (colors, icons, borders)
- Mobile-optimized for WeChat's reading environment
- Dark mode compatible (colors adjust automatically)

## Examples in Context

### Example 1: Tutorial Article

```markdown
## How to Set Up Your Account

First, navigate to the settings page.

:::callout tip
Make sure you're logged in before accessing settings.
:::

Then follow these steps:
1. Click "Account Settings"
2. Fill in your profile information
3. Save changes

:::callout warning
Changes take effect immediately and cannot be undone.
:::
```

### Example 2: Product Announcement

```markdown
## Our Journey So Far

:::timeline
**January 2024** Initial concept and research
**March 2024** First prototype completed
**June 2024** Beta launch with 50 users
**September 2024** Public release
:::

:::quote
We built this product because we believe everyone deserves better tools.
:::
```

### Example 3: Interview Article

```markdown
## Interview with the Founder

:::dialogue
What inspired you to start this company?
> I saw a gap in the market that nobody was addressing properly.
What's your vision for the next five years?
> We want to become the go-to solution for small businesses worldwide.
:::
```

---

## Technical Implementation

Container syntax is processed during the WeChat repurposing step:
1. Markdown with containers → HTML with styled sections
2. CSS classes applied based on container type
3. Icons and colors added automatically
4. Mobile-responsive layout ensured

No manual HTML editing required — the conversion handles everything.
