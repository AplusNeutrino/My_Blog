# UI-019 — THINK介绍与写作卡片文字被返回顶部按钮遮挡

状态：validation-pending。最小实现已完成；修复后截图、production与部署未验收。

## 2026-10-18 先记录复现、范围及验收

- base main40e6ee2b693778dacca9140ff9fabaf454176c78；审计工作base8b3308db63b810c58afbce317a27427d3a38072e。精确[run39110109162](https://github.com/AplusNeutrino/My_Blog/actions/runs/39110109162) build117624212912 success，deploy117628254520/live117628258809 skipped，不作已部署。265 tests、T01/authoring44/5/7、production Jekyll及旧门禁成功。
- 专项artifact12129943687共51332149 bytes，下载字节独立SHA256=60d83add292b465be9e17097e35803e93f4b4cc4b65b7cf36fa10693cfc0eee5，与服务端一致。8流程JSON共32页、292原生帧；机械核对每流程44唯一href按12/12/12/8无重漏、URL/末页刷新/上一页、main覆盖/PNG实际视口/无横向溢出通过。不等于292张已人工看完。
- 实际查看390 Light第1页13帧的3联系表；放大原图2/6/7/8确认：介绍末行、Progressive Disclosure摘要、互联网标签摘要与Z.A.T.O.摘要的右端文字被固定圆钮覆盖。保留相同文件名的before原图。用户报告：无；证据为实际CI生产图，不是推测或审美偏好。尚未线上复验。
- P2根因：介绍段与nv-writing-record-body流式文字没有为窄/中屏固定按钮保留横向安全空间；A10原门禁只检查横向溢出和分页完整性，未检查这些文字Range与按钮交叉，所以CI成功仍漏报。不是分页数据/正文错误。
- 最小实施范围先记录：assets/css/neutriverse-sections.css仅在<=1199.98px给THINK介绍与写作卡片body留2.75rem右侧文字空间；tools/check_think_build_visual.py在THINK四页原生滚轮每帧新增实际文字Range/按钮可见性严格相交检查，失败先保存PNG/JSON再抛错；必要接线回归、本轮计划日志与公开before证据。工作分支ui/fix-019；不改按钮/字号/主题/内容/数据/链接/排序/分页语义/hidden/noindex/外部仓库/旧COMPLETE。不扩为全站重新设计。
- 验收：同一修复head生产四宽度双主题四页原生截图、真实滚轮/返回顶部/分页/末页刷新/上一页通过；新增逐帧介绍与可见记录全部文字不与可见按钮相交，实际查看修复后相同遮挡场景及其他尺寸；T01/authoring/production Jekyll/原门禁不减。通过后才main，精确main build/deploy/live及相同场景线上图另验。无新用户决策；gh不在PATH，不编造Issue。

## 最小实现与本机验证

- 仅THINK介绍/记录body在<=1199.98px增加2.75rem右侧文字空间，保留日期列/卡片外框/按钮/字号/文本/链接/筛选语义。四页每帧新增可见记录（12或末页8）与唯一介绍scope计数、Text Range和可见按钮严格不相交；缺scope/空文本/相交先存原生PNG/诊断JSON再失败。原门禁/超时/主192/14侧栏/24公开往返均保留。
- 增2项接线回归；本机267 tests OK，authoring44posts/5fragments/7projects、T01正文/日期/URL/hidden44/5/5及git diff --check通过。无本机Ruby/Jekyll/Chrome，不声称修复后视觉或production通过；新head必须重新采证，不使用8b成功替代。main仍40e6ee2b，未部署。
- 原图ui019-before/public-sweep-think-page-1-390-light-{2,6,7,8}.png保留；3张联系表只含已看的13帧；ui019-before-summary.json列明8原JSON摘要与实际查看边界。无用户决策或权限扩张。
