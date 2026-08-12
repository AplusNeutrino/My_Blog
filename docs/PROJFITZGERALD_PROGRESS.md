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
13. **GOAI 评审对齐：** 涉及比赛定位、PPT、Demo、评审优化时，按《GOAI 无界应用｜Boundless Agents 参赛手册》的六个评分维度审查：行业场景价值、Agent 能力与任务闭环、产品体验与 Demo、技术实现深度、安全合规与可追溯、开放 / 复用。
14. **比赛文案真实性：** README、Project Summary、Pitch、Demo 和评审材料只能陈述真实 code / test / runtime evidence 支持的能力；不得为了评分宣称尚未实现的 Agent、RAG、企业权限、live provider 或自动决策能力。
15. **生成资产状态分离：** 内容源、构建脚本和最终生成的 PPT/PDF/视频/截图必须分别记录状态；仅更新文案源不能视为正式演示资产已经同步。
16. **唯一 tracker 规则：** 本文件继续作为唯一进度真源，`/projfitzgerald/` 只读取本文件；不得在 FitzSight repo 或其他文档中创建第二份任务状态 tracker。

<!-- TRACKER_DATA_START -->
```json
{
  "project": {
    "name": "Project Fitzgerald / FitzSight",
    "subtitle": "Financial Operations Intelligence Agent",
    "track": "GOAI 2026 · Boundless Agents · AI+金融",
    "northStar": "让 Brokerage / FinTech Operations Analyst 提出“为什么这个经营指标变了？”，由 Agent 在受限工具边界内自主调查并生成可验证的 decision support，最终业务决策由人完成。",
    "phase": "FitzSight v0.12.0 published / v0.12.1 formal deck + GOAI final reviewer gate complete / external runtime + human actions remain evidence-gated",
    "priority": "P0",
    "lastUpdated": "2026-08-12",
    "sourceVersion": "FitzSight v0.12.1 delivery · based on published AplusNeutrino/FitzSight main 04f196e74495d345fa7bc979d7447070c56e4020 (Release FitzSight v0.12.0) · My_Blog progress commit 9fe230c1ca8c0b457b4d67df35686aa4efcacca6 · v0.12.1 not yet published"
  },
  "summary": {
    "verifiedDone": 74,
    "inProgress": 7,
    "todo": 0,
    "blocked": 0,
    "note": "FitzSight v0.12.0 is verified as published on main commit 04f196e7 and the unique My_Blog progress source was updated in commit 9fe230c1. v0.12.1 completes the remaining local GOAI-alignment work: formal 12-slide PPTX/PDF regenerated as one CRM/FTD hero + one false-correlation refusal, real runtime-derived hero trace/answer evidence embedded, tested failure/insufficient-evidence branch shown, competition-facing docs/operator assets synchronized, and the official six-dimension GOAI reviewer gate completed without exceeding implementation evidence. Validation: 87 tests collected / 86 passed / 1 skipped / 0 failed; compileall PASS; v0.12.1 fixed benchmark 5/5 PASS; adversarial 8/8 PASS; slide overflow test PASS; same-source PDF rendered as 12 pages; local submission preflight PASS; handoff ready_for_user_takeover=true; final-machine local_core_ready=true with deterministic Agent smoke verified. The seven remaining in-progress items require Streamlit/OpenAI live runtime, portal confirmation, or real human rehearsal evidence; none are closed by presentation generation."
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
          "updated": "2026-08-12",
          "evidence": "v0.11 final_machine_check 默认不调用 OpenAI；仅用户显式传入 --include-openai 且主动配置稳定 API key/model 时才执行 live validator。build environment 未进行 live provider call，T4 保持 in_progress。",
          "owner": "user_runtime_manual",
          "executionMode": "explicit_opt_in_only"
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
          "updated": "2026-08-12",
          "evidence": "v0.11 新增 portable Final Machine Kit + final_machine_check；已在 clean extracted kit 中验证 local_core_ready=true。build environment Streamlit dependency 仍缺失，live health check status=not_run_dependency_missing，因此 E1 保持 in_progress，需最终演示机器真实 PASS。",
          "owner": "user_runtime_manual",
          "executionMode": "final_machine_manual_validation"
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
          "updated": "2026-08-12",
          "evidence": "v0.11 继续维持 user-manual-only submission boundary；manual handoff ZIP（SHA-256 cf455c4a646a105be49fc883900529c2ad8e1ae36e5df69bc4544dfe6a6383e3）、upload bundle、PPT/PDF、offline HTML/video、field map、Final Machine Kit 均已准备并 integrity PASS。实际 GOAI portal review/upload/final submit 与 confirmation screenshot/email/receipt 仍只由用户手动完成，未提供外部确认前保持 in_progress。",
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
          "updated": "2026-08-12",
          "evidence": "v0.9 deterministic SQLite latency snapshot 已存在；v0.11 final-machine tooling 保留 provider telemetry，但 OpenAI live provider 未实际调用，因此真实 provider latency/token/cost 仍无证据，F5 保持 in_progress。",
          "owner": "user_runtime_manual",
          "executionMode": "live_provider_evidence_required"
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
          "updated": "2026-08-12",
          "evidence": "v0.11 新增 FitzSight_Final_Machine_Kit.zip（SHA-256 55fa98046825a55a9bf5a3e760f379a8c0359f95a876f977039ac2fe393ebdea），包含 full local repo snapshot、Windows/POSIX launchers、manual handoff、offline HTML/video；将 kit 解压到全新目录后，final_machine_check 实跑 local_core_ready=true、deterministic Agent verified、preflight PASS。Local + video fallback 已验证；Live Streamlit 仍需最终机器真实 health-check，故保持 in_progress。",
          "owner": "user_runtime_manual",
          "executionMode": "final_machine_live_validation"
        },
        {
          "id": "R4",
          "title": "5–8 分钟路演与 <3 分钟演示",
          "status": "in_progress",
          "priority": "P2",
          "updated": "2026-08-12",
          "evidence": "v0.11 新增 REHEARSAL_PLAN.json、REHEARSAL_OPERATOR_CARD.md 与 rehearsal_assistant.py；脚本可本地记录 pitch/demo/Q&A 实测时长并按 5–8min / <3min 门槛判定。代码/干跑不等于真实演练，仍需用户人工计时证据后才能 done。",
          "owner": "user_manual",
          "executionMode": "human_rehearsal_required"
        },
        {
          "id": "R5",
          "title": "Q&A、稳定性与 business story",
          "status": "in_progress",
          "priority": "P2",
          "updated": "2026-08-12",
          "evidence": "v0.11 final-machine checklist + compact rehearsal operator card + existing JUDGE_QA/business story/offline fallback 已整合到 portable kit；但最终 Q&A/stability rehearsal 必须用户真实进行并提供结果，因此保持 in_progress。",
          "owner": "user_manual",
          "executionMode": "human_rehearsal_required"
        }
      ]
    },
    {
      "id": "M7",
      "title": "GOAI 手册对齐与 v0.12 评审升级",
      "date": "2026-08-12 → 2026-08-17",
      "status": "done",
      "goal": "以官方六维评分为约束，冻结 beachhead persona，强化真实 Agent Journey / product evidence / evaluation credibility / enterprise boundary，同时不超过真实实现范围",
      "items": [
        {
          "id": "V12-01",
          "title": "GOAI Boundless Agents 手册重审与 gap matrix",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "My_Blog progress source re-audit commit 9e51d906；按行业价值、Agent 闭环、产品体验、技术深度、安全可追溯、开放复用六维形成 v0.12 backlog。"
        },
        {
          "id": "V12-02",
          "title": "Primary persona / beachhead positioning freeze",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "README.md、MASTER_PLAN.md、docs/INITIAL_ROUND_PROJECT_SUMMARY.md、docs/PITCH_DECK_CONTENT.md、docs/V0.12_POSITIONING_AND_HERO.md：Primary=Brokerage / FinTech Operations Analyst；Secondary=Regional Operations / Sales Operations Manager；beachhead=acquisition → FTD → client-fund flows。"
        },
        {
          "id": "V12-03",
          "title": "Flagship CRM/FTD bounded-adaptive Agent Journey",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "src/fitzsight/investigation/engine.py + agent/orchestrator.py + tools/document_evidence.py；tool results 决定已批准 anomaly/event/document 分支；agent.branch_decision evidence；approved follow-up；tests/test_v12_hero_journey.py 覆盖 normal + event-tool failure / insufficient-evidence branch。"
        },
        {
          "id": "V12-04",
          "title": "Real UI/trace/Evidence/Verifier product-process evidence",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "scripts/build_hero_evidence.py 实跑 verified hero；docs/V0.12_HERO_RUN.json；submission/FitzSight_Hero_Run_Evidence.html/.png；含 user input、bounded trace、branch rationale、Evidence IDs、Verifier、guardrail、follow-up。PNG 由真实 runtime JSON 渲染，不是手工分析 mock。; v0.12 final-machine deterministic smoke verified and runtime-derived hero HTML/PNG remain local presentation evidence; Streamlit live remains separate/unverified"
        },
        {
          "id": "V12-05",
          "title": "Pitch 1 hero + 1 refusal narrative",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "v0.12.1 scripts/build_pitch_deck.py regenerated formal 12-slide PPTX/PDF as 1 CRM/FTD hero + 1 false-correlation refusal; runtime-derived FitzSight_Hero_Run_Trace/Answer images embedded; slides_test PASS (no canvas overflow); PDF 12 pages render-reviewed. PPTX SHA-256 6ede0712f14642aee88e10b9e3ff56e9413ce36b45ea12f53c4328ee4298090a; PDF SHA-256 914da2589b253efcaf2e35872009c13efee8e1209ef0698f355e941ad904caab."
        },
        {
          "id": "V12-06",
          "title": "Evaluation v2: holdout seeds + question paraphrases",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "scripts/run_evaluation_v2_holdout.py + docs/V0.12_HOLDOUT_RESULTS.json：2 unseen seeds × 4 paraphrase cases = 8 runs；routing 100%、verification 100%、evidence coverage 100%、false-correlation refusal 100%；supported-candidate 75%，1 个 unseen CRM seed fail-closed insufficient_evidence。"
        },
        {
          "id": "V12-07",
          "title": "Evaluation v2: controlled architecture ablation",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "scripts/run_evaluation_v2_ablation.py + docs/V0.12_ABLATION_RESULTS.json：Full verifier gate adversarial refusal 100%、unsafe answer 0%；no-verifier-gate ablation adversarial unsafe answer 100%、emitted evidence coverage 66.7%；明确非 Generic LLM baseline。"
        },
        {
          "id": "V12-08",
          "title": "Lightweight financial Document Evidence",
          "status": "done",
          "priority": "P1",
          "updated": "2026-08-12",
          "evidence": "src/fitzsight/tools/document_evidence.py + synthetic_documents/*：3 个固定 synthetic operational docs / source paragraph IDs；CRM hero 使用 CRM-CHANGE-2026-0715#p1 并进入 Evidence Registry/Verifier；无 arbitrary filesystem/network/vector RAG。"
        },
        {
          "id": "V12-09",
          "title": "Enterprise deployment boundary / blueprint",
          "status": "done",
          "priority": "P1",
          "updated": "2026-08-12",
          "evidence": "docs/ENTERPRISE_DEPLOYMENT_BOUNDARY.md：区分当前 PoC implemented controls 与 production SSO/RBAC/row-field policy/PII masking/retention/tenant isolation/observability blueprint；未宣称这些企业控制已实现。"
        },
        {
          "id": "V12-10",
          "title": "Decision Support / Human Decision language consistency",
          "status": "done",
          "priority": "P1",
          "updated": "2026-08-12",
          "evidence": "README、MASTER_PLAN、Project Summary、Pitch source、Architecture、Compliance、active rehearsal/video source 已统一“Autonomous investigation. Human decision.” / Decision Support → Human Decision；继续禁止 automated high-impact financial decisions。"
        },
        {
          "id": "V12-11",
          "title": "Full competition asset synchronization",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "v0.12.1 synchronized README/MASTER_PLAN/IMPLEMENTATION_STATUS/PROJECT_PROGRESS, Project Summary, Pitch source, Architecture/Compliance/UI Demo, speaker notes, Demo Runbook/video/rehearsal/operator/Judge Q&A/portal/field-map/checklist assets; upload/manual-handoff/final-machine packages rebuilt from synchronized formal deck. Streamlit/OpenAI live and portal/human evidence remain separate."
        },
        {
          "id": "V12-12",
          "title": "Final GOAI handbook reviewer gate",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "docs/V0.12.1_GOAI_REVIEWER_GATE.md audits current package against official handbook: industry value 25%, Agent loop 25%, product/Demo 20%, technical depth 15%, safety/compliance/traceability 10%, open/reuse 5%, plus AI+Finance document understanding/evidence trace/risk/compliance/no-overstep checks. Gate PASS for prepared package; live Streamlit/OpenAI, portal and human rehearsal explicitly remain unverified."
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
    },
    {
      "id": "RK-15",
      "level": "medium",
      "title": "Final presentation machine differs from build environment",
      "mitigation": "v0.11 portable Final Machine Kit + one-command readiness JSON；Streamlit/OpenAI 只有最终机器/真实 provider evidence 才能标 done；失败立即回退 deterministic CLI/offline HTML/video。"
    },
    {
      "id": "RK-16",
      "level": "high",
      "title": "Primary persona / beachhead 过宽",
      "mitigation": "v0.12 Primary 固定 Brokerage / FinTech Operations Analyst；Secondary 只作邻近角色；主链 acquisition → FTD → client-fund flows。"
    },
    {
      "id": "RK-17",
      "level": "high",
      "title": "Agent 被评委理解为固定 pipeline",
      "mitigation": "CRM hero 增加 bounded result-driven branch + fail-closed dependency path + approved follow-up，并在真实 execution trace 中显示 branch rationale。"
    },
    {
      "id": "RK-18",
      "level": "high",
      "title": "主故事缺少真实产品过程证据",
      "mitigation": "v0.12 生成 runtime-derived HERO_RUN JSON + HTML/PNG，显示 input/trace/Evidence/Verifier/final guardrail；formal deck 下一步必须嵌入。"
    },
    {
      "id": "RK-19",
      "level": "high",
      "title": "固定 seed / showcase benchmark 可信度不足",
      "mitigation": "v0.12 新增 unseen seeds + paraphrase holdout 与 no-verifier-gate architecture ablation；保留不足证据案例，不抹平成 100% 根因命中。"
    },
    {
      "id": "RK-20",
      "level": "medium",
      "title": "Document understanding / enterprise knowledge depth 不足",
      "mitigation": "先实现轻量 source-addressable synthetic document evidence；明确不是 production RAG，后续扩展必须保持 source/evidence/verifier boundary。"
    },
    {
      "id": "RK-21",
      "level": "high",
      "title": "“Decision”文案被误解为自动高影响金融决策",
      "mitigation": "统一为 Autonomous investigation. Human decision. / analytical decision support；Compliance 明确高影响决策在 FitzSight 外由授权人执行。"
    },
    {
      "id": "RK-22",
      "level": "medium",
      "title": "Enterprise readiness 被误宣称为已实现",
      "mitigation": "ENTERPRISE_DEPLOYMENT_BOUNDARY.md 将 SSO/RBAC/PII/retention 等明确标为 production blueprint-only；比赛材料必须区分 implemented vs planned。"
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
    "D-034 Final handoff 必须 self-contained/operator-oriented：用户拿到 portable handoff packet 后即可依据 START_HERE、field map、manual checklist、runtime instructions 与已生成资产自行完成外部提交，无需额外代码生成",
    "D-035 Final-machine 默认检查必须 local/provider-safe：允许 deterministic local checks 与 127.0.0.1 Streamlit health probe；不得默认调用 live model provider，OpenAI 仅通过用户显式 --include-openai opt-in 执行",
    "D-036 Final-machine readiness 与 external submission 是两条独立真源：local demo-ready 不能推断 GOAI portal 已上传/已提交/已确认；外部提交始终按 user-manual evidence 更新",
    "D-037 Human rehearsal evidence 必须由用户真实演练产生：AI 可生成 timing targets/operator card/recording tool，但代码存在或模拟时长不能关闭 R4/R5",
    "D-038 GOAI 手册六维评分成为后续 competition review gate；不能只按功能数量优化。",
    "D-039 Primary persona 固定为 Brokerage / FinTech Operations Analyst；Secondary 为 Regional Operations / Sales Operations Manager；主链 acquisition → FTD → client-fund flows。",
    "D-040 CRM/FTD 是 primary hero；false-correlation 是 strongest refusal；其余 workflow 作为 breadth，不再五个故事等权铺陈。",
    "D-041 Agent autonomy 采用 bounded adaptive execution：tool results 可选择下一 approved action，但 planner/model 仍不能生成 SQL、任意 tool args、任意文件访问或高影响金融动作。",
    "D-042 Judge-facing product evidence 必须展示真实 input → trace/branch → Evidence IDs → Verifier → guarded answer；manual mock 不能替代 runtime evidence。",
    "D-043 正式 pitch 采用 1 hero + 1 refusal narrative；net deposit/customer intelligence/marketing 主要进入 breadth / appendix / Q&A。",
    "D-044 Evaluation v2 必须包含 unseen seed/question paraphrase holdout 与 architecture ablation；不得把 fixed-seed benchmark 当成泛化证明。",
    "D-045 Document Evidence 先做小而可验证的 synthetic source/paragraph corpus；不为评分虚构大规模 RAG/enterprise knowledge capability。",
    "D-046 Enterprise deployment 只提供 implemented-vs-planned blueprint；SSO/RBAC/PII/tenant/retention/observability 未实现前不得写成当前能力。",
    "D-047 Competition-facing end state 统一为 Decision Support → Human Decision；tagline 采用 Autonomous investigation. Human decision.。",
    "D-048 /projfitzgerald 继续只读取本 PROJFITZGERALD_PROGRESS.md；FitzSight repo 中 PROJECT_PROGRESS.md 只能作 implementation handoff note，不得成为第二 tracker。"
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

## 当前实现基线（v0.12.0 已发布 / v0.12.1 本地交付）

- 正式产品名：**FitzSight**
- 唯一进度真源：本文件；tracker：`https://neutriverse.uk/projfitzgerald/`
- 实现仓库：`AplusNeutrino/FitzSight`
- 本轮开发前已核验公开 `main`：commit `04f196e74495d345fa7bc979d7447070c56e4020`，message `Release FitzSight v0.12.0`。
- My_Blog 唯一进度真源已核验对应发布提交：`9fe230c1ca8c0b457b4d67df35686aa4efcacca6`，message `Update FitzSight progress for v0.12.0`。
- 本次本地交付版本：`v0.12.1`；**尚未由用户发布到 GitHub**。
- Build tests：`87 tests collected`；完整非重叠分组汇总 `86 passed, 1 skipped, 0 failed`；唯一 skip 为 build sandbox DuckDB-specific integration test。
- Compile：`PASS`。
- v0.12.1 fixed benchmark regression：`5/5 PASS`；root-cause scenario accuracy / false-correlation rejection / mean evidence coverage 均 `100%`；verifier violations `0`。
- v0.12.1 adversarial gate：`8/8 PASS`。
- Evaluation v2（核心实现未改）：8 holdout runs routing/verification/evidence coverage `100%`；false-correlation refusal `100%`；supported-candidate `75%`，保留 1 个正确 `insufficient_evidence` CRM unseen seed。
- Formal Deck：12 slides；1 CRM/FTD hero + 1 false-correlation refusal；真实 runtime-derived trace/answer Evidence 进入主叙事；`slides_test.py` = PASS，无 canvas overflow；same-source PDF = 12 pages 并 render-review PASS。
- Formal deck hashes：PPTX `6ede0712f14642aee88e10b9e3ff56e9413ce36b45ea12f53c4328ee4298090a`；PDF `914da2589b253efcaf2e35872009c13efee8e1209ef0698f355e941ad904caab`。
- GOAI final reviewer gate：`docs/V0.12.1_GOAI_REVIEWER_GATE.md` = PASS；按官方六维和 AI+金融资料理解/依据追溯/风险提示/合规/避免越权逐项核验。
- Local release readiness：submission preflight `PASS`；handoff `ready_for_user_takeover=true`；final-machine `local_core_ready=true`；deterministic Agent smoke `verified`。
- Streamlit live：**未验证**；本轮 final-machine report 使用 provider-safe/local path，不能把 UI code/PPT 当 live PASS。
- OpenAI live：未请求、未调用，**未验证**；无 live provider latency/token/cost claim。
- GOAI portal / Gmail / final submit / confirmation：**user-manual only，未执行**。
- Human pitch/demo/Q&A rehearsal：仍需要用户真实计时与稳定性证据。

## 下一阶段：External Runtime + Human Evidence Closure

1. 最终演示机器运行 Streamlit live health-check；真实 PASS 后关闭 E1，并完成 R3 的 Live/local/video 三套闭环。
2. OpenAI planner 保持 explicit opt-in；只有真实 provider call 才能关闭 T4，并据真实 telemetry 更新 F5。
3. 用户真实执行 pitch/demo/Q&A rehearsal 后关闭 R4/R5。
4. GOAI portal review/upload/final submit/confirmation 继续由用户手动完成并以实际凭证更新 G6。
5. 不再新增无明确评分收益的核心 intent；后续代码工作只围绕最终机器稳定性或有证据的新评审需求。

## 更新日志
- 2026-08-12：核验用户已发布 v0.12.0：FitzSight main=`04f196e74495d345fa7bc979d7447070c56e4020`，My_Blog progress commit=`9fe230c1ca8c0b457b4d67df35686aa4efcacca6`。在该真实 published baseline 上构建 v0.12.1：formal 12-slide PPTX/PDF 重构为 1 CRM/FTD hero + 1 false-correlation refusal，嵌入 runtime-derived hero trace/answer Evidence，加入 tested failure branch 与 Evaluation v2；同步 competition docs/operator assets，完成官方 GOAI 六维 final reviewer gate。87 collected / 86 passed / 1 skipped / 0 failed；compileall、5/5 benchmark、8/8 adversarial、slides overflow、12-page PDF render、preflight、handoff、local final-machine deterministic smoke 均 PASS。V12-05/V12-11/V12-12 关闭；M7 done；总计 74 done / 7 in_progress / 0 todo / 0 blocked。剩余 7 项均继续要求真实 Streamlit/OpenAI/portal/human evidence。


- 2026-08-12：FitzSight v0.12.0 delivery 基于已核验 `main` 272dc3d5 构建：完成 primary persona/beachhead freeze、bounded-adaptive CRM hero + event dependency fail-closed branch、approved follow-up、source-addressable synthetic document evidence、runtime-derived hero process evidence、holdout seed/paraphrase evaluation、controlled verifier-gate ablation、enterprise deployment boundary 与 Human Decision wording；85 collected / 84 passed / 1 skipped / 0 failed；compileall、5/5 benchmark、8/8 adversarial PASS；local submission preflight PASS、handoff `ready_for_user_takeover=true`、final-machine `local_core_ready=true` 且 deterministic Agent smoke `verified`。正式 PPT/PDF 尚未按 v0.12 narrative regenerate，因此 V12-05/V12-11 仍 in_progress；V12-12 final handbook gate 仍 todo。Streamlit/OpenAI live 仍未验证；无 GitHub/GOAI/Gmail/external write。
- 2026-08-12：GOAI Boundless Agents handbook re-audit 创建 M7/v0.12 backlog，并将公开 FitzSight main 校正为 v0.11.0 commit 272dc3d5；V12-01 done，其余待实现。
- 2026-08-12：FitzSight v0.11 完成 final-machine operations：新增 portable Final Machine Kit、Windows/POSIX launchers、one-command final_machine_check、explicit-opt-in OpenAI validation boundary、rehearsal timing recorder/plan/operator card；79 tests collected / 78 passed / 1 skipped；5/5 benchmark、8/8 adversarial、compileall、preflight、handoff/kit integrity 均 PASS；clean extracted kit 实跑 `local_core_ready=true` 且 deterministic Agent `verified`；剩余 runtime/human evidence 保持 evidence-gated。
