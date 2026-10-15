# UI-A08d Library时间线限定检查

状态：validation-pending，非已确认产品缺陷。
Base main：2e3d2844af408504cb616b9596ea682c97c3edd0。
2026-10-15 云Chrome，实际1363×936，Prospero Light。

从公开Library根页点击“加载时间线”，最终46条日期/事件/作品记录可见，scrollX=0。[实际桌面截图](uia08d-timeline-1363-light.jpg)已查看：时间线标题和首段文字未见裁切。截图不包含全部记录，不能代表四宽度双主题或全库存验收；未根据此局部结果猜测修改样式。

新增现有审计的8组时间线流程：初始未加载→真实按钮加载→非空且最多100条、日期/事件文本→首尾滚动截图/行与页面边界→重复加载等待ul实际替换、整组记录不重复→整页刷新lazy重置→键盘Enter加载相同记录→刷新后首段截图。共24张新状态图和24份JSON；原192+14场景不删减。对动态同步内容不固定46条，不从聊天补入测试数据。

本地222 tests、authoring44/5/7、T01保护44/5/5与diff check通过；新测试只是审计契约，不冒充Chrome交互或视觉正常。本机无Ruby/Chrome，精确工作head production Jekyll/浏览器/24图人工检查及实际main部署/live均待验收，未合main。gh未安装未虚构Issue，无新待答问题；其他Library模式/控件和全站剩余矩阵仍pending。

前置main的[run38749174621](https://github.com/AplusNeutrino/My_Blog/actions/runs/38749174621) head精确2e3d2844，build116470712739/deploy116473447923/verify-live-ui116473729990全部success，仅作为已部署前置，不代表本次新审计通过。

## 2026-10-15 失败证据与审计假设修正

[run38757230686](https://github.com/AplusNeutrino/My_Blog/actions/runs/38757230686)精确head02d11892f9d9741a0f5739a423e01bedabd3fe7f，build116499547427 failure，deploy116500623040/live116500622929 skipped。222 tests/4 Ruby/T01/authoring/Jekyll通过；完整192+14未完成。

下载artifact11983209912，11611426 bytes，sha256:1cc7a1ff7bb4b6ba843b1628990badc56bc48a48041731e097ad2d92c1abb839独立匹配。人工看[390 Night首段](uia08d-initial-start-390-dark.png)及[尾段](uia08d-initial-tail-390-dark.png)，未确认显示缺陷；失败发生在之后再次访问旧加载按钮。既有markup将按钮放在时间线容器内、成功时replaceChildren(list)，旧button引用必然失效。初始“重复加载”验收不适用于当前一次性lazy界面，不能据此宣称网站故障或增加新按钮。

新审计明确核对加载后按钮移除且只有一个ul、首尾滚动记录不变，再刷新恢复未加载状态、键盘Enter重新加载同组文本；保留日期/数量/溢出/24图及所有原门禁，不捕获Stale异常后假装通过。新head production/live仍pending。

## 2026-10-16 生产机械通过，但截图发现UI-009

精确head47b3c294711c77abb62b321f71f5ae1eb658f855 / run38765012413，build116526426682 success，deploy/live skipped。223 tests/4 Ruby/T01/authoring/Jekyll/旧门禁、192+14与8时间线流程机械通过；24首/尾/刷新诊断无行/页面横向溢出、scrollX=0，每组46条、单列表、一次性按钮替换、滚动保持和刷新lazy/Enter同组记录均通过。

artifact11989890630摘要独立匹配。人工看24张图两联系表并放大390 Light首/尾与1024 Night刷新原图，确认390 Light长作品名尾部被固定返回顶部按钮遮住，详见[UI-009](ui009-checks.md)。故UI-A08d不标done、不合main；以下保存的“production”文件是此次机械记录与视觉失败证据，不是视觉验收通过：

- [完整audit192](uia08d-production-audit.json)
- [24行/页面诊断](uia08d-production-timeline.json)
- [390/768双主题三状态](uia08d-production-contact-390.jpg)
- [1024/1366双主题三状态](uia08d-production-contact-1024.jpg)

修复及真实文字行/按钮不相交门禁先工作分支，新head完整production/live和修复后截图仍pending；其他Library控件/全站矩阵不由本项推断完成。

## 2026-10-16 UI-009修复后生产检查

head2fcde494 / run38774806960 build116560105866 success，224 tests/4 Ruby/T01/authoring/Jekyll/旧门禁及192+14通过；分支deploy/live skipped。人工看四宽度双主题24张新图两联系表和三张代表原图，长作品名完整换行，24文字行/按钮诊断均无相交。8时间线加载/单列表/滚动保持/刷新lazy/Enter同记录通过；完整摘要/JSON/截图见[UI-009修复后证据](ui009-checks.md#2026-10-16-修复后生产验收通过)。

本项仍validation-pending，待实际main部署和线上同24图；既有失败与UI-009遮挡历史保留，没有以原机械通过或静态测试冒充视觉正常。
