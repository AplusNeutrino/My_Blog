# UI-A05 检索页检查

- Base main：93825c661a073c949335538dad8dd48620e11605；UI-001–004历史不重跑或改写。
- 检查范围：Tags、Archive、Thoughts独立页面，以及THINK内Series目录（没有新增/series/路由），390/768/1024/1366两主题共32场景。
- 实际操作：长标签键盘打开/返回、归档文章打开/返回、Series筛选数量/可分享URL/返回、Thought末条稳定锚点/返回。未将点赞、所有hover/focus或全部文章阅读算作已通过。
- 所有原生产门禁保留；本次只改检查脚本及证据文档，没有修改样式、正文、metadata、URL、hidden/noindex或外部项目仓库。

## 失败诊断与修正

- Series现有stateUrl保留目录hash；初始脚本要求无hash的精确URL，已改为仍严格核对path/query，保留数量与返回断言。
- 原移动门禁Escape后立即点trigger，在关闭动画途中坐标(133,24)命中topbar-title；补点击前有限动画等待，不删除焦点断言或改为JS click。
- 2114197f / run38548101812的失败图与JSON（artifact11884993704）显示1024px侧栏已收起，theme按钮x=-228。根因是Archive打开post按网站既有规则收起并记住状态；脚本没召回就点inert控件。f3d51b79通过真实召回按钮恢复展开，保留产品规则，不清存储。
- 前一轮[部分20张联系表](uia05-partial-contact.jpg)与[桌面Archive Night](uia05-archive-night.jpg)不是32项全面通过证据。

## 生产验证与历史待验收

工作分支head f3d51b79f1b8e813fa7e94b4ebc2592772566277 / [run38554138564](https://github.com/AplusNeutrino/My_Blog/actions/runs/38554138564) completed/success。205 tests、基线/authoring/Jekyll、全部旧门禁、152页面场景与14侧栏专项通过。artifact11888706352已下载；看32张检索viewport[联系表](uia05-production-contact.jpg)，放大1024 Light Thoughts与此前390 Night四页原图，暂无确认新产品显示缺陷。32组新往返操作全部通过；完整152项[JSON](uia05-production-audit.json)保留实际窗口/主题/几何/交互。

将检查和证据非强推提交main，精确main提交的build/deploy/live152+14与截图仍待核对。UI-A05维持validation-pending；不能把production截图当线上复验或全站COMPLETE。原152全页+64viewport+14侧栏PNG在artifact保留14天。

## 部署后验收（2026-10-14）

精确main head `f755f17c3e1f1a1b66eee714ef4b8ff8aec73cfb` 的 [run38554989713](https://github.com/AplusNeutrino/My_Blog/actions/runs/38554989713) completed/success：build `115821799412`、deploy `115823409636`、verify-live-ui `115823632192` 均success。205 tests、T01正文/URL/hidden保护、authoring、production Jekyll与原门禁通过；生产和部署后直接访问neutriverse.uk均152页面场景+14侧栏专项通过。部署于11:17:36 UTC完成，线上检查11:17:58–11:20:43 UTC执行。

下载该run的live artifact `11890351589`，核对152项[线上JSON](uia05-live-audit.json)及32组新增往返交互。实际操作最长标签Instruction Set Architecture打开/返回、Archive首条公开文章打开/返回、Series Database Systems筛选数量/精确path-query/返回，以及Thought末条稳定锚点/返回；全部通过，没有用生产截图替代线上证据。

人工逐张查看四宽度双主题32张线上viewport，并放大390 Light Tags、768 Night Thoughts、1024 Light Archive、1366 Night Series原图：标签换行与计数、归档长标题、Thought中文/时间线、Series卡片及筛选控件可见，未确认新的遮挡/溢出/内容消失缺陷。线上与生产在上述场景表现一致，无本次产品样式变更，故不伪造“修复前后差异”。

- [390px 双主题联系表](uia05-live-contact-390.jpg)
- [768px 双主题联系表](uia05-live-contact-768.jpg)
- [1024px 双主题联系表](uia05-live-contact-1024.jpg)
- [1366px 双主题联系表](uia05-live-contact-1366.jpg)

UI-A05限定范围done；Thought点赞/全部hover-focus、代表文章完整阅读、Library/友链、观察应用及隐蔽应用矩阵仍pending。全站计划不是COMPLETE。截图原文件保留在上述artifact（14天）；联系表与完整JSON永久留仓库。gh仍不在PATH，没有虚构Issue。本次仅计划/日志/证据更新，文档提交触发的CI另行核对，不能混用为以上实现head验收。
