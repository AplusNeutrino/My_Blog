# Neutriverse Content Taxonomy Migration Audit

> Created: 2026-09-29  
> Scope: 44 `_posts/*.md` plus 5 fragments in `_tabs/thoughts.md` (49 writing items).  
> Rule: front matter / taxonomy only; article bodies are out of scope. Filenames, dates, slugs and permalinks remain unchanged.

## Baseline

Posts use YAML front matter with legacy `categories` and `tags`; new semantic fields are `type`, `topic`, optional `series`, and canonical `tags`. Legacy categories remain temporarily for compatibility. Thoughts are YAML objects under `fragments:` in `_tabs/thoughts.md` and are rendered by `_layouts/thoughts.html`.

## Article migration table

| # | Article | Old Category | Old Tags | New Type | New Topic | New Series | New Tags | Confidence | Status / Notes |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | 2024-10-07-TestInfo.md | 记忆碎片 | FirstPost | note | computation | — | Site Styling; Markdown | confident | migrated Step 4; body read; body prose preserved |
| 2 | 2024-10-08-DBMS-01.md | 学习笔记; DBMS笔记 | DBMS; E-R模型 | note | computation | Database Systems | E-R Model; Data Models; Data Independence | confident | migrated Step 4; body read; body prose preserved |
| 3 | 2024-10-09-DBMS-02.md | 学习笔记; DBMS笔记 | DBMS; 关系数据库; 三类约束; 三大范式 | note | computation | Database Systems | Relational Databases; Integrity Constraints; Normalization | confident | migrated Step 4; body read; body prose preserved |
| 4 | 2024-10-12-DBMS-03.md | 学习笔记; DBMS笔记 | DBMS; 关系代数运算 | note | computation | Database Systems | Relational Algebra; SQL | confident | migrated Step 4; body read; body prose preserved |
| 5 | 2024-10-14-DBMS-04.md | 学习笔记; DBMS笔记 | DBMS; SQL | note | computation | Database Systems | SQL; Views; Integrity Constraints | confident | migrated Step 4; body read; body prose preserved |
| 6 | 2024-10-15-DBMS-05.md | 学习笔记; DBMS笔记 | DBMS; 关系查询 | note | computation | Database Systems | Query Optimization; Query Processing; Join Algorithms | confident | migrated Step 4; body read; body prose preserved |
| 7 | 2024-10-22-DBMS-06.md | 学习笔记; DBMS笔记 | DBMS; 数据库安全性; 存取控制 | note | computation | Database Systems | Database Security; Access Control; DAC; MAC | confident | migrated Step 4; body read; body prose preserved |
| 8 | 2024-10-29-DBMS-07.md | 学习笔记; DBMS笔记 | DBMS; 数据库完整性 | note | computation | Database Systems | Integrity Constraints; Triggers | confident | migrated Step 4; body read; body prose preserved |
| 9 | 2024-10-30-PythonIntro.md | 学习笔记; Python笔记 | Python | note | computation | — | Python | confident | migrated Step 4; body read; body prose preserved |
| 10 | 2024-11-05-DBMS-08.md | 学习笔记; DBMS笔记 | DBMS; 数据库恢复 | note | computation | Database Systems | Database Recovery; Write-Ahead Logging; UNDO; REDO | confident | migrated Step 4; body read; body prose preserved |
| 11 | 2024-11-12-DBMS-09.md | 学习笔记; DBMS笔记 | DBMS; 并发控制; ACID特性; 封锁机制 | note | computation | Database Systems | Concurrency Control; ACID; Locking; Two-Phase Locking | confident | migrated Step 4; body read; body prose preserved |
| 12 | 2024-11-19-DBMS-10.md | 学习笔记; DBMS笔记 | DBMS; 函数依赖分析; 范式规范 | note | computation | Database Systems | Functional Dependencies; Normalization; Database Design | confident | migrated Step 5; body read; body prose preserved |
| 13 | 2025-02-26-计组-01.md | 学习笔记; 计组笔记 | 计算机组成原理; 计算机系统 | note | computation | Computer Architecture | Computer Systems; CPU Performance; Von Neumann Architecture | confident | migrated Step 5; complete body read in line ranges; body prose preserved |
| 14 | 2025-03-12-计组-02.md | 学习笔记; 计组笔记 | 计算机组成原理; 计算机数据 | note | computation | Computer Architecture | Data Representation; Two's Complement; IEEE 754; ALU | confident | migrated Step 5; body read; body prose preserved |
| 15 | 2025-03-27-计组-03.md | 学习笔记; 计组笔记 | 计算机组成原理; 存储器; RAM | note | computation | Computer Architecture | Memory Hierarchy; Cache; SRAM; DRAM | confident | migrated Step 5; body read; body prose preserved |
| 16 | 2025-04-16-计组-04.md | 学习笔记; 计组笔记 | 计算机组成原理; 指令; 寻址 | note | computation | Computer Architecture | Instruction Set Architecture; Addressing Modes; RISC; CISC | confident | migrated Step 5; body read; body prose preserved |
| 17 | 2025-04-25-计组-05.md | 学习笔记; 计组笔记 | 计算机组成原理; CPU | note | computation | Computer Architecture | CPU; Pipelining; Control Unit | confident | migrated Step 5; body read; body prose preserved |
| 18 | 2025-05-07-计组-06.md | 学习笔记; 计组笔记 | 计算机组成原理; 总线; I/O | note | computation | Computer Architecture | Bus; I/O; DMA; Interrupts | confident | migrated Step 5; body read; body prose preserved |
| 19 | 2025-05-21-计组-07.md | 学习笔记; 计组笔记 | 计算机组成原理; 微机 | note | computation | Computer Architecture | Microcomputer; System Bus; Instruction Cycle | confident | migrated Step 5; body read; body prose preserved |
| 20 | 2025-06-11-计组-08.md | 学习笔记; 计组笔记 | 计算机组成原理; 汇编语言 | note | computation | Computer Architecture | Assembly Language; 8086; Procedures; Stack | confident | migrated Step 5; complete body read via ranged/blob reads; body prose preserved |
| 21 | 2025-08-22-FF1记录.md | 阅览记录; 游戏记录 | 最终幻想 | essay | otaku | — | Final Fantasy; JRPG; Game Design; Narrative Design | confident | migrated Step 5; body read; body prose preserved |
| 22 | 2025-09-02-计网-01.md | 学习笔记; 计网笔记 | 计算机网络 | note | computation | Computer Networks | Network Architecture; TCP/IP; OSI Model; Packet Switching | confident | migrated Step 5; body read; body prose preserved |
| 23 | 2025-09-12-计网-02.md | 学习笔记; 计网笔记 | 计算机网络; 物理层 | note | computation | Computer Networks | Physical Layer; Signal Encoding; Multiplexing; Shannon Capacity | confident | migrated Step 6; full body read; body prose preserved |
| 24 | 2025-09-13-最后的纳尔马斯克.md | 地下墓穴; FFXIV | FFXIV | essay | otaku | — | Final Fantasy XIV; Fan Fiction; Garlean Empire; Nhalmasque | confident | migrated Step 6; full body re-read in ranges before write; body prose preserved |
| 25 | 2025-09-15-为什么我要跳过FF2.md | 阅览记录; 游戏记录 | 最终幻想 | essay | otaku | — | Final Fantasy II; JRPG; Game Design; Progression Systems | confident | migrated Step 6; full body read; body prose preserved |
| 26 | 2025-09-25-计网-03.md | 学习笔记; 计网笔记 | 计算机网络; 数据链路层 | note | computation | Computer Networks | Data Link Layer; Ethernet; CRC; VLAN | confident | migrated Step 6; full body read; body prose preserved |
| 27 | 2025-10-04-TMT理论.md | 记忆碎片; 思维链条 | TMT; Ernest Becker; Immortality Project | note | humanity | — | Terror Management Theory; Ernest Becker; Immortality Project; Symbolic Immortality | confident | migrated Step 6; full body read; body prose preserved |
| 28 | 2025-10-11-计网-04.md | 学习笔记; 计网笔记 | 计算机网络; 网络层 | note | computation | Computer Networks | IPv4; Routing; CIDR; NAT; ICMP | confident | migrated Step 6; full body read; body prose preserved |
| 29 | 2025-10-15-计网-05.md | 学习笔记; 计网笔记 | 传输层 | note | computation | Computer Networks | TCP; UDP; Congestion Control; Flow Control | confident | migrated Step 6; full body read; body prose preserved |
| 30 | 2025-10-21-计网-06.md | 学习笔记; 计网笔记 | HTTP; FTP; DNS; DHCP | note | computation | Computer Networks | HTTP; FTP; DNS; DHCP | confident | migrated Step 6; full body re-read before write; body prose preserved |
| 31 | 2025-11-05-计网-07.md | 学习笔记; 计网笔记 | 网络安全; IPS; 防火墙; DDOS | note | computation | Computer Networks | Network Security; Cryptography; Firewall; IDS/IPS; DDoS | confident | migrated Step 6; full body read; body prose preserved |
| 32 | 2025-11-25-计网-08.md | 学习笔记; 计网笔记 | WPAN; GSM; 3G三大标准 | note | computation | Computer Networks | Wi-Fi; CSMA/CA; WPAN; Mobile Networks | confident | migrated Step 6; full body re-read in ranges before write; body prose preserved |
| 33 | 2025-11-29-计网-09.md | 学习笔记; 计网笔记 | VoIP; IP 电话网关; H.323; SIP; SDP; QoS 指标 | note | computation | Computer Networks | VoIP; RTP/RTCP; SIP; QoS | confident | migrated Step 6; full body read in ranges before write; body prose preserved |
| 34 | 2025-12-14-计网-10.md | 学习笔记; 计网笔记 | IPv4/IPv6; MPLS; P2P | note | computation | Computer Networks | IPv6; MPLS; P2P; BitTorrent | confident | migrated Step 7; full body read; body prose preserved |
| 35 | 2025-12-17-NoSQL项目面经.md | 学习笔记; 面试经验 | NoSQL | note | computation | — | MongoDB; Data Modeling; Denormalization; Indexing | confident | migrated Step 7; full body read; body prose preserved |
| 36 | 2025-12-19-ROSSMANN项目.md | 学习笔记; 面试经验 | XGBoost | note | computation | — | XGBoost; Sales Forecasting; Feature Engineering; RMSPE | confident | migrated Step 7; full body read in ranges; body prose preserved |
| 37 | 2026-02-12-不完备性.md | 记忆碎片; 思维链条 | 不完备性; 康托尔对角线法; 理查德悖论; 哥德尔第一不完备性定理; 哥德尔第二不完备性定理 | note | computation | — | Incompleteness Theorems; Cantor Diagonal Argument; Halting Problem; Gödel Numbering | confident | migrated Step 7; full body read; body prose preserved |
| 38 | 2026-05-24-neutriverse-site-changelog.md | 记忆碎片; 站点维护 | Neutriverse; Changelog; 维护记录 | note | computation | — | Neutriverse; Changelog; Jekyll | confident | migrated Step 7; full body read; body prose preserved |
| 39 | 2026-06-15-超过五千亿吨空气的重压之下.md | 阅览记录; 游戏记录 | 神圣而可怖的空气; Z.A.T.O. | essay | otaku | — | Z.A.T.O.; Social Conformity; Identity; Innocence | confident | migrated Step 7; full body read; body prose preserved |
| 40 | 2026-06-30-阿卡夏便笺akashanotes.md | 记忆碎片; 软件发布 | 桌面便签; Windows; 小工具 | note | computation | — | Akasha Notes; Windows; Desktop Widgets | confident | migrated Step 7; full body read; body prose preserved |
| 41 | 2026-07-06-于因特网标签们展开双翼.md | 记忆碎片; 思维链条 | 社会身份; 情感极化; 外群体敌意 | essay | humanity | — | Social Identity; Affective Polarization; Out-group Animosity; Social Media | confident | migrated Step 7; full body read; body prose preserved |
| 42 | 2026-07-09-丰聪耳机toyosatomimisheadphone.md | 记忆碎片; 软件发布 | 东方Project; 丰聪耳神子; STT | note | computation | — | Toyosatomimi's Headphone; Speech-to-Text; Translation; Windows | confident | migrated Step 7; full body read; body prose preserved |
| 43 | 2026-08-07-学习笔记-progressive-disclosure和skill.md | 学习笔记; LLM笔记 | Progressive Disclosure; SKILL | note | computation | — | Progressive Disclosure; Agent Skills; Context Engineering; Tool Routing | confident | migrated Step 7; full body read in ranges; body prose preserved |
| 44 | 2026-08-17-哥德尔编码和-rag-embedding-之间的关系.md | 记忆碎片; 思维链条 | 哥德尔编码; Embedding; RAG | note | computation | — | Gödel Numbering; Embeddings; RAG; Semantic Search | confident | migrated Step 7; full body read; body prose preserved |

## Fragment inventory

| Date | Existing tags | New Type | New Topic | Canonical Tags | Status |
|---|---|---|---|---|---|
| 2024-09-12 | 目标, 可能性 | fragment | humanity | 目标; 可能性 | migrated Step 7 |
| 2024-10-30 | 交流 | fragment | humanity | 交流 | migrated Step 7 |
| 2025-03-23 | 等待 | fragment | humanity | 等待 | migrated Step 7 |
| 2025-11-12 | 孤独 | fragment | humanity | 孤独 | migrated Step 7 |
| 2026-05-02 | 侦探小说 | fragment | arts | 侦探小说 | migrated Step 7 |

## Step 4 progress

Batch A is complete. All first-quarter target bodies (#1–#11) were read before classification, and all eleven front matters now contain the approved `type`, `topic`, optional durable `series`, and reduced canonical `tags`. Legacy `categories` remain temporarily for compatibility. No article filename/date/slug/permalink was changed. No intentional article-body prose edit was made.

## Step 5 progress

Batch B (#12–#22) is complete. All eleven article bodies were read before classification and all eleven front matters now contain the approved `type`, `topic`, optional durable `series`, and canonical reduced `tags`. The earlier connected-read truncation for #13 and #20 was resolved with ranged/blob reads before either classification was finalized. No filename/date/slug/permalink was changed and no intentional article-body prose edit was made.

## Step 6 progress

Batch C (#23–#33) is complete. All eleven bodies were read before classification, using ranged reads where necessary, and all eleven front matters now contain the approved `type`, `topic`, optional durable `series`, and canonical reduced `tags`. #32 was migrated in commit `4eb84796119ea84d687b889d2250975a2f19b60f`; #33 was migrated in commit `42bb9a4b19048b56ee0741e1a6b3bfa0472609bf`. Current GitHub state was re-read to verify #33 taxonomy metadata before closing the batch. No filename/date/slug/permalink was changed and no intentional article-body prose edit was made. No build/runtime PASS is claimed.

## Step 7 progress

Batch D (#34–#44) and all five current Thoughts fragments are migrated. Every remaining post body was read before classification; the final outstanding article #36 was migrated in commit `0625b2786ae7514af8020c5c1002b31979cc9b5b`. Earlier Step 7 article commits include #34 `5c7f64c920015913ab72313ec5eff48ee2736ec3`, #35 `b18f504a47d5addc0b09b74713571ff16b928ee9`, #37 `90fdb218954ff112101de5c3d6543f6c1b23ed51`, #38 `aea2e51f4a7831ef56fcd4a795d71b88af74adff`, #39 `67c3929249e313ec42868e6b07c9430ecaea4d6e`, #40 `a9782d1e6ba21f5dd85fcc333d2d5652f66c4543`, #41 `3072dd005f4328109d27024c2e8bb832a4089602`, #42 `08a67de623bd7808e87423c1643e38d9b9ad1ab4`, #43 `f76bedcd6aea404744880171c153c3fe69bb4a9c`, and #44 `9f514884237a9a81aa783c86e89d56f9a6c8d427`. Thoughts were aligned in `a4ebf1e15db24046eb79a65a9674bf8ccf26088f`. No filename/date/slug/permalink changed and no intentional article-body prose edit was made. Owner-review items: none identified during classification; final validation remains Step 8. No build/runtime PASS is claimed.