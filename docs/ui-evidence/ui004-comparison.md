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
