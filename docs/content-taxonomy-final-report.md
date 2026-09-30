# Neutriverse Content Taxonomy Final Report

> Validation snapshot: 2026-09-30  
> Repository state validated: `63289f26ad99dfca7b8afcbc58af72b6e25cdcf5` before this report commit  
> Scope: 44 `_posts/*.md` articles plus 5 current Thoughts fragments (49 writing items)

## Migration totals

- Articles migrated: **44 / 44**.
- Thoughts fragments aligned: **5 / 5**.
- Total writing items covered by the migration audit: **49 / 49**.
- Audit classifications marked `confident`: **49 / 49**; owner-review classification items recorded by Step 7: **none**.

## Type counts

| Type | Count |
|---|---:|
| `fragment` | 5 |
| `note` | 39 |
| `essay` | 5 |
| **Total** | **49** |

All audited Type values are within the approved controlled vocabulary: `fragment`, `note`, `essay`.

## Topic counts

| Topic | Count |
|---|---:|
| `computation` | 38 |
| `humanity` | 7 |
| `otaku` | 4 |
| `arts` | 0 |
| **Total** | **49** |

All audited Topic values are within the approved controlled vocabulary: `otaku`, `arts`, `computation`, `humanity`.

## Series

Only three durable Series are in use after migration:

- `Database Systems` — 10 articles.
- `Computer Architecture` — 8 articles.
- `Computer Networks` — 10 articles.

No one-item course/category Series was retained merely to mirror the legacy hierarchy.

## Tag inventory

The migration audit records **93 unique legacy tag strings** and **157 unique final canonical tag strings** across the 44 articles and 5 Thoughts fragments.

The global unique-tag count therefore increased rather than decreased. This is not hidden as a PASS: broad structural/course tags were removed or canonicalized, while body-derived specific concepts were added for retrieval. Per-item tag counts remain within the intended small-tag approach in the audit, but the Definition-of-Done phrase “materially reduced/canonicalized” is only partially satisfied if interpreted as requiring a lower global vocabulary count. This remains an explicit review item before Step 8 can be closed.

Representative merges/canonicalizations include:

- `最终幻想` → `Final Fantasy`; `FFXIV` → `Final Fantasy XIV`.
- `TMT` → `Terror Management Theory`.
- `STT` → `Speech-to-Text`.
- `SKILL` → `Agent Skills` after body review.
- `哥德尔编码` → `Gödel Numbering`.
- `DDOS` → `DDoS`.
- Network/database/architecture Chinese concept labels were replaced by canonical technical names such as `Physical Layer`, `Relational Algebra`, `Database Recovery`, `Addressing Modes`, and `Assembly Language`.

Representative removals/retirements include `FirstPost`, the broad course tags `计算机组成原理` and `计算机网络`, and generic structural/editorial labels whose role is now carried by Type/Topic/Series. Legacy `categories` remain temporarily in front matter for compatibility as required by the migration plan.

## URL compatibility

The authoritative audit and batch execution evidence state that migration did not rename post files or intentionally change `date`, `slug`, or explicit `permalink` fields. A repository compare from the completed taxonomy-plumbing baseline (`a3cb7cc0d0f93fa8d29f6a61ea9ae3566774069c`) to the completed Step 7 state (`63289f26ad99dfca7b8afcbc58af72b6e25cdcf5`) shows the same migrated `_posts/*.md` paths as modified files, with no migrated post path reported as renamed or deleted. URL compatibility is therefore preserved at the file/path level; no URL-changing migration is recorded.

## Body-preservation validation

Batch audit entries record that every article body was read before classification and that body prose was preserved. The baseline-to-Step-7 GitHub compare shows front-matter-sized diffs for most migrated articles. Three files (`2024-10-07-TestInfo.md`, `2025-12-17-NoSQL项目面经.md`, and `2025-12-19-ROSSMANN项目.md`) show large add/delete counts consistent with whole-file newline/serialization normalization during replacement. The current connector compare summary does not prove byte-for-byte or semantic body equality for those three files, so Step 8 does **not** claim a complete body-diff PASS until those bodies are independently compared against the pre-migration baseline.

## Taxonomy surfaces

Step 3 added `_data/content_taxonomy.yml` and `_includes/post-taxonomy.html`, and adapted `_layouts/post.html` plus `_includes/post-series.html`. Static review established the intended Type/Topic/Series surface, but runtime validation exposed a build defect described below.

## Tests and build evidence

GitHub Actions run **36687172696** (`Build and Deploy`, head `63289f26ad99dfca7b8afcbc58af72b6e25cdcf5`) completed with **failure**.

Evidence from the run:

- Regression-test step: **PASS**, `27` tests run, `OK`.
- Jekyll build step: **FAIL**.
- Failure: `Liquid Exception: undefined method 'gsub' for an instance of Integer in _layouts/post.html` while Jekyll's `slugify` filter was rendering post metadata.
- The migrated `2025-06-11-计组-08.md` currently has `tags: [Assembly Language, 8086, Procedures, Stack]`; YAML parses unquoted `8086` as an integer, and `_layouts/post.html` applies `slugify` directly to each tag. This is a migration-caused build blocker. No build/runtime PASS is claimed.

## Unresolved review items / blockers

1. **Build blocker:** quote the numeric canonical tag (`"8086"`) or make taxonomy tag rendering stringify values before `slugify`, then obtain a successful Jekyll build on the resulting commit.
2. **Body-diff verification:** independently compare article bodies for the three large-stat replacement diffs listed above against the pre-migration baseline to rule out accidental prose changes rather than relying on patch statistics.
3. **Global tag vocabulary:** confirm that the increase from 93 legacy unique strings to 157 final canonical strings is acceptable under the intended “reduced/canonicalized” model, or perform another evidence-based canonical reduction without altering bodies.

Because these items remain unresolved, Step 8 must remain unchecked.

## Relevant commits

- Inventory/audit foundation: `27e2187bbbb9b3c6bc51e0afa8d47586951819f0`.
- Canonical tag map: `73ff315e55a8e42777b2dd21be1dd5377a1344de`.
- Taxonomy plumbing completion: `a3cb7cc0d0f93fa8d29f6a61ea9ae3566774069c` (with preceding Step 3 commits recorded in the execution plan).
- Batch A audit completion: `15f7b9c0ddf2f18bce623838882f4d6f1f555b6d`.
- Batch B audit completion: `1e4964501134e506f5147359d4b8929a3fe4d2e3`.
- Batch C audit completion: `3318d6667afca60146e8092e0c60073208da44f1`.
- Thoughts fragment alignment: `a4ebf1e15db24046eb79a65a9674bf8ccf26088f`.
- Final article migration (#36): `0625b2786ae7514af8020c5c1002b31979cc9b5b`.
- Step 7 audit reconciliation: `3edfd5fca9ba16599ba5575e03681b69486c393f`.
- Step 7 completion state: `63289f26ad99dfca7b8afcbc58af72b6e25cdcf5`.

This report is a Step 8 validation artifact, not a declaration that Step 8 is complete.