# Neutriverse Content Restructure Plan

> Status: approved for execution  
> Repository: `AplusNeutrino/My_Blog`  
> Target completion: 2026-09-29 10:00 (UTC+8)  
> Scope: content taxonomy, tag rationalization, front-matter migration, supporting classification UI/data, validation  
> Hard rule: **do not rewrite article body content**

## 1. Approved content model

The new taxonomy separates four questions:

- **Type** — `fragment`, `note`, `essay`. Argument structure outranks mechanical word count.
- **Topic** — exactly one of `otaku`, `arts`, `computation`, `humanity`.
- **Series** — optional; only for a durable continuing line of inquiry, not to preserve an old folder/category name.
- **Tags** — a small canonical set of specific works/entities, technical concepts, analytical themes, named theories/frameworks/people.

Preferred post front matter:

```yaml
---
title: ...
date: ...
type: note
topic: computation
series: computer-networks   # optional
tags:
  - TCP
  - Congestion Control
# preserve permalink / slug / layout / image / description / other required fields
---
```

## 2. Topic definitions

- `otaku`: Games, Anime, Manga, Visual Novels, JRPG and related subculture.
- `arts`: Film, Books, Literature and adjacent traditional cultural works.
- `computation`: Computing, AI, Data, Programming, Databases, Networks, Algorithms, ML/LLM and data science.
- `humanity`: Society, Philosophy, Personal reflection, internet culture, values, identity and human experience.

Do not create another top-level Topic during this migration.

## 3. Classification rules

1. Read each article itself before assigning its new classification; never classify from filename alone when body content is available.
2. Assign exactly one `type` and one primary `topic` to each post in migration scope.
3. Add `series` only where a real future-extensible thread exists. Course-derived lines may be reframed as enduring subjects (for example `计网笔记` → `Computer Networks`).
4. Reduce tags based on actual subject matter. Do not use tags to repeat Type, Topic or Series.
5. Keep legacy `categories` temporarily only if current Jekyll/Chirpy compatibility requires them.
6. Preserve unrelated metadata.
7. **Do not modify article body text, headings, wording, quotations, images or argument structure.**
8. Preserve existing URLs: do not rename post files or change `date`, `slug` or `permalink` unless an unavoidable technical issue is documented.

## 4. Tag rationalization

Retain useful retrieval tags such as named works/franchises, technologies/concepts, analytical themes, and named theories/people. Merge synonyms, spelling/case variants and redundant abbreviation/full-name pairs into one canonical form.

Normally retire generic editorial/domain labels whose work is now done by Type/Topic/Series, such as 学习、学习笔记、笔记、记录、随笔、随想、杂谈、思考, broad media-only tags such as 游戏/动画/电影/书籍, and broad computation-domain tags used only to mean Computing/AI/Data.

Default tag-count targets: Fragment `0–3`, Note `2–5`, Essay `3–6`. These are judgment guidelines, not hard limits.

Step 2 must inventory old tag usage, produce the canonical old → new map, protect useful one-off entity/concept tags, and document uncertain cases.

## 5. Migration audit

The authoritative audit is `docs/content-taxonomy-migration.md`. It records source file/title, old categories/tags, new Type/Topic/Series/Tags, confidence (`confident`/`review`) and notes. Every migrated article must have an audit entry.

The canonical tag/legacy-category decision companion is `docs/content-taxonomy-tag-map.md`; per-article final decisions remain recorded in the authoritative migration audit as articles are read and migrated.

## 6. Implementation boundaries

Allowed: front-matter metadata, taxonomy data/config, minimum compatible taxonomy/index/template plumbing, tag cleanup, audit/report files, and fixes directly caused by this migration.

Out of scope: prose rewriting, opinion changes, stylistic body editing, broad site redesign, unrelated refactors, and gratuitous URL changes.

## 7. Eight-step execution plan

Each run reads this file and current GitHub state, executes **the first unchecked step only**, then updates this plan and records evidence. A blocked step remains unchecked.

### Step 1 — Repository + content inventory

- [x] Locate article/Thought sources and front-matter conventions; inventory published writing; identify category/tag generation; establish migration count and audit; confirm URL-sensitive metadata.

**Execution evidence — 2026-09-29:** Created `docs/content-taxonomy-migration.md` with the complete 44-post source inventory plus 5 current Thoughts fragments (49 writing items total). Confirmed posts live in `_posts/`; Thoughts are 5 YAML objects embedded in `_tabs/thoughts.md` and rendered by `_layouts/thoughts.html`; no `_thoughts` collection exists. Confirmed existing discovery through `_tabs/categories.md`, `_tabs/tags.md`, archives, custom layouts, and existing `_includes/post-series.html`. Representative front matter confirms current `categories` + `tags` convention. URL-safety rule established: leave filenames, dates, slugs and explicit permalinks unchanged. No article body was edited. Audit commit: `27e2187bbbb9b3c6bc51e0afa8d47586951819f0`. Plan-status update commit: `8a1a2f6322aa1bce992ab8e2c7f4a2f898ae6cc8`. No blocker.

### Step 2 — Canonical taxonomy + tag map

- [x] Read current tag inventory; build canonical reduction map; identify retired generic tags, synonym/case merges and protected entity tags; map old category/series-like structures; document uncertain cases in the audit. Do not edit article bodies.

**Execution evidence — 2026-09-29:** Read front matter for all 44 posts and the Step-1 fragment inventory. Added `docs/content-taxonomy-tag-map.md`, which maps every observed legacy tag family to KEEP/MERGE/RETIRE/REVIEW decisions, defines canonical naming rules, maps legacy categories to Type/Topic/Series responsibilities, and records body-review uncertainties. Durable Series candidates are `Database Systems`, `Computer Architecture`, `Computer Networks`, with `LLM Systems` explicitly conditional on later body review. Broad subject tags carried by those Series are scheduled for retirement; useful one-off entity/concept tags are protected rather than removed by frequency. No article body or article front matter was modified. Tag-map commit: `73ff315e55a8e42777b2dd21be1dd5377a1344de`. Plan-status update commit: `d820aae2ae5c0b2cfa7bb4d26ef7c9dae1a3e629`. No blocker.

### Step 3 — Implement taxonomy plumbing

- [x] Add/adapt the minimum machinery required for `type`, `topic`, `series` and canonical `tags` in templates/indexes/navigation without breaking existing URLs. Prefer adapting current category/tag machinery. Inspect existing `_includes/post-series.html` before changing Series behavior. Validate syntax/build as repository tooling permits.

**Execution evidence — 2026-09-29:** Added `_data/content_taxonomy.yml` as the four-Topic/three-Type presentation dictionary (`fcd9a84fcd7afba1d430c9a4bcc0d0b0c7a4f070`) and `_includes/post-taxonomy.html` to surface Type, Topic and optional Series on migrated posts (`029d73ea68022ace48ebc040e477835eac0ec863`). Updated `_layouts/post.html` to render the new semantic metadata while retaining legacy category links and existing tag URLs for compatibility (`374c1e9625e24a22fa9b95a8b642fed52b5b5ec2`). Inspected and adapted `_includes/post-series.html`: explicit `page.series` now groups posts directly by durable Series, while unmigrated posts retain the legacy category-based fallback until migration finishes (`a3cb7cc0d0f93fa8d29f6a61ea9ae3566774069c`). No post filename/date/slug/permalink or article body was touched. Liquid/YAML changes were statically reviewed, but no executable Jekyll build was available through the connected GitHub interface in this run, so build/runtime PASS is intentionally not claimed. No blocker for migration; full build validation remains Step 8.

### Step 4 — Article migration batch A

- [ ] Read and classify approximately the first quarter of the 44 posts. Front matter only. Apply Type, Topic, optional Series and reduced tags; preserve URLs and bodies; update audit for every migrated file.

### Step 5 — Article migration batch B

- [ ] Read and classify approximately the second quarter using the same rules; front matter only; update audit.

### Step 6 — Article migration batch C

- [ ] Read and classify approximately the third quarter using the same rules; front matter only; update audit.

### Step 7 — Article migration batch D + Fragments/Thoughts

- [ ] Read/classify remaining posts; align current Thoughts to `type: fragment` in the least disruptive architecture-compatible way; finish tag cleanup; update audit and list owner-review items.

### Step 8 — Full validation + final handoff

- [ ] Validate all writing classifications, allowed Topic values, meaningful optional Series, tag reduction, body preservation, URL/permalink preservation and generated taxonomy surfaces. Run available build/tests where feasible and review diffs for accidental prose changes. Create `docs/content-taxonomy-final-report.md` with migration totals, Type/Topic counts, Series list, old/new unique tag counts, merges/removals, URL compatibility, validation/build evidence, unresolved review items and relevant commit SHAs.

## 8. Definition of done

Done means all relevant writing has been individually read/classified; Type uses only Fragment/Note/Essay; Topic uses only the four approved values; learning material is organized by enduring subject/question rather than course sequence alone; Series are optional and extensible; tags are materially reduced/canonicalized; bodies are unchanged; URLs are preserved wherever possible; the site can surface the taxonomy with minimal compatible extensions; and complete audit/final-report evidence exists.

## 9. Safety and handoff

Read before writing. Never infer classification from filename alone. Never claim build/runtime PASS without running the validation. Do not silently change URLs or prose. Re-read GitHub state on every run. Per `AGENTS.md`, final handoffs involving changed files must include copy-paste-ready PowerShell commit/push commands when manual Git operation is relevant; automated GitHub commits must be listed by SHA in the final report.
