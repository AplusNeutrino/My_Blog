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
12. **手动提交边界：** 与比赛提交有关的外部写操作（GOAI portal 打开/填写/上传/最终提交、确认截图/邮件获取等）默认由用户手动完成。AI 只负责本地准备、校验、打包与说明；除非用户针对某个具体外部动作另行明确授权，否则不得主动访问 Gmail、提交平台或执行其他外部写操作。

<!-- TRACKER_DATA_START -->
```json
{
  "project": {
    "name": "Project Fitzgerald / FitzSight",
    "subtitle": "Financial Operations Intelligence Agent",
    "track": "GOAI 2026 · Boundless Agents · AI+金融",
    "northStar": "让金融业务管理者提出‘为什么这个指标变了？’，由 Agent 自主完成数据调查、统计验证与证据化解释。",
    "phase": "FitzSight v0.10.0 operator handoff complete / manual-submission boundary enforced / user takeover packet ready",
    "priority": "P0",
    "lastUpdated": "2026-08-11",
    "sourceVersion": "FitzSight v0.10.0 delivery · based on AplusNeutrino/FitzSight main 5304c5cf (Release FitzSight v0.9.0) · DuckDB deployment runtime already validated"
  },
  "summary": {
    "verifiedDone": 62,
    "inProgress": 7,
    "todo": 0,
    "blocked": 0,
    "note": "FitzSight v0.10.0 completes the local operator handoff layer without performing any external submission. Build validation: 74 tests collected; 73 passed, 1 skipped; compileall PASS. Benchmark regression 5/5 PASS and adversarial suite 8/8 PASS. v0.10 adds an explicit user-manual submission boundary, single-entry START_HERE guide, manual submission/runtime checklists, field map, machine-readable handoff readiness, and portable FitzSight_Manual_Handoff.zip. Local preflight PASS reports external_write_actions_performed=false, portal automation=false, Gmail/email automation=false, and ready_for_user_takeover=true. F7 is now done. G6 remains in_progress and owned by user_manual until actual portal submission/confirmation evidence is provided. Streamlit/OpenAI live runtime and timed human rehearsal remain separate external/manual evidence tasks."
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
        },
        {
          "id": "A9",
          "title": "第四 synthetic benchmark：Americas paid-media volume / lead-quality shift",
          "status": "done",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": "v0.7 scenarios.py + generator.py + investigation/lead_quality.py；default seed leads +838 (+315.0%)，FTD -10.84pp，Paid Search mix +60.52pp，Paid Search FTD -16.44pp，p=4.43e-05，4/4 claims verified"
        },
        {
          "id": "A10",
          "title": "第五 synthetic benchmark：Asia false-correlation trap",
          "status": "done",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": "v0.7 Asia Affiliate quality deterioration + nearby unrelated OFFICE_RELOCATION event；Asia FTD -8.13pp，Affiliate -15.81pp，p=0.00463；false correlation rejected=true，4/4 claims verified"
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
          "status": "done",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": "v0.6 src/fitzsight/tools/segmentation.py + tests/test_segmentation.py；transparent behavioral_value_score_v1 using observable deposits/trading only；normal SQL does not query *_gt；Europe default 6,770 customers, 100% coverage, 4 segments"
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
          "evidence": "v0.9 OpenAI Responses provider 增加 response/model/token/planning-latency telemetry，live validator 可执行完整 planner→tools→verifier；当前 build environment 无 FITZSIGHT_MODEL/API key，check=status not_run_missing_configuration，保持 in_progress。"
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
        },
        {
          "id": "C9",
          "title": "Customer Intelligence / segmentation 第三 Agent intent",
          "status": "done",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": "v0.6 CustomerSegmentationTool + CustomerIntelligenceInvestigationEngine + catalog/router/runtime integration；rule planner 与 JSON-file planner 均通过；SQLite Agent 5/5 claims verified；third benchmark PASS"
        },
        {
          "id": "C10",
          "title": "第四/第五 approved Agent intents：marketing quality + false-correlation guardrail",
          "status": "done",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": "v0.7 agent/catalog.py + investigation/lead_quality.py + router/runtime；plan_version 0.7；两个新 intent 均经 deterministic tools → Evidence Registry → Verifier 闭环"
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
          "evidence": "v0.9 streamlit_app.py 已改为纯 presentation renderer over verified result；runtime validator 已实现。build environment 实际 check=status not_run_dependency_missing（Streamlit 未安装），因此 live runtime 仍未验证。"
        },
        {
          "id": "E2",
          "title": "KPI cards",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.9 src/fitzsight/ui/presenter.py：pure presentation layer 从 verified Agent result 生成 KPI cards；tests/test_ui_presenter.py 对 5 workflows 验证每次 5 KPI cards，JSON-safe；不依赖 Streamlit runtime。"
        },
        {
          "id": "E3",
          "title": "Investigation trace",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.9 pure presenter 生成 approved AgentPlan trace rows + verifier outcome；tests/test_ui_presenter.py 对 5 workflows 验证 trace 非空；Streamlit live rendering 单独由 E1 跟踪。"
        },
        {
          "id": "E4",
          "title": "Charts",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.9 pure presenter 为 5 intents 生成 presentation-only ChartSpec；tests/test_ui_presenter.py 验证每个 workflow chart 非空；业务数值仍来自 verified Agent result。"
        },
        {
          "id": "E5",
          "title": "Evidence cards 与 report",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.9 pure presenter 生成 verified findings / guardrail / Evidence cards，并验证所有 Evidence status=success、presentation JSON-safe；offline HTML 同样展示 verified findings/evidence。"
        },
        {
          "id": "G1",
          "title": "Project summary",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "docs/INITIAL_ROUND_PROJECT_SUMMARY.md updated for v0.7 five-intent / 5-scenario benchmark and adversarial metrics"
        },
        {
          "id": "G2",
          "title": "PPT / PDF",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.8 generated submission/FitzSight_GOAI_Initial_Round.pptx and .pdf from the same 12-slide source; PDF exported via LibreOffice, inspected as 12 pages / 16:9, rendered to PNG and visually reviewed with no clipping/overlap; PPTX SHA-256 25e11a245cc09017e7a6f710f605cf13a59c457711e19dc900773fc8118553f1; PDF SHA-256 41e58215828281891c6138d18a379926f4ad111efb1b599754db656626f43421"
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
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.9 submission/FitzSight_Offline_Demo_Backup.mp4：由 5/5 verified deterministic Agent runs 的 offline-demo JSON 生成；H.264 1280x720 30fps，实际约 64s；intro/middle/end representative frames visual review 无明显 clipping/overlap。Live Streamlit screen capture 仍由 E1/R3 跟踪。"
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
          "status": "in_progress",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "v0.10 已生成 START_HERE_MANUAL / MANUAL_SUBMISSION_CHECKLIST / GOAI_FIELD_MAP / portable FitzSight_Manual_Handoff.zip（SHA-256 a072233574b4ef3ba029a78a5f9473b4a17f433276ae3b3d4cd46643ddb7737c），preflight PASS 且明确 external_write_actions_performed=false、portal automation=false、Gmail/email automation=false。实际 GOAI portal review/upload/final submit 与 confirmation screenshot/email/receipt 由用户手动完成；未提供外部确认前保持 in_progress。",
          "owner": "user_manual",
          "executionMode": "manual_only"
        },
        {
          "id": "G7",
          "title": "Secrets、license、repo visibility 检查",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-11",
          "evidence": "repo 已验证 public；.gitignore/.env.example 已存在；v0.6 新增 MIT LICENSE 与 THIRD_PARTY_NOTICES.md；仍需最终提交前再做一次 secrets/dependency scan"
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
          "status": "done",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": "evaluation/benchmark_catalog.json v0.7 已包含 5 个独立 synthetic scenarios；scripts/run_benchmark.py 5/5 PASS"
        },
        {
          "id": "F2",
          "title": "Root cause scoring",
          "status": "done",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": "v0.7 4 个 anomaly/driver scenarios 均通过；root-cause scenario accuracy 100%"
        },
        {
          "id": "F3",
          "title": "Evidence coverage scoring",
          "status": "done",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": "v0.7 five-scenario mean evidence coverage 100%"
        },
        {
          "id": "F4",
          "title": "Hallucination / overclaim scoring",
          "status": "done",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": "v0.7 scripts/run_adversarial_evaluation.py + evaluation/adversarial_cases.json：8/8 PASS；scope refusal / planner policy / evidence integrity / causal overclaim / _gt leakage / false-correlation rejection 均 100%"
        },
        {
          "id": "F5",
          "title": "Latency / cost measurement",
          "status": "in_progress",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": "v0.9 docs/V0.9_DETERMINISTIC_LATENCY.json：SQLite full-Agent 5 workflows × 3 = 15 verified runs；overall mean 292.29ms / p50 300.90ms / p95 343.35ms（build-environment-specific）。OpenAI live provider latency/token/cost 尚无真实调用证据，因此保持 in_progress。"
        },
        {
          "id": "F6",
          "title": "Test suite 与 evaluation harness",
          "status": "done",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": "v0.7 5-scenario benchmark + 8-case adversarial evaluation harness；build tests 50 passed, 1 skipped；compileall PASS"
        },
        {
          "id": "F7",
          "title": "UI、视频与部署脚本优化",
          "status": "done",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": "v0.10 完成 operator handoff layer：pure UI/offline/video/runtime validators 维持；新增 build_manual_handoff.py、handoff_readiness.py、START_HERE_MANUAL、manual checklist、runtime checklist、field map 与 portable manual handoff ZIP（SHA-256 a072233574b4ef3ba029a78a5f9473b4a17f433276ae3b3d4cd46643ddb7737c）；preflight/handoff integrity PASS。Live Streamlit 本身仍由 E1/R3 单独跟踪，不再阻塞 F7 的本地优化 DoD。"
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
          "status": "done",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": "v0.8 scripts/start_demo.py 提供 one-command auto/ui/cli launcher；auto 在 Streamlit 不可用时 fallback deterministic CLI；3 launcher unit tests PASS，实际 `python scripts/start_demo.py --mode cli --backend sqlite` 完整执行并输出 final status verified；.env.example 已存在"
        },
        {
          "id": "R2",
          "title": "Benchmark results 与完整 compliance explanation",
          "status": "done",
          "priority": "P1",
          "updated": "2026-08-11",
          "evidence": "docs/V0.7_BENCHMARK_RESULTS.json + docs/V0.7_ADVERSARIAL_RESULTS.json + docs/COMPLIANCE_AND_SAFETY.md；5/5 benchmark PASS，8/8 adversarial PASS，compliance/safety boundary documented"
        },
        {
          "id": "R3",
          "title": "Live / local / video 三套 Demo",
          "status": "in_progress",
          "priority": "P2",
          "updated": "2026-08-11",
          "evidence": "v0.9 已具备 local deterministic launcher + self-contained offline HTML + H.264 video backup；DuckDB local runtime此前已验证。Live Streamlit path 尚未在 final machine 验证，因此 Live/local/video 三套状态仍未全部 done。"
        },
        {
          "id": "R4",
          "title": "5–8 分钟路演与 <3 分钟演示",
          "status": "in_progress",
          "priority": "P2",
          "updated": "2026-08-11",
          "evidence": "v0.9 submission/PITCH_REHEARSAL.md 设定 6m30s pitch + 2m20s demo target，并有 12-slide speaker notes / demo runbook；仍缺人工计时 rehearsal 记录，保持 in_progress。"
        },
        {
          "id": "R5",
          "title": "Q&A、稳定性与 business story",
          "status": "in_progress",
          "priority": "P2",
          "updated": "2026-08-11",
          "evidence": "v0.9 Judge Q&A、business story、5-scenario benchmark、8-case adversarial gate、offline fallback 与 submission assets 已齐；最终稳定性/Q&A rehearsal 仍需用户现场计时/演练证据。"
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
    },
    {
      "id": "RK-11",
      "level": "high",
      "title": "Customer segmentation 被误用为高影响决策",
      "mitigation": "segmentation 明确标注 descriptive-only；Verifier/claim guardrail 禁止 credit、AML、suitability、eligibility、restriction 或 adverse-action 推断"
    },
    {
      "id": "RK-12",
      "level": "medium",
      "title": "False correlation / post-hoc narrative",
      "mitigation": "nearby-event falsification benchmark + causal-language verifier；时间邻近不能单独构成 root-cause evidence"
    },
    {
      "id": "RK-13",
      "level": "high",
      "title": "Competition-facing metrics drift from current deterministic runtime",
      "mitigation": "v0.9 pitch deck Slides 4–8 use fresh verified Agent runs in a temporary synthetic dataset; active README/project-summary/pitch docs synchronized; regression test rejects stale net-deposit/customer values."
    },
    {
      "id": "RK-14",
      "level": "high",
      "title": "外部提交动作越界 / 未经用户授权访问外部账户",
      "mitigation": "v0.10 固化 user-manual-only submission boundary；自动化默认只做本地 prepare/validate/package，不访问 Gmail、不提交 portal、不执行外部写操作。"
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
    "D-016 UI 只负责展示 verified outputs/evidence，不重新计算业务指标或绕过 verifier",
    "D-017 Customer segmentation 必须透明且 descriptive-only：behavioral_value_score_v1 仅使用 observable deposit/trading behavior；禁止 normal Agent 使用 hidden *_gt labels；不得转化为 credit/AML/suitability/adverse-action 决策",
    "D-018 Benchmark evidence quality 成为一等指标：runner 输出 scenario pass rate、root-cause scenario accuracy、evidence coverage、verifier violations 与 deterministic latency",
    "D-019 FitzSight 项目代码采用 MIT License；third-party dependencies 继续遵守各自 license，并由 THIRD_PARTY_NOTICES.md 跟踪",
    "D-020 UI KPI/cards/charts/trace 只读取 verified Agent result，不能重新定义 KPI 或形成第二条未验证 analytics path",
    "D-021 Acquisition analysis 必须区分 volume、mix 与 within-channel performance；不能把 more leads 等同于 better performance",
    "D-022 Nearby event 需要 falsification before causal attribution；时间邻近不能自动升级为 root cause",
    "D-023 Adversarial evidence/safety checks 成为 release gate：scope refusal、planner policy、evidence integrity、causal overclaim、_gt leakage、false correlation 均需可复现测试",
    "D-024 初始 5-scenario benchmark 目标已完成；后续优先 competition demo/runtime/submission assets，而不是无明确评估收益地继续扩场景",
    "D-025 初赛阶段停止无明确收益的 benchmark 扩张；v0.8 优先 judge-facing clarity、runnable demo、submission assets 与 preflight",
    "D-026 正式 PPTX/PDF 只能总结已验证项目状态；不得在 presentation 中引入 repository evidence 不支持的新分析结论；PDF 必须由同一 PPTX 导出并 render-review",
    "D-027 One-command startup 必须保留 deterministic fallback；Streamlit/外部模型不可用时，核心 competition demo 仍可通过 CLI 运行",
    "D-028 Submission preflight 是本地 release gate，不等于 portal submission success；实际上传、截图、邮件确认继续要求外部证据",
    "D-029 UI presentation logic 必须 pure/testable：KPI cards、ChartSpec、trace 与 Evidence cards 只从 verified Agent result 派生；Streamlit 仅作为 renderer，不形成第二条 analytics path",
    "D-030 Competition-facing numeric claims 必须来自 current verified runtime：pitch-deck builder 使用临时 synthetic dataset fresh-run 生成 Slides 4–8；active submission docs 禁止依赖 stale hardcoded benchmark values",
    "D-031 Offline HTML/MP4 是 resilience assets，不是 live runtime evidence；其生成要求 5/5 verified deterministic runs，但不能据此关闭 Streamlit/OpenAI live validation",
    "D-032 Live provider telemetry 可记录 response ID、requested/returned model、token usage 与 measured planning latency；不得输出 API key，也不在无真实调用/可靠 pricing source 时编造 monetary cost",
    "D-033 Competition submission 默认 user-manual only：AI/自动化只负责本地准备、校验、hash、render 与 package；不得自行打开/提交 GOAI portal、上传文件、访问 Gmail 获取确认、发送邮件或执行其他外部账户写操作，除非用户对具体动作另行明确授权",
    "D-034 Final handoff 必须 self-contained/operator-oriented：用户拿到 portable handoff packet 后即可依据 START_HERE、field map、manual checklist、runtime instructions 与已生成资产自行完成外部提交，无需额外代码生成"
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

## 当前实现基线（v0.10）

- 正式产品名：**FitzSight**
- 实现仓库：`AplusNeutrino/FitzSight`
- 已核验公开代码基线：`v0.9.0` commit `5304c5cf3917f344273aa1a2465e81a0a2b74b00`（`Release FitzSight v0.9.0`）
- 本次实现版本：`v0.10.0`
- Build tests：`74 tests collected`；完整非重叠分组汇总 `73 passed, 1 skipped`；唯一 skip 为 build sandbox 缺少 DuckDB
- Compile：`python -m compileall -q src scripts tests streamlit_app.py` → `PASS`
- Deterministic benchmark regression：`5/5 PASS`；scenario/root-cause/false-correlation/evidence coverage 均 `100%`；verifier violations `0`
- Adversarial release gate：`8/8 PASS`
- Manual handoff ZIP：`submission/FitzSight_Manual_Handoff.zip`；integrity `PASS`；`external_submission_performed=false`；`network_actions_performed=false`
- Handoff readiness：`ready_for_user_takeover=true`；portal copy、PPTX/PDF、offline HTML/video、manual checklist、operator boundary 均已准备
- Final local preflight：`PASS`；missing files=`0`；generated CSV=`0`；secret hits=`0`；manual handoff ZIP integrity=`true`
- **Manual submission boundary：** GOAI portal review/upload/final submit、confirmation screenshot/email/receipt 均由用户手动完成；AI 默认不得主动访问 Gmail、提交平台或执行外部写操作
- DuckDB deployment runtime：此前已验证；default constrained planner 与 JSON-file planner 均 `verified`
- Streamlit live check：仍需最终演示机器真实 health-check 才能关闭 E1/R3
- OpenAI live check：仍需用户主动配置稳定 API key/model 并提供真实 validator 输出才可关闭 T4/F5

## 下一阶段：User Takeover / External Evidence Only

1. 用户从 `submission/START_HERE_MANUAL.md` 开始；需要提交的文本、PPT/PDF、offline demo/video 与 field map 已全部准备。
2. GOAI portal 的打开、字段核对、上传、最终提交与确认截图/邮件/receipt **只由用户手动完成**；未收到用户明确指令时 AI 不访问 Gmail/portal。
3. 最终演示机器运行 `python scripts/runtime_doctor.py` 与 `python scripts/validate_streamlit_runtime.py`；真实 PASS 后关闭 E1/R3。
4. OpenAI planner 为可选路径；仅在用户主动配置稳定 credential/model 后运行 `python scripts/validate_openai_runtime.py`，并只记录非 secret telemetry。
5. 用户按 `submission/PITCH_REHEARSAL.md` 完成人工计时与 Q&A/stability rehearsal；完成后再关闭 R4/R5。
6. 初赛前不再扩核心 intent/benchmark；后续实现仅修复可靠性、证据完整性、安全边界或交接可用性问题。

## 更新日志

- 2026-08-11：FitzSight v0.10 完成 operator handoff：固化 user-manual-only submission boundary；新增 OPERATOR_BOUNDARY、START_HERE_MANUAL、manual submission/runtime checklist、GOAI field map、build_manual_handoff、handoff_readiness 与 portable manual handoff ZIP；74 tests collected / 73 passed / 1 skipped；5/5 benchmark、8/8 adversarial、compileall 与 preflight 均 PASS；`ready_for_user_takeover=true`；F7 关闭为 done，G6 明确 owner=`user_manual` 且实际 portal/邮件确认仍需用户证据。

- 2026-08-11：FitzSight v0.9 完成 runtime/submission resilience：pure tested UI presenter、5/5 verified offline HTML、H.264 backup video、runtime doctor、Streamlit/OpenAI live validators、provider telemetry、15-run deterministic latency、portal/rehearsal assets 与 upload convenience bundle；active pitch deck/current docs 修复 stale metrics 并改为 fresh verified runtime source；69 tests collected / 68 passed / 1 skipped；final preflight PASS。

- 2026-08-11：依据 Master Plan 建立初始追踪基线。
- 2026-08-11：发布并验证 FitzSight v0.1 → v0.5；完成 Synthetic Data、deterministic Tool Layer、Evidence/Verifier、CRM/FTD + Net Deposit multi-intent Agent、OpenAI provider adapter 与 Streamlit shell。
- 2026-08-11：部署环境完成 DuckDB runtime validation：`data/generated` 成功加载；default constrained planner 与 JSON-file planner 均成功执行；final status `verified`；verifier evidence `E0012`；final-answer evidence `E0013`；`T3` 关闭为 `done`。
- 2026-08-11：FitzSight v0.6 新增 Customer Intelligence 第三 Agent intent、3-scenario benchmark、UI KPI/chart/trace/evidence code、Project Summary、Pitch content source 与 MIT License。
- 2026-08-11：FitzSight v0.7 新增 Americas marketing lead-quality 与 Asia false-correlation 第四/第五 Agent intents；初始 benchmark catalog 达到 `5 scenarios`，`5/5 PASS`。
- 2026-08-11：v0.7 benchmark 指标：scenario pass rate `100%`、root-cause scenario accuracy `100%`、false-correlation rejection accuracy `100%`、mean evidence coverage `100%`、verifier violations `0`。
- 2026-08-11：v0.7 adversarial release gate `8/8 PASS`；完成 scope refusal、planner SQL/high-impact policy、missing evidence、causal overclaim、`*_gt` leakage 与 false-correlation falsification 检查。
- 2026-08-11：v0.7 新增完整 `COMPLIANCE_AND_SAFETY.md`，Pitch Deck content source 扩展为 12 slides；下一阶段切换为 initial-round submission sprint。
- 2026-08-11：FitzSight v0.8 完成 initial-round submission sprint：`scripts/start_demo.py` one-command launcher（CLI 实跑 verified / auto fallback tested）、12-slide PPTX/PDF 生成并 render-review、submission preflight PASS、Demo Runbook / Speaker Notes / Judge Q&A / Submission Checklist 完成；G2 与 R1 关闭为 done；实际 Streamlit/OpenAI live runtime、video recording 与 portal submission 仍保持未完成状态。
