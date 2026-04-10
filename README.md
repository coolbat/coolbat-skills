# coolbat-skills

A personal skill library for agentic workflows — writing, design, and product development.

Skills in this repo have been tested through real projects, not just drafted as prompt ideas.

---

## Skill Bundles

### Writing

Structured long-form writing workflow with English-first architecture and Chinese writing support.

| Skill | Purpose |
|-------|---------|
| `writing-workflow` | Main router for structured writing projects |
| `content-briefing` | Turns rough requests into usable briefs |
| `content-research` | Handles current facts, sourcing, and evidence |
| `content-drafting` | Generates angles, outlines, and drafts |
| `content-polishing` | Reviews structure, facts, and platform fit |
| `content-humanizing` | Reduces visible AI-writing patterns |
| `content-repurpose` | Adapts final drafts for WeChat / Xiaohongshu / SEO |
| `image-brief-generator` | Produces image briefs with bilingual prompts |

```
brief
  -> research risk check
  -> foundation research
  -> direction selection
  -> outline
  -> outline-targeted research
  -> draft -> polish -> humanize -> repurpose -> image briefs
```

---

### Design & Product

Skills for building and designing product pages, tool sites, and UI screens.

| Skill | Purpose |
|-------|---------|
| `premium-tool-page` | Build a V2.0 premium tool page from a keyword — keyword analysis, page strategy, template code or Stitch brief |
| `stitch-design-brief` | Convert PRD, requirements, or page strategy into a structured Stitch generation prompt |

```
keyword
  -> premium-tool-page (strategy + template code)
       -> stitch-design-brief (if Stitch design path chosen)
            -> Stitch generate -> review -> edit -> implementation
```

---

## Repository Layout

```
skills/
  writing-workflow/
  content-briefing/
  content-research/
  content-drafting/
  content-polishing/
  content-humanizing/
  content-repurpose/
  image-brief-generator/
  premium-tool-page/
  stitch-design-brief/
```

---

## Install

Copy the skill directories you want into your local skills folder:

```
~/.agents/skills/
```

Keep these intact for each skill:
- `SKILL.md`
- `assets/`
- `references/` where present

---

## License

MIT
