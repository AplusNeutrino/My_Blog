# UI-016 — ABOUT关系卡片说明被固定按钮覆盖

状态：validation-pending；a17ee7ec精确production及UI016限定人工视觉验收通过，可交付main；main自身CI/部署/同场景live仍待验，不标done。

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
