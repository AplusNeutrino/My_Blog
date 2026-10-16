# UI-011：Library目录计数被返回顶部按钮遮挡

状态：confirmed / ready。P2。Base/复现main `41dca277eace9aa053bcb87e3cd21892b5ae6390`。本轮只记录复现，不提前宣称修复或完整矩阵通过。

证据分类：实际线上截图确认，不是用户偏好或源码推测。1024×900、Prospero Light、Library根页、书籍评分分类；将评分区滚动居中后，下方目录“漫画”右侧计数与固定返回顶部圆钮占据相同位置，被按钮表面和向上箭头遮住。截图来自精确head的[run38871666487](https://github.com/AplusNeutrino/My_Blog/actions/runs/38871666487)线上job116880240197，artifact12033767964内`rating-book-1024-light-library.png`，完整artifact摘要已独立验证。不是只凭DOM推断。

![1024 Light线上复现](ui011-before-1024-light.png)

目前没有根因几何诊断、其他滚动位置和四宽度双主题完整专项，因此未修复、未交付产品变更。下一项先以同场景真实浏览器复现并记录计数文字/按钮rect及hit-test，再定位受作用域约束的最小避让策略；不要直接全局隐藏返回顶部、不减小字体或修改目录数据。

拟定范围（定位后收敛）：Library作用域样式、现有真实浏览器审计/必要回归、UI计划日志与本证据；若需共享返回顶部组件改动，必须检查文章与其他页面不回退。验收：390/768/1024/1366双主题滚动不同目录行，真实计数文本不与可见固定按钮相交、按钮仍可点击返回顶部，保留全部既有门禁、T01/authoring/Jekyll及精确main部署/live同场景复验。

gh不在PATH，未创建或编造Issue。无新用户决策，不改旧正文/metadata/URL/hidden/noindex、数据、外部仓库或上一轮COMPLETE。
