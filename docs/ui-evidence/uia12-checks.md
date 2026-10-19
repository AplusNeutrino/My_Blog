# UI-A12 — Ravenis / Occult Atlas 共享导航与控件

- Base/main：`dd55edad557f265429653577b69371abbc565628`（2026-10-19）。精确 [run39197940928](https://github.com/AplusNeutrino/My_Blog/actions/runs/39197940928) build/deploy/verify-live-ui 全部 success；关闭该证据 head pending。
- 预先范围：两应用既有共享导航、主题、滚动、核心控件与返回；Night / Prospero Light，390/768/1024/1366px。先实际复现，未确认不改产品。云浏览器当前仅1363×936；其余尺寸 pending，不能用 DOM 或旧矩阵替代。
- 如确认缺陷，允许最小修改共享导航 include/CSS、应用自身布局/脚本、必要专项回归与 workflow 接入；每个缺陷先另记编号、截图、条件和精确文件。不开发新功能、不修改关联仓库、数据与旧内容、应用 noindex/隐蔽边界。
- 本机 gh/Ruby/Chrome 不在 PATH；未创建或编造 Issue。本地浏览器连接缺 originating browser context，按浏览器技能用云浏览器实际操作。生产与多视口验证必须另取精确 head CI 证据。
- 状态：in-progress；无新增用户决策。全站仍 IN PROGRESS，不写 COMPLETE。

## UI-023 — P1，实际复现后预先记录

- 2026-10-19，base dd55edad，云 Chrome1363×936 Night：Ravenis共享导航进入Atlas，点击“星盘控制”，真实截图 `uia12-atlas-night-open-before.jpg`：标题被顶部共享导航遮住，整个弹层受暗色遮罩覆盖。DOM补充（非视觉替代）：panel hidden=false、fixed/top24/z1000，但父.sky-command z50；body::after scrim z900，共享导航z120。子元素z1000不能逃出父z50的stacking context。
- 最小文件范围：`occult-atlas-app/styles.css`（仅打开时父层级）、`_data/occult_atlas.yml`（资源缓存版本）、必要专项脚本/测试/workflow、计划日志与截图。不改业务/远端服务/内容/路由/noindex。
- 验收：打开后标题与控件可见、弹层在scrim/共享导航之上；四宽度双主题正常viewport截图实际看；真实click、Escape焦点返回、重开、Tab与侧栏开闭/共享导航往返；全部既有门禁、精确head production/Actions、main部署及线上同场景。未验证保留工作分支validation-pending。
- Atlas初始显示服务连接/唤醒，随后出现数据；不把暂态服务延迟直接记成UI缺陷，不修改关联服务仓库。

## 实现与真实验证状态

- 实现：`6c88687ce47212e9eb4035d5c56b22852831b295`，工作分支 `ui/fix-023`。[精确run39203108583](https://github.com/AplusNeutrino/My_Blog/actions/runs/39203108583)，build117900091713运行中；不以其他head的成功代替本次。
- 277 tests、authoring44/5/7、T01正文/URL/hidden44/5/5、专项Python语法与git diff check本机通过。无本机Ruby/Jekyll/Chrome，尚未运行production或多视口浏览器验收。
- 4张本轮云浏览器原截图在 `uia12-before/`，其中Atlas Light/Night均是修复前遮挡，不冒充修复后画面。Ravenis主题切换、筛选展开、共享导航到Atlas及返回、Atlas Escape关闭并恢复触发器焦点已真实操作。
- 新CI专项8流程需要查看正常viewport PNG；机械诊断/故障注入不是视觉验收，远端服务未fixture也不据此全面认证健康。production专项/完整CI/main交付/部署后同场景仍validation-pending。
- 审计记录分支 `audit/ui-a12` 不触发全局Pages队列，避免取消实现CI。main仍dd55edad，产品修复尚未上线；无新增用户决策。下轮先核对6c88687c同一head与截图，不直接合入main。

### 同一实现 production 专项增量（非完整CI/部署验收）

- run39203108583 的 production Jekyll、Search/Atom、压缩点赞脚本及新增OBSERVE专项已success；专项于05:11:40 UTC结束。完整build仍运行，deploy/live尚无成功证据，不将这些子步骤写成整场通过。
- 专项artifact12164324126，3152313 bytes，独立下载SHA256 `0cdee4d0c39c5a61f543db3af05f76254c113c906bc86b020eb2ddc300372035`与Actions digest匹配。
- 实际查看42张正常viewport PNG组成的8张原生尺寸联系表，另放大1366 Light open和390 Night focus两原PNG。原遮挡已消除：弹层标题完整、内容不再被scrim压暗、原生Tab焦点可见；手机展开/滚动画面未见本作用域新增横溢出。8流程click/Tab/Escape焦点恢复/重开/导航返回通过，旧z50注入8次均被同门禁拒绝；390滚动192px、768/1024滚动31px，1366短内容未溢出故scrollTop0，不伪称桌面已滚完整长内容。
- 重要局限：此次CI访问两应用时仍处加载态，Ravenis正文及Atlas服务数据/完整动态选项未加载；图中disabled按钮是原加载状态。没有fixture，但这不是远端健康或已加载业务控件验收；已加载长弹层/查询/导出/星体筛选仍pending，应补线上同场景。布局层级专项通过不等于UI-A12/全站完成。
- `uia12-production/`保存8张已看联系表、2原PNG、原audit.json与42源PNG哈希summary；其余原PNG在精确head artifact（14天），未称全站永久截图。修复前4云图仍独立保存，不混作after。
