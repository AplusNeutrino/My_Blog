# Neutriverse Canonical Tag and Legacy Taxonomy Map

> Step 2 artifact, 2026-09-29. Source: front matter of all 44 `_posts/*.md` files plus the 5 current Thoughts fragments. This document defines migration intent; final per-article tags are assigned only after the article body is read in Steps 4–7.

## Canonical policy

Tags are for **specific retrieval concepts**, not structural classification. Type, Topic and Series carry structure.

Keep/canonicalize tags when they identify: (1) a named work/franchise/entity; (2) a concrete technical concept/protocol/tool; (3) a specific analytical theme; or (4) a named theory/person/framework. Retire tags whose only job is to mean note/record/maintenance, a broad medium/domain already represented by Topic, or a course/subject grouping better represented by Series.

Target tag counts remain: Fragment 0–3, Note 2–5, Essay 3–6. A useful one-off tag is not removed merely because it appears once.

## Legacy category → new role

| Legacy category | New role / disposition |
|---|---|
| 学习笔记 | Retire as structural category; Type becomes `note` or `essay` after body read. |
| 记忆碎片 | Retire as structural category; Type becomes `note`/`essay`; true short fragments remain in Thoughts as `fragment`. |
| 思维链条 | Retire as structural category; argument depth is represented by Type. |
| 阅览记录 | Retire; Type + Topic replaces it. |
| 游戏记录 | Retire; `topic: otaku`, with specific work/franchise retained as tags. |
| DBMS笔记 | Durable Series candidate: `Database Systems`. |
| 计组笔记 | Durable Series candidate: `Computer Architecture`. |
| 计网笔记 | Durable Series candidate: `Computer Networks`. |
| Python笔记 | Durable Series candidate only if more Python notes exist later; do not force a one-item Series during migration. |
| LLM笔记 | Durable Series candidate: `LLM Systems` (current item count is small; retain only if body-level migration confirms continuity). |
| 面试经验 | Retire as category; preserve concrete project/technology tags. Could become a future Series only if the user develops it as a continuing line. |
| 软件发布 | Retire as category; software/product name and technologies are tags; BUILD/project plumbing is outside this taxonomy migration. |
| 站点维护 | Retire as category; `Neutriverse` may remain a specific entity tag. |
| 地下墓穴 | Legacy presentation/visibility category; do not reinterpret until the hidden FFXIV article is read. Preserve compatibility if template logic depends on it. |
| FFXIV | Not a structural category in the new model; canonical specific work/franchise tag should be `Final Fantasy XIV` if body review confirms. |

## Canonical old → new tag map

`KEEP` means the current spelling is already useful. `MERGE` gives the preferred canonical form. `RETIRE` means structural/generic information should be represented elsewhere. `REVIEW` means body reading is required before final assignment.

### Database / programming

| Old tag | Action | Canonical tag / note |
|---|---|---|
| DBMS | MERGE | `Database Systems` — broad subject belongs primarily to Series; retain as tag only where retrieval value remains after body read. |
| E-R模型 | MERGE | `Entity–Relationship Model` |
| 关系数据库 | MERGE | `Relational Database` |
| 三类约束 | MERGE | `Database Constraints` |
| 三大范式 | MERGE | `Database Normalization` |
| 关系代数运算 | MERGE | `Relational Algebra` |
| SQL | KEEP | `SQL` |
| 关系查询 | MERGE | `Query Processing` |
| 数据库安全性 | MERGE | `Database Security` |
| 存取控制 | MERGE | `Access Control` |
| 数据库完整性 | MERGE | `Data Integrity` |
| 数据库恢复 | MERGE | `Database Recovery` |
| 并发控制 | MERGE | `Concurrency Control` |
| ACID特性 | MERGE | `ACID` |
| 封锁机制 | MERGE | `Locking` |
| 函数依赖分析 | MERGE | `Functional Dependency` |
| 范式规范 | MERGE | `Database Normalization` |
| Python | KEEP | `Python` |
| NoSQL | KEEP | `NoSQL` |
| XGBoost | KEEP | `XGBoost` |

### Computer architecture

| Old tag | Action | Canonical tag / note |
|---|---|---|
| 计算机组成原理 | RETIRE | Series `Computer Architecture` carries the broad subject. |
| 计算机系统 | MERGE | `Computer Systems` |
| 计算机数据 | MERGE | `Data Representation` |
| 存储器 | MERGE | `Memory Hierarchy` when that is the actual article focus. |
| RAM | KEEP | `RAM` |
| 指令 | MERGE | `Instruction Set` |
| 寻址 | MERGE | `Addressing Modes` |
| CPU | KEEP | `CPU` |
| 总线 | MERGE | `System Bus` |
| I/O | KEEP | `I/O` |
| 微机 | MERGE | `Microcomputer` |
| 汇编语言 | MERGE | `Assembly Language` |

### Computer networks

| Old tag | Action | Canonical tag / note |
|---|---|---|
| 计算机网络 | RETIRE | Series `Computer Networks` carries the broad subject. |
| 物理层 | MERGE | `Physical Layer` |
| 数据链路层 | MERGE | `Data Link Layer` |
| 网络层 | MERGE | `Network Layer` |
| 传输层 | MERGE | `Transport Layer` |
| HTTP | KEEP | `HTTP` |
| FTP | KEEP | `FTP` |
| DNS | KEEP | `DNS` |
| DHCP | KEEP | `DHCP` |
| 网络安全 | MERGE | `Network Security` |
| IPS | KEEP | `IPS` |
| 防火墙 | MERGE | `Firewall` |
| DDOS | MERGE | `DDoS` (case normalization) |
| WPAN | KEEP | `WPAN` |
| GSM | KEEP | `GSM` |
| 3G三大标准 | MERGE | `3G` unless body review identifies specific standards worth separate tags. |
| VoIP | KEEP | `VoIP` |
| IP 电话网关 | MERGE | `VoIP Gateway` |
| H.323 | KEEP | `H.323` |
| SIP | KEEP | `SIP` |
| SDP | KEEP | `SDP` |
| QoS 指标 | MERGE | `QoS` |
| IPv4/IPv6 | SPLIT/REVIEW | Prefer `IPv4` and `IPv6` when both materially discussed. |
| MPLS | KEEP | `MPLS` |
| P2P | KEEP | `P2P` |

### AI / software / web

| Old tag | Action | Canonical tag / note |
|---|---|---|
| Progressive Disclosure | KEEP | `Progressive Disclosure` |
| SKILL | MERGE | `Agent Skills` if the article refers to the SKILL.md agent-skill mechanism; confirm on body read. |
| Embedding | KEEP | `Embedding` |
| RAG | KEEP | `RAG` |
| 哥德尔编码 | MERGE | `Gödel Numbering` |
| 桌面便签 | MERGE | `Desktop Notes` |
| Windows | KEEP | `Windows` |
| 小工具 | RETIRE | Generic product-form label; specific product/technology tags are more useful. |
| STT | MERGE | `Speech-to-Text` |
| Neutriverse | KEEP | `Neutriverse` |
| Changelog | RETIRE | Editorial form, not subject matter. |
| 维护记录 | RETIRE | Editorial form, not subject matter. |

### Works / culture / humanities

| Old tag | Action | Canonical tag / note |
|---|---|---|
| 最终幻想 | MERGE | `Final Fantasy` |
| FFXIV | MERGE | `Final Fantasy XIV` |
| 神圣而可怖的空气 | REVIEW | Preserve if this is a distinct named work/translation/entity; otherwise merge into the work tag after body read. |
| Z.A.T.O. | KEEP | `Z.A.T.O.` |
| 东方Project | MERGE | `Touhou Project` |
| 丰聪耳神子 | MERGE | `Toyosatomimi no Miko` |
| TMT | MERGE | `Terror Management Theory` |
| Ernest Becker | KEEP | `Ernest Becker` |
| Immortality Project | KEEP | `Immortality Project` |
| 不完备性 | MERGE | `Incompleteness Theorems` |
| 康托尔对角线法 | MERGE | `Cantor's Diagonal Argument` |
| 理查德悖论 | MERGE | `Richard's Paradox` |
| 哥德尔第一不完备性定理 | MERGE | `Gödel's First Incompleteness Theorem` |
| 哥德尔第二不完备性定理 | MERGE | `Gödel's Second Incompleteness Theorem` |
| 社会身份 | MERGE | `Social Identity` |
| 情感极化 | MERGE | `Affective Polarization` |
| 外群体敌意 | MERGE | `Out-group Hostility` |

### Thoughts fragment tags

| Old tag | Action | Canonical tag / note |
|---|---|---|
| 目标 | MERGE | `Goals` |
| 可能性 | MERGE | `Possibility` |
| 交流 | MERGE | `Communication` |
| 等待 | KEEP/REVIEW | `Waiting`; retain only if useful as future retrieval vocabulary. |
| 孤独 | MERGE | `Loneliness` |
| 侦探小说 | MERGE | `Detective Fiction` |

### Test-only tag

| Old tag | Action | Canonical tag / note |
|---|---|---|
| FirstPost | RETIRE | Hidden test post metadata; no durable retrieval value. |

## Controlled naming conventions

1. Prefer established English proper names and technical terms for canonical tags (`Final Fantasy`, `RAG`, `SQL`, `Terror Management Theory`). This keeps mixed-language synonyms from multiplying.
2. Preserve acronyms where they are the normal public name (`SQL`, `RAG`, `HTTP`, `DNS`, `CPU`, `VoIP`).
3. Normalize acronym case (`DDOS` → `DDoS`).
4. Do not duplicate acronym + expansion as separate tags unless both are independently useful search terms.
5. A Series name carries the durable broad subject, so broad subject tags such as `计算机网络` and `计算机组成原理` should normally disappear from individual posts.
6. Specific concepts survive even when they occur once. Frequency alone is not a deletion criterion.
7. Do not add speculative tags from titles. Body review in Steps 4–7 decides final per-post tags.

## Series candidates for migration

- `Database Systems` — current DBMS sequence.
- `Computer Architecture` — current 计组 sequence.
- `Computer Networks` — current 计网 sequence.
- `LLM Systems` — candidate, but only one current explicit LLM-note article is visible; use only if body-level review supports a durable thread.

`Python` is not yet a Series by default because the current inventory contains one explicit Python note. `Interview Notes`, `Software Releases`, `Game Records`, `Memory Fragments`, and `Thought Chains` are not Series under the approved definition.

## Uncertain cases reserved for body-level migration

- Hidden `Zodiac` test post: whether it should receive normal Type/Topic metadata or remain excluded/hidden while still schema-valid.
- `地下墓穴` on “最后的纳尔马斯克人”: likely presentation/hidden-site semantics; preserve until template dependency is understood.
- `神圣而可怖的空气`: may be a named entity/translation tied to `Z.A.T.O.` rather than a reusable analytical tag.
- `SKILL`: canonicalize to `Agent Skills` only if the article is specifically about the agent skill/SKILL.md mechanism.
- `IPv4/IPv6`: split only if both protocols are materially discussed.
- Thoughts tags `Waiting` and similarly abstract one-offs: keep only when they provide plausible future retrieval value; Fragments may validly have zero tags.

No post body or post front matter was modified in Step 2.