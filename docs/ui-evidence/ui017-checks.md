# UI-017 — ABOUT时间线说明被固定按钮遮挡

状态：done（仅UI-017时间线说明作用域）；fa1c2c89精确main构建/部署/live及同场景人工复验通过。全站矩阵仍IN PROGRESS，新证据提交自身CI另核对。

## 2026-10-18 精确main部署与线上限定验收

- 验收main `fa1c2c89fe9512a7c2527de70b9f68953248d4ac` /[run39081409231](https://github.com/AplusNeutrino/My_Blog/actions/runs/39081409231)：build117538917578、deploy117541886151、verify-live-ui117541923994全部success。260 tests、Ruby渲染、T01保护44/5/5、authoring44/5/7、production Jekyll/Search/feed/SEO/资源/路由/全部旧门禁及production/live各192+14、24公开流程177原生帧通过；live日志明确https://neutriverse.uk。
- live artifact12119179516 /491952108 bytes，独立SHA256 `a598c1eb9a6664aed6e328cdbbbee6ba15a91e5ad0fd995be51684125b587361`匹配。实际人工逐张查看四宽度双主题18个时间线说明可见帧/[8联系表](ui017-live-contacts/)，放大[390 Light线上原图](ui017-live-about-timeline-390-light.png)与before对照：Ravenis说明全文完整、按钮与文字分离，日期/标题/链接/外框/主题保持，未确认新缺陷。未把全部177自动帧当人工整页验收。
- [线上摘要与production对照](ui017-live-summary.json)：ABOUT8流程每帧timeline目标5、emptyRoots0、严格逐行交集0，诊断与656b78ff已验production完全相同；24流程帧数/往返目标一致、scrollY最大差0。原生滚轮全main覆盖、真实返回顶部pointer click、Library/友链点击与浏览器返回通过，无横向溢出/scrollX0。
- 本机260 tests/authoring44/5/7/T01保护44/5/5/diff再通过，本机无Chrome/Jekyll；AGENTS/docs/agents/ADR/旧COMPLETE与本轮台账/用户补充核对，CONTEXT无，gh不在PATH不编造Issue，独立worktree保留原目录用户修改。本轮仅公开验收证据/计划/日志，不追加产品/数据/原文/metadata/URL/hidden/noindex、外部仓库或旧COMPLETE修改。
- UI017限定done；A09剩余整页与其余矩阵pending，无新用户决策。fresh main仍fa1c2c89才expected-head非强推，新文档head自身CI/deploy/live另核对，不用本成功代验；全站不标COMPLETE/不写final报告或暂停。

## 2026-10-18 精确生产与限定视觉验收

- 实现 `656b78ff036c8cfe6028ba67ce106a52894f8236` /[run39077837409](https://github.com/AplusNeutrino/My_Blog/actions/runs/39077837409)：build117528572919 completed/success，deploy117531646803/live117531646743 skipped符合工作分支规则，不冒称已部署。
- 260 tests、Ruby渲染、T01正文/metadata/URL/hidden保护44/5/5、authoring44/5/7、production Jekyll/Search/feed/SEO/资源/路由/全部原门禁，以及主192/侧栏14/公开24流程177原生帧完整通过；字体30s/有限动画20s及旧逐行文字门禁保持。
- artifact12118321539 /492621257 bytes，独立SHA256 `0a2688f1340db2d563b68c374975a03291946ef03329620e1088e884945ff077`匹配。人工逐张查看时间线说明可见的18帧/[8联系表](ui017-production-contacts/)，覆盖390/768/1024/1366双主题，放大[390 Light修复后原图](ui017-production-about-timeline-390-light.png)与before对照：Ravenis说明全文完整并避开圆钮；日期/标题/来源链接、时间线外框和双主题保持，窄列自然增加换行，没有确认新缺陷。
- [24流程及目标帧摘要](ui017-production-summary.json)：ABOUT8流程每帧timeline目标rootCount5、emptyRoots0、严格真实文字行overlaps=[]。真实原生滚轮覆盖main、返回顶部pointer click、Library/友链点击及浏览器返回通过，无横向溢出/scrollX0。只人工验收18目标帧，不声称全部177帧、A09剩余整页或全站通过。
- 本机260 tests/authoring44/5/7/T01保护44/5/5/diff再次通过；本机无Chrome/Jekyll，浏览器与production构建证据来自该精确CI。AGENTS/docs/agents/ADR/旧COMPLETE与本轮台账、用户补充核对，CONTEXT无，gh不在PATH不编造Issue；独立worktree保护原目录用户修改。
- 本轮仅追加公开验收证据/计划/日志，不追加产品或数据修改；fresh main仍d5ac222且保留home_popular/Library同步后才非强推交付。新main自身Actions/build/deploy/live及线上同场景人工截图仍validation-pending，不用工作分支成功替代；全站IN PROGRESS，无新增用户决策，下一项核对该新main。

## 2026-10-18 范围与复现

- Task UI-017 / P2；编辑base main `d5ac222e86f348c1097c0b599395eb06f9218aba`，仅比已部署880bddf8新增home_popular推荐URL，保留该数据。复现来源精确880bddf8 /[run39073683931](https://github.com/AplusNeutrino/My_Blog/actions/runs/39073683931)，build117516332761/deploy117519061350/live117519102104全部success；未用其成功代验最新d5ac。
- 实际视觉复现：390px Prospero Light，ABOUT“网站与项目轨迹”Ravenis节点说明，原生public-sweep-about-390-light-8.png，行尾“外”等文字进入44px返回顶部圆钮并被盖住。联系表疑点后放大原图确认，非DOM猜测/审美偏好。同一Night第8原图已看，没有确认遮挡，不将其写成双主题均复现。
- live artifact12116846894 /491849339 bytes，独立SHA256 `8d054c2c7ceb573ca47f26356837a039c937b22d58ab5adbe75690a5ad5e727b`匹配；原生before永久保存。原detailTextButton未覆盖时间线event说明，CI成功不代表该处无问题。
- 根因待源码定位；拟最小范围为同组件时间线说明p避让固定按钮文字通道，不改文案/日期/链接、时间线结构、卡片外框、字号/主题、按钮或数据。审计现有detailTextButton追加该说明作用域，要求目标存在/每目标非空/严格真实文字行无交集，失败仍采PNG/JSON再拒绝。新增必要接线与CSS回归，不放宽任何旧门禁/30s字体/20s动画等待。
- 文件范围：assets/css/neutriverse-sections.css、tools/check_think_build_visual.py、tests/test_public_page_sweep_audit.py、本文件/公开before、本轮计划/日志及UI-A09部分检查记录。半成品留ui/fix-017，不直接main；保留原目录用户修改、home_popular/Library同步、旧原文/metadata/URL/hidden/noindex和旧COMPLETE，不修改外部仓库。

## 验收

- 全回归、T01保护44/5/5、authoring44/5/7、production Jekyll/产物/全部旧门禁；精确新head Actions。
- 四宽度双主题原生滚动截图，时间线说明逐行真实Range不与按钮交叉；实际查看目标帧并放大390 Light原场景对照，真实滚轮/返回顶部/Library与友链往返。生产通过后才交付main，随后同head build/deploy/live及同场景截图复验；之前validation-pending。
- gh不在PATH，不虚构Issue；无新用户决策。UI-A09整页仍pending，作者旧br空白/倒计时保留，不以局部通过推断全站完成。

## 已实施与实际检查边界

- 根因已定位：模板.about-timeline-event > div > p输出原event.text，原Night共享规则仅margin/font/line-height，没有固定按钮文字通道；Light字形/换行使390原帧右端进入圆钮。不是所有主题都确认遮挡，不修改内容或字体。
- 仅共享CSS <=1199.98px给该组件说明p右padding2.75rem；不改event网格、时间/标题/来源链接、外框、字号/双主题或固定按钮，>=1200不变。现有detailTextButton追加这一个作用域，保留旧intro/relations/日期等、目标存在/非空/真实Range严格交集及失败PNG/JSON/抛错。新增2项接线/CSS回归，不能代替浏览器验收。
- 本机260 tests、authoring44/5/7、T01保护44/5/5、diff通过。本机无Chrome/Jekyll，新head production及修复后截图尚未取得，不宣称视觉通过。原始[before PNG](ui017-before-about-timeline-390-light.png)/[原帧诊断](ui017-before-about-timeline-390-light.json)保留；旧诊断未检查时间线文字，所以仍需新精确head回归与人工复验。
