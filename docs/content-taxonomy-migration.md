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
| 24 | 2025-09-13-最后的纳尔马斯克.md | 地下墓穴; FFXIV | FFXIV | essay | otaku | — | Final Fantasy XIV; Fan Fiction; Garlean Empire; Nhalmasque | confident | Step 6 body fully read; classification decided; metadata write pending |
| 25 | 2025-09-15-为什么我要跳过FF2.md | 阅览记录; 游戏记录 | 最终幻想 | essay | otaku | — | Final Fantasy II; JRPG; Game Design; Progression Systems | confident | migrated Step 6; full body read; body prose preserved |
| 26 | 2025-09-25-计网-03.md | 学习笔记; 计网笔记 | 计算机网络; 数据链路层 | note | computation | Computer Networks | Data Link Layer; Ethernet; CRC; VLAN | confident | migrated Step 6; full body read; body prose preserved |
| 27 | 2025-10-04-TMT理论.md | 记忆碎片; 思维链条 | TMT; Ernest Becker; Immortality Project | note | humanity | — | Terror Management Theory; Ernest Becker; Immortality Project; Symbolic Immortality | confident | migrated Step 6; full body read; body prose preserved |
| 28 | 2025-10-11-计网-04.md | 学习笔记; 计网笔记 | 计算机网络; 网络层 | note | computation | Computer Networks | IPv4; Routing; CIDR; NAT; ICMP | confident | migrated Step 6; full body read; body prose preserved |
| 29 | 2025-10-15-计网-05.md | 学习笔记; 计网笔记 | 传输层 | note | computation | Computer Networks | TCP; UDP; Congestion Control; Flow Control | confident | migrated Step 6; full body read; body prose preserved |
| 30 | 2025-10-21-计网-06.md | 学习笔记; 计网笔记 | HTTP; FTP; DNS; DHCP | note | computation | Computer Networks | HTTP; FTP; DNS; DHCP | confident | migrated Step 6; full body re-read before write; body prose preserved |
| 31 | 2025-11-05-计网-07.md | 学习笔记; 计网笔记 | 网络安全; IPS; 防火墙; DDOS | note | computation | Computer Networks | Network Security; Cryptography; Firewall; IDS/IPS; DDoS | confident | Step 6 body fully read; classification decided; metadata write pending |
| 32 | 2025-11-25-计网-08.md | 学习笔记; 计网笔记 | WPAN; GSM; 3G三大标准 | note | computation | Computer Networks | Wi-Fi; CSMA/CA; WPAN; Mobile Networks | confident | Step 6 body fully read in ranges; classification decided; metadata write pending |
| 33 | 2025-11-29-计网-09.md | 学习笔记; 计网笔记 | VoIP; IP 电话网关; H.323; SIP; SDP; QoS 指标 | note | computation | Computer Networks | VoIP; RTP/RTCP; SIP; QoS | confident | Step 6 body fully read in ranges; classification decided; metadata write pending |
| 34 | 2025-12-14-计网-10.md | pending | pending | — | — | — | — | — | pending later batch |
| 35 | 2025-12-17-NoSQL项目面经.md | pending | pending | — | — | — | — | — | pending later batch |
| 36 | 2025-12-19-ROSSMANN项目.md | pending | pending | — | — | — | — | — | pending later batch |
| 37 | 2026-02-12-不完备性.md | pending | pending | — | — | — | — | — | pending later batch |
| 38 | 2026-05-24-neutriverse-site-changelog.md | pending | pending | — | — | — | — | — | pending later batch |
| 39 | 2026-06-15-超过五千亿吨空气的重压之下.md | pending | pending | — | — | — | — | — | pending later batch |
| 40 | 2026-06-30-阿卡夏便笺akashanotes.md | pending | pending | — | — | — | — | — | pending later batch |
| 41 | 2026-07-06-于因特网标签们展开双翼.md | pending | pending | — | — | — | — | — | — | pending later batch |
| 42 | 2026-07-09-丰聪耳机toyosatomimisheadphone.md | pending | pending | — | — | — | — | — | — | pending later batch |
| 43 | 2026-08-07-学习笔记-progressive-disclosure和skill.md | pending | pending | — | — | — | — | — | — | pending later batch |
| 44 | 2026-08-17-哥德尔编码和-rag-embedding-之间的关系.md | pending | pending | — | — | — | — | — | — | pending later batch |

## Fragment inventory

| Date | Existing tags | Status |
|---|---|---|
| 2024-09-12 | 目标, 可能性 | pending Step 7 |
| 2024-10-30 | 交流 | pending Step 7 |
| 2025-03-23 | 等待 | pending Step 7 |
| 2025-11-12 | 孤独 | pending Step 7 |
| 2026-05-02 | 侦探小说 | pending Step 7 |

## Step 4 progress

Batch A is complete. All first-quarter target bodies (#1–#11) were read before classification, and all eleven front matters now contain the approved `type`, `topic`, optional durable `series`, and reduced canonical `tags`. Legacy `categories` remain temporarily for compatibility. No article filename/date/slug/permalink was changed. No intentional article-body prose edit was made.

## Step 5 progress

Batch B (#12–#22) is complete. All eleven article bodies were read before classification and all eleven front matters now contain the approved `type`, `topic`, optional durable `series`, and canonical reduced `tags`. The earlier connected-read truncation for #13 and #20 was resolved with ranged/blob reads before either classification was finalized. No filename/date/slug/permalink was changed and no intentional article-body prose edit was made.

## Step 6 progress

Batch C targets #23–#33. All eleven bodies have been read before classification, using ranged reads where necessary. Metadata is now written for #23 and #25–#30. Remaining writes are #24 and #31–#33. This audit also reconciles earlier stale statuses for #26, #28 and #29 against current GitHub state. Step 6 remains incomplete. No filename/date/slug/permalink was changed and no intentional article-body prose edit was made. No build/runtime PASS is claimed.