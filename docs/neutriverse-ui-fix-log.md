# Neutriverse UI 修复执行日志

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
