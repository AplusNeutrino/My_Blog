# UI-007 Library分页刷新状态丢失

状态：validation-pending；修复后浏览器矩阵与部署未验收。

Base main `eb016b52ab6d167a8b1594cef96c6ea3eb1f0dea`。
2026-10-15 云Chrome，实际innerWidth1363、innerHeight936，Prospero Light。
从公开Library书籍目录点击“下一页”，URL变为`https://neutriverse.uk/library/?category=book&page=2`，当前页按钮2；刷新并等待目录加载后，该URL未变但当前页按钮1、首卡为“猎魔人 卷四 轻蔑时代”。

[刷新后错误显示第1页内容的截图](ui007-before-1363-light.jpg)。URL/页码另由当次只读DOM核对，截图本身不显示浏览器地址栏，不单独用截图推断URL。未把刚刷新时暂未加载的封面认作图片故障。

根因：初次render调用时items为空，renderCards按totalPages=1将state.page改为1；异步目录加载成功后已丢失请求页码。最小修复：仅在libraryDataLoaded为true（目录请求成功）后收缩越界页；保留原异步加载、空数据和错误提示。

Node直接执行真实renderCards函数回归：数据未到达时page2保留；60条/24每页时第2页首ID24；过大页码99加载后收缩到3；已加载合法空目录收缩到1。原函数作为负对照应失败，不能用改写算法冒充实际代码验证。

浏览器审计在四宽度×双主题既有Library场景内新增：下一页ID与第1页不重复、完整刷新URL/当前页/ID全部一致、上一页恢复；来源Bangumi与从可见卡片读到的年份组合、刷新、清除恢复。截图保存page2/open/combined/cleared四状态，不固定随同步变化的条目总数。

218项本地回归、authoring及T01保护通过；真实Chrome、production Jekyll、修复后截图与精确main部署/live仍pending，先工作分支不合main。高级筛选桌面局部操作未确认显示缺陷，未猜测修改样式。gh未安装不虚构Issue；无新增用户决定问题。
