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
10. **Agent 安全边界：** Planner/LLM 输出始终视为不可信输入；只能选择已批准高层 action，不能直接生成或执行 SQL、任意工具参数、高风险金融动作；最终结论必须经过 EvidenceClaimVerifier，验证失败则 fail closed。
11. **External runtime 证据规则：** OpenAI API、Streamlit、DuckDB 或其他 optional/external runtime 只有在实际依赖可用并有运行输出时才可标记 live validation `done`；mock/compile/code presence 只能证明实现或接口测试，不能替代真实运行证据。

<!-- TRACKER_DATA_START -->
```json
{
  "project": {
    "name": "Project Fitzgerald / FitzSight",
    "subtitle": "Financial Operations Intelligence Agent",
    "track": "GOAI 2026 · Boundless Agents · AI+金融",
    "northStar": "让金融业务管理者提出‘为什么这个指标变了？’，由 Agent 自主完成数据调查、统计验证与证据化解释。",
    "phase": "FitzSight v0.5.0 multi-intent Agent implemented / DuckDB runtime validated / OpenAI + Streamlit runtime validations next",
    "priority": "P0",
    "lastUpdated": "2026-08-11",
    "sourceVersion": "FitzSight v0.5.0 delivery · DuckDB deployment runtime validated 2026-08-11"
  },
  "summary": {
    "verifiedDone": 41,
    "inProgress": 9,
    "todo": 15,
    "blocked": 0,
    "note": "FitzSight v0.5.0 multi-intent Agent build remains validated at 40 passed, 1 skipped in the restricted build environment, with compileall PASS and 2/2 deterministic benchmark PASS. The previously skipped DuckDB-specific runtime path has now been explicitly validated in the deployment environment: DuckDB loaded data/generated, both the default constrained planner and JSON-file planner completed successfully, final status was verified, verifier evidence E0012 and final-answer evidence E0013. Therefore T3 is now done. OpenAI live API and Streamlit runtime validation remain in_progress until separate real-runtime evidence is provided."
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
          "evidence": "src/fitzsight/data/generator.py；docs/DATA_DICTIONARY.md"
        },
        {
          "id": "A2",
          "title": "Synthetic data generator v0",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "src/fitzsight/data/generator.py；固定 seed 20260811；deterministic test 已通过"
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
          "evidence": "src/fitzsight/data/scenarios.py + generator.py；场景日期 2026-07-15，Europe Team A/B"
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
          "evidence": "src/fitzsight/data/scenarios.py；docs/DATA_DICTIONARY.md；_gt 字段被明确限定为 evaluation-only"
        },
        {
          "id": "A8",
          "title": "第二 synthetic benchmark：Europe high-value withdrawal cluster / net-deposit shock",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.5 src/fitzsight/data/scenarios.py + generator.py；default seed current Europe net deposits -$82,168.18 vs baseline $141,733.52；net change -$223,901.70；top-11 withdrawal share 92.2%"
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
          "evidence": "src/fitzsight/analytics/kpis.py：FTD conversion、deposits、withdrawals、net deposits、trading volume"
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
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.3 src/fitzsight/tools/contribution.py + tests/test_contribution.py：symmetric binary-rate decomposition；segment contributions reconstruct aggregate FTD-rate change within floating-point precision；default benchmark ranks Team A/B as largest negative contributors"
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
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.3 src/fitzsight/tools/anomaly.py + tests/test_anomaly.py；median/MAD robust baseline integrated into deterministic investigation；default benchmark flags 8 post-change high response-time anomaly days"
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
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "2026-08-11 deployment runtime validation completed with DuckDB using data/generated. Default constrained planner and JSON-file planner both executed successfully; final status=verified; verifier evidence=E0012; final answer evidence=E0013. Runtime evidence reported from deployment environment."
        },
        {
          "id": "T4",
          "title": "OpenAI Responses planner live runtime validation",
          "status": "in_progress",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "provider code 与 fake-client integration tests 已通过；build 环境无用户 API credential / live model access，不能宣称真实联网调用已验证"
        }
      ]
    },
    {
      "id": "M3",
      "title": "Agent MVP",
      "date": "2026-08-14",
      "status": "done",
      "goal": "跑通问题 → 调查 → 验证 → 证据化报告的最小闭环",
      "items": [
        {
          "id": "C1",
          "title": "Intent understanding",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "src/fitzsight/agent/planner.py: ConstrainedRulePlanner + StructuredJSONPlanner; unsupported intent refused before external planner callback; tests/test_agent_planner.py"
        },
        {
          "id": "C2",
          "title": "Investigation plan",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "src/fitzsight/agent/models.py + planner.py: strict AgentPlan / AgentPlanStep schema and approved action sequence; 7 planner tests pass"
        },
        {
          "id": "C3",
          "title": "Tool selection 与调用",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "src/fitzsight/agent/orchestrator.py: planner output validated then routed only to deterministic investigation engine; arbitrary SQL/tool actions rejected"
        },
        {
          "id": "C4",
          "title": "Investigation loop 与 anomaly drilldown",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "FitzSightAgent.run() executes question → plan → deterministic investigation → verifier → final answer; Agent CLI end-to-end SQLite run verified"
        },
        {
          "id": "C5",
          "title": "Verifier",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "src/fitzsight/agent/verifier.py: EvidenceClaimVerifier checks evidence existence/digest/status, _gt boundary and causal overclaim; verifier tests pass"
        },
        {
          "id": "C6",
          "title": "Final auditable report",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "src/fitzsight/agent/renderer.py + AgentRunResult: fail-closed verified final answer containing only verified claim text; end-to-end status verified"
        },
        {
          "id": "D3",
          "title": "Claim-to-evidence mapping",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.4 verifier validates all claim Evidence IDs and digests; end-to-end Agent run verified 6/6 evidence-linked claims with 13 audit evidence records"
        },
        {
          "id": "C7",
          "title": "Multi-intent Agent routing 与第二业务意图",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.5 agent/catalog.py + investigation/net_deposit.py + router.py；两个 intent 均完成 Agent → deterministic tools → verifier 闭环；2/2 benchmark PASS"
        },
        {
          "id": "C8",
          "title": "Concrete OpenAI Responses structured planner adapter",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.5 providers/openai_planner.py；fake Responses client test 验证 json_schema strict、store=False、local scope gate、post-generation plan validation；live API runtime 单独由 T4 跟踪"
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
          "status": "in_progress",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.5 streamlit_app.py 已实现 question input、planner/backend selector 与两条 preset intent；compileall PASS；build 环境未安装 Streamlit，尚无 runtime smoke test"
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
          "status": "in_progress",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.5 Streamlit demo 可展示 Agent plan 与完整 audit_evidence；尚未实现执行中的实时 step-by-step trace"
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
          "status": "in_progress",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.5 UI 展示 verified findings、guardrail、metrics、Evidence/audit JSON；尚未形成最终 Evidence card 视觉组件与正式报告页"
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
      "status": "in_progress",
      "goal": "从一个可运行 Demo 扩展为可评估、可复现系统",
      "items": [
        {
          "id": "F1",
          "title": "5 synthetic scenarios 与 benchmark schema",
          "status": "in_progress",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": "v0.5 evaluation/benchmark_catalog.json 已包含 2 个独立 synthetic scenarios（CRM/FTD + Europe net deposit）；目标仍为 5 scenarios"
        },
        {
          "id": "F2",
          "title": "Root cause scoring",
          "status": "in_progress",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": "v0.5 scripts/run_benchmark.py 对两个 scenario 执行预期方向、verification 与 root_cause_status 检查；尚未形成正式 root-cause accuracy aggregate metric"
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
          "status": "in_progress",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": "v0.5 新增 two-scenario benchmark runner/catalog；build validation 40 passed, 1 skipped；尚未完成 planned 5-scenario evaluation harness"
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
      "status": "in_progress",
      "goal": "陌生评委可一键运行；现场 Demo 稳定并有双重备份",
      "items": [
        {
          "id": "R1",
          "title": "One-command startup 与 .env.example",
          "status": "in_progress",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": ".env.example 已包含 OPENAI_API_KEY/FITZSIGHT_MODEL/FITZSIGHT_DATA_DIR/FITZSIGHT_BACKEND；CLI 与 Streamlit entrypoint 已有，但尚未完成 one-command startup"
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
    },
    {
      "id": "RK-09",
      "level": "medium",
      "title": "External provider/runtime not locally reproducible",
      "mitigation": "OpenAI/Streamlit/DuckDB 分别保留 optional dependency 与 deterministic fallback；无真实 runtime evidence 不标 done"
    },
    {
      "id": "RK-10",
      "level": "medium",
      "title": "Second intent over-interprets customer withdrawal motives",
      "mitigation": "只报告 observed withdrawal concentration/driver；Verifier guardrail 禁止把行为模式升级为客户动机、AML 或投资结论"
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
    "D-009 每次 AI 向用户交付新的 FitzSight 代码/文件包时，必须把当次已同步更新的 PROJFITZGERALD_PROGRESS.md 一并放入同一个交付 ZIP；用户随后自行将代码与进度真源分别部署到 FitzSight 与 My_Blog",
    "D-010 在引入 LLM Planner/Orchestrator 前先完成 deterministic Contribution Analysis 与 Anomaly Detection；LLM 只能编排工具，不负责计算业务数字",
    "D-011 Agent planner output is untrusted：只能选择批准的高层 action，不能生成 SQL、任意 tool arguments 或高风险业务动作；所有计算继续由 deterministic tools 完成",
    "D-012 Deterministic planner fallback 是比赛必备能力；无网络/API 时仍可完成核心 Demo，StructuredJSONPlanner 仅作为 provider-neutral LLM adapter 且必须经过同一 plan validator",
    "D-013 采用 approved-intent expansion 而不是 unrestricted tool autonomy；每个新业务意图都有固定 action contract 与 deterministic executor",
    "D-014 净入金场景区分 observed driver 与 customer motive；可量化 withdrawal pressure/concentration，但不能无证据推断客户为何提款或给出 AML/投资结论",
    "D-015 concrete external provider 首选 OpenAI Responses structured planner；strict JSON schema + store=False，且 local classifier/validator 仍为最终权限边界",
    "D-016 UI 只负责展示 verified outputs/evidence，不重新计算业务指标或绕过 verifier"
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

## 当前实现基线（v0.5）

- 正式产品名：**FitzSight**
- 实现仓库：`AplusNeutrino/FitzSight`
- 已核验公开基线：`v0.4.0` commit `2935ddaa690e29d669607492233b3539ef310152`（`Release FitzSight v0.4.0`）
- 当前实现版本：`v0.5.0`；已提供部署环境 DuckDB runtime 验证证据
- Build tests：分组汇总 `40 passed, 1 skipped`；`41 tests collected`
- Compile validation：`python -m compileall -q src scripts tests streamlit_app.py` → `PASS`
- Build 环境仍记录 DuckDB-specific test skip；但部署环境已完成真实 DuckDB runtime validation，因此 `T3` 已关闭为 `done`
- DuckDB deployment runtime：数据目录 `data/generated`；default constrained planner 与 JSON-file planner 均成功；final status `verified`；verifier evidence `E0012`；final-answer evidence `E0013`
- Two-scenario deterministic benchmark：`2/2 PASS`
- CRM benchmark 保持：Affected FTD `-7.53 pp`；Control `-1.21 pp`；response median `+29.15 min`；verification PASS
- 新 Net Deposit benchmark：baseline `$141,733.52` → current `-$82,168.18`；change `-$223,901.70`；deposit change `+$24,365.52`；withdrawal change `+$248,267.22`；top-11 withdrawal share `92.2%`；verification `5/5 PASS`
- 新 OpenAI provider：Responses API structured planner adapter 已实现；fake-client integration test 验证 strict JSON schema、`store=False` 与 local policy；**live API 未验证**
- 新 Streamlit demo shell：代码与 compile validation 已完成；**runtime smoke test 未验证**

## 下一开发切片：FitzSight v0.6

1. `DuckDB` runtime 已验证并关闭 T3；下一步优先验证 `OpenAI Responses`（若有 API key/model）与 `Streamlit` runtime，只有实际输出才能关闭 T4/E1 等任务。
2. P1 引入 Customer Intelligence / segmentation，但必须作为 deterministic Tool，再决定是否暴露为第三个 Agent intent。
3. 将 benchmark catalog 从 2 scenarios 扩展到至少 3，逐步接近计划中的 5 scenarios。
4. UI 增加真实 business KPI cards、图表与更清晰的 investigation trace；UI 继续只读取 verified result。
5. 开始初赛 Project Summary / PPT/PDF 的正式内容版本，不再只停留在 Master Plan outline。
6. 保留 deterministic fallback，任何 live provider failure 都不得导致核心 Demo 失效。
7. Final license 仍需在提交前完成。

## 更新日志

- 2026-08-11：核验 `AplusNeutrino/FitzSight` 已部署 v0.4.0，main commit `2935ddaa`（`Release FitzSight v0.4.0`）。
- 2026-08-11：完成 FitzSight v0.5.0 multi-intent Agent：新增 `net_deposit_anomaly_investigation` 与 Europe high-value withdrawal-cluster synthetic benchmark。
- 2026-08-11：第二意图 default-seed 结果：net-deposit change `-$223,901.70`；withdrawal change `+$248,267.22`；top-11 withdrawal share `92.2%`；5/5 claims verification PASS。
- 2026-08-11：新增 `MultiIntentInvestigationEngine`、intent/action catalog、OpenAI Responses structured planner adapter、Streamlit demo shell、two-scenario benchmark catalog/runner。
- 2026-08-11：v0.5 build validation 分组汇总 `40 passed, 1 skipped`；`compileall PASS`；two-scenario benchmark `2/2 PASS`。
- 2026-08-11：A8、C7、C8 按代码/测试/运行证据标为 `done`；E1/E3/E5/F1/F2/F6/R1/T4 按已实现但尚未达到完整 DoD 的状态标为 `in_progress`。
- 2026-08-11：新增 External runtime 证据规则：mock/compile/code presence 不得替代 DuckDB/OpenAI/Streamlit 的真实 runtime validation。
- 2026-08-11：新增 D-013–D-016，固定 approved-intent expansion、withdrawal-motive guardrail、OpenAI provider 权限边界及 UI 非分析权威原则。

- 2026-08-11：部署环境完成 DuckDB runtime validation：`data/generated` 成功加载；default constrained planner 与 JSON-file planner 均成功执行；final status `verified`；verifier evidence `E0012`；final-answer evidence `E0013`。据此 `T3` 从 `in_progress` 更新为 `done`。

### 历史摘要

- v0.1.0：Synthetic Data + first CRM Ground Truth baseline；用户验证 `5 passed`。
- v0.2.0：Deterministic Tool Layer；build `17 passed, 1 skipped`。
- v0.3.0：Contribution Analysis + Anomaly Detection；build `19 passed, 1 skipped`。
- v0.4.0：Constrained Agent MVP + verifier + fail-closed renderer；build `31 passed, 1 skipped`。
