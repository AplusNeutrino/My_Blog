# Neutriverse Master Restructure Plan

> Status: **living master plan**
> Repository: `AplusNeutrino/My_Blog`
> Purpose: capture the long-term redesign direction for Neutriverse and preserve implementation history
> Current state: **Phase 1 and Phase 2 completed; T00–T31 done; T32 in-progress; implementation decisions resolved; hourly execution authorized**
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

**当前状态：计划细化与启动决定已完成，T00–T31 done，T32 in-progress。用户已于 2026-10-03 23:10 授权设置每小时执行任务；自动化登记见第 25 节。**
最新完成：T31 已把 390/768/1024/1366px × Night/Prospero Light 的首页、四入口和实际文章响应式/阅读/无障碍检查接入 production Pages 门禁，并修正 Prospero Light 接口强调色对比度；精确 CI/Pages 通过。下一项 T32 Search 索引与 RSS/feed 补全。
本轮完成状态：准备、维护项 T01–T05，以及 Phase 2 基线/设计/T08 骨架已完成；其余 Phase 2–8 实现按依赖继续。

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

当前 T00–T31 = done，T32 = in-progress；其余 = pending（仅待各自依赖）；没有 awaiting-user 的启动项。后续每次运行更新真实状态。任务是小时候选单位，执行时可按第 21 节继续拆小。除维护 Phase 1 的项外，不重新迁移全部文章.

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

主计划当前运行字段：active_run = T32-20261008-2056；branch = main；base = 8940a82967b26f1caa154e2a4e189ab981ab71cd；checkpoint = T31 done；next = T32 in-progress；completion = IN PROGRESS.

T32 本次范围：把现有写作发现面收敛为明确的公开策略：Search 索引全部 39 篇公开文章与 5 条 Fragments；`/feed.xml` 继续使用原 URL，并按真实日期输出最近 20 个公开写作项，文章与 Fragment 共用稳定链接，hidden 永不进入两类公开输出。拟新增单一 discovery 配置、覆盖现有 search JSON、提供站内 Atom feed、在页面 head 宣告 feed、增加构建产物校验脚本并接入 production workflow，同时添加静态契约测试；不改正文/Fragment 文本、metadata、旧 URL、hidden/noindex、项目/ABOUT/应用数据或外部仓库。验收为构建后 Search 恰含 44 个唯一公开写作项与 5 个稳定 Fragment 锚点，Atom feed 顺序/上限/自链接/条目链接正确且含 Fragments，不含 5 篇 hidden，回归、T01 baseline、Jekyll、既有浏览器门禁及精确 head Pages build/deploy 成功。预计剩余：实现与验证后 T32 done，T33 ready。

T31 本次范围：建立独立的 production-build 浏览器门禁，在 390/768/1024/1366px 四个视口和 Night/Prospero Light 两主题下检查首页、THINK、BUILD、OBSERVE、ABOUT 与实际文章阅读页。门禁机械核对页面无横向溢出、入口与卡片布局可见、文章正文宽度不超过 740px、富内容被容器约束、主要交互目标不小于 44px、键盘焦点有至少 2px 可见轮廓、关键正文/说明/链接的计算后颜色达到 WCAG AA，并在 `prefers-reduced-motion: reduce` 下关闭 Neutriverse 自有过渡/动画。拟新增专项检查脚本并接入 Pages workflow，补齐共享 CSS 的统一 focus/reduced-motion 规则及静态契约测试；不改内容、路由、分类、项目/ABOUT 事实、隐藏/noindex 边界、应用数据或外部项目。验收为四断点×两主题矩阵真实 Chrome 通过，全套回归、T01 baseline、production Jekyll 与精确 head Pages build/deploy 成功。预计剩余：实现与验证后 T31 done，T32 ready。

T31 验收证据：新增 `tools/check_responsive_accessibility.py` 并接入 production Pages workflow；真实 Chrome 对首页、THINK、BUILD、OBSERVE、ABOUT 形成 4 视口 × 2 主题 × 5 页面 = 40 项布局/对比/焦点检查，并在每个视口/主题读取真实文章验证 ≤740px 阅读宽度、字号/行高、富内容 containment 与横向溢出，同时验证 ≥44px 目标、≥2px 焦点和 reduced-motion。共享 CSS 增加统一 focus/reduced-motion 规则，Prospero Light 的 Neutriverse 接口 accent/focus 改用已有 `--prospero-teal-deep`，实测导航文字对比由 4.1387 提升到合规值。范围提交 `e1eeb2ac9bb17ec4d65819ddf5ddcbe574787190`；主体实现 `f03d1254bbbbf4a995a12d302e44db27010a7888`；颜色解析修复 `570b9d2c21b2c74e33252ec670bb279e34d1b8c7`；最终对比度实现/契约及 final head 为 `fa431129021e0616e4e07cacc5918950f8027046` / `c927b27d37cdfdd8fd2197399679fa253d752f79`。首轮 [run 37774058716](https://github.com/AplusNeutrino/My_Blog/actions/runs/37774058716) 暴露十六进制颜色解析边界，第二轮 [run 37774453315](https://github.com/AplusNeutrino/My_Blog/actions/runs/37774453315) 正确暴露 Prospero Light 导航 4.1387:1，均未记为通过。最终 [run 37774796110](https://github.com/AplusNeutrino/My_Blog/actions/runs/37774796110) 对应精确 head，completed/success；build `113303295461` 的 167 tests、production Jekyll、既有移动门禁、40 项新矩阵、文章阅读检查、Ravenis 与 artifact upload 均成功，deploy `113303814462` 成功。artifact `11549517059`，digest `sha256:3780fd6633f8b386a102c1d36dda539803bcd3040694d2d12218acaea4366e2f`。T01 baseline protection passed（44 posts / 5 Fragments；Type essay/note/fragment = 5/39/5）；未改文章/Fragment、metadata、旧 URL、事实/可见性/应用数据或外部项目。T31 done，T32 ready，无新增用户问题。

T30 本次范围：在四入口单一数据源上增加只作次级提示的 section signal，并新增一个 THINK/BUILD/OBSERVE/ABOUT 共用的 identity include；THINK、BUILD、OBSERVE 的共享 layout 与 ABOUT 入口都使用同一标题、中文说明、摘要、signal 和四入口导航层级。入口性格只通过数据属性、简短副标签与纯 CSS 的纸面线、构造网格、观测准星、连续轨道四种非交互纹理表达；主标题、中文说明与导航始终优先，两主题继续使用同一 DOM 和现有语义 token。拟改四入口数据、共享 identity include/layout、ABOUT 入口、共享 CSS、静态回归与 390px Chrome 门禁；不改文章/Fragment、入口 URL、旧链接、项目/ABOUT 事实、Library/友链/旅行数据、Gate/NAVI、Ravenis/Occult Atlas 索引边界或外部项目。验收为四入口共享组件和字段可机械核对，副标签不替代或遮挡清晰导航，四种性格不依赖 JS/图片/颜色单独传意，双主题、键盘、390px、全回归、production Jekyll 与精确 head Pages 成功。预计剩余：完成实现与验证后 T30 done，T31 ready。

T30 验收证据：四入口数据各增加 `signal_label` 与中文 `signal_note`，共享 `_includes/neutriverse-section-identity.html` 统一渲染英文名、中文说明、摘要与次级 signal；THINK/BUILD/OBSERVE layout 和 ABOUT 均使用该组件及同一四入口导航。四种入口性格由共享 CSS 的纸面线、构造网格、观测准星、连续轨道表达，同时有可读文字与 aria label，不依赖 JS、图片或颜色单独传意；390px 下改为单列 identity，标题和导航保持优先。范围提交 `4860e38c51877150472f1c0b6fa20dfc1855cb60`；实现及 final head `cc6fa8ba6091c0a69cab4e90eccfb96988592858`。本地 162 tests、T01 baseline protection、四入口 YAML、Python 编译与 diff check 通过。[Actions run 37754831784](https://github.com/AplusNeutrino/My_Blog/actions/runs/37754831784) 对应该精确 head，completed/success；build `113236704458` 的回归、production Jekyll、390px Chrome 四入口 identity/无溢出/导航、双主题与 artifact upload 全部成功，deploy `113237217132` 成功。artifact `11538868917`，digest `sha256:1d009f05ee0a0aefce9d3c1ab82aa4b96b495a4b7b445e1d86540d3c4723e381`。未改文章/Fragment、front matter、文件名、date/slug/permalink、旧 URL、项目/ABOUT 事实、Library/友链/旅行数据、Gate/NAVI、索引边界或外部项目。T30 done，T31 ready，无新增用户问题。

T20 本次范围：实现 T18 已配置但尚未渲染的 Current Signal、Featured 与 System Status，保持首页完整顺序 Identity → Latest Transmissions → Explore → Current Signal → Featured → System Status。Current Signal 只使用已批准的“Neutriverse 网站重构”及其站内说明；Featured 优先使用 `neutriverse_home.featured.posts` 中仍公开可见的文章，不足时依次从 `home_popular.posts` 与最新公开文章补足到最多 4 条，始终排除 hidden 且不显示访问量；System Status 仅从公开内容动态计算 Records、posts/fragments 分解与最后更新时间，项目目录在 T21 建立前无数据则不渲染项目指标，作为自然降级而非伪造数量。拟改首页 layout、共享 CSS、首页配置契约测试、新增 T20 静态回归及 390px Chrome 门禁、主计划/日志；不改文章/Fragment 原文或 metadata、旧 URL、hidden/noindex、外部项目，也不提前实现 T21 项目 schema。验收为六区块顺序、Current Signal 唯一来源、精选 4 条公开且链接真实、状态值与公开源一致、无项目源时项目指标缺席、两主题/390px/回归/Jekyll/Pages 对精确 SHA 通过。

T19 本次范围：按 T18 单一配置重构首页主体，先显示仅使用站内公开身份信息的 NEUTRIVERSE / Neutrino 简介，再输出 8 条按真实日期倒序的公开近期表达（39 篇非 hidden posts 与 `_tabs/thoughts.md` 五条 Fragment 同源合并），最后使用既有四入口数据渲染 THINK / BUILD / OBSERVE / ABOUT。Akasha Notes 与 Toyosatomimi's Headphone 现有站内项目文章通过首页配置获得次级 Project Log 关联标识，不新增第四种 Type、不修改文章 metadata。移除首页旧 category 墙/分页脚本；T20 的 Current Signal、轻量状态与精选区块仍不提前实现。拟改首页配置/layout、共享 CSS、静态回归与 390px Chrome 门禁、主计划/日志；不改文章/Fragment 原文、旧 URL、hidden/noindex 或外部项目。验收为首页前三个已实现区块顺序正确、四入口可达、近期流含 Note/Essay/Fragment 且真实日期倒序、Project Log 仅为次级标识、hidden 不输出、双主题/390px/回归/Jekyll/Pages 对精确 SHA 通过。

T18 本次范围：新增首页单一配置源，固定首页区块顺序为 Identity → Latest Transmissions → Explore → Current Signal → Featured → System Status，并明确各区块的数据来源、公开/hidden 边界与缺省降级。现有首页主卡从 pin 优先改为最新公开文章优先；固定推荐迁入同一配置，旧 `home_recommend.yml` 停用；Current Signal 仅使用已批准的“Neutriverse 网站重构”。拟改首页配置、home layout、静态回归与 390px Chrome 门禁、主计划/日志；不在 T18 提前实现 T19 的混合 Fragment/Project Log 流或 T20 的完整新首页区块，不改任何文章/Fragment、旧 URL 或外部项目。验收为单一配置可机械核对，最新公开文章确为首页首要表达，固定推荐/当前焦点无第二来源，hidden 不进入首页，精确实现 SHA 的回归/Jekyll/浏览器/Pages 通过。

T17 本次范围：把 Archive、Tags 与 Search 明确接入 THINK 的“当前可用入口”，保留 `/archives/`、`/tags/`、`/categories/` 与既有搜索模态框；Search 使用真实 button action 调用 Chirpy 原生搜索，不制造假 URL。导航脚本需支持侧栏与 THINK 内多个搜索触发器；Archive、Tags、Search 继续只读取非 hidden 文章。拟改 section 数据/入口模板、导航脚本、共享 CSS、静态回归和 390px Chrome 门禁；不改任何文章/Fragment 原文、metadata、旧 URL、hidden/noindex 或外部项目。验收为 THINK 内 Archive/Tags 普通链接及 Search 按钮可用，搜索打开且聚焦并可关闭，三种检索均无 hidden 条目，精确实现 SHA 的回归/Jekyll/浏览器/Pages 通过。


T25 本次范围：把 `/observe/` 从手写的两个 section links 升级为由 `_data/neutriverse_projects.yml` 中 `contexts` 含 `observe` 的实体单源渲染的观察目录。每张卡同时提供 `/build/<stable-id>/` 项目事实页和既有 noindex 应用入口，明确“了解项目”与“打开观察界面”，不做重定向或循环跳转。拟新增 OBSERVE catalog include 与静态回归，接入共享 section layout，移除 `_data/neutriverse_sections.yml` 中重复的 Ravenis/Occult 手写 links，补充共享 CSS 和 390px Chrome 门禁；不改 `/ravenis/`、`/occult-atlas/` 应用、数据流程、主题、浏览器状态、noindex/sitemap 或兼容 `/occult-atlas-app/`。验收为目录恰含 Ravenis、Occult Atlas，无 Gate/NAVI/MMXProj；两项目事实/应用链接真实且互不替代；OBSERVE 本身可索引，两个应用继续 noindex；无 JS 可读可达；两主题、390px、全回归、production Jekyll 与精确 head Pages 成功。预计剩余：完成实现与验证后 T25 done，T26 ready。

T25 验收证据：`/observe/` 现从 `_data/neutriverse_projects.yml` 中 `contexts: observe` 单源渲染，恰含 Ravenis 与 Occult Atlas；每张卡分别进入 `/build/ravenis/` / `/build/occult-atlas/` 事实页以及 `/ravenis/` / `/occult-atlas/` 应用，无重定向、循环或 JS 依赖。OBSERVE 本身可索引，两应用继续 noindex；Gate/NAVI/MMXProj 未进入目录。范围提交 `a7889f733a660548fb716913444b3d66259a8721`；主体实现 `6202afd48b692126783b244303e7f7d6e27ca078`；测试契约修复及 final head `a0cc3605b3c3d498a704c2c90485714127aa9aa6`。首次 [run 37720837335](https://github.com/AplusNeutrino/My_Blog/actions/runs/37720837335) 在 142 tests 中有 2 条旧/新测试断言未同步，Jekyll 与部署未执行，未记为通过；修复仅让 BUILD 契约接受新的非 BUILD/OBSERVE 分支，并区分合法 routes 清单与已移除的手写 links。最终 [Actions run 37721161289](https://github.com/AplusNeutrino/My_Blog/actions/runs/37721161289) completed/success；build `113128867874` 的 142 tests、production Jekyll、390px Chrome、双主题、OBSERVE 实体/事实与应用链接/noindex、hidden/Ravenis 与 artifact upload 全部通过，deploy `113129329149` 成功。artifact `11525881465`，digest `sha256:30b7dbb9bc0d4b563a14519a54188bcdbe4f5cd9f13c485c75f31d915c7552ae`。未改文章/Fragment、旧 URL、Ravenis/Occult 应用本体或外部项目。T25 done，T26 ready，无新增用户问题。

T26 本次范围：为 Ravenis 与 Occult Atlas 新增同一个精简、数据驱动的 OBSERVE 应用导航壳，让两个应用均可返回首页与 `/observe/`、进入各自 BUILD 事实页，并在 Ravenis / Occult Atlas 之间直接切换。共享 include 只读取 `_data/neutriverse_projects.yml` 中 `contexts: observe` 的两实体，当前应用使用 `aria-current`；不引入新 JS、不触碰 Ravenis 数据发布/筛选逻辑、Occult Atlas 星历/API/浏览器状态，不改 noindex/sitemap 或 `/occult-atlas-app/` 兼容跳转。拟新增共享 include/CSS/静态回归，接入 Ravenis 页、Occult Atlas layout 和其 390px Chrome 门禁，只为 Atlas 外层增加不影响内部工作台的弹性布局。验收为两页导航来源、链接和当前态一致，无 Gate/NAVI/MMXProj；Ravenis 日期/时段/检索与 Atlas 工作台/控制面板仍可用；Night / Prospero Light、390px、全回归、production Jekyll 与精确 head Pages 成功。预计剩余：完成实现与验证后 T26 done，T27 ready。

T26 验收证据：新增共享 include/CSS，Ravenis 与 Occult Atlas 均从项目 catalog 输出 HOME、OBSERVE、Ravenis/Occult Atlas 切换和当前 BUILD 事实链接，当前应用使用 `aria-current=page`；无 Gate/NAVI/MMXProj，无新 JavaScript。Ravenis 日期/时段/检索及原数据脚本、Occult Atlas 星盘/筛选/控制/API/浏览器状态均保持；两应用继续 noindex，`/occult-atlas-app/` 兼容跳转不变，390px 与 Night / Prospero Light 通过。范围提交 `f518154982aa8687b51b1bddaaeb4a3ad8f32573`；主体实现 `76de0db77d502270f61a769e0a426fd05ec60443`；浏览器门禁修复及 final head `76014a77bb8370b3d5cb9d554502be133cff7c0e`。首次 [run 37726043964](https://github.com/AplusNeutrino/My_Blog/actions/runs/37726043964) 的 146 tests 与 Jekyll 成功，但把空的 `#ravenis-slot-nav` 误当必需可见控件，Chrome 失败、部署跳过，未记为通过；门禁改核对可见的 `#ravenis-period-nav`，静态测试仍验证 slot 容器存在。最终 [Actions run 37726199153](https://github.com/AplusNeutrino/My_Blog/actions/runs/37726199153) completed/success；build `113144813310` 的 146 tests、production Jekyll、390px Chrome、双主题、共享导航/当前态/noindex/核心控件/兼容跳转、Ravenis 与 artifact upload 全部成功，deploy `113145097044` 成功。artifact `11527662883`，digest `sha256:cbd242c500cb54fe1f5966b58e98882dfe1ae794309d309b7eac97bb444c7036`。未改文章/Fragment、旧 URL、应用业务脚本或外部项目。T26 done，T27 ready，无新增用户问题。

T27 本次范围：把 `_tabs/about.md` 中散落的身份说明、旧状态、路线图、阅读/影像栈配置迁入唯一 `_data/neutriverse_about.yml`，由共享 include 渲染；保留改造前已经公开的站内文字与 `2026-08-17` 日期，同时把旧动态内容明确标为历史快照/非实时状态，防止过期内容被理解为当前事实。ABOUT 继续保留四入口导航、Library、友链与旅行关系；旅行地球的开关、数据和脚本不动。拟新增 ABOUT 数据、profile include、静态回归，并调整 about 页面与 390px Chrome 门禁；不从聊天记忆、履历或其他外部资料补写个人事实，不提前完成 T28 新身份/Currently/网站理念或 T29 时间线，不改文章/Fragment、旧 URL、Library 同步、友链/旅行数据、Gate/NAVI 与外部项目。验收为唯一数据源可机械核对，旧动态日期和非实时声明同时显示，迁移前后信息集合有来源，ABOUT/Library/友链/旅行锚点保持，双主题、390px、全回归、production Jekyll 与精确 head Pages 成功。预计剩余：完成实现与验证后 T27 done，T28 ready。

T27 验收证据：`_data/neutriverse_about.yml` 成为 ABOUT 身份、状态、路线图及阅读/影像栈的唯一内容源，`_includes/neutriverse-about-profile.html` 统一渲染，`_tabs/about.md` 删除旧内嵌字符串与管道配置。原站内动态信息保留 `2026-08-17`，新增可见“历史快照 · 非实时状态”、语义化 `<time>` 与 `data-as-of`，避免旧信息冒充当前；数据逐项来自改造前网站，没有使用聊天记忆或外部履历。Library、友链与旅行关系入口仍为 `/library/`、`/links/`、`/about/#travel-globe-title`；旅行地球开关/数据/脚本、Library 同步、友链数据和当前可见性未改。范围提交 `cd77870a9c9b27f0188582f0d1bedf3984e790fb`；主体实现及 final head `77c0e81a03b3a0e5e2102e6968170905f073c73c`。[Actions run 37735976935](https://github.com/AplusNeutrino/My_Blog/actions/runs/37735976935) completed/success；build `113175459662` 的 151 tests、production Jekyll、390px Chrome、ABOUT 单源/日期/历史声明/5+5 栈/关联入口/无溢出、双主题、Ravenis 与 artifact upload 全部成功，deploy `113175770630` 成功。artifact `11531562000`，digest `sha256:3c465d941177e815e8d01113ee1ff84764dd4f2f9f59a86dbceb01cf68e86d47`。未改文章/Fragment、旧 URL、Library/旅行/友链数据、Gate/NAVI 或外部项目，未提前实现 T28/T29。T27 done，T28 ready，无新增用户问题。

T28 本次范围：在 T27 的 ABOUT 单一数据源上增加四个明确区块：可读的站点身份、仅描述网站工作的 Currently、由现有公开站点配置支持的互联网身份/邻居关系、以及从本主计划与现有四入口提炼的网站理念。Currently 只使用已批准的“Neutriverse 网站重构”，携带 `as_of` 和“网站维护状态、非个人实时状态”说明；旧 `2026-08-17` 内容继续独立标作历史快照。拟改 `_data/neutriverse_about.yml`、ABOUT profile include、Night/Prospero Light 样式、静态回归与 390px Chrome 门禁；不使用聊天记忆或外部履历，不新增单位/住址/健康/私人联系方式，不改文章/Fragment、Library/友链/旅行数据与功能、旧 URL、Gate/NAVI、外部项目，也不提前实现 T29 时间线。验收为身份文案可读，Currently 的来源/日期/维护点清楚且不虚构个人实时状态，公开互联网入口有站内依据且安全使用外链属性，网站理念与四入口及连续性原则一致；双主题、键盘、390px、全回归、production Jekyll 与精确 head Pages 成功。预计剩余：完成实现与验证后 T28 done，T29 ready。

T28 验收证据：`_data/neutriverse_about.yml` schema 升至 2，在同一来源内增加身份、Currently、公开坐标与四条网站理念；Currently 唯一内容为已批准的“Neutriverse 网站重构”，带 `2026-10-08`、主计划来源、明确维护字段及“网站维护状态 · 非个人实时状态”。公开坐标只使用既有 `neutriverse.uk`、GitHub `AplusNeutrino`、X `@Neutrino_X` 与 `/links/`，外链使用 `noopener noreferrer`；没有邮箱、单位、住址、健康或聊天记忆资料。旧 `2026-08-17` 个人动态仍在独立历史快照中并明确非实时。范围提交 `d7081afdd5e769c946e0cefacd7d78728ba92f79`；实现及 final head `c3dc0e3e9d1bc5301483702579bb04d95c936dc4`。本地 157 tests、T01 baseline protection 与 diff check 通过；本机无 Bundler，未把本地 Jekyll 记为成功。[Actions run 37741773002](https://github.com/AplusNeutrino/My_Blog/actions/runs/37741773002) 对应该精确 head，completed/success；build `113193881526` 的 157 tests、production Jekyll、390px Chrome、ABOUT 当前/历史语义、四坐标、四理念、双主题与 artifact upload 全部成功，deploy `113194183144` 成功。artifact `11534355036`，digest `sha256:563950bde7229db798a72e6f9e7f6000163f6b339582c5399d3dc89ea94771c5`。未改文章/Fragment、旧 URL、Library/友链/旅行数据与功能、Gate/NAVI 或外部项目，未提前实现 T29。T28 done，T29 ready，无新增用户问题。

T29 本次范围：在 ABOUT 单一数据源中增加“网站与项目轨迹”时间线，并把 Library、友情链接、旅行记忆三类关系整理为可读且可机械核对的关系区块。时间线只采用仓库历史、现有站内页面与公开项目记录能够直接证明的站点/项目事件，每项同时给出日期、来源标签与真实来源链接，不把个人经历、聊天记忆或推断写成事件。Library 与友链继续链接既有 `/library/`、`/links/`；旅行关系明确标为“能力保留、当前未公开”，不生成可点击的隐藏入口，不公开地点数据，同时保持 `_tabs/about.md` 中 `travel_globe_enabled = false`、旅行数据和脚本原样。拟改 ABOUT 数据/include、ABOUT 关系入口数据、Night/Prospero Light 样式、静态回归与 390px Chrome 门禁；不改文章/Fragment、Library 同步、友链/旅行数据、Gate/NAVI、旧 URL或外部项目。验收为至少四个按日期排列且逐项可追溯的站点/项目事件，三类关系状态与动作准确，现有 Library 同步与旅行实现受保护，双主题、键盘、390px、全回归、production Jekyll 与精确 head Pages 成功。预计剩余：完成实现与验证后 T29 done，T30 ready。

T29 验收证据：`_data/neutriverse_about.yml` schema 升至 3，增加按日期升序排列的五项网站/项目轨迹：仓库初始提交、自定义域名、Akasha Notes Project Log、Toyosatomimi's Headphone Project Log 与 Ravenis 接入；三项 GitHub 事件链接精确 commit，两项项目事件链接既有站内记录，每项均有日期、来源标签与真实来源，不包含聊天记忆或新增私人履历。ABOUT 同一数据源还增加三张关系卡：Library 与友链继续分别进入 `/library/`、`/links/`；旅行卡显示“能力保留 · 当前未公开”，使用不可交互状态而非隐藏工具链接。四入口数据中的旅行项改为链接公开的关系说明锚点 `/about/#about-relations-title`，不再指向未渲染的地球锚点；`travel_globe_enabled = false`、旅行数据/脚本、Library 同步和友链数据均未改。范围提交 `0ad4bd9bf12a8c88e97d747d93acb67fe67729b4`；实现及 final head `2999e151bd9b73d7a7ac2035ad2577abd2134d2c`。本地 162 tests、T01 baseline protection、YAML 解析、Python 编译与 diff check 通过；本机无 Bundler，未把本地 Jekyll 记为成功。[Actions run 37747072603](https://github.com/AplusNeutrino/My_Blog/actions/runs/37747072603) 对应该精确 head，completed/success；build `113210969211` 的 162 tests、production Jekyll、390px Chrome、五项时间线/来源安全、三类关系/旅行非入口、双主题、Ravenis 与 artifact upload 全部成功，deploy `113211459174` 成功。artifact `11536790383`，digest `sha256:35b00e6ae4deb8029729954780d381ccd099aa9e2d4c217e082850bb1534972f`。未改文章/Fragment、front matter、文件名、date/slug/permalink、旧 URL、Library/友链/旅行数据、Gate/NAVI 或外部项目。T29 done，T30 ready，无新增用户问题。

T24 本次范围：为 Ravenis、Occult Atlas、Gate、OfficeSpire 建立 `/build/<stable-id>/` 数据驱动详情页，并将 BUILD 卡片从旧应用/仓库或无动作状态统一引向项目事实页。Ravenis 与 Occult Atlas 详情继续 `noindex`，现有应用 URL 与 noindex 不变；Gate 详情不公开 `/gate/` 工具入口并继续 noindex；OfficeSpire 只使用公开 README，保留 `implemented_unverified`，不把 source-complete 或版本 metadata 误称为 runtime-qualified / release。拟改 `_data/neutriverse_projects.yml`、项目 schema、四个详情入口、详情静态回归、BUILD 列表预期与 390px Chrome 门禁；复用现有 layout/CSS，若无需变更则不触碰。验收为四条 canonical 详情生成、七项目均有唯一详情入口；Ravenis/Occult 的应用动作存在且旧应用保持 noindex，Gate 无公开应用/仓库动作，OfficeSpire 仅有真实 repository/文档入口和精确状态；不存在的 Project Log/Release 自然降级；来源可追溯；文章/Fragment、旧 URL、外部仓库不变；全回归、production Jekyll、390px 双主题与精确 head Pages 成功。预计剩余：完成实现与验证后 T24 done，T25 ready。

T24 验收证据：catalog 为 Ravenis、Occult Atlas、Gate、OfficeSpire 加入真实 `detail_url`，七张 BUILD 卡现在都进入唯一项目事实页；新增四条 canonical 页面。Ravenis/Occult 详情与原应用继续 noindex/sitemap false，动作仍指向原 `/ravenis/`、`/occult-atlas/`；Gate 详情 noindex 且 catalog 没有 `/gate/` 动作；OfficeSpire 仅显示公开仓库、README 文档与来源明确的 `implemented_unverified`，README 明示未发布，因此没有 releases。四项无站内 Project Log 时使用模板空状态。范围提交 `bdd370742f83d30a5862281807acf5c245d7a53a`；主体实现 `e01d0b867b6add71c63d07e8f3d6950e901d58b4`；长链接修复 `75986c2d7e180aabefdac5facad1169d45c6fb2a`；移动焦点门禁稳定化及 final head `e0011626bee436fede98a0716dfa02d8e8009d87`。首次 run `37716362399` 的 136 tests 与 Jekyll 成功，但 Chrome 检出 OfficeSpire 长 README 来源链接令 375px 页面横向宽 518px，未记为通过；run `37716525213` 验证长链接修复通过。随后文档 head `7a5975736e53910702feda8e61e4ca6b4e0f31df` 的 run `37716701179` 在回归/Jekyll 成功后复现既有遮罩关闭与下一帧焦点恢复竞态，未记为通过；门禁改为等待“关闭且焦点返回”的完整契约。最终 [Actions run 37716834575](https://github.com/AplusNeutrino/My_Blog/actions/runs/37716834575) completed/success，build `113115128909`、deploy `113115487252` 成功，136 tests、production Jekyll、390px 双主题、七详情事实/状态/动作/来源/noindex、BUILD 筛选、hidden/Ravenis 与 artifact upload 全部通过。artifact `11523997952`，digest `sha256:8eb4a93046ca6b5618b8de81095eb05d472a726bd2a765a7cf7983142620d876`。未改文章/Fragment、旧 URL、原应用行为或外部项目。T24 done，T25 ready，无新增用户问题。

T23 本次范围：把“第一组有依据项目”固定为站内来源最完整的 FitzSight、Akasha Notes、Toyosatomimi's Headphone，分别建立 `/build/fitzsight/`、`/build/akasha-notes/`、`/build/toyosatomimis-headphone/` 三个数据驱动详情页。详情共用 T21 模板，显示概览、公开状态或明确的未记录降级、真实应用/仓库、关联文章与来源；BUILD 卡片优先进入详情页，详情再区分“了解项目”和“打开应用/仓库”。拟改 catalog/schema、通用项目 layout、BUILD 卡片、共享 CSS、三个详情入口、静态回归及 390px Chrome 门禁；不复制文章正文，不把版本文章推断为 active/complete，不建立其余四项目详情，不修改关联仓库。验收为三条 canonical 详情路由真实生成；FitzSight 保留 tracker/repository，Akasha/Headphone 保留 Project Log/repository；三者 status 未知时明确显示未记录而非伪造；来源可追溯；卡片直达详情且旧应用/文章 URL 不变；两主题、390px、回归、Jekyll 与精确 head Pages 通过。预计剩余：完成实现和验证后 T23 done，T24 ready。

T23 验收证据：新增 `/build/fitzsight/`、`/build/akasha-notes/`、`/build/toyosatomimis-headphone/` 三个 canonical 详情页，并在 catalog 写入对应 `detail_url`；其余四项目仍无 detail_url，留给 T24。共享项目 layout 统一输出 Overview、Status、Actions、Project Log、可选 Releases 与 Source Ledger；前三项目没有来源确认的 status，因此页面明确说明未记录且不推断 active/complete/paused。FitzSight 动作保留 `/projfitzgerald/` 和公开仓库；Akasha/Headphone 分别保留原 Project Log 和仓库。BUILD 卡片优先进入详情页，旧应用/文章 URL 均未替换。范围提交 `68e045969c43d73217a47b24416d44d4be9689c5`；实现及 final head `325f48298506ecf3fb620f2b203a9ee0349aa7f5`。[Actions run 37711002137](https://github.com/AplusNeutrino/My_Blog/actions/runs/37711002137) completed/success；build job `113096701703` 的 136 项回归、production Jekyll、390px Chrome、双主题、三详情事实/动作/来源、BUILD 筛选、hidden/Ravenis 与 artifact upload 全部成功；deploy job `113096912163` 成功。artifact `11522125928`，digest `sha256:e12402f79607620336697b1c7844284616af6ad9f4b9b23c1c62207fd0a220ef`。未改文章/Fragment、旧 URL、noindex 或外部项目，未提前生成 T24 页面。T23 done，T24 ready，无新增用户问题。

T22 本次范围：在 `/build/` 从 T21 的唯一 project catalog 渲染七个批准项目卡，并提供渐进增强的 status 筛选与可分享 `?status=` 状态。每张卡只指向当前已存在且已授权公开的应用、Project Log 或仓库；Gate 仍显示为项目实体，但不公开隐藏工具链接，在详情页尚未由 T23/T24 建立前显示自然说明而不制造假链接。拟新增项目列表 include、筛选脚本及静态回归，调整 BUILD layout 接入、页面说明、共享 CSS 与 390px Chrome 门禁；不修改 catalog 事实、不生成项目详情页、不改关联项目仓库。验收为恰有 Q5 七项目且无 MMXProj；默认全量可读，无 JS 时链接仍可达；筛选 `implemented_unverified` = OfficeSpire 1 项、`unspecified` = 6 项，刷新/后退/非法参数行为稳定；六个已授权公开动作目标正确，Gate 无公开 href；两主题、390px、回归、Jekyll 与精确 head Pages 通过。预计剩余：完成实现和验证后 T22 done，T23 ready。

T22 验收证据：`/build/` 通过新增 `_includes/neutriverse-project-list.html` 从 T21 catalog 渲染七张项目卡，`assets/js/neutriverse-project-filters.js` 提供渐进增强的 `?status=` 筛选；默认/无 JS 保留七项。FitzSight、Akasha Notes、Toyosatomimi's Headphone、Ravenis、Occult Atlas、OfficeSpire 分别直达既有应用、Project Log 或仓库；Gate 仅显示项目记录和“工具入口保持未公开”，无 `/gate/` href。状态完全来自 catalog：`implemented_unverified` 仅 OfficeSpire 1 项，`unspecified` 6 项；刷新、后退与非法参数回退通过。范围提交 `be1780f9aea13a93c6396a5ba0ffdb50c2403ef1`；主体实现 `b6cf998dcc8abdb796e144002a45010569b67a69`；测试契约修复及 final head `f6a33049f446360a8ee7f553babc11ea714965ef`。首次 [run 37705683923](https://github.com/AplusNeutrino/My_Blog/actions/runs/37705683923) 在 129 tests 中因静态测试误找 HTML 属性名而失败，未进入 Jekyll；修复只把断言对齐实际 DOM dataset 名。最终 [run 37705790326](https://github.com/AplusNeutrino/My_Blog/actions/runs/37705790326) completed/success；build job `113079711585` 的 129 项回归、production Jekyll、390px Chrome、双主题、BUILD 筛选/动作、hidden/Ravenis 与 artifact upload 全部成功；deploy job `113080119126` 成功。artifact `11519850872`，digest `sha256:d54f72bb0a24e20778d507f4d6c37e6343c1527aaa7b286a8ef576411909e7da`。未改 catalog 事实、文章/Fragment、旧 URL、noindex 或外部项目；未提前生成详情页。T22 done，T23 ready，无新增用户问题。

T21 本次范围：以七个已批准项目为唯一 BUILD catalog，建立稳定 ID、可追溯来源、可选状态/链接/Release 语义和通用项目详情模板。拟新增 `_data/neutriverse_projects.yml`、`docs/neutriverse-project-schema.md`、`_layouts/neutriverse-project.html`、项目 catalog 回归测试，并仅为 catalog 接入补充共享样式、首页 Projects 动态状态和 390px 门禁预期；不提前实现 T22 的 `/build/` 项目清单/筛选或 T23/T24 的项目详情页。验收为七个稳定 ID 唯一且无 MMXProj；每项摘要/链接均有站内或公开来源；status/links/releases 均可省略且模板自然降级；没有项目被要求提供不存在的 Release；Ravenis/Occult Atlas/Gate 的 noindex/隐蔽边界不变；回归、production Jekyll、390px 双主题与精确 head Pages 通过。预计剩余：完成实现、验证、记录精确证据后 T21 done，T22 ready。

T21 验收证据：新增 `_data/neutriverse_projects.yml` 作为七项目单一 catalog，并新增 `docs/neutriverse-project-schema.md`、`_layouts/neutriverse-project.html` 与 `tests/test_project_catalog.py`；首页从该 catalog 动态显示 Projects = 7，移动门禁同步核验。stable ID 为 `fitzsight`、`akasha-notes`、`toyosatomimis-headphone`、`ravenis`、`occult-atlas`、`gate`、`officespire`，无 MMXProj。所有项目有来源；未知 status/links/releases 均省略，catalog 没有任何 releases 字段；模板仅在字段存在时渲染。Gate 为 `unlisted_noindex` 且无公开 links；Ravenis/Occult Atlas 为 `listed_noindex`；OfficeSpire 唯一状态为公开 README 明示的 `implemented_unverified`。范围提交 `95818c1dd9a28fba47ccc4e3b3b48af83810e540`；实现及 final head `029a0110a27a15019ad809e7113cb362c479fd95`。[Actions run 37700336301](https://github.com/AplusNeutrino/My_Blog/actions/runs/37700336301) 精确对应该 head，completed/success；build job `113062000744` 的 122 项回归、production Jekyll、390px Chrome、双主题、hidden/Ravenis 与 artifact upload 全部成功；deploy job `113062326427` 成功。artifact `11517690309`，digest `sha256:4749ebd6e80812fe37331ab1be10da408441734c6c5f2291a5e7e832b1fc6d84`。未改旧文章/Fragment、旧 URL、hidden/noindex 或外部项目；未提前实现 T22 列表/筛选或 T23/T24 详情页。T21 done，T22 ready，无新增用户问题。

T20 验收证据：首页按配置补齐 Current Signal、Featured Records 与 System Status，形成 Identity → Latest Transmissions → Explore → Current Signal → Featured → System Status 六区块顺序。Current Signal 只读取 `_data/neutriverse_home.yml` 已批准的“Neutriverse 网站重构”、摘要与 `/about/`；Featured 先取两条配置文章，再从不含公开访问量的 `home_popular.posts` 补足，最终四条均为非 hidden 真实文章且无重复；System Status 从公开源动态计算 44 Records、39 posts + 5 Fragments、最近更新 2026-08-17，T21 catalog 尚不存在时不渲染 Projects 指标。范围提交 `f75a8e6c00a6c674c3cf8581e2e840a598a4f65b`，主体实现 `5e70e23674026679f3ece8efd9f23e594d5ad396`，主题门禁修复 `6effe6dc3e99a8d445a4750f1a6ea7c787aa3faf`，final head `0e521a53a1408f56ee657fb1197148f9ed9a68da`。run `37694173615` 的 115 项回归与 Jekyll 成功，但移动侧栏关闭时直接点击不可见主题按钮；run `37694396230` 确认六区块与主题切换成功，但将 overflow 锁定的离屏侧栏宽度误判为用户可滚动；两次均未记为通过。最终 [run 37694550921](https://github.com/AplusNeutrino/My_Blog/actions/runs/37694550921) completed/success；build job `113042896498` 的 115 项回归、production Jekyll、390px Chrome、双主题、hidden 检查、Ravenis 与 artifact upload 全部成功，deploy job `113043399090` 成功；artifact `11515256020`，digest `sha256:60f17f4bc971a11d62b2b4c2ef40587bbcaac1f7c0b34243d4aa2ec2ecbc063c`。未改文章/Fragment 原文或 metadata、文件名、日期、slug/permalink、旧 URL、hidden/noindex 或外部项目，也未提前实现 T21。T20 done，T21 ready，无新增用户问题。

T19 验收证据：`_layouts/home.html` 已用站内公开信息呈现 NEUTRIVERSE / Neutrino 身份，按真实日期合并 39 篇非 hidden posts 与 `_tabs/thoughts.md` 的五条同源 Fragment，首页输出最近 8 条并包含 Note / Essay / Fragment；Fragment 链接回原 Thoughts 稳定锚点。四入口复用 `_data/neutriverse_sections.yml`；Akasha Notes 与 Toyosatomimi's Headphone 仅显示 `Project Log / …` 次级关系，不新增 Type。旧 category 墙与首页分页脚本已移除，T20 区块未提前实现。范围提交 `70921743c2f0991f03bac65f1b475a6466f4a5b8`，主体实现 `cf2a02914540660645ab2d5a47572963a8387ea6`，测试契约修复 `4e1775b2ed980a8e7a638e88ecbda7127afce5a7` / `7f733b159e2724f368989e15a88fa269f6c23a64`，生成 URL 匹配修复及 final head `8905c13602bb272a806eca10f22ccd2969f62bc0`。失败 run `37687050652` 暴露两条 T18 旧断言；`37687173271` 暴露一条残留 YAML 断言；`37687516979` 的 110 项回归与 Jekyll 已成功，但 Chrome 发现中文项目 URL 编码不匹配；均未记为通过。最终 [run 37687699563](https://github.com/AplusNeutrino/My_Blog/actions/runs/37687699563) completed/success；build job `113019655845` 的 110 项回归、production Jekyll、390px Chrome、双主题、hidden 检查、Ravenis 与 artifact upload 均成功，deploy job `113020001949` 成功；artifact `11512292304`，digest `sha256:b8f04c5220a159565bf0a7829ea5287355e1d27180026dc29842ad0e4002ceac`。未改文章/Fragment 原文或 front matter、文件名、日期、slug/permalink、旧 URL、hidden/noindex 或外部项目。T19 done，T20/T21 ready，无新增用户问题。

T18 验收证据：新增 `_data/neutriverse_home.yml` 作为首页结构与编辑选择的单一来源，固定 Identity → Latest Transmissions → Explore → Current Signal → Featured → System Status 顺序；声明公开 posts、Thoughts Fragment、Project Log 关系、四入口、状态数据的来源与 hidden 排除策略。Current Signal 仅使用批准事实“Neutriverse 网站重构”；固定推荐从旧 `home_recommend.yml` 迁入，新旧文件不再保存两套值。现有首页主卡取消 pin 优先，改为 `all_visible_posts | first`，浏览器从 THINK 构建页读取最新公开文章真实路径并与首页主卡逐项比较；精选区域也仅遍历公开文章。final head `74dd320059aab642d57933960af7adeb142e2034` 的 Actions run `37678793810` completed/success；build job `112989195647` 的 105 项回归、production Jekyll、390px Chrome、双主题、Ravenis 与 artifact upload 均成功，deploy job `112989813922` 成功；artifact `11508296680`，digest `sha256:7cafeb8a79f405c384c5287ead8f555145b61bf2eb15927dc56c841974fd45ac`。未改文章/Fragment、front matter、文件名、日期、slug/permalink、旧 URL、hidden/noindex 或外部项目；T19/T20 UI 未提前实现。T18 done，T19 ready，无新增用户问题。

T17 验收证据：THINK 的共享入口数据新增 Search action；入口模板将 Archive/Tags 保持为普通链接，将 Search 渲染为无假 URL 的 button，并复用现有 Chirpy 原生搜索。导航脚本从只绑定首个代理改为绑定全部 `data-nv-search-trigger`，侧栏与 THINK 页面入口均可打开并聚焦同一搜索框。100 项回归、production Jekyll、390px Chrome、双主题、Archive 实际账本与生成搜索索引的 hidden 检查均通过；Tags 的索引、详情及关系计数继续在模板层过滤 hidden。初始 run `37672096216` 因门禁过宽扫描整个 Archive HTML 而非实际账本失败；run `37672371791` 确认 Search 打开/聚焦成功，但错误假定 Escape 可关闭 Chirpy 搜索；两者均未记为通过。final head `8d047175d2da89ee3614f9041b998b2ef8c5303c` 的 Actions run `37672590085` completed/success；build job `112967859911` 与 deploy job `112968329095` 成功；artifact `11504919047`，digest `sha256:ec4352a24ad4941ae83b34d315b8649c678ea8bf0a71eac93b0c58ee45c519c5`。未改文章/Fragment、front matter、文件名、日期、slug/permalink、旧 URL、hidden/noindex 或外部项目。T17 done，T18 ready，无新增用户问题。

T16 本次范围：使用现有 `page.type` 与 `_data/content_taxonomy.yml`，在文章详情增加共享 Type 标识及 `nv-post--note` / `nv-post--essay` 语义类；THINK 时间线为三种 Type 输出稳定类名，以紧凑记录、编辑型长文、时间戳信号形成可感知但不改变内容顺序的视觉差异。共享 CSS 同时约束文章阅读宽度约 700–740px，并保证正文中的代码块、表格与图片在窄屏内部滚动/缩放而不造成页面级溢出；Thoughts 继续使用现有 Fragment 卡片。拟改 taxonomy 标签、post layout、writing-list、共享 CSS、静态回归与 390px Chrome 门禁；不改任何 `_posts/` 或 Fragment 的正文、标题、front matter、日期、slug/permalink、旧 URL、hidden/noindex 与外部项目。验收为 Note/Essay 详情各有正确标识与差异化布局、THINK 三种记录类可核对、正文哈希不变、390px 无页面溢出且代码/表格/图片安全、双主题和精确实现 SHA 的回归/Jekyll/Pages 通过。

T16 验收证据：`content_taxonomy.types` 为 fragment/note/essay 增加片段/笔记/长文中文标签；文章布局从现有 `page.type` 读取同一数据，输出 `nv-post--note` / `nv-post--essay` 与可见双语标识，正文 `{{ content }}` 仍唯一。THINK 清单统一输出 `is-<type>`，Note 用紧凑记录左规则、Essay 用更强开篇层级、Fragment 用虚线信号卡，不改变排序/筛选/链接。共享样式将文章 header/content/tail 限制为 46rem（736px），代码/highlight/table-wrapper 内部横向滚动，图片/视频/iframe 不超容器。初始 run `37663655248` 的 96 项回归和 Jekyll 成功，但浏览器门禁错误地期待 CSS 视觉大写后的 DOM 文本 `NOTE`，实际语义文本正确为 `Note / 笔记`，故未记为通过；最终门禁按真实 DOM 文本、语义类和 data type 核对，并逐一打开 Note/Essay 构建链接，验证正文宽度、body 无横向溢出及富内容不逃逸。final head `f1ddf8190c12c2c37cdcd17ff7ace16fe3590b4d` 的 Actions run `37663923756` completed/success；build job `112938169888` 与 deploy job `112938558111` 成功；artifact `11501184118`，digest `sha256:cadb386235f7e19c6c121eff9be232f018efcd3ffae058a33800b5826185635d`。未修改任何文章/Fragment 正文或 front matter、文件名、日期、slug/permalink、旧 URL、hidden/noindex 与外部项目。T16 done，T17 ready，无新增用户问题。

T15 本次范围：保留 `_tabs/thoughts.md` 为五条 Fragment 的唯一内容来源，为每条记录补充显式、唯一且不随排序变化的稳定 `id`；`_layouts/thoughts.html` 与 THINK 混合时间线共同读取同一 ID，旧日期派生锚点保持为当前五条 ID，Fragment 文本与日期不改。增加静态回归，验证 ID 唯一、格式稳定、两处渲染不复制文本且直达链接一致；扩展 390px Chrome 门禁，从 `/think/?type=fragment` 打开一条来源链接并确认落到 `/thoughts/#<id>` 的对应卡片。拟改 Fragment source metadata、两处模板、回归/门禁与计划日志；不改文章、Thought 正文/date/type/topic/tags、旧 URL 或外部项目。验收为五条原文/日期与 T01 基线一致、五个锚点唯一可直达、THINK 仍为 44 项且 Fragment 筛选为 5 项、精确实现 SHA 的回归/Jekyll/浏览器/Pages 通过。

T15 验收证据：`_tabs/thoughts.md` 仍是五条 Fragment 的唯一内容来源，每条新增显式唯一 ID，当前值与既有 `fragment-YYYY-MM-DD` 锚点完全相同；新增说明规定同日多条追加短后缀且发布后不修改。Thoughts 卡片与 THINK 来源链接都读取该 ID，日期派生仅作旧/缺失数据兜底，模板不复制五条正文。初始实现 run `37656324275` 因新测试把注释示例误算为真实条目、旧 T11 测试仍断言日期拼接而在回归阶段失败；测试契约修复 run `37656612002` 的 92 项回归与 Jekyll 已通过，但长页原生点击被固定层拦截，Chrome 门禁失败；两次均未记为通过。最终门禁用与 T13/T14 一致的 DOM click 跟随真实普通链接，仍验证同一 href/目标卡片。final head `cf916da6c46f7d1b5962da92af9f96001b6b6fab` 的 Actions run `37656781396` completed/success；build job `112913743570` 的 92 项回归、production Jekyll、390px Chrome、Ravenis 与 artifact upload 均成功，deploy job `112914304585` 成功；artifact `11499200919`，digest `sha256:32e97d3b8bbdc58c129ccbbbbdf5681570f5283e16ee71e665eff50321bce311`。T01 基线继续保护五条 text/date/type/topic/tags；未改文章、旧 URL、hidden/noindex 或外部项目。T15 done，T16 ready，无新增用户问题。

T14 本次范围：为现有三个显式 Series 建立稳定定义与 `/think/?series=<id>` 浏览面：Database Systems（database-systems，10 篇）、Computer Architecture（computer-architecture，8 篇）、Computer Networks（computer-networks，10 篇）。Series 标签/ID/说明集中在 `_data/content_taxonomy.yml`，目录计数与筛选直接复用公开 `nv_writing_items`，不从旧 categories 回退、不复制文章列表；现有 `post-series.html` 继续按日期升序，并补充指向该 Series 浏览面的稳定链接及边界正确的上一篇/下一篇。拟改 taxonomy、Series 浏览 include、writing-list、筛选脚本、post-series、共享样式、静态回归和 390px Chrome 门禁；不改旧学习笔记或其他文章/Fragment 的正文、标题、front matter、文件名、日期、slug/permalink、旧 URL。验收为三个目录项唯一且计数 10/8/10；可分享 Series 状态刷新/后退正确；无 JS 普通链接和完整 44 项仍可达；首篇仅下一篇、中间篇双向、末篇仅上一篇，目标均为相邻日期文章；精确实现 SHA 的回归、Jekyll、浏览器与 Pages 通过。

T14 验收证据：`content_taxonomy.series` 集中保存三个稳定 ID/标签/说明；Series 目录从同一 `nv_writing_items` 按显式 `series` 计数，结果 10/8/10，共 28 篇，不使用 categories。`series` 查询参数、下拉控制、目录当前态、刷新与后退接入既有状态机；无 JS 保留普通链接与全部 44 项。文章系列面板按日期升序，根链接指回稳定筛选，并以边界判断生成上一篇/下一篇。初始 run `37649992497` 的回归/Jekyll 成功但 Chrome 因门禁把受保护文章路径假定为小写候选 URL 而失败，未记为通过；最终门禁从构建后的 `/think/` 获取真实文章 href，再核对首篇 1/10 仅 next、中间 5/10 prev+next、末篇 10/10 仅 prev。final head `ac7ca06a20196efcf36156916da91a6d5a372d19` 的 Actions run `37650721617` completed/success；build job `112893031112` 与 deploy job `112893560452` 成功；artifact `11495159334`，digest `sha256:36c5d70c8f16165429b09a8a8c22d0a036826b027c1029372335eb5d73122aa0`。未修改旧学习笔记/文章/Fragment 内容或 metadata、文件名、旧 URL、hidden 可见性及外部项目。T14 done，T15 ready，无新增用户问题。

T13 本次范围：在 `/think/` 增加四个稳定 Topic 入口，固定顺序为 Computation / Humanity / Otaku / Arts；标签与说明复用 `_data/content_taxonomy.yml`，每个数量直接从 T11/T12 已合并的 39 篇公开文章 + 5 条 Fragment 同一集合筛选得出，不维护第二套计数或内容列表。入口链接使用可分享的 `/think/?topic=<id>` 并由现有 T12 状态恢复机制激活对应筛选；JavaScript 只同步当前入口状态，不复制分类来源。拟新增 Topic 浏览 include，并调整 writing-list 接线、taxonomy 顺序、共享样式、静态回归与 390px Chrome 门禁；不新增 Topic、不改文章/Fragment、metadata、旧 URL 或外部项目。验收为四入口唯一且数量 computation/humanity/otaku/arts = 34/6/3/1，总和 44；点击、刷新、后退保持 Topic；无 JavaScript 时入口仍是普通可达链接且完整 44 项继续呈现；双主题/移动端/构建部署通过。

T13 验收证据：新增 `_includes/neutriverse-topic-browser.html`，由 `content_taxonomy.topic_order` 决定唯一顺序并从传入的 `nv_writing_items` 使用 `where: 'topic'` 计数；没有第二份内容列表或硬编码数字。四个普通链接为 `/think/?topic=<id>`，脚本增强后同步筛选和 `aria-current`，刷新及浏览器历史状态继续由 T12 机制维护。公开数量 computation/humanity/otaku/arts = 34/6/3/1，总和 44。初始实现 run `37641150181` 与滚动修复 run `37641420057` 均真实记录为 Chrome 门禁失败：长页下 Selenium 原生点击被固定界面层拦截，回归/Jekyll 已通过但未据此验收；最终门禁改为对同一真实链接触发 DOM click，同时静态门禁继续校验普通 href/no-JS 兜底。最终 head `56ee549945d3b61e57b8dd86d67c7b6bab61b82c` 的 Actions run `37641634348` completed/success，build job `112861822320` 与 deploy job `112862459369` 均成功；artifact `11491912924`，digest `sha256:c6c408891eaba643ab1d4bc9b8f4ec0ff4ee01152561bb1c17d9bbabfd61ab70`。未改文章/Fragment 内容或 metadata、旧 URL、hidden 可见性及外部项目。T13 done，T14 ready，无新增用户问题。

T12 本次范围：在 T11 的 44 项服务端清单上做渐进增强，加入 Type（all/note/essay/fragment）与 Topic（all/computation/humanity/otaku/arts）组合筛选、newest/oldest 排序、固定每页 12 项分页，以及 `type`/`topic`/`sort`/`page` 查询参数状态。有效 URL 刷新后保持条件，筛选变化重置到第 1 页，非法参数回退默认，前进/后退恢复界面；无 JavaScript 时控制区不伪装可用且完整 44 项原链接仍在 HTML 中。拟改 writing-list include、新增专用脚本、THINK layout 接线、共享样式、静态回归和真实 Chrome 门禁；不改 `_posts/`、Fragment 数据/原文、front matter、日期、slug/permalink、旧路由或外部项目。

T12 验收证据：实现提交 `e8e70c636ca2456874e0aa25ecc4a341ac78de2d`（父提交为范围记录 `a8b0d0461e5a4faf8129cc5ce92932b27672bfa3`）。服务端继续输出 44 个原始可达链接，JavaScript 增强默认 12/44、4 页，支持三种 Type、四种 Topic、newest/oldest、组合过滤、空结果、合法状态刷新、浏览器前进/后退和非法参数规范化；筛选变化回第 1 页。390px Chrome 实测 fragment+humanity = 4、oldest 首项 2024-09-12、page 2 刷新、双主题与无横向溢出均通过。精确 Actions run `37611360209` 对应该实现 head，build job `112759102707` 与 deploy job `112759519223` success；artifact `11477777654`，digest `sha256:668c992fc4263720558f1699ccb61a87905d759266f68ed44744d4534f55afa9`。未改旧文章/Fragment 内容、metadata、日期、slug/permalink、旧路由或外部项目。T12 done，T13 ready，无新增用户问题。

T11 本次范围：在 `/think/` 使用现有 `site.posts` 与 `_tabs/thoughts.md` 的 Fragment 单一来源生成倒序写作时间线；公开范围为 39 篇非 hidden 文章 + 5 条 Fragment，共 44 项。每项显示 Type/Topic，文章保留原链接，Fragment 链接回 Thoughts 的稳定锚点；无内容时显示真实空状态。组合筛选、排序切换、分页与 URL 状态属于 T12，本次不提前实现。拟改共享 section layout、新写作列表 include、Thought anchor、共享样式、相关回归与现有 390px Chrome 门禁；不改任何文章/Fragment 原文、front matter、日期、slug/permalink、旧路由或外部项目。

T11 完成证据：实现 `d28ac191c41f316919348b8878977f7b53cb64be` 在 `/think/` 输出 44 项日期倒序写作清单，Type 为 35 Note / 4 Essay / 5 Fragment，Topic 为 computation 34 / humanity 6 / otaku 3 / arts 1；首项日期 2026-08-17，hidden 标题不输出，文章沿用原 URL，Fragment 返回 `/thoughts/` 稳定锚点，真实空状态已实现。精确 Actions run `37605371371`：build job `112739422247` 的回归、production Jekyll 与 390px Chrome 门禁成功，deploy job `112739815749` 成功；Pages artifact `11474821554`，digest `sha256:288ccb2ac908394dca5dd7b34574682bbdb83159586570d71350005117100550`。未改文章/Thought 原文、front matter、日期、slug/permalink、旧路由或外部项目。后续文档 head `2898a46811aa8170ade88d105a67b41ab0e8a390` 的 run `37605673482` 暴露 Chrome 焦点读取早于 `requestAnimationFrame` 的测试竞态（站点清单、回归和 Jekyll 均正常）；`b1554ce9d3bbfe9f4e56a2f434b3bbf16d572b5a` 改为等待抽屉打开且焦点进入侧栏，并缩短隐藏标题失败输出。其精确 run `37605887655` 的 build `112741125853`、deploy `112741535916` 全部成功，artifact `11475450372`，digest `sha256:6820ea6e1a328cb58e54613937c38918756cc1b92df7c6b6287b190a78ae7dde`。

T10.b 本次范围：增强 Chirpy 原生手机 sidebar trigger/mask 的 aria-expanded、关闭焦点恢复、Escape 与断点清理；仅调整导航交互脚本/共享样式、相关测试、计划/日志。验收：390px CSS viewport 的四入口/辅助入口/关闭路径可用、无 body 横向溢出、44px 关键触控目标、打开后焦点进入 sidebar、Escape/mask/导航后关闭并回 trigger；两主题与对应实现 SHA CI/部署通过。若窄视口只能通过浏览器 zoom 获得，须同时记录实际 innerWidth，不以桌面截图替代。

T10 拆分：T10.a 桌面折叠键盘/焦点与状态（done）；T10.b 手机菜单/关闭/焦点与 390px 实际验收（done）。T10.b 保留 Chirpy 原生抽屉并补 controls/expanded、打开焦点、Escape/遮罩焦点返回、跨断点清理、44px trigger 与移动横向滚动锁；77 tests 和 production build 通过。GitHub Actions 的真实 Chrome 以 innerWidth 390 / innerHeight 701 验证 HOME + 四入口、三个辅助入口、Light/Night、打开/关闭/导航路径；final head `337132987101fcb170db718a9713619013fe12d7` 的 build/deploy 成功。T10 done，解锁 T11 与 T21；按顺序下一项 T11。

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
状态：工具确认创建成功并启用。
- 名称：推进 Neutriverse 重构
- Automation ID：6ac11b88fe048191ae937f499e28ed30
- 时区：Asia/Shanghai
- DTSTART：2026-10-04 00:00（北京时间）
- RRULE：FREQ=HOURLY;INTERVAL=1
- 任务每轮读取最新主计划/日志，拆分并完成工作，遇到问题转做独立任务；全部验收后暂停此任务。
- 旧的 Neutriverse Taxonomy Migration 已停用；本次没有重启旧迁移任务。
- 2026-10-07 16:46 用户要求暂停重复 scheduled 并保留每小时一次；peek 核对只有上述完整重构任务（当时 paused），旧迁移保持 paused；已恢复上述 ID 为 enabled，原 hourly RRULE 不变，未创建第二条任务。
- 创建成功表示定时配置已保存，不等于未来所有实现/构建已完成；实际执行以日志与提交为准。


## 26. 当前执行状态与证据

### T01 — 基线盘点（done）

- Run：2026-10-04 00:01；active_run = none（本次工作已交接，无执行占用）；branch = main。
- Base SHA：97281227aaafe176870b28bc8a352a0e536e29d6。
- 开始范围记录提交：2878fbb0c8d4af0eea7e902a4a8faf4701abf910。
- 基线交付提交：e1c7f29defce1e2821e81fdd87e4bdbf71597c63。
- 文件：tools/content_restructure_baseline.py、docs/neutriverse-restructure-baseline.json、docs/neutriverse-restructure-baseline.md。
- 覆盖：44 文章（5 hidden）、5 Fragment、14 页面来源、99 布局/配置/集成文件哈希。
- 当前统计：Type essay/note/fragment = 5/39/5；Topic computation/humanity/otaku/arts = 38/6/4/1；全部写作独立 Tags = 157。T02 需修正旧报告 humanity/arts 统计。
- 验证：44 个原 Git blob 的 SHA-256 独立核对通过；44 个源 URL 候选唯一；正文/日期/slug/permalink/hidden/published 核对无差异；原保护源与基线 SHA 的 git diff 通过；27 项现有 Python 回归通过。
- 历史基线构建：run 37132489511（head 97281227...）completed/success；不代表新交付构建。
- 当前交付 CI：[37135823458](https://github.com/AplusNeutrino/My_Blog/actions/runs/37135823458)，head e1c7f29...，最终检查 completed/success；T01 done，T02/T06 ready。
- 限制：本环境缺 Ruby；线上 sitemap 返回 HTTP 403。源路径在 JSON 标记 runtime_url_verified=false；生成 URL/robots/Tag 详情与线上视觉留 T33/T38，不声称已通过。
- 保护：未改文章/Fragments/配置/应用行为；文档和 tools 原配置排除站点发布内容。
- 下一步：T02/T06 已解锁，优先 T02。

### T02 — 分类/审计/报告一致性（done）

- Run：2026-10-04 01:00；base SHA = `c6d8ef5ce1a1a22d635d2f2a9e461509d47852a3`；branch = main。
- 本次范围：从 T01 基线与 authoritative audit 独立核对 44 篇文章 + 5 条 Fragment 的 Type/Topic/Series/Tags；修正 `docs/content-taxonomy-final-report.md` 的统计错误并解释原因。
- 拟改文件：`docs/content-taxonomy-final-report.md`、必要的只读校验脚本、本主计划、执行日志。
- 验收：49/49 条源分类与 audit 一致；报告 Type/Topic/Series/Tag 数字由可重复检查支持；不修改内容 front matter 或正文；相关回归通过。
- 实现提交：`e595599463b3eee38b4dc38ce6baecbdda7b05a6`；修正报告 Humanity 7→6、Arts 0→1，新增 current source ↔ authoritative audit ↔ report 回归测试。
- 实际核对：44/44 文章与 5/5 Fragment 的 Type/Topic/Series/Tags 逐项一致；Series 10/8/10；旧/新独立标签 93/157 可重复复现。唯一冲突是报告聚合表的转录错误，未改内容或审计来迎合报告。
- 本地验证：`PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v`，28 tests OK；`git diff --check` 通过。
- CI：实现 head `e595599...` 的 run 37139226666 被后续 push 依 Pages concurrency 取消；包含该实现的直接后续状态提交 `1b9bf7b...` 在 [run 37139271289](https://github.com/AplusNeutrino/My_Blog/actions/runs/37139271289) completed/success。该成功构建实际包含相同实现树及仅追加的计划/日志，T02 done，T03/T04/T06 ready。
- 保护：未修改任何文章、Fragment、front matter、权威 audit、文件名或 URL 元数据。

### T03 — Series 回退与隐藏文章过滤（done）

- Run：2026-10-04 01:58；base SHA = `1b9bf7b38c9c0ea79419de55205e9615be39f76e`；branch = main。
- 本次范围：让 Series 只由显式 `series` metadata 驱动；无 Series 的已迁移文章不再按旧 categories 自动组成系列；Series 列表统一排除 `hidden: true` 文章。
- 拟改文件：`_includes/post-series.html`、相关回归测试、本主计划、执行日志。
- 验收：无 `page.series` 时不渲染 Series 面板；有 Series 时按日期列出同 series 且非 hidden 的文章；页面链接/正文/分类 metadata 不变；全套回归和 Pages build 通过。
- 实现提交：`338a9c97e1dd615f099ab88ebe011649ca7fcd1a`。`_includes/post-series.html` 已删除 categories 回退；仅非 hidden 且有显式 `page.series` 的页面渲染面板，并从同系列列表排除 hidden 文章。新增 `tests/test_post_series_visibility.py` 防止回退恢复。
- 本地验证：`git diff --check` 通过；`PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v`，31 tests OK。
- CI：[run 37142745038](https://github.com/AplusNeutrino/My_Blog/actions/runs/37142745038) 由实现 head 精确触发，completed/success；包含回归测试、Jekyll build 与 Pages 部署流程。
- 保护：未修改文章、Fragment、front matter、categories/series 值、文件名或 URL。
- 结论：T03 验收完成；T04/T06 ready。

### T04 — Tags 使用频率、重复与二轮映射（done）

- Run：2026-10-04 02:55；base SHA = `b2a2a15321efb0c443b57f001368227105b1cdce`；branch = main。
- 前置核对：base 对应 [run 37142886517](https://github.com/AplusNeutrino/My_Blog/actions/runs/37142886517) completed/success；T03 状态提交已部署。
- 本次范围：从 44 篇文章 + 5 条 Fragment 的真实 metadata 统计 157 个独立 Tags 及使用位置；逐项记录 keep/merge/retire、目标和理由；给 T05 明确有限改动与旧标签 URL 策略。
- 拟改文件：新增 `tools/content_tag_review.py`、`docs/content-taxonomy-tag-review.md`、相关回归测试、本主计划、执行日志。
- 验收：157/157 个当前标签均有频率、公开/hidden 使用数、决定与理由；低频本身不作为删除理由；作品/实体标签不会仅因一次使用被删；建议改动可机械复核且不在 T04 修改文章或 Fragment metadata/正文。
- 用户问题：无。
- 范围记录提交：`792176c47f2eeef15f5cc7a2819cc7159109f2e3`；实现提交：`dbdeb5a77cee9f88e106aa861d0523da89716879`。
- 交付：`docs/content-taxonomy-tag-review.md` 覆盖 157/157 Tags、165 次关联；150 个一次性标签、6 个两次、1 个三次。17 个标签只用于 hidden 内容，语义保留，公开聚合过滤交 T05/T17。
- 有限变更集：仅 `Bus` → `System Bus`（merge）和 `Changelog`（retire）；预计独立标签 157→155、关联 165→164。两个旧标签 URL 均指定 noindex 兼容跳转策略。其余 155 个标签 KEEP。
- 可复现工具/测试：新增 `tools/content_tag_review.py` 与 `tests/test_content_tag_review.py`；生成物自检通过，全套 34 tests OK，`git diff --check` 通过。
- 保护验证：T01 baseline 对照 passed；44 posts / 5 Fragments 的正文、文本及受保护 URL metadata 无变化。T04 未修改任何文章或 Fragment metadata。
- CI：[run 37146556058](https://github.com/AplusNeutrino/My_Blog/actions/runs/37146556058) 对应实现 head，completed/success；包含回归、Jekyll build、artifact 与 deploy。
- 结论：T04 done；T05/T06 ready。

### T05 — 有限标签修改及兼容处理（done）

- Run：2026-10-04 04:01；base SHA = `185236ff7b73934815df6f3c506edd0d40252446`；branch = main。
- 前置核对：base 对应 [run 37146695323](https://github.com/AplusNeutrino/My_Blog/actions/runs/37146695323) completed/success；T04 状态与审计均已部署。
- 本次范围：仅应用 `Bus` → `System Bus`、删除 `Changelog` 两项；同步 authoritative audit/final report；保留 `/tags/bus/` 与 `/tags/changelog/` noindex 兼容入口；公开 tags 目录、tag 详情与 trending tags 排除 hidden posts/hidden-only tags。
- 拟改文件：两篇文章 front matter、`docs/content-taxonomy-migration.md`、`docs/content-taxonomy-final-report.md`、标签布局/组件、两个兼容页、相关测试、本主计划与执行日志。
- 验收：实际/审计/报告一致为 155 个写作 Tags、164 次关联；旧标签路径有明确目标且 noindex；公开标签面不列 hidden；正文、Fragment 原文、文件名、date/slug/permalink/旧文章 URL 均通过 T01 baseline；对应实现 SHA 的测试、Jekyll build、Pages deploy 成功。
- 用户问题：无。
- 范围记录提交：`05c34dcd87f73d4638b3074d435c899b779df0a6`；实现提交：`c2cf7da1e969502d34655ad69db3eb8795bb9b5e`。
- Metadata：仅两篇文章 front matter 改动；`Bus` 合并为 `System Bus`，`Changelog` 删除。authoritative audit 与 final report 同步为 149 个文章 Tags、155 个全部写作 Tags、164 次关联；`System Bus` 两次使用。
- 可见性：公开 Tags 目录、单 Tag 详情、trending tags 均按 `hidden != true` 过滤；hidden-only 标签不进入公开索引，直接标签详情不列隐藏文章。
- 兼容：`/tags/bus/` noindex 跳转 `/tags/system-bus/`；`/tags/changelog/` noindex 跳转 `/tags/neutriverse/`；两个源路径 `sitemap: false`。
- 本地验证：T04 审计快照复现通过；39 tests OK；`git diff --check` 通过；T01 baseline protection passed，44 posts / 5 Fragments 的正文、文本、文件名及 date/slug/permalink 未变。
- CI：[run 37150481141](https://github.com/AplusNeutrino/My_Blog/actions/runs/37150481141) 精确对应实现 head，completed/success；回归、Jekyll build、artifact upload、Pages deploy 均成功。
- 生成产物：artifact `11283507681`（digest `sha256:177108483abe5ee333c9328801a2355d1522871535bc6d3fbdd6b5a5d0a0e3ab`）中确认五个相关路径均存在；公开索引不含退役/hidden-only 抽查项，两个 redirect 含 noindex 与正确目标，hidden-only 详情抽查为 0 个文章链接。
- 结论：T05 done；T06 ready。

### T06 — 页面归属、路由与可见性映射（done）

- Run：2026-10-04 05:04；base SHA = `02a1e0c4ac709ac36b4303acc6b02957b876db68`；branch = main。
- 本次范围：以 T01 的 14 个页面源为底，盘点动态/生成路由、四入口、特殊模块、公开发现、隐蔽发现、noindex、sitemap 和 robots 语义；只建立实现契约，不改线上页面行为。
- 范围记录提交：`c6c20a8ab14ea585d67560d906ee47990a67c6b4`；中途 PGL 同步 bot 在其上快进提交 `5b394610033ba311e7f0368afd14751f91fa5fe2`；实现提交基于该新 head 安全重建为 `5a01abb2988f4a77e8c4fbc0f2d33931a105b8ee`，没有覆盖同步结果。
- 交付：`docs/neutriverse-route-visibility-map.md` 为 authoritative contract；覆盖 14/14 页面源、文章/Category/Tag/Feed/Search/Sitemap/robots/兼容路由、四入口和非独立特殊模块。Ravenis/Occult Atlas 明确为 OBSERVE 可发现且应用页 noindex；Library/友链/旅行归 ABOUT；Gate/NAVI 保持旧 URL 和隐蔽程度。
- BUILD 边界：列入 FitzSight、Akasha Notes、Toyosatomimi's Headphone、Ravenis、Occult Atlas、Gate、OfficeSpire；MMXProj 明确排除；项目详情和应用入口分离，不修改关联项目仓库。
- 验证：新增 7 项文档契约测试，全套 46 tests OK；`git diff --check` 通过；T01 baseline protection passed（44 posts / 5 Fragments、页面源和保护 URL 未变）。本环境无 Ruby，因此本地不声称 Jekyll build；对应实现 SHA 的 Pages workflow 补足构建验证。
- CI：[run 37154308445](https://github.com/AplusNeutrino/My_Blog/actions/runs/37154308445) 精确对应实现 head，completed/success；测试、Jekyll build、artifact upload 和 deploy 成功。
- 用户问题：无。结论：T06 done；T07 ready。

### T07 — 双主题基础规范与共享组件契约（done）

- Run：2026-10-04 06:04；base SHA = `df9d33f5e2c845dec388710601f08a780d9a5f5f`；branch = main。
- 本次范围：将 `DESIGN.md` 从 Prospero Light 单主题说明升级为 Night / Prospero Light 的权威共享契约；只改规范与契约测试，不改 CSS、模板、页面、路由或正文。
- 范围记录提交：`bf3bf1d01becf609c0f8cc1185afc849960e7464`；实现提交：`6f3ee6e7bc6b4664af34afb9c977394e807a6d1c`。
- 冲突收敛：删除“保持旧信息架构”的约束，改为保留 Chirpy 壳层能力但以 THINK/BUILD/OBSERVE/ABOUT 替换旧一级 tab；Ravenis 改为经 `/observe/` 公开发现且应用页继续 `noindex,nofollow`，与 Q3/T06 一致。
- 契约：定义双主题语义等价、canonical theme controller、11 个共享语义 token、字体/17px 长文/700–740px 阅读宽度、8px+4px 间距、九类共享组件、2px/3px focus、44×44px 移动目标、390/768/1024/1366px、reduced-motion 与无页面级横向溢出规则；补充 Ravenis/Occult Atlas/Gate/NAVI/Library/友链/旅行地球边界。
- 验证：新增 8 项设计契约测试，全套 54 tests OK；`git diff --check` 通过；T01 baseline check passed（44 posts / 5 Fragments、页面源与保护 URL 未变）。本地无 Ruby，未声称本地 Jekyll build。
- CI：[run 37157623519](https://github.com/AplusNeutrino/My_Blog/actions/runs/37157623519) 精确对应实现 head，completed/success；测试、Jekyll build、artifact upload 和 deploy 成功。
- 用户问题：无。结论：T07 done；T08 ready。

### T08 — 四入口数据、页面骨架与可复用导航（done）

- Run：2026-10-04 07:00；base SHA = `12d0d70139bcdfa7192820c6f228d9be54bbfbe1`；branch = main。
- 范围记录提交：`ae9de7696125609b22e3caa1e7a4fda0168e8f6b`；初始实现提交：`e5b256505c1ad7e4c8593d49d7c9a5d76336bb6a`；完整主题文件修复及最终验收 head：`3818729a1a17e36128d876d5ea06961c7752ab40`。
- 交付：`_data/neutriverse_sections.yml` 作为四入口英文名、中文说明、摘要与当前真实链接的单一来源；新增共享 section layout、主入口导航、入口链接 include、共享 CSS，以及 `/think/`、`/build/`、`/observe/` 三个 canonical 页面；原 `/about/` 页面保留并接入同一组件。
- 边界：公共四入口导航仅含 THINK/BUILD/OBSERVE/ABOUT；OBSERVE 连接 Ravenis/Occult Atlas；BUILD 骨架只连接现有 FitzSight、Akasha Notes、Toyosatomimi's Headphone 站内依据。Gate/NAVI/MMXProj 未进入这些公共入口；未伪造未完成项目详情或状态。
- 失败与修复证据：初始实现的 [run 37160568512](https://github.com/AplusNeutrino/My_Blog/actions/runs/37160568512) 因提交接口静默截断大型主题 CSS 而失败，精确失败为 Night 主题关联文章表面断言。没有将其记作通过；修复提交以完整 blob 恢复两份主题文件并保留 `--nv-*` 映射。
- 本地验证：全套 62 tests OK；T01 baseline check passed（44 posts / 5 Fragments，正文、文件名、日期及保护 URL 未变）；`git diff --check` 通过。
- CI：[run 37160746998](https://github.com/AplusNeutrino/My_Blog/actions/runs/37160746998) 精确对应最终 head `3818729a...`，regression tests、Jekyll build、artifact upload 与 Pages deploy 全部 completed/success。
- 构建产物：artifact `11286954602`（digest `sha256:4d70e6e18f517a598f8f2c7963dc3906e73357edf6928135f8a01d9204060ef8`）内四个页面均存在；四入口导航逐页只含四个 canonical；各中文说明及实际 section links 正确；共享 CSS 存在；Night/Light 文件分别为 148589/70176 bytes，确认未再次截断。
- 用户问题：无。结论：T08 done；T09 ready。

### T09 — 桌面导航与辅助入口（done）

- 原实现 `145d4b9aba56d049a3814140b07def3eff1a513c`；本次范围提交 `6f6fa62dbc97cfe2ee863b73f92fa11c4b8fff76`；修复依次为 `1d809bdf1ba05224f064f9941fec003d40497af5`、`ba33bcbbfdd243b265eb50eeb4f5543dd8eb59ea`、`c50938297d9b9388aceff5df84e60c051973dac9`。
- 修复旧 CSS 隐藏 Tags/Archive、辅助文字折行及 Chirpy tab 内边距压缩 grid；中文/辅助必要标签提升为 12px。改动仅三文件：Night CSS、共享导航 CSS、sidebar 测试；没有改正文或用户首页推荐。
- 本地：73 tests OK；`git diff --check` 通过；T01 protection passed，44 posts / 5 Fragments 的正文、日期、文件名、slug/permalink/旧 URL 不变。
- 精确最终 [run 37594247954](https://github.com/AplusNeutrino/My_Blog/actions/runs/37594247954) head `c509382...`：回归、Jekyll build、artifact upload、Pages deploy 全部成功；artifact `11469916226`，digest `sha256:be289d881b1e8f7ac29de1a3f1727b81e7937f2c91443d5cc6b9e99b0e7b9fc8`。
- 实际桌面浏览器：1363px，四入口/home active 与跳转、Tags/Archive、Search 查询 Akasha 及取消、双主题切换均通过；最终辅助入口宽约 81px、无折行/隐藏，明暗模式无页面横向溢出；Tab 到 THINK 的焦点环为 2px/3px。RSS/既有社交链接保留且可到达，不对外发送信息。
- 验收边界：T09 桌面范围 done；未将此结果代替 T10 的 390px、手机折叠/焦点恢复或 T31 全断点专项。没有新增用户问题；下一项 T10 ready。

### T10.a — 桌面侧栏键盘与折叠状态（done；父 T10 in-progress）

- Base `b7fd898660d9bbabd6d0a8bdd0396069ef014aeb`；范围提交 `23108f19456f86ef76911eb520be0f1a01b7037f`；实现 `0968f1da56201a55d3c340dd8c323f6dc7c8c141`。
- 交付：折叠时 sidebar inert/aria-hidden、展开按钮 hidden/expanded 与状态同步，桌面 avatar 动作角色/标签正确、Space/Enter/Escape 可操作、焦点关闭→展开按钮/打开→avatar；断点切入手机时释放桌面 inert，不改 native 手机菜单本体。
- 验证：75 tests OK（含 Node 执行实际 controller 的状态/焦点行为）；T01 protection passed；diff check 通过。精确 [run 37596416095](https://github.com/AplusNeutrino/My_Blog/actions/runs/37596416095)，head `0968f1d...`，回归/Jekyll/上传/部署全部成功，build/deploy jobs `112710055792` / `112710337878`。
- 浏览器：1363px，Night Space 收起→inert/焦点 recall；Shift+Tab 去页脚且不进入 sidebar；打开→avatar；HOME Escape 收起；Light Enter 收起/打开与焦点恢复正确，2px 主题焦点环；未把此结果说成手机通过。
- 无用户问题。下一项 T10.b 手机菜单与 390px；T11/T21 依赖父 T10，暂不解锁。


### T10.b — 手机菜单、焦点与 390px 验收（done；父 T10 done）

- 范围提交：`c7b89d9e71903d3791facc960c4eb20e51980879`；功能实现链最终 head：`337132987101fcb170db718a9713619013fe12d7`。
- 交付：原生 sidebar trigger 同步 `aria-controls/expanded` 与动作名称；打开焦点进入菜单；Escape 和遮罩关闭后焦点回 trigger；Tab 在打开菜单内循环；跨 850px 清理状态。移动端 trigger 最小 44px，sidebar 垂直滚动且根页面横向滚动锁定。
- 可复现真浏览器：`tools/check_mobile_sidebar.py` 在 Pages workflow 构建后启动 Chrome 390×844，实测 `innerWidth=390`、trigger `46×44`、HOME + THINK/BUILD/OBSERVE/ABOUT、3 个辅助入口、Light/Night、Escape/遮罩/导航关闭与焦点。关闭态 `bodyScrollWidth=bodyClientWidth`；抽屉打开时根页面 `overflow-x:hidden`，用户不可横向滚动。
- 最终证据：[run 37600119191](https://github.com/AplusNeutrino/My_Blog/actions/runs/37600119191)，head `337132987101fcb170db718a9713619013fe12d7`；build `112722158257`、deploy `112722471895` success，77 tests、Jekyll、Chrome 验收及 Pages 部署通过。artifact `11471544488`，digest `sha256:ebf2eab52a17774d669d1a34deb1d77efa7487881ea4f3808ba1e0c8847bf2a7`。
- 保护：实现链未触及 `_posts/`、`_thoughts/`、文件名、date/slug/permalink、正文、旧路由或外部项目仓库。无新增待答问题；下一项 T11。
