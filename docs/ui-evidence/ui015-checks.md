# UI-015 — 公开说明/状态/日期的固定按钮避让

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
