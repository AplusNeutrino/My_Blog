# UI-006 Library移动搜索遮挡副标题

状态：validation-pending；不是视觉已通过报告。

## 修复前实际证据

来源head `e6a54de259b8c67d5bc6e6f0214e1bd519eaea7f`，
[run38689759158](https://github.com/AplusNeutrino/My_Blog/actions/runs/38689759158)，
build116272713219 success，工作分支deploy/live skipped。
artifact11951832064（sha256:c2e1b65ce679fe223d0bd0b7cce819d8275c1c6064bc9ebac21b8b213fa35df9）下载摘要独立匹配。

实际查看24张搜索结果/空状态/清空截图的两联系表，并放大390 Light空状态、1024 Night结果、768 Night清空原图。390px双主题打开搜索后，输入框覆盖副标题“对曾经品鉴过的作品进行记录”。原8条搜索交互记录均通过，192项页面几何只检查页面级溢出，未捕获此内部遮挡；因此没有把原CI成功当视觉正常。

- [修复前390/768两主题三状态](uia08c-production-search-390.jpg)
- [修复前1024/1366两主题三状态](uia08c-production-search-1024.jpg)

查询来自公开目录首本书的实际标题与ID，不固定同步后可能变化的条目总数。结果URL/刷新、空提示/零卡片、清空恢复根页的8条真实浏览器检查通过，但不等于界面无遮挡。

## 根因与最小修复

720px内搜索label绝对定位于按钮wrap下方，没有为其占据的高度预留空间，落入同一header内的副标题区域。仅将移动header设为两列Grid，标题和按钮第一行、搜索第二行跨列；保留原输入、切换、搜索状态和桌面布局，无内容/metadata/URL/同步数据改动。

新增浏览器回归：结果/空状态/清空每次记录heading、search、header实际矩形；拒绝搜索与标题区相交，拒绝搜索超出header进入后续内容，保留页面溢出检查。隐藏搜索不占行，打开后正常布局推下后续内容，不用遮罩掩盖缺陷。

本机215项测试、authoring、T01保护与diff check通过；真实修复后Chrome截图、production Jekyll和精确main部署/live均待验收，不能借用修复前head成功。无新增用户决定问题；筛选/分页、时间线和其他全站矩阵仍pending。
