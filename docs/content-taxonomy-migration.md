# Neutriverse Content Taxonomy Migration Audit

> Created: 2026-09-29  
> Scope: `_posts/*.md` plus the short-form fragments embedded in `_tabs/thoughts.md`  
> Migration rule: front matter / taxonomy only; article bodies are out of scope.

## Inventory baseline

### Writing sources

- Long-form/article source: `_posts/`
- Published Markdown post count: **44** (`.placeholder` excluded)
- Short-form source: `_tabs/thoughts.md`
- Current fragment count: **5**
- Total writing items in migration scope: **49**
- Thoughts are not Jekyll posts: they are YAML objects under the `fragments:` key in the Thoughts tab front matter and are rendered by `_layouts/thoughts.html`.

### Current metadata convention

Posts use YAML front matter. Observed fields include `title`, `date`, `categories`, `tags`, `description`, plus optional theme/site metadata. A representative DBMS post uses `categories: [学习笔记, DBMS笔记]` and `tags: [DBMS, E-R模型]`.

The migration must preserve all unrelated front-matter fields. New semantic fields will be `type`, `topic`, optional `series`, and canonical `tags`. Legacy `categories` may remain temporarily if required for compatibility.

### URL/permalink baseline

No repository-wide migration should rename `_posts` files or change `date`, `slug`, or `permalink` fields. Jekyll/Chirpy post URLs are therefore protected by leaving filename/date/explicit permalink metadata unchanged. Exact URL compatibility will be re-checked during final validation.

### Existing discovery machinery

- `_tabs/categories.md` uses `layout: categories` and is rendered by `_layouts/categories.html`.
- `_tabs/tags.md` uses the site's tags layout and existing Jekyll tag data.
- `_tabs/archives.md` supplies chronological discovery.
- `_tabs/thoughts.md` uses custom `layout: thoughts`, rendered by `_layouts/thoughts.html`.
- `_includes/post-series.html` already provides series-oriented presentation logic and should be examined before adding any new Series machinery.
- `_config.yml` uses `jekyll-theme-chirpy`; `tabs` and `hidden_pages` are configured as output collections.

## Source-file inventory

The 44 Markdown posts, in chronological filename order, are:

1. `_posts/2024-10-07-TestInfo.md`
2. `_posts/2024-10-08-DBMS-01.md`
3. `_posts/2024-10-09-DBMS-02.md`
4. `_posts/2024-10-12-DBMS-03.md`
5. `_posts/2024-10-14-DBMS-04.md`
6. `_posts/2024-10-15-DBMS-05.md`
7. `_posts/2024-10-22-DBMS-06.md`
8. `_posts/2024-10-29-DBMS-07.md`
9. `_posts/2024-10-30-PythonIntro.md`
10. `_posts/2024-11-05-DBMS-08.md`
11. `_posts/2024-11-12-DBMS-09.md`
12. `_posts/2024-11-19-DBMS-10.md`
13. `_posts/2025-02-26-计组-01.md`
14. `_posts/2025-03-12-计组-02.md`
15. `_posts/2025-03-27-计组-03.md`
16. `_posts/2025-04-16-计组-04.md`
17. `_posts/2025-04-25-计组-05.md`
18. `_posts/2025-05-07-计组-06.md`
19. `_posts/2025-05-21-计组-07.md`
20. `_posts/2025-06-11-计组-08.md`
21. `_posts/2025-08-22-FF1记录.md`
22. `_posts/2025-09-02-计网-01.md`
23. `_posts/2025-09-12-计网-02.md`
24. `_posts/2025-09-13-最后的纳尔马斯克.md`
25. `_posts/2025-09-15-为什么我要跳过FF2.md`
26. `_posts/2025-09-25-计网-03.md`
27. `_posts/2025-10-04-TMT理论.md`
28. `_posts/2025-10-11-计网-04.md`
29. `_posts/2025-10-15-计网-05.md`
30. `_posts/2025-10-21-计网-06.md`
31. `_posts/2025-11-05-计网-07.md`
32. `_posts/2025-11-25-计网-08.md`
33. `_posts/2025-11-29-计网-09.md`
34. `_posts/2025-12-14-计网-10.md`
35. `_posts/2025-12-17-NoSQL项目面经.md`
36. `_posts/2025-12-19-ROSSMANN项目.md`
37. `_posts/2026-02-12-不完备性.md`
38. `_posts/2026-05-24-neutriverse-site-changelog.md`
39. `_posts/2026-06-15-超过五千亿吨空气的重压之下.md`
40. `_posts/2026-06-30-阿卡夏便笺akashanotes.md`
41. `_posts/2026-07-06-于因特网标签们展开双翼.md`
42. `_posts/2026-07-09-丰聪耳机toyosatomimisheadphone.md`
43. `_posts/2026-08-07-学习笔记-progressive-disclosure和skill.md`
44. `_posts/2026-08-17-哥德尔编码和-rag-embedding-之间的关系.md`

## Fragment inventory

Current Thoughts entries (5):

| Date | Existing tags | Migration status |
|---|---|---|
| 2024-09-12 | 目标, 可能性 | pending Step 7 |
| 2024-10-30 | 交流 | pending Step 7 |
| 2025-03-23 | 等待 | pending Step 7 |
| 2025-11-12 | 孤独 | pending Step 7 |
| 2026-05-02 | 侦探小说 | pending Step 7 |

## Article migration table

This table is intentionally initialized from the source inventory. Old categories/tags and all new classifications are filled only after the relevant article has been read; filename-only classification is prohibited.

| # | Article | Old Category | Old Tags | New Type | New Topic | New Series | New Tags | Confidence | Notes |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | 2024-10-07-TestInfo.md | pending read | pending read | — | — | — | — | — | — |
| 2 | 2024-10-08-DBMS-01.md | 学习笔记; DBMS笔记 | DBMS; E-R模型 | — | — | — | — | — | representative front matter inspected in Step 1 |
| 3 | 2024-10-09-DBMS-02.md | pending read | pending read | — | — | — | — | — | — |
| 4 | 2024-10-12-DBMS-03.md | pending read | pending read | — | — | — | — | — | — |
| 5 | 2024-10-14-DBMS-04.md | pending read | pending read | — | — | — | — | — | — |
| 6 | 2024-10-15-DBMS-05.md | pending read | pending read | — | — | — | — | — | — |
| 7 | 2024-10-22-DBMS-06.md | pending read | pending read | — | — | — | — | — | — |
| 8 | 2024-10-29-DBMS-07.md | pending read | pending read | — | — | — | — | — | — |
| 9 | 2024-10-30-PythonIntro.md | pending read | pending read | — | — | — | — | — | — |
| 10 | 2024-11-05-DBMS-08.md | pending read | pending read | — | — | — | — | — | — |
| 11 | 2024-11-12-DBMS-09.md | pending read | pending read | — | — | — | — | — | — |
| 12 | 2024-11-19-DBMS-10.md | pending read | pending read | — | — | — | — | — | — |
| 13 | 2025-02-26-计组-01.md | pending read | pending read | — | — | — | — | — | — |
| 14 | 2025-03-12-计组-02.md | pending read | pending read | — | — | — | — | — | — |
| 15 | 2025-03-27-计组-03.md | pending read | pending read | — | — | — | — | — | — |
| 16 | 2025-04-16-计组-04.md | pending read | pending read | — | — | — | — | — | — |
| 17 | 2025-04-25-计组-05.md | pending read | pending read | — | — | — | — | — | — |
| 18 | 2025-05-07-计组-06.md | pending read | pending read | — | — | — | — | — | — |
| 19 | 2025-05-21-计组-07.md | pending read | pending read | — | — | — | — | — | — |
| 20 | 2025-06-11-计组-08.md | pending read | pending read | — | — | — | — | — | — |
| 21 | 2025-08-22-FF1记录.md | pending read | pending read | — | — | — | — | — | — |
| 22 | 2025-09-02-计网-01.md | pending read | pending read | — | — | — | — | — | — |
| 23 | 2025-09-12-计网-02.md | pending read | pending read | — | — | — | — | — | — |
| 24 | 2025-09-13-最后的纳尔马斯克.md | pending read | pending read | — | — | — | — | — | — |
| 25 | 2025-09-15-为什么我要跳过FF2.md | pending read | pending read | — | — | — | — | — | — |
| 26 | 2025-09-25-计网-03.md | pending read | pending read | — | — | — | — | — | — |
| 27 | 2025-10-04-TMT理论.md | pending read | pending read | — | — | — | — | — | — |
| 28 | 2025-10-11-计网-04.md | pending read | pending read | — | — | — | — | — | — |
| 29 | 2025-10-15-计网-05.md | pending read | pending read | — | — | — | — | — | — |
| 30 | 2025-10-21-计网-06.md | pending read | pending read | — | — | — | — | — | — |
| 31 | 2025-11-05-计网-07.md | pending read | pending read | — | — | — | — | — | — |
| 32 | 2025-11-25-计网-08.md | pending read | pending read | — | — | — | — | — | — |
| 33 | 2025-11-29-计网-09.md | pending read | pending read | — | — | — | — | — | — |
| 34 | 2025-12-14-计网-10.md | pending read | pending read | — | — | — | — | — | — |
| 35 | 2025-12-17-NoSQL项目面经.md | pending read | pending read | — | — | — | — | — | — |
| 36 | 2025-12-19-ROSSMANN项目.md | pending read | pending read | — | — | — | — | — | — |
| 37 | 2026-02-12-不完备性.md | pending read | pending read | — | — | — | — | — | — |
| 38 | 2026-05-24-neutriverse-site-changelog.md | pending read | pending read | — | — | — | — | — | — |
| 39 | 2026-06-15-超过五千亿吨空气的重压之下.md | pending read | pending read | — | — | — | — | — | — |
| 40 | 2026-06-30-阿卡夏便笺akashanotes.md | pending read | pending read | — | — | — | — | — | — |
| 41 | 2026-07-06-于因特网标签们展开双翼.md | pending read | pending read | — | — | — | — | — | — |
| 42 | 2026-07-09-丰聪耳机toyosatomimisheadphone.md | pending read | pending read | — | — | — | — | — | — |
| 43 | 2026-08-07-学习笔记-progressive-disclosure和skill.md | pending read | pending read | — | — | — | — | — | — |
| 44 | 2026-08-17-哥德尔编码和-rag-embedding-之间的关系.md | pending read | pending read | — | — | — | — | — | — |

## Step 1 findings / constraints

1. The content architecture is conventional Jekyll/Chirpy for posts and custom front-matter data for Thoughts; no separate `_thoughts` collection exists.
2. Category and tag discovery are already implemented, so the new taxonomy should adapt rather than replace this machinery.
3. A custom `_includes/post-series.html` exists; Step 3 must inspect its current contract before implementing Series changes.
4. Article URL preservation is compatible with front-matter-only taxonomy edits provided filenames, dates, slugs, and explicit permalinks are not changed.
5. Full old-tag canonicalization belongs to Step 2; this audit deliberately does not infer tags or categories from filenames.
6. No article body content was changed during inventory.
