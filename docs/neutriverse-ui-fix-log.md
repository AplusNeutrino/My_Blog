# Neutriverse UI 修复执行日志

## 2026-10-15 — UI-A07b 复制实值与文档部署恢复

- Base main536281728dcc314c71c64936b06334b2f74bb800，已读最新AGENTS/domain/ADR0001、旧COMPLETE计划/报告与本UI计划日志；CONTEXT不存在、gh不可用。原repo有用户/历史未提交修改，本次另建干净worktree，不覆盖它们。
- run38595958153 build115962616665 success，但deploy115965315382持续updating_pages十分钟超时并取消，live skipped；这是部署状态未完成，不宣称该head上线或视觉通过，不把上一个cd4ec29e成功替代它。重试失败jobs已获工具确认；同head新deploy115988897534 success，verify-live-ui115989007513仍运行。未改workflow超时/门禁，不暂停自动化。
- 任务UI-A07b，范围现有公开阅读审计、必要审计回归与本计划日志。Chirpy现有Copy link复制window.location.href；先为测试origin授予读写clipboard权限，写入非URL sentinel，再真实click原按钮，既要求成功提示，也读实际系统clipboard严格等于当前URL。不替换/spy clipboard API，不JS click，不访问用户剪贴板（仅隔离CI浏览器）。两篇公开文章×四宽度×双主题16场景；旧视觉和媒体断言全部保留。
- 先ui/audit-007b验证production，未验证不提交main。实际剪贴板与精确head生产/线上仍pending；本轮不改网站产品、旧正文/metadata/URL/hidden/noindex或旧COMPLETE历史。无新增待答问题。
- 本机207 tests（含新增2项审计回归）、authoring44/5/7、T01保护44/5/5、diff通过，不代替真实Chrome剪贴板验收。云浏览器1363×936 Light实际点击Copy link，截图成功提示正常，但cloud clipboard API仍读空；仅记验证局限，未确认产品复制故障。等待旧head live完成后才推ui分支，避免共享pages concurrency取消本次恢复验证。

## 2026-10-15 — UI-A07 精确main线上验收

- Task UI-A07限定验收；base/current main cd4ec29eb1ab500563b9247af7ae98ac1661438a。已读最新AGENTS/三domain docs/ADR0001、旧COMPLETE计划报告和本UI计划日志；CONTEXT不存在、gh不可用，未虚构Issue。独立干净worktree，保护用户修改。
- 先记录范围：仅本UI计划/日志、docs/ui-evidence/uia07-checks.md及live JSON/四联系表；验收对应head部署、176+14检查、16阅读记录和40张真实线上截图，不重复修改已验收产品，不把CI替代视觉复核。
- run38590193242精确匹配上述head；build115942706728、deploy115945097313、verify-live-ui115945238565 completed/success。205 Python tests、4项Ruby渲染回归、T01/authoring/production Jekyll/旧门禁与production/live各176+14通过。
- 下载live artifact11906993444，核对16阅读记录：8代码可见、8图片三图加载、8移动touch或桌面arrow下一张/上一张/关闭、16复制反馈；实际clipboardBytes均not-verified。人工看40张viewport/gallery/feedback四联系表，并放大390 Light代码、768 Night弹层、1024 Light图片、1366 Night复制反馈原图。无新增确认显示缺陷，不猜测改样式。
- JSON与四联系表永久入仓库；原PNG留artifact14天。源正文/metadata/URL/hidden/noindex、关联仓库、旧COMPLETE记录未变。本机205 tests、authoring44/5/7、T01保护44/5/5与git diff --check通过；Ruby/production/live证据来自上述CI，不冒称本机执行。
- UI-A07限定done；UI-A07b实际剪贴板内容与其他完整页面/hover-focus矩阵继续pending。非强推文档提交后其CI另行核对，不冒称新文档head已部署；下一项先核对文档head再补复制实值或Library/友链。全站IN PROGRESS，没有新增待答问题，不暂停任务。

## 2026-10-14 — UI-A07 代码/图片/复制与媒体检查

- Base main c5b99ed2284ac327270de5c952f0a026d85d87b3，run38577189934 completed/success已核对。已读AGENTS/domain/ADR0001、旧COMPLETE计划/报告和本UI计划/日志；CONTEXT不存在、gh不可用，不虚构Issue。独立干净worktree，不覆盖用户修改。
- 先限定范围tools/check_think_build_visual.py、计划/日志和公开截图证据，不改产品样式/正文/metadata/URL。UI-A07代表计组07plain代码、FF1图片；两页×四宽度×双主题共16场景，真实控件和截图。候选高亮代码示例经metadata核对为hidden，已排除，不浏览或生成公开证据；plain未提供代码复制按钮属于既有渲染分支，不自行新增功能。
- 云浏览器1363×936 Light：计组07目录跳转代码块后待paint完成，代码5行可读；Copy link点击后出现“链接已复制！”提示，但云clipboard API读为空，记实际字节未验证，不据此报告网站复制故障。
- FF1第一次用基线source_url_candidate的小写ff1路径得到404；通过公开Archive真实链接核对为/posts/FF1%E8%AE%B0%E5%BD%95/，只修审计目标，不改旧路由。页面初始lazy图片未加载不是缺陷；待complete后首图加载成功，实际点击图片打开GLightbox、Next切换成功，动画结束后截图可见。
- 尚未确认新产品缺陷；先ui/audit-007生产完整16截图/交互（总矩阵176+14），再main/live精确head；复制链接反馈与实际剪贴板字节分开记证，后者pending。其他矩阵不冒称完成，无新增待答问题。
- 初始审计head17f592ee1d6ab8af1ce7479829c3936ec43a153d / run38587265953失败：205 tests/4项Ruby/T01/authoring/Jekyll/原门禁通过，新矩阵390 Night图片弹层Next为ElementNotInteractable。下载artifact11905583133并看reading-failure.png，移动弹层显示图片和关闭按钮但无桌面箭头；这是脚本点隐藏控件，尚不是产品故障。调整为箭头可见时真实click，否则真实W3C touch swipe，仍严格核对下一张/上一张/关闭和URL，不JS调用gallery API、不删断言。main c5b99ed2未改，完整生产/live仍pending。
- head952047504e9c64cc3edf3e8d32d632ad052fffeb / run38587922497在W3C swipe动作报MoveTargetOutOfBounds：WebElement.rect是document坐标，文章已滚动后y超出viewport。改用getBoundingClientRect的viewport坐标，真实touch动作与所有翻页断言保留，不改产品。前次非强推ref工具出现一次RemoteProtocolError，读取分支确认未移动后按原expected SHA安全更新成功，没有强推。尚未完成16场景，继续工作分支。
- head5068d0f0f6bdc5d25f9d3bb3108f728c8304bd01 / run38588368297失败：触摸动作不再越界，但390 Night下一张src等待超时。推测新浏览器仅改窗口宽度、没有在gallery初始化前启用触摸能力；现在390/768显式启用CDP touch emulation（maxTouchPoints=1），其余宽度关闭，补失败JSON触摸能力诊断，保留原swiper/下一张src断言。官方源码网络读取失败，未用其作根因证据；不把此推测称产品故障。完整production/live仍pending，main未改。
- 最终审计head2c60e4e1aeff6897447e6a0a90a65251869f547f / run38588924737 completed/success，build115938279064 success（branch deploy/live skipped）。205 tests、4项Ruby渲染回归、T01/authoring/production Jekyll/全部原门禁、176场景+14侧栏专项通过。
- 下载production artifact11906433178，16新阅读记录全部通过：代码可见、3图lazy加载、移动touch swipe/桌面arrow下一张上一张关闭及URL保持、复制提示。看40张viewport/gallery/copy-feedback四宽度双主题联系表，放大390 Light代码、390 Night弹层、1024 Light图片、1366 Light复制提示，无新确认产品缺陷；不猜测改样式。JSON、四联系表及1363px线上Light媒体截图入docs/ui-evidence/uia07*。
- 本机205tests/T01/authoring/diff通过；不冒称本机Ruby或浏览器。审计及证据非强推main（expected c5b99ed2）后，实际main head build/deploy/live176+14与16阅读场景线上截图仍validation-pending；下一轮先核对。不把production通过或cloud桌面图当移动线上验收。UI-A07b复制实际字节pending，其余矩阵继续IN PROGRESS；无新增待答问题，保护项未改。

## 2026-10-14 — UI-005 精确main部署复验

- Task UI-005验收；base/current main5922412f7fc82af68984091e75c142242c290cec，独立干净worktree；已读最新AGENTS/三domain docs/ADR0001/旧主计划与最终报告/本轮计划日志，CONTEXT不存在，gh不可用，未虚构Issue。用户补充无新决定。
- 本次范围仅本计划/日志和docs/ui-evidence/ui005-comparison.md、live JSON/联系表；先核对精确head，再看线上截图，不再重复改已验证产品实现或旧COMPLETE记录。
- run38570020301 head严格匹配base，build115872459830、deploy115874598655、verify-live-ui115874783745均completed/success。4项Ruby渲染回归、205 Python tests、T01/authoring/Jekyll/原门禁与production160+14通过；直接线上160+14通过。CI成功不作为人工视觉验收替代。
- 下载live artifact11898410699；人工看8张表格viewport联系表并放大390 Light/768 Night/1024 Light/1366 Night，另看1366 Light全页两表；行列恢复，原先连续竖线正文消失。8项均2table/2wrapper、局部横向滚轮阅读成功，无整页溢出。对应JSON/联系表永久入docs/ui-evidence，源PNG仍在artifact14天。
- 本机205 tests、authoring44/5/7、T01保护44/5/5与git diff --check再核对通过；没有Ruby/Chrome本机假验证。源md/metadata/URL/hidden/noindex/外部项目未变。
- UI-005 done；其产品实现c20396fa、验收main5922412f，证据文档提交触发的CI另行核对。不把表格一项算完整阅读审计；下一项代码/图片/复制/媒体，Library/友链/观察应用和隐蔽应用仍pending，完整UI计划IN PROGRESS。无新增待答问题。

## 2026-10-14 — UI-005 / UI-A06 表格渲染

- Base9708457fee99f7a00d8d74bb13bf59d669687ad4，run38560753961 completed/success；独立worktree未覆盖用户修改。AGENTS/domain/ADR/旧COMPLETE报告与计划、本UI计划日志已读；CONTEXT不存在，gh不在PATH，未虚构Issue。
- 线上1363×936 Light实际点击计组04目录“三、寻址方式”，待滚动完成后截图看到两张表格变为竖线连续正文；DOM确认article.content table数量0，合法表格文本被p承载。截图ui005-before-table.jpg；根因候选为ATX heading后缺空行，先Ruby实际渲染回归验证，不凭CSS猜测。
- 任务UI-005（P1，阅读行列关系丢失）；范围_plugins/markdown-table-boundaries.rb、tests/test_markdown_table_boundaries.rb、tools/check_think_build_visual.py、现有workflow、计划/日志/公开证据。不修改旧md正文或metadata；仅post pre_render内存输入补表格边界，限定合法header/separator紧邻标题，fenced代码示例与普通文本原样保留。不是全站parser迁移。
- 验收：真实原文渲染两张table、helper幂等/代码示例不变，T01源哈希保持；390/768/1024/1366×Night/Light截图、横向滚轮阅读与无整页溢出；精确branch生产、main部署及live复验。半成品先ui/fix-005，状态validation-pending。代表文章代码/图片及全部阅读控件尚未完成，无新增待答问题。
- 初始head98a03cc161ea45dfb3a23e9a9c1ef582ef092990 / run38568937714在Ruby新测试启动失败：bundle未包含minitest（LoadError），尚未执行渲染断言/production/浏览器，无修复后截图。改为零额外依赖的Ruby断言入口，保留全部4项渲染/保护断言，不改变产品实现、不放宽门禁。205本机tests、authoring44/5/7与44/5/5基线通过；Night桌面亦确认0 tables。
- 修正head c20396fa62672943eda5d675955cc6eeb394d3ea / run38569176497 build115869531704 success；4项Ruby实际渲染测试、205 Python tests、T01/authoring/Jekyll、原门禁通过。160场景+14侧栏专项全部通过；新增8表格场景各2table/2wrapper，四宽度两主题真实pointer-wheel横向滚动全部成功，无整页溢出。
- 下载production artifact11897310795；人工看8截图联系表并放大390 Light/1366 Night，表格恢复行列，保持宽容器内横向阅读。生产JSON/联系表与原线上截图保存docs/ui-evidence/ui005*。分支deploy/live skipped，不能当线上验收；修复和已验证证据非强推main（expected9708457f）后，实际main head的build/deploy/live160+14及8线上截图仍须核对，UI-005保持validation-pending。

## 2026-10-14 — UI-A05接续：侧栏状态诊断

- 最新main93825c66、工作分支2114197f83fbba92cd430b94ded82c892d08b307，run38548101812 failure / deploy skipped。已读最新AGENTS/domain/ADR/旧计划及最终报告/本计划日志；CONTEXT不存在、gh不可用。范围仅审计脚本settle/计划日志，内容/URL/样式不改。
- 下载artifact11884993704并查看scene-failure.png/JSON：1024×900 THINK Light目标，实际Night、主题button x=-228且sidebar关闭，图中左上“召回”控制可见。不是圆角/标题缺陷，也不是按钮加载消失。
- 根因已核对metadata-hook：Archive实际打开文章，post自动收起并写入neutriverse-sidebar-collapsed=true；返回后THINK按存储恢复collapsed。此前脚本只考虑手机抽屉、不考虑desktop已收起状态；在inert侧栏上点击主题失败。
- 本次先通过真实召回按钮恢复展开，再执行主题/截图检查；不清localStorage、不JS click、不改网站默认文章行为或删门禁。保留32检索交互与152整体场景。UI-A05仍validation-pending，先分支production与截图，之后main/live。无新增待答问题。
- head f3d51b79f1b8e813fa7e94b4ebc2592772566277 / run38554138564 build115818958254 success（分支deploy/live skipped符合规则）。205 tests/T01/authoring/Jekyll/原门禁、152场景+14侧栏专项全部通过。artifact11888706352已下载，JSON含32检索场景/32组交互；看32张viewport联系表并放大1024 Light Thoughts，结合390 Night四页与云端Tags/Archive检查暂无新增确认缺陷。没有凭审美改网站。
- 将验证过的审计及本文档证据非强推提交main（expected93825c66），UI-A05仍validation-pending，下一轮核对本次main实际head的build/deploy/live152+14以及同场景截图，不用分支成功代替。矩阵只补该四类核心浏览；Thought点赞/所有focus/代表文章/Library与应用共享导航仍pending。无新增待答问题。

## 2026-10-14 — UI-A05 精确main线上验收

- Task UI-A05；base/main `f755f17c3e1f1a1b66eee714ef4b8ff8aec73cfb`，独立worktree且工作区干净；读取AGENTS/三domain docs/ADR0001、旧计划已COMPLETE及最终报告、本轮计划/日志。CONTEXT不存在，gh不可用，未编造Issue。
- 本轮最小范围：核对同一实现head的Actions/build/deploy/live与32张检索页面截图；只更新NEUTRIVERSE_UI_FIX_PLAN.md、本日志、docs/ui-evidence/uia05-checks.md及live JSON/四张联系表，不改产品、旧内容或旧COMPLETE历史。
- run38554989713 completed/success，head严格匹配base：build115821799412、deploy115823409636、verify-live-ui115823632192均success。205 tests、T01保护、authoring、production Jekyll及所有原门禁通过。生产152+14通过；直接线上152+14通过。deploy完成11:17:36 UTC，live检查11:17:58–11:20:43 UTC，不使用别的提交成功代替。
- 下载live artifact11890351589，核对152项JSON/32组新往返操作；查看390/768/1024/1366两主题32张viewport联系表，并放大390 Light Tags、768 Night Thoughts、1024 Light Archive、1366 Night Series原图。无新增确认遮挡/溢出或内容消失；与生产场景一致，本轮没有猜测改样式。
- 已验证长标签打开/返回、归档文章打开/返回、Series数量/URL/返回、Thought末条稳定锚点/返回；不把这些操作冒充Thought点赞或全部文章阅读。UI-A05 done，完整矩阵仍IN PROGRESS。证据链接见docs/ui-evidence/uia05-checks.md；无新增待答问题。
- 本机复核205 tests和authoring44/5/7通过。基线首个命令遗漏必填--output，CLI拒绝且未改基准；补临时输出路径后44 posts/5 Fragments/5 hidden保护通过，git diff --check通过。本机不冒称production构建或浏览器，以上精确head的Actions承担该验证。
- 本次证据文档提交后的CI尚需下一轮核对，不影响以上明确实现head的已完成验收。下一最小检查组：代表文章代码/表格/图片，两主题四宽度及阅读控件；剩余Library/友链/观察与隐蔽应用仍pending。正文/metadata/文件名/URL/hidden/noindex/外部项目均未改。

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
