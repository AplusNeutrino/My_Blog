# Project Fitzgerald / FitzSight 进度真源

> 本文件是 `/projfitzgerald` 项目追踪页的**唯一、独立进度真源**。页面直接读取本文件中的 `TRACKER_DATA` JSON；后续项目状态只维护这一份文件，不创建或并行维护第二个进度真源。
>
> **实现仓库：** `https://github.com/AplusNeutrino/FitzSight`  
> **进度真源：** `https://github.com/AplusNeutrino/My_Blog/blob/main/docs/PROJFITZGERALD_PROGRESS.md`  
> **追踪页：** `https://neutriverse.uk/projfitzgerald/`

## AI 更新规则

1. 只在有代码、文件、测试、截图、校验结果或提交记录等证据时，将任务设为 `done`；仅在主计划中出现不等于已完成。
2. 已开始但未满足 Definition of Done 的任务设为 `in_progress`，否则保持 `todo`；明确延期的任务设为 `blocked`。
3. 更新任务时同步维护 `updated`、`evidence`、顶部 `lastUpdated`、`summary` 和文末更新日志。
4. 新任务必须保留唯一 `id`，并归入现有阶段；范围或工作流变更需同时记录到 `decisions`。
5. 所有核心功能必须满足：可运行、尽量有确定性测试、处理失败状态、输出可见、证据已记录、文档已更新、无 secrets、可从干净环境演示。
6. **正式产品名固定为 `FitzSight`。** `FinSight` 仅视为项目早期历史命名。后续维护的代码、README、Master Plan、Release Notes、包元数据、UI、PPT、演示文案和新生成文件均必须使用 `FitzSight`；发现仍在使用 `FinSight` 的维护中内容时，应在最近一次交付中统一修正。历史 Git commit 信息不要求重写。
7. **每次 AI 向用户交付新的 FitzSight 代码/文件包时，必须把当次更新后的 `PROJFITZGERALD_PROGRESS.md` 一并放进同一个 ZIP 交付包。** 进度文件应反映该交付包实际包含并验证过的状态，不能提前把未实现功能标为完成。用户收到 ZIP 后自行将代码内容部署到 `AplusNeutrino/FitzSight`，并将本进度文件部署到 `AplusNeutrino/My_Blog/docs/PROJFITZGERALD_PROGRESS.md`。
8. 每次开始新的实现工作前，优先读取 `My_Blog/docs/PROJFITZGERALD_PROGRESS.md` 判断当前任务，再读取 `AplusNeutrino/FitzSight` 当前 `main` 作为代码基线；如果计划文件与代码/测试/提交证据不一致，以可验证实现证据校正本进度真源。
9. 每个交付包应保留清晰版本号、Release Notes（如适用）、测试结果和关键验证证据；若当次无法实际运行某项测试，应明确记录“未验证”，不能视为通过。
10. **Agent 安全边界：** Planner/LLM 输出始终视为不可信输入；只能选择已批准高层 action，不能直接生成或执行 SQL、任意工具参数、高风险金融动作；最终结论必须经过 EvidenceClaimVerifier，验证失败则 fail closed。
11. **External runtime 证据规则：** OpenAI API、Streamlit、DuckDB 或其他 optional/external runtime 只有在实际依赖可用并有运行输出时才可标记 live validation `done`；mock/compile/code presence 只能证明实现或接口测试，不能替代真实运行证据。
12. **手动提交边界：** 与比赛提交有关的外部写操作（GOAI portal 打开/填写/上传/最终提交、确认截图/邮件获取等）默认由用户手动完成。AI 只负责本地准备、校验、打包与说明；除非用户针对某个具体外部动作另行明确授权，否则不得主动访问 Gmail、提交平台或执行其他外部写操作。
13. **GOAI 手册对齐规则：** competition-facing 计划、PPT、README、Demo 与评测优先按官方 Boundless Agents 手册的行业场景价值、Agent 闭环、产品体验、技术深度、安全合规、开放复用六维度审查；计划中出现的新能力不等于已实现。
14. **Implemented vs Blueprint：** RBAC、PII masking、retention、document RAG 等生产能力只有在存在代码/测试/运行证据时才可标 implemented；否则必须写为 planned / production blueprint。
15. **Competition evidence rule：** 主 PPT / Demo 中的 UI、trace、Evidence、Verifier、benchmark/baseline 结果必须来源于真实运行或可复现实验；不得用手工 mock、猜测 baseline 或未经执行的 live-provider 结果替代。
16. **单一进度真源规则：** `My_Blog/docs/PROJFITZGERALD_PROGRESS.md` 是 Project Fitzgerald / FitzSight 唯一独立进度真源；不得创建或维护 `*_VALIDATED.md`、副本 tracker 或其他并行状态文件作为第二真源。DuckDB 等 runtime validation 直接记录在本文件的任务 evidence、summary 与更新日志中。

<!-- TRACKER_DATA_START -->
```json
{
  "project": {
    "name": "Project Fitzgerald / FitzSight",
    "subtitle": "Financial Operations Intelligence Agent",
    "track": "GOAI 2026 · Boundless Agents · AI+金融",
    "northStar": "让 Brokerage / FinTech Operations Analyst 针对获客、FTD 转化与客户资金流异常提出“为什么这个指标变了？”，由 Agent 在受限权限下自主完成调查、统计验证与证据化解释，最终业务决策保留给人。",
    "phase": "FitzSight v0.11.0 published / GOAI handbook re-audit complete / v0.12 GOAI Alignment & Evaluation Upgrade planned",
    "priority": "P0",
    "lastUpdated": "2026-08-12",
    "sourceVersion": "FitzSight v0.11.0 published · AplusNeutrino/FitzSight main 272dc3d5dc180bced000bcac289358dba12fdd08 · DuckDB deployment runtime already validated · 2026-08-12 GOAI Boundless Agents handbook re-audit",
    "primaryPersona": "Brokerage / FinTech Operations Analyst",
    "positioning": "Evidence-grounded investigation Agent for acquisition, FTD conversion, client-fund-flow and related financial-operations anomalies",
    "tagline": "Autonomous investigation. Human decision."
  },
  "summary": {
    "verifiedDone": 63,
    "inProgress": 7,
    "todo": 11,
    "blocked": 0,
    "note": "FitzSight v0.11.0 is verified as published on main commit 272dc3d5. The 2026-08-12 official GOAI Boundless Agents handbook re-audit does not roll back existing implementation evidence: 79 tests collected / 78 passed / 1 skipped, compileall PASS, 5/5 deterministic benchmark PASS, 8/8 adversarial PASS, DuckDB deployment runtime already validated, and the final-machine/local/offline handoff remains intact. The re-audit adds a new v0.12 GOAI Alignment & Evaluation Upgrade milestone rather than pretending planned capabilities already exist. Priority gaps are: a narrower Brokerage/FinTech Operations Analyst persona, one flagship bounded-adaptive CRM/FTD investigation, real product-process UI/trace/evidence presentation, holdout + ablation Evaluation v2, lightweight document evidence for the finance “资料理解” criterion, enterprise deployment governance as an explicit blueprint, and consistent “Autonomous investigation. Human decision.” wording. Existing seven external/runtime/human items remain evidence-gated; portal/email submission remains user-manual only."
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
      "date": "2026-08-12 → 2026-08-16",
      "status": "in_progress",
      "goal": "以官方 Boundless Agents 手册的行业场景价值 25% / Agent 能力与任务闭环 25% / 产品体验与 Demo 20% / 技术实现深度 15% / 安全合规与可追溯 10% / 开放复用 5% 为直接优化目标，在不扩大核心 intent 的前提下补齐定位、旗舰 Agent Journey、真实产品过程证据与 Evaluation v2。",
      "items": [
        {
          "id": "V12-01",
          "title": "GOAI 官方手册重审与 gap matrix",
          "status": "done",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "2026-08-12 依据用户提供的《GOAI 无界应用｜Boundless Agents 参赛手册》§1.3、§5、§8、§9、§10 与附录 C 完成重审；本进度真源记录新增缺口：primary persona 过宽、Agent 动态调查展示不足、PPT 偏结果而非过程、5/5 自建 benchmark 缺少 holdout/ablation 证据、金融“资料理解”展示偏弱、enterprise deployment boundary 与 decision-support 文案需统一。本项只证明审查/规划完成，不把任何尚未实现能力视为 done。"
        },
        {
          "id": "V12-02",
          "title": "Primary persona / beachhead market 定位冻结",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "",
          "dod": "competition-facing README / Project Summary / Pitch / Master Plan 统一以 Brokerage / FinTech Operations Analyst 为 primary persona，Regional Operations / Sales Operations Manager 为 secondary user；主业务链明确为 acquisition → FTD conversion → client-fund flows。"
        },
        {
          "id": "V12-03",
          "title": "Flagship CRM/FTD bounded-adaptive Agent Journey",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "",
          "dod": "以 CRM/FTD 作为 hero workflow，展示 question → bounded plan → contribution drilldown → latency/statistics → event/document evidence → verifier → answer → follow-up；至少包含 insufficient-evidence 或 tool-failure 分支。后续步骤可由工具结果决定，但所有动作仍必须来自 approved action catalog，禁止 unrestricted SQL/tool autonomy。"
        },
        {
          "id": "V12-04",
          "title": "真实 UI / trace / Evidence / Verifier 视觉证据进入主叙事",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "",
          "dod": "主 PPT / Demo 至少展示一张来自真实 verified run 的产品界面或等价截图，可见用户输入、Agent plan/trace、tool/evidence IDs、verifier status、最终 answer/guardrail；禁止以手工 mock 代替运行证据。"
        },
        {
          "id": "V12-05",
          "title": "Pitch 重构：1 个 hero investigation + 1 个 refusal case",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "",
          "dod": "主 deck 不再连续平铺 5 个结果型案例；CRM/FTD 作为完整产品/Agent hero，false-correlation 作为“知道什么时候不能证明”的 trust case；Net Deposit 作为 breadth proof，Customer Intelligence / Marketing 移入 appendix。"
        },
        {
          "id": "V12-06",
          "title": "Evaluation v2：holdout seeds + question paraphrase robustness",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "",
          "dod": "在不增加大量业务场景的前提下，对至少 hero/refusal 场景使用未参与当前固定 benchmark 展示的 seed / anomaly magnitude / question paraphrase 进行 holdout 测试；报告 intent routing stability、root-cause/support status、evidence coverage、refusal correctness，并明确 benchmark 构造方式与适用范围。"
        },
        {
          "id": "V12-07",
          "title": "Evaluation v2：architecture ablation / baseline harness",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "",
          "dod": "形成可复现实验协议，比较至少 Full FitzSight 与去除关键 verifier/evidence gate 的受控 ablation，量化 evidence coverage、unsupported causal claim、unsafe answer/refusal 与 verifier violations。Generic LLM / LLM+SQL baseline 只有在用户显式 opt-in、真实 provider 可用且协议公平时才运行；无真实调用不得填充或推断结果。"
        },
        {
          "id": "V12-08",
          "title": "轻量级金融资料理解 / Document Evidence",
          "status": "todo",
          "priority": "P1",
          "updated": "2026-08-12",
          "evidence": "",
          "dod": "使用 synthetic operational documents（如 KPI definition、CRM routing change ticket、operations policy / incident note）补充 structured-data investigation；文档来源/段落 ID 进入 Evidence Registry 并可被 verifier 引用。不为打勾而宣称未实现的大型 RAG / vector database。"
        },
        {
          "id": "V12-09",
          "title": "Enterprise Deployment Boundary 蓝图",
          "status": "todo",
          "priority": "P1",
          "updated": "2026-08-12",
          "evidence": "",
          "dod": "新增 production blueprint：identity/RBAC → row/field policy & PII masking → read-only semantic/data layer → FitzSight → evidence/audit log → human analyst；明确当前 PoC 为 synthetic/read-only，RBAC/retention/PII controls 属生产部署要求，不得写成当前已实现。"
        },
        {
          "id": "V12-10",
          "title": "Decision-support / autonomy 文案一致性清理",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "",
          "dod": "所有维护中材料把 Question → Data → Analysis → Evidence → Decision 统一改为 Decision Support / Human Decision；统一使用“Autonomous investigation. Human decision.”或等价表述，不得暗示 FitzSight 自动作出投资、AML、信贷、适当性或其他高风险专业决策。"
        },
        {
          "id": "V12-11",
          "title": "比赛文档全链路同步",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "",
          "dod": "MASTER_PLAN、README、INITIAL_ROUND_PROJECT_SUMMARY、PITCH_DECK_CONTENT、Architecture/Compliance/Demo/Operator docs 与最终 PPT/PDF 对 persona、hero flow、evaluation、safety wording 和当前 runtime evidence 保持一致；历史 release artifact 可保留历史状态。"
        },
        {
          "id": "V12-12",
          "title": "GOAI handbook final reviewer gate",
          "status": "todo",
          "priority": "P0",
          "updated": "2026-08-12",
          "evidence": "",
          "dod": "发布 v0.12 前逐项核验官方手册：目标用户/痛点/任务闭环、Agent planning/tool/result/verification、真实 Demo 过程、失败/不确定分支、数据来源与模拟逻辑、金融行业边界、第三方依赖、运行/部署/测试证据、PPT/视频/仓库一致性；任何未实现项必须标 planned/blueprint，不得包装为已完成。"
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
      "mitigation": "官方规则以官网/组委会通知为准；用户自行关注官方群/邮件。AI 仅在用户明确要求时查询公开网页，不默认访问 Gmail 或执行外部账户操作。"
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
      "mitigation": "每次向用户交付代码包时，必须在同一个 ZIP 中附带唯一进度真源 PROJFITZGERALD_PROGRESS.md；DuckDB/live/runtime 等验证状态直接写入该文件，不维护第二 tracker。"
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
      "title": "Primary persona / first-use scenario 过宽导致行业价值被稀释",
      "mitigation": "v0.12 统一 primary persona 为 Brokerage / FinTech Operations Analyst；主故事聚焦 acquisition→FTD→client-fund-flow investigation，其他 workflow 作为 breadth/appendix。"
    },
    {
      "id": "RK-17",
      "level": "high",
      "title": "评委将 FitzSight 视为固定 analytics pipeline 而非 Agent",
      "mitigation": "展示 bounded conditional investigation、follow-up 与 failure/insufficient-evidence branch；允许工具结果决定下一批准动作，但继续禁止 arbitrary SQL/tool parameters。"
    },
    {
      "id": "RK-18",
      "level": "high",
      "title": "PPT 展示最终分析结果多，真实产品过程证据不足",
      "mitigation": "主 deck 以真实 verified UI/trace/Evidence/Verifier 截图或等价运行证据为主，明确用户如何开始、Agent 如何推进、失败如何处理、结果如何追溯。"
    },
    {
      "id": "RK-19",
      "level": "high",
      "title": "自建 synthetic benchmark 的 5/5 / 100% 指标可信度被质疑",
      "mitigation": "Evaluation v2 增加 holdout seed/paraphrase robustness 与 architecture ablation；公开 benchmark 构造/ground-truth 定义；Generic LLM baseline 只在真实公平实验后报告。"
    },
    {
      "id": "RK-20",
      "level": "medium",
      "title": "AI+金融专项“资料理解”展示相对薄弱",
      "mitigation": "以 synthetic incident ticket / KPI definition / operations policy 增加 lightweight Document Evidence，source paragraph 进入 Evidence Registry；不虚构未实现 RAG 能力。"
    },
    {
      "id": "RK-21",
      "level": "medium",
      "title": "Decision / autonomous 营销语言与金融辅助决策边界冲突",
      "mitigation": "competition-facing language 统一为 Decision Support / Human Decision；核心口号固定为 Autonomous investigation. Human decision."
    },
    {
      "id": "RK-22",
      "level": "medium",
      "title": "Enterprise RBAC / PII / retention 蓝图被误解为当前已实现",
      "mitigation": "生产部署治理能力仅以 blueprint 标注；当前 implemented claims 继续限定为 synthetic data、read-only analytical path、Evidence/audit boundary 与现有 verifier。"
    }
  ],
  "unknowns": [
    "初赛 PPT 页数 / 文件大小 / 模板限制（手册未给具体上限，最终以 portal / 组委会通知为准）",
    "Demo 视频时长 / 文件大小 / 上传格式（手册未给具体上限）",
    "初赛 portal 是否提供独立 repo / Demo URL / supplementary material 字段",
    "复赛在线体验 / 本地部署的具体平台、账号与现场验收环境",
    "复赛 / 决赛现场网络、依赖安装与测试环境限制",
    "决赛路演与专家问答精确时长",
    "交通住宿报销标准",
    "官方评委名单",
    "指定技术 / 模型合作资源及申请规则"
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
    "D-038 v0.12 定位为 GOAI Alignment & Evaluation Upgrade：不新增无明确评分收益的核心 intent，优先优化官方手册权重最高的行业场景价值、Agent 闭环与产品 Demo。",
    "D-039 Primary persona 固定为 Brokerage / FinTech Operations Analyst；Regional Operations / Sales Operations Manager 为 secondary user；hero business chain 为 acquisition → FTD conversion → client-fund flows。",
    "D-040 Main competition story 采用 1 hero + 1 refusal：CRM/FTD 展示完整调查闭环，false-correlation 展示证据不足时拒绝因果结论；其他 workflow 作为 breadth proof / appendix。",
    "D-041 Agent 升级只允许 bounded adaptivity：工具结果可决定下一 approved action / branch，但 planner 继续不能生成任意 SQL、任意 tool parameters 或高风险金融动作。",
    "D-042 Evaluation v2 优先 holdout seed/paraphrase robustness 与 architecture ablation，而不是继续增加场景数量；Generic LLM baseline 必须基于真实、可复现、公平的 live-provider 实验，未运行不得报告结果。",
    "D-043 金融“资料理解”采用 lightweight Document Evidence：synthetic operational ticket / KPI definition / policy 文档可进入 Evidence Registry 并绑定 source paragraph；不为比赛形式化堆叠大型 RAG。",
    "D-044 Enterprise Deployment Boundary 作为 production blueprint：RBAC、row/field policy、PII masking、retention 等未实现治理能力必须明确标 planned，不得与当前 PoC implemented claims 混淆。",
    "D-045 Competition language 统一为 Decision Support / Human Decision；推荐 tagline：Autonomous investigation. Human decision.；不得使用会暗示自动高风险金融决策的表述。",
    "D-046 主 PPT / Demo 必须展示真实运行过程证据：UI、plan/trace、tool/evidence、verifier、failure/guardrail；手工 mock 不得替代运行证据。",
    "D-047 v0.12 的 GOAI 对齐工作不改变 D-033 手动提交边界：GOAI portal / Gmail / final submit / confirmation 仍由用户手动完成，除非用户对具体外部动作另行明确授权。",
    "D-048 Project Fitzgerald / FitzSight 的唯一独立进度真源保持为 My_Blog/docs/PROJFITZGERALD_PROGRESS.md；DuckDB validation 作为该文件中的 runtime evidence 记录，不单独建立 *_VALIDATED.md 或其他并行 tracker。"
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

## 当前实现基线（v0.11 已发布 / v0.12 规划重审）

- 正式产品名：**FitzSight**
- 当前公开实现仓库：`AplusNeutrino/FitzSight`
- 2026-08-12 已核验公开 `main`：commit `272dc3d5dc180bced000bcac289358dba12fdd08`，message `Release FitzSight v0.11.0`
- DuckDB deployment runtime：已验证，T3 保持 `done`
- v0.11 Build tests：`79 tests collected`；完整非重叠分组汇总 `78 passed, 1 skipped`；唯一 skip 为 build sandbox DuckDB-specific integration；既有 deployment runtime 证据不因此回退
- Compile：`PASS`
- Deterministic benchmark：`5/5 PASS`
- Adversarial release gate：`8/8 PASS`
- root-cause scenario accuracy / false-correlation rejection / mean evidence coverage：当前固定 benchmark 均 `100%`
- verifier violations：`0`
- Final Machine Kit clean extraction：`local_core_ready=true`；deterministic Agent final status `verified`；submission preflight `PASS`
- Streamlit build-environment live validation：仍未完成，E1/R3 保持 `in_progress`
- OpenAI live planner：explicit opt-in only；无真实 provider call 证据，T4/F5 保持 `in_progress`
- GOAI portal / Gmail / final submit / confirmation：**user-manual only**
- **本次 2026-08-12 更新只完成官方手册重审、计划重构与 tracker 更新；没有把 v0.12 新能力提前标为 implemented。**

## GOAI 官方手册重审结论（2026-08-12）

官方 Boundless Agents 初赛/跨阶段要求与评审重点对 FitzSight 的直接影响：

| 官方维度 | 权重 | 当前 FitzSight 证据 | 重审后的主要缺口 | v0.12 处理 |
|---|---:|---|---|---|
| 行业场景价值 | 25% | 金融运营 KPI 异常调查真实、已有 5 个 synthetic workflows | primary user 过宽，首个强需求岗位与业务链不够锋利 | 固定 Brokerage / FinTech Operations Analyst；主业务链 acquisition → FTD → client-fund flows |
| Agent 能力与任务闭环 | 25% | constrained planner → deterministic tools → Evidence Registry → Verifier | 当前材料更像安全 workflow，bounded dynamic investigation / follow-up / failure branch 展示不足 | CRM/FTD hero journey 加 conditional drilldown、follow-up、insufficient-evidence/tool-failure branch |
| 产品体验与 Demo | 20% | Streamlit presenter、offline HTML/video、trace/evidence cards 已有 | 主 PPT 目前平铺多个最终结果，真实产品过程视觉证据不足 | 1 hero + 1 refusal；真实 UI/trace/evidence/verifier 进入主叙事 |
| 技术实现深度 | 15% | read-only SQL/Python、statistics、decomposition、verifier、DuckDB、tests | 技术不是当前首要短板 | 保持架构，不为“更 Agent”放开 SQL/tool 权限 |
| 安全、合规、可追溯 | 10% | synthetic-only、fail closed、causal guardrail、no high-impact actions | competition wording 中 Decision/autonomous 需完全一致；production governance 需说明 | “Autonomous investigation. Human decision.”；enterprise boundary 明确 blueprint |
| 开放 / 复用 | 5% | public repo、MIT、synthetic generator、tests、docs、portable kit | 可进一步说明如何迁移为金融运营调查模板 | 在文档中补配置/迁移边界，不扩新核心 framework |

金融赛题专项强调“资料理解、依据追溯、风险提示、合规意识、避免越权决策”。FitzSight 后四项较强；v0.12 只补一个轻量、可验证的 synthetic operational-document evidence path，不为了形式完整而临时堆叠大型 RAG。

官方手册已明确并从 `unknowns` 移除的事项：
- 团队可个人参赛；组队人数不超过 3 人；
- 初赛作品简介为 500 字以内；
- 初赛方案 PPT/PDF 必交，Demo/原型与代码包可选；
- 复赛起 Demo、代码/等价工程材料、数据来源与合规说明进入必交范围；
- 开源并非初赛强制，但复赛/决赛需评审可访问的代码或等价工程材料；
- 模拟数据允许，但必须说明模拟逻辑、字段含义和适用边界。

## v0.12 — GOAI Alignment & Evaluation Upgrade

P0 顺序：

1. **定位冻结**：Primary persona 改为 Brokerage / FinTech Operations Analyst；secondary user 保留 Regional Operations / Sales Operations Manager；五个 workflow 不再等权展示。
2. **Hero Agent Journey**：以 CRM/FTD 为唯一旗舰调查，加入 bounded conditional drilldown、follow-up 与 failure/insufficient-evidence branch；绝不改成 unrestricted SQL Agent。
3. **产品证据进入主 deck**：主 PPT 展示真实 UI / Agent plan / tool execution / Evidence ID / Verifier / final guardrail，证明系统“如何运行”而不只展示最终数字。
4. **叙事压缩为 1+1**：CRM/FTD = investigation hero；False Correlation = refusal/trust hero；Net Deposit = breadth proof；Customer Intelligence / Marketing = appendix。
5. **Evaluation v2**：优先 holdout seeds / anomaly magnitude / question paraphrases + architecture ablation，回答“这套 architecture 为什么有效”，而不是把 5 个场景简单扩成更多场景。
6. **金融资料理解补强**：只增加轻量 synthetic document evidence（KPI definition / routing ticket / operations policy / incident note）与 source-paragraph Evidence；不虚构大型 RAG。
7. **Enterprise deployment blueprint**：RBAC、row/field policy、PII masking、retention、audit 只作为生产部署边界说明；未实现部分明确标 planned。
8. **语言统一**：`Question → Data → Analysis → Evidence → Decision Support`；推荐 tagline：`Autonomous investigation. Human decision.`
9. **全仓库比赛文档同步**：MASTER_PLAN / README / Project Summary / Pitch / Architecture / Compliance / Demo / Operator assets 对齐同一 persona、hero story、evaluation 和 safety wording。
10. **最终 handbook reviewer gate**：逐项核验官方要求及附录 Demo checklist，确保 PPT、视频、仓库、说明文档和现场展示一致。

保持不变的边界：
- 不新增无明确评分收益的第六个核心 intent；
- 不为了“多轮/Agent”表现而允许 LLM 生成任意 SQL 或任意 tool arguments；
- 不把 synthetic benchmark 说成真实客户效果；
- 不把 enterprise blueprint 说成已实现 production control；
- 不在未实际调用前报告 Generic LLM/OpenAI baseline、token cost 或 provider latency；
- GOAI portal / Gmail / final submit / confirmation 仍由用户手动完成。

## 仍需外部 / 人工证据的既有任务

1. 最终演示机器 Streamlit live health-check：成功后关闭 E1，并完成 R3 的 Live/local/video 三套闭环。
2. OpenAI planner 继续可选：只有用户显式 opt-in + 稳定 credential/model + 真实运行输出后才能关闭 T4；对应 live-provider latency/token/cost 才能更新 F5。
3. GOAI portal review/upload/final submit/confirmation：G6 继续 `owner=user_manual` / `manual_only`。
4. 用户真实完成人工 pitch/demo/Q&A rehearsal 后，才可关闭 R4/R5。
5. v0.12 文档/代码工作不得用任何上述外部任务“尚未完成”作为理由虚构验证结果。

## 更新日志

- 2026-08-12：纠正进度真源文件名误记。确认 `AplusNeutrino/My_Blog/docs/PROJFITZGERALD_PROGRESS.md` 继续作为 Project Fitzgerald / FitzSight 的唯一、独立进度真源，并由 `/projfitzgerald/` 追踪页读取。先前提及的 `*_DUCKDB_VALIDATED.md` 不再作为规划文件或第二 tracker；DuckDB runtime validation 继续作为本文件中的既有 evidence 保留。本次仅纠正真源约定，不改变 v0.11/v0.12 任务完成状态或验证计数。


- 2026-08-12：依据官方《GOAI 无界应用｜Boundless Agents 参赛手册》与既有 v0.11 实现证据完成一次 competition-alignment 重审。确认当前最大缺口不在核心技术，而在 primary persona、Agent 动态调查展示、真实产品过程、benchmark 泛化/ablation 可信度、金融资料理解与 enterprise deployment boundary。新增 M7 / V12-01→V12-12；V12-01（手册重审与 gap matrix）有本文件作为证据标 `done`，其余 11 项保持 `todo`，不提前宣称实现。总计更新为 63 done / 7 in_progress / 11 todo / 0 blocked。同时统一后续方向为“Autonomous investigation. Human decision.”，并保留 user-manual-only submission boundary。


- 2026-08-12：FitzSight v0.11 完成 final-machine operations：新增 portable Final Machine Kit、Windows/POSIX launchers、one-command final_machine_check、explicit-opt-in OpenAI validation boundary、rehearsal timing recorder/plan/operator card；79 tests collected / 78 passed / 1 skipped；5/5 benchmark、8/8 adversarial、compileall、preflight、handoff/kit integrity 均 PASS；clean extracted kit 实跑 `local_core_ready=true` 且 deterministic Agent `verified`；剩余 7 项全部保持 external/runtime/human evidence-gated。

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
