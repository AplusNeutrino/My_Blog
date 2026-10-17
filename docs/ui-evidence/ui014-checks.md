# UI-014 — OBSERVE / ABOUT 说明段避让固定按钮

状态：done（d1bdcbf2精确main部署/线上限定验收）；此前pending按时间保留。

## 2026-10-17 精确main线上验收：done

- main `d1bdcbf2e00d7fc2abd30917af8573856af8719a` / [run39035135431](https://github.com/AplusNeutrino/My_Blog/actions/runs/39035135431)：build117403304548/deploy117406508063/live117406677161全部success。254 tests/Ruby/T01/authoring/Jekyll/全部旧门禁、production/live各192+14及24public通过；线上日志确认https://neutriverse.uk。
- live artifact12102362109，491375605 bytes，独立sha256 `076eedee986dcad849ddfd97293c0e3be3e179fdf7ceedd71e884929226be46d` 匹配Actions。此次只人工查看两个说明容器实际可见的32线上原生帧的[16联系表](ui014-live-intro-contacts/)，不是全部177帧；已放大[390 Light OBSERVE](ui014-live-observe-390-light.png)、[390 Night ABOUT](ui014-live-about-390-dark.png)，与旧图对比文字完整且不与按钮重叠。
- [线上摘要](ui014-live-summary.json)保留实际审阅文件名/24流程/两页121帧intro诊断。121诊断与生产完全相同，24流程帧数量/viewport/scrollY/visibleMain及公开往返相同，覆盖滚动坐标最大差0。16两页流程真实滚轮全覆盖/返回顶部/公开详情与Library友链往返均通过。
- 关闭UI014部署与线上pending，仅两个说明容器done；UI015/A09整页/全站其他矩阵不因此通过。此轮没有产品变化，新证据head CI另核对，无新用户待决问题。

## 2026-10-17 精确production验收

- 实现 `ad1540d04b1acb161fe6820cf099c1471f249b0f` / [run39031283966](https://github.com/AplusNeutrino/My_Blog/actions/runs/39031283966)：build117392071294 success；deploy117395105647/live117395105624 skipped（分支，不是已部署）。254 tests/Ruby/T01/authoring/production Jekyll与产物/所有旧门禁、192+14及24public通过。
- artifact12100198625，494296408 bytes，独立sha256 `249226eb5ece06604da78ba0fb83b53635f4d4c056b29b5e5565e41cefb75d98` 与Actions匹配。
- 人工查看OBSERVE/ABOUT四宽度双主题16流程121原生滚动帧的[全部34联系表](ui014-production-contacts/)，放大[OBSERVE390 Light](ui014-production-observe-390-light.png)与[ABOUT390 Night](ui014-production-about-390-dark.png)，与本文原图对照：文字已在按钮左侧换行，全文可读，主题/外框/字号保留。其余首页56帧未在此轮重新人工验收，不声称本次177图全人工通过。
- [24流程摘要](ui014-production-summary.json)保存16流程逐帧文字行/按钮矩形与空overlaps；目标恰好一个且含正文，所有帧严格交集通过。16流程连续覆盖/无横向溢出/真实返回顶部与公开目标往返通过。
- 生产通过仅针对UI014两个说明容器，不等于OBSERVE/ABOUT整页正常。新UI015见下；本次只加证据后可交付已验收修复main，新main自身build/deploy/live及相同场景人工复验仍须核对。无新用户决策，gh不可用不编造Issue。

## 新独立队列 UI-015（尚未修复）

实际390 Night原图放大确认，均来自同一artifact：

- [ABOUT理念段第6帧](ui015-before-about-principle-390-dark.png)：固定按钮覆盖“新的结构”尾端。
- [ABOUT待阅读日期第11帧](ui015-before-about-date-390-dark.png)：2026/02/06尾端被按钮盖住。
- [OBSERVE卡片状态第3帧](ui015-before-observe-meta-390-dark.png)：Occult Atlas的“应用保持 NOINDEX”末端被按钮盖住。

这些不是本文已修两个说明容器，列P2下一独立最小范围，不改全站按钮或作者内容；A09整体不标done。

2026-10-17线上补充同类实际复现：[ABOUT维护说明390 Night第4帧](ui015-before-about-maintenance-390-dark.png)，尾端“来源说明”部分被按钮遮住，已放大原图确认。纳入UI015剩余文字容器范围，不冒称UI014修复覆盖了它。

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
