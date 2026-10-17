# UI-015 — 公开说明/状态/日期的固定按钮避让

状态：done（仅UI015四类已确认遮挡）；精确main构建/部署/线上同场景人工复验通过。历史失败和部分验收记录保留，不代表当时已完成；全站矩阵仍IN PROGRESS。

## 2026-10-18 精确main部署与线上限定验收

- Base/验收main `c001784bd31e67ce6da8512ceedcf058922c9261`，实现为7f61a5f1；[run39052090726](https://github.com/AplusNeutrino/My_Blog/actions/runs/39052090726) build117452566638、deploy117456022205、verify-live-ui117456065349全部completed/success。线上job明确 `UI_LIVE_BASE=https://neutriverse.uk`；不以旧head成功代验。
- 256 tests、Ruby渲染、T01正文/metadata/URL/hidden保护44/5/5、authoring44/5/7、production Jekyll、Search/feed/SEO/路由/资源和全部既有门禁通过；production/live各192主场景、14侧栏、24公开流程/177原生滚动帧完整通过。字体等待未再失败，但旧5面loading原因仍未证实，保留诊断与30s/20s时限，未宣称修复字体根因。
- live artifact12109095954，492573504 bytes，独立SHA256 `55aea233c4877d45ee0007e7d89f1d725a7bcbda7ebb7591d59477a7a95209de` 与GitHub digest匹配。实际逐张查看UI015目标可见的45线上帧/[18联系表](ui015-live-contacts/)，覆盖390/768/1024/1366×Night/Prospero Light；原四个390 Night场景放大重新对照before：[维护](ui015-live-about-maintenance-390-dark.png)、[理念](ui015-live-about-principle-390-dark.png)、[日期](ui015-live-about-date-390-dark.png)、[状态](ui015-live-observe-meta-390-dark.png)。来源说明与“新的结构”尾字、2026/02/06日期、NOINDEX状态均完整，按钮不再遮挡，主题/卡片外框/列数保留。
- [线上24流程/45帧及生产对照摘要](ui015-live-summary.json)：ABOUT/OBSERVE16流程共121帧detailTextButton分组诊断与已验收7f61生产逐项完全相同，目标存在且逐个非空、严格真实文字行交集均0；24流程frame数量、公开往返目标一致，scrollY最大差0。每流程无横向溢出，16流程真实滚轮覆盖main、返回顶部pointer click、项目事实页/Library/友链往返通过。这里区分自动121帧诊断与45帧人工视觉，不冒称全部177帧或整页矩阵人工完成。
- 本机256 tests、authoring44/5/7、T01保护44/5/5、diff再次通过，本机无Jekyll/Chrome；独立worktree不触碰原目录用户字体/缓存/未跟踪文件，gh仍不在PATH不编造Issue。AGENTS/docs/agents/ADR、旧COMPLETE与当前计划/日志、用户补充已核对，CONTEXT无。
- 本轮只更新本UI计划/日志与公开live证据，不追加产品/数据/旧正文/metadata/filename/date/slug/permalink/URL/hidden/noindex或关联仓库修改。UI015限定done；新证据文档head的CI单独核对，全站仍IN PROGRESS，无新确认缺陷/用户待决问题。下一项先核对证据head，再补UI-A09剩余整页截图与交互或其他尚未覆盖矩阵，不重复审美修改。

## 2026-10-18 同head重试通过，限定生产视觉验收

- 验收实现 `7f61a5f154f9736816e8a379b74ecacc6f3f8b43`；[run39043515933 attempt2](https://github.com/AplusNeutrino/My_Blog/actions/runs/39043515933/attempts/2) build117439836139 completed/success；工作分支deploy117443253294、live117443253210按条件skipped，不冒称部署。原30s字体/20s动画等待与全部门禁未修改；本次未复现字体等待失败，但不能据此宣称字体根因已修复。
- 256 Python tests、Ruby渲染、T01保护44/5/5、authoring44/5/7、production Jekyll、Search/feed/SEO/路由/资源与全部原门禁通过；主192、侧栏14、公开24流程/177原生滚动帧完整。artifact12106114081，492265573 bytes，独立SHA256 `cc093dac6e3a061ab546c7c7222e156840cfcc7ef8d4ff9d5016fbd7f0ba5727` 匹配。
- 人工逐张查看四宽度390/768/1024/1366 × Night/Prospero Light中四类目标可见的45帧，汇成[18张联系表](ui015-production-contacts/)；放大[维护](ui015-production-about-maintenance-390-dark.png)、[理念](ui015-production-about-principle-390-dark.png)、[日期](ui015-production-about-date-390-dark.png)、[状态](ui015-production-observe-meta-390-dark.png)四张390 Night原图，对应before中尾字、2026/02/06日期及NOINDEX状态现在完整可见，固定按钮不再遮字。卡片外框/列数/主题保持；768/1024状态正常换行，1366原布局未改。只验收UI015作用域，不声称全部177帧或全页矩阵人工通过。
- [完整24流程与45帧选取摘要](ui015-production-summary.json)：ABOUT/OBSERVE共16流程的每类目标存在且非空，逐行严格按钮交集均0，intro旧门禁仍通过；连续真实滚轮覆盖main，返回顶部pointer click与公开链接往返通过，无横向溢出。自动诊断与人工看图分列，静态回归不替代视觉。
- 本机再次256 tests、authoring44/5/7、T01保护44/5/5、diff check通过；本机无Jekyll/Chrome，以上生产浏览器证据来源精确head CI。gh仍不在PATH，未编造Issue。
- fresh main仍 `097129418f5a014d3d1d85b2441f934854dcda3a`。交付包含实现7f61与失败证据56d3bef的后续提交，仅新增上述证据及计划/日志，本轮不再改产品。合main后必须核对新main自身Actions/build/deploy，再取同场景线上原生图对照，之前保持validation-pending。无新缺陷/待决问题，全站IN PROGRESS；UI-A09及其余未覆盖矩阵不标done。

## 2026-10-18 同head生产失败与受控重试

- 真实实现 `7f61a5f154f9736816e8a379b74ecacc6f3f8b43` / [run39043515933](https://github.com/AplusNeutrino/My_Blog/actions/runs/39043515933) attempt1 build117427571131 failure、deploy117430042339/live117430042559 skipped。256 tests/Ruby/T01/authoring/Jekyll/产物及前置门禁通过；仅主144/192、公开18/24共139帧，侧栏0。
- artifact12104867929，331800012 bytes，独立sha256 `c46f5b02fdd9f9fd168d8b426eae27ab01954d2be1c5016d68d7bda35317fd4f` 匹配。已实际放大[维护](ui015-partial-about-maintenance-390-dark.png)、[理念](ui015-partial-about-principle-390-dark.png)、[日期](ui015-partial-about-date-390-dark.png)、[状态](ui015-partial-observe-meta-390-dark.png)四张390 Night修复后原图，原尾字/日期完整且按钮不重叠。[部分18流程摘要](ui015-partial-production-summary.json)显示三宽双主题严格文字交集均0；139帧未全人工验收，1366与完整/main/live仍pending。
- [失败1366 Night原图](ui015-font-failure-1366-dark.png)及[字体诊断摘要](ui015-font-failure-summary.json)已保存，摘要保留原JSON SHA256/5个loading面/51条Font网络元数据，完整JSON仍在原artifact。5面loading：Noto Sans SC400/500/600、Noto Serif SC400/600；51条捕获请求均HTTP200/fromDiskCache/finished，无捕获未完成或失败请求。只说明本次捕获范围，不足证明CDN/浏览器根因，未推测修改产品字体。
- 原30s fonts.ready与20s有限动画等待、全部门禁不变；本轮仅一次同head受控重试attempt2 build117439836139运行中。不移动ui/fix-015/main，证据存verification/ui015-7f61-retry避免取消重试；下一轮先核对同head，若再次失败先比较诊断，不以重试代替根因分析。没有新产品缺陷或用户待决问题。

## 实现前范围（2026-10-17）

- Task UI-015 / P2；base main `097129418f5a014d3d1d85b2441f934854dcda3a`，工作分支拟 `ui/fix-015`。main原用户修改不动。
- 实际原生图已重新查看：[ABOUT理念](ui015-before-about-principle-390-dark.png)、[书目日期](ui015-before-about-date-390-dark.png)、[维护说明](ui015-before-about-maintenance-390-dark.png)、[OBSERVE状态](ui015-before-observe-meta-390-dark.png)。390 Night固定按钮覆盖尾字/日期/NOINDEX状态，不是审美偏好。生产来源ad1540d0 artifact12100198625；维护说明来源d1bdcbf2 live artifact12102362109。
- 根因：这四个文字作用域不在首页/UI014的文字通道中，普通内边距仍允许文字进入固定44px按钮区域。
- 最小产品文件：`assets/css/neutriverse-sections.css`。仅缺少右侧辅助栏的宽度内给已确认的ABOUT理念列表、维护说明、书目条目及OBSERVE卡片状态留文字通道；保留容器外框/列数、主题、字号、正文、模板、数据及全站共享按钮。不把旧br空白当缺陷。
- 审计：`tools/check_think_build_visual.py`、`tests/test_public_page_sweep_audit.py`。保留首页/UI014所有原逐行Range断言；新增四类目标分别必须存在且含文字、逐行严格无按钮交集，失败保留PNG/JSON。原192+14/24public、字体/动画等待与其他门禁不减。
- 文档：本文件、本轮计划/日志。gh不在PATH，不用API冒充Issue操作，不虚构编号；CONTEXT不存在，AGENTS/docs/agents/ADR/旧COMPLETE与本轮台账和用户补充已核对。

## 验收

本机全回归、authoring、T01正文/metadata/URL/hidden保护、diff；精确分支head production Jekyll及产物/全部原门禁，390/768/1024/1366×Night/Light连续原生截图人工查看，放大原四处场景；真实滚轮、返回顶部及公开链接往返。通过后才合main；该main自身build/deploy/live同场景截图复验完成才done。当前validation-pending，不以静态测试替代视觉。

## 上一证据head

`09712941` / [run39038972286](https://github.com/AplusNeutrino/My_Blog/actions/runs/39038972286)：build117414389679/deploy117417289853/live117417342881全部completed/success，关闭该文档提交CI pending。不用它替代本次实现验证。

## 本次实现及真实验证边界

- 仅<=1199.98px的四类作用域：理念li、维护dd、OBSERVE状态meta增加右padding2.75rem；书目time为absolute，单独right:calc(0.62rem + 2.75rem)。不动卡片外框/网格列数/字号/主题、旧文本/模板/数据、全站按钮或>=1200px。
- detailTextButton按selector分组保存rootCount/emptyRoots/lines/overlaps、可见按钮矩形；每类目标必须存在且逐个有文字，任何真实文字行交集都拒绝，并保存原生PNG与完整诊断。原首页recentTextButton及UI014 introTextButton断言原样保留。
- 本机256项tests、authoring44/5/7、T01保护44/5/5、git diff --check通过；没有本机Jekyll/Chrome或新head修复后截图，不冒称视觉正常。当前production/人工截图/main/live均validation-pending，留ui/fix-015。
