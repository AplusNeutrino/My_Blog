# Neutriverse UI 修复执行日志

## 2026-10-14 — UI-A05接续：侧栏状态诊断

- 最新main93825c66、工作分支2114197f83fbba92cd430b94ded82c892d08b307，run38548101812 failure / deploy skipped。已读最新AGENTS/domain/ADR/旧计划及最终报告/本计划日志；CONTEXT不存在、gh不可用。范围仅审计脚本settle/计划日志，内容/URL/样式不改。
- 下载artifact11884993704并查看scene-failure.png/JSON：1024×900 THINK Light目标，实际Night、主题button x=-228且sidebar关闭，图中左上“召回”控制可见。不是圆角/标题缺陷，也不是按钮加载消失。
- 根因已核对metadata-hook：Archive实际打开文章，post自动收起并写入neutriverse-sidebar-collapsed=true；返回后THINK按存储恢复collapsed。此前脚本只考虑手机抽屉、不考虑desktop已收起状态；在inert侧栏上点击主题失败。
- 本次先通过真实召回按钮恢复展开，再执行主题/截图检查；不清localStorage、不JS click、不改网站默认文章行为或删门禁。保留32检索交互与152整体场景。UI-A05仍validation-pending，先分支production与截图，之后main/live。无新增待答问题。

## 2026-10-14 — UI-A05 检索页视觉矩阵

- Base main93825c661a073c949335538dad8dd48620e11605，run38541205915 completed/success已核对。已读最新AGENTS/domain/ADR/旧主计划与最终报告/本轮计划日志；CONTEXT不存在，gh不可用，不虚构Issue。
- 先记录任务UI-A05（检查，不预设缺陷）：范围tools/check_think_build_visual.py、计划/日志和公开截图证据。Tags/Archive/Thoughts各独立页、Series按现有THINK内目录，无/series/独立路由；不新增路由。390/768/1024/1366双主题32场景，fullpage+viewport；长标签/归档链接/Series筛选及返回、Thought末条稳定锚点及返回。保留旧门禁与全部内容/URL/hidden边界。
- 云浏览器1363×936 Light Tags首屏截图已查看：三列长标签文字和计数可见，暂未确认缺陷；实际点击Cantor Diagonal Argument打开既有详情成功。不能据此宣称移动端或全站通过。
- 先工作分支执行新增矩阵，不凭猜测修改样式。状态validation-pending；待精确head截图人工检查及交互后更新矩阵。无新增待答问题。
- 初始head6bcac453adc10b7e7eb87628c6d55d13141e8d04 / run38546863646失败：390px Night四类截图已生成，Tags/Archive打开返回、Thought稳定锚点返回通过；Series跳转的精确URL断言超时。源码writeState从当前URL创建对象、保留hash，脚本未计入既有目录锚点，改为仍精确核对path/query而容许原hash；数量与返回断言保留，网站行为未改。artifact11885560243已下载，人工看390px Tags与Series viewport，无确认遮挡/溢出；其他视口仍pending。
- 修正head6d0df28f2ba197bcbf3e04385ef9187b25fc9a3c / run38547296531失败：settle主题按钮ElementNotInteractable，不能据此猜测网站根因。新增逐场景日志与失败PNG/JSON（url/mode/open/focus/toggle rect/display），保持所有原断言与真实click；半成品继续ui/audit-005，不合入main。云端Tags双主题/详情返回、Archive Night首屏和滚动到末尾已检查，暂无新增确认缺陷；其他尺寸/完整32矩阵pending。205本地tests、authoring、44/5/5保护通过。
- 已下载artifact11885131572，95项JSON包括390/768两主题及1024 Night；看20张retrieval viewport联系表并放大390 Tags/Archive/Thoughts/Series，中文/换行和目录可见，暂无确认产品缺陷。Thought点赞/更多功能不属于已验证stableAnchor往返，不能冒称通过。
- 诊断head a38ff743a005f311b7d3265ece4a61548a053b86 / run38547751557失败在未修改的原check_mobile_sidebar.py733：Escape后菜单trigger正处于关闭动画，点击point(133,24)被topbar-title拦截。新增等待有限动画结束后再进行原pointer click，所有open/mask/focus断言仍在；没有关闭动画、JS click替代或删除门禁。诊断script尚未运行到新场景，其失败诊断未产生，不虚构截图。
- 本轮范围追加必要原gate的点击稳定等待；实现半成品仍ui/audit-005，main93825c66未改，新增CI/完整32截图与live复验pending。新待答问题无。下轮从本分支最新head核对，而非拿main旧CI当本次成功；公开桌面Archive Night截图与部分联系表保存证据。

## 2026-10-14 — UI-004部署复核 / UI-003a失败诊断

- Base main 787a4a61bb6fa468874968f49acb3d2731555859，AGENTS/三domain docs/ADR/旧主计划与最终报告/本计划日志已读取；CONTEXT不存在，gh不可用。独立worktree，未覆盖用户修改。
- 精确head run38535247898：build115756443059 success、deploy115757821072 success、verify-live-ui115758159364 failure。production205 tests/保护/authoring/Jekyll/全部旧门禁/120场景/14侧栏专项通过；live120场景已完成，但快速mask关闭wait超时。不能将deploy成功或分支通过当线上验收。
- 本轮最小范围：只修正tools/check_think_build_visual.py的点击起始时序并补失败截图/状态诊断、计划/日志。UI-003a/004不改为done。源码与日志显示快速循环开始前只等关闭attribute/focus，没等shell关闭transition；移动中的trigger可能造成指针误点。这是待验证推断，尚未凭它修改网站JS。
- 保留“打开→立即mask点击”的快速场景，仅在每轮开始前等已关闭shell稳定；焦点/两帧/非重叠/hit-test断言全部保留。失败时保存open/focus/trigger rect/mask位置命中与截图，避免无证据重试。先工作分支验证，再精确main/live复验。无新增待答问题。
- 实现/诊断head8415050ddd200f51c471b84e0011e3d46260a305的工作分支run38539640916 build success后，expected-main787a4a61非强推合入main；本机205 tests与authoring通过。
- 精确head的main run38540154437：build115772623467、deploy115774058340、verify-live-ui115774185770均completed/success。production205 tests/T01/authoring/Jekyll/全部原门禁/120场景/14侧栏专项通过，部署后直接neutriverse.uk的120场景/16组筛选返回与14侧栏专项通过。
- 下载live artifact11882032589（120全页+32viewport+14sidebar截图、audit/sidebar JSON），人工看14截图联系表并放大1024×900 Light，短窗滚到底后检索与主题区分开，中文与控件正常；390/768两主题各3次快速mask关闭（共12次），跨两帧焦点仍为trigger，主题切换/Escape与桌面搜索取消均通过。UI-004/UI-003a done；live JSON与联系表持久留docs/ui-evidence。截图表不代替未检查页面，全站未COMPLETE。
- 下一项Series/Tags/Archive/Thoughts四宽度双主题独立视觉/交互检查。无新增待答问题；旧正文/metadata/URL/hidden/noindex未改，gh仍不可用。最终证据文档提交的CI另行核对，不把它冒称已通过。

## 2026-10-14 — UI-004 / UI-003a专项

- Base main 7d376af1f05329dca43861c47c4dde83ded20786，run38526904330 completed/success；独立worktree保留用户修改。已读AGENTS/三domain docs/ADR/旧主计划与最终报告/本轮计划日志，CONTEXT不存在，gh不在PATH，未虚构Issue。
- 先记录范围：assets/css/neutriverse-sections.css、tests/test_sidebar_height.py、tools/check_think_build_visual.py、计划日志。验收：组间无重叠，短窗侧栏可滚动、主题/搜索可点；390/768移动快速mask关闭焦点恢复。两主题，窗口700/900/1100高，记录实际innerHeight，生产与线上同场景截图；旧门禁不放宽。
- 人工查看ui003-live-build-night.png（精确head e020fb73部署后1024×900窗口）确认DISCOVER和社交区重叠。线上1363×936计算：nav min-height=0、flex-shrink=1，内部primary/utility保留内容高度；短窗口nav压缩后内容绘制越界。CSS让profile/nav/bottom不压缩，侧栏纵向滚动；没有缩小字体/隐藏导航或新增设计。
- 状态in-progress，先ui/fix-004分支；UI-003a仍pending。无新增待答问题，其他全站矩阵继续pending。
- 初稿2a8068f5246e7ffd49b3a6f64ea304ea683e7cf1 / run38533201661：205 tests、基线、authoring、production Jekyll、原移动与40项响应式门禁通过；THINK/BUILD脚本在主题点击处失败，坐标x=-214。滚动容器中的关闭侧栏按钮被is_displayed误判为可操作；审计改用实际可见mobile trigger判断抽屉模式，打开后等transition结束并真实滚动到按钮，再pointer点击。未改变主题功能或放宽断言，未合入main。
- a93f494fc10da59d65154a9ff2abf7f1096e3139工作分支run38533540459 success：120场景/14侧栏专项通过，artifact11879545786已下载，人工看14截图联系表并放大1024×900 Night与390×700 Light。非强推main至同一head后run38534120830失败（deploy/live skipped）：新脚本768×700 Night scroll=0、底部在viewport外。开菜单的延迟焦点回到avatar会重置刚设置的滚动；测试需先等原开菜单焦点完成，再滚到底截图。未放宽hit-test/范围/非重叠断言。此前分支success不替代main/live验收；UI-004/UI-003a仍pending，线上尚未更新。
- 修正head ba75465277be11c48c7f4242138842a88effc953 / run38534716282 completed/success。205 tests、保护/authoring、Jekyll、原移动/40响应式、120场景/16组筛选返回、14侧栏专项通过，移动两宽度两主题各3次快速mask关闭焦点断言通过。实现样式没有再改变；修正只等待开菜单焦点定位完成才滚动采证。把该实现及本状态记录非强推提交main，精确main提交的build/deploy/live待核对；UI-004/UI-003a均validation-pending，下一轮先核对同一head和部署后截图，不拿分支CI代替线上通过。gh不可用、无新增待答问题。

## 2026-10-14 — UI-003

- Base main c12d9d2ac262e924ce800f7e303f59279a0e9741，上一文档head的run38506420729 completed/success，保护原工作目录使用独立worktree。
- 已读最新AGENTS/domain/issue/triage、ADR0001、主计划/最终报告、本轮计划日志；CONTEXT不存在。gh不在PATH，未编造Issue。
- 复现来自上一精确head的390/768px实际Chrome截图：顶栏为Neutriverse-section / Neutriverse-project。根因：Chirpy topbar在未识别layout的分支回退到page.layout；自定义布局已有page.title但没进入该分支。
- 范围先记录：仅section/project顶栏以page.title呈现；长标题约束在菜单和搜索之间，必要回归覆盖语义标题/完整辅助标题/控件不重叠。四宽度双主题Chrome截图，viewport与侧栏几何补充；其他布局/内容/URL/noindex/外部项目不改。
- 当前in-progress，无新增用户问题。云浏览器仅1363×936，移动视觉与线上复验通过CI浏览器取得；不能用桌面截图冒充手机验收。
- 接续复核：main c12d9d2ac262e924ce800f7e303f59279a0e9741 / run38506420729 success；工作分支实际head e020fb73e9de4fcd91732c2bc7e281575f3395af / run38509991407 success，非强推快进main后run38526220139验证中。未覆盖用户修改。
- 实现链：b55a54ef93c7aae20a80a1e8ad253e2aa91dc6ec为title模板/溢出样式/新门禁；d86e300d99a073904bdd17174a1db1540da14452补OBSERVE。run38509680549在原390px mask关闭焦点门禁超时，未部署。源码推断竞态为开菜单的rAF在快速关闭后移回焦点；e020fb73e9de4fcd91732c2bc7e281575f3395af增加callback执行时菜单仍打开的条件。原断言没有放宽，204测试/原移动门禁重新通过，记UI-003a。
- 已下载artifact11869786736：120项production场景、16组筛选/刷新/返回、32张viewport截图。看8张viewport联系表，390/768pxTHINK/BUILD/OBSERVE及长项目名标题正常、按钮无遮挡。新JSON记录desktop sidebar rect为[0,260]，viewport展开完整；前轮全页CDP部分裁切并非该viewport实际状态，不凭它改transform。
- 新确认UI-004（P1）：1024/1366×900窗口、两主题viewport，侧栏底部DISCOVER检索组与主题/社交组重叠；不是全页合成疑点。下轮优先以短窗口复现并修复高度布局。截图证据来自精确head artifact，不把测试通过视为视觉正常。
- 本次本地204 tests、authoring44/5/7、T01基线44/5/5与diff check通过。gh仍不在PATH，未虚构Issue；旧正文/metadata/URL/noindex/隐藏应用边界未改。UI-003/UI-003a待main精确head部署与live120场景复验。
- 精确head e020fb73e9de4fcd91732c2bc7e281575f3395af的main run38526220139：build115727074632、deploy115727829396、verify-live-ui115727902355均success。204 tests/T01/authoring/Jekyll/原门禁/production120通过。部署后直接访问neutriverse.uk的live120场景与16组筛选/刷新/返回通过，artifact11875927572已下载；人工查看390pxTHINK Light、长项目名Night、768pxOBSERVE Light与1024pxBUILD Night截图，移动标题正确、控件无遮挡；UI-004在线viewport同样复现。
- 云浏览器1363×936线上THINK：reload后topbar文本/tooltip均THINK，主题Light→Night切换正常。这仅是桌面补充，手机视觉证据以上述live浏览器为准。UI-003 done。
- UI-003a仍validation-pending：保护代码已部署，旧production mask/Escape焦点门禁通过；live120的菜单操作覆盖主题与Escape，但没有独立快速mask关闭焦点断言。下一轮与UI-004短桌面布局优先补此专项，不将已部署当全面交互验收。无新增用户问题。

## 2026-10-14 — UI-002 / UI-A02

- Base main：bc3efad53188f1ff86ae5b49d5a159a136643792；上一轮文档head的run38500584485 completed/success，实际核对，无并发移动。
- 读取最新AGENTS、domain/issue/triage、ADR0001、主计划、最终报告、本轮计划/日志。gh依然不在PATH，未编造Issue；独立worktree保护原工作目录。
- 线上Chrome1363×936 Light：BUILD全页截图、implemented_unverified筛选到1/7、进入OfficeSpire详情均已实际操作；列表/详情没有发现遮挡或横向溢出。
- UI-002复现：项目详情hero/section computed borderTopLeftRadius=0px；--nv-radius-lg和--nv-font-mono为空。仓库CSS引用--nv-radius-lg、--nv-radius-md、--nv-shadow-soft、--nv-font-mono，但全assets/css没有定义。这是无效样式引用，不按审美偏好重新设计。
- 范围与验收先记录：共享CSS补圆角默认值（沿用现有0.5/0.35rem），等宽文本复用--nv-font-data；阴影显式none保持现有表现。新增未定义变量回归与112个THINK/BUILD状态/详情截图场景，四视口两主题。workflow允许ui/**工作分支build但仅main/master可部署。先工作分支通过后合入，main精确headCI/Pages与线上同场景复验。
- 保护：旧正文/metadata/URL/hidden/noindex/项目事实/私有边界/外部仓库不改。暂无新增用户问题。状态in-progress。
- 本地：201 tests、T01正文/URL/hidden基线（44/5/5）、authoring（44/5/7）通过；本机无Ruby/Bundler/Chrome，production和浏览器由精确head Actions执行。
- 工作分支初始head e226865a6b631748180b006c4997bb5c0195563f / run38505052935失败：新审计直接点击移动端隐藏主题按钮。没有网站行为修改，脚本改为真实打开菜单、切换、Escape关闭；未称验收通过。
- 后续head 7deb6fab8088d8d9393cb97ab1e43cf5192a8f05 / run38505335036失败：浏览器返回后smooth滚动未到位，指针点击在视口外（y1383）。改为instant居中滚动后正常pointer click，不JS触发点击、不放宽断言。head 4d7eac959d1448cbdeb490aebf11e1a79a7b66d4 / run38505520642正在验证；deploy工作分支跳过符合预期。
- 线上THINK Night1363×936：Fragment筛选5项、刷新保留、浏览器返回恢复12项均实际操作并全页截图查看；未在这个场景确认新缺陷。
- head4d7eac959d1448cbdeb490aebf11e1a79a7b66d4的工作分支run38505520642 build成功、deploy按条件跳过。201 tests、T01、authoring、production Jekyll和既有门禁通过；新112截图场景/16组交互通过，artifact11867593738下载并看8张联系表，390px THINK控件/正文和项目长标题、1024px OfficeSpire、1366px BUILD放大查看。截图是实际production浏览器，不把几何断言当人工视觉验收。
- UI-003新确认：390/768px顶栏显示内部layout名Neutriverse-section / Neutriverse-project；下轮独立修复，不以测试通过视为全站正常。1024/1366px全页CDP截图侧栏出现部分裁切疑点，尚未断定是真实布局缺陷还是截图合成，下一轮先补viewport与侧栏开闭复现证据。
- 线上Night桌面搜索：输入“计网”显示10项公开结果，全页截图检查；取消返回THINK正常。无新增待答问题。
- main复核仍为base后非强推快进至4d7eac959d1448cbdeb490aebf11e1a79a7b66d4；本次main run38505942304待精确head build/deploy与线上复验，UI-002仍未标done。
- 完成：main run38505942304 completed/success，精确head4d7eac959d1448cbdeb490aebf11e1a79a7b66d4；build115663355032、deploy115664001709均success。201 tests、T01、authoring、production Jekyll、112新截图/16交互及旧门禁通过。线上OfficeSpire1363×936双主题hero8px / section5.6px、IBM Plex Mono字体栈；逐张前后截图确认，主题切换、详情返回BUILD与implemented_unverified筛选1/7、实际article圆角8px通过。UI-002 done；JSON、8联系表和前后图持久保存在docs/ui-evidence。
- 下一项UI-003与侧栏截图疑点复现，其他页面矩阵仍pending；没有需要用户决定的新问题，继续独立工作，不将局部通过写成全站COMPLETE。

## 2026-10-14 — UI-001 / 初始化

- Base：`dd2e52ee17322519190fdacf1a12e5d35f035ead`，最新main包含用户后续首页推荐更新和Library同步；独立worktree保护旧工作目录。
- 已读取AGENTS、docs/agents三文档、ADR0001、主计划/最终报告；CONTEXT不存在，本轮计划/日志此前不存在。
- gh CLI不可用（PATH中没有gh）；未创建或虚构GitHub Issue，暂以UI-001台账记录。
- 真实线上Chrome 1363×936：THINK Light/Night截图均看到两列导航卡片底部不齐；点击头像收起/展开侧栏、点击主题切换后等待完成再看截图。
- 几何复现：Light收起侧栏时OBSERVE卡片122.171875px，所在单元格144.5625px；Night展开侧栏时THINK/OBSERVE卡片122.171875px，BUILD/ABOUT144.5625px。差22.390625px。根因：Grid拉伸li但li内部a未拉伸。
- Task：UI-001，P2；计划范围：assets/css/neutriverse-sections.css，tools/check_responsive_accessibility.py，.github/workflows/pages-deploy.yml，本计划与日志。
- 验收：导航卡片填满单元格，两主题四视口及首页/四入口；必要回归、保护、authoring、production build、精确headCI/Pages与线上截图；不改任何内容或链接。
- 当前：in-progress。待答问题：无。

- 实现：导航li设为flex，内部链接flex:1，填满同一Grid行的高度；不设固定卡片高度、不截断文字。
- 回归：production的40项响应式矩阵新增卡片/单元格上下及宽度差<=1px断言；修复前22.39px差会触发此门禁。生成40张公共导航截图及几何JSON，作为14天CI artifact保存，未发布到站点。
- 本地实际验证：197 tests通过；44 posts/5 Fragments/5 hidden保护基线通过；authoring 44/5/7通过；Python编译与diff check通过。本机没有Ruby/Bundler、Selenium/Chrome，production构建与浏览器矩阵交由本次精确head的Actions验证，尚未称通过。
- 当前：validation-pending，待精确实现head的CI/Pages与部署后线上复验。

- 发布路径：本地git push缺少HTTPS凭据，未改变远端；改用已连接GitHub的tree/commit与expected-head非强推ref更新。

- 实现提交：d5465ce91413b820063290b3258b0a14c0c19116；run 38499382899失败、deploy跳过。197 tests、保护、authoring、Jekyll、Search/feed、SEO、资源已通过；移动门禁在首页featured硬编码断言失败，尚未执行新导航矩阵，没有截图artifact。
- 必要门禁修复UI-001a：用户base的home_popular.yml已自动更新，旧门禁仍期待计网03。改为从当前首页配置、热门推荐、已构建公开Search索引计算精确预期；保持固定推荐优先、popular顺序、最新补齐、hidden/不存在/Fragment排除、去重和limit，不修改数据或产品行为。新增3项真实预期测试覆盖动态推荐变化和排除，未删除或放宽门禁。

- 门禁修复提交c7ec321ba9cf458fda7fea9ec43ad0fe4ea580b5 / run38499644956：移动门禁已通过；新导航矩阵执行到截图阶段发生Chrome element screenshot renderer timeout，部署跳过。产生25张部分截图artifact11865630083，不称40项全部通过。改为先instant滚动到导航，再保存带页面上下文的viewport截图，保存失败仍阻断，所有几何/焦点/对比门禁保持。

- 人工看run38499644956的25张部分导航截图：Light中文正常、Night显示方框；线上Night中文正常。这是CI系统缺少CJK fallback字体，不作为网站缺陷。给production浏览器环境安装fonts-noto-cjk以取得有效中文截图。此前element截图有被视口截断，已改上下文viewport截图；不会将这些部分截图当全站验收。

- 截图收敛head eb43672fffdc7288ebaa2f221f024be5c4f30414 / run38499996282被新中文字体环境提交取消；不视为通过。
- 最终实现head：0348b33c7e00a5f4584181c8d7244da88fc50244；[Actions38500122266](https://github.com/AplusNeutrino/My_Blog/actions/runs/38500122266) completed/success，build115644835170、deploy115645302262均成功；200 tests、T01保护、authoring、production Jekyll、Search/feed、SEO/旧路由、资源/集成、390px移动门禁、40项响应式/无障碍与导航几何、Ravenis及artifact均通过。
- 视觉artifact11865525942含40张viewport截图+40项JSON，已下载并人工查看联系表；中文方框问题已消除。导航几何最大bottomDifference=0px。github-pages artifact11865278209。截图artifact保留14天；代表性线上前后截图与完整几何JSON写入docs/ui-evidence永久保留。
- 线上部署后Chrome1363×936：/think/ Light和Night展开侧栏均4张卡片144.5625px、cell144.5625px；前后截图逐一确认边框底部对齐，中文换行与文字/入口原样保留。双主题切换正常。
- 本轮额外看到THINK Light1363px列表、Fragment筛选、分页/辅助导航区，未在这些画面确认新的显示缺陷；首页Night首屏已看。未冒称全页面/全尺寸审计完成。
- UI-001 done。原文、metadata、文件名/date/slug/permalink、旧URL、hidden/noindex、应用业务与外部仓库未改变。gh不可用已记；无新增待答问题。下一项THINK筛选/分页与BUILD列表/详情的全页视觉矩阵。
