# Neutriverse Content Restructure Plan

> Status: approved for execution  
> Repository: `AplusNeutrino/My_Blog`  
> Target completion: 2026-09-29 10:00 (UTC+8)  
> Scope: content taxonomy, tag rationalization, front-matter migration, supporting classification UI/data, validation  
> Hard rule: **do not rewrite article body content**

## 1. Goal

Reorganize Neutriverse's writing system around a durable content model that can support a large and growing body of public writing without turning the site into a course-folder archive or an unbounded tag cloud.

The new model separates four independent questions:

- **Type** — how deeply is this piece expressed?
- **Topic** — which broad long-term domain does it belong to?
- **Series** — is it part of a continuing line of inquiry?
- **Tags** — what specific works, concepts, technologies, themes, or entities does it concern?

Existing article URLs should remain unchanged wherever technically possible.

## 2. Approved taxonomy

### 2.1 Type

Exactly three writing types:

- `fragment`
  - very short, immediate thought or observation
  - normally no complete argument
  - primarily maps to the current Thoughts/short-form system
- `note`
  - usually up to roughly 1000 Chinese characters, but length is not mechanical
  - one piece, one specific idea / question / observation
  - includes short reviews, focused cultural commentary, technical explanations, and learning notes
- `essay`
  - contains a clear central proposition that needs sustained development, comparison, synthesis, or argument
  - may span multiple works, sources, disciplines, or technical ideas
  - no strict upper or lower word-count rule

Decision principle: **argument structure outranks word count**.

### 2.2 Topic

Exactly four long-lived top-level topics:

- `otaku`
  - Games, Anime, Manga, Visual Novels, JRPG, related subculture
- `arts`
  - Film, Books, Literature, and adjacent traditional cultural works
- `computation`
  - Computing, AI, Data, Programming, Databases, Networks, Algorithms, ML/LLM, data science
- `humanity`
  - Society, Philosophy, Personal reflection, internet culture, values, identity, human experience

These are intentionally broad. Do not create new top-level topics during migration unless the current plan is explicitly revised by the owner.

### 2.3 Series

`series` is optional.

A Series means: **a continuing line of inquiry that can receive future pieces**.

Good candidates include:

- Computer Networks
- Database Systems
- Understanding LLMs
- Formal Systems
- a recurring thematic criticism project

Do **not** use Series merely to preserve old folder names or content-purpose labels such as:

- 学习笔记
- 游戏记录
- 软件发布
- 记忆碎片
- 思维链条

Course-derived series may survive, but should be reframed as an enduring subject rather than a frozen lecture sequence. Example: `计网笔记` → `Computer Networks`, where future non-course articles can still belong.

## 3. Front-matter target model

Preferred semantic shape:

```yaml
---
title: ...
date: ...
type: note
topic: computation
series: computer-networks   # optional; omit when not used
tags:
  - TCP
  - Congestion Control
  - Transport Layer
# preserve existing permalink / slug / layout / image / other required fields
---
```

Rules:

1. Preserve existing permalink/slug behavior and existing URLs wherever possible.
2. Preserve all unrelated metadata required by the site/theme.
3. Modify front matter only unless a technical classification template/data file must be changed.
4. **Do not alter article body text, argument, wording, headings, quotations, images, or prose structure.**
5. Do not mechanically force a `series` value onto every article.
6. If current architecture requires retaining legacy `categories` temporarily for compatibility, keep them only as a migration bridge; the new semantic source of truth is `type/topic/series/tags`.

## 4. Tag rationalization strategy

The current tag system should be reduced and normalized, not indiscriminately deleted.

### 4.1 What a tag should represent

A tag should usually be one of:

1. **Named work / franchise / object**
   - `Final Fantasy XVI`
   - `NieR: Automata`
   - `Ghost in the Shell`
2. **Specific technical concept / technology**
   - `RAG`
   - `Embedding`
   - `TCP`
   - `B+ Tree`
3. **Specific analytical concept / theme**
   - `Narrative Design`
   - `Identity`
   - `Memory`
   - `Apocalypse`
4. **Named theory / framework / person when genuinely useful for retrieval**
   - `Gödel`
   - `Terror Management Theory`

### 4.2 What should normally stop being a tag

Retire tags whose job is already handled by Type, Topic, or Series, including generic labels such as:

- 学习 / 学习笔记
- 笔记
- 记录
- 随笔 / 随想
- 杂谈
- 思考
- 游戏 / 动画 / 电影 / 书籍 when used only as broad media labels
- Computing / AI / Data when used only as broad domain labels already represented by `topic: computation`
- old category names that describe editorial purpose rather than subject matter

### 4.3 Normalization rules

- Merge obvious synonyms, spelling variants, abbreviations, plural/singular variants, and capitalization variants.
- Prefer canonical technical terminology for technical tags.
- Prefer official/common work titles for media tags.
- Do not create both a full term and abbreviation unless each has independent retrieval value; prefer one canonical form.
- Avoid duplicating `topic` or `series` as a tag unless a concrete audit shows a strong discovery reason.
- Do not delete a highly specific one-off tag merely because it is used once if it names a work, concept, technology, theory, or person that is genuinely useful for later lookup.

### 4.4 Tag-count target

These are defaults, not hard validation limits:

- Fragment: `0–3` tags
- Note: `2–5` tags
- Essay: `3–6` tags

A piece should have enough tags to be findable, but not enough to become a summary of every noun in the article.

### 4.5 Canonicalization workflow

During the article audit:

1. inventory every existing tag and usage count;
2. group near-duplicates and synonyms;
3. identify tags made redundant by Type/Topic/Series;
4. retain high-value named entities and concepts;
5. create a canonical old → new mapping;
6. migrate article metadata using that mapping plus article-specific judgment;
7. validate that no obviously useful retrieval path was lost.

## 5. Classification judgment rules

When reading each article:

1. Read the article itself, not only its current category/tag names.
2. Assign exactly one `type`.
3. Assign exactly one primary `topic` unless the current implementation proves a strong need for multi-topic support; default is one topic.
4. Assign `series` only when a real continuing thread exists.
5. Rewrite tags as a small canonical set based on actual subject matter.
6. Mark ambiguous cases in the migration audit rather than inventing new taxonomy.
7. Preserve the body byte-for-byte whenever feasible.

### Borderline examples

- 900 characters with a sustained thesis and comparison → may be `essay`.
- 1500 characters that mainly explain one technical mechanism → may remain `note`.
- a learning article should not be classified by the old course folder alone; classify by the idea it explains.
- a game/anime/film/book article is classified by depth (`type`) and domain (`topic`), not by a generic “review” label.

## 6. Required migration audit

Create and maintain a machine- or human-readable audit file during migration with at least:

| Field | Meaning |
|---|---|
| Article | source file/title |
| Old Category | prior category values |
| Old Tags | prior tags |
| New Type | fragment/note/essay |
| New Topic | otaku/arts/computation/humanity |
| New Series | optional |
| New Tags | canonical reduced set |
| Confidence | confident/review |
| Notes | reason for ambiguous or notable decisions |

Preferred location: `docs/content-taxonomy-migration.md` or an equivalent clearly named file.

## 7. Implementation boundaries

### Allowed

- front-matter metadata changes
- taxonomy data/config changes
- category/topic/type/series index or template changes required to make the new model function
- tag cleanup and canonicalization
- migration audit/report files
- tests/build fixes directly caused by the taxonomy migration

### Not allowed in this migration

- rewriting article prose
- changing the author's historical opinions
- stylistic editing of article bodies
- broad redesign of the entire Neutriverse visual language
- unrelated refactors
- gratuitous URL changes

## 8. Eight-step hourly execution plan

Each automation run must first read this file and the current repository state, then execute **the first unchecked step only**. After completing a step, update this document by changing `[ ]` to `[x]` and append a short dated execution note under that step. If a step is partially blocked, record the blocker clearly and do not falsely mark it complete.

### Step 1 — Repository + content inventory (03:00)

- [ ] Locate all article/Thought source directories and front-matter conventions.
- Inventory all published writing files, categories, tags, existing permalinks, and special layouts.
- Identify how category/tag pages are generated today.
- Establish exact migration count and create the initial migration audit file.
- Confirm which metadata fields can be changed without changing URLs.

### Step 2 — Canonical taxonomy + tag map (04:00)

- [ ] Read the current tag inventory and build the first canonical tag reduction map.
- Identify retired generic tags, synonym merges, spelling/case normalization, and protected high-value entity tags.
- Map old category/series-like structures to the new model.
- Record all rules and uncertain cases in the migration audit.
- Do not edit article bodies.

### Step 3 — Implement taxonomy plumbing (05:00)

- [ ] Add or adapt the minimum site machinery required for `type`, `topic`, `series`, and canonical `tags` to be usable in templates/indexes/navigation without breaking existing URLs.
- Prefer adapting existing category/tag machinery over replacing the CMS architecture.
- Preserve backwards compatibility where needed during migration.
- Validate syntax/build as far as repository tooling permits.

### Step 4 — Article migration batch A (06:00)

- [ ] Read and classify approximately the first quarter of existing long-form/article source files.
- Edit front matter only.
- Apply `type`, `topic`, optional `series`, and reduced canonical tags.
- Preserve permalinks and body content.
- Update migration audit for every migrated file.

### Step 5 — Article migration batch B (07:00)

- [ ] Read and classify approximately the second quarter of existing long-form/article source files using the same rules.
- Front matter only; preserve URLs and body content.
- Update migration audit.

### Step 6 — Article migration batch C (08:00)

- [ ] Read and classify approximately the third quarter of existing long-form/article source files using the same rules.
- Front matter only; preserve URLs and body content.
- Update migration audit.

### Step 7 — Article migration batch D + Fragments/Thoughts (09:00)

- [ ] Read and classify the remaining article files.
- Migrate/align the current Thoughts/short-form system to `type: fragment` in the least disruptive way supported by the existing architecture.
- Complete tag cleanup across all migrated content.
- Update migration audit and explicitly list any items requiring owner review.

### Step 8 — Full validation + final handoff (10:00)

- [ ] Validate the complete migration:
  - every writing item has the intended new classification where applicable;
  - no article body was intentionally changed;
  - existing URLs/permalinks were preserved wherever possible;
  - tag duplication and generic editorial tags were materially reduced;
  - topic values are limited to `otaku`, `arts`, `computation`, `humanity`;
  - Series usage is optional and meaningful;
  - generated classification pages/templates do not obviously break;
  - repository build/tests are run where feasible.
- Review diffs for accidental prose edits.
- Produce a final report at `docs/content-taxonomy-final-report.md` containing:
  - total items migrated;
  - counts by Type and Topic;
  - Series list;
  - old vs new unique tag counts;
  - canonical tag merges/removals;
  - URL compatibility notes;
  - validation/build results;
  - unresolved review items;
  - relevant commit SHAs.
- Mark this plan complete only if evidence supports completion.

## 9. Definition of done

The migration is done when:

- all relevant existing writing has been individually read and classified;
- Type uses only Fragment / Note / Essay;
- Topic uses only Otaku / Arts / Computation / Humanity;
- learning notes are organized by enduring subject/question rather than merely by course sequence;
- Series are optional, durable, and future-extensible;
- tags are meaningfully reduced and canonicalized;
- article body content remains unchanged;
- existing URLs are preserved wherever possible;
- the site can surface the new taxonomy using its existing architecture or minimal compatible extensions;
- a complete audit and final report exist.

## 10. Execution safety rules

- Read before writing.
- Never infer an article classification from filename alone when body content is available.
- Do not claim runtime/build PASS without actually running the available validation.
- Do not silently change URLs.
- Do not silently rewrite prose.
- Keep changes scoped to this migration.
- If repository state changes between hourly runs, re-read current files and continue from GitHub truth rather than stale assumptions.

## 11. Repository handoff convention

Per `AGENTS.md`, any final handoff involving changed files must include copy-paste-ready PowerShell commands for committing and pushing changes when manual Git operation is relevant. Automated GitHub commits should still be listed by SHA in the final migration report.
