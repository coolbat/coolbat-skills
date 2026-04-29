---
name: content-style-learning
description: Use when the user wants to import published articles to build a style library, or learn from their edits to improve future drafts. Supports "import exemplar", "learn my edits", and "show style library" commands.
---

# Content Style Learning

## Overview

This skill builds and maintains a user's writing style library by:
1. Extracting style fingerprints from published articles (exemplars)
2. Learning from user edits to AI-generated drafts
3. Injecting learned style patterns into future drafts

The goal: make AI drafts progressively more like the user's own writing.

## When to Use

Use this skill when:
- User says "import exemplar" / "导入范文" / "build style library"
- User says "learn my edits" / "学习我的修改" after editing a draft
- User says "show style library" / "查看范文库"
- User wants future drafts to match their personal style

## Style Fingerprint Components

A style fingerprint captures:
- **Sentence rhythm**: average length, variance, short-to-long ratio
- **Paragraph pacing**: typical paragraph length, rhythm pattern
- **Emotional expression**: intensity, frequency, typical phrases
- **Transition patterns**: how the writer moves between ideas
- **Opening hooks**: typical ways to start articles
- **Closing patterns**: typical ways to end articles
- **Vocabulary temperature**: formal vs casual word choice
- **Personal voice markers**: recurring phrases, sentence structures, rhetorical devices

## Workflow

### Mode 1: Import Exemplar

**Trigger**: User provides one or more published articles (markdown files)

**Steps**:

1. **Read the article**
   - Extract full text
   - Identify article type (opinion/narrative/tutorial/analysis)
   - Note language (zh/en)

2. **Extract style fingerprint**
   
   Analyze and record:
   
   **Sentence-level**:
   - Average sentence length
   - Sentence length variance (shortest vs longest)
   - Ratio of short sentences (< 15 chars) to long sentences (> 40 chars)
   - Typical sentence openings (first 3-5 words patterns)
   
   **Paragraph-level**:
   - Average paragraph length
   - Paragraph rhythm (short-short-long, long-short-long, etc.)
   - Transition word frequency and types
   
   **Emotional markers**:
   - Emotional intensity words and their frequency
   - Exclamation/question mark usage
   - Rhetorical device patterns (metaphor, repetition, contrast)
   
   **Structural patterns**:
   - Opening hook style (extract first 2-3 sentences)
   - Closing style (extract last 2-3 sentences)
   - Transition phrases between sections
   - Self-correction patterns ("但是", "不过", "actually", "however")
   
   **Voice markers**:
   - First-person vs third-person ratio
   - Recurring phrases or expressions
   - Vocabulary temperature (formal/casual word ratio)

3. **Categorize the exemplar**
   
   Assign category based on content type:
   - `opinion`: opinion-led articles with clear judgment
   - `narrative`: story-driven or case study articles
   - `tutorial`: instruction-focused practical guides
   - `analysis`: evidence-led analytical pieces
   - `general`: fallback for mixed types

4. **Save to style library**
   
   Create file at:
   ```
   meta/style-library/exemplars/{slug}.md
   ```
   
   Format:
   ```markdown
   ---
   title: {article title}
   category: {opinion|narrative|tutorial|analysis|general}
   language: {zh|en}
   date_imported: {YYYY-MM-DD}
   word_count: {count}
   fingerprint:
     sentence_avg_length: {number}
     sentence_variance: {number}
     short_long_ratio: {number}
     paragraph_avg_length: {number}
     paragraph_rhythm: "{pattern}"
     emotional_intensity: {low|medium|high}
     voice_person: {first|third|mixed}
     vocabulary_temperature: {formal|neutral|casual}
   ---
   
   ## Opening Hook Sample
   {first 2-3 sentences}
   
   ## Emotional Peak Sample
   {1-2 sentences from emotional high point}
   
   ## Transition Sample
   {1-2 transition sentences}
   
   ## Closing Sample
   {last 2-3 sentences}
   ```

5. **Update index**
   
   Append to `meta/style-library/index.yaml`:
   ```yaml
   exemplars:
     - slug: {slug}
       title: {title}
       category: {category}
       language: {language}
       date_imported: {date}
       fingerprint_summary: "{brief description of style}"
   ```

### Mode 2: Learn from Edits

**Trigger**: User has edited a draft and says "learn my edits" / "学习我的修改"

**Steps**:

1. **Locate the edited draft**
   - Check `drafting/` and `polish/` directories for recent files
   - Ask user to specify file if multiple candidates exist

2. **Compare original vs edited**
   
   Identify changes in:
   - Sentence structure modifications
   - Word choice replacements
   - Added or removed content
   - Tone adjustments
   - Paragraph reordering

3. **Extract edit patterns**
   
   Categorize edits:
   - **Sentence simplification**: long → short
   - **Tone shift**: formal → casual or vice versa
   - **Voice injection**: added first-person perspective
   - **Specificity increase**: vague → concrete
   - **Emotional amplification**: neutral → expressive
   - **Structural reorganization**: reordered sections

4. **Save to edit history**
   
   Append to `meta/style-library/edit-history.yaml`:
   ```yaml
   - date: {YYYY-MM-DD}
     file: {file path}
     edit_patterns:
       - type: {pattern type}
         example_before: "{original text}"
         example_after: "{edited text}"
         rule: "{inferred preference}"
   ```

5. **Update style preferences**
   
   Merge patterns into `meta/style-library/preferences.yaml`:
   ```yaml
   sentence_preferences:
     - prefer_short_sentences: {true|false}
     - avoid_passive_voice: {true|false}
   
   tone_preferences:
     - formality_level: {formal|neutral|casual}
     - personal_voice_strength: {low|medium|high}
   
   content_preferences:
     - specificity_level: {abstract|balanced|concrete}
     - emotional_expression: {restrained|moderate|expressive}
   
   structural_preferences:
     - paragraph_length: {short|medium|long}
     - transition_style: {explicit|implicit}
   ```

### Mode 3: Show Style Library

**Trigger**: User says "show style library" / "查看范文库"

**Steps**:

1. Read `meta/style-library/index.yaml`
2. Display summary:
   - Total exemplars count
   - Breakdown by category
   - Breakdown by language
   - Most recent imports
3. Show top 3-5 exemplars with their fingerprint summaries

## Integration with Drafting

When `content-drafting` is invoked:

1. Check if `meta/style-library/index.yaml` exists
2. If yes:
   - Load exemplars matching the current article category
   - Extract sample segments (opening, emotional peak, transition, closing)
   - Inject into drafting prompt as style examples
   - Apply preferences from `preferences.yaml` as hard constraints

3. If no:
   - Use generic writing guidelines only
   - Suggest user to import exemplars for better style matching

## Guardrails

- Do not modify the original exemplar articles
- Do not invent style patterns not present in the source material
- When learning from edits, only extract patterns that appear 2+ times
- Do not override explicit brief requirements with learned preferences
- Respect language boundaries (don't mix zh/en style patterns)

## Checklist

### For Import Exemplar:
- [ ] Article read and analyzed
- [ ] Style fingerprint extracted
- [ ] Category assigned
- [ ] Exemplar file saved
- [ ] Index updated

### For Learn from Edits:
- [ ] Original and edited versions compared
- [ ] Edit patterns identified
- [ ] Edit history updated
- [ ] Preferences merged

### For Show Style Library:
- [ ] Index read
- [ ] Summary displayed
- [ ] Top exemplars shown
