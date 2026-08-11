# Project Fitzgerald / FinSight 进度真源

> 本文件是 `/projfitzgerald` 项目追踪页的唯一数据源。页面会直接读取下方 `TRACKER_DATA` JSON。后续让 AI 更新进度时，只修改本文件；不要直接在网页文件中复制或维护任务状态。

## AI 更新规则

1. 只在有代码、文件、测试、截图或提交记录等证据时，将任务设为 `done`；仅在主计划中出现不等于已完成。
2. 已开始但未满足 Definition of Done 的任务设为 `in_progress`，否则保持 `todo`；明确延期的任务设为 `blocked`。
3. 更新任务时同步维护 `updated`、`evidence`、顶部 `last_updated`、`summary` 和文末更新日志。
4. 新任务必须保留唯一 `id`，并归入现有阶段；范围变更需同时记录到 `decisions`。
5. 所有核心功能必须满足：可运行、尽量有确定性测试、处理失败状态、输出可见、证据已记录、文档已更新、无 secrets、可从干净环境演示。

<!-- TRACKER_DATA_START -->
```json
{
  "project": {
    "name": "Project Fitzgerald / FinSight",
    "subtitle": "Financial Operations Intelligence Agent",
    "track": "GOAI 2026 · Boundless Agents · AI+金融",
    "northStar": "让金融业务管理者提出‘为什么这个指标变了？’，由 Agent 自主完成数据调查、统计验证与证据化解释。",
    "phase": "初赛冲刺 / MVP 设计阶段",
    "priority": "P0",
    "lastUpdated": "2026-08-11",
    "sourceVersion": "Master Plan · 2026-08-11"
  },
  "summary": {
    "verifiedDone": 8,
    "inProgress": 0,
    "todo": 51,
    "blocked": 0,
    "note": "完成数仅包含主计划已明确形成的规划产物；主计划中所有开发与提交复选框均未勾选。"
  },
  "milestones": [
    {
      "id": "M0",
      "title": "定义与设计",
      "date": "2026-08-11",
      "status": "in_progress",
      "goal": "冻结项目定位、范围、架构、数据设计与初赛叙事",
      "items": [
        {"id":"M0-01","title":"项目定位与赛道选择","status":"done","priority":"P0","updated":"2026-08-11","evidence":"主计划 §1.1–1.3、D-001、D-002"},
        {"id":"M0-02","title":"Problem Statement","status":"done","priority":"P0","updated":"2026-08-11","evidence":"主计划 §6"},
        {"id":"M0-03","title":"MVP Scope 与不做清单","status":"done","priority":"P0","updated":"2026-08-11","evidence":"主计划 §7、§40、§43"},
        {"id":"M0-04","title":"核心 Demo Scenario","status":"done","priority":"P0","updated":"2026-08-11","evidence":"主计划 §25、D-007"},
        {"id":"M0-05","title":"逻辑架构草案","status":"done","priority":"P0","updated":"2026-08-11","evidence":"主计划 §9–11"},
        {"id":"M0-06","title":"核心数据表设计","status":"done","priority":"P0","updated":"2026-08-11","evidence":"主计划 §12.3"},
        {"id":"M0-07","title":"初赛 PPT 大纲","status":"done","priority":"P0","updated":"2026-08-11","evidence":"主计划 §33"},
        {"id":"M0-08","title":"安全、合规与开源边界","status":"done","priority":"P0","updated":"2026-08-11","evidence":"主计划 §20–22、§46"},
        {"id":"M0-09","title":"创建 finsight GitHub repo","status":"todo","priority":"P0","updated":"2026-08-11","evidence":"未提供"},
        {"id":"M0-10","title":"上传 MASTER_PLAN.md","status":"todo","priority":"P0","updated":"2026-08-11","evidence":"未提供"},
        {"id":"M0-11","title":"建立最小项目目录","status":"todo","priority":"P0","updated":"2026-08-11","evidence":"未提供"}
      ]
    },
    {
      "id": "M1",
      "title": "数据与基线",
      "date": "2026-08-12",
      "status": "todo",
      "goal": "生成可复现的合成金融经营数据，并用 SQL/Python 找回 Ground Truth",
      "items": [
        {"id":"A1","title":"定义 schema","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"A2","title":"Synthetic data generator v0","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"A3","title":"生成 customers / deposits / withdrawals / sales_activity / business_events","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"A4","title":"注入 CRM Routing Change","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"A5","title":"SQL baseline analysis","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"A6","title":"手工验证 root cause","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"A7","title":"Ground truth 文件与 data dictionary","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""}
      ]
    },
    {
      "id": "M2",
      "title": "工具与分析层",
      "date": "2026-08-13",
      "status": "todo",
      "goal": "建立真实、只读、可记录证据的分析工具",
      "items": [
        {"id":"B1","title":"KPI definitions","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"B2","title":"Period comparison","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"B3","title":"Contribution analysis","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"B4","title":"Statistical tests","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"B5","title":"Anomaly detection","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"B6","title":"Customer segmentation","status":"todo","priority":"P1","updated":"2026-08-11","evidence":""},
        {"id":"D1","title":"Evidence ID 与 registry","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"D2","title":"Tool logs","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"T1","title":"Schema / SQL / KPI / comparison / statistics tools","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"T2","title":"Unit tests","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""}
      ]
    },
    {
      "id": "M3",
      "title": "Agent MVP",
      "date": "2026-08-14",
      "status": "todo",
      "goal": "跑通问题 → 调查 → 验证 → 证据化报告的最小闭环",
      "items": [
        {"id":"C1","title":"Intent understanding","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"C2","title":"Investigation plan","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"C3","title":"Tool selection 与调用","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"C4","title":"Investigation loop 与 anomaly drilldown","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"C5","title":"Verifier","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"C6","title":"Final auditable report","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"D3","title":"Claim-to-evidence mapping","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""}
      ]
    },
    {
      "id": "M4",
      "title": "演示与初赛材料",
      "date": "2026-08-15 → 2026-08-16",
      "status": "todo",
      "goal": "完成可演示 UI、PPT 与初赛提交",
      "items": [
        {"id":"E1","title":"Streamlit chat / question input","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"E2","title":"KPI cards","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"E3","title":"Investigation trace","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"E4","title":"Charts","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"E5","title":"Evidence cards 与 report","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"G1","title":"Project summary","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"G2","title":"PPT / PDF","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"G3","title":"Architecture documentation","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"G4","title":"Demo recording","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"G5","title":"README（含 limitations）","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"G6","title":"提交、截图、邮件确认与备份 PDF","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""},
        {"id":"G7","title":"Secrets、license、repo visibility 检查","status":"todo","priority":"P0","updated":"2026-08-11","evidence":""}
      ]
    },
    {
      "id": "M5",
      "title": "评审等待期强化",
      "date": "2026-08-17 → 2026-08-24",
      "status": "todo",
      "goal": "从一个可运行 Demo 扩展为可评估、可复现系统",
      "items": [
        {"id":"F1","title":"5 synthetic scenarios 与 benchmark schema","status":"todo","priority":"P1","updated":"2026-08-11","evidence":""},
        {"id":"F2","title":"Root cause scoring","status":"todo","priority":"P1","updated":"2026-08-11","evidence":""},
        {"id":"F3","title":"Evidence coverage scoring","status":"todo","priority":"P1","updated":"2026-08-11","evidence":""},
        {"id":"F4","title":"Hallucination / overclaim scoring","status":"todo","priority":"P1","updated":"2026-08-11","evidence":""},
        {"id":"F5","title":"Latency / cost measurement","status":"todo","priority":"P1","updated":"2026-08-11","evidence":""},
        {"id":"F6","title":"Test suite 与 evaluation harness","status":"todo","priority":"P1","updated":"2026-08-11","evidence":""},
        {"id":"F7","title":"UI、视频与部署脚本优化","status":"todo","priority":"P1","updated":"2026-08-11","evidence":""}
      ]
    },
    {
      "id": "M6",
      "title": "复赛与决赛准备",
      "date": "2026-08-25 → 2026-09-22",
      "status": "todo",
      "goal": "陌生评委可一键运行；现场 Demo 稳定并有双重备份",
      "items": [
        {"id":"R1","title":"One-command startup 与 .env.example","status":"todo","priority":"P1","updated":"2026-08-11","evidence":""},
        {"id":"R2","title":"Benchmark results 与完整 compliance explanation","status":"todo","priority":"P1","updated":"2026-08-11","evidence":""},
        {"id":"R3","title":"Live / local / video 三套 Demo","status":"todo","priority":"P2","updated":"2026-08-11","evidence":""},
        {"id":"R4","title":"5–8 分钟路演与 <3 分钟演示","status":"todo","priority":"P2","updated":"2026-08-11","evidence":""},
        {"id":"R5","title":"Q&A、稳定性与 business story","status":"todo","priority":"P2","updated":"2026-08-11","evidence":""}
      ]
    }
  ],
  "risks": [
    {"id":"RK-01","level":"high","title":"时间极紧","mitigation":"只做最小可信闭环，P0 优先"},
    {"id":"RK-02","level":"high","title":"Demo 能跑但证据不足","mitigation":"所有 numeric claims 绑定 tool evidence"},
    {"id":"RK-03","level":"high","title":"数据与职业合规","mitigation":"只用 synthetic data；禁止真实 PII 与雇主信息"},
    {"id":"RK-04","level":"medium","title":"范围膨胀","mitigation":"按 §43 五问过滤新功能"},
    {"id":"RK-05","level":"medium","title":"官方规则更新","mitigation":"每日检查官网、官方群与邮件"},
    {"id":"RK-06","level":"medium","title":"现场 Demo 失败","mitigation":"Live、local、video 三套预案"}
  ],
  "unknowns": [
    "团队人数最终限制","初赛 PPT 页数/大小限制","项目简介字符限制","是否必须 public repo","Demo 视频长度",
    "决赛路演与答辩时长","交通住宿报销标准","官方评委名单","Boundless handbook","指定技术/模型合作资源"
  ],
  "decisions": [
    "D-001 选择 Boundless Agents","D-002 选择 AI+金融","D-003 不做股票投资 Agent",
    "D-004 Synthetic Data First","D-005 Evidence First","D-006 Agent 数量服从任务","D-007 MVP 聚焦 Anomaly Investigation"
  ]
}
```
<!-- TRACKER_DATA_END -->

## 状态口径

| 状态 | 含义 |
|---|---|
| `done` | 有明确交付物或主计划已形成可引用的规划产物 |
| `in_progress` | 已开始，但尚未达到 Definition of Done |
| `todo` | 尚无开始证据 |
| `blocked` | 已开始但被明确外部条件阻塞 |

## 更新日志

- 2026-08-11：依据 Master Plan 建立初始追踪基线；规划产物 8 项完成，工程与提交任务均保持未完成。
