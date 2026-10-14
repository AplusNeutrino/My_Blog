# Neutriverse UI 修复执行日志

## 2026-10-14 — UI-003

- Base main c12d9d2ac262e924ce800f7e303f59279a0e9741，上一文档head的run38506420729 completed/success，保护原工作目录使用独立worktree。
- 已读最新AGENTS/domain/issue/triage、ADR0001、主计划/最终报告、本轮计划日志；CONTEXT不存在。gh不在PATH，未编造Issue。
- 复现来自上一精确head的390/768px实际Chrome截图：顶栏为Neutriverse-section / Neutriverse-project。根因：Chirpy topbar在未识别layout的分支回退到page.layout；自定义布局已有page.title但没进入该分支。
- 范围先记录：仅section/project顶栏以page.title呈现；长标题约束在菜单和搜索之间，必要回归覆盖语义标题/完整辅助标题/控件不重叠。四宽度双主题Chrome截图，viewport与侧栏几何补充；其他布局/内容/URL/noindex/外部项目不改。
- 当前in-progress，无新增用户问题。云浏览器仅1363×936，移动视觉与线上复验通过CI浏览器取得；不能用桌面截图冒充手机验收。

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
