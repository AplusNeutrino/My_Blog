# UI-004 — 短窗口侧栏重叠

- Base：7d376af1f05329dca43861c47c4dde83ded20786。
- 实现：a93f494fc10da59d65154a9ff2abf7f1096e3139（初稿2a8068f的审计点击失败如实记在日志）。
- 修复前：[线上1024×900 Night viewport](ui003-live-build-night.png)，检索文字和底部按钮重叠。
- 根因：导航flex box允许压缩且min-height=0，子内容却保留实际高度并溢出绘制。修复让profile/nav/bottom保持内容高度，由sidebar纵向滚动承载短窗；不缩字、不隐藏项目/导航、不重新设计。
- 工作分支[run38533540459](https://github.com/AplusNeutrino/My_Blog/actions/runs/38533540459) success：205 tests、T01/authoring/production Jekyll、全部原门禁、120项THINK/BUILD/OBSERVE截图和16组筛选/返回、14项短/高窗口专项通过。
- [14张侧栏viewport联系表](ui004-contact.jpg)：窗口390/768/1024/1366×700，1024/1366×900，1366×1100，两主题。真实innerHeight分别557/757/957。人工看联系表并放大1024×900 Night与390×700 Light原图；短窗滚动到底可完整操作检索/主题组，桌面组间8px，无重叠；高窗无需滚动。
- 新几何门禁：primary.bottom≤utilities.top、utilities.bottom≤social.top，控件中心hit-test必须命中自身且边界在viewport内。真实pointer主题切换、desktop搜索/取消，mobile Escape及连续3次mask关闭后跨两帧焦点仍在trigger。没有删除或放宽原门禁。
- UI-003a保护callback的production专项也通过；仍需本次main线上专项，不以存在代码或他次CI成功代替。
- 原图artifact11879545786保留14天；联系表与sidebar JSON长期留仓库。网页原文/metadata/URL/noindex/hidden边界不变。此局部通过不代表全站矩阵COMPLETE。
- main run38534120830在新专项768×700抽屉滚动前焦点尚未完成时失败，deploy/live skipped。脚本补等待抽屉开启动作的焦点完成后再滚动；不将分支success视为main/线上验收。
- 修正head ba75465277be11c48c7f4242138842a88effc953 / [run38534716282](https://github.com/AplusNeutrino/My_Blog/actions/runs/38534716282) success，全部生产门禁重新通过；样式与已查看联系表的a93f494f相同，只有审计等待时序修正。下轮必须下载本次main的live截图同场景复验；当前UI-004/UI-003a仍validation-pending。

## 最终部署与复验（2026-10-14）

- 787a4a61 / run38535247898 build/deploy success，但live在快速mask wait超时。未冒称通过。诊断8415050d仅稳定每次循环开始前的已关闭shell，保留open→立即mask点击；失败时新增状态和截图。网站JS/CSS本次没有再改变。
- 精确head8415050ddd200f51c471b84e0011e3d46260a305：[main run38540154437](https://github.com/AplusNeutrino/My_Blog/actions/runs/38540154437) build115772623467 / deploy115774058340 / verify-live-ui115774185770均success。205 tests、保护/authoring/Jekyll/所有原门禁、production120+14与live120+14通过。
- live artifact11882032589已下载、人工看14张[联系表](ui004-live-contact.jpg)并放大1024×900 Light原图。短/高窗口实际innerHeight557/757/957；桌面检索与底部组间8px、移动不重叠，全部按钮中心hit-test通过且位于可见viewport。真实主题切换、desktop搜索取消、mobile Escape与12次快速mask关闭通过，跨两帧focus保持trigger。
- [线上专项JSON](ui004-live-sidebar-audit.json)永久留仓库；原始120+32+14截图在本次artifact保存14天。UI-004与UI-003a done；全站矩阵仍未COMPLETE。
