# Neutriverse UI 修复计划

状态：IN PROGRESS。独立于已 COMPLETE 的 T00–T39 重构；不改写历史验收。
启动日期：2026-10-14。仓库：AplusNeutrino/My_Blog。

## 范围与保护

只修复已实际复现的显示/交互缺陷；不借审美偏好重新设计。保留 Night / Prospero Light、四入口英文与中文说明、Jekyll/Pages、旧 URL、正文和 metadata、hidden/noindex、Gate/NAVI/旅行隐蔽边界、七项目且排除 MMXProj。不修改外部项目仓库或从聊天补入个人信息。

## 流程与验收

每轮先读 main/head、AGENTS/domain/ADR、本计划与日志；记录问题 ID、base、范围、复现、验收后实现。通过的小交付非强推提交 main，半成品留工作分支。精确实现 head 的 CI/build/deploy 与部署后同场景截图都通过才标 done；未完成验证保持 validation-pending。问题需通过 gh 跟踪；gh 不可用时在日志准确记录，不编造 Issue。

截图人工检查与自动几何/交互检查分别记证；通过测试不等于视觉正常。已有内容保护、authoring、Search/feed、SEO、资源、移动/无障碍门禁保留。

## 问题台账

| ID | 优先级 | 已复现问题 | 状态 | 验收 |
|---|---|---|---|---|
| UI-001 | P2 | 四入口导航卡片同一行底部不齐，长中文摘要使内部链接未撑满 Grid 单元格 | done | 两主题、四视口：首页及四入口卡片边框撑满各自单元格，保留换行/链接/焦点；production CI 与线上复验 |
| UI-002 | P2 | 项目/观察组件引用未定义的圆角、阴影与等宽字体变量；圆角失效、数据文本字体回退 | done | 变量默认值与运行时圆角/字体通过，112截图/交互与旧门禁通过，精确head main部署和双主题线上复验通过 |
| UI-003 | P2 | 390/768px截图顶栏显示内部布局名 Neutriverse-section / Neutriverse-project，而不是页面标题 | in-progress | 顶栏显示当前页面语义名称，长项目名不遮挡菜单/搜索；双主题复验 |

## 检查矩阵

以下每行必须逐页覆盖 390/768/1024/1366px × Night/Light，并人工看截图与操作；扩展到320/1920px/缩放时记录实际条件。云浏览器当前1363×936，仅记该视口；其他尺寸以CI/本地浏览器证据补充。不能以五页面的既有40项门禁冒充全站检查。

| 页面组 | 视觉检查 | 交互 |
|---|---|---|
| 首页、THINK、BUILD、OBSERVE、ABOUT | 导航UI-001：40项截图与几何通过；THINK 1363px双主题已部署复验。全页检查仍pending | THINK侧栏展开/收起、双主题切换已操作；其他pending |
| THINK筛选/分页、Series、Tags、Archive、Thoughts | THINK四状态×两主题×四宽度已生成并看联系表，390px正文/控件分段放大；Series/Tags/Archive/Thoughts独立页pending | THINK筛选/刷新/返回、四视口自动交互通过；Night桌面搜索/取消实际操作；其他pending |
| BUILD列表、七个BUILD详情 | 80张两主题四宽度全页截图已生成并看联系表；长项目名与OfficeSpire原图放大；UI-002双主题线上复验通过 | BUILD筛选/刷新/返回属于16组自动交互，通过；线上详情返回/状态筛选通过；应用/外部来源链接不作本轮修改 |
| 代表文章：代码、表格、图片 | pending | 滚动/阅读/复制/媒体pending |
| Library、友链 | pending | 目录/延迟加载/链接pending |
| Ravenis、Occult Atlas | pending | 共享导航/核心控件/返回pending |
| Gate/NAVI（仅既有隐蔽边界） | pending | 不将私有截图/入口加入公开台账 |

## 集中问题队列

无新增需要用户决定的问题。未来按Q编号记录影响、选项、推荐；未回复不视为同意，继续无关任务。

## 完成条件

全部矩阵有明确截图和交互证据；所有确认缺陷完成部署复验；无validation-pending或未解释阻塞。写 docs/neutriverse-ui-fix-final-report.md，标 COMPLETE、最终main/线上核对后暂停“修复 Neutriverse UI”。不无限审美修改。

## 当前运行

2026-10-14 UI-003：base c12d9d2ac262e924ce800f7e303f59279a0e9741，run38506420729 success已核对。范围：topbar模板、必要溢出样式、回归与浏览器标题/控件/viewport截图证据、计划/日志。只修复自定义公开section/project布局的顶栏名称；其他布局保留Chirpy行为。先工作分支验收，再核对main部署。侧栏疑点只复核，不凭全页合成截图改样式。

2026-10-14 UI-002 / UI-A02：base = bc3efad53188f1ff86ae5b49d5a159a136643792；工作分支验证后main非强推至4d7eac959d1448cbdeb490aebf11e1a79a7b66d4；[run38505942304](https://github.com/AplusNeutrino/My_Blog/actions/runs/38505942304) build/deploy success，双主题线上复验通过，UI-002 done。[证据与局限](docs/ui-evidence/ui002-comparison.md)。下一项UI-003移动顶栏名称，先核实侧栏截图疑点；不将此局部审计当全站COMPLETE。无新增待答问题。

UI-001 done；base = dd2e52ee17322519190fdacf1a12e5d35f035ead；最终实现head = 0348b33c7e00a5f4584181c8d7244da88fc50244；[run38500122266](https://github.com/AplusNeutrino/My_Blog/actions/runs/38500122266) build/deploy成功；无待答问题。下一项：THINK筛选/分页/阅读区与BUILD列表/七详情全页视觉检查，继续补矩阵，不把导航截图当全站通过。

UI-001证据：[前后对照](docs/ui-evidence/ui001-comparison.md)，40项几何JSON与两主题线上截图持久保存。必要CI修复包含推荐预期模块/3项测试、viewport截图与CJK字体；内容/数据/URL未改。
