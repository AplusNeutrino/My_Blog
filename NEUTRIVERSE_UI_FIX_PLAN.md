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
| UI-003 | P2 | 390/768px截图顶栏显示内部布局名 Neutriverse-section / Neutriverse-project，而不是页面标题 | done | 120项production与120项部署后live场景、32张viewport、标题/tooltip/控件不重叠门禁通过；移动双主题截图复验 |
| UI-003a | P2 | 快速关闭移动菜单时延迟焦点可能回到已关闭侧栏；390px mask焦点门禁超时 | done | production及live390/768双主题各3次快速mask关闭、跨两帧焦点保持在trigger；原mask/Escape门禁通过 |
| UI-004 | P1 | 1024/1366×900窗口的实际viewport截图显示侧栏DISCOVER检索组与社交/主题组重叠 | done | production及live14短/高窗口场景无重叠、按钮hit-test/主题/搜索通过；人工查看本次live截图 |

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

UI-A05检查进行中：base93825c66/run38541205915 success；Tags/Archive/Thoughts独立页+THINK内Series目录32双主题四宽度截图及往返操作。Tags桌面首屏与长标签详情跳转已实际检查，尚未确认新缺陷；不猜测改样式。工作分支新增检查pending，其他页面矩阵仍保留pending。

UI-004/UI-003a已验收：head8415050ddd200f51c471b84e0011e3d46260a305的[main run38540154437](https://github.com/AplusNeutrino/My_Blog/actions/runs/38540154437) build/deploy/verify-live-ui均success。205 tests、保护/authoring/Jekyll/原门禁、production120+14与live120+14通过；查看本次live14张联系表，放大1024×900 Light原图，侧栏检索/主题分开且可操作。live移动两宽度两主题各3次快速mask关闭及跨两帧焦点断言通过。证据artifact11882032589及永久JSON/联系表。上次live失败未隐藏；只稳定每次点击起点，仍保留快速open→mask操作。下一项独立检查Series/Tags/Archive/Thoughts四视口双主题；全站矩阵仍IN PROGRESS，无新增待答问题。

2026-10-14接续：base main787a4a61，run38535247898 build/deploy success，但verify-live-ui快速mask关闭焦点wait失败。UI-003a/UI-004仍validation-pending。本轮仅诊断/修正审计起始点击时序，补失败状态截图，不放宽断言、不推测改产品；下轮/本轮以修正后的精确head重新核对production+live。其他独立页矩阵未冒称完成。

UI-004接续：实现与审计head ba75465277be11c48c7f4242138842a88effc953，工作分支run38534716282 success；205 tests、T01/authoring/Jekyll/全部旧门禁、120场景与14短/高窗口专项通过。a93f494f在main的run38534120830因新脚本焦点/滚动时序失败，未部署；ba754652补等待焦点完成后滚动，没有放宽断言。将修复与此状态记录非强推提交main，UI-004/UI-003a均validation-pending；下轮先核对该main head的build/deploy/verify-live-ui和同场景截图，再继续独立页面矩阵。[前后证据](docs/ui-evidence/ui004-comparison.md)。无新增待答问题。

2026-10-14 UI-004：base 7d376af1f05329dca43861c47c4dde83ded20786，run38526904330 success已核对。先记录范围：共享侧栏CSS、短窗口几何/指针/截图回归、UI-003a快速mask关闭专项、计划日志。已查看上一head线上1024px BUILD Night截图确认重叠；桌面1363×936测量nav flex-shrink=1/min-height=0，其children不随压缩而缩小。保留组高度，让容器滚动，不改变内容/尺寸风格。先工作分支验证；尚未部署验收。

UI-003已部署并验收：实现head e020fb73e9de4fcd91732c2bc7e281575f3395af；[main run38526220139](https://github.com/AplusNeutrino/My_Blog/actions/runs/38526220139) build/deploy/verify-live-ui success。UI-003a保护代码已部署、原production菜单焦点门禁通过，但快速mask关闭的同场景线上焦点专项检查仍validation-pending（live矩阵只操作主题菜单/Escape，不冒称mask复验）。下一项优先UI-004，并补UI-003a线上专项；其他独立页面矩阵仍pending。无待答问题。[证据与局限](docs/ui-evidence/ui003-comparison.md)。

2026-10-14 UI-003接续：main仍c12d9d2a，ui/fix-003实际head e020fb73e9de4fcd91732c2bc7e281575f3395af，run38509991407 build success（deploy/live按工作分支规则skipped）。下载artifact11869786736，120项标题/控件/溢出/圆角/noindex与16组交互通过，人工查看32张viewport联系表。非强推main至同一head后run38526220139正在build/deploy/live验证；未标done。下一优先UI-004；全页截图侧栏裁切疑点被viewport/rect澄清，不修改其开闭transform。

2026-10-14 UI-003：base c12d9d2ac262e924ce800f7e303f59279a0e9741，run38506420729 success已核对。范围：topbar模板、必要溢出样式、回归与浏览器标题/控件/viewport截图证据、计划/日志。只修复自定义公开section/project布局的顶栏名称；其他布局保留Chirpy行为。先工作分支验收，再核对main部署。侧栏疑点只复核，不凭全页合成截图改样式。

2026-10-14 UI-002 / UI-A02：base = bc3efad53188f1ff86ae5b49d5a159a136643792；工作分支验证后main非强推至4d7eac959d1448cbdeb490aebf11e1a79a7b66d4；[run38505942304](https://github.com/AplusNeutrino/My_Blog/actions/runs/38505942304) build/deploy success，双主题线上复验通过，UI-002 done。[证据与局限](docs/ui-evidence/ui002-comparison.md)。下一项UI-003移动顶栏名称，先核实侧栏截图疑点；不将此局部审计当全站COMPLETE。无新增待答问题。

UI-001 done；base = dd2e52ee17322519190fdacf1a12e5d35f035ead；最终实现head = 0348b33c7e00a5f4584181c8d7244da88fc50244；[run38500122266](https://github.com/AplusNeutrino/My_Blog/actions/runs/38500122266) build/deploy成功；无待答问题。下一项：THINK筛选/分页/阅读区与BUILD列表/七详情全页视觉检查，继续补矩阵，不把导航截图当全站通过。

UI-001证据：[前后对照](docs/ui-evidence/ui001-comparison.md)，40项几何JSON与两主题线上截图持久保存。必要CI修复包含推荐预期模块/3项测试、viewport截图与CJK字体；内容/数据/URL未改。
