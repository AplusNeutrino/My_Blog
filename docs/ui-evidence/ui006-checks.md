# UI-006 Library移动搜索遮挡副标题

状态：UI-006 done，UI-A08c1上述搜索路径限定done。各阶段历史状态保留，最终线上验收见末节；全站检查未完成。

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

## 2026-10-15 修复后生产验收

验收head `1edcde07cb948b60a0fac2e275229a0c70769686`，[run38703172752](https://github.com/AplusNeutrino/My_Blog/actions/runs/38703172752)，build116316270106 success；分支deploy/live skipped。215 tests、T01、authoring44/5/7、production Jekyll、既有门禁与192+14真实浏览器场景通过。

下载artifact11956813908，sha256:1a92c572c41e5f6eafe48c323548c86ef21ae006738e8481698d6ab0ceb5c136。人工查看24张四宽度双主题三状态截图两联系表，放大390 Light空状态、390 Night结果、1366 Light清空；移动搜索已在副标题下方正常流占行，没有标题/返回/后续控件遮挡。桌面没有新增确认缺陷。

- [修复后390/768两主题三状态](ui006-production-search-390.jpg)
- [修复后1024/1366两主题三状态](ui006-production-search-1024.jpg)
- [完整192场景记录](ui006-production-audit.json)
- [24份搜索矩形](ui006-production-search-geometry.json)

8搜索流程均刷新保留、空提示、清空返回通过。390 Light空状态标题区bottom146.0625、搜索top157.25、搜索bottom与header.bottom均190.84375，标题与搜索约11px间隔。未展开搜索时保持隐藏，不额外公开信息。JSON与联系表永久入仓，原PNG在artifact保留14天。

UI-006/UI-A08c1仍validation-pending：交付main后核对实际新head build/deploy/live及线上同场景截图；本节不等于线上验收。Library高级筛选/分页/时间线及全站余下矩阵仍pending。

## 2026-10-15 精确main部署与线上复验

验收main `ea8b62d58414465661d1f7d88d883e353b9b5b90`，
[run38710416815](https://github.com/AplusNeutrino/My_Blog/actions/runs/38710416815) build116340121129、deploy116342302377、verify-live-ui116342443999全部success。215 tests、T01/authoring/production Jekyll/旧门禁及production/live各192+14通过。

live artifact11960851998，sha256:118f943c583b640080f74525a940f72111a0a12da6f95e28b8c7ebf116318caf下载独立核对。线上job目标为https://neutriverse.uk；8组搜索路径与24矩形检查通过。实际看24张搜索三状态线上截图两联系表，放大390 Light空状态、390 Night结果、1024 Light清空原图，移动搜索不再覆盖副标题或后续返回/工具栏，桌面无新增确认缺陷。

- [完整live audit192记录](ui006-live-audit.json)
- [24份live搜索矩形](ui006-live-search-geometry.json)
- [线上390/768双主题三状态](ui006-live-search-390.jpg)
- [线上1024/1366双主题三状态](ui006-live-search-1024.jpg)

UI-006 done；UI-A08c1限定搜索结果/刷新保留/空结果提示/清空恢复根页done。高级筛选/分页、时间线、完整库存/离屏加载和其他全站矩阵仍pending，不将局部验收扩写为全站正常。JSON及联系表永久入库，原PNG留artifact14天。本次只持久化证据，无产品/内容/URL/隐藏边界改变；文档提交CI另核对。
