# Neutriverse Master Restructure Plan

> Status: **living master plan**  
> Repository: `AplusNeutrino/My_Blog`  
> Purpose: capture the long-term redesign direction for Neutriverse and preserve implementation history  
> Current state: **Phase 1 — Content Foundation completed**  
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
Recent Essay / Note / Fragment / Project Log

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
PROJECT LOG
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