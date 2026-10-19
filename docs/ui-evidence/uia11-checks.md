# UI-A11 / UI-022 Thoughts 点赞压缩语法错误

状态：生产限定验收通过，main部署/线上复验validation-pending。不代表全站 COMPLETE，也不代表远端点赞服务健康。

## 实际复现与根因

- base/main `c59add7d72e766757b95688b7edf01af65a3a45e`，2026-10-19 云Chrome实际1363×936，Night/Prospero Light。
- `/thoughts/` 五条计数持续为“…”；Light首条点击后未变色、aria-pressed=false、未disabled。两主题真实截图见 `uia11-cloud/`。
- 控制台5次 `SyntaxError: Unexpected end of input`；只读DOM显示5份点赞脚本均一行，`// A like...`后直接连着countRequestToken及其余代码。并非远端请求超时，也不是审美偏好。
- 同一base在线代表文章《计组笔记 07》Night也实际点击并截图：计数“…”、pressed=false、console同一SyntaxError；`uia11-cloud/article-night-before.jpg`。属于同一共享组件故障，不另开重复问题；修复后文章浏览器交互尚未验证。
- 最小产品修复仅 `_includes/post-like.html` 一行注释由 `//` 改为 `/* */`，保留存储、请求、计数去重与原文/metadata/URL/隐蔽边界。

## 工作分支验证

- 实现head `bcb8c15e324d19aea1b07548ee5bf8ac1a5769d9`，分支 `ui/fix-022`。
- [Actions 39188642432](https://github.com/AplusNeutrino/My_Blog/actions/runs/39188642432)，build job `117856336619` 已于2026-10-19 02:31:02 UTC completed/success。deploy `117861510830`、live `117861511847` 按分支规则skipped，不冒称部署通过。
- 本机276 tests、T01正文/URL/hidden基线44/5/5、authoring44/5/7、diff通过；本机无Ruby/Jekyll/Chrome。
- 本head Actions已完整通过276 tests、T01/authoring/legacy table/production Jekyll、真实压缩产物Thoughts五份/文章一份Node解析、专项8流程，以及Search/Atom、SEO、集成、移动/无障碍、THINK/BUILD原门禁与Ravenis产物。新增3项回归含旧注释故障注入，确实拒绝同类吞尾语法错误。
- 专项artifact `12158993310`，16314300 bytes，独立下载SHA256 `dc229618b1b4f4fb9b8791653b3c50cd2e38a4cc111005b46606cc1596ee51de` 与Actions digest匹配。

## 真实浏览器客户端交互与实际看图

| 实际视口 | 主题 | 初始/点击/键盘/刷新 |
|---|---|---|
| 390×701 | Night / Prospero Light | 两组通过；每组4张视口截图实际查看 |
| 768×757 | Night / Prospero Light | 两组通过；每组4张视口截图实际查看 |
| 1024×757 | Night / Prospero Light | 两组通过；每组4张视口截图实际查看 |
| 1366×757 | Night / Prospero Light | 两组通过；每组4张视口截图实际查看 |

- 8流程均五个独立like key、初始0；真实点击首条变1，原生Tab到第二条并见焦点框，Space激活第二条变1；重复点第一条不重复POST；真实指针hover第三条，刷新后前两条pressed=true且计数1，后三条false/0，全部按钮可用。每组恰好2个fixture POST。
- 实际查看32张viewport组成的8张原生尺寸联系表，放大390 Night刷新、390 Light键盘焦点、1024双主题刷新4张full PNG。计数、点赞色态、焦点框、中文正文与标签可见，没有为审美改样式。此处只验本项，不代替全站、所有文章点赞、其他hover/focus或浏览器缩放矩阵。
- **fixture边界**：独立一次性Chrome profile，只拦截既定点赞origin的/likes与/like；点击前严格核对5份endpoint/path，拒绝超出fixture的真实点赞写入。页面JS/CSS/布局/原生点击与键盘是真实生产产物；fixture计数不是生产服务统计，不证明远端服务健康。
- **截图局限**：Page.captureScreenshot全页PNG对固定侧栏存在与正常viewport不同的捕获效果；全页不用于侧栏布局验收。本项布局判断来自32张正常viewport截图，full图仅补看下部内容/计数。没有把DOM断言当视觉验收。

## 待完成

以最新main c59add7d与审计父提交262c7611为base交付：本轮只更新计划/日志/本证据文档，产品/数据/回归/审计与bcb8c15e完全相同；显式复用同一实现此前已看32张viewport证据，不称本轮新图。获生产限定验收后非强推交付main；新main提交自身Actions/build/deploy/live仍须独立核对，实际线上同场景截图与交互、remote/fallback结果后才关闭UI-022。UI-A11与全站其余矩阵保持pending。gh不可用未建Issue；无新待答用户决定。

看图联系表是由原始viewport PNG拼接的审阅辅助图，不改变页面内容；原始PNG及完整full截图在上述精确head artifact，原始32张viewport SHA256在uia11-production/summary.json。保留一张390 Light联系表供快速对照；其余7张联系表已实际查看但不重复入库，大体积原图继续按Actions artifact归档，不称全部已永久入库。
