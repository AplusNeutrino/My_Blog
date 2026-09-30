# Neutriverse Content Taxonomy Final Report

> Validation snapshot: 2026-09-30  
> Repository state validated: `01bc78839bd943646de7f3fd826e6050ddd21db1` before this report update  
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

The unique-string count increased because the legacy vocabulary was dominated by repeatedly reused broad structural/course labels, while the approved model explicitly calls for a small per-item set of specific works/entities, technical concepts, analytical themes and named theories/frameworks/people. The migration therefore treats “reduced/canonicalized” as reduction of generic/redundant labels and bounded per-item tag sets, not as a requirement that the global count of distinct specific concepts be lower than the legacy count. Per-item tag counts remain within the plan's Fragment 0–3, Note 2–5 and Essay 3–6 guidance. On that documented interpretation, the final vocabulary satisfies the approved model without deleting useful one-off retrieval concepts merely to force a smaller global number.

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

The authoritative audit and batch execution evidence state that migration did not rename post files or intentionally change `date`, `slug`, or explicit `permalink` fields. A repository compare from the completed taxonomy-plumbing baseline (`a3cb7cc0d0f93fa8d29f6a61ea9ae3566774069c`) to the completed Step 7 state (`63289f26ad99dfca7b8afcbc58af72b6e25cdcf5`) shows the same migrated `_posts/*.md` paths as modified files, with no migrated post path reported as renamed or deleted. URL compatibility is preserved at the file/path level; no URL-changing migration is recorded.

## Body-preservation validation

Batch audit entries record that every article body was read before classification and that body prose was preserved. The baseline-to-Step-7 compare showed front-matter-sized diffs for most migrated articles. Three files had whole-file-sized add/delete statistics caused by newline/serialization normalization and therefore received independent pre/post review:

- `2024-10-07-TestInfo.md` — pre/post body comparison completed; body preserved.
- `2025-12-17-NoSQL项目面经.md` — pre/post body comparison completed; body preserved.
- `2025-12-19-ROSSMANN项目.md` — complete pre-migration body at parent `cef59e90a895b85e96c2a62b3f0c875d6e204ac0` was compared in ranges against current state `01bc78839bd943646de7f3fd826e6050ddd21db1`; after accounting for the five additional taxonomy front-matter lines, the body content matches through the end of the file. The large commit statistic is attributable to CRLF→LF normalization plus front-matter changes, not prose changes.

No accidental article-body edit remains identified by Step 8 validation.

## Taxonomy surfaces

Step 3 added `_data/content_taxonomy.yml` and `_includes/post-taxonomy.html`, and adapted `_layouts/post.html` plus `_includes/post-series.html`. The final GitHub Actions validation below confirms the resulting site builds successfully.

## Tests and build evidence

An earlier GitHub Actions run, `36687172696`, exposed a real Jekyll failure: `_posts/2025-06-11-计组-08.md` had canonical tag `8086` parsed by YAML as an integer before `_layouts/post.html` applied `slugify`. Commit `5fc783bcb82beadaeba157ed1c38f83216442e11` corrected the front matter by quoting `"8086"`; no article body was changed.

Final validation is GitHub Actions run **36699387397**, workflow **Build and Deploy**, at head **`01bc78839bd943646de7f3fd826e6050ddd21db1`**. The run completed with **success**. Its `build` job completed successfully, including `Run regression tests`, `Build site`, and `Upload site artifact`; its `deploy` job also completed successfully, including `Deploy to GitHub Pages`. This is the runtime/build evidence used for the final PASS claim.

## Unresolved review items

**None.** Step 7 recorded no owner-review classification items. Step 8 resolved the numeric-tag build defect, all three large-diff body-preservation checks, and the interpretation of canonical tag reduction under the approved per-item/specific-concept model.

## Relevant commits

- Inventory/audit foundation: `27e2187bbbb9b3c6bc51e0afa8d47586951819f0`.
- Canonical tag map: `73ff315e55a8e42777b2dd21be1dd5377a1344de`.
- Taxonomy plumbing completion: `a3cb7cc0d0f93fa8d29f6a61ea9ae3566774069c`.
- Batch A audit completion: `15f7b9c0ddf2f18bce623838882f4d6f1f555b6d`.
- Batch B audit completion: `1e4964501134e506f5147359d4b8929a3fe4d2e3`.
- Batch C audit completion: `3318d6667afca60146e8092e0c60073208da44f1`.
- Thoughts fragment alignment: `a4ebf1e15db24046eb79a65a9674bf8ccf26088f`.
- Final article migration (#36): `0625b2786ae7514af8020c5c1002b31979cc9b5b`.
- Step 7 audit reconciliation: `3edfd5fca9ba16599ba5575e03681b69486c393f`.
- Step 7 completion state: `63289f26ad99dfca7b8afcbc58af72b6e25cdcf5`.
- Numeric-tag Jekyll compatibility fix: `5fc783bcb82beadaeba157ed1c38f83216442e11`.
- Numeric-tag validation-report update / successful workflow head: `01bc78839bd943646de7f3fd826e6050ddd21db1`.

Step 8 validation is complete. The plan file records the final completion commit separately.