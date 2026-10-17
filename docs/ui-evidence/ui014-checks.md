# UI-014 — OBSERVE / ABOUT 说明段避让固定按钮

## 实现前范围（2026-10-17）

- Task ID：UI-014，P2；base main `fa23a32cf5f41b8fd6e47a3aebda7197213fb84e`。
- 实际复现而非偏好：390 Light OBSERVE 的“数据流程”说明、390 Night ABOUT 的介绍段右端被返回顶部圆钮覆盖。已重新查看原生 PNG：[OBSERVE](ui014-before-observe-390-light.png)、[ABOUT](ui014-before-about-390-dark.png)。来源为 d50f1bc9 的 production artifact12096771963；不是新 head 的修复后截图。
- 根因：两个普通文本容器使用完整内容宽度，没有固定按钮文字通道；首页 UI-012/013 的卡片规则不覆盖它们。
- 最小产品范围：`assets/css/neutriverse-sections.css`，只给窄屏 OBSERVE `.nv-section-intro` 与 ABOUT `.about-info-text` 留右侧文字通道。不移动/隐藏共享按钮，不更改字体、主题、正文、数据、DOM、旧 URL 或私有边界。
- 审计范围：`tools/check_think_build_visual.py`、`tests/test_public_page_sweep_audit.py`。保留首页逐行 Range 回归，给 observe/about 的这两个明确容器增加相同真实文字行/可见按钮严格交集检查；不存在目标或无文字也拒绝。失败保留原生 PNG/JSON 并抛错。
- 文档范围：本文件、本轮根计划与日志。gh CLI 当前不在 PATH，无法按仓库规范创建 Issue，不使用 API 代替，不编造编号。

## 验收与限制

1. 本地相关回归、全 tests、T01 正文/URL/hidden 基线、authoring、diff check；本机没有 Jekyll/Chrome 时明确交由 CI。
2. 新精确工作分支 head 的 production Jekyll、既有全部门禁、192主场景/14侧栏、24公开流程不减少；四宽度390/768/1024/1366 × Night/Light 的连续原生视口 PNG、真实滚轮/返回顶部/公开详情与 Library/友链往返。
3. 人工查看修复后 OBSERVE/ABOUT 全部滚动图，并放大原390两场景前后对比。文字不与按钮相交、中文完整、其余外框/主题不变；没有将静态测试当视觉验收。
4. 生产验收后才可交付 main；该 main 自身 build/deploy/live 与相同场景人工截图复验后才 done。现在 `validation-pending`，留 `ui/fix-014`，全站不 COMPLETE，不暂停任务。

## 上一证据提交核对

`fa23a32c` / [run39027206328](https://github.com/AplusNeutrino/My_Blog/actions/runs/39027206328)：build117380439666、deploy117383385470、verify-live-ui117383421916 均 completed/success。关闭该文档 head 的 CI pending；不据此宣称 UI-014 已修或 OBSERVE/ABOUT 新视觉验收通过。

## 本次实现与本地验证

- CSS仅<=767.98px的两个明确容器增加2.75rem右padding；>=768px以及其他容器/按钮不动。四宽度截图仍全部检查，不由此推断桌面无缺陷。
- 审计新增introTextButton字段保留所用selector、rootCount、textNodes、可见行矩形、按钮矩形与overlaps；每帧目标必须恰好一个且含文字，严格拒绝相交。原recentTextButton字段及首页全部断言原样保留。
- 本机254项tests、authoring44/5/7、T01保护44/5/5、git diff --check通过。本机未运行Jekyll/Chrome，当前没有新head修复后截图；production/人工视觉/main/live全部validation-pending，不标done。
