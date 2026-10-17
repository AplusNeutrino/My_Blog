# UI-012 — 首页近期表达正文避让固定返回顶部按钮

状态：validation-pending。范围先记录2026-10-17，base分支37fa1d786d415388edd7d0559a08cdfda5112ea5；main53787e0bbe111da193918ee959e82780b58d87c3不动。

- 已复现：390 Night原生首页第3帧中，返回顶部按钮覆盖Z.A.T.O.正文首行右端，原图ui012-before-home-390-dark.png。不是单纯审美偏好；Light/其余尺寸尚待本次矩阵验证。
- 根因范围：首页近期表达卡片沿用普通内边距，文字可延伸至固定按钮所在右侧区域。拟仅在无右侧辅助栏布局（<=1199.98px）给.nv-home-transmission预留额外右内边距，不移动共享按钮、不改全站容器/DOM/内容/metadata；宽屏辅助栏把正文与按钮分隔，保持原样。
- 回归：每个首页滚动帧用Range读取近期表达真实文本行矩形与可见返回顶部按钮矩形，严格拒绝交集，保存诊断；四宽度双主题截图人工看原场景与长标题/换行，真实按钮点击及入口往返保留。原192+14和所有专项门禁不减。
- UI-A09另有等待阻塞：精确37fa1d78/run39004907637 build117315276681 failure，deploy117317704915/live117317705669 skipped；artifact12090578680 /485643590 bytes /sha256:7148d9cb1248a08ed9287fb84e3d514564c4df664a9a2fca75ea6938f29de708独立匹配。1366 Light首页从OBSERVE返回后，入口background-color过渡duration180/iterations1/playState running/currentTime0/startTime null；永久旋转动画另有iterations Infinity（JSON序列化null），原门禁已有排除。不能据此断言浏览器内部BFCache根因，但阻塞对象已定位。拟仅真实指针移出入口悬停，再执行同一settle等待，禁止取消动画/改CSS以绕门禁。
- 文件范围：assets/css/neutriverse-sections.css、tools/check_think_build_visual.py、必要回归、本轮计划日志与公开证据。不改数据/原文/旧URL/hidden/noindex、关联仓库或旧COMPLETE。先工作分支验证；production截图/main部署/live未通过前不交付main。gh未安装不编造Issue，无新用户决策。

## 本轮实现（待真实生产验收）

- 2026-10-17生产限定验收：d50f1bc9/run39019844860 build117359307157 success；四宽度双主题首页连续图已看，全部近期表达真实文字行与按钮无交集，390 Night旧Z.A.T.O.原图已放大对照，[修复后原图](ui012-production-accepted-home-390-dark.png)。真实返回顶部/四入口往返、252 tests/4 Ruby/T01/authoring/Jekyll/所有门禁/192+14/24流程通过。可独立交付main，但精确新main部署/live仍pending，不标done；OBSERVE/ABOUT新UI014不与本项混同。

- 2026-10-17接续：d91bd721/run39008835671首次build失败于1366 Night THINK字体就绪脚本，并非UI-012交集断言。390/768/1024双主题首页近期表达Range均无按钮交集；已看六组首页联系表与390 Night第3/4、390 Light第4帧原图，原Z.A.T.O.正文无遮挡。1366、全24流程、main部署/live仍pending，不标done。新UI-013位于精选卡片，不在近期表达选择器范围，已独立排队。同head attempt2 build117337553687运行中，未改变门禁/产品/超时；artifact及局限见uia09-checks.md。

- 真实修复提交be98b7b00369e789f3c65cf38916bc5c2e0ba37f，9个远程blob与本地git hash-object逐项一致；随后只追加SHA检查点。最终分支head生产截图/门禁必须单独核对，未交付main。

- 卡片仅在<=1199.98px增加2.75rem右内边距，保留卡片外框/双主题/DOM与桌面宽屏布局；不宣称所有页面固定栏问题已处理。
- 每张首页原生滚动截图前，TreeWalker/Range提取近期表达所有可见文本行，用实际按钮矩形与显示/透明状态严格检查交集；失败先保存PNG/JSON再抛错。返回流程通过ActionBuilder真实指针移至顶部中间，解除入口hover，再执行原settle；不取消动画、不增加时限、不放宽通过条件，失败动画诊断保留。
- 本机248 tests、authoring44/5/7、T01保护44/5/5、diff check通过；本机没有Ruby/Jekyll/Chrome，修复后四宽度双主题截图/24流程和main/live仍validation-pending，先ui/audit-009。不用静态回归当UI-012已修复并验收。
