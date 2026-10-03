# Neutriverse Master Restructure Plan

> Status: **living master plan**  
> Repository: `AplusNeutrino/My_Blog`  
> Purpose: capture the long-term redesign direction for Neutriverse and preserve implementation history  
> Current state: **Phase 1 completed; T00 done; T01 ready; implementation decisions resolved; hourly execution authorized**  
> Principle: Neutriverse is not merely a blog; it is a long-lived personal digital universe for thinking, building, observing, and leaving a trace on the internet.

---

## 0. Core vision

Neutriverse should evolve from a themed personal blog into a **personal digital universe**.

Its purpose is not only to publish finished projects or maintain a portfolio. It should preserve a visible record of what Neutrino thinks, creates, studies, observes, and becomes over time.

A useful working statement is:

> **Neutriverse is a continuously growing personal digital universe. It preserves my thoughts, presents the systems I build, observes the outside world, and records the traces left by all of them over time.**

The site should support decades of accumulation rather than optimize only for the current number of posts.

The long-term conceptual model is:

```text
NEUTRIVERSE
│
├── THINK      What I think
├── BUILD      What I make
├── OBSERVE    What I watch
└── ABOUT      Who I am
```

Another shorthand for the same idea:

```text
I think.
I build.
I observe.
I exist.
```

The four sections are not equal content silos. **THINK is expected to become the largest body of accumulated material**, while BUILD, OBSERVE, and ABOUT provide other ways to understand the same person and universe.

---

## 1. Product / identity principles

### 1.1 Writing is the site, not a separate “Blog” feature

Avoid treating the site as:

```text
Website
└── Blog
```

Prefer:

```text
Neutriverse
├── Thoughts
├── Projects
├── Systems
└── Neutrino
```

Writing should feel native to the site rather than being one module inside it.

### 1.2 The site should express a person, not a résumé

Professional work, technical learning, games, anime, books, philosophy, social observation, and personal reflection do not need to be split into separate identities.

The site should allow them to coexist as different traces of the same author.

### 1.3 Preserve long-term continuity

Existing URLs, historical posts, project histories, and earlier ways of thinking are valuable records. Major redesign work should prefer additive migration and compatibility over destructive rewriting.

### 1.4 The interface may have lore, but usability comes first

Neutriverse already uses concepts such as modules, probes, cults, signals, observatories, and other in-universe language. This identity should be retained, but it should become a **presentation layer**, not a prerequisite for understanding navigation.

Preferred pattern:

```text
Clear information architecture
↓
THINK / BUILD / OBSERVE / ABOUT

Worldbuilding / personality layer
↓
Signal / Probe / Cult / Observatory / Fragment / Module
```

For example, a page may visibly say `OBSERVE — Ravenis` while a smaller secondary label describes it as a public intelligence node or fictional module.

Do not force first-time visitors to decode the lore before they can navigate the site.

---

## 2. Top-level information architecture

### 2.1 THINK — What I think

THINK contains writing and intellectual traces: short fragments, focused notes, long essays, reviews/criticism, technical explanations, learning notes, and continuing lines of inquiry.

Its primary organization is **expression depth + subject**, not legacy course folders.

Conceptually:

```text
THINK
│
├── Fragments
├── Notes
├── Essays
│
├── Topics
├── Series
├── Tags
└── Archive / Search
```

`Archive`, `Tags`, and `Search` are retrieval tools rather than top-level identity sections.

### 2.2 BUILD — What I make

BUILD contains long-lived projects, software, experiments, tools, demos, releases, and development histories.

A project is **not the same thing as a post describing the project**.

Projects should eventually become durable entities with pages such as:

```text
PROJECT
FitzSight

Overview
Status
Demo
Documentation
Release
Development Log
Related Posts
Repository
```

Posts become records produced during a project's life rather than being the project itself.

Likely existing/future BUILD entities include projects such as FitzSight, Akasha Notes, Toyosatomimi's Headphone, and other experiments.

### 2.3 OBSERVE — What I watch

OBSERVE groups systems that inspect or interpret the outside world.

Existing examples already fit this model well:

- **Ravenis** — public intelligence / news / event observation.
- **Occult Atlas** — astronomical / astrological observation interface.

Future external-world systems may also live here: market observation, AI radar, data monitors, or other observatories.

This makes these applications feel intentional rather than like unrelated tools embedded in a blog.

### 2.4 ABOUT — Who I am

ABOUT replaces Archive as the fourth top-level identity section.

It should become an **author node / digital identity page**, not merely a résumé page.

Possible structure:

```text
ABOUT NEUTRINO

01 / IDENTITY
Who I am and what I care about

02 / CURRENTLY
Working on
Thinking about
Learning
Reading
Playing

03 / MY INTERNET
GitHub
Other public identities / contact surfaces

04 / THIS WEBSITE
Why Neutriverse exists
How it evolved
Design philosophy

05 / TIMELINE
A lightweight history of my internet / project / writing presence
```

The old idea of Archive is therefore split:

- **Content Archive** belongs under THINK as a retrieval tool.
- **Personal / site history** can appear under ABOUT as a timeline.

---

## 3. Homepage direction

The homepage should stop behaving like a combination of category index, dashboard, blog feed, and hidden-navigation puzzle.

Its job should be to answer five questions quickly:

1. What is this place?
2. Who is behind it?
3. What is happening here recently?
4. What can I explore?
5. What should I read / open next?

A possible hierarchy:

```text
NEUTRIVERSE
A personal universe of thoughts, systems and observations.

LATEST TRANSMISSIONS
Recent Essay / Note / Fragment (project-related writing may carry a secondary Project Log label)

EXPLORE THE UNIVERSE
THINK
BUILD
OBSERVE
ABOUT

CURRENT SIGNAL
Current major project / interest / focus

SYSTEM STATUS
Records / Projects / Last update / lightweight site state
```

The homepage should prioritize **recent expression** over a wall of categories.

Posts of different types may appear in one chronological stream, clearly labeled:

```text
ESSAY
NOTE
FRAGMENT
# Secondary relationship label when applicable: PROJECT LOG
```

This helps the homepage answer: **“What has this person been thinking or doing lately?”**

---

## 4. THINK content model

### 4.1 Type — how deeply is this expressed?

The approved Type vocabulary is:

- `fragment`
- `note`
- `essay`

Argument structure matters more than mechanical word count.

#### Fragment

A low-friction thought trace.

Typical scale: one sentence to roughly 200 Chinese characters, but not a hard limit.

Use for:

- a sudden observation;
- an incomplete idea;
- a concise judgment;
- something worth preserving before it becomes a larger piece.

Fragments usually do not need a full article title, summary, hero image, or complete argument.

Existing `/thoughts/` is conceptually the Fragment interface.

#### Note

The primary everyday writing form.

Working principle:

> **One note, one idea.**

Typical scale: roughly 300–1000 Chinese characters, but structure matters more than length.

Use for:

- one specific reaction to a game / anime / film / book;
- a focused cultural observation;
- a technical explanation;
- a learning note written in the author's own understanding;
- one concrete question or concept.

Avoid forcing a Note to review an entire work. A narrow claim is preferred over generic titles such as “某某观后感”.

#### Essay

A developed argument or substantial piece of criticism.

Use when there is a thesis that needs sustained argument, comparison, evidence, or synthesis.

Essays may cross multiple works, disciplines, or sources and may be several thousand words or longer.

Examples of suitable shapes:

- comparing recurring themes across several games;
- a long-form argument about AI systems;
- combining cultural criticism, theory, and personal interpretation.

### 4.2 Thought growth is allowed

The system should support a natural path such as:

```text
Thought
  ↓
Fragment
  ↓
Note
  ↓
Essay
```

Not every Fragment must become a Note, and not every Note must become an Essay. The point is to reduce the psychological cost of publishing and preserve intermediate thinking.

### 4.3 Professional learning belongs in the same system

Learning notes should not be treated as a separate “course notebook” universe.

Prefer:

```text
Why does a database index usually use a B+ Tree?
```

over:

```text
DBMS Lecture 4 Notes
```

The former can remain useful years after the original course ends.

This is guidance for future writing only. Existing learning-note titles, bodies and structure will not be rewritten or split during this redesign.

Course-derived material may still be grouped into durable Series, but the article itself should ideally center a reusable question or concept.

---

## 5. Topic model

Every writing item receives one primary Topic from exactly four stable domains.

### `otaku`

Games, Anime, Manga, Visual Novels, JRPG, related subculture, and adjacent criticism.

This is intentionally a broad “otaku / subculture” domain rather than separate game/anime categories.

### `arts`

Film, Books, Literature, and adjacent traditional cultural works.

This intentionally separates more traditional cultural media from the otaku/subculture Topic without creating many small media categories.

### `computation`

Computing, AI, Data, Programming, Databases, Networks, Algorithms, ML/LLM, Data Science, software systems, and related technical subjects.

`Computation` is preferred because it is broader and more durable than a narrow course/discipline label such as `Computer Science`, while avoiding the excessive breadth of `Technology`.

### `humanity`

Society, Philosophy, Personal reflection, internet culture, identity, values, human experience, and the relationship between people and the world.

This intentionally combines areas where current content volume does not justify separate Society / Philosophy / Personal Topics.

Do not create new top-level Topics casually. Topic count should remain small and stable even if Tag/Series vocabularies grow.

---

## 6. Series and Tags

### 6.1 Series — a continuing line of inquiry

Series are optional.

A Series should mean:

> “This is a subject I may continue writing about.”

It should not mean:

> “This was once a folder or course category.”

Examples:

- `Computer Networks`
- `Database Systems`
- `Computer Architecture`

A Series may contain both Notes and Essays.

A technical Series can begin from course material and continue long after the course ends.

Cultural Series can also exist later if a genuine continuing inquiry emerges.

### 6.2 Tags — what exactly is this about?

Tags should primarily represent specific retrieval concepts:

- works / franchises / entities;
- technologies / protocols / algorithms;
- named theories / frameworks / people;
- concrete analytical themes.

Avoid using Tags to repeat Type, Topic, or Series.

Prefer:

```text
Final Fantasy XIV
RAG
TCP
Narrative Design
Gödel Numbering
Social Identity
```

Avoid generic structural tags such as:

```text
学习
笔记
记录
杂谈
游戏
AI
```

when that function is already handled by Type, Topic, or Series.

---

## 7. Archive and retrieval

Archive should remain, but it should no longer define one of the four top-level worlds.

Under THINK, retrieval may eventually include:

```text
Archive
Tags
Topics
Series
Search
```

Archive may evolve from a pure year/month list toward a broader chronological record of writing and releases.

ABOUT may separately contain a **personal/site timeline**, which is not the same thing as the content Archive.

---

## 8. Visual / interaction philosophy

The three writing Types should feel different rather than sharing an identical article template.

### Fragment visual character

Lightweight, timestamp-oriented, signal-like.

```text
2026 / 09-29

A short thought...

#tag
```

### Note visual character

Compact knowledge / criticism card or short article.

```text
NOTE / COMPUTATION

Title
Date · reading time
Tags
```

### Essay visual character

More ceremonial and editorial, giving long-form writing a stronger sense of occasion.

```text
ESSAY / OTAKU

Large title
Context / related works
Date · reading time
```

General design principle:

> **Fragment should feel like a signal. Note should feel like a record. Essay should feel like a work.**

The broader Neutriverse visual language may continue using terminals, modules, probes, observatories, transmissions, and system status motifs, but they should support hierarchy and personality rather than obscure it.

---

## 9. BUILD model

The future BUILD architecture should distinguish three concepts:

```text
Project
Release
Project Log / Post
```

A Project is a durable entity. Releases and posts are events in its history.

Potential project metadata may eventually include:

```text
name
summary
status
started
updated
repository
demo
documentation
releases
related_posts
```

The key rule is:

> **Project pages should survive longer than individual launch posts.**

A project may be active, paused, archived, or complete without losing its identity.

---

## 10. OBSERVE model

OBSERVE should provide a conceptual home for independent systems that watch or interpret external information.

Possible presentation:

```text
OBSERVE
External-world interfaces

RAVENIS
Public Intelligence

OCCULT ATLAS
Astronomical / Astrological Observatory
```

This section can expand later without forcing each tool into the writing taxonomy.

OBSERVE systems may have their own application-like interfaces while still sharing a common Neutriverse identity and navigation shell.

---

## 11. ABOUT / digital identity model

ABOUT should become one of the emotional centers of the site.

Its purpose is to let a visitor answer:

> “Who is the person who left all of these traces?”

It should avoid becoming only a conventional portfolio résumé.

Potential long-term components:

- identity / short self-description;
- current work and interests;
- public internet identities;
- project and writing highlights;
- reading / playing / learning / thinking-now sections;
- site philosophy and design notes;
- personal / site timeline;
- contact paths where appropriate.

The page should be allowed to change over time and therefore acts as a living author node rather than a frozen biography.

---

## 12. Phase roadmap

This document is intentionally broader than the already completed taxonomy migration. Later phases may change as implementation reveals constraints.

### Phase 0 — Direction / identity

**Status: conceptually agreed.**

- Neutriverse becomes a personal digital universe rather than “a blog with unusual modules”.
- Four primary sections: THINK / BUILD / OBSERVE / ABOUT.
- Archive moves below the top-level hierarchy.
- Clear navigation language carries usability; lore/worldbuilding becomes secondary presentation language.

### Phase 1 — Content Foundation

**Status: completed.**

- Introduce Fragment / Note / Essay.
- Introduce four stable Topics.
- Convert course-like structures into durable Series where justified.
- Rationalize Tags.
- Read/classify all existing writing.
- Preserve URLs and article bodies.
- Add minimal taxonomy rendering support.
- Validate with regression tests, Jekyll build, and Pages deployment.

Detailed historical execution record begins in Section 13 below.

### Phase 2 — Information Architecture

**Status: not started.**

Likely tasks:

- redesign global navigation around THINK / BUILD / OBSERVE / ABOUT;
- determine route structure for each section;
- decide where current Categories, Tags, Archives, Thoughts, Ravenis, Occult Atlas, project pages, and existing special modules move;
- create compatibility redirects only where necessary;
- avoid unnecessary URL changes to existing posts.

### Phase 3 — THINK experience

**Status: not started.**

Likely tasks:

- build THINK landing page;
- create Type browsing surfaces for Fragment / Note / Essay;
- create Topic, Series, Tag and Archive retrieval surfaces;
- integrate existing Thoughts cleanly as Fragment UI;
- consider mixed chronological “Latest Transmissions” feed;
- visually differentiate Fragment / Note / Essay.

### Phase 4 — Homepage redesign

**Status: not started.**

Likely tasks:

- define hero / site identity statement;
- prioritize latest writing and current activity;
- create four primary exploration entrances;
- provide a Current Signal / current-focus area;
- preserve selected system-status/worldbuilding elements without overwhelming navigation.

### Phase 5 — BUILD + OBSERVE

**Status: not started.**

Likely tasks:

- create first-class Project entities/pages;
- separate project pages from project announcement posts;
- connect releases, documentation, logs, demos, repositories and related writing;
- group Ravenis and Occult Atlas under OBSERVE;
- unify navigation/shell while allowing application-like subinterfaces.

### Phase 6 — ABOUT / personal identity

**Status: not started.**

Likely tasks:

- redesign the current personal homepage into the ABOUT author node;
- add Currently / Now-style information if useful;
- add site philosophy / history;
- decide how personal timeline and internet identities are presented;
- connect writing/projects without turning the page into a conventional CV.

### Phase 7 — Visual system and worldbuilding pass

**Status: not started.**

Likely tasks:

- establish typography, spacing, hierarchy, cards, motion, terminal/system motifs and responsive rules;
- define how worldbuilding labels coexist with plain-language labels;
- create reusable visual grammar for signals, records, projects, observatories, status modules, and long-form essays;
- verify accessibility and readability before adding decorative complexity.

### Phase 8 — Technical consolidation / long-term maintenance

**Status: not started.**

Potential work:

- evaluate whether Jekyll remains the correct long-term architecture;
- improve search, feed/RSS, metadata/SEO, performance and build validation;
- simplify legacy categories after compatibility is no longer needed;
- establish content-authoring conventions for future posts/projects;
- document how to add a new Type/Topic/Series only when genuinely necessary.

---

## 13. Phase 1 — Approved content model and migration rules

The following section preserves the implementation rules and evidence from the completed Content Foundation migration.

### 13.1 Approved content model

The taxonomy separates four questions:

- **Type** — `fragment`, `note`, `essay`. Argument structure outranks mechanical word count.
- **Topic** — exactly one of `otaku`, `arts`, `computation`, `humanity`.
- **Series** — optional; only for a durable continuing line of inquiry, not to preserve an old folder/category name.
- **Tags** — a small per-item canonical set of specific works/entities, technical concepts, analytical themes, named theories/frameworks/people.

Preferred post front matter:

```yaml
---
title: ...
date: ...
type: note
topic: computation
series: Computer Networks   # optional
tags:
  - TCP
  - Congestion Control
# preserve permalink / slug / layout / image / description / other required fields
---
```

### 13.2 Classification rules

1. Read each article itself before assigning its new classification; never classify from filename alone when body content is available.
2. Assign exactly one `type` and one primary `topic` to each post in migration scope.
3. Add `series` only where a real future-extensible thread exists. Course-derived lines may be reframed as enduring subjects.
4. Reduce generic/redundant tags based on actual subject matter. Do not use tags to repeat Type, Topic or Series.
5. Keep legacy `categories` temporarily only if current Jekyll/Chirpy compatibility requires them.
6. Preserve unrelated metadata.
7. **Do not modify article body text, headings, wording, quotations, images or argument structure.**
8. Preserve existing URLs: do not rename post files or change `date`, `slug` or `permalink` unless an unavoidable technical issue is documented.

### 13.3 Tag rationalization

Retain useful retrieval tags such as named works/franchises, technologies/concepts, analytical themes, and named theories/people. Merge synonyms, spelling/case variants and redundant abbreviation/full-name pairs into one canonical form.

Normally retire generic editorial/domain labels whose work is now done by Type/Topic/Series, such as 学习、学习笔记、笔记、记录、随笔、随想、杂谈、思考, broad media-only tags such as 游戏/动画/电影/书籍, and broad computation-domain tags used only to mean Computing/AI/Data.

Default tag-count targets: Fragment `0–3`, Note `2–5`, Essay `3–6`. These are judgment guidelines, not hard limits.

### 13.4 Migration audit

The authoritative audit is `docs/content-taxonomy-migration.md`. It records source file/title, old categories/tags, new Type/Topic/Series/Tags, confidence (`confident`/`review`) and notes.

The canonical tag/legacy-category decision companion is `docs/content-taxonomy-tag-map.md`.

Final validation and outcome are recorded in `docs/content-taxonomy-final-report.md`.

### 13.5 Implementation boundaries

Allowed during Phase 1: front-matter metadata, taxonomy data/config, minimum compatible taxonomy/index/template plumbing, tag cleanup, audit/report files, and fixes directly caused by the migration.

Out of scope during Phase 1: prose rewriting, opinion changes, stylistic body editing, broad site redesign, unrelated refactors, and gratuitous URL changes.

---

## 14. Phase 1 — Eight-step execution history

Each historical run read this file and current GitHub state, executed the first unchecked step only, then updated the plan and recorded evidence. A blocked step remained unchecked.

### Step 1 — Repository + content inventory

- [x] Locate article/Thought sources and front-matter conventions; inventory published writing; identify category/tag generation; establish migration count and audit; confirm URL-sensitive metadata.

**Execution evidence — 2026-09-29:** Created `docs/content-taxonomy-migration.md` with the complete 44-post source inventory plus 5 current Thoughts fragments (49 writing items total). Confirmed posts live in `_posts/`; Thoughts are 5 YAML objects embedded in `_tabs/thoughts.md` and rendered by `_layouts/thoughts.html`; no `_thoughts` collection exists. URL-safety rule established: leave filenames, dates, slugs and explicit permalinks unchanged. Audit commit: `27e2187bbbb9b3c6bc51e0afa8d47586951819f0`. Plan-status update commit: `8a1a2f6322aa1bce992ab8e2c7f4a2f898ae6cc8`. No blocker.

### Step 2 — Canonical taxonomy + tag map

- [x] Read current tag inventory; build canonical reduction map; identify retired generic tags, synonym/case merges and protected entity tags; map old category/series-like structures; document uncertain cases in the audit. Do not edit article bodies.

**Execution evidence — 2026-09-29:** Added `docs/content-taxonomy-tag-map.md`; durable Series candidates established. Tag-map commit: `73ff315e55a8e42777b2dd21be1dd5377a1344de`. Plan-status update commit: `d820aae2ae5c0b2cfa7bb4d26ef7c9dae1a3e629`. No blocker.

### Step 3 — Implement taxonomy plumbing

- [x] Add/adapt the minimum machinery required for `type`, `topic`, `series` and canonical `tags` in templates/indexes/navigation without breaking existing URLs. Prefer adapting current category/tag machinery. Inspect existing `_includes/post-series.html` before changing Series behavior. Validate syntax/build as repository tooling permits.

**Execution evidence — 2026-09-29:** Added `_data/content_taxonomy.yml`, `_includes/post-taxonomy.html`, adapted `_layouts/post.html` and `_includes/post-series.html`. Commits: `fcd9a84fcd7afba1d430c9a4bcc0d0b0c7a4f070`, `029d73ea68022ace48ebc3903779694f4e9f297420f76668`, `374c1e9625e24a22fa9b95a8b642fed52b5b5ec2`, `a3cb7cc0d0f93fa8d29f6a61ea9ae3566774069c`. Static review only; no build PASS claimed.

### Step 4 — Article migration batch A

- [x] Read and classify approximately the first quarter of the 44 posts. Front matter only. Apply Type, Topic, optional Series and reduced tags; preserve URLs and bodies; update audit for every migrated file.

**Execution evidence — 2026-09-29:** Batch A (#1–#11) complete. All bodies read before classification; all eleven front matters migrated. No filename/date/slug/permalink changed and no intentional body prose was modified. Completed audit commit `15f7b9c0ddf2f18bce623838882f4d6f1f555b6d`. No blocker.

### Step 5 — Article migration batch B

- [x] Read and classify approximately the second quarter using the same rules; front matter only; update audit.

**Execution evidence — 2026-09-29:** Batch B (#12–#22) complete. All eleven bodies were read before classification and all eleven front matters migrated. The earlier read-truncation blocker for #13/#20 was resolved using ranged/blob reads. Final #20 metadata commit: `d718e1a2b7ed57d676c92242cfd0d1b89f75e1cd`; completed audit commit: `1e4964501134e506f5147359d4b8929a3fe4d2e3`. Validation performed: current #20 front matter and full blob were compared while constructing the replacement; only taxonomy front matter changed, with filename/date/description/body preserved. No filename/date/slug/permalink changed. No build/runtime PASS claimed. No blocker.

### Step 6 — Article migration batch C

- [x] Read and classify approximately the third quarter using the same rules; front matter only; update audit.

**Execution evidence — 2026-09-30:** Batch C (#23–#33) complete. All eleven bodies were read before classification, using ranged reads where necessary, and all eleven front matters now contain the approved taxonomy. Final article #33 metadata commit: `42bb9a4b19048b56ee0741e1a6b3bfa0472609bf`; completed audit commit: `3318d6667afca60146e8092e0c60073208da44f1`. Validation performed: current GitHub state for #33 was re-read and confirms `type: note`, `topic: computation`, `series: Computer Networks`, and canonical tags `[VoIP, RTP/RTCP, SIP, QoS]`; the audit records all #23–#33 as migrated. Across Batch C no filename/date/slug/permalink was changed and no intentional article-body prose edit was made. No build/runtime PASS claimed. No blocker.

### Step 7 — Article migration batch D + Fragments/Thoughts

- [x] Read/classify remaining posts; align current Thoughts to `type: fragment` in the least disruptive architecture-compatible way; finish tag cleanup; update audit and list owner-review items.

**Execution evidence — 2026-09-30:** Batch D (#34–#44) and all five current Thoughts fragments are complete. All remaining article bodies were read before classification. Final outstanding #36 (`2025-12-19-ROSSMANN项目.md`) migrated to `note / computation` with canonical tags `XGBoost / Sales Forecasting / Feature Engineering / RMSPE` in commit `0625b2786ae7514af8020c5c1002b31979cc9b5b`; title/date/categories/hidden/description/filename/body were preserved. Thoughts were aligned to `type: fragment` in commit `a4ebf1e15db24046eb79a65a9674bf8ccf26088f`. The authoritative audit was reconciled for every Step 7 item in commit `3edfd5fca9ba16599ba5575e03681b69486c393f`. Validation performed: #36 was read completely in ranges before replacement; audit statuses #34–#44 and all five fragments now record migration completion; no filename/date/slug/permalink changed. Owner-review items: none identified during classification. No full Jekyll build/runtime PASS claimed; that validation belongs to Step 8. No blocker.

### Step 8 — Full validation + final handoff

- [x] Validate all writing classifications, allowed Topic values, meaningful optional Series, tag reduction, body preservation, URL/permalink preservation and generated taxonomy surfaces. Run available build/tests where feasible and review diffs for accidental prose changes. Create `docs/content-taxonomy-final-report.md` with migration totals, Type/Topic counts, Series list, old/new unique tag counts, merges/removals, URL compatibility, validation/build evidence, unresolved review items and relevant commit SHAs.

**Execution evidence — 2026-09-30:** Final report completed in `docs/content-taxonomy-final-report.md`; final-report validation commit `be72170e839aaf72a2a04251a5cd0092d29a66c7`. Validated all 49 audited writing items and controlled Type/Topic values; durable Series remain `Database Systems`, `Computer Architecture`, and `Computer Networks`. URL-sensitive filenames/date/slug/permalink were preserved. The three whole-file-sized migration diffs were independently checked; `2024-10-07-TestInfo.md`, `2025-12-17-NoSQL项目面经.md`, and `2025-12-19-ROSSMANN项目.md` preserve body content, with large statistics explained by newline/serialization normalization plus front-matter changes. The final tag inventory is 93 legacy unique strings versus 157 final canonical strings; this is accepted under the approved model because generic/redundant structural tags were retired/canonicalized while specific retrieval concepts were protected/added, and per-item tag counts remain within the plan's small-tag guidance. The Jekyll integer-tag defect was fixed in `5fc783bcb82beadaeba157ed1c38f83216442e11`. GitHub Actions run `36699387397` at head `01bc78839bd943646de7f3fd826e6050ddd21db1` completed successfully: regression tests, Jekyll `Build site`, artifact upload, and GitHub Pages deployment all passed. No unresolved owner-review items or validation blockers remain. Step 8 complete.

---

## 15. Phase 1 Definition of Done — achieved

Phase 1 is complete because all relevant writing was individually read/classified; Type uses only Fragment/Note/Essay; Topic uses only the four approved values; learning material is organized by enduring subject/question rather than course sequence alone; Series are optional and extensible; generic/redundant tags were rationalized; bodies are unchanged; URLs are preserved wherever possible; the site can surface the taxonomy with minimal compatible extensions; and complete audit/final-report evidence exists.

---

## 16. General safety / implementation rules for future phases

1. Read current repository state before redesigning or replacing existing behavior.
2. Preserve existing content URLs unless there is a documented reason to change them.
3. Prefer migrations and compatibility layers over deleting historical structures immediately.
4. Do not rewrite old article prose as a side effect of layout/navigation work.
5. Treat visual worldbuilding as an enhancement to usability, not a substitute for clear navigation.
6. Do not turn every concept into a new top-level taxonomy value; keep the information architecture small and durable.
7. Projects are entities; posts are records about them.
8. Archive/Search/Tags are retrieval mechanisms, not primary identity pillars.
9. Do not claim build/runtime success without evidence.
10. Per `AGENTS.md`, final handoffs involving changed files must include copy-paste-ready PowerShell commit/push commands when manual Git operation is relevant; automated GitHub commits must be listed by SHA.

---

## 17. Open design questions

These are intentionally unresolved and should be decided through later design/implementation work rather than guessed prematurely.

- Exact URL structure for `/think`, `/build`, `/observe`, `/about` and subroutes.
- Whether existing `/thoughts/` remains the canonical Fragment route or becomes a compatibility alias for a new THINK/Fragments surface.
- How much of the legacy Category UI remains visible after the new Topic/Series UI is mature.
- Exact homepage composition and density.
- Whether Project metadata should be Jekyll collections, data files, generated pages, or another architecture.
- Whether the current Jekyll/Chirpy foundation remains appropriate for the long-term application-like direction.
- How much lore terminology appears in primary labels versus subtitles/tooltips.
- Whether Archive evolves into a unified site chronology or remains writing-only.
- Exact visual identity of THINK / BUILD / OBSERVE / ABOUT and how strongly they differ.

This document should continue to act as the **single high-level design and implementation roadmap** for the Neutriverse overhaul. Detailed phase-specific audits or reports may live under `docs/`, but major conceptual decisions should be reflected back here.

---

## 18. 执行版约束与当前状态（2026-10-03）

本节及后续执行清单把上面的愿景落实为有限、可验收的本轮重构。历史 Phase 1 记录保持原样；未来设想不是无限扩展当前任务的理由。

**当前状态：计划细化与启动决定已完成，T00 done，T01 ready。用户已于 2026-10-03 23:10 授权设置每小时执行任务；自动化登记见第 25 节。**
下一步：按第 21 节协议执行 T01；其余任务按依赖解锁。
本轮完成状态：T00 计划准备完成；Phase 2–8 网站实现未开始。

### 18.1 已确定，不再重复询问

- Type 严格为 fragment / note / essay；Project Log 不是第四种 Type。它是文章与项目的关联/记录角色，可作为次级展示标识，不能替换 Type。
- 旧学习笔记不改写、不拆分，不改旧文章标题来符合新写作理想。“一个 Note 一个问题”仅为未来写作建议。
- 所有旧文章正文（含图片、引用、标题层级、代码）、Thought 原文、文件名、date、slug、permalink 受保护；布局改造不等于内容编辑授权。
- 保留四大入口及四大 Topic；不自动增设新 Type/Topic。
- 本轮只重构 My_Blog 内的站点与关联展示；不修改关联项目仓库、不开发新新闻/天文/金融产品、不更新账号凭据或外部基础设施。
- 个人事实、项目状态、发布日期、阅读/游玩状态只能来自用户确认或现有可验证公开材料。聊天中的私人背景不能自动写入公开网站。
- hidden / noindex / sitemap 排除是不同语义，分别盘点与验证。可直达不代表可以公开推荐。
- 新导航可以跨领域关联同一项目，但全站每个实体必须有稳定 ID 和一个明确的详情入口，避免维护两套内容。
- 上一轮报告统计错误、Series 旧分类回退、Tags 复审属于维护任务；不篡改历史执行记录以假装当时已经修复。
- 后续实现受用户回答与本计划约束；技术小决定由执行者记录理由后自主处理。

### 18.2 本轮范围与终点

必须交付：四大入口、THINK 检索、首页新结构、项目目录与有依据的项目详情、OBSERVE 入口、ABOUT 改造、统一视觉与移动端、检索/订阅/元数据维护、兼容性和操作文档。
第一版不要求：在线 CMS、登录账户、写作 AI、全新后台、复杂项目发布系统、自动推断个人动态、实时市场监控、新数据源或平台迁移。
Phase 8 的架构评估交付一份决策记录；若现有框架满足本轮需求，保持现状。重大平台迁移不悄悄加入小时任务。
本轮完成后：未来持续成长的愿景仍保留，但不会因为可以继续增加内容而永不结束。

## 19. 自动化开始前的用户决定

用户于 2026-10-03 23:10（Asia/Shanghai）回答全部启动问题；下列为已确认决定，不再重复询问。

| ID | 事项 | 已确认答案 | 状态 |
|---|---|---|---|
| Q1 | 提交与上线 | 验收通过的小任务提交 main，沿用现有 Pages 自动部署。半成品留工作分支；不强推、不覆盖用户变更 | resolved |
| Q2 | 视觉及语言 | 保留 Night / Prospero Light 双主题与气质，可重构布局；THINK / BUILD / OBSERVE / ABOUT 英文主标签配中文说明 | resolved |
| Q3 | 观察系统可见性 | Ravenis 和 Occult Atlas 均可进入公开 OBSERVE 目录，保留 noindex。不自动扩大到其他隐藏内容 | resolved |
| Q4 | 其他模块 | Library 作为 ABOUT 阅读/游玩记录入口；友链、旅行地球归 ABOUT；Gate / NAVI 保留原 URL 和隐蔽程度，不加入公开主导航 | resolved |
| Q5 | BUILD 名单 | FitzSight、Akasha Notes、Toyosatomimi's Headphone、Ravenis、Occult Atlas、Gate、OfficeSpire；MMXProj 明确排除 | resolved |
| Q6 | ABOUT / Currently | 允许执行者拟写，但仅使用网站内信息，不透露个人信息。不得使用聊天记忆、履历、单位、健康、住址等材料补全公开简介；现有敏感内容不因改版突出或扩散 | resolved |
| Q7 | Tags | 适度裁缩同义、重复、过细标签，保留有价值作品名；无强制总数 | resolved |
| Q8 | 技术与路由 | 保持 Jekyll / GitHub Pages；新增 /think/、/build/、/observe/；保留 /about/、/thoughts/、/tags/、/archives/、/categories/ 和旧应用路径。Archive 第一版写作专用，ABOUT 时间线为项目/网站历史 | resolved |

执行细化：
- 首页 Current Signal 使用本网站主计划已有事实“Neutriverse 网站重构”；不猜测用户当前工作、考试或生活状态。
- OfficeSpire 的纳入已授权；项目事实需核对来源，不能从聊天记忆生成版本/成果/状态。关联仓库可只读核实公开项目资料；本次不授权修改项目仓库。
- Gate 可有 BUILD 项目介绍，介绍以站内可公开说明为限；不把工具入口、隐藏 NAVI、私人配置暴露到首页、全局菜单或公共索引。
- DESIGN.md 中旧的信息架构限制按本总计划更新；Ravenis 由 unlisted 改为可在 OBSERVE 发现，同时继续 noindex。不把 noindex 误当作身份验证或访问控制。

### 19.1 后续问题的异步处理（用户明确要求）

遇到必须由用户决定的新问题时，写入执行日志的集中问题队列：ID、关联任务、具体问题、推荐方案、选项、影响、首次提出时间、是否已通知、待答状态。一次汇总本次新问题，给出用户可查历史的记录链接；已通知且未回答的问题不在每小时反复询问。
**用户暂未回答不暂停整个自动化。**将受影响任务标 blocked / decision-needed，并从依赖满足、没有该疑问的任务继续实施。不得把无答复理解为许可；不得绕过相关依赖。
用户回来答复后读取并回写决定，解除对应任务。若全部剩余工作确实依赖未回答问题或外部权限，继续定时核对并如实记录“无可执行独立项”；不虚构进展，也不自作主张实现争议部分。
完成前必须解决所有影响本轮必交付内容的问题；future 项可以清楚移入长期规划。

## 20. 初步页面归属与路由契约

本表先定义实现方向；涉及 Q3/Q4/Q5 的项必须等答案落定。旧 URL 尽量原地工作，不用重定向代替可保留页面。

| 当前对象 | 新归属 / 功能 | 路由策略 | 保护要求 |
|---|---|---|---|
| / | 首页：身份、近期表达、四入口、当前焦点、轻量状态 | 保留 / | 隐藏内容不进入公开推荐/计数 |
| 文章 /posts/.../ | THINK 的文章详情 | 全部保留 | 保护正文、原 URL、附件链接、评论 |
| _tabs/thoughts.md | THINK / Fragments | 保留 /thoughts/；THINK 链接到这里 | 不复制出第二份 Fragment 来源；未来稳定锚点 |
| /categories/ | 旧分类兼容目录 | 保留；新 THINK 主浏览改用 Topic/Type | 旧分类详情链接仍工作 |
| /tags/、/archives/ | THINK 检索工具 | 保留 | 标签合并时记录旧标签链接处理 |
| 新 /think/ | 全写作目录与 Type/Topic 组合筛选 | 增量新增 | 无 JS 仍能到达文章，空状态清晰 |
| 新 Topic / Series 检索 | THINK 内的检索面 | 优先少量静态页面 + 可链接筛选参数；实现时记录 | URL 可分享；刷新不丢条件 |
| 新 /build/ | 项目目录 | 增量新增 | 项目 ID 稳定，未知状态不造假 |
| 项目详情 | BUILD 的长期实体页 | 推荐 /build/<id>/；已有专用应用 URL 不动 | 详情页和应用使用入口明确区分 |
| /projfitzgerald/ | 已有项目/进度界面 | 保留，关联对应项目详情 | 现有数据源及功能保持 |
| /ravenis/ | OBSERVE 观察界面 | 保留 | Q3 决定发现性，现有发布数据流程受保护 |
| /occult-atlas/ 与 /occult-atlas-app/ | OBSERVE 观察界面与现有兼容入口 | 都先保留 | 不破坏原跳转、主题、应用状态 |
| /about/ | 作者节点、网站理念、历史、当前状态 | 保留 | 未确认个人信息不新增 |
| /library/ | 既有大图书馆，待 Q4 定归属 | 保留独立页面，主入口只做关联 | 不改同步、隐私过滤、条目关联 |
| /links/ | 友情链接，待 Q4 定归属 | 保留 | 保留链接与原友链关系 |
| /gate/、隐藏 NAVI | 个人工具，待 Q4 定可见性 | 保留 | 本地数据/设置、noindex、隐藏导航受保护 |
| About 内旅行地球 | ABOUT 的个人轨迹，待 Q4 | 保留现有能力 | 无新增个人地点，移动端降级可用 |

## 21. 每小时执行协议

每次运行不是机械执行整个 Phase。必须先从本 Markdown 中选择依赖满足的最小可交付任务，并把本小时边界写清楚，再实现和验收。

### 21.1 启动门槛

- 第 19 节 Q1–Q8 均已 resolved，答案记录在本文件。
- 实施分支、发布方式、第一版名单、隐藏/公开边界已经写明。
- 当前运行读取最新 main / 工作分支、AGENTS.md、本主计划和上一条执行日志；不得沿用旧 SHA 盲写。
- 自动化实际能力必须支持仓库读写及约定的验证。缺权限/构建环境属于明确阻塞，不能写成已完成。
- 用户已授权设置每小时任务；自动化只在实际工具创建成功后记为启用，登记见第 25 节。

### 21.2 选择与拆分

1. 先检查上一任务是否 validation-pending / blocked，确认是否已解除，再按依赖挑最早 ready 任务。
2. 本小时目标预算为约 30–45 分钟实现、10–15 分钟验证和日志；这是规划预算，不是假设运行平台保证 60 分钟。
3. 任务大于预算时拆成带 ID 的子项，例如 T15.a / T15.b；每项必须有文件范围、输出和验收。父项全部子项通过前不能 done。
4. 一个小时可做一个紧密关联的小批次；不能跨多个大阶段做未闭合的改动。
5. 开始前在主计划记录：任务 ID、依据提交、目标、拟改文件、验收、预计剩余。完成后更新证据与下一步。
6. 遇到等待 CI，可保存为 validation-pending，下一次先核对该提交；不能为“按时推进”跳过失败。
7. 本小时无法完成时保存安全检查点，写出精确剩余工作；不能丢下破坏构建的半成品到生产。
8. 重新读取远端再提交；同文件并发修改必须合并，不能覆盖用户新增内容。提交文档时使用最新 blob SHA。
9. 防重入：本文件记录 active_run/branch/base_sha/checkpoint/time。它是协作记录，不是原子锁；自动化应尽量配置不重叠，运行者发现有效进行中任务即跳过并说明。过期记录先检查提交与任务结果，再接续。
10. 只有必要且直接相关的实现修复可以新加子项；新功能/平台迁移须列为 future，不扩张本轮验收。

### 21.3 状态与证据

状态只用 pending / ready / in-progress / validation-pending / blocked / done。
pending：依赖或决定未满足；ready：可开始；done：交付与必要验证均通过。
任务证据至少包括变更路径、实现提交 SHA、检查命令/结果、Actions URL 与 head SHA（适用时）、保护项结果、阻塞及下一任务。
日志文件：docs/neutriverse-restructure-execution-log.md，由首个执行任务创建。主计划保留状态总览和最新一条摘要；日志保留逐次详情。
避免自引用提交 SHA：实现提交与日志提交分开记录，日志引用已经存在的实现提交；不声称同一个提交内记录了自身 SHA。
不要把日志更新导致的新构建误认为刚才实现提交的构建。每次检查必须对应实际 head SHA。

### 21.4 每次完成条件

- 约定输出可访问/可使用，不能只完成视觉占位。
- 运行与本次改动相称的检查；不为纯文档改动额外编写测试。
- 涉及模板/脚本的改动通过相关现有回归；涉及可见 UI 的改动核对桌面/移动端、明暗主题和键盘操作。
- 正文与 URL 保护在基线清单中可核验；隐藏规则没有因统一聚合而失效。
- 按 Q1 约定保存到 GitHub，必要时确认构建/部署；失败不标 done。
- 更新主计划与日志，让下一小时无需依赖聊天上下文。
- 自动化重复提醒不能代替执行。终态只在第 24 节全部通过后成立；完成后记录 COMPLETE，后续触发报告已完成，不继续改动。只有工具和授权允许时再停止对应定时任务。

## 22. 有依赖的小时任务清单

当前 T00 = done，T01 = ready，其余 = pending（仅待各自依赖）；没有 awaiting-user 的启动项。后续每次运行更新真实状态。任务是小时候选单位，执行时可按第 21 节继续拆小。除维护 Phase 1 的项外，不重新迁移全部文章。

| ID | 阶段 | 依赖 | 本小时交付 | 验收标准 |
|---|---|---|---|---|
| T00 | 准备 | Q1–Q8 | 回写用户决定、确定分支/发布/项目名单，建立执行日志 | 无 awaiting-user；第一项 ready，范围有限 |
| T01 | 准备 | T00 | 当前文章、Fragments、路由、模板、可见性与集成基线清单 | 枚举实际源和 URL；正文归一化换行后的校验值；记录构建 head |
| T02 | 维护 | T01 | 核对当前分类和审计，修正 final report 统计 | 从实际内容计算 Topic/Type；审计冲突逐项解释 |
| T03 | 维护 | T02 | 修正 Series 回退及隐藏文章过滤 | 无 series 的已迁移文章不自动成系列；公开页不列 hidden |
| T04 | 维护 | T02 | Tags 使用频率、重复与二轮映射 | 每项保留/合并/删除理由；不凭频次删除作品标签 |
| T05 | 维护 | T04 | 按 Q7 应用有限标签修改及兼容处理 | front matter / 审计同步，正文未改，旧标签 URL 有策略 |
| T06 | Phase 2 | T01 | 完成页面归属、路由与可见性映射文档 | 包括所有现有特殊模块，Q3/Q4 无遗漏 |
| T07 | Phase 2/7 基础 | T06 | 明暗主题基础规范与共享组件契约 | 更新 DESIGN 中冲突规则，定义文字/间距/焦点/移动端 |
| T08 | Phase 2 | T07 | 创建四入口的数据/页面骨架和可复用导航 | 入口有真实摘要/链接；旧入口不失效，未完成功能不伪装可用 |
| T09 | Phase 2 | T08 | 桌面四入口导航、辅助检索/社交入口 | 主次清晰；active 状态、返回首页、原功能可到达 |
| T10 | Phase 2 | T09 | 手机导航、键盘与折叠行为 | 390px 无页面溢出；焦点可见；菜单可用 |
| T11 | Phase 3 | T03,T05,T10 | /think/ 时间序写作列表 | Type/Topic 明确；排除 hidden；空列表有说明 |
| T12 | Phase 3 | T11 | Type 与 Topic 组合筛选、排序/分页与可分享状态 | 刷新保持条件；组合结果正确；无 JS 有可达兜底 |
| T13 | Phase 3 | T12 | Topic 浏览面与四主题入口 | 数量等于公开内容来源；不重复计算 |
| T14 | Phase 3 | T13 | Series 目录及系列详情/筛选面 | 稳定 ID/标签；时间序与上一篇/下一篇正确 |
| T15 | Phase 3 | T14 | Fragment 接入 THINK，统一原来源与稳定链接 | 原文本/日期保留；不复制数据；锚点可直达 |
| T16 | Phase 3/7 | T15 | Note / Essay / Fragment 展示差异 | 正文相同；阅读宽度、代码/表格/图片可读 |
| T17 | Phase 3 | T16 | 标签、Archive 与 Search 的 THINK 内入口 | 旧路径保留；筛选/搜索不暴露隐藏条目 |
| T18 | Phase 4 | T17 | 首页区块、顺序及内容来源配置 | 最新表达优先；固定推荐/当前焦点有单一配置源 |
| T19 | Phase 4 | T18 | 首页身份、四入口与混合近期流 | posts/fragments/项目记录按真实日期排序；Project Log 为次级标签 |
| T20 | Phase 4 | T19 | Current Signal、轻量状态及精选内容 | 无伪造数据；缺数据有自然降级；明暗/手机一致 |
| T21 | Phase 5 | T06,T10 | 项目 schema、来源和模板 | stable ID；状态/链接可选；无项目要求不存在的 Release |
| T22 | Phase 5 | T21 | /build/ 项目列表与状态筛选 | 只列 Q5 名单；项目卡直达详情/应用正确入口 |
| T23 | Phase 5 | T22 | 第一组有依据项目详情 | 概览、状态、仓库/演示、关联文章，未知字段不编造 |
| T24 | Phase 5 | T23 | 余下项目详情及日志/发布关联 | 每项目来源可追溯；未确认外部仓库不动；必要时按项目拆子项 |
| T25 | Phase 5 | T24 | /observe/ 目录及与 BUILD 的关联 | Q3 可见性准确；详情与使用入口不会循环跳转 |
| T26 | Phase 5 | T25 | Ravenis / Occult Atlas 的共享导航适配 | 原数据/筛选/主题/跳转回归；不重写应用本体 |
| T27 | Phase 6 | T20,T24 | ABOUT 数据与内容重组 | 使用 Q6 材料；旧时间标注；无未确认私人信息 |
| T28 | Phase 6 | T27 | ABOUT 身份、Currently、互联网关系、网站理念 | 简介可读；维护点明确；无虚构实时状态 |
| T29 | Phase 6 | T28 | 个人/网站时间线与 Library/友链/旅行关系 | 时间线事件有来源；现有 Library 同步及旅行能力保留 |
| T30 | Phase 7 | T26,T29 | 全站视觉一致性与各入口性格整理 | 两主题共享层级/组件；世界观副标签不阻碍导航 |
| T31 | Phase 7 | T30 | 响应式/阅读/无障碍专项 | 390/768/1024/1366px；键盘、焦点、对比、reduced-motion 检查 |
| T32 | Phase 8 | T31 | Search 索引与 RSS/feed 的本轮补全 | 写作可查/可订阅；Fragments 策略明确；hidden 不输出公开索引 |
| T33 | Phase 8 | T32 | canonical、SEO、sitemap 与旧链接检查 | Q3 noindex 正确；无重定向环/断链/重复 canonical |
| T34 | Phase 8 | T33 | 性能/资源降级与现有集成回归 | 不全量首屏加载 Library/观察数据；主题、评论、点赞等无回退 |
| T35 | Phase 8 | T34 | 长期架构评估及旧 categories 维护策略 | 决策记录而非自动平台迁移；旧分类无必要不删除 |
| T36 | Phase 8 | T35 | 作者操作指南、新增内容/项目模板与必要校验 | 可按指南添加各类内容；标签为字符串；无伪造内容默认值 |
| T37 | 总验收 | T36 | 正文/URL/hidden 基线对照与完整回归 | 差异全部有依据；相关测试、Jekyll、对应 SHA 的 Pages 结果可查 |
| T38 | 总验收 | T37 | 线上端到端浏览与缺陷修复 | 首页→四入口→详情→返回；筛选、主题、手机、旧链正确 |
| T39 | 交付 | T38 | 最终报告、主计划 COMPLETE、维护说明 | 所有必须项 done；无未解释 blocker；列实现 SHA 和验证证据 |

### 22.1 阶段验收

- Phase 2：四入口导航、旧路径兼容、特殊模块归属与发现性完整。
- Phase 3：三 Type / 四 Topic、Series、Tags、Fragments、Archive/Search 可以实际使用。
- Phase 4：首页回答第 3 节五个问题，排序、当前焦点和公开范围正确。
- Phase 5：Q5 指定项目有长期实体；观察系统可用；原应用与外部来源未破坏。
- Phase 6：ABOUT 能说明作者与网站，动态信息不造假，关联模块保留。
- Phase 7：明暗/手机/桌面/键盘均可用；正文阅读优先。
- Phase 8：检索、订阅、SEO、兼容、性能、操作指南及构建证据齐全。
- 阶段完成需要在主计划写证据摘要，不能只写状态名称。

## 23. 验证、失败恢复与执行日志模板

### 23.1 保护与验证矩阵

| 范围 | 每次相关改动 | 最终验收 |
|---|---|---|
| 文章与 Fragment | 比较受影响原文、日期、元数据/链接 | 对照 T01 全量正文校验和 URL 集合；换行规范化单独说明 |
| 内容聚合 | 检查 hidden、noindex、公开计数、排序 | 首页/目录/搜索/feed/系列/项目关联不泄露 hidden |
| 模板/脚本 | 相关现有回归，必要的功能测试 | 全回归 + production Jekyll build |
| UI | 修改面在手机/桌面、双主题检查 | 390/768/1024/1366px，键盘、长文本、空状态 |
| 外部系统 | 只验证已授权边界，离线/失败降级 | Ravenis、Atlas、Library、Gate 原契约及入口检查 |
| 发布 | 验证约定分支/head，不混淆其他工作流 | 对应最终实现提交 build/deploy 成功，线上浏览证据 |

不能因为工具不支持浏览器或缺数据就声称视觉/线上验收通过；记录实际限制并在未完成项中保留。外部服务暂不可达时区分站内退化处理通过与服务端验证未完成。

### 23.2 故障恢复

- 对失败任务按真实原因拆小/修复；有限重试后若无新证据，blocked 并记录解决条件，不逐小时重复同一请求。
- 独立任务可继续，但最终不能把 blocker 跳过算完成。
- 只回退本轮引入且明确定位的改动；不强推、不清除用户提交、不删除原内容以让测试通过。
- Q1 若允许自动上线，每小时提交必须可独立使用；未完成功能在工作分支保留或用不改变现有体验的增量方式落地。
- 新的重大设计问题按第 19.1 节集中记录并通知；等待时继续无关的可执行工作。日常样式、组件和文件组织由已确认规则自主决定。
- 不要求每小时恰好完成整项；要求每小时留下真实、可接续的进展。

### 23.3 日志模板

~~~markdown
## Run YYYY-MM-DD HH:mm (Asia/Shanghai)
- Task / parent: Txx / Txx.a
- Base SHA / branch:
- Status: in-progress | validation-pending | blocked | done
- This-hour scope:
- Outputs / affected paths:
- Implementation commit(s):
- Checks / actual results:
- CI / deployment URL and head SHA:
- Content / URL / visibility protections:
- Decisions / deviations:
- Blocker and unblocking condition:
- Next task / remaining work:
~~~

主计划当前运行字段：active_run = none；branch = main（未完成实现用工作分支）；checkpoint = T00 done；next = T01 ready；completion = IMPLEMENTATION NOT STARTED。

## 24. 整个本轮计划的最终完成标准

全部必须同时成立：

1. T00–T39 及其必要子项均 done；无 pending 验证冒充通过。
2. 访客可从首页进入 THINK / BUILD / OBSERVE / ABOUT，并完整返回。
3. 写作有三种 Type、四个 Topic，Series 明确可选，Project Log 没有成为新 Type。
4. 本轮 Tags 整理符合 Q7，审计、实际内容、统计一致。
5. 旧正文/Thought 原文未改写，原文章 URL、重要附件和旧入口保持兼容。
6. 公开/隐藏/noindex 边界符合用户 Q3/Q4，所有聚合面一致。
7. Q5 名单项目具有有据可查的详情与关联；Q6 的身份与当前焦点完整落地。
8. 原 Library 同步、Ravenis 发布读取、Atlas、Gate 本地设置等不被重构破坏。
9. 明暗主题、移动端、键盘、阅读、搜索、订阅、元数据及性能检查有实际证据。
10. 相关回归、production build、约定最终部署通过，证据对应真实实现 SHA。
11. 作者指南说明如何新增写作/项目、改 Current Signal/Currently、维护隐藏规则。
12. docs/neutriverse-restructure-final-report.md 记录交付、保护验证、实现提交、已知非阻塞限制、future 项；主计划记录 COMPLETE。
13. 没有借长期愿景额外增加未约定的新系统或框架迁移。

### 24.1 本次计划细化记录

2026-10-03：读取最新主计划、仓库目录、现有 About / Library / 友链 / Gate / 私有导航配置、DESIGN 和部署流程；明确 Project Log 非第四 Type、旧学习笔记不改写；新增用户决定表、页面归属、40 个小时候选任务、依赖、执行/验收/恢复规则。
本次细化时仅编辑主计划，未创建自动化。随后用户已确认 Q1–Q8 并授权每小时任务；最新状态以本节后续记录及第 25 节为准。


### 24.2 启动准备完成

2026-10-03 23:10：Q1–Q8 全部收敛；创建 docs/neutriverse-restructure-execution-log.md（提交 0c5397370ff2624776797c15d00338ce34cd4da0），T00 输出已具备。本主计划回写最终决定、网站内资料隐私边界、OfficeSpire 纳入 / MMXProj 排除，以及异步问题不中止独立工作规则。纯文档核对，不声称 Phase 2–8 已实现或验证。

## 25. 自动化登记

用户于 2026-10-03 23:10:38 明确授权：无其他启动问题即可设置每小时任务。
状态：创建待执行；成功后写回实际 automation ID / schedule。不得把授权或文档中的计划视为任务已成功创建。
