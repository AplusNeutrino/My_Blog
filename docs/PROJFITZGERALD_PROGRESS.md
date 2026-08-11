# Project Fitzgerald / FitzSight 进度真源

> 本文件是 `/projfitzgerald` 项目追踪页的唯一数据源。页面会直接读取下方 `TRACKER_DATA` JSON。后续让 AI 更新进度时，只修改本文件；不要直接在网页文件中复制或维护任务状态。
>
> **实现仓库：** `https://github.com/AplusNeutrino/FitzSight`  
> **进度真源仓库：** `https://github.com/AplusNeutrino/My_Blog/blob/main/docs/PROJFITZGERALD_PROGRESS.md`

## AI 更新规则

1. 只在有代码、文件、测试、截图、校验结果或提交记录等证据时，将任务设为 `done`；仅在主计划中出现不等于已完成。
2. 已开始但未满足 Definition of Done 的任务设为 `in_progress`，否则保持 `todo`；明确延期的任务设为 `blocked`。
3. 更新任务时同步维护 `updated`、`evidence`、顶部 `lastUpdated`、`summary` 和文末更新日志。
4. 新任务必须保留唯一 `id`，并归入现有阶段；范围或工作流变更需同时记录到 `decisions`。
5. 所有核心功能必须满足：可运行、尽量有确定性测试、处理失败状态、输出可见、证据已记录、文档已更新、无 secrets、可从干净环境演示。
6. **正式产品名固定为 `FitzSight`。** `FinSight` 仅视为项目早期历史命名。后续维护的代码、README、Master Plan、Release Notes、包元数据、UI、PPT、演示文案和新生成文件均必须使用 `FitzSight`；发现仍在使用 `FinSight` 的维护中内容时，应在最近一次交付中统一修正。历史 Git commit 信息不要求重写。
7. **每次 AI 向用户交付新的 FitzSight 代码/文件包时，必须把当次更新后的 `PROJFITZGERALD_PROGRESS.md` 一并放进同一个 ZIP 交付包。** 进度文件应反映该交付包实际包含并验证过的状态，不能提前把未实现功能标为完成。用户收到 ZIP 后自行将代码内容部署到 `AplusNeutrino/FitzSight`，并将 `PROJFITZGERALD_PROGRESS.md` 部署到 `AplusNeutrino/My_Blog/docs/PROJFITZGERALD_PROGRESS.md`。
8. 每次开始新的实现工作前，优先读取 `My_Blog/docs/PROJFITZGERALD_PROGRESS.md` 判断当前任务，再读取 `AplusNeutrino/FitzSight` 的当前 `main` 分支作为代码基线；如果两者不一致，以可验证代码/测试/提交证据校正进度真源。
9. 每个交付包应保留清晰版本号、Release Notes（如适用）、测试结果和关键验证证据；若当次无法实际运行某项测试，应明确记录“未验证”，不能视为通过。

<!-- TRACKER_DATA_START -->
```json{
  "project": {
    "name": "Project Fitzgerald / FitzSight",
    "subtitle": "Financial Operations Intelligence Agent",
    "track": "GOAI 2026 · Boundless Agents · AI+金融",
    "northStar": "让金融业务管理者提出‘为什么这个指标变了？’，由 Agent 自主完成数据调查、统计验证与证据化解释。",
    "phase": "FitzSight v0.2.0 deterministic Tool Layer implemented / deployment and DuckDB runtime validation pending",
    "priority": "P0",
    "lastUpdated": "2026-08-11",
    "sourceVersion": "FitzSight v0.2.0 delivery · based on AplusNeutrino/FitzSight main 6a3d774"
  },
  "summary": {
    "verifiedDone": 28,
    "inProgress": 2,
    "todo": 31,
    "blocked": 0,
    "note": "FitzSight v0.2.0 deterministic Tool Layer has been implemented and validated in the build environment: 17 passed, 1 skipped, compileall PASS, deterministic benchmark investigation recovered -7.53pp affected FTD change and +29.15min median response shift with 6 evidence records. The sole skipped test is DuckDB-specific because the build environment lacks the dependency; T3 remains in_progress until deployment validation."
  },
  "milestones": [
    {
      "id": "M0",
      "title": "定义、设计与仓库基线",
      "date": "2026-08-11",
      "status": "done",
      "goal": "冻结项目定位、范围、架构与命名，并建立可持续读取的公开实现仓库",
      "items": [
        {
          "id": "M0-01",
          "title": "项目定位与赛道选择",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "MASTER_PLAN.md §1.1–1.3、D-001、D-002"
        },
        {
          "id": "M0-02",
          "title": "Problem Statement",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "MASTER_PLAN.md §6"
        },
        {
          "id": "M0-03",
          "title": "MVP Scope 与不做清单",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "MASTER_PLAN.md §7、§40、§43"
        },
        {
          "id": "M0-04",
          "title": "核心 Demo Scenario",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "MASTER_PLAN.md §25、D-007"
        },
        {
          "id": "M0-05",
          "title": "逻辑架构草案",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "MASTER_PLAN.md §9–11"
        },
        {
          "id": "M0-06",
          "title": "核心数据表设计",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "MASTER_PLAN.md §12.3；FitzSight/docs/DATA_DICTIONARY.md"
        },
        {
          "id": "M0-07",
          "title": "初赛 PPT 大纲",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "MASTER_PLAN.md §33"
        },
        {
          "id": "M0-08",
          "title": "安全、合规与开源边界",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "MASTER_PLAN.md §20–22、§46；FitzSight README Safety"
        },
        {
          "id": "M0-09",
          "title": "创建 FitzSight GitHub repo",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "公开仓库 AplusNeutrino/FitzSight，默认分支 main"
        },
        {
          "id": "M0-10",
          "title": "上传 MASTER_PLAN.md",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "AplusNeutrino/FitzSight@6a3d774 包含 MASTER_PLAN.md"
        },
        {
          "id": "M0-11",
          "title": "建立最小项目目录并发布 v0.1.0",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "初始提交 6a3d774：Initial FitzSight v0.1.0 release；用户确认 SHA-256 全部通过"
        },
        {
          "id": "M0-12",
          "title": "全仓库统一正式命名为 FitzSight",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.2 delivery: implementation snapshot contains no legacy product-name references; package moved to src/fitzsight; pyproject project name=fitzsight; MASTER_PLAN/README/docs normalized to FitzSight"
        }
      ]
    },
    {
      "id": "M1",
      "title": "数据与基线",
      "date": "2026-08-12",
      "status": "done",
      "goal": "生成可复现的合成金融经营数据，并在 Agent 之前找回 Ground Truth",
      "items": [
        {
          "id": "A1",
          "title": "定义 schema",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "src/finsight/data/generator.py；docs/DATA_DICTIONARY.md"
        },
        {
          "id": "A2",
          "title": "Synthetic data generator v0",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "src/finsight/data/generator.py；固定 seed 20260811；deterministic test 已通过"
        },
        {
          "id": "A3",
          "title": "生成 customers / salespeople / sales_activity / deposits / withdrawals / trades / business_events",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "generator.py + scripts/generate_data.py；v0.1.0 测试通过"
        },
        {
          "id": "A4",
          "title": "注入 CRM Routing Change",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "src/finsight/data/scenarios.py + generator.py；场景日期 2026-07-15，Europe Team A/B"
        },
        {
          "id": "A5",
          "title": "SQL baseline analysis",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.2 deterministic investigation executes SQL through ReadOnlySQLTool on the SQLite fallback in build environment and recovers the benchmark; preferred DuckDB runtime validation is tracked separately as T3"
        },
        {
          "id": "A6",
          "title": "验证 root cause / Ground Truth 可恢复",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "docs/BASELINE_RESULTS.md：affected FTD 23.37%→15.84%（-7.53pp），response median 94.3→123.45min，p=0.00235；control -1.21pp，p=0.53327"
        },
        {
          "id": "A7",
          "title": "Ground truth 定义与 data dictionary",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "src/finsight/data/scenarios.py；docs/DATA_DICTIONARY.md；_gt 字段被明确限定为 evaluation-only"
        }
      ]
    },
    {
      "id": "M2",
      "title": "工具与分析层",
      "date": "2026-08-13",
      "status": "in_progress",
      "goal": "建立真实、只读、可记录证据的分析工具，并形成 deterministic investigation engine",
      "items": [
        {
          "id": "B1",
          "title": "KPI definitions / helpers",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "src/finsight/analytics/kpis.py：FTD conversion、deposits、withdrawals、net deposits、trading volume"
        },
        {
          "id": "B2",
          "title": "Period comparison",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "src/fitzsight/tools/comparison.py + tests/test_kpi_tools.py; evidence-linked generic PeriodComparisonTool verified"
        },
        {
          "id": "B3",
          "title": "Contribution analysis",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "B4",
          "title": "Statistical tests",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "src/fitzsight/tools/statistics.py: two-proportion z/chi-square + 95% diff CI, Mann–Whitney U, Welch t; automated tests pass"
        },
        {
          "id": "B5",
          "title": "Anomaly detection",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "B6",
          "title": "Customer segmentation",
          "status": "todo",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "D1",
          "title": "Evidence ID 与 registry",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "src/fitzsight/evidence/registry.py + v0.2 Tool integration: sequential Evidence IDs, parameters, result digest, status, payload, lookup"
        },
        {
          "id": "D2",
          "title": "Tool logs",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.2 tool executions are recorded in EvidenceRegistry; SQL execution also records failed calls before raising"
        },
        {
          "id": "T1",
          "title": "Schema / read-only SQL / KPI / comparison / statistics tools",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "Schema Inspector, read-only SQL, KPI, period comparison and statistics Tool interfaces implemented and integration-tested on SQLite fallback; DuckDB-specific runtime validation separated into T3"
        },
        {
          "id": "T2",
          "title": "Unit tests",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "Build-environment pytest: 17 passed, 1 skipped; skipped item is DuckDB backend integration only. compileall PASS. See docs/V0.2_VALIDATION.md"
        },
        {
          "id": "T3",
          "title": "DuckDB backend runtime integration validation",
          "status": "in_progress",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "DuckDB backend code is implemented in src/fitzsight/data/store.py, but the build environment lacks the duckdb package and cannot install it; automated DuckDB integration test therefore skipped. User should run pip install -e \".[dev]\", pytest -q, and scripts/investigate.py --backend duckdb after deployment."
        }
      ]
    },
    {
      "id": "M3",
      "title": "Agent MVP",
      "date": "2026-08-14",
      "status": "todo",
      "goal": "跑通问题 → 调查 → 验证 → 证据化报告的最小闭环",
      "items": [
        {
          "id": "C1",
          "title": "Intent understanding",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "C2",
          "title": "Investigation plan",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "C3",
          "title": "Tool selection 与调用",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "C4",
          "title": "Investigation loop 与 anomaly drilldown",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "C5",
          "title": "Verifier",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "C6",
          "title": "Final auditable report",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "D3",
          "title": "Claim-to-evidence mapping",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        }
      ]
    },
    {
      "id": "M4",
      "title": "演示与初赛材料",
      "date": "2026-08-15 → 2026-08-16",
      "status": "in_progress",
      "goal": "完成可演示 UI、PPT 与初赛提交",
      "items": [
        {
          "id": "E1",
          "title": "Streamlit chat / question input",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "E2",
          "title": "KPI cards",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "E3",
          "title": "Investigation trace",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "E4",
          "title": "Charts",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "E5",
          "title": "Evidence cards 与 report",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "G1",
          "title": "Project summary",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "G2",
          "title": "PPT / PDF",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "G3",
          "title": "Architecture documentation",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "docs/ARCHITECTURE.md + docs/TOOL_LAYER.md + MASTER_PLAN architecture sections"
        },
        {
          "id": "G4",
          "title": "Demo recording",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "G5",
          "title": "README（含 limitations）",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "README.md updated for FitzSight v0.2 with Quick Start, evidence architecture, SQL safety, Safety/Compliance and explicit Limitations"
        },
        {
          "id": "G6",
          "title": "提交、截图、邮件确认与备份 PDF",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "G7",
          "title": "Secrets、license、repo visibility 检查",
          "status": "in_progress",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "repo 已验证 public；.gitignore 与 .env.example 已存在；license 仍待最终确认"
        }
      ]
    },
    {
      "id": "M5",
      "title": "评审等待期强化",
      "date": "2026-08-17 → 2026-08-24",
      "status": "todo",
      "goal": "从一个可运行 Demo 扩展为可评估、可复现系统",
      "items": [
        {
          "id": "F1",
          "title": "5 synthetic scenarios 与 benchmark schema",
          "status": "todo",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "F2",
          "title": "Root cause scoring",
          "status": "todo",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "F3",
          "title": "Evidence coverage scoring",
          "status": "todo",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "F4",
          "title": "Hallucination / overclaim scoring",
          "status": "todo",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "F5",
          "title": "Latency / cost measurement",
          "status": "todo",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "F6",
          "title": "Test suite 与 evaluation harness",
          "status": "todo",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "F7",
          "title": "UI、视频与部署脚本优化",
          "status": "todo",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": ""
        }
      ]
    },
    {
      "id": "M6",
      "title": "复赛与决赛准备",
      "date": "2026-08-25 → 2026-09-22",
      "status": "todo",
      "goal": "陌生评委可一键运行；现场 Demo 稳定并有双重备份",
      "items": [
        {
          "id": "R1",
          "title": "One-command startup 与 .env.example",
          "status": "todo",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": ".env.example 已存在，但 one-command startup 尚未完成"
        },
        {
          "id": "R2",
          "title": "Benchmark results 与完整 compliance explanation",
          "status": "todo",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": "已有首个 baseline result，但尚未达到多场景 benchmark / 完整 compliance DoD"
        },
        {
          "id": "R3",
          "title": "Live / local / video 三套 Demo",
          "status": "todo",
          "priority": "P2",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "R4",
          "title": "5–8 分钟路演与 <3 分钟演示",
          "status": "todo",
          "priority": "P2",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "R5",
          "title": "Q&A、稳定性与 business story",
          "status": "todo",
          "priority": "P2",
          "updated": "2026-08-11",
          "evidence": ""
        }
      ]
    }
  ],
  "risks": [
    {
      "id": "RK-01",
      "level": "high",
      "title": "时间极紧",
      "mitigation": "只做最小可信闭环，P0 优先"
    },
    {
      "id": "RK-02",
      "level": "high",
      "title": "Demo 能跑但证据不足",
      "mitigation": "所有 numeric claims 绑定 tool evidence"
    },
    {
      "id": "RK-03",
      "level": "high",
      "title": "数据与职业合规",
      "mitigation": "只用 synthetic data；禁止真实 PII 与雇主信息"
    },
    {
      "id": "RK-04",
      "level": "medium",
      "title": "范围膨胀",
      "mitigation": "按 MASTER_PLAN §43 五问过滤新功能"
    },
    {
      "id": "RK-05",
      "level": "medium",
      "title": "官方规则更新",
      "mitigation": "每日检查官网、官方群与邮件"
    },
    {
      "id": "RK-06",
      "level": "medium",
      "title": "现场 Demo 失败",
      "mitigation": "Live、local、video 三套预案"
    },
    {
      "id": "RK-07",
      "level": "low",
      "title": "命名回归",
      "mitigation": "正式产品名固定为 FitzSight；每次交付前 grep 检查维护中内容是否出现旧命名"
    },
    {
      "id": "RK-08",
      "level": "medium",
      "title": "代码包与进度真源不同步",
      "mitigation": "每次向用户交付代码包时，必须在同一个 ZIP 中附带当次更新后的 PROJFITZGERALD_PROGRESS.md"
    }
  ],
  "unknowns": [
    "团队人数最终限制",
    "初赛 PPT 页数/大小限制",
    "项目简介字符限制",
    "是否必须 public repo",
    "Demo 视频长度",
    "决赛路演与答辩时长",
    "交通住宿报销标准",
    "官方评委名单",
    "Boundless handbook",
    "指定技术/模型合作资源"
  ],
  "decisions": [
    "D-001 选择 Boundless Agents",
    "D-002 选择 AI+金融",
    "D-003 不做股票投资 Agent",
    "D-004 Synthetic Data First",
    "D-005 Evidence First",
    "D-006 Agent 数量服从任务",
    "D-007 MVP 聚焦 Anomaly Investigation",
    "D-008 正式产品名固定为 FitzSight；FinSight 仅视为早期历史命名，维护中的代码、文档、PPT、包描述与 UI 均应统一为 FitzSight",
    "D-009 每次 AI 向用户交付新的 FitzSight 代码/文件包时，必须把当次已同步更新的 PROJFITZGERALD_PROGRESS.md 一并放入同一个交付 ZIP；用户随后自行将代码与进度真源分别部署到 FitzSight 与 My_Blog"
  ]
}
```
<!-- TRACKER_DATA_END -->

## 状态口径

| 状态 | 含义 |
|---|---|
| `done` | 有明确交付物/验证证据，且达到该任务当前 Definition of Done |
| `in_progress` | 已有实现或证据，但尚未达到完整 Definition of Done |
| `todo` | 尚无开始证据 |
| `blocked` | 已开始但被明确外部条件阻塞 |

## 当前实现基线

- 正式产品名：**FitzSight**
- 实现仓库：`AplusNeutrino/FitzSight`
- 当前 GitHub 基线：`main` at `6a3d774`（用户已部署的 v0.1.0）
- 本次待用户部署交付：**FitzSight v0.2.0**
- v0.2 Build 环境测试：**17 passed, 1 skipped**
- `compileall`：**PASS**
- 唯一 skip：DuckDB backend integration（build 环境无 `duckdb` 包；不视为通过）
- SQLite fallback 端到端调查：**PASS**
- Affected FTD：`23.37% → 15.84%`，`-7.53 pp`
- Europe control：`-1.21 pp`
- Affected median response time：`+29.15 min`
- Conversion p-value：`0.002346`
- Response Mann–Whitney p-value：约 `1.86e-17`
- Root-cause status：`supported_candidate`
- Evidence records：`6`
- Evidence-linked claims：`4`

## 当前下一动作

用户部署 v0.2 后优先执行：

```bash
pip install -e ".[dev]"
pytest -q
python scripts/investigate.py --backend duckdb
```

若 DuckDB test 不再 skip 且 investigation 正常恢复 benchmark，则把 `T3` 从 `in_progress` 更新为 `done`。随后进入剩余 pre-Agent 能力：Contribution Analysis、Anomaly Detection，并准备 LLM Planner/Orchestrator。

## 固定交付包规则

后续每次交付必须采用同包同步：

```text
FitzSight_vX.Y.Z_delivery.zip
├── FitzSight/
│   └── 当次完整实现快照
└── PROJFITZGERALD_PROGRESS.md
```

用户自行拆分部署：

- `FitzSight/...` → `AplusNeutrino/FitzSight`
- `PROJFITZGERALD_PROGRESS.md` → `AplusNeutrino/My_Blog/docs/PROJFITZGERALD_PROGRESS.md`

## 更新日志

- 2026-08-11：依据 Master Plan 建立初始追踪基线。
- 2026-08-11：核验 `AplusNeutrino/FitzSight` v0.1.0 初始提交 `6a3d774`；用户确认 SHA-256 全通过、`pytest` 为 `5 passed`。
- 2026-08-11：正式产品命名固定为 **FitzSight**；建立“代码交付包必须同步附带进度真源”规则。
- 2026-08-11：完成 FitzSight v0.2.0 本地交付快照：正式命名清理、AnalyticsStore、Schema Inspector、Read-only SQL、KPI、Period Comparison、Statistics、Evidence 全链路、deterministic investigation、claim-to-evidence mapping、architecture/limitations 文档。
- 2026-08-11：v0.2 build validation：`17 passed, 1 skipped`、`compileall PASS`；SQLite fallback 端到端调查恢复 benchmark。DuckDB runtime 因 build 环境缺依赖保持 `T3 in_progress`，等待用户部署验证。
