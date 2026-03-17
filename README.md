# coolbat-skills

Personal skill bundles for agentic writing workflows.

This repository currently publishes the first complete bundle: `writing-workflow`, a structured long-form writing system for:
- WeChat long-form articles
- SEO blog drafts
- bilingual Chinese/English writing
- WeChat and Xiaohongshu repurposing
- image brief generation

## Included Skills

- `writing-workflow`
- `content-briefing`
- `content-research`
- `content-drafting`
- `content-polishing`
- `content-humanizing`
- `content-repurpose`
- `image-brief-generator`

## What This Bundle Does

This is not a single prompt file.
It is a routed writing system with sub-skills for:
- brief normalization
- two-stage research
- angle selection and outlining
- drafting
- editorial review
- humanizing
- platform repurposing
- image brief generation

## Repository Layout

```text
skills/
  writing-workflow/
  content-briefing/
  content-research/
  content-drafting/
  content-polishing/
  content-humanizing/
  content-repurpose/
  image-brief-generator/
```

## Installation

Copy the desired skill directories into your local skill directory.

For Codex-style setups, that is typically a folder like:

```text
~/.agents/skills/
```

After copying:
- keep the directory names unchanged
- preserve each skill's `SKILL.md`
- preserve `agents/openai.yaml` and `assets/templates/`

## Recommended Usage

Start from `skills/writing-workflow/SKILL.md`.

The workflow is designed to:
1. normalize the brief
2. assess research risk
3. run `foundation` research when needed
4. propose directions before full drafting
5. run `outline-targeted` research when needed
6. draft
7. polish
8. humanize
9. repurpose
10. generate image briefs if needed

## References

The main workflow includes:
- a case study based on a real OpenClaw article project
- an evolution note explaining why the workflow rules were tightened over time

See:
- `skills/writing-workflow/references/case-study.md`
- `skills/writing-workflow/references/evolution-note-2026-03.md`

## License

MIT
