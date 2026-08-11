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
```json
{
  "project": {
    "name": "Project Fitzgerald / FitzSight",
    "subtitle": "Financial Operations Intelligence Agent",
    "track": "GOAI 2026 · Boundless Agents · AI+金融",
    "northStar": "让金融业务管理者提出‘为什么这个指标变了？’，由 Agent 自主完成数据调查、统计验证与证据化解释。",
    "phase": "FitzSight v0.1.0 已验证 / v0.2 Tool Layer 准备阶段",
    "priority": "P0",
    "lastUpdated": "2026-08-11",
    "sourceVersion": "FitzSight v0.1.0 · commit 6a3d774 · Master Plan 2026-08-11"
  },
  "summary": {
    "verifiedDone": 18,
    "inProgress": 9,
    "todo": 33,
    "blocked": 0,
    "note": "已核验 FitzSight 公开实现仓库 AplusNeutrino/FitzSight 与初始提交 6a3d774。v0.1.0 已部署至 main；用户确认 SHA-256 校验全部通过且 pytest 为 5 passed。当前已完成 Synthetic Data、CRM Routing Change 注入、Python baseline、基础 KPI 与测试；DuckDB/SQL Tool Layer、通用统计工具、Evidence 全链路集成与 Agent 尚未完成。"
  },
  "milestones": [
    {
      "id": "M0",
      "title": "定义、设计与仓库基线",
      "date": "2026-08-11",
      "status": "in_progress",
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
          "status": "in_progress",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "正式命名已确认；当前 v0.1.0 中 README/MASTER_PLAN/包描述仍存在 FinSight 文本，需在下一交付包完成全仓库命名清理"
        }
      ]
    },
    {
      "id": "M1",
      "title": "数据与基线",
      "date": "2026-08-12",
      "status": "in_progress",
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
          "status": "in_progress",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "Python/pandas baseline 已完成并找回 Ground Truth；DuckDB/read-only SQL baseline 尚未实现，计划进入 v0.2"
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
          "status": "in_progress",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "analytics/baseline.py 已有 CRM 场景 pre/post comparison；尚需抽象为通用 Tool"
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
          "status": "in_progress",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "当前 baseline 已实现 conversion chi-square；尚需通用 statistical-test tool、effect size/CI 与错误处理"
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
          "status": "in_progress",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "src/finsight/evidence/registry.py 已有 EvidenceRegistry primitive；尚未接入每次 Tool execution"
        },
        {
          "id": "D2",
          "title": "Tool logs",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": ""
        },
        {
          "id": "T1",
          "title": "Schema / read-only SQL / KPI / comparison / statistics tools",
          "status": "in_progress",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "KPI 与场景 comparison 已有；Schema Inspector、DuckDB SQL Tool、通用 statistics Tool 尚未完成"
        },
        {
          "id": "T2",
          "title": "Unit tests",
          "status": "in_progress",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.1.0 用户验证 pytest：5 passed；v0.2 Tool Layer 的新增测试尚未实现"
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
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "MASTER_PLAN 含逻辑架构，但独立工程架构文档尚未形成"
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
          "status": "in_progress",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "FitzSight/README.md 已存在并含 Safety/设计原则；尚需统一 FitzSight 命名并增加明确 Limitations 段"
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
      "level": "medium",
      "title": "项目命名漂移",
      "mitigation": "正式产品名固定为 FitzSight；后续交付执行全仓库文本与文档命名检查"
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
| `done` | 有明确交付物/验证证据，且已达到该任务当前 Definition of Done |
| `in_progress` | 已有实现或证据，但尚未达到完整 Definition of Done |
| `todo` | 尚无开始证据 |
| `blocked` | 已开始但被明确外部条件阻塞 |

## 当前实现基线

- 正式产品名：**FitzSight**
- 实现仓库：`AplusNeutrino/FitzSight`
- 分支：`main`
- 已验证版本：`v0.1.0`
- 初始提交：`6a3d774`（完整 SHA：`6a3d7742afb740e4e8e421f4603907798f2d2db9`）
- 初始提交信息：`Initial FitzSight v0.1.0 release`
- 用户侧文件 SHA-256 校验：**全部通过**
- 用户侧测试：**5 passed**
- 当前 Ground Truth baseline：
  - Affected Europe Team A+B FTD：`23.37% → 15.84%`
  - 变化：`-7.53 pp`
  - Median response time：`94.3 → 123.45 min`
  - Conversion test：`p = 0.00235`
  - Europe control：`-1.21 pp`，`p = 0.53327`
- 当前结论：Synthetic Ground Truth 已可在无 Agent 条件下通过 Python baseline 恢复；下一阶段重点是 DuckDB/read-only SQL + Tool Layer + Evidence integration。

## 下一开发切片：FitzSight v0.2

按 P0 顺序：

1. 全仓库正式命名统一：`FinSight → FitzSight`（历史 Git commit 不重写）。
2. DuckDB data layer。
3. Schema Inspector。
4. Read-only SQL Tool（仅允许 SELECT / safe query path）。
5. 通用 KPI Tool。
6. Period Comparison Tool。
7. Statistical Test Tool。
8. Evidence-wrapped Tool Execution / Tool Logs。
9. Deterministic Investigation Engine。
10. 新增对应测试并保持 clean-start 可运行。
11. **仍然不接 LLM，直到 deterministic investigation 稳定。**

### v0.2 目标验收

```bash
python scripts/investigate.py --question "Why did European FTD conversion deteriorate after July 15?"
```

应在**不依赖 LLM 做算术或捏造结论**的情况下输出：

- structured investigation plan/result；
- tool execution trace；
- evidence IDs；
- SQL/data references；
- statistical result；
- affected vs control comparison；
- supported/unsupported claim boundary。

## 交付包规则

后续每一次交付 ZIP 推荐结构：

```text
FitzSight_vX.Y.Z_delivery.zip
├── FitzSight/                       # 当次完整代码/文档快照
│   ├── README.md
│   ├── MASTER_PLAN.md
│   ├── ...
│   └── RELEASE_NOTES_vX.Y.Z.md
└── PROJFITZGERALD_PROGRESS.md       # 当次同步更新后的进度真源
```

用户负责拆分并部署：

```text
FitzSight/...
→ github.com/AplusNeutrino/FitzSight

PROJFITZGERALD_PROGRESS.md
→ github.com/AplusNeutrino/My_Blog/docs/PROJFITZGERALD_PROGRESS.md
```

## 更新日志

- 2026-08-11：依据 Master Plan 建立初始追踪基线；规划产物 8 项完成，工程与提交任务保持未完成。
- 2026-08-11：核验 `AplusNeutrino/FitzSight` 已创建并部署 v0.1.0 至 `main`；初始提交 `6a3d774`；用户确认 SHA-256 全通过、`pytest` 为 `5 passed`。
- 2026-08-11：将仓库创建、Master Plan 上传、最小目录、Synthetic Data、CRM Routing Change、Ground Truth baseline、KPI helpers 等有证据任务同步为 `done/in_progress`；进度汇总更新为 `18 done / 9 in_progress / 33 todo / 0 blocked`。
- 2026-08-11：正式产品命名固定为 **FitzSight**；新增全仓库命名清理任务 `M0-12`。
- 2026-08-11：新增长期交付规则：**每次 AI 交付新的 FitzSight 文件包时，必须在同一 ZIP 内附上当次更新后的 `PROJFITZGERALD_PROGRESS.md`，由用户自行分别部署到两个仓库。**
