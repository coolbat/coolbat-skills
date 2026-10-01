## Sub-skill: content-style-learning

Use to build and maintain a writing style library. Can be invoked independently at any time.

Three commands:

| Command | Action |
|---------|--------|
| `import exemplar` / `导入范文` | Import a published article and extract its style fingerprint |
| `learn my edits` / `学习我的修改` | Learn from user edits to an AI draft |
| `show style library` / `查看范文库` | Display current accumulated style patterns |

### Mode 1: Import Exemplar

1. Read the article — identify type (opinion/narrative/tutorial/analysis) and language
2. Extract style fingerprint:
   - Sentence-level: average length, variance, short/long ratio, typical openings
   - Paragraph-level: average length, rhythm pattern, transition types
   - Emotional markers: intensity words, rhetorical devices (metaphor, repetition, contrast)
   - Structural patterns: opening hook style, closing style, transition phrases
   - Voice markers: first/second/third person ratio, recurring phrases, vocabulary temperature
3. Save to `meta/style-library/exemplars/{slug}.md` with frontmatter (title, category, language, date, fingerprint fields) and sample sections (opening hook, emotional peak, transition, closing)
4. Update `meta/style-library/index.yaml`

### Mode 2: Learn from Edits

1. Locate the edited draft in `drafting/` or `polish/`
2. Compare original vs edited — identify changes in: sentence structure, word choice, tone, paragraph reordering
3. Categorize edit patterns: sentence simplification / tone shift / voice injection / specificity increase / emotional amplification / structural reorganization
4. Append to `meta/style-library/edit-history.yaml`
5. Merge patterns into `meta/style-library/preferences.yaml`

Only extract patterns that appear 2+ times.

### Mode 3: Show Style Library

Read `meta/style-library/index.yaml` and display: total exemplars, breakdown by category and language, top 3-5 exemplars with fingerprint summaries.

### Integration with drafting

When `content-drafting` runs, it automatically checks for `meta/style-library/index.yaml` and injects matching exemplar samples as style examples. The more exemplars imported, the closer future drafts will match the author's voice.

### Guardrails

- Do not modify original exemplar articles
- Do not invent style patterns not present in the source material
- Do not override explicit brief requirements with learned preferences
- Respect language boundaries — do not mix zh/en style patterns
