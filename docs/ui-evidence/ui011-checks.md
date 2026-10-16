# UI-011：Library目录计数被返回顶部按钮遮挡

当前状态：confirmed / validation-pending。P2。Base/复现main `41dca277eace9aa053bcb87e3cd21892b5ae6390`。下文“未修复/ready”为初次记录，最新实现与验证状态见末节。

证据分类：实际线上截图确认，不是用户偏好或源码推测。1024×900、Prospero Light、Library根页、书籍评分分类；将评分区滚动居中后，下方目录“漫画”右侧计数与固定返回顶部圆钮占据相同位置，被按钮表面和向上箭头遮住。截图来自精确head的[run38871666487](https://github.com/AplusNeutrino/My_Blog/actions/runs/38871666487)线上job116880240197，artifact12033767964内`rating-book-1024-light-library.png`，完整artifact摘要已独立验证。不是只凭DOM推断。

![1024 Light线上复现](ui011-before-1024-light.png)

目前没有根因几何诊断、其他滚动位置和四宽度双主题完整专项，因此未修复、未交付产品变更。下一项先以同场景真实浏览器复现并记录计数文字/按钮rect及hit-test，再定位受作用域约束的最小避让策略；不要直接全局隐藏返回顶部、不减小字体或修改目录数据。

拟定范围（定位后收敛）：Library作用域样式、现有真实浏览器审计/必要回归、UI计划日志与本证据；若需共享返回顶部组件改动，必须检查文章与其他页面不回退。验收：390/768/1024/1366双主题滚动不同目录行，真实计数文本不与可见固定按钮相交、按钮仍可点击返回顶部，保留全部既有门禁、T01/authoring/Jekyll及精确main部署/live同场景复验。

gh不在PATH，未创建或编造Issue。无新用户决策，不改旧正文/metadata/URL/hidden/noindex、数据、外部仓库或上一轮COMPLETE。

## 2026-10-16 最小修复与待验收范围

实施base main `600f29073e94b2d8ad17e3365db4c262e9d398f6`；[run38878173427](https://github.com/AplusNeutrino/My_Blog/actions/runs/38878173427) build116898172377/deploy116901351049/live116901426946全部success。本轮云1363×936 Light实际点击书籍评分、滚动目录后看截图并只读测量：计数right1041.8125，按钮left1240.40625/right1284.40625；此宽度计数和按钮无交集。不能调整云视口，不把它当1024/390复测。

源码定位：目录flex space-between把计数推到行右边缘，原行padding未为固定44px按钮预留通道；与已保存1024px截图相符。只在`assets/pgl/pgl.css`的<=1199px（无右侧panel）为`.pgl-category-ledger-item,.pgl-wishlist-entry`增加`padding-inline-end:3.5rem`，沿用既有时间线避让尺度，不改变全局按钮、字号、主题、数据或页面结构。1366px不增加无必要空白。

现有真实浏览器审计新增`library_ledger_controls`：逐个滚动根8计数/愿望单7计数，使目标经过按钮高度（受真实页面长度限制，不伪造页面）；用Range真实文字行判交集、clientWidth判边界。根场景必须按钮可见且hit-test，至少一次目标确实进入按钮垂直带；真实目录进入/返回保持计数、真实按钮点击回顶部。新根目录book/comic/music/wishlist-entry和愿望单首末共48张四宽度双主题PNG/JSON，8组流程；原192+14与全部门禁不删不放宽。

本地233 tests、authoring44/5/7、T01保护44/5/5与diff通过；新增3项仅是作用域/接线回归，不是视觉验收。本机未运行Ruby/Jekyll/Chrome，未取得修复后响应式截图；先`ui/fix-011`，精确head的production192+14/48图/8流程以及main部署/live同场景仍validation-pending。无新用户决策，gh未安装不编造Issue。

## 2026-10-16 生产截图与交互验收

验收head `55c41c973f179e3c500bbe846eba76fd61bc6204`，包含实际修复 `86d8453820eec1eda59f604d4524381a121b25a5`；base main `600f29073e94b2d8ad17e3365db4c262e9d398f6`。[run38885320771](https://github.com/AplusNeutrino/My_Blog/actions/runs/38885320771) build116921858701 success，deploy116924481966/verify-live-ui116924483260 skipped（分支，不是部署通过）。233 tests、4 Ruby、T01/authoring/production Jekyll/Search/feed/SEO/资源/移动无障碍及192+14通过。

artifact12038779445 /211911942 bytes，sha256 `fc46827b17d6e616c63acbb5c05055a26b8b1684e56dafeb030f28d06f0cb489` 独立匹配。已人工看48张390×844、768/1024/1366×900、Night/Prospero Light、根目录book/comic/music/wishlist-entry和愿望单first/last三联系表；放大1024 Light漫画、390 Night愿望单入口与390 Light愿望单末端原图，和修复前1024 Light对照。计数全文可见、按钮不再遮住计数，1366原有布局保持；无新增确认缺陷。

1024px漫画计数刻意滚到按钮垂直带后：Light计数right902.40625、按钮left918.359375，相隔15.953125px；Night计数right898.5、按钮left914.5625，相隔16.0625px。两个主题selectedInButtonBand/buttonHit均true、overlaps为空；不是通过避开问题滚动位置获得“通过”。

8组根8/愿望单7计数逐行滚动、真实文字Range与按钮判交集、可用clientWidth边界、根场景按钮可见且hit-test、目录进入/返回计数不变及真实返回顶部点击均通过；48诊断无横向溢出/scrollX。视觉人工查看和这些机械断言分开记录。

- [390/768根目录四状态](ui011-production-contact-390.jpg)
- [1024/1366根目录四状态](ui011-production-contact-1024.jpg)
- [四宽度愿望单首末状态](ui011-production-contact-wishlist.jpg)
- [完整192 audit及交互](ui011-production-audit.json)
- [48目录计数诊断](ui011-production-ledger.json)

生产验收通过后交付main；UI-011仍validation-pending，必须新main自身Actions/build/deploy及线上同48图/8流程复验，不能以localhost代替线上。本轮仅证据文档、不追加产品改动；无新用户决策，其他全站矩阵仍pending。
