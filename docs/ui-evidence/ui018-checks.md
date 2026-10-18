# UI-018 — ABOUT历史状态更新日期被固定按钮覆盖

状态：done（仅UI-018日期标签作用域）；c696aa9精确main build/deploy/live与部署后原场景人工复验通过。全站矩阵仍IN PROGRESS，新证据提交自身CI另核对。

## 2026-10-18 范围与实际复现

- Task UI-018 / P2；base main `5ff4c8eb503df23b18b9b8c977957449bdb76b8f` /[run39085413284](https://github.com/AplusNeutrino/My_Blog/actions/runs/39085413284) build117550794106/deploy117553847516/live117553882588全部success。260 tests/Ruby/T01/authoring/Jekyll/旧门禁、production/live各192+14及24公开流程177帧通过，不将CI成功当整页视觉正常。
- 实际复现：1024px Night，ABOUT PERSONAL ORBIT状态区右下“更新于2026-08-17”末端被44px返回顶部圆钮盖住，public-sweep-about-1024-dark-6.png联系表疑点后放大原图确认。Light同位置原图日期完整，不写成双主题均复现。证据非用户报告/DOM猜测/审美偏好。
- live artifact12120503918 /492063761 bytes /独立SHA256 `acfa73f792bd2236b7abe3715ed5ea90ab6a701ea2afe4b53da742b0b254229b`匹配。原PNG/原帧诊断永久保存；旧门禁未覆盖该历史状态更新标签，不能用旧通过证明无覆盖。
- 拟最小范围：仅日期标签为固定按钮预留文字通道；不改历史日期/原文/metadata、状态实时性含义、主体布局/字号/主题、按钮、数据或外部仓库。现有逐行detailTextButton追加该明确作用域，目标存在/非空/严格真实Range交集0，失败仍保存PNG/JSON并拒绝；2必要回归，不放宽旧时限/门禁。
- 文件范围：assets/css/neutriverse-sections.css、tools/check_think_build_visual.py、tests/test_public_page_sweep_audit.py、本文件/before/部分A09记录、UI计划/日志。先ui/fix-018工作分支，未通过生产人工验收不交main。独立worktree保留原目录用户修改、home_popular/Library同步、旧COMPLETE；gh不在PATH不编造Issue，无新用户决策。

## 验收

- 全回归、T01保护44/5/5、authoring44/5/7、精确head production Jekyll/产物/全部旧门禁。
- 四宽度双主题原生滚动图与逐行文字遮挡回归；实际看目标画面，放大原1024 Night位置before/after、日期完整且返回顶部可点击，真实滚轮/Library友链往返。生产通过后再main，并核对新main自身build/deploy/live和线上同场景，之前validation-pending。
- A09仍pending；作者旧br空白/倒计时保留，不重设计/不公开隐蔽边界，不推断全站完成。

## 实现与本机验证

- 根因：.about-now-updated在桌面为position:absolute/right:0/bottom:-1.9rem，固定圆钮进入其右端；旧UI015书目time不覆盖该快照日期。窄屏原position:static规则保留，不改时间/字号来绕过。
- 最小CSS仅<=1199.98px把该标签right改2.75rem；不改bottom/position/主体布局、原历史日期或主题，>=1200不变。现有detailTextButton追加[data-about-profile] .about-now-updated，目标必须存在/非空/严格真实文字行交集0，旧scope与失败采证/重抛、字体30s/动画20s保持；新增2接线/CSS回归，不当视觉证明。
- 本机262 tests、authoring44/5/7、T01保护44/5/5、diff通过。本机无Chrome/Jekyll，精确新head production/产物/修复后人工截图/main/live均待验；原[before PNG](ui018-before-about-updated-1024-dark.png)/[原帧诊断](ui018-before-about-updated-1024-dark.json)保留。先核对同一工作head，不用旧5ff成功代验。

## 2026-10-18 精确生产与限定视觉验收

- 实现822b03f0929ea1b5e0c68f8d2b432f4aef278c7c；[run39089046015](https://github.com/AplusNeutrino/My_Blog/actions/runs/39089046015) build117561626252 success；工作分支deploy117564304823/live117564305246 skipped，不当已部署。262 tests、4项Ruby渲染、T01保护44/5/5、authoring44/5/7、production Jekyll/Search/feed/SEO/资源及原门禁通过；主192、侧栏14、公开24流程177原生帧完整产出。
- artifact12122386729 /491118024 bytes，独立SHA256 c6cdf084f4ba68ca99e8778beeec748696d9535d76559a1f3a8cd36321eb9e45匹配；[精简摘要](ui018-production-summary.json)保留原JSON哈希/24流程及该日期逐行诊断。实际逐张查看四宽度双主题10目标帧/8联系表；放大[1024 Night修复后原图](ui018-production-about-updated-1024-dark.png)对照before，原被盖住的日期尾端完整位于按钮左侧。原日期/主题/主体布局保留，390静态日期与1366原布局无新增确认缺陷。
- ABOUT八流程每帧目标rootCount1、emptyRoots0、严格文字行交集0；真实原生滚轮覆盖main、返回顶部pointer click、Library/友链点击及浏览器返回通过，24流程scrollX0且无横向溢出。仅人工验收10目标帧，不冒称177帧/A09全页人工完成。
- 本机262 tests/authoring/T01/diff再次通过；本机无Chrome/Jekyll，视觉与production证据来自该精确CI。gh仍不在PATH，不编造Issue；独立worktree保护原目录用户修改。只追加公开证据/计划日志，不追加产品或数据修改，旧COMPLETE/原文/metadata/URL/hidden/noindex/外部仓库不动。
- fresh main仍5ff4c8eb时才expected-head非强推交付；新main自身build/deploy/live及线上同场景仍validation-pending，UI018未标done。无新增用户决策，下一项核对同一新main，全站IN PROGRESS。

## 2026-10-18 精确main部署与线上限定验收

- 验收main c696aa9484d99a5d07fae662615c2381f499daa9；[run39092301033](https://github.com/AplusNeutrino/My_Blog/actions/runs/39092301033) build117571422808/deploy117574250958/verify-live-ui117574288474全部success。262 tests、4项Ruby、T01保护44/5/5、authoring44/5/7、production Jekyll/Search/feed/SEO/资源及全部旧门禁通过；production/live各192+14与24公开流程177原生帧，live日志明确https://neutriverse.uk。
- live artifact12124180750 /493382730 bytes /独立SHA256 a32bf3590395f1be93ee8893bd81a256f27f9b581cac644156af6f8feb828748匹配。实际逐张人工查看四宽度双主题10个日期目标帧/8联系表；放大[1024 Night线上原图](ui018-live-about-updated-1024-dark.png)与before对照，日期末端完整位于圆钮左侧，原日期/主题/主体布局保留，无新确认缺陷。只限定UI018，不将177帧或A09整页冒称全部人工验收。
- [24流程精简摘要](ui018-live-summary.json)保留原JSON SHA256、来源head/artifact、10目标帧和8联系表。ABOUT八流程每帧目标rootCount1/emptyRoots0/严格逐行交集0，与822b03f0生产日期诊断完全相同；24流程帧数/往返目标一致、scrollY最大差0/scrollX0/无横向溢出。真实原生滚轮覆盖main、返回顶部pointer click、Library/友链点击及浏览器返回通过。
- 本机262 tests/authoring/T01再通过；本机无Chrome/Jekyll，真实浏览器证据来自精确CI。gh不在PATH不编造Issue；独立worktree不动原目录用户修改。仅追加公开证据与计划日志，不改原文/metadata/URL/hidden/noindex、同步数据、外部仓库或旧COMPLETE。UI018限定done，新证据head自身CI另核对；无新用户决策，A09与全站仍IN PROGRESS，不写final报告或暂停。
