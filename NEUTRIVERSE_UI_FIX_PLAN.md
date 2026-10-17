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
| UI-016 | P2 | 390 Night线上原生图：ABOUT“友情链接”关系卡片说明右端被固定返回顶部按钮覆盖 | done | 5862ab0e同head attempt2 build/deploy/live全部success；四宽度双主题12线上关系帧/8联系表实际查看，390 Night原图对照全文无覆盖；8流程真实滚轮/返回顶部/Library友链往返通过，仅此作用域done |
| UI-015 | P2 | 390 Night实际原生图：ABOUT理念段尾字、书目日期/维护说明及OBSERVE卡片noindex状态被固定按钮覆盖 | done | c001784b精确main build/deploy/live全部success；四宽度双主题45线上目标帧/18联系表实际查看，390四原图与before对比尾字/日期/NOINDEX完整，16组真实滚轮/返回顶部/公开往返通过；仅四类作用域done |
| UI-014 | P2 | 实际390 Light OBSERVE说明段与390 Night ABOUT介绍段右端被固定返回顶部按钮覆盖 | done | d1bdcbf2精确main build/deploy/live全成功；两容器四宽度双主题32线上帧16联系表已看、原390两场景放大对比无覆盖，16流程真实返回顶部及公开往返通过；仅本作用域done |
| UI-013 | P2 | 768 Night首页精选内容右下Progressive Disclosure卡片的正文被固定返回顶部按钮覆盖，原生第5帧实际复现 | done | e437b97d精确main build/deploy/live均成功；四宽度双主题56首页线上滚动图/10联系表已看，原768 Night精选原图放大对照无文字遮挡，真实返回顶部与入口往返通过 |
| UI-012 | P2 | 390 Night首页返回顶部圆钮覆盖近期表达Z.A.T.O.卡片正文首行右端，实际原生PNG已复现 | done | e437b97d精确main build/deploy/live均成功；四宽度双主题56首页线上滚动图已看，原390 Night Z.A.T.O.原图放大对照无文字遮挡，逐行Range与返回顶部/四入口往返通过 |
| UI-011 | P2 | 1024px Light实际线上截图中返回顶部圆钮覆盖Library目录漫画计数 | done | 831f2898精确main build/deploy/live通过；四宽度双主题48线上图已人工看并放大原遮挡场景，计数完整且按钮可操作；8组逐行滚动/往返/真实返回顶部、48诊断及192+14通过 |
| UI-010 | P2 | 390px双主题评分末端提示超出可用视口，被右侧滚动条裁去尾字；旧几何错误按innerWidth验收 | done | 41dca277精确main build/deploy/live通过；四宽度双主题32线上评分图已人工看，首末提示全文可见且在clientWidth/shell内；8分类/摘要/真实键盘/退出隐藏/刷新和192+14通过 |
| UI-009 | P2 | 390px Light时间线长作品名尾部被固定返回顶部按钮遮住 | done | 8eb17637精确main部署/live通过；四宽度双主题24张首/尾/刷新线上图人工复验，24诊断真实文字行不与可见按钮相交，8时间线加载/滚动/刷新/键盘流程通过 |
| UI-008 | P2 | 390px高级筛选浮层溢出窄屏，聚焦/定位后页面横向偏移、标题左侧被裁 | done | 3a6258a2精确main部署/live通过；四宽度双主题32张四状态线上图人工复验，面板均在viewport内、scrollX=0，标题左缘完整 |
| UI-007 | P2 | Library第2页刷新后URL仍page=2但显示第1页，加载前空列表错误收缩页码 | done | 3a6258a2精确main部署/live通过；8组下一页/刷新同URL与ID/上一页、来源年份组合刷新与清除通过，32图人工复验 |
| UI-006 | P2 | 390px双主题Library搜索框覆盖副标题，绝对定位未占用布局空间 | done | ea8b62d5精确main部署/live通过；四宽度双主题24张线上三状态截图已看，8搜索流程及24矩形无重叠通过；移动搜索独占布局行 |
| UI-001 | P2 | 四入口导航卡片同一行底部不齐，长中文摘要使内部链接未撑满 Grid 单元格 | done | 两主题、四视口：首页及四入口卡片边框撑满各自单元格，保留换行/链接/焦点；production CI 与线上复验 |
| UI-002 | P2 | 项目/观察组件引用未定义的圆角、阴影与等宽字体变量；圆角失效、数据文本字体回退 | done | 变量默认值与运行时圆角/字体通过，112截图/交互与旧门禁通过，精确head main部署和双主题线上复验通过 |
| UI-003 | P2 | 390/768px截图顶栏显示内部布局名 Neutriverse-section / Neutriverse-project，而不是页面标题 | done | 120项production与120项部署后live场景、32张viewport、标题/tooltip/控件不重叠门禁通过；移动双主题截图复验 |
| UI-003a | P2 | 快速关闭移动菜单时延迟焦点可能回到已关闭侧栏；390px mask焦点门禁超时 | done | production及live390/768双主题各3次快速mask关闭、跨两帧焦点保持在trigger；原mask/Escape门禁通过 |
| UI-004 | P1 | 1024/1366×900窗口的实际viewport截图显示侧栏DISCOVER检索组与社交/主题组重叠 | done | production及live14短/高窗口场景无重叠、按钮hit-test/主题/搜索通过；人工查看本次live截图 |
| UI-005 | P1 | 计组04两张Markdown表格紧邻标题，线上渲染为连续竖线正文，失去行列结构 | done | 原md/metadata不改；4项渲染回归与T01通过；精确main部署和live四宽度双主题8截图/两table/横向阅读通过，已人工复验 |

## 检查矩阵

以下每行必须逐页覆盖 390/768/1024/1366px × Night/Light，并人工看截图与操作；扩展到320/1920px/缩放时记录实际条件。云浏览器当前1363×936，仅记该视口；其他尺寸以CI/本地浏览器证据补充。不能以五页面的既有40项门禁冒充全站检查。

| 页面组 | 视觉检查 | 交互 |
|---|---|---|
| 首页、THINK、BUILD、OBSERVE、ABOUT | 导航UI-001：40项截图与几何通过；THINK 1363px双主题已部署复验。全页检查仍pending | THINK侧栏展开/收起、双主题切换已操作；其他pending |
| THINK筛选/分页、Series、Tags、Archive、Thoughts | THINK四状态已检查；UI-A05的Series目录/Tags/Archive/Thoughts：390/768/1024/1366双主题32张生产及线上viewport已人工查看并放大代表原图，无新增确认缺陷 | THINK筛选/刷新/返回通过；UI-A05线上32组长标签/归档打开返回、Series精确筛选数量/返回、Thought稳定锚点/返回通过；点赞及其余hover/focus仍pending |
| BUILD列表、七个BUILD详情 | 80张两主题四宽度全页截图已生成并看联系表；长项目名与OfficeSpire原图放大；UI-002双主题线上复验通过 | BUILD筛选/刷新/返回属于16组自动交互，通过；线上详情返回/状态筛选通过；应用/外部来源链接不作本轮修改 |
| 代表文章：代码、表格、图片 | UI-005表格8场景及UI-A07代码/图片16场景：四宽度双主题生产/live截图已人工查看并放大代表原图，未新增确认缺陷 | 表格横向阅读、图片逐张加载、移动touch/桌面arrow翻页关闭、复制提示及UI-A07b线上实际剪贴板16场景通过；其余阅读控件pending |
| Library、友链 | UI-A08a根页/弹层/目录/友链40图、UI-A08b可见封面8图、UI-A08c1搜索24图及UI-007/008筛选32图已看；UI-009/UI-A08d时间线24图、UI-A08e排序/列表32张四宽度双主题生产/live图已人工查看 | 弹层/目录返回/友链键盘、56次可见封面加载、8组搜索、分页/来源年份/清除8流程通过；时间线8流程与24文字按钮不相交通过；UI-A08e书籍评分/年份组内降序、标题排序刷新同URL/ID、列表偏好刷新、Enter网格及默认恢复8流程线上通过；完整库存/离屏加载、Steam排序/摘置等其他控件及外部站点仍pending |
| Library搁置/已放弃（UI-A08f） | 32张四宽度双主题生产/live四状态截图已人工查看，空提示/状态标签/卡片可见，无新增确认缺陷 | 8组状态刷新URL/ID、category/status隔离、清除保留status并恢复状态内默认ID、返回根/书籍原ID线上通过；此限定项done，不代表其他Library控件通过 |
| Library愿望单（UI-A08g） | 32张四宽度双主题生产/live目录/分类/刷新/空状态图已人工查看，长标题/封面/计数/空提示可见，无新增确认缺陷 | 8组目录计数、category/status隔离、整页刷新URL/ID、空提示及刷新、两级返回与书籍原ID恢复线上通过；限定done，完整库存/离屏加载及评分控件仍pending |
| Library评分（UI-A08h / UI-010） | 四宽度双主题32张生产/live评分状态图已人工查看、放大390双主题首末提示及1024 Light原图，评分提示裁切已修复；另确认UI-011目录计数被固定按钮覆盖，不作全页通过 | 8组八分类分箱/摘要、真实Shift+Tab/Tab首末提示及退出隐藏、刷新恢复全域线上通过，32诊断与生产一致；评分限定done，完整库存/离屏加载/Steam及全站余项pending |
| Library目录计数/固定按钮（UI-011） | 四宽度双主题根目录四状态/愿望单首末48生产/live图已人工看并放大1024 Light漫画、390 Night愿望单入口、390 Light愿望单末端，计数无遮挡；限定done | 8组根8/愿望单7计数逐行滚动真实文字不与按钮相交、目录往返计数不变、真实返回顶部点击通过；48诊断与生产相同，不据此推断完整库存/离屏加载通过 |
| Ravenis、Occult Atlas | pending | 共享导航/核心控件/返回pending |
| Library默认书籍全网格（UI-A08k） | 71ceb601精确main build/deploy/live通过；四宽度双主题310线上原生行图的992卡片32联系表已人工看，放大390 Light/1024 Night原图，封面/标题完整，无新确认缺陷；限定done | 八流程124书籍6页全ID/原生逐行覆盖、无溢出、992加载及原分页刷新返回门禁线上通过；与生产ID/图片相同，卡片坐标最大差0.543px；其他分类仍pending |
| Library默认书籍分页/加载（UI-A08j） | 4140b667精确main build/deploy/live通过；四宽度双主题96页首/尾线上图已人工看并放大390 Light首、768 Night末页首，浮层关闭、封面可见，限定done；中间区域完整视觉见已done的UI-A08k | 8组完整124书籍6页/992原生封面加载、ID完整无重复、末页刷新URL/ID、上一页/返回根/重入首批ID通过；96几何横向边界与生产一致，纵坐标差异最大0.307px；其他分类仍pending |
| Library Steam/游戏首批离屏封面（UI-A08i） | b4a50239精确main重试build/deploy/live通过；四宽度双主题40线上图已人工看，关闭浮层后8张空提示清晰可见，统计/首屏/末端/刷新无新确认缺陷；限定done | 8组游戏第一页24卡原生滚动/解码共192次加载、时长排序分组、刷新URL/ID、Steam空来源刷新/清除/返回线上通过，40诊断与生产相同；仅当前无遥测路径，不推断完整库存或有数据时成就通过 |
| Gate/NAVI（仅既有隐蔽边界） | pending | 不将私有截图/入口加入公开台账 |

## 集中问题队列

无新增需要用户决定的问题。未来按Q编号记录影响、选项、推荐；未回复不视为同意，继续无关任务。

## 完成条件

全部矩阵有明确截图和交互证据；所有确认缺陷完成部署复验；无validation-pending或未解释阻塞。写 docs/neutriverse-ui-fix-final-report.md，标 COMPLETE、最终main/线上核对后暂停“修复 Neutriverse UI”。不无限审美修改。

Library UI-A08c2仅覆盖下一页/刷新/上一页、来源与年份组合、清除；排序、列表模式、摘置/已放弃尚未验收，随余下Library检查继续，不由此限定done推断全部高级筛选完成。

## 当前运行

2026-10-18 UI016限定done：精确main5862ab0e/run39067300977 attempt2 build117502673032/deploy117505713846/live117505765011全部success；258 tests/T01/authoring/Jekyll/原门禁、production/live各192+14及24公开流程177帧通过。live artifact12114393947独立SHA256匹配；12关系目标帧/8联系表实际查看、390 Night原图before/after全文无覆盖。ABOUT8流程诊断与production相同、真实滚轮/顶部按钮/公开往返通过，24流程scrollY差0。旧失败/取消及未知动画根因保留，不改时限/门禁。新证据提交自身CI另核对；全站IN PROGRESS，A09剩余整页与其他矩阵pending，无新用户问题。[限定线上证据](docs/ui-evidence/ui016-checks.md#2026-10-18-同head部署与线上限定验收通过)。

2026-10-18 UI016接续pending：8095f4a5/run39065426364 build117491963533/deploy117495092346 success，live117495142367 cancelled，未完整线上验收。main现5862ab0e14211edf63f264593638a5131c003616，仅保留新增Library六文件同步，UI/审计未变；其run39067300977 attempt1 build117497614664失败于1024 Light ABOUT从Library返回后有限动画等待，deploy117499783132/live117499784181 skipped。258 tests/Ruby/T01/authoring/Jekyll/前置门禁通过，主144/公开17流程139帧/侧栏0；artifact12114355647独立摘要匹配，失败原图实际看、无新显示缺陷确认。180ms背景色及500ms按钮透明度过渡running/time0/startTime null，根因未知，不改时限/动画/门禁。一次同head失败job重试attempt2 build117502673032运行中；不移动main/ui分支，证据留verification/ui016-5862-return-retry。无新用户问题，UI016/完整matrix仍pending，下一项同head重试及部署/live。[诊断与局限](docs/ui-evidence/ui016-checks.md#2026-10-18-已部署head的live取消最新main返回等待失败)。

2026-10-18 UI016生产限定视觉验收通过：实现a17ee7ec0db3e4fe9f534fa76bf7f663d5b5d0f9，[run39060823145](https://github.com/AplusNeutrino/My_Blog/actions/runs/39060823145) build117478235105 success、deploy117481148392/live117481148909 skipped（工作分支）。258 tests/Ruby/T01/authoring/production Jekyll/全部旧门禁、192+14及24公开流程177帧通过；artifact12111467085独立摘要匹配。人工看四宽度双主题12关系说明帧8联系表，放大390 Night原场景，与before对比说明全文可见、按钮不遮字；三目标逐个非空/严格交集0，8真实滚轮/返回顶部/Library友链往返通过。仅回写公开证据和计划日志，允许非强推交付；新main自身CI/部署/live仍validation-pending，A09全页和其余矩阵IN PROGRESS，无新缺陷/用户决策。[证据与局限](docs/ui-evidence/ui016-checks.md#2026-10-18-精确production与限定视觉验收)。

2026-10-18 UI-A09接续发现UI016：base main8bff45a9e83f1598dd7d248e5aaeb8350d7a2889 /run39056732011 build117466109670/deploy117469225064/live117469268662全部success，关闭UI015证据head pending。live artifact12110591949独立摘要匹配；原三页177帧中已实际查看12联系表68帧，390 Night ABOUT第9原图放大确认关系卡说明被按钮覆盖，优先转UI016，不将未看完矩阵标done。先记录[范围与原图](docs/ui-evidence/ui016-checks.md)，仅<=1199.98px给关系p加右2.75rem，新增该作用域严格文字门禁且全部旧断言/时限不动。未验收前留ui/fix-016，main不改；gh不可用不编造Issue，无新用户决策。其余24联系表109帧尚未人工验收，UI-A09整体pending，旧br/倒计时保留。

2026-10-18 UI015精确main线上限定done：base/验收main c001784bd31e67ce6da8512ceedcf058922c9261，[run39052090726](https://github.com/AplusNeutrino/My_Blog/actions/runs/39052090726) build117452566638/deploy117456022205/live117456065349全部success。256 tests/Ruby/T01保护44/5/5、authoring44/5/7、production Jekyll/全部原门禁，production/live各192+14及24公开流程177原生帧通过。live artifact12109095954独立SHA256匹配；人工看四宽度双主题四类目标45帧/18联系表，放大390 Night维护/理念/日期/状态与before对比，尾字与日期完整、固定按钮不遮字。两页16流程121帧detail诊断与生产完全相同、交集0，真实滚轮/返回顶部/公开往返通过；不冒称177帧/全页均人工验收。仅本UI证据/计划日志回写，新文档head CI另核对；无新缺陷或用户决策，字体旧根因未证实。全站IN PROGRESS，下一项UI-A09剩余整页及其余未覆盖矩阵。[线上证据与局限](docs/ui-evidence/ui015-checks.md#2026-10-18-精确main部署与线上限定验收)。

2026-10-18 UI015部分生产/字体阻塞：7f61a5f154f9736816e8a379b74ecacc6f3f8b43 /run39043515933 attempt1 build117427571131 failure，deploy117430042339/live117430042559 skipped；256 tests/Ruby/T01/authoring/Jekyll与前置门禁通过，主144/192、公开18/24/139帧、侧栏0。artifact12104867929独立摘要匹配。已放大看390 Night四原遮挡修复后原图，部分避让通过；三宽双主题四类逐行交集均0，但139图未全人工验收、1366及完整/main/live仍pending。字体1366 Night首THINK ready30s超时，5面loading（Sans400/500/600、Serif400/600）；捕获51 Font请求均finished/200缓存，无未完成事件，根因仍不确定，不据此改产品字体或放宽门禁。已做同head一次失败job重试attempt2 build117439836139运行中，不移动ui/fix-015或main；证据另存verification/ui015-7f61-retry，避免取消重试。无新用户决策，下一项核对同head重试。[诊断与边界](docs/ui-evidence/ui015-checks.md)。

2026-10-17 UI015实现待验：base097129418f5a014d3d1d85b2441f934854dcda3a /run39038972286 build117414389679/deploy117417289853/live117417342881全部success，关闭上一证据head CI pending。重新查看四张原图、先写ui015范围后，仅<=1199.98px的理念/维护说明/观察卡状态留右2.75rem文字通道，绝对定位日期right另加2.75rem；外框/列数/字号/主题/正文/按钮不动。新增四类作用域非空与严格真实行/按钮交集门禁，原首页/UI014/192+14/24public及全部等待不减。本机256 tests、authoring44/5/7、T01保护44/5/5、diff通过；本机无Jekyll/Chrome，生产/人工截图/main/live validation-pending，留ui/fix-015，main未改。gh不可用不编造Issue，无新用户决策；下一项核对同head。[UI015](docs/ui-evidence/ui015-checks.md)。

2026-10-17 UI014线上限定done：d1bdcbf2e00d7fc2abd30917af8573856af8719a /run39035135431 build117403304548/deploy117406508063/live117406677161全部success，254 tests/Ruby/T01/authoring/Jekyll/旧门禁、production/live各192+14及24public通过。live artifact12102362109独立摘要匹配；只人工查看两个说明容器实际可见的32线上帧16联系表，并放大原390两场景与旧图对比，遮挡已消除。两页121帧intro诊断与生产完全相同，16真实滚轮/返回顶部/公开往返通过。UI014 done，不将177全部帧或A09整页称视觉通过；UI015补维护说明同类原图仍待修，无新用户决策，gh不可用。本次只回写证据，证据新head CI另核对；全站IN PROGRESS，下一项UI015。[线上证据](docs/ui-evidence/ui014-checks.md)。

2026-10-17 UI014生产限定通过：ad1540d04b1acb161fe6820cf099c1471f249b0f /run39031283966 build117392071294 success、deploy117395105647/live117395105624 skipped（工作分支）。254 tests/Ruby/T01/authoring/Jekyll/全部旧门禁、192+14及24public通过；artifact12100198625独立摘要匹配。人工看OBSERVE/ABOUT四宽度双主题121帧34联系表，放大原390两场景，UI014说明段遮挡已消除，16流程真实返回顶部/公开往返通过。本次只追加证据，可交付已验收最小产品修复至main；新main自身CI/部署/live仍pending，不标done。另放大确认UI015理念段/书目日期/卡片状态仍遮挡，排下一项，A09与全站不标正常；无新用户决策，gh不可用不编造Issue。[UI014](docs/ui-evidence/ui014-checks.md)。

2026-10-17 UI014实现待验：base main fa23a32cf5f41b8fd6e47a3aebda7197213fb84e /run39027206328 build117380439666、deploy117383385470、live117383421916全部success，关闭上一证据head的CI pending。本轮重新查看390 Light OBSERVE/390 Night ABOUT原图，先记录范围后仅<=767.98px给两明确说明容器增加2.75rem右padding；不改共享按钮、原文或数据。原首页Range保留，新增两页目标必须存在且有文字/逐行严格无按钮交集，失败保存PNG/JSON。本机254 tests、authoring44/5/7、T01保护44/5/5、diff通过；没有本机Jekyll/Chrome，精确新head production/人工截图/main/live均pending，留ui/fix-014，不合main。gh不在PATH，不编造Issue；无新用户决策，不将静态测试当视觉验收。下一轮先核对同一分支head。[UI014范围与验收](docs/ui-evidence/ui014-checks.md)。

2026-10-17 UI012/013线上限定done：验收main e437b97d089359c47f8e83a691a3e9e43dbd2989 /run39023453629 build117369686142/deploy117372301121/live117372348023全部success，252 tests/Ruby/T01/authoring/Jekyll/全部门禁、production与live各192+14及24public通过。live artifact12098546289摘要独立匹配，四宽度双主题首页56滚动帧10联系表全部实际看并放大390 Night近期/768 Night精选原图，文字无遮挡、八流程返回顶部与四入口往返通过，关本两项pending。OBSERVE/ABOUT其余线上图未全人工验收、UI014待修，全站IN PROGRESS，无新缺陷或用户决策。本次只回写证据/计划日志，不追加产品改动；新证据head CI另核对，下一项优先UI014最小修复。[线上证据](docs/ui-evidence/uia09-checks.md)。

2026-10-17生产验收：d50f1bc9/run39019844860 build117359307157 success，deploy117362280180/live117362280399 skipped。252 tests/4 Ruby/T01/authoring/Jekyll/全部门禁、192+14及24public/177滚动帧通过；artifact12096771963独立摘要匹配。36联系表全部实际看并放大首页两旧遮挡、OBSERVE/ABOUT代表原图，UI012/013生产限定验收通过，可独立交付main，新main自身部署/live仍pending。新确认UI014说明段遮挡列队列；A09不标三页整体done。ABOUT显式br空白保留，不凭偏好删旧内容。字体本次未复现不宣称根因修好，无新用户决策，gh不可用不编造Issue。[证据](docs/ui-evidence/uia09-checks.md)。

2026-10-17 UI-A09-F字体阻塞定位：563d054f/run39015972699 build117348035702 failure，deploy117349896137/live117349895961 skipped；250 tests/Ruby/T01/authoring/Jekyll/前置门禁通过，主144/192、新public18/24、139帧/侧栏0。artifact12095147120摘要匹配，失败图及UI-013 768 Night/ UI-012 390 Night原图实际看，遮挡已避让但完整视觉未验收。字体集合loading，具体为Noto Sans SC400/500/600三个面；不猜CDN根因。仅补Unicode/Font网络事件诊断，不改产品/缓存/字体/等待门槛，252 tests/authoring/T01/diff通过。保存ui/audit-009，main53787e0b不动，原图/诊断及旧失败保留；无新用户决策，gh不可用不编造Issue。下一轮核对精确新head生产及网络诊断，UI012/013/A09仍pending。[证据](docs/ui-evidence/uia09-font-wait-checks.md)。

2026-10-17 UI-013实现待验：base工作78d01a32、main53787e0b不动；d91/run39008835671 attempt2 build117337553687仍失败于1366 Night THINK document.fonts.ready约30s，deploy117339610923/live117339611045 skipped。artifact12093428361独立摘要匹配，144主/18新流程/139帧/侧栏0，失败原图实际看，不称全验收。本轮先记录ui013范围后仅精选网格外列/单列避让，扩展逐行Range门禁；字体失败补状态诊断并原样抛错，不延长/跳过等待。250 tests/authoring/T01/diff通过，新精确production/完整视觉/main/live pending，留ui/audit-009；合入78d01a32真实失败记录与原图，不覆盖用户修改或旧COMPLETE。无新用户决策，gh未安装不编造Issue。[证据](docs/ui-evidence/ui013-checks.md)。

2026-10-17接续：d91bd721 / run39008835671首次build117326775861失败于1366 Night THINK document.fonts.ready脚本30s超时（非此前有限动画等待）；248 tests/4 Ruby/T01/authoring/Jekyll/SEO/资源通过，主144/192、新public18/24、139滚动帧，侧栏0。artifact12092431014摘要独立匹配。实际查看六组首页联系表及390双主题Z.A.T.O.原图，近期表达已避让；768 Night精选卡片第5帧确认UI-013，未将全首页标通过。139图未全验收。已重试同head，attempt2 build117337553687运行中，不延长等待或改门禁，不移动main53787e0b或ui/audit-009以免取消重试；记录另存verification/ui-a09-d91-retry。无新用户决策；下一项同head完整验收后处理UI-013。[记录](docs/ui-evidence/uia09-checks.md)。

UI-012最小实现/UI-A09返回阻塞定位（2026-10-17）：base工作head37fa1d78，main53787e0b不动。run39004907637 build117315276681 failure，deploy/live skipped；246 tests/Ruby/T01/authoring/Jekyll/主192通过，新public21/24、162滚动帧未全人工验收，侧栏0。artifact12090578680摘要匹配，1366 Light失败PNG/动画JSON已看，入口background-color有限过渡running/time0/startTime null。仅真实指针移出hover再执行原等待，门禁不减；UI-012首页卡片在无辅助栏宽度预留右空间并严格Range交集回归。本机248 tests/authoring/T01/diff通过；新head production/截图/main/live pending，留ui/audit-009，无新用户决策。[证据](docs/ui-evidence/ui012-checks.md)。

UI-A09首次失败/UI-012新复现（2026-10-17）：8831153b/run39001620617 build117305564644 failure，deploy/live skipped。245 tests/Ruby/T01/authoring/Jekyll及前置门禁通过，主审计仅24场景、新public0/侧栏0完成，不能标完整通过。artifact12089466875独立摘要匹配，实际看首页390 Night九帧并放大第3帧，确认UI-012返回顶部遮正文；优先队列转其首页最小修复。另在真实点击返回后的settle有限动画条件超时，当前无足够动画根因证据；仅补失败PNG/动画快照并原样抛错，不放宽旧门禁。main仍53787e0b，新诊断留ui/audit-009，生产及main/live继续pending，无新用户决策。[证据](docs/ui-evidence/uia09-checks.md)。

UI-A09范围先记录（2026-10-17）：base53787e0bbe111da193918ee959e82780b58d87c3精确run38997545484 build117293294892/deploy117295587015/live117295621809均success。选择首页/OBSERVE/ABOUT四宽度双主题24流程的重叠原生纵向截图、真实滚轮和公开有界往返；只增审计/必要回归及计划日志证据，不猜测改产品。云1363×936首页Light首屏实际看并滚动，无新确认缺陷；完整production/main/live仍validation-pending，先ui/audit-009。gh不可用不编造Issue，无新用户决策；范围与保护见[UI-A09](docs/ui-evidence/uia09-checks.md)，不重复书籍视觉或旧COMPLETE。

UI-A08k限定done（2026-10-17）：验收main71ceb60146048d463772c8c35a12ae39a5cc8c79 /run38993751090 build117281561210、deploy117283869973、live117283912634均success；243 tests/4 Ruby/T01/authoring/Jekyll/旧门禁及production/live各192+14通过。live artifact12086956833独立摘要匹配，人工看310线上原生行图的992卡片32联系表并放大390 Light/1024 Night原图，无新增确认缺陷。八流程124书籍6页/全行覆盖/992加载/刷新返回通过，ID/图片与生产相同，卡片坐标差最大0.543px。默认书籍中间区域视觉pending关闭；其他分类及全站余项继续pending，无新用户决策。本轮只回写计划日志/live证据，新证据head CI另核对，下一项优先首页/OBSERVE/ABOUT全页滚动交互。[证据](docs/ui-evidence/uia08k-checks.md)。

UI-A08k生产验收（2026-10-17）：723c651515b372756e12879f9c757a2cc8dc1b6b /run38989785855 build117269649689 success，deploy117272512100/live117272512541 skipped。243 tests/4 Ruby/T01/authoring/Jekyll/旧门禁/192+14通过。artifact12085016466独立摘要匹配；四宽度双主题全部310原生行图/992卡片的32联系表已人工看，放大390 Light第3页第4行/1024 Night第4页第3行原图，取景与坐标一致，未确认新产品缺陷。仅已验收审计/必要回归/证据，不改产品/数据；fresh main仍dcb9e136，非强推交付后须新main自身build/deploy/live及310线上行图，继续validation-pending。其他分类/全站余项pending，无新用户决策。[证据](docs/ui-evidence/uia08k-checks.md)。

UI-A08k取景修正（2026-10-17）：eccb2551/run38984590940 build通过，但实际看390双主题8联系表与390 Light第3页原图，CDP整页像素布局不匹配拍摄前rect，裁图混入上一行/裁去本行标题；非新确认产品缺陷，不将243 tests/48 PNG尺寸通过冒充视觉验收。仅改为真实逐行滚动原生viewport截图、全行卡片在topbar下及视口内、PNG尺寸/全ID覆盖断言；保留原96页首尾和所有加载交互。当前预计310行图，动态随列数/库存计算；其他宽度原整页未人工验收。本次修正工作分支ui/audit-008k，新head production/main/live仍validation-pending；main保持dcb9e136，无新用户决策。[证据](docs/ui-evidence/uia08k-checks.md)。

UI-A08k范围先记录（2026-10-17）：base dcb9e1362124d27bcf78aa0fe3d3aeb2cd3cd4b3，run38979246164 build117235958658/deploy117238946046/live117239020388全部success。选择默认书籍6页中间区域视觉证据：沿用真实逐卡加载/分页后，每页补原生CDP整页截图，当前4宽度×2主题×6页=48图；不改窗口或产品DOM/样式、不用DOM代替看图。文件限现有审计、必要回归、UI计划日志及uia08k证据，产品/数据不改，无新确认缺陷/用户决策；gh不可用不编造Issue。先ui/audit-008k，真实production截图、人工检查与main/live仍validation-pending，其他分类/全站继续pending。

UI-A08j限定done（2026-10-17）：验收main4140b667ef00b8b4723d29687306e2fdc5d1ef01 /run38973034490 build117215745464/deploy117219743993/live117219913508均success；241 tests/4 Ruby/T01/authoring/Jekyll/原门禁/production与live各192+14通过。live artifact12079130735独立摘要匹配，人工看96双主题四宽度页首尾图8联系表，放大390 Light首/768 Night末页首，未确认新缺陷。8流程完整124书籍6页/992原生加载/末页刷新与返回通过，ID/图片与生产相同，96几何仅纵坐标最大0.307px差异，原始证据保留。不据此推断中间区域完整视觉/其他分类通过，全站IN PROGRESS，无新用户决策。本轮只回写计划日志与live证据，新证据head CI另核对；下一项其余默认分类/中间区域及全站余项。[证据](docs/ui-evidence/uia08j-checks.md)。

UI-A08j最新数据生产验收（2026-10-17）：8eef170b98feea451bd210fe6190b8488fa36451 /run38967018561 build117196107879 success，deploy117200632292/live117200633470 skipped；241 tests/4 Ruby/T01/authoring/Jekyll/原门禁/192+14通过。artifact12075822645独立摘要匹配，人工看新数据四宽度双主题96页首尾图8联系表并放大390 Light首/768 Night末页首，未新增确认缺陷。8流程/完整124书籍6页/992原生加载/末页刷新返回与96几何通过；9个同步数据blob保持dda8dc31原值。只交付已验证审计/证据，不改样式；精确新main head build/deploy/live及96线上图仍validation-pending。中间卡片完整视觉、其他分类与全站余项仍pending，无新用户决策。

UI-A08j数据接续（2026-10-17）：生产6613d252限定范围已验收；交付前main并发前进dda8dc3172f69163975cc0d082833feb13b9cb67，9个Library同步数据文件更新，expected_sha复核已停止main操作，未覆盖同步。将审计/证据基于最新main保存ui/audit-008j-sync，9文件精确保留main blob；默认书籍仍124，仍须新精确head production及96图重验，不能用同数量或旧截图替代。main/deploy/live仍validation-pending，无新用户决策，全站IN PROGRESS。

UI-A08j生产验收（2026-10-17）：精确6613d252 /run38960141641 build117173359902 success，deploy117177120300/live117177121847 skipped（分支）。241 tests/4 Ruby/T01/authoring/Jekyll/既有门禁/192+14通过；下载artifact12073100672独立摘要匹配，人工查看四宽度双主题96页首/尾图8联系表，放大390 Light首/768 Night末页首原图，浮层关闭后封面可见，无新确认缺陷。8组完整124书籍6页/992原生加载/末页刷新与返回、96几何通过。仅此范围生产通过，中间卡片完整视觉和其他分类仍pending；非强推交付main后，精确新head build/deploy/live及96线上图仍validation-pending。全站IN PROGRESS，无新用户决策。[证据](docs/ui-evidence/uia08j-checks.md)。

UI-A08j取景修正（2026-10-17）：57a95067/run38952889668 build通过，deploy/live按分支skipped；人工看96图四联系表及390 Light首/768 Night末页首原图，发现前置Steam流程残留open筛选浮层遮住封面，不是已确认产品缺陷。8流程/124书籍6页/992原生加载和96几何通过不能替代视觉验收。只修审计真实关闭面板及拍摄前断言，新增1回归，原断言不放宽；本次修正留ui/audit-008j，production新head/main/live继续validation-pending。main保持325db4d0，无新用户决策，完整矩阵仍IN PROGRESS。[证据](docs/ui-evidence/uia08j-checks.md)。

UI-A08j（2026-10-17）validation-pending：base325db4d0771c3fd518d52ebf908e7d6b45962453；该head run38944307535 build117119432424/deploy117122814466/live117122895755全部success。范围先记录：默认书籍完整分页、逐卡原生封面滚动/解码、末页刷新及返回；当前124条/6页，动态按公开数据计算。四宽度双主题各页首尾截图，中间卡片只有加载/几何检查，不冒充逐卡视觉验收。只改现有审计、必要回归、本计划日志及uia08j证据，不改产品/数据。无新确认缺陷或用户决策；gh不可用不虚构Issue。工作分支ui/audit-008j，production及main/live待验证；其他分类与全站矩阵仍pending。

UI-A08i限定done（2026-10-17）：验收main b4a502396bd02650738f4b69912ef2bdca437173 / run38920457806 attempt2 build117067139721/deploy117071593206/live117071699364全部success。237 tests/4 Ruby/T01/authoring/Jekyll/旧门禁、production/live各192+14通过。live artifact12058453192独立摘要匹配，人工看四宽度双主题40图并放大390 Light来源、768 Night末端原图，空提示可读、封面正常；8流程/192次原生加载/40诊断通过且与生产相同。首次失败与0a12dac8记录合入保留，不改产品/数据或旧COMPLETE；本轮仅计划日志与公开live证据，新证据head CI另核对。当前无遥测路径限定通过，有数据时成就等未检不冒称通过；全站IN PROGRESS，无新用户决策，下一项完整库存/其余分页图片及其他全站矩阵。

UI-A08i main接续validation-pending（2026-10-17）：精确main b4a502396bd02650738f4b69912ef2bdca437173 / run38920457806首次build117038739414 failure，deploy117041059374/live117041060364 skipped。237 tests/Ruby/T01/authoring/Jekyll与前置门禁通过；Chrome在390 Night Library场景结束后的下一次driver.get（按场景顺序为友链）控制通道localhost:52101读取120s超时，未收到目标场景日志，不能断言目标页面UI故障。部分artifact12054128548摘要独立匹配，只有390 Night本项5张图，已看source原图空提示可见，不代替完整40图/线上验收。已重试同一run失败jobs，第二次build117067139721运行中；不改产品/审计/超时门槛。为不取消同head重试，仅在verification/ui-a08i-retry-log保存本次3文档诊断记录，不移动main。无新用户决策，完整库存与其他全站项仍pending。

UI-A08i生产验收通过、待main/live（2026-10-16）：base main仍f2d463cf，验收head707b6d49c3066bcfaa54ed3f10bfe811608e966a / run38913520936 build117015038501 success，deploy117019410328/live117019410572 skipped（分支）。237 tests/4 Ruby/T01/authoring/Jekyll/旧门禁/192+14通过；artifact12051129960摘要独立匹配，人工看40图两联系表并放大390 Light来源、768 Night末端、1024 Light来源原图，关闭浮层后的空提示清晰可读，未确认新产品缺陷。8流程、40诊断、192次原生封面加载通过。仅交付已验收审计及计划日志/公开证据，main精确head部署/live同40图仍validation-pending；Steam隐私边界未变，只有无遥测路径已检查，完整库存/其余分页和全站矩阵仍pending，无新用户决策。

UI-A08i接续validation-pending：base main仍f2d463cf、工作head53b53605；run38905074465 build116986945525 success、deploy/live skipped。236 tests/Ruby/T01/authoring/Jekyll/192+14及8流程/192次逐卡原生加载通过；下载artifact12047752802独立摘要匹配，人工看40图及代表原图未确认新产品缺陷。但8张来源图的正常高级筛选浮层覆盖空提示，不能以is_displayed当视觉验收；本轮仅审计补真实关闭浮层后同场景采图及1项回归，不改产品或放宽断言。首次图/JSON按局限保存，修正后精确head完整40图/8流程与main/live仍待验收，main不改；无新用户决策，有遥测时Steam视觉pending-no-data，不突破隐私边界。

UI-A08i真实审计实现9f6f0fb021c35167d5419afc9a05f4c174f7a4e6已保存ui/audit-008i，5个blob与本地hash一致；随后仅追加SHA检查点。main仍f2d463cf，未部署新审计；最终分支head production40图/8流程与main/live必须分别核对，保持validation-pending，无新用户决策。

UI-A08i validation-pending：仅新增审计与3项接线回归；目标统计/游戏Steam排序首屏/离屏末端/刷新/来源5状态共40图和8流程。逐卡真实滚动、原生complete/decode/两帧、初始离屏与natural尺寸记录、数据库存/状态组内时长排序、刷新/清除/返回和clientWidth门禁已实现，本地236 tests/authoring/T01/diff通过；不代表响应式视觉/Jekyll通过。本机无Ruby/Chrome，先工作分支ui/audit-008i，main不改；完整库存/其余分页图片/真实Steam成就等仍pending，无新产品缺陷或用户决策。

UI-A08i in-progress（2026-10-16）：base main f2d463cfb75168b7ca0a883915ef56efa0b7b4e4；run38897628035 build116961810761/deploy116964440787/live116964525050全部success。范围仅现有浏览器审计、必要接线回归、本计划日志与uia08i公开证据；限定Steam统计不可用展示、游戏Steam游玩时间排序/刷新同URL与ID、Steam来源真实库存或空提示/刷新/清除/返回，以及该排序第1页逐卡滚动原生离屏封面加载。云1363×936 Light实际排序、Steam空状态刷新截图已看，无新增确认产品缺陷，不改产品/数据；四宽度双主题目标32状态图和8流程尚待精确工作分支验收。完整库存/其余分页图片及有数据时Steam成就等不冒称通过；无新用户决策，gh未安装不编造Issue。

UI-011 done（2026-10-16）：base/验收main831f2898372f37bb9f226748073cdeca45962085，run38891686220 build116942440784/deploy116945366767/live116945432409全部success；233 tests、4 Ruby、T01/authoring/Jekyll/旧门禁及production/live各192+14通过。live artifact12042547968摘要独立匹配，人工看四宽度双主题48图三联系表并放大1024 Light漫画、390 Night愿望单入口与390 Light愿望单末端，计数全文可见、不再被按钮遮住，未新增确认缺陷。8组逐行滚动/往返/真实返回顶部和48诊断与生产逐项相同，评分/目录限定通过，不代表全Library正常。本轮仅UI计划日志及ui011公开live证据，不追加产品/数据改动，新文档head CI另核对；无新用户决策。全站仍IN PROGRESS，下一项完整库存/离屏加载与Steam及其余矩阵。[线上证据](docs/ui-evidence/ui011-checks.md#2026-10-16-精确main线上验收)。

UI-011生产验收通过、待main/live（2026-10-16）：base main600f29073e94b2d8ad17e3365db4c262e9d398f6，验收head55c41c973f179e3c500bbe846eba76fd61bc6204（实际修复86d8453820eec1eda59f604d4524381a121b25a5）。run38885320771 build116921858701 success、deploy116924481966/live116924483260 skipped（分支，不作部署）；233 tests、4 Ruby、T01/authoring/Jekyll/旧门禁及192+14通过。artifact12038779445摘要独立匹配；人工看48张四宽度双主题根目录四状态/愿望单首末三联系表，再放大1024 Light漫画、390 Night愿望单入口及390 Light愿望单末端原图，对照修复前1024截图，计数全文可见、不再被按钮遮挡。8组根8/愿望单7计数逐行滚动、不相交、目录往返计数不变及真实返回顶部点击通过，48诊断无横向溢出。仅UI计划日志与ui011公开生产证据，不追加产品改动；验收后非强推main仍validation-pending，须新main精确head build/deploy/live同48图复验。无新增确认缺陷/用户决策，其他全站项仍pending。[证据](docs/ui-evidence/ui011-checks.md#2026-10-16-生产截图与交互验收)。

UI-011真实实现86d8453820eec1eda59f604d4524381a121b25a5已保存ui/fix-011，6个上传blob与本地hash逐项一致；随后仅追加此SHA检查点。main仍600f2907，未部署/未合main；最终分支head精确production192+14/48图/8流程及main/live必须分别验收，保持validation-pending，无新用户决定。

UI-011 validation-pending：已实现<=1199px仅Library目录/愿望单入口padding-inline-end:3.5rem，保持按钮/字号/数据不变；新增真实逐行滚动、count文字与固定按钮不相交/可用视口、根目录场景必须显示按钮并hit-test、目录往返计数不变及真实按钮回顶部审计，目标48图/8流程。新增3项接线回归，本地233 tests、authoring44/5/7、T01保护44/5/5及diff通过；没有本机Ruby/Jekyll/Chrome，不把单测当视觉通过。先保存ui/fix-011，main保持600f2907；精确head生产192+14、新48图与main部署/live均待验证，无新用户决策。

UI-011 in-progress（2026-10-16）：base main600f29073e94b2d8ad17e3365db4c262e9d398f6；run38878173427 build116898172377/deploy116901351049/live116901426946全部success。已读当前仓库约束、ADR、旧COMPLETE计划报告与UI计划日志，CONTEXT不存在，gh未安装不编造Issue。原始1024 Light目录漫画计数遮挡截图已保存；本轮云1363×936 Light滚动目录实际截图/DOM测量无相交（计数right1041.81、按钮left1240.41），不能冒充1024已复测。源码定位目录行无固定按钮避让；拟仅assets/pgl/pgl.css在<=1199px给目录/愿望单入口保留右侧空间，tools/check_think_build_visual.py新增真实逐行滚动/文字按钮不相交及返回顶部操作、必要回归、计划日志与ui011证据。保留192+14及原门禁，未验证存ui/fix-011，不合main。无新用户决策，不改数据/原文/metadata/URL/hidden/noindex/外部仓库。

UI-010 done / UI-A08h限定done（2026-10-16）：base/验收main41dca277eace9aa053bcb87e3cd21892b5ae6390，run38871666487 build116876943806/deploy116880022801/live116880240197全部success；230 tests、4 Ruby、T01/authoring/Jekyll/旧门禁及production/live各192+14通过。live artifact12033767964摘要独立匹配；人工看32评分图两联系表并放大390双主题末端/Night首端及1024 Light书籍原图，提示全文可见，8流程/32诊断与生产相同，UI-010闭合。另从1024 Light同原图确认UI-011固定返回顶部按钮覆盖目录漫画计数，独立记录ready、下一项优先复现根因；不将评分验收扩写全页通过。本轮仅UI计划日志与ui010/uia08h线上证据、ui011复现记录，不改产品/数据/旧COMPLETE，无新用户决策；新文档head CI另核对。全站仍IN PROGRESS，完整库存/离屏加载、Steam及其余矩阵pending。[线上证据](docs/ui-evidence/ui010-checks.md#2026-10-16-精确main线上验收)。

UI-010 / UI-A08h生产验收通过、待main/live（2026-10-16）：base main仍3d822d563af3b798a98887d3f35505496931d63c；验收head c9d2280d4c139158371496798782933ac3c88bdd（实际修复dc3454d778d628c60576ab5fa57dd9b416e9a4f1），run38864744419 build116855162216 success，deploy116857968018/live116857968151 skipped（分支，不作部署）。230 tests、4 Ruby、T01/authoring/production Jekyll/旧门禁及192+14通过。artifact12031007024完整下载后独立sha256匹配；人工看四宽度双主题32评分图两联系表，并放大390 Light/Night末端、390 Night首端和1024 Light书籍原图，提示尾字完整、首末提示在shell内。8评分分类/摘要/真实键盘/退出隐藏/刷新默认流程及32诊断通过；390 Light末端right由390.39收回355（clientWidth379），Night350.99（clientWidth375）。本轮仅UI计划日志及ui010/uia08h公开生产证据，不追加产品改动；验收后非强推main，仍validation-pending，须新main精确head部署/live同32图复验。无新用户决策；完整库存/离屏加载、Steam与全站余项pending。[证据](docs/ui-evidence/ui010-checks.md#2026-10-16-修复后生产验收)。

UI-010 / UI-A08h validation-pending：真实修复dc3454d778d628c60576ab5fa57dd9b416e9a4f1已expected_sha非强推保存ui/audit-008h，10个上传blob与本地hash逐项相同；随后只追加此SHA记录。本地230 tests/authoring/T01/diff通过，不等于修复后视觉验收；新head须完整192+14、新32图/8流程/clientWidth与shell边界，再交付main/live。main仍3d822d56，未部署；无新用户决策。

UI-010 / UI-A08h修复in-progress（2026-10-16）：base main3d822d563af3b798a98887d3f35505496931d63c、工作分支base9d8d3c0869853fd69e4623c50b68ebf1607c8b12；run38858665322 build116836040776 success、deploy116838599413/live116838599804 skipped，229 tests/4 Ruby/T01/authoring/Jekyll/192+14通过但不作视觉通过。artifact12029150207摘要独立匹配，人工看32评分图并放大390 Light/Night末端提示，确认尾字被滚动条裁切；Light提示right390.39，实际可用页宽379，旧innerWidth390检查漏报。范围assets/pgl/pgl.js与pgl-rating-polish.js两renderer提示定位、现有审计/必要回归、UI计划日志与ui010/uia08h公开证据；只夹紧提示到shell且新增clientWidth/shell边界断言，不放宽门禁/重新设计。不合main，gh未安装不编造Issue，无新用户决策。

UI-A08h审计竞争修复validation-pending：实现7577e4cff209073f438a2f41bd2e718292ecccc7已expected_sha非强推保存ui/audit-008h，5个上传blob与本地hash一致。本地229 tests/authoring/T01/diff通过，但新head production完整192+14/32图/8流程及main/live仍待验证；旧fb511faf因刷新异步SVG逐节点读取stale失败，不是已确认产品缺陷。不改产品/放宽门禁，main仍3d822d56；随后仅追加此SHA检查点，无新用户决策。

UI-A08h审计修复in-progress（2026-10-16）：base main仍3d822d563af3b798a98887d3f35505496931d63c，工作分支base fb511faf9d364e9907f07ee71958d9547d996532 / run38854460953 build116822998597 failure，deploy116823893916/live116823894777 skipped。准确失败是刷新verify(all)逐节点读取时SVG异步重绘引发StaleElementReferenceException，不作产品缺陷。artifact12026791958摘要独立匹配；只生成390双主题/768 Night共12张评分状态图，人工放大390 Light首末端与768 Night书籍图，不能冒充32图/8流程通过。范围仅评分审计/必要回归、UI计划日志与uia08h公开证据；拟改同一帧原子只读快照保留全部断言和真实键盘，不改产品/放宽门禁，仍工作分支validation-pending，无新用户决策。

UI-A08h validation-pending：真实评分审计实现585126e1533ea5aeb2b9b2c822499955b4702da8已expected_sha非强推保存ui/audit-008h，6个上传blob与本地hash逐项相同。本地228 tests、authoring44/5/7、T01保护44/5/5和diff通过；云1363 Light分类切换与真实键盘提示/退出隐藏正常，未确认新产品缺陷。main仍3d822d56；随后仅追加实现SHA记录，最终检查点head production192+14、新32图/8流程与main部署/live需分别验收，不以单测或其他提交CI替代。无新用户决策，完整库存/离屏加载、Steam与其他全站项pending。

UI-A08h in-progress（2026-10-16）：base main3d822d563af3b798a98887d3f35505496931d63c，精确run38849000797 build116805821290/deploy116808150183/live116808204281全部success。已读仓库约束/ADR及旧COMPLETE计划报告，CONTEXT不存在、gh未安装。范围仅tools/check_think_build_visual.py、必要审计回归、UI计划日志及docs/ui-evidence/uia08h*公开证据；云1363×936 Light书籍/音乐评分切换及Shift+Tab末端点提示已实际操作并看图，未确认新产品缺陷。拟补四宽度双主题八分类评分/摘要、真实键盘端点提示及退出隐藏、刷新默认恢复，32状态图与几何；未验证留ui/audit-008h，不改产品/数据/旧内容，不合main。完整库存/离屏加载、Steam及全站余项仍pending，无新用户决策。

UI-A08g限定done（2026-10-16）：base/验收main b95bba7ccf511b0797c004621764c79112acf792，[run38843916122](https://github.com/AplusNeutrino/My_Blog/actions/runs/38843916122) build116789975836/deploy116792410025/live116792468638全部success；227 tests、4 Ruby、T01/authoring/Jekyll/旧门禁及production/live各192+14通过。live artifact12022769374摘要独立匹配，人工看32张四宽度双主题目录/分类/刷新/空状态两联系表，放大390 Light分类长标题、390 Night空提示与1024 Light刷新原图，未新增确认缺陷。8愿望单流程与32元素诊断和生产一致，计数/分类隔离/刷新URL与ID/空提示/两级返回及书籍原ID恢复通过，无横向溢出/scrollX。本轮仅UI计划日志及docs/ui-evidence/uia08g*公开live证据，不改产品/数据/旧COMPLETE；新文档head CI另核对。无新用户决策，全站IN PROGRESS，下一项Library评分控件，完整库存/离屏加载、Steam及其他全站项pending。[证据](docs/ui-evidence/uia08g-checks.md#2026-10-16-精确main线上验收)。

UI-A08g生产验收通过、待main/live（2026-10-16）：base main23343d67baba17dbe787f5611eea39ed90ad0b79、验收head8240a3b192e32b935541208532fd491cd3b75033，run38838899369 build116774445703 success，deploy116776769147/live116776770483 skipped（工作分支，不作部署）。227 tests、4 Ruby、T01/authoring/Jekyll/旧门禁及192+14通过。artifact12020114567摘要独立匹配；人工看32张四宽度双主题index/category/reloaded/empty两联系表，放大390 Light刷新、390 Night目录和1024 Light空提示原图，未确认新产品缺陷。8愿望单计数/分类与status隔离、刷新同URL/ID、空提示、两级返回与书籍原ID恢复通过，32几何无横向溢出/scrollX。本轮只改UI计划日志及docs/ui-evidence/uia08g*公开生产证据，不改产品/数据/旧COMPLETE；验收后非强推main仍validation-pending，须新main部署/live同32图。无新待答问题，评分及其他全站项仍pending。

UI-A08g validation-pending：真实愿望单审计实现e5f3b3bfc369763951d1374eeb7756b1e9b7190d已expected_sha非强推保存ui/audit-008g，6个远程blob与本地hash逐项相同。本地227 tests、authoring44/5/7、T01保护44/5/5、diff通过；云1363 Light非空分类刷新、Night空分类刷新与两级返回已实际操作并看截图，未确认新缺陷。main仍23343d67，随后仅追加此实现SHA记录；最终检查点head的production192+14、新32图/8流程、main部署/live必须分别核对，不以单测或其他提交CI替代。无新待答问题，评分控件及其余全站矩阵pending。

UI-A08g in-progress（2026-10-16）：base main23343d67baba17dbe787f5611eea39ed90ad0b79，精确run38833481298 build116757262447/deploy116759522336/live116759587790全部success。先读仓库约束与旧COMPLETE历史；CONTEXT不存在、gh未安装。范围仅tools/check_think_build_visual.py、必要接线回归、UI计划日志和docs/ui-evidence/uia08g*公开证据。云1363×936 Light实际愿望单目录、漫画分类、刷新与返回目录截图未确认新缺陷（初始封面异步加载，刷新后全部完成）；拟补四宽度双主题目录/非空分类/刷新/空分类32图和URL/ID/status/category隔离、目录计数及两级返回，未验证留ui/audit-008g，不改产品/数据/旧内容，不合main。评分控件与其他全站项仍pending，无新用户决策。

UI-A08f限定done（2026-10-16）：base/验收main7225dcca0015509cac855c7283a9d793257c8683，[run38827719864](https://github.com/AplusNeutrino/My_Blog/actions/runs/38827719864) build116738970873/deploy116741229180/live116741300079全部success；226 tests、4 Ruby、T01/authoring/Jekyll/旧门禁和production/live各192+14通过。live artifact12015679614摘要独立匹配，人工看32张四宽度双主题book-hold/game-hold/game-dropped/cleared两联系表并放大390 Light空提示、390 Night搁置、1024 Light清除原图，未新增确认缺陷；8流程刷新同URL/ID、状态隔离、清除保留status并恢复状态内默认ID、返回根/书籍原ID及32几何通过。范围仅UI计划日志、docs/ui-evidence/uia08f*公开live证据，不改产品/数据/用户首页推荐，新文档head CI另核对。无新用户问题，全站IN PROGRESS；下一项Library愿望单与评分控件，完整库存/离屏加载及其余全站仍pending。[证据](docs/ui-evidence/uia08f-checks.md#2026-10-16-精确main线上验收)。

UI-A08f生产验收通过、待main/live（2026-10-16）：base main40824656997ec79b0bfe875b33705acef33e65f1、验收head63bb246c655ffba55df566daf6dcda7c4f0e11c0 / run38821881510 build116720567164 success，deploy116723405622/live116723406291 skipped（工作分支，不作部署）。226 tests、4 Ruby、T01/authoring/Jekyll/旧门禁及192+14通过，artifact12013457997摘要独立匹配。人工看32张四宽度双主题book-hold/game-hold/game-dropped/cleared两联系表，放大390 Light空提示、390 Night已放弃和1024 Light搁置原图，未新增确认产品缺陷。8状态刷新/隔离/清除/返回流程和32几何通过。本轮范围仅UI计划日志与docs/ui-evidence/uia08f*公开生产证据，不改产品/用户首页推荐/数据或旧COMPLETE；验收后非强推main仍validation-pending，须新main精确部署/live同32图。无新用户问题，其他全站矩阵仍pending。

UI-A08f真实审计实现ea5fb0e15aca4e9a4ff51683072ada05cf7ac5a5已expected_sha非强推保存ui/audit-008f，6个远程blob与本地hash逐一相同；随后仅追加此SHA记录。最终检查点head需单独核对production192+14及新32图/8流程，main保持40824656，未部署新审计或标视觉通过。无新待答问题，继续validation-pending。

UI-A08f validation-pending：已实现真实状态切换/三次刷新同URL与ID、标签/空提示/category隔离、清除保留状态并恢复状态内默认ID、返回根/书籍原ID审计，四宽度双主题32图/JSON待CI。本地226 tests、authoring44/5/7、T01保护44/5/5、diff通过；云1363 Light实际清除仍已放弃、返回根成功。未确认新产品缺陷，未改样式/数据；先ui/audit-008f，main仍40824656，production192+14/32图和main/live未验收。无新用户问题。

UI-A08f验收契约补充：源码既有“清除筛选”只重置来源/年份/排序，不清除搁置或已放弃状态；因此验证清除后仍处该状态、恢复该状态默认排序ID，通过返回按钮回分类根。不得为审计擅改产品清除语义。

UI-A08f in-progress：base main40824656997ec79b0bfe875b33705acef33e65f1，保留用户新增_data/home_popular.yml，不覆盖；上次文档bcc58e47/run38814934654 build116697108846/deploy116699969989/live116700077492全部success。已读最新AGENTS/domain/ADR、旧COMPLETE计划报告和UI日志；CONTEXT不存在、gh未安装。范围仅现有浏览器审计/必要回归/计划日志及公开状态证据，不改产品。云1363×936 Light书籍搁置空提示、游戏9条搁置刷新保持、4条已放弃实际切换及截图未确认新缺陷；拟补四宽度双主题状态/刷新同URL与ID/状态标签与category隔离/清除恢复/返回目录32图8流程，未验证留ui/audit-008f，production/main/live pending。无新用户问题，其他Library/全站矩阵仍pending。

UI-A08e限定done（2026-10-16）：验收main/base ae9e1b40aaf2824b91c0ceb1076db3f6a826902c，[run38809080788](https://github.com/AplusNeutrino/My_Blog/actions/runs/38809080788) build116677946585/deploy116681317407/live116681407285全部success。最新head保留同步数据，production/live各192+14、225 tests、4 Ruby、T01/authoring/Jekyll/旧门禁通过。live artifact12007758338摘要独立匹配，人工看32张四宽度双主题评分/年份/列表/刷新两联系表，放大390 Light刷新、390 Night评分、1024 Light列表原图，未新增确认缺陷；8排序/列表流程和32几何通过。计划日志与公开live证据回写，不改产品；新文档head CI另核对。无新待答问题，全站IN PROGRESS；下一项Library摘置/已放弃与剩余控件，不从限定done推断完整库存/全部排序/全站通过。[证据](docs/ui-evidence/uia08e-checks.md#2026-10-16-最新main线上验收)。

UI-A08e线上复验进行中（2026-10-16）：base/current main ae9e1b40aaf2824b91c0ceb1076db3f6a826902c，9f411fdf之后为既有Library同步7文件，本轮保留不覆盖；原run38807345479 build/deploy success但live cancelled，不以取消当通过。改验最新head自身run38809080788 build116677946585/deploy116681317407/live116681407285全部success，下载live artifact12007758338摘要独立匹配。范围仅UI计划日志与docs/ui-evidence/uia08e*公开live证据；逐张人工看同32图、核对8流程及32几何后才限定done。其他Library/全站矩阵仍pending，无新待答问题，不改产品/数据/旧COMPLETE。

UI-A08e生产验收通过、待main/live：本轮base main5a3b947fd9ea9ad2d6d7135d52b8afbebfcfb9cd、验收head b392d508df2e340285694426acdf72abbd0cc63d，run38799655164 build116645533313 success；deploy116648196476/live116648198287 skipped（工作分支）。225 tests、4 Ruby、T01/authoring/Jekyll/旧门禁及192+14通过。artifact12004835019摘要独立匹配，人工看32张四宽度双主题评分/年份/列表/刷新图两联系表，放大390 Light列表、390 Night年份和1024 Light刷新原图，未确认新产品缺陷。8排序/刷新/列表偏好/键盘恢复流程通过，32几何无横向溢出/scrollX且pressed一致。本轮范围仅本UI计划/日志、docs/ui-evidence/uia08e*公开生产证据，不改产品；验收后非强推main仍validation-pending，须新main部署/live同场景验收。无新用户问题，完整库存/其余控件及全站仍pending。

UI-A08e validation-pending：真实审计实现c7e248e18e222584a65d6fc277e679d8978d4837已expected_sha非强推保存ui/audit-008e，6个远程blob与本地hash逐项相同。本地225 tests/authoring/T01/diff通过；云1363 Light评分列表刷新保持及Enter网格恢复通过。main仍5a3b947f；随后仅记录SHA检查点，最终head production192+14、新32图/8流程与main/live需分别验收。无确认新产品缺陷、未改样式/数据，无新用户问题。

UI-A08e in-progress：base main5a3b947fd9ea9ad2d6d7135d52b8afbebfcfb9cd，run38790272247 build116612728961/deploy116616173047/live116616346613全部success。范围仅现有浏览器审计、必要接线回归、计划日志与公开证据，不改产品。云1363×936 Light真实评分排序及列表切换已看截图，未确认新缺陷；验收补四宽度双主题评分/年份排序、标题排序刷新同ID、列表切换保持ID/刷新持久化/键盘恢复网格及32状态图，保留进行中优先契约和全部192+14。未验证先工作分支ui/audit-008e，不合main；完整库存/摘置/评分等其余控件仍pending，无新待答问题。

UI-009 done / UI-A08d限定done（2026-10-16）：base与验收main8eb17637def2f3b185d0d1733fe62a611351e222，[run38781988055](https://github.com/AplusNeutrino/My_Blog/actions/runs/38781988055) build116584281245/deploy116587790492/verify-live-ui116587884313全部success；224 tests、4 Ruby、T01/authoring/Jekyll/旧门禁及production/live各192+14通过。live artifact11997335321摘要独立匹配；人工看24张四宽度双主题时间线首/尾/刷新图两联系表，放大390 Light首段、390 Night刷新及1024 Light尾段，长作品名完整换行、未被固定按钮遮住。24真实文字诊断按钮可见、overlaps=[]，8时间线流程同记录通过。本轮仅计划日志与公开live证据，不改产品，文档新head CI另核对；无新用户问题。全站IN PROGRESS，下一项Library排序/列表与剩余控件，不从此限定done推断完整库存或全站已验收。[证据](docs/ui-evidence/ui009-checks.md#2026-10-16-精确main线上验收)。

UI-009/UI-A08d生产验收通过、待main/live：base main2e3d2844af408504cb616b9596ea682c97c3edd0，验收head2fcde494768cd4f45c10ae6615e85219f8c8fd62 / run38774806960 build116560105866 success，分支deploy116563569328/live116563569815 skipped。224 tests、4 Ruby、T01/authoring/Jekyll/旧门禁与192+14通过；artifact11993626620摘要独立匹配。人工看24张四宽度双主题start/tail/reloaded图两联系表，放大390 Light首段、390 Night刷新、1024 Light尾段：长作品名完整换行、不再被返回顶部按钮覆盖。24实际文字/按钮诊断均按钮可见且overlaps=[]、无行/页面溢出/scrollX，8时间线流程46条/单列表/滚动保持/刷新lazy/Enter同记录通过。范围仅计划日志与公开生产证据，不追加产品改动；验收后非强推main，仍validation-pending，需新main精确部署/live同24图，不用localhost代替。全站仍IN PROGRESS，无新用户问题。[证据](docs/ui-evidence/ui009-checks.md)。

UI-009真实修复063053c23b287432dd7ff76328da2e22f9509c1a已expected_sha非强推保存ui/audit-008d，12个上传blob与本地hash一致；随后仅追加实现SHA记录。最终检查点head的production192+14/新24图/文字按钮相交诊断及main/live需单独验收，main仍2e3d2844，UI-009/UI-A08d validation-pending；无新待答问题。

UI-009修复及诊断已实现，先ui/audit-008d：720px内时间线padding-right3.5rem，仅为固定按钮留空间；审计新增真实可见文字行与#back-to-top矩形相交检查，按钮必须可见，原全部断言/24图/8流程保留。本地224 tests/authoring44/5/7/T01保护44/5/5/diff通过；本机未运行Ruby/Jekyll/Chrome，修复后production192+14和精确main/live均待新head验收。UI-A08d/UI-009保持validation-pending，main不改，无新待答问题。[缺陷证据](docs/ui-evidence/ui009-checks.md)。

UI-009 in-progress / UI-A08d继续validation-pending：base main2e3d2844、工作head47b3c294；run38765012413 build116526426682 success，deploy116529172398/live116529172648 skipped。223 tests/4 Ruby/T01/authoring/Jekyll/192+14及8时间线流程通过，artifact11989890630摘要匹配。实际看24张时间线首/尾/刷新两联系表并放大390 Light首/尾、1024 Night刷新，确认390 Light固定返回顶部按钮覆盖长作品名尾部，不能以原机械通过说视觉正常或合main。最小范围pgl.css、现有审计/必要回归、计划日志/公开证据：窄屏timeline列表预留按钮避让，不移动全站按钮或重新设计，补真实文字行矩形与按钮不相交门禁。新head完整production/24图与main/live待验收；gh未安装未编造Issue，无新待答问题。

UI-A08d审计修正实现e8ab0dbc2f3090454cc7933370639c0d956cd75a已expected_sha非强推保存ui/audit-008d；7个上传blob与本地hash相同。随后仅追加实现SHA记录，最终检查点head需单独验证，main仍2e3d2844；本地223 tests/authoring/T01/diff通过，production192+14、新24图/8流程及main/live未验收。无新待答问题，不将审计错误当网站缺陷。

UI-A08d继续validation-pending：base main2e3d2844、验收branch02d11892；run38757230686 build116499547427 failure，deploy116500623040/live116500622929 skipped。222 tests/4 Ruby/T01/authoring/Jekyll与此前门禁通过，但完整192+14未完成。下载artifact11983209912摘要匹配，实际看390 Night时间线start/tail原图未确认新产品缺陷；失败为审计再次点击已被既有replaceChildren移除的按钮。范围仍现有审计/必要契约回归/计划日志/公开证据，仅修审计为一次性按钮替换+单列表、滚动保持，再刷新lazy/Enter同记录，不新增产品按钮或降低内容/溢出/刷新断言。新head完整24图/8流程与main/live待验收，无新用户问题。

UI-A08d真实审计实现1ce495f6722c9ea17cf6e640633ce2963fd4aa04已保存ui/audit-008d，6个远程blob与本地hash一致；本次随后仅追加SHA检查点，最终分支head CI需单独核对，main仍2e3d2844。状态validation-pending，下轮优先核对该分支最终head production192+14及24图/8流程，未部署或验收不进main。

UI-A08d validation-pending：已新增真实时间线加载/首尾滚动/重复加载等待实际ul替换/刷新lazy重置/Enter加载同记录审计，新增24图及逐行溢出JSON；222本地tests、authoring44/5/7、T01保护44/5/5与diff check通过。本机未运行Ruby/Jekyll/Chrome，先ui/audit-008d精确head production192+14与24图，再决定main和live；main保持2e3d2844，未改产品，无新用户问题。[限定桌面证据](docs/ui-evidence/uia08d-checks.md)。

UI-A08d in-progress：base main 2e3d2844af408504cb616b9596ea682c97c3edd0，上次run38749174621 build116470712739/deploy116473447923/live116473729990全部success。范围仅tools/check_think_build_visual.py、必要审计回归、UI计划日志与公开时间线证据；不改产品样式/数据。云Chrome1363×936 Light真实加载时间线46条，截图未确认新显示缺陷；拟补四宽度双主题加载、首尾截图/滚动边界、重复加载不重复、刷新后键盘Enter加载同记录。未验收留ui/audit-008d，完整production192+14及新24图、main/live pending；不把DOM/静态测试当视觉通过。gh不可用未编造Issue，无新用户问题，其他Library控件/全站矩阵仍pending。

UI-007/UI-008 done / UI-A08c2限定done（2026-10-15）：base与验收main 3a6258a2cfaca97c281d3d96843c238508f57f63，[run38739750905](https://github.com/AplusNeutrino/My_Blog/actions/runs/38739750905) build116438041048、deploy116441394565、verify-live-ui116441674267全部success；220 tests、4 Ruby、T01/authoring/Jekyll/旧门禁及production/live各192+14通过。live artifact11975492793摘要独立匹配；人工看32张线上四宽度双主题page2/open/combined/cleared图两联系表并放大390 Night面板、390 Light页2、1024 Light组合原图。8分页/筛选流程URL与ID保持、上一页/清除恢复，32诊断scrollX=0且展开面板在viewport内。仅本UI计划/日志及公开live证据回写，不改产品或旧COMPLETE；文档新head CI另核对，无新用户问题。下一项Library时间线，完整库存/离屏加载和其余全站矩阵仍pending，不标全站完成。[证据](docs/ui-evidence/ui007-checks.md#2026-10-15-精确main线上验收)。

UI-007/UI-008生产验收通过、待main/live：base main eb016b52ab6d167a8b1594cef96c6ea3eb1f0dea，验收head51f5e99947ccf1bfce29754efac93d1b5f9740a0 / run38731750252 build116411370430 success，工作分支deploy/live skipped。220 tests、T01/authoring/Jekyll/旧门禁及192+14通过；下载artifact11971222460并核对摘要。实际看32张分页/展开浮层/组合筛选/清除四宽度双主题图两联系表，放大390 Night面板、390 Light页2与1024 Light组合原图；第2页刷新同ID、上一页恢复、来源/年份刷新/清除8流程通过，面板均在viewport内且scrollX=0。只交付已通过修复和公开证据，不追加产品改动；状态仍validation-pending，需实际main head部署/live同场景，不以localhost代替。全站IN PROGRESS，无新增用户问题。[证据](docs/ui-evidence/ui007-checks.md)。

UI-008修复实现bada5371158fb52728bf04f70da4721beb4a6a8a已保存ui/fix-007；本地220 tests/authoring/T01/diff通过，main eb016b52不改。UI-007与UI-008均validation-pending，新检查点head完整production192+14、32新图/矩形/年份诊断及main/live未验收，无新待答问题。

UI-007/UI-008接续validation-pending：base main eb016b52、工作head ab85af5a，run38724996114 build116388845796 failure（年份可见文本断言），deploy/live skipped；218 tests/T01/authoring/Jekyll/旧门禁此前通过。已下载artifact11967657119并看390 Night page2/open/failure原图，第2页刷新保留已通过；高级筛选浮层超出窄屏并触发水平偏移，标题左侧被裁，新增确认UI-008 P2。只修720px内浮层以整个toolbar为定位参照、左右约束；审计补panel真实矩形/scrollX与年份textContent诊断，保留严格年份/URL/ID/刷新断言。文件范围pgl.css、现有审计/必要回归、UI计划日志/证据，不扩大重新设计。先ui/fix-007重新完整192+14及32图，main不变，无新用户问题。

UI-007 validation-pending：实现35139d7bfe0f3cc0620bbd4bfbdbbd3b4d5abe04保存ui/fix-007，main仍eb016b52。本地218 tests、authoring、T01与diff通过，原函数负对照准确捕获加载前页码丢失。计划/日志及公开复现截图已持久化；下轮先核对最终分支head production192+14、新32张分页/筛选图和真实交互，通过后再非强推main与live复验，不以helper单测代替视觉通过。无新用户问题。

UI-007 in-progress / UI-A08c2：base eb016b52ab6d167a8b1594cef96c6ea3eb1f0dea，run38717518673 build116363722730/deploy116366321159/live116366415960全部success已核对。云1363×936 Light实际打开书籍高级筛选、来源Bangumi与年份2011组合、清除及下一页；刷新前页码2，刷新后URL仍category=book&page=2而界面页码1/首项猎魔人卷四，确认P2分页状态丢失。根因首次renderCards在异步目录加载前按空items把page收缩为1。最小范围pgl.js、现有审计/必要回归、UI计划日志；仅在目录加载成功后校正越界页，保留合法page2。四宽度双主题真实下一页/刷新相同ID/上一页、来源/年份/清除及截图为验收；先工作分支production192+14，未验收不进main。高级筛选桌面局部未确认显示缺陷，不猜测改样式；gh未安装不虚构Issue，无新用户问题。

UI-006 done / UI-A08c1限定done：验收main/base ea8b62d58414465661d1f7d88d883e353b9b5b90 / run38710416815 build116340121129、deploy116342302377、verify-live-ui116342443999全部success。215 tests、T01/authoring/production Jekyll/旧门禁及production/live各192+14通过。下载live artifact11960851998并核对摘要，人工看24张线上搜索三状态图两联系表，放大390 Light空状态、390 Night结果与1024 Light清空原图；副标题完整、搜索独立行、未遮挡后续内容。8组搜索刷新/结果/空提示/清空和24矩形通过。本次仅计划/日志与公开live证据，不改产品；文档head CI另核对。全站IN PROGRESS，无新用户问题；下一项UI-A08c2高级筛选/分页，完整库存/离屏加载等仍pending。[证据](docs/ui-evidence/ui006-checks.md)。

UI-006 / UI-A08c1生产验收通过、待main/live：base main c5c40820a23e7d64b7fbdd42ff6d95d1093eb6fb；验收head1edcde07cb948b60a0fac2e275229a0c70769686 / run38703172752 build116316270106 success，工作分支deploy/live skipped。215 tests、T01/authoring/Jekyll/全部旧门禁及192+14通过；下载artifact11956813908并核对摘要，人工看24张搜索三状态截图两联系表并放大390 Light空状态、390 Night结果、1366 Light清空原图，副标题不再被搜索框覆盖。8搜索流程及24真实矩形JSON通过。仅将已通过修复与公开证据非强推main，状态仍validation-pending；必须再核对实际main head build/deploy/live及同24场景截图，不能用localhost替代。文件范围计划/日志与docs/ui-evidence/ui006*，不追加产品改动；其余全站矩阵未完成，无新增用户问题。

UI-006 validation-pending：修复实现960fa5a51518453d85a1f6bccf2b0529197ac40d保存在ui/audit-008c；[run38703062082](https://github.com/AplusNeutrino/My_Blog/actions/runs/38703062082)已触发、当前in-progress，尚无修复后视觉或线上验收。本地215 tests/authoring/T01/diff通过，8个远程blob哈希与本地逐一相同。仅追加此实现SHA检查点，新文档head CI另核对；main仍c5c40820。下轮先核对最终分支head完整production和24张搜索状态截图/矩形JSON，通过再非强推main及live复验。无新待答问题。

UI-006 in-progress（UI-A08c1截图发现）：base main c5c40820a23e7d64b7fbdd42ff6d95d1093eb6fb / 工作head c5fd955a632a1722b1c9f73618041a7f0738307d。环境已恢复，下载e6a54de2 artifact11951832064并核对sha256；人工看24张搜索状态图两联系表及390 Light空状态、1024 Night结果、768 Night清空原图，确认390px双主题搜索框遮挡副标题。P2，根因为720px内搜索框绝对定位于按钮容器、未占布局空间。拟改assets/pgl/pgl.css、现有搜索审计、必要回归、UI计划日志及公开前后证据；改为标题/按钮一行、搜索独立一行，保留展开收起/输入/URL，不重新设计。验收四宽度双主题结果/空状态/清空无标题或后续内容遮挡、页面不溢出，原213 tests/T01/authoring/Jekyll/旧门禁保持，精确head生产与线上截图复验。未验收留工作分支，不以原CI成功宣称无缺陷；gh未安装不虚构Issue，无新用户问题。

UI-A08c1 validation-pending（2026-10-15 远程证据核对）：base/main c5c40820a23e7d64b7fbdd42ff6d95d1093eb6fb；验收分支head e6a54de259b8c67d5bc6e6f0214e1bd519eaea7f。[run38689759158](https://github.com/AplusNeutrino/My_Blog/actions/runs/38689759158) completed/success，build116272713219 success，deploy/live按工作分支规则skipped。213 tests、T01保护、authoring44/5/7、production Jekyll与192场景浏览器检查通过；artifact11951832064，sha256:c2e1b65ce679fe223d0bd0b7cce819d8275c1c6064bc9ebac21b8b213fa35df9。当前执行环境握手失败且无可调用本地执行/浏览器工具，不能下载解包并人工查看24张搜索状态截图；仅核对日志与artifact元数据，不宣称视觉通过。范围仅本UI计划/日志远程检查点，代码、main、线上和旧COMPLETE历史不改；新检查点head CI另核对。恢复后先查看同一验收head四宽度双主题结果/空状态/清空截图，再决定main与部署后复验。gh CLI本轮无法执行，未创建Issue；无新用户问题，临时环境故障不标COMPLETE或永久blocked。

UI-A08c1 in-progress：base c5c40820a23e7d64b7fbdd42ff6d95d1093eb6fb，run38684810581 build116257125018/deploy116258814970/live116258877904全部success。最小范围现有审计/必要helper回归/计划日志：Library输入站内公开书名、结果/URL、刷新保留、无结果提示、清空返回，四宽度双主题8流程截图。云1363×936 Light实际输入“猎魔人”显示9条结果，截图已看未确认新缺陷；不改产品。筛选/分页拆至UI-A08c2后续，先工作分支production192+14，main/live pending，无新用户问题。

UI-A08b限定done：验收main/base57a6817cd90f27f41039c92040c38ff3de53a03e / run38679922788 build116241892225、deploy116243565530、verify-live-ui116243614933全部success。211 tests、4 Ruby、T01/authoring/Jekyll/旧门禁及production/live192+14通过。下载live artifact11946904727，8场景56次可见封面complete/原生尺寸/解码通过；人工看8张线上截图两联系表并放大390 Light原图，没有空白封面或新增确认缺陷。仅回写计划/日志/公开证据，新文档head CI另核对。下一项UI-A08c Library搜索/筛选/分页，完整库存/离屏加载及全站剩余矩阵pending，无新待答问题。[证据](docs/ui-evidence/uia08b-checks.md)。

UI-A08b生产通过、待main/live：base main30e26ead4ee97aa6bc3120aec3372897bb1285bc，验收head aa328fa7b8f5e09d58adbe3d8aada6f7ae0f8b03 / run38674518402 build116224939740 success，分支deploy/live skipped。8场景56次可见封面complete/尺寸/原生decode通过；人工查看8张解码后截图两联系表并放大390 Night原图，均显示封面，无新增确认产品缺陷。211 tests/4 Ruby/T01/authoring/Jekyll/旧门禁及192+14通过；只交付审计和公开证据，不改样式或图片源。非强推main后核对实际head部署及live8图/加载记录，仍validation-pending，搜索/筛选/分页等另项pending，无新问题。[证据](docs/ui-evidence/uia08b-checks.md)。

UI-A08b接续validation-pending：base main30e26ead、工作head de7dbdf4；run38668866802 build116206975426 success、deploy/live skipped。下载artifact11942794466，8场景56次可见封面complete/尺寸全部通过；实际看8张covers截图及390 Night后续category原图，前者局部空白、后者封面已显示，不能以尺寸成功替代视觉。现有decoding=async可在load后下一paint显示，审计仅补原生decode()与两帧后采图，不修改src/loading或网站产品。文件范围现有审计/4项helper回归/计划日志；生产192+14与新截图待精确head重验，不进main，无新用户问题。

UI-A08b in-progress：base30e26ead4ee97aa6bc3120aec3372897bb1285bc，run38663584681 build116190250811/deploy116192067722/live116192142932全部success已核对。最小范围tools/check_think_build_visual.py、封面审计回归、本计划日志；仅检查书籍目录当前viewport内img.pgl-cover，等待真实complete并记录naturalWidth/currentSrc，再截图；不改src/loading、不强制加载、不猜测修产品。四宽度双主题8加载场景，完整192+14及线上验证pending。搜索/筛选/分页等另项pending，先工作分支，无新用户问题。

UI-A08a限定done：验收main/base85980c7e95f2407bbfb9232fafaf5e8cf9f485b4 / run38657575079 build116170877784、deploy116172735660、verify-live-ui116172823721全部success。207 tests、4项Ruby、T01/authoring/production Jekyll/旧门禁与production/live192+14通过。下载live artifact11937374039，人工查看40张线上关系场景四联系表，放大390 Light弹层及768 Night友链焦点原图，16限定交互通过。部分目录封面在截图时尚未加载，完整图片加载专项保留pending，不当作已修复或视觉正常；仅回写计划/日志/公开证据，不改产品。新文档head CI单独核对；下一项UI-A08b优先补可见封面加载状态和Library搜索/筛选/分页，其他全站矩阵仍IN PROGRESS，无新待答问题。[证据](docs/ui-evidence/uia08a-checks.md)。

UI-A08a生产通过、待main/live：base main9809089372832f3d6ff7a499a85c48755da7208e；验收head d770c3565f03c537ef23273423b6ee98f139dcef / run38651914436 build116152939726 success，工作分支deploy/live skipped。207 tests、4项Ruby、T01/authoring/production Jekyll/旧门禁及192+14通过；下载artifact11935087411、人工查看40张关系场景截图四联系表并放大390 Light弹层和1024 Night友链焦点原图，未确认新产品缺陷。仅审计/计划日志与公开证据非强推main，保留同步数据；实际main head部署及live同场景仍validation-pending。全站IN PROGRESS，无新待答问题。[证据](docs/ui-evidence/uia08a-checks.md)。

UI-A08a接续 validation-pending：base main98090893、branch22b184d3；run38644349352 build116127411671 failure，deploy/live skipped。390 Night Library弹层/目录/返回已通过，友链焦点失败。下载artifact11931034197并实际看弹层、目录和友链失败截图，无新增确认产品缺陷；Element.send_keys每次先聚焦目标，原脚本对同一卡片发Shift+Tab实际移走焦点，不是全局反向Tab。仅改审计为ActionChains真实全局Tab遍历、Tab/Shift+Tab往返，保留严格activeElement断言，并补焦点tag/class/href诊断。范围审计/计划日志；192+14、四宽度两主题完整截图与线上仍pending，main不改，无新用户问题。

UI-A08a接续 validation-pending：branch7ca4df8a/run38636477276失败于390 Night目录打开后的返回click；已下载artifact11928481822查看目录截图/JSON，category=book、drawerOpen=false、scrollY161。原弹层与目录click已通过，pgl分类事件启动smooth scroll，返回点击可能在滚动中。只补返回按钮instant居中、两帧与viewport hit-test再真实click，截图在稳定视口记录，所有原断言保留。main新增9809089372832f3d6ff7a499a85c48755da7208e为9个Library同步数据文件，已无冲突合并进工作分支并原样保护；不回退同步。范围仍审计/计划日志，main不改、192+14与线上验收pending，无新用户问题。

UI-A08a接续 validation-pending：base maina5738952、branch57efc919，run38628620429 build116074140246失败于390 Night弹层关闭后目录click坐标y1621被拦截；此前207 tests/Ruby/T01/authoring/Jekyll/旧门禁通过。下载artifact11926170787查看失败截图，页面在首屏、弹层已闭；close事件异步恢复opener焦点可能与下次自动滚动竞争。本轮仅修审计：等待恢复焦点及两帧，再instant滚动目录、hit-test后真实click，补失败几何JSON，不放宽目录/弹层/URL断言，不猜测改产品。main未改，完整192+14和线上矩阵仍pending，无新用户问题。

UI-A08a in-progress：base a5738952dc9584e4e8282dbd5090bfe17992e2af，run38620953323 build/deploy/live全部success已核对。范围仅tools/check_think_build_visual.py、本计划/日志；Library根页/当前条目弹层/书籍目录返回、友链卡片href与键盘焦点，四宽度双主题16页面场景（总192+14）。云1363×936 Light已实际查看上述界面和操作弹层/目录，无新增确认缺陷，不改产品。时间线/高级筛选/分页/搜索与外部站点可用性另留pending；先ui/audit-008分支production，未验证不进main，无新用户问题。

UI-A07b done（限定两篇公开文章Copy link）：base/验收main aa3dbcec717bbbec27e02c0dd196fb0822a6fdec，[run38611417490](https://github.com/AplusNeutrino/My_Blog/actions/runs/38611417490) build116015462124、deploy116017753847、verify-live-ui116018039763全部success。207 tests、4项Ruby、T01/authoring/production Jekyll/旧门禁、production/live各176+14通过；16线上clipboardBytes=verified、sentinel已替换、copiedUrl精确等于当前https://neutriverse.uk URL。人工查看16复制反馈四联系表并放大四宽度代表原图，无新增确认缺陷。只回写计划/日志与公开证据，不改样式或内容；新证据文档提交CI另行核对。下一项Library/友链四宽度双主题目录/延迟加载/链接矩阵，全站IN PROGRESS，无新增用户问题。

UI-A07b生产通过、待main/live：base main536281728dcc314c71c64936b06334b2f74bb800，审计验收head e431aeaced355ccb155595fe912860a4007f59dd / run38604621533 build115992207806 success，分支deploy/live skipped。207 tests、4项Ruby、T01/authoring/Jekyll/旧门禁、176+14场景通过；16实际剪贴板内容精确等于当前URL，sentinel均替换。人工查看16复制反馈截图的四联系表并放大1366 Light代码原图，没有新确认缺陷。仅将已验证审计和[证据](docs/ui-evidence/uia07b-checks.md)非强推main，状态仍validation-pending；下一轮核对实际main head build/deploy/live与16线上复制记录/截图，不以localhost复制通过代替线上。其余矩阵IN PROGRESS，无新用户问题。

UI-A07b validation-pending：审计实现2892b031dc0e0de8493bbe03a7b10ce1a24620b9，本机207 tests/authoring/T01/diff通过，未冒称真实剪贴板或视觉验收。上一文档head536281728dcc314c71c64936b06334b2f74bb800的run38595958153重试build115988897946、deploy115988897534、live115989007513均success，部署恢复；首次超时历史保留。现在将实现和状态非强推保存ui/audit-007b，main不改，下一轮先核对其精确head生产CI与剪贴板16记录/截图，再决定main及live。无新增用户问题。

UI-A07b in-progress：base536281728dcc314c71c64936b06334b2f74bb800；范围仅tools/check_think_build_visual.py、必要审计回归、本UI计划/日志。补16公开阅读场景复制实际字节：浏览器测试origin授予clipboard读写权限，先写不等于URL的sentinel，真实点击原按钮，再读系统clipboard并严格等于当前完整URL，保留原成功提示和所有视觉/媒体门禁。未确认产品缺陷不改样式。先工作分支production，通过后main/live；没有把未运行的检查标done。上次文档run38595958153部署十分钟updating_pages超时，已重试失败jobs；同head重试deploy成功、live尚在运行，不暂停任务或修改部署超时阈值。无新用户问题。

UI-A07 done（限定代码/图片/媒体与复制提示）：验收main/base cd4ec29eb1ab500563b9247af7ae98ac1661438a，[run38590193242](https://github.com/AplusNeutrino/My_Blog/actions/runs/38590193242) build115942706728、deploy115945097313、verify-live-ui115945238565全部success。176+14线上检查通过，人工查看新增40张截图的四联系表并放大四宽度代表图，代码/图片/弹层无新增确认缺陷。本轮只回写计划/日志与公开live证据；正文/metadata/样式未改，旧COMPLETE历史不动。文档提交CI另行核对；UI-A07b剪贴板实际字节仍pending，下一项先核对文档head再补实际复制或Library/友链矩阵，全站IN PROGRESS。无新增用户问题。

UI-A07生产通过、待main/live：审计head2c60e4e1aeff6897447e6a0a90a65251869f547f / run38588924737 success；205 tests、4项Ruby、T01/authoring/Jekyll/旧门禁、176+14通过。新增16阅读场景、真实移动touch/桌面arrow/关闭及复制提示通过；人工看40张viewport/gallery/feedback联系表，放大代表原图，无新增确认产品缺陷。审计与[证据](docs/ui-evidence/uia07-checks.md)非强推main，精确head线上矩阵仍validation-pending；UI-A07b剪贴板实际字节pending，不以成功提示代替。下轮先核对main/live再继续复制实值/未检页面，无新增用户问题。

UI-A07（检查，不预设缺陷）：base c5b99ed2284ac327270de5c952f0a026d85d87b3，run38577189934 completed/success已核对。范围现有浏览器审计、计划/日志及公开证据；代表计组07plain代码、FF1公开图片，390/768/1024/1366×Night/Light，共16场景。验收代码/图片可见且不引起整页溢出、图片逐张lazy加载及弹层下一张/返回/关闭、复制链接反馈；剪贴板实际字节明确pending。候选高亮示例因hidden排除，不生成公开截图。桌面1363×936已看代码/图片并操作弹层翻页，没有新增确认缺陷，不猜测改产品。先ui/audit-007验证；本轮不改旧文章/metadata/URL/hidden/noindex。无新增待答问题。

UI-005 done：base/main5922412f7fc82af68984091e75c142242c290cec，[run38570020301](https://github.com/AplusNeutrino/My_Blog/actions/runs/38570020301) build115872459830、deploy115874598655、verify-live-ui115874783745均success。4项Ruby渲染回归、205 tests、T01/authoring/production Jekyll/全部旧门禁、生产与live各160+14通过。下载live artifact11898410699，看8张表格viewport联系表并放大四宽度代表图，1366 Light全页两表复核，行列恢复且横向阅读通过。只回写计划/日志/公开证据，本次没有额外产品修改；文档提交CI另行核对。下一项代码/图片/复制/媒体阅读场景，完整矩阵仍IN PROGRESS，无新增用户问题。[证据](docs/ui-evidence/ui005-comparison.md)。

UI-005生产通过，待main/live：实现head c20396fa62672943eda5d675955cc6eeb394d3ea，[run38569176497](https://github.com/AplusNeutrino/My_Blog/actions/runs/38569176497) build success；4项Ruby渲染回归、205 tests、T01/authoring/Jekyll/旧门禁、160+14浏览器矩阵通过。已查看8张表格截图并放大390 Light/1366 Night，真实横向滚动通过；没有更改旧md。准备非强推main并核对其实际head部署后同场景，UI-005保持validation-pending；[前后记录](docs/ui-evidence/ui005-comparison.md)。无新增待答问题，代码/图片阅读仍pending。

UI-005 / UI-A06：base9708457fee99f7a00d8d74bb13bf59d669687ad4，run38560753961 completed/success已核对。1363×936线上计组04 Light实际截图确认两张表格为pipe prose，DOM为0 table；原md有合法header/separator但紧邻ATX标题。最小范围：render-only post hook、Ruby渲染回归、现有CI与8场景表格截图/横向操作、计划日志；不改正文源/metadata、配置全局parser或其他页面设计。先ui/fix-005，生产与线上截图pending；完整代码/图片阅读检查仍pending。无新增用户问题。

UI-A05 done（限定检索页截图与已列交互）：base/main head f755f17c3e1f1a1b66eee714ef4b8ff8aec73cfb，[run38554989713](https://github.com/AplusNeutrino/My_Blog/actions/runs/38554989713) build/deploy/verify-live-ui全部success；205 tests、T01/authoring/production Jekyll/旧门禁、production与live各152+14通过。下载live artifact11890351589，人工查看32张检索viewport（四张分宽度联系表）及390 Light Tags、768 Night Thoughts、1024 Light Archive、1366 Night Series原图。未确认新产品缺陷，本次仅证据文档更新，不修改网站样式/内容；文档提交CI另行核对，不冒称其已通过。下一项代表文章代码/表格/图片阅读矩阵，Thought点赞等仍pending；全站IN PROGRESS，无新增待答问题。

UI-A05生产检查通过，等待main/线上复验：head f3d51b79f1b8e813fa7e94b4ebc2592772566277 / run38554138564 success；205 tests、保护/authoring/Jekyll/旧门禁、152场景+14侧栏专项通过。新增32检索截图与32组往返操作已核对，联系表人工查看；未确认新产品缺陷，没有改样式。将审计+证据非强推main，状态validation-pending。下一轮先核对本次main head的build/deploy/live152+14与截图，然后继续Thought其他交互/代表文章等矩阵。详见[UI-A05记录](docs/ui-evidence/uia05-checks.md)，无新增待答问题。

UI-A05本轮接续：base main93825c66 / branch2114197f，run38548101812失败诊断已取回；Archive打开post按既有规则存储侧栏collapsed，下一页主题按钮因此在inert侧栏。审计补真实召回按钮后再检查主题，不修改产品规则。先ui/audit-005精确head验收，32新检索截图与main/live仍pending；失败PNG/JSON来源artifact11884993704。

UI-A05检查进行中：base93825c66/run38541205915 success；Tags/Archive/Thoughts独立页+THINK内Series目录32双主题四宽度截图及往返操作。Tags桌面首屏与长标签详情跳转已实际检查，尚未确认新缺陷；不猜测改样式。工作分支新增检查pending，其他页面矩阵仍保留pending。

UI-A05工作分支ui/audit-005：6bcac453的Series hash预期失败已修正；6d0df28f生成95场景但主题按钮不可交互失败；诊断a38ff743/run38547751557在原mobile gate关闭动画中的pointer点击被topbar-title拦截，未进入新矩阵。补原gate点击前等待有限动画结束，焦点/真实click/所有断言不变。部分20张检索viewport联系表已看（390/768双主题+1024 Night），暂无新增确认产品缺陷；1366和1024 Light/完整生产及live矩阵pending。下轮先检出该工作分支精确head核对CI，不重做历史已done事项。

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
