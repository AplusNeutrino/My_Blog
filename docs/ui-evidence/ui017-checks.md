# UI-017 — ABOUT时间线说明被固定按钮遮挡

状态：validation-pending；最小实现留ui/fix-017，修复后生产/人工截图/部署/线上均待验，main不改。

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
