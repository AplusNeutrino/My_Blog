# Neutriverse Tag Second-Pass Review

> T04 artifact, 2026-10-04. Source head: `b2a2a15321efb0c443b57f001368227105b1cdce`. 
> Scope: 44 posts and 5 Fragments. This is a decision audit; T04 does not edit content metadata.

## Method and guardrails

- Read the current `tags` arrays from all 49 writing items; visibility is recorded separately from semantic value.
- Compare exact names and meanings against Type, Topic, Series and the first-pass canonical map.
- A one-off tag is kept when it names a work/entity, technical concept or concrete analytical theme.
- T04 proposes only finite changes. T05 applies accepted metadata edits and compatibility routes; T17 completes public-index filtering.
- Item references use `H:` for hidden posts and `F:` for Fragments.

## Inventory summary

| Measure | Current | After proposed T05 changes |
|---|---:|---:|
| Writing items | 49 | 49 |
| Unique tags | 157 | 155 |
| Tag assignments | 165 | 164 |
| Used once | 150 | n/a until T05 |
| Used twice | 6 | n/a until T05 |
| Used three times | 1 | n/a until T05 |
| Hidden-only tags | 17 | semantic tags retained; public listing filtered separately |
| Mixed public/hidden tags | 0 | unchanged |

The frequency distribution is sparse, but that reflects a small and varied archive. It is not evidence that named works or precise concepts should be deleted.

## Finite change set for T05

| Current tag | Decision | Canonical target | Metadata effect | Legacy tag URL strategy |
|---|---|---|---|---|
| `Bus` | MERGE | `System Bus` | Replace one assignment; target then has two uses. | Preserve `/tags/bus/` as a noindex redirect stub to `/tags/system-bus/`. |
| `Changelog` | RETIRE | — | Remove one editorial-form assignment; keep `Neutriverse` and `Jekyll`. | Preserve `/tags/changelog/` as a noindex redirect stub to `/tags/neutriverse/`. |

No other tag change is proposed. In particular, hidden-only tags remain semantically intact: deleting metadata is not a substitute for fixing public tag indexes. Fragment tags remain in their existing language, and one-off works/entities remain available for future retrieval.

## Complete decision inventory

| Tag | Uses | Public | Hidden | Decision | Target | Reason | Item references |
|---|---:|---:|---:|---|---|---|---|
| `8086` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-06-11-计组-08 |
| `Access Control` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-10-22-DBMS-06 |
| `ACID` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-11-12-DBMS-09 |
| `Addressing Modes` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-04-16-计组-04 |
| `Affective Polarization` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-07-06-于因特网标签们展开双翼 |
| `Agent Skills` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-08-07-学习笔记-progressive-disclosure和skill |
| `Akasha Notes` | 1 | 1 | 0 | KEEP | `—` | 命名作品、人物或实体，具有直接检索价值；即使单次出现也保留。 | 2026-06-30-阿卡夏便笺akashanotes |
| `ALU` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-03-12-计组-02 |
| `Assembly Language` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-06-11-计组-08 |
| `BitTorrent` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-12-14-计网-10 |
| `Bus` | 1 | 1 | 0 | MERGE | `System Bus` | 与现有 `System Bus` 指向同一硬件互连概念；统一命名可形成跨文章检索。 | 2025-05-07-计组-06 |
| `Cache` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-03-27-计组-03 |
| `Cantor Diagonal Argument` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-02-12-不完备性 |
| `Changelog` | 1 | 0 | 1 | RETIRE | `—` | 编辑形式而非主题；同篇仍有 `Neutriverse` 与 `Jekyll`，检索信息不会丢失。 | H:2026-05-24-neutriverse-site-changelog |
| `CIDR` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-10-11-计网-04 |
| `CISC` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-04-16-计组-04 |
| `Computer Systems` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-02-26-计组-01 |
| `Concurrency Control` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-11-12-DBMS-09 |
| `Congestion Control` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-10-15-计网-05 |
| `Context Engineering` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-08-07-学习笔记-progressive-disclosure和skill |
| `Control Unit` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-04-25-计组-05 |
| `CPU` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-04-25-计组-05 |
| `CPU Performance` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-02-26-计组-01 |
| `CRC` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-09-25-计网-03 |
| `Cryptography` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-11-05-计网-07 |
| `CSMA/CA` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-11-25-计网-08 |
| `DAC` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-10-22-DBMS-06 |
| `Data Independence` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-10-08-DBMS-01 |
| `Data Link Layer` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-09-25-计网-03 |
| `Data Modeling` | 1 | 0 | 1 | KEEP | `—` | 具体概念仅用于 hidden 内容；不以可见性替代语义判断，公开索引过滤交由 T05/T17。 | H:2025-12-17-NoSQL项目面经 |
| `Data Models` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-10-08-DBMS-01 |
| `Data Representation` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-03-12-计组-02 |
| `Database Design` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-11-19-DBMS-10 |
| `Database Recovery` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-11-05-DBMS-08 |
| `Database Security` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-10-22-DBMS-06 |
| `DDoS` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-11-05-计网-07 |
| `Denormalization` | 1 | 0 | 1 | KEEP | `—` | 具体概念仅用于 hidden 内容；不以可见性替代语义判断，公开索引过滤交由 T05/T17。 | H:2025-12-17-NoSQL项目面经 |
| `Desktop Widgets` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-06-30-阿卡夏便笺akashanotes |
| `DHCP` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-10-21-计网-06 |
| `DMA` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-05-07-计组-06 |
| `DNS` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-10-21-计网-06 |
| `DRAM` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-03-27-计组-03 |
| `E-R Model` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-10-08-DBMS-01 |
| `Embeddings` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-08-17-哥德尔编码和-rag-embedding-之间的关系 |
| `Ernest Becker` | 1 | 1 | 0 | KEEP | `—` | 命名作品、人物或实体，具有直接检索价值；即使单次出现也保留。 | 2025-10-04-TMT理论 |
| `Ethernet` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-09-25-计网-03 |
| `Fan Fiction` | 1 | 0 | 1 | KEEP | `—` | 具体概念仅用于 hidden 内容；不以可见性替代语义判断，公开索引过滤交由 T05/T17。 | H:2025-09-13-最后的纳尔马斯克 |
| `Feature Engineering` | 1 | 0 | 1 | KEEP | `—` | 具体概念仅用于 hidden 内容；不以可见性替代语义判断，公开索引过滤交由 T05/T17。 | H:2025-12-19-ROSSMANN项目 |
| `Final Fantasy` | 1 | 1 | 0 | KEEP | `—` | 命名作品、人物或实体，具有直接检索价值；即使单次出现也保留。 | 2025-08-22-FF1记录 |
| `Final Fantasy II` | 1 | 1 | 0 | KEEP | `—` | 命名作品、人物或实体，具有直接检索价值；即使单次出现也保留。 | 2025-09-15-为什么我要跳过FF2 |
| `Final Fantasy XIV` | 1 | 0 | 1 | KEEP | `—` | 具体概念仅用于 hidden 内容；不以可见性替代语义判断，公开索引过滤交由 T05/T17。 | H:2025-09-13-最后的纳尔马斯克 |
| `Firewall` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-11-05-计网-07 |
| `Flow Control` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-10-15-计网-05 |
| `FTP` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-10-21-计网-06 |
| `Functional Dependencies` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-11-19-DBMS-10 |
| `Game Design` | 2 | 2 | 0 | KEEP | `—` | 已在 2 个内容项复用，且未与 Type、Topic 或 Series 重复。 | 2025-08-22-FF1记录, 2025-09-15-为什么我要跳过FF2 |
| `Garlean Empire` | 1 | 0 | 1 | KEEP | `—` | 具体概念仅用于 hidden 内容；不以可见性替代语义判断，公开索引过滤交由 T05/T17。 | H:2025-09-13-最后的纳尔马斯克 |
| `Gödel Numbering` | 2 | 2 | 0 | KEEP | `—` | 已在 2 个内容项复用，且未与 Type、Topic 或 Series 重复。 | 2026-02-12-不完备性, 2026-08-17-哥德尔编码和-rag-embedding-之间的关系 |
| `Halting Problem` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-02-12-不完备性 |
| `HTTP` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-10-21-计网-06 |
| `I/O` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-05-07-计组-06 |
| `ICMP` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-10-11-计网-04 |
| `Identity` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-06-15-超过五千亿吨空气的重压之下 |
| `IDS/IPS` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-11-05-计网-07 |
| `IEEE 754` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-03-12-计组-02 |
| `Immortality Project` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-10-04-TMT理论 |
| `Incompleteness Theorems` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-02-12-不完备性 |
| `Indexing` | 1 | 0 | 1 | KEEP | `—` | 具体概念仅用于 hidden 内容；不以可见性替代语义判断，公开索引过滤交由 T05/T17。 | H:2025-12-17-NoSQL项目面经 |
| `Innocence` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-06-15-超过五千亿吨空气的重压之下 |
| `Instruction Cycle` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-05-21-计组-07 |
| `Instruction Set Architecture` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-04-16-计组-04 |
| `Integrity Constraints` | 3 | 3 | 0 | KEEP | `—` | 已在 3 个内容项复用，且未与 Type、Topic 或 Series 重复。 | 2024-10-09-DBMS-02, 2024-10-14-DBMS-04, 2024-10-29-DBMS-07 |
| `Interrupts` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-05-07-计组-06 |
| `IPv4` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-10-11-计网-04 |
| `IPv6` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-12-14-计网-10 |
| `Jekyll` | 1 | 0 | 1 | KEEP | `—` | 具体概念仅用于 hidden 内容；不以可见性替代语义判断，公开索引过滤交由 T05/T17。 | H:2026-05-24-neutriverse-site-changelog |
| `Join Algorithms` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-10-15-DBMS-05 |
| `JRPG` | 2 | 2 | 0 | KEEP | `—` | 已在 2 个内容项复用，且未与 Type、Topic 或 Series 重复。 | 2025-08-22-FF1记录, 2025-09-15-为什么我要跳过FF2 |
| `Locking` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-11-12-DBMS-09 |
| `MAC` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-10-22-DBMS-06 |
| `Markdown` | 1 | 0 | 1 | KEEP | `—` | 具体概念仅用于 hidden 内容；不以可见性替代语义判断，公开索引过滤交由 T05/T17。 | H:2024-10-07-TestInfo |
| `Memory Hierarchy` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-03-27-计组-03 |
| `Microcomputer` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-05-21-计组-07 |
| `Mobile Networks` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-11-25-计网-08 |
| `MongoDB` | 1 | 0 | 1 | KEEP | `—` | 具体概念仅用于 hidden 内容；不以可见性替代语义判断，公开索引过滤交由 T05/T17。 | H:2025-12-17-NoSQL项目面经 |
| `MPLS` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-12-14-计网-10 |
| `Multiplexing` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-09-12-计网-02 |
| `Narrative Design` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-08-22-FF1记录 |
| `NAT` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-10-11-计网-04 |
| `Network Architecture` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-09-02-计网-01 |
| `Network Security` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-11-05-计网-07 |
| `Neutriverse` | 1 | 0 | 1 | KEEP | `—` | 具体概念仅用于 hidden 内容；不以可见性替代语义判断，公开索引过滤交由 T05/T17。 | H:2026-05-24-neutriverse-site-changelog |
| `Nhalmasque` | 1 | 0 | 1 | KEEP | `—` | 具体概念仅用于 hidden 内容；不以可见性替代语义判断，公开索引过滤交由 T05/T17。 | H:2025-09-13-最后的纳尔马斯克 |
| `Normalization` | 2 | 2 | 0 | KEEP | `—` | 已在 2 个内容项复用，且未与 Type、Topic 或 Series 重复。 | 2024-10-09-DBMS-02, 2024-11-19-DBMS-10 |
| `OSI Model` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-09-02-计网-01 |
| `Out-group Animosity` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-07-06-于因特网标签们展开双翼 |
| `P2P` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-12-14-计网-10 |
| `Packet Switching` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-09-02-计网-01 |
| `Physical Layer` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-09-12-计网-02 |
| `Pipelining` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-04-25-计组-05 |
| `Procedures` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-06-11-计组-08 |
| `Progression Systems` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-09-15-为什么我要跳过FF2 |
| `Progressive Disclosure` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-08-07-学习笔记-progressive-disclosure和skill |
| `Python` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-10-30-PythonIntro |
| `QoS` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-11-29-计网-09 |
| `Query Optimization` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-10-15-DBMS-05 |
| `Query Processing` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-10-15-DBMS-05 |
| `RAG` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-08-17-哥德尔编码和-rag-embedding-之间的关系 |
| `REDO` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-11-05-DBMS-08 |
| `Relational Algebra` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-10-12-DBMS-03 |
| `Relational Databases` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-10-09-DBMS-02 |
| `RISC` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-04-16-计组-04 |
| `RMSPE` | 1 | 0 | 1 | KEEP | `—` | 具体概念仅用于 hidden 内容；不以可见性替代语义判断，公开索引过滤交由 T05/T17。 | H:2025-12-19-ROSSMANN项目 |
| `Routing` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-10-11-计网-04 |
| `RTP/RTCP` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-11-29-计网-09 |
| `Sales Forecasting` | 1 | 0 | 1 | KEEP | `—` | 具体概念仅用于 hidden 内容；不以可见性替代语义判断，公开索引过滤交由 T05/T17。 | H:2025-12-19-ROSSMANN项目 |
| `Semantic Search` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-08-17-哥德尔编码和-rag-embedding-之间的关系 |
| `Shannon Capacity` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-09-12-计网-02 |
| `Signal Encoding` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-09-12-计网-02 |
| `SIP` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-11-29-计网-09 |
| `Site Styling` | 1 | 0 | 1 | KEEP | `—` | 具体概念仅用于 hidden 内容；不以可见性替代语义判断，公开索引过滤交由 T05/T17。 | H:2024-10-07-TestInfo |
| `Social Conformity` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-06-15-超过五千亿吨空气的重压之下 |
| `Social Identity` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-07-06-于因特网标签们展开双翼 |
| `Social Media` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-07-06-于因特网标签们展开双翼 |
| `Speech-to-Text` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-07-09-丰聪耳机toyosatomimisheadphone |
| `SQL` | 2 | 2 | 0 | KEEP | `—` | 已在 2 个内容项复用，且未与 Type、Topic 或 Series 重复。 | 2024-10-12-DBMS-03, 2024-10-14-DBMS-04 |
| `SRAM` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-03-27-计组-03 |
| `Stack` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-06-11-计组-08 |
| `Symbolic Immortality` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-10-04-TMT理论 |
| `System Bus` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-05-21-计组-07 |
| `TCP` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-10-15-计网-05 |
| `TCP/IP` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-09-02-计网-01 |
| `Terror Management Theory` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-10-04-TMT理论 |
| `Tool Routing` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-08-07-学习笔记-progressive-disclosure和skill |
| `Toyosatomimi's Headphone` | 1 | 1 | 0 | KEEP | `—` | 命名作品、人物或实体，具有直接检索价值；即使单次出现也保留。 | 2026-07-09-丰聪耳机toyosatomimisheadphone |
| `Translation` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2026-07-09-丰聪耳机toyosatomimisheadphone |
| `Triggers` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-10-29-DBMS-07 |
| `Two's Complement` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-03-12-计组-02 |
| `Two-Phase Locking` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-11-12-DBMS-09 |
| `UDP` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-10-15-计网-05 |
| `UNDO` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-11-05-DBMS-08 |
| `Views` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-10-14-DBMS-04 |
| `VLAN` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-09-25-计网-03 |
| `VoIP` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-11-29-计网-09 |
| `Von Neumann Architecture` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-02-26-计组-01 |
| `Wi-Fi` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-11-25-计网-08 |
| `Windows` | 2 | 2 | 0 | KEEP | `—` | 已在 2 个内容项复用，且未与 Type、Topic 或 Series 重复。 | 2026-06-30-阿卡夏便笺akashanotes, 2026-07-09-丰聪耳机toyosatomimisheadphone |
| `WPAN` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2025-11-25-计网-08 |
| `Write-Ahead Logging` | 1 | 1 | 0 | KEEP | `—` | 具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。 | 2024-11-05-DBMS-08 |
| `XGBoost` | 1 | 0 | 1 | KEEP | `—` | 具体概念仅用于 hidden 内容；不以可见性替代语义判断，公开索引过滤交由 T05/T17。 | H:2025-12-19-ROSSMANN项目 |
| `Z.A.T.O.` | 1 | 1 | 0 | KEEP | `—` | 命名作品、人物或实体，具有直接检索价值；即使单次出现也保留。 | 2026-06-15-超过五千亿吨空气的重压之下 |
| `交流` | 1 | 1 | 0 | KEEP | `—` | 保留 Fragment 原有检索词与语言；未发现同义冲突，不为统一英文而改写。 | F:2024-10-30 |
| `侦探小说` | 1 | 1 | 0 | KEEP | `—` | 保留 Fragment 原有检索词与语言；未发现同义冲突，不为统一英文而改写。 | F:2026-05-02 |
| `可能性` | 1 | 1 | 0 | KEEP | `—` | 保留 Fragment 原有检索词与语言；未发现同义冲突，不为统一英文而改写。 | F:2024-09-12 |
| `孤独` | 1 | 1 | 0 | KEEP | `—` | 保留 Fragment 原有检索词与语言；未发现同义冲突，不为统一英文而改写。 | F:2025-11-12 |
| `目标` | 1 | 1 | 0 | KEEP | `—` | 保留 Fragment 原有检索词与语言；未发现同义冲突，不为统一英文而改写。 | F:2024-09-12 |
| `等待` | 1 | 1 | 0 | KEEP | `—` | 保留 Fragment 原有检索词与语言；未发现同义冲突，不为统一英文而改写。 | F:2025-03-23 |

## T05 handoff

1. Change only the two assignments listed above and update the authoritative migration audit/final counts.
2. Add the two explicit legacy tag route stubs before generated archive pages disappear.
3. Make public tag aggregation count/list only non-hidden posts; do not expose hidden-only names through the public index or trending tags.
4. Re-run the content-protection baseline so article/Fragment bodies and protected URL metadata remain unchanged.
5. Verify the exact implementation SHA with regression tests, Jekyll build and Pages deployment.
