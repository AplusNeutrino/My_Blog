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

## 2026-10-15 UI-007/UI-008生产验收

验收head `51f5e99947ccf1bfce29754efac93d1b5f9740a0`，
[run38731750252](https://github.com/AplusNeutrino/My_Blog/actions/runs/38731750252) build116411370430 success；工作分支deploy/live skipped。
220 tests、T01/authoring/production Jekyll/旧门禁、192页面+14侧栏场景通过。

artifact11971222460，sha256:16e9da6fbfb21213aaa06ca6c2ef94307441aceae894adf1463da2c48e9548c5下载独立匹配。人工看32张四宽度双主题page2/open/combined/cleared截图两联系表，放大390 Night面板、390 Light第2页与1024 Light组合筛选原图；移动浮层不再裁切页面左缘，分页刷新保持按钮2及同组内容，无新增确认缺陷。

- [完整192项生产记录](ui007-production-audit.json)
- [32份面板/年份几何诊断](ui007-production-filters.json)
- [390/768双主题四状态](ui007-production-contact-390.jpg)
- [1024/1366双主题四状态](ui007-production-contact-1024.jpg)

8条分页/筛选流程均通过：页2刷新URL与ID一致、上一页恢复、来源Bangumi与动态公开年份组合刷新ID一致、清除恢复；32份几何诊断scrollX=0，所有展开面板在viewport内。前一head的失败历史与UI-008记录保留，没有降低断言换取成功。JSON和联系表永久保存，原PNG在artifact留14天。

本节是localhost production验收，UI-007/UI-008仍validation-pending：main交付后核对实际head部署/live同32场景，不宣称已上线。时间线、完整库存/离屏加载及全站其他矩阵仍pending。
