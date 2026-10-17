# UI-016 — ABOUT关系卡片说明被固定按钮覆盖

状态：done（仅UI-016关系说明作用域）。5862ab0e同head attempt2完整build/deploy/live及部署后人工复验通过；全站矩阵仍IN PROGRESS，新证据提交自身CI另核对。

## 2026-10-18 同head部署与线上限定验收通过

- 精确main `5862ab0e14211edf63f264593638a5131c003616` / [run39067300977 attempt2](https://github.com/AplusNeutrino/My_Blog/actions/runs/39067300977/attempts/2)：build117502673032、deploy117505713846、verify-live-ui117505765011全部success。258 tests、Ruby渲染、T01保护44/5/5、authoring44/5/7、production Jekyll/Search/feed/SEO/资源/旧门禁及production/live各192主场景、14侧栏、24公开流程177原生帧通过；live日志明确https://neutriverse.uk。
- live artifact12114393947，490933485 bytes；独立SHA256 `c96fee2114716eb82ccbcd12aa8f08242c9c95e69d706f1898da455668a31011`匹配。实际查看四宽度双主题关系说明可见的12帧/[8联系表](ui016-live-contacts/)，放大[390 Night线上原图](ui016-live-about-relations-390-dark.png)对照before，原说明全文避开圆钮，卡片边框/标题/链接/双主题保留，未确认新增显示缺陷。未把全部177帧自动诊断当人工全页验收。
- [线上摘要与production对照](ui016-live-summary.json)：24流程帧数/往返目标一致、scrollY最大差0；ABOUT8流程关系组诊断与已验production完全相同，每帧rootCount3、emptyRoots0、严格文字行overlaps=[]。真实原生滚轮覆盖main、返回顶部pointer click、Library/友链点击及浏览器返回通过；scrollX0且无横向溢出。
- 保留以下attempt1失败、旧live取消及完整原始诊断；此次成功不证明有限动画等待的内部根因已解决。没有修改产品/审计/等待时限或门禁、Library同步/原文/metadata/URL/hidden/noindex。gh不在PATH，不编造Issue；本机258 tests/authoring/T01/diff再通过，本机无Jekyll/Chrome。
- UI016限定done；A09剩余整页与其他矩阵pending，无新用户决策。只提交计划/日志/公开证据，父1776aa4保留失败历史，非强推且fresh main必须仍5862；新文档head自身CI/deploy/live另核对，不用本成功代验，不将全站标COMPLETE。

## 2026-10-18 已部署head的live取消；最新main返回等待失败

- 实现交付main `8095f4a579926e9f35bf859e52f731c39c2dde9a` / [run39065426364](https://github.com/AplusNeutrino/My_Blog/actions/runs/39065426364)：build117491963533、deploy117495092346 success；verify-live-ui117495142367 cancelled，不将部分线上artifact当完整通过。
- fresh main变为 `5862ab0e14211edf63f264593638a5131c003616`，唯一新增提交为既有Library同步，修改6个library/source/sync_status数据文件；UI产品/审计/指令/ADR/旧COMPLETE计划报告均未变。保留该同步，不回退main；workflow共用pages并设置cancel-in-progress:true，与旧live被新运行中断的时序一致。
- 最新[run39067300977](https://github.com/AplusNeutrino/My_Blog/actions/runs/39067300977) attempt1 build117497614664 failure，deploy117499783132/live117499784181 skipped。258 tests、Ruby渲染、T01保护44/5/5、authoring44/5/7、production Jekyll/Search/feed/SEO/资源/前置门禁通过；主144/192、公开17/24完成、139原生公开PNG、侧栏0。第18个ABOUT流程已采图但Library返回后未完成，因此17不是18。
- failure artifact12114355647，331667680 bytes，独立SHA256 `3d5b34e9703fc516267bff95cdffaca610c6da5d0da0a123358c224f61f271cc`匹配。已人工查看[1024 Light返回失败原图](ui016-return-stalled-1024-light.png)，未在该图确认新显示缺陷；[完整动画诊断](ui016-return-stalled-1024-light.json)明确phase=settle-after-browser-back、destination=/library/、readyState complete、scrollX0/scrollY2997。两条有限过渡background-color180ms（ABOUT入口）及opacity500ms（返回顶部），iterations1/state running/currentTime0/startTime null；其余永久装饰不是原门禁阻塞项。不能据此断言BFCache/浏览器根因或删除动画/延长等待，亦不能归咎Library数据。
- [部分17流程/9个关系说明可见帧诊断摘要](ui016-5862-partial-summary.json)保留原失败JSON SHA256、流程/原生帧计数与关系Range；三宽双主题目标3/非空/交集0，只是部分自动证据，9帧未全人工查看，1366/完整production/部署/live仍pending。原完整包留精确artifact14天，不冒称整页视觉通过。
- fresh main未再移动后，对最新5862的失败jobs仅做一次受控同head重试：attempt2 build117502673032 in_progress。未重新运行旧8095、未改任何产品/审计/时限/门禁，也未用旧成功代验。若再失败，先比较两次诊断，不连续重试宣布通过。
- 本机258 tests、authoring44/5/7、T01保护44/5/5、diff再次通过，本机无Jekyll/Chrome。AGENTS/docs/agents/ADR/旧COMPLETE及本轮台账、用户补充核对，CONTEXT无，gh不在PATH不编造Issue。证据存verification/ui016-5862-return-retry，main和ui/fix-016不移动以免取消重试；不覆盖原目录用户修改/Library同步，其他内容/URL/hidden/noindex/外部仓库不动。全站IN PROGRESS，无新确认缺陷或用户待决问题；下一项核对同一5862重试及部署/live截图。

## 2026-10-18 精确production与限定视觉验收

- 验收实现 `a17ee7ec0db3e4fe9f534fa76bf7f663d5b5d0f9` / [run39060823145](https://github.com/AplusNeutrino/My_Blog/actions/runs/39060823145)，build117478235105 completed/success；工作分支deploy117481148392/live117481148909按规则skipped，不冒称已部署。
- 258 Python tests、Ruby渲染、T01正文/metadata/URL/hidden保护44/5/5、authoring44/5/7、production Jekyll、Search/feed/SEO/资源/路由/全部旧门禁通过；主192、侧栏14、公开24流程177原生帧完整通过。原字体30s/有限动画20s及所有旧逐行文字门禁保持。
- artifact12111467085，492254922 bytes，独立SHA256 `9c9b2dd0acf172a5e38164493c5eb37ba26907de50cb7493cf269aa32397dfea`匹配GitHub digest。首次取得artifact遇MCP请求超时，随后同artifact重取成功；未重跑CI/换head，没有把下载故障当产品失败。
- 实际逐张查看关系说明可见的12帧/[8联系表](ui016-production-contacts/)，覆盖390/768/1024/1366×Night/Prospero Light。放大[390 Night修复后原生图](ui016-production-about-relations-390-dark.png)并对照before：“站点邻居与互联网往来继续保存在现有友链页面。”全文完整，按钮与正文分离。原卡片外框/列数/标题/链接/主题保持，较窄列说明自然增加换行，无裁切或横向溢出；1366布局不变。
- [24流程与选取帧摘要](ui016-production-summary.json)：ABOUT8流程每帧关系目标rootCount=3、emptyRoots=0、严格真实文字行overlaps=[]；原intro/UI015等门禁保留。8流程连续原生滚轮覆盖main，末端真实返回顶部与Library/友链点击、浏览器返回通过。只人工验收12关系目标帧，不声称全部177帧或A09整页通过。
- 本机258 tests、authoring44/5/7、T01保护44/5/5及diff再次通过，本机无Jekyll/Chrome。AGENTS/docs/agents/ADR/旧COMPLETE计划报告/本轮计划日志及用户补充已核对，CONTEXT无，gh不在PATH不编造Issue；独立worktree不覆盖原目录用户字体/缓存/未跟踪文件。
- fresh main仍 `8bff45a9e83f1598dd7d248e5aaeb8350d7a2889`，本次只增加公开验收证据及计划/日志，不追加产品修改。非强推交付后必须核对新main自身Actions/build/deploy/live并人工看同场景，之前validation-pending；全站仍IN PROGRESS，无新确认缺陷或用户待决问题，UI-A09剩余整页与其他矩阵不标done。

## 2026-10-18 实现前范围与复现

- Task UI-016 / P2，base main `8bff45a9e83f1598dd7d248e5aaeb8350d7a2889`。此head [run39056732011](https://github.com/AplusNeutrino/My_Blog/actions/runs/39056732011) build117466109670/deploy117469225064/live117469268662全部success，不把测试通过当整页视觉正常。
- 实际复现：390px Night，线上原生 `public-sweep-about-390-dark-9.png`，“阅读、邻居与旅行记忆”中的“友情链接”卡片说明第一行右端被44px返回顶部圆钮覆盖。已放大查看，不是DOM推测/用户偏好。来源live artifact12110591949，491777943 bytes，独立SHA256 `28855b85123470e7e0bf045a715dee673ec45ac59ebfffc2760e61cc6dd465be`匹配。
- [原生before](ui016-before-about-relations-390-dark.png)与[原帧诊断](ui016-before-about-relations-390-dark.json)永久保存。原诊断没有关系段文字Range，故原门禁成功不代表此处无遮挡；新回归需加入关系段目标并保留UI012–015各自门禁。
- 根因：`_includes/neutriverse-about-profile.html`输出的 `.about-relation-card > p` 无固定按钮文字通道；现有UI015只覆盖理念、维护、日期和OBSERVE状态。三张同组件说明均使用该结构，单纯改变父卡片尺寸/移动全站按钮没有必要。
- 最小范围：仅共享CSS <=1199.98px为ABOUT关系卡片说明增加右2.75rem文字空间；不改卡片外框/网格列数、字号/主题、按钮、链接、模板或数据/旧正文。审计现有detailTextButton增加此作用域，要求目标存在、逐个有文字、逐行严格无按钮交集；失败仍保存PNG/JSON再拒绝。增加必要接线/CSS回归，不放宽任何原时限/门禁。
- 文档范围：本文件、UI计划/日志、UI-A09补充记录及本before证据。原目录用户字体/缓存/未跟踪文件不动，gh不在PATH，不编造Issue；无新用户待决问题。其余尺寸主题是待验条件，不宣称已复现。

## 验收条件

- 本机全回归、authoring、T01正文/metadata/URL/hidden保护、diff；精确工作head的production Jekyll/产物及全部原门禁。
- 390/768/1024/1366 × Night/Prospero Light连续原生截图，关系说明逐行Range与可见按钮无交集；实际查看截图并放大原390 Night场景、真实滚轮/返回顶部/Library和友链往返。通过后才合main，再核对该main自身build/deploy/live并同场景人工复验，之前保持validation-pending。
- UI-A09整页检查被本确认缺陷阻塞，不能标done；旧br空白与倒计时不凭偏好删改，其他应用/隐藏边界不公开。

## 实现与本机验证边界

- CSS仅新增<=1199.98px关系卡p右padding2.75rem；审计在原detailTextButton selectors中追加关系说明，所有旧scope/非空/严格交集/失败采证保持。两项接线/CSS回归新增，不是视觉证明。
- 本机258 tests、authoring44/5/7、T01保护44/5/5与git diff --check通过。本机无Jekyll/Chrome，未取得新head修复后截图；精确工作head production Jekyll/产物/全门禁、四宽度双主题人工截图、main部署/live同场景仍validation-pending。先核对ui/fix-016自身Actions再决定是否交付，不用8bff旧CI替代本次。
