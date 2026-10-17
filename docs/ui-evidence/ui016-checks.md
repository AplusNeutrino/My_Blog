# UI-016 — ABOUT关系卡片说明被固定按钮覆盖

状态：validation-pending；最小实现保存工作分支ui/fix-016，未部署，尚未视觉验收。

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
