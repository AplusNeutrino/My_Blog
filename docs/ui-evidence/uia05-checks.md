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

## 待验收

工作分支head f3d51b79f1b8e813fa7e94b4ebc2592772566277 / [run38554138564](https://github.com/AplusNeutrino/My_Blog/actions/runs/38554138564) completed/success。205 tests、基线/authoring/Jekyll、全部旧门禁、152页面场景与14侧栏专项通过。artifact11888706352已下载；看32张检索viewport[联系表](uia05-production-contact.jpg)，放大1024 Light Thoughts与此前390 Night四页原图，暂无确认新产品显示缺陷。32组新往返操作全部通过；完整152项[JSON](uia05-production-audit.json)保留实际窗口/主题/几何/交互。

将检查和证据非强推提交main，精确main提交的build/deploy/live152+14与截图仍待核对。UI-A05维持validation-pending；不能把production截图当线上复验或全站COMPLETE。原152全页+64viewport+14侧栏PNG在artifact保留14天。
