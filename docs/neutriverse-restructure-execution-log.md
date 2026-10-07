# Neutriverse 重构执行日志

主计划：[根目录总计划](../NEUTRIVERSE_CONTENT_RESTRUCTURE_PLAN.md)。时间均为 Asia/Shanghai。
只记录真实完成的工作；用户未在本次要求创建自动化。

## Run 2026-10-03 23:10 — T00 决定收敛

- Task: T00（计划准备，网站实现尚未开始）
- Base plan blob: 9847e977cf99a7ee671d1bc641f855fdd8a34227
- Branch: main；用户允许验收通过的小任务直接提交并由现有 Pages 上线。
- 用户决定：Q1/Q2/Q3/Q4/Q7/Q8 按建议；Q5 推荐名单全部纳入，并加入 OfficeSpire，排除 MMXProj；Q6 允许拟写，但严格仅使用网站内已有资料，不透露个人信息。
- 当前焦点：以本网站已有总计划为依据使用“Neutriverse 网站重构”；不推断工作、考试、健康、住址或阅读状态。
- 异步问题：统一记录编号、影响、选项和待答状态，集中提出；跳过受影响任务，继续依赖满足的其他工作。无答案不视为同意；所有剩余项都受阻时如实报告，不虚构进展。
- 本次输出：执行日志初始化；主计划回写答案与执行规则由随后提交完成。
- 验证：读取最新主计划及目录，确认日志路径不存在后创建。纯文档任务不声称完成新 UI、构建或线上功能验收。
- 保护：未修改文章、页面、配置或应用行为；未启动定时任务。
- 下一步：T01 当前内容/路由/可见性/集成基线。定时任务由用户另行安排。

## 待用户决定的问题队列

目前无未解决的启动问题。新问题按 D001、D002 顺序记录，并注明关联任务、影响、已确认边界、推荐方案、状态和首次提出时间。记录后集中通知；不在每小时重复提出已通知的问题。答复回来后同步回写主计划与此队列。

## Run 2026-10-08 07:01 — T21 项目 schema、来源和模板范围

- Task：T21；status = in-progress；依赖 T06、T10 done。
- Base / branch：`5d41704f37f6de7db7e23effda914fe563c4a194` / main；base 是 T20 证据提交后的自动 Library 数据同步，只改个人 Library 公开投影数据；T20 实现 head `0e521a53a1408f56ee657fb1197148f9ed9a68da` 的 [Actions run 37694550921](https://github.com/AplusNeutrino/My_Blog/actions/runs/37694550921) completed/success。
- 本次最小交付：七个批准项目的单一 catalog、稳定 ID、逐项来源台账与通用详情模板；状态、站外链接、关联文章和 releases 均为可选字段，未知即省略。
- 拟改：新增 `_data/neutriverse_projects.yml`、`docs/neutriverse-project-schema.md`、`_layouts/neutriverse-project.html`、`tests/test_project_catalog.py`；必要时补充共享 CSS、首页 Projects 动态状态断言与 390px 门禁；同步主计划/日志。
- 验收：恰有 FitzSight、Akasha Notes、Toyosatomimi's Headphone、Ravenis、Occult Atlas、Gate、OfficeSpire 七个唯一稳定 ID，无 MMXProj；所有公开事实有站内或公开仓库来源；模板对缺 status/links/releases 自然降级，不虚构 Release；noindex/隐藏边界不变；回归、Jekyll、390px 双主题与精确实现 SHA 的 Pages 成功。
- 边界：不提前实现 T22 的 `/build/` 列表/状态筛选，不生成 T23/T24 项目详情页，不改关联项目仓库、旧文章/Fragment、旧 URL 或隐藏入口。
- 用户问题：无。

## Run 2026-10-08 06:04 — T20 首页 Current Signal、精选与状态

- Task：T20；status = done；依赖 T19 done。
- Base / branch：`7ddf9353c4b41f6a8d2d56d2914287f92aa59ed8` / main；base 的 [Actions run 37688234891](https://github.com/AplusNeutrino/My_Blog/actions/runs/37688234891) completed/success。
- 范围提交：`f75a8e6c00a6c674c3cf8581e2e840a598a4f65b`；主体实现：`5e70e23674026679f3ece8efd9f23e594d5ad396`；移动主题门禁修复：`6effe6dc3e99a8d445a4750f1a6ea7c787aa3faf`；final head：`0e521a53a1408f56ee657fb1197148f9ed9a68da`。
- 输出：`_layouts/home.html`、`assets/css/neutriverse-sections.css`、`tests/test_homepage_mixed_stream.py`、`tests/test_homepage_completion.py`、`tools/check_mobile_sidebar.py`。首页已按配置形成六区块完整顺序。
- Current Signal：仅从 `_data/neutriverse_home.yml` 读取已批准的“Neutriverse 网站重构”、现有摘要和 `/about/`，不读取聊天记忆、运行时间或私人状态。
- Featured：先取两条配置文章，再按 `home_popular.posts` 补足；最终顺序为“为什么我要跳过 FF2”“FF1 记录”“计组 02”“计网 03”，四条均匹配 `home_visible_posts`、无重复、无访问量、无 hidden。
- System Status：由公开源动态得到 44 Records、39 posts + 5 Fragments、Last Update 2026-08-17；项目 catalog 尚未由 T21 建立，因此 Projects 指标不渲染，验证了缺数据自然降级。
- 真实失败：run `37694173615` 的 115 tests 与 Jekyll 成功，但门禁在关闭的移动侧栏内直接点击不可见主题按钮；run `37694396230` 已验证六区块和主题切换，却将根层 `overflow-x:hidden` 下的离屏侧栏 `scrollWidth` 误判为用户可横向滚动。两次均未记为通过，随后仅修复门禁的真实交互与现有横向锁定契约。
- 最终验证：[Actions run 37694550921](https://github.com/AplusNeutrino/My_Blog/actions/runs/37694550921) 精确对应 final head，completed/success；build job `113042896498` 的 115 项回归、production Jekyll、390px Chrome、双主题、hidden 检查、Ravenis 与 artifact upload 全部成功；deploy job `113043399090` 成功。
- Artifact：`11515256020`；digest `sha256:60f17f4bc971a11d62b2b4c2ef40587bbcaac1f7c0b34243d4aa2ec2ecbc063c`。
- 保护：未改文章/Fragment 原文或 metadata、文件名、日期、slug/permalink、旧路由、hidden/noindex、外部项目；未提前实现 T21。
- 用户问题：无。active_run = none；checkpoint = T20 done；next = T21。

## Run 2026-10-08 05:02 — T19 首页身份、四入口与混合近期流

- Task：T19；status = done；依赖 T18 done。
- Base / branch：`24edc5d67a4241e042c42d855a0730b02a8f3dda` / main；base 的 [Actions run 37679190641](https://github.com/AplusNeutrino/My_Blog/actions/runs/37679190641) completed/success。
- 范围提交：`70921743c2f0991f03bac65f1b475a6466f4a5b8`；主体实现：`cf2a02914540660645ab2d5a47572963a8387ea6`；测试契约修复：`4e1775b2ed980a8e7a638e88ecbda7127afce5a7`、`7f733b159e2724f368989e15a88fa269f6c23a64`；生成 URL 匹配修复及 final head：`8905c13602bb272a806eca10f22ccd2969f62bc0`。
- 输出：`_data/neutriverse_home.yml`、`_layouts/home.html`、`assets/css/neutriverse-sections.css`、`tests/test_homepage_mixed_stream.py`、`tests/test_homepage_configuration.py`、`tools/check_mobile_sidebar.py`。首页顺序为 Identity → Latest Transmissions → Explore；公开 posts 与原来源 Fragments 按真实日期倒序，显示 8 条并包含 Note/Essay/Fragment；四入口复用既有数据。
- Project Log：Akasha Notes 与 Toyosatomimi's Headphone 仅作为首页次级关系标签；生成路径使用 Jekyll 的稳定百分号编码 URL 匹配，不新增第四种 Type、不修改文章 metadata。
- 真实失败：run `37687050652` 在 110 项回归中因两条 T18 旧断言失败；run `37687173271` 因一条残留 YAML 断言失败；run `37687516979` 已通过 110 项回归与 Jekyll，但 Chrome 检出 Project Log 因中文 URL 编码未显示。三次均未记为通过，随后仅修复对应测试契约或 URL 匹配。
- 最终验证：[Actions run 37687699563](https://github.com/AplusNeutrino/My_Blog/actions/runs/37687699563) 精确对应 final head，completed/success；build job `113019655845` 的 110 项回归、production Jekyll、390px Chrome、双主题、hidden 检查、Ravenis 与 artifact upload 全部成功；deploy job `113020001949` 成功。
- Artifact：`11512292304`；digest `sha256:b8f04c5220a159565bf0a7829ea5287355e1d27180026dc29842ad0e4002ceac`。
- 边界与保护：移除旧首页 category 墙/分页脚本；T20 的 Current Signal、轻量状态与精选区块未提前实现。未改文章/Fragment 原文或 front matter、文件名、日期、slug/permalink、旧路由、hidden/noindex 或外部项目。
- 用户问题：无。active_run = none；checkpoint = T19 done；next = T20（T21 也 ready，按最早依赖先做 T20）。

## Run 2026-10-08 03:58 — T18 范围记录

- Task：T18；status = done；依赖 T17 done。
- Base / branch：`da37689e5a7710eb9e03244e393a59887d99f531` / main；[Actions run 37672947558](https://github.com/AplusNeutrino/My_Blog/actions/runs/37672947558) 精确对应 base，completed/success，无 validation-pending。
- 本次最小交付：建立首页区块顺序、内容来源、固定推荐与 Current Signal 的单一配置契约；现有首页主卡改为最新公开文章优先，为 T19/T20 实现提供稳定输入。
- 拟改：新增 `_data/neutriverse_home.yml`，调整 `_layouts/home.html`，停用旧 `_data/home_recommend.yml`，新增静态回归并扩展 `tools/check_mobile_sidebar.py`，同步主计划与本日志。
- 验收：配置顺序为 Identity → Latest Transmissions → Explore → Current Signal → Featured → System Status；Latest 公开来源明确，固定推荐与 Current Signal 只有一个配置源；首页主卡等于最新公开文章；hidden 不进入主卡/推荐；390px、双主题、回归、Jekyll 与精确 head Pages 成功。
- 边界：T18 不提前实现 T19 的 posts/fragments/Project Log 混合流，也不提前实现 T20 的完整 Current Signal、轻量状态和精选区块 UI。
- 保护：不改文章/Fragment 正文或 metadata、文件名、日期、slug/permalink、旧路由、hidden/noindex 或外部项目。
- 用户问题：无；Current Signal 使用用户已批准且主计划已有的“Neutriverse 网站重构”。

- 范围 / 实现：`b8f20d7433ac6f1c6d4deb0c8432ee51cd970d8c` / `74dd320059aab642d57933960af7adeb142e2034`；均以 expected head 非强推更新 main。
- 实际交付：新增 `_data/neutriverse_home.yml`，统一保存首页六区块顺序、各区块来源、hidden 策略、固定推荐、降级顺序及 Current Signal；旧 `home_recommend.yml` 只保留迁移指针，不再形成第二套值。
- 最新表达：现有首页主卡取消 pin 优先，改取最新公开文章；390px Chrome 从 THINK 构建产物读取最新公开文章真实路径，与首页主卡比较相等。首页主卡和精选候选均来自已过滤的 `all_visible_posts`，五个 hidden 标题未出现在编辑区域。
- 配置契约：Identity 读取 site title/tagline；Latest 声明 visible posts、Thoughts items 与 project 关系；Explore 读取四入口；Current Signal 为“Neutriverse 网站重构”；状态声明公开内容来源。T19/T20 将按该契约实现完整 UI。
- 精确验证：[Actions run 37678793810](https://github.com/AplusNeutrino/My_Blog/actions/runs/37678793810) 对应 final head `74dd320059aab642d57933960af7adeb142e2034`，completed/success；build job `112989195647` 的 105 项回归、production Jekyll、390px Chrome、双主题、Ravenis 与 artifact upload 均成功；deploy job `112989813922` 成功。
- 部署证据：artifact `11508296680`，digest `sha256:7cafeb8a79f405c384c5287ead8f555145b61bf2eb15927dc56c841974fd45ac`。
- 保护：未改文章/Fragment 正文或 metadata、文件名、日期、slug/permalink、旧 URL、hidden/noindex 或外部项目。
- 结论：T18 done；T19 ready。用户问题：无。

## Run 2026-10-08 02:59 — T17 范围记录

- Task：T17；status = done；依赖 T16 done。
- Base / branch：`41e799a58664cc87a187c18a4c7d0472475eac75` / main。
- 上一文档提交核验：`21d21899be575aa1805b85e0ed728bc51396018f` 的 [Actions run 37664158625](https://github.com/AplusNeutrino/My_Blog/actions/runs/37664158625) 回归与 Jekyll 成功，但 390px 侧栏遮罩原生点击被导航链接拦截，未作为通过；稳定门禁修复 `41e799a58664cc87a187c18a4c7d0472475eac75` 的 [run 37671462486](https://github.com/AplusNeutrino/My_Blog/actions/runs/37671462486) completed/success，main 已恢复精确绿灯。
- 本次最小交付：把 Archive、Tags 与 Search 明确纳入 THINK 内部检索入口；保留旧路径，Search 调用现有原生模态框而非假链接。
- 拟改：`_data/neutriverse_sections.yml`、`_includes/neutriverse-section-links.html`、`assets/js/neutriverse-navigation.js`、`assets/css/neutriverse-sections.css`、相关静态回归与 `tools/check_mobile_sidebar.py`、主计划与本日志。
- 验收：THINK 内 Archive/Tags 为真实旧路径链接，Search 为可聚焦 button；侧栏与 THINK 内两个触发器都可打开原生搜索并聚焦；Archive、Tags 与搜索索引继续过滤 hidden；390px、双主题、回归、Jekyll 与精确实现 head Pages 成功。
- 保护：不改 `_posts/`、Fragment 原文/metadata、文件名、日期、slug/permalink、旧路由、hidden/noindex 或外部项目。
- 用户问题：无；使用既有 Search 模态框与已批准 THINK 检索定位，不引入新公开内容。

- 范围 / 实现 / hidden 门禁修复 / Search 关闭门禁修复：`66f4de2d71232b259e1711169763e691f7ba37d7` / `e66a246ca11945ed0558b47e75d85df9ecf9a6c6` / `c5e4dbfea56a7abfaa46f72048015bf5db475ebf` / `8d047175d2da89ee3614f9041b998b2ef8c5303c`；均以 expected head 非强推更新 main。
- 实际交付：THINK “当前可用入口”保留 Archive `/archives/`、Tags `/tags/` 与旧分类兼容路径，并新增真实 Search button；Search 不制造 `href="#"`，而是复用 Chirpy 原生搜索。导航脚本绑定全部 Search 代理，侧栏与 THINK 内入口共用同一原生触发器。
- 可见性：Archive 账本、Tags 索引/详情/关系计数与生成搜索索引都继续从非 hidden 文章读取；构建门禁直接核对五个 hidden 标题不在 Search 索引和实际 `#archives` 账本。
- 失败记录：[run 37672096216](https://github.com/AplusNeutrino/My_Blog/actions/runs/37672096216) 的 100 项回归与 Jekyll 成功，但门禁过宽扫描整个 Archive HTML（含主题辅助数据）而非实际账本；[run 37672371791](https://github.com/AplusNeutrino/My_Blog/actions/runs/37672371791) 确认 Search 打开和聚焦成功，但错误假定 Escape 是 Chirpy 的关闭契约。两次均未标为通过；最终使用实际 `#archives` 与原生 `#search-cancel`。
- 精确验证：[Actions run 37672590085](https://github.com/AplusNeutrino/My_Blog/actions/runs/37672590085) 对应 final head `8d047175d2da89ee3614f9041b998b2ef8c5303c`，completed/success；build job `112967859911` 的 100 项回归、production Jekyll、390px Chrome、双主题、Ravenis 与 artifact upload 均成功；deploy job `112968329095` 成功。
- 部署证据：artifact `11504919047`，digest `sha256:ec4352a24ad4941ae83b34d315b8649c678ea8bf0a71eac93b0c58ee45c519c5`。
- 保护：未改任何文章/Fragment 正文或 metadata、文件名、日期、slug/permalink、旧 URL、hidden/noindex 或外部项目。
- 结论：T17 done；T18 ready。用户问题：无。

## Run 2026-10-08 01:58 — T16 范围记录

- Task：T16；status = done；依赖 T15 done。
- Base / branch：`5eaf4ee45c77eb09c2bd5933a2e4d2fc25b37c9b` / main；T15 文档 [Actions run 37657069525](https://github.com/AplusNeutrino/My_Blog/actions/runs/37657069525) 精确对应 base，completed/success，无 validation-pending。
- 本次最小交付：在不修改任何旧正文/front matter 的前提下，让 Note、Essay、Fragment 在 THINK 清单与文章详情形成语义和视觉可辨识的层级；补齐长文阅读宽度与代码/表格/图片的窄屏容器规则。
- 拟改：`_data/content_taxonomy.yml`、`_layouts/post.html`、`_includes/neutriverse-writing-list.html`、`assets/css/neutriverse-sections.css`、相关静态回归与 `tools/check_mobile_sidebar.py`、主计划与本日志。
- 验收：Note/Essay 详情从同一 taxonomy 显示正确双语 Type 标识并使用不同语义类；THINK 三种记录类齐全；正文宽度约 700–740px，代码/表格/图片不造成页面级溢出；390px Chrome、两主题、回归、Jekyll 与精确 head Pages 成功。
- 保护：不改 `_posts/`、Fragment text/date/type/topic/tags、文件名、slug/permalink、旧路由、hidden/noindex 或外部项目。
- 用户问题：无；差异化遵循已批准的 T07 设计契约，不引入新 Type。
- 范围 / 实现 / 门禁修复：`ba55217e0163dd9ee7958b0d1d03e98f1070167c` / `160c45616ebcca92fb9e8a6e3dffd54c1ea6b7c6` / `f1ddf8190c12c2c37cdcd17ff7ace16fe3590b4d`；均以 expected head 非强推更新 main。
- 实际交付：三种 Type 的双语标签集中在 taxonomy；文章详情从 `page.type` 读取并显示 Type 标识，Note 与 Essay 使用不同语义类和开篇层级；THINK 清单为 Note/Essay/Fragment 输出稳定类型类，分别呈现紧凑记录、编辑型长文和时间戳信号节奏。文章 header/content/tail 限制为 46rem，代码/highlight/table-wrapper 内部滚动，图片、视频与 iframe 不超正文容器。
- 失败记录：[run 37663655248](https://github.com/AplusNeutrino/My_Blog/actions/runs/37663655248) 的 96 项回归和 production Jekyll 成功，但浏览器门禁把 CSS 视觉大写误当成 DOM 文本大写，错误期待 `NOTE / 笔记`；实际 DOM 为语义正确的 `Note / 笔记`。未标作通过；修复只调整门禁断言，不改变页面实现。
- 精确验证：[Actions run 37663923756](https://github.com/AplusNeutrino/My_Blog/actions/runs/37663923756) 对应 final head `f1ddf8190c12c2c37cdcd17ff7ace16fe3590b4d`，completed/success；build job `112938169888` 的 96 项回归、production Jekyll、390px Chrome、Ravenis 与 artifact upload 均成功；deploy job `112938558111` 成功。
- 浏览器验收：从构建后的 THINK 分别取真实 Note/Essay 链接，核对 Type/data/class/双语标识；正文宽度不超过 740px，body 无横向溢出，代码、表格、图片、视频与 iframe 均未逃逸容器。现有主题切换与双主题 token 回归继续通过。
- 部署证据：artifact `11501184118`，digest `sha256:cadb386235f7e19c6c121eff9be232f018efcd3ffae058a33800b5826185635d`。
- 保护：正文插槽仍唯一；未修改任何 `_posts/` 或 Fragment 正文/front matter、文件名、日期、slug/permalink、旧 URL、hidden/noindex 或外部项目。
- 结论：T16 done；T17 ready。用户问题：无。

## Run 2026-10-08 01:02 — T15 范围记录

- Task：T15；status = done；依赖 T14 done。
- Base / branch：`dd27fb3bb1b91287b2014e4317e9438cef734c6d` / main；T14 文档 head 的 Actions 结果在上次日志已核对为 completed/success，无 validation-pending。
- 本次最小交付：把五条 Fragment 的稳定 ID 声明在唯一来源 `_tabs/thoughts.md`，Thoughts 页面锚点与 THINK 混合时间线共同读取，不再各自从日期隐式拼接；当前五个公开锚点字符串保持不变。
- 拟改：`_tabs/thoughts.md`、`_layouts/thoughts.html`、`_includes/neutriverse-writing-list.html`、静态回归、390px Chrome 门禁、主计划与本日志。
- 验收：ID 唯一且格式稳定；五条原文/日期与 T01 基线一致；Fragment 内容不复制；`/think/?type=fragment` 仍为 5 项且来源链接可直达对应 `/thoughts/#<id>`；精确实现 SHA 的回归、Jekyll、浏览器与 Pages 成功。
- 保护：不改任何文章；不改 Fragment text/date/type/topic/tags；不改文件名、slug/permalink、旧路由、hidden/noindex 或外部项目。
- 用户问题：无；这是 T15 既定稳定实体 ID 规则的实现细化。
- 范围 / 实现 / 测试契约修复 / 浏览器门禁修复：`016d3845b1a89cac62d9ca456bbb65354b22923d` / `4e1a842bf8661b47aad68687965dba9cac8816ff` / `8211ae26c0555b07228c66428a139609dbcf14fa` / `cf916da6c46f7d1b5962da92af9f96001b6b6fab`；均以 expected head 非强推更新 main。
- 实际交付：五条 Fragment 各有显式唯一稳定 ID，当前锚点字符串不变；Thoughts 页面和 THINK 来源链接共同读取同一字段，日期派生仅保留为兼容兜底；注释明确同日多条的短后缀规则及发布后不可改约束。唯一正文来源仍为 `_tabs/thoughts.md`，模板没有复制原文。
- 失败记录：[run 37656324275](https://github.com/AplusNeutrino/My_Blog/actions/runs/37656324275) 在回归阶段失败，原因为新测试误计注释示例、旧 T11 断言未同步；[run 37656612002](https://github.com/AplusNeutrino/My_Blog/actions/runs/37656612002) 的 92 项回归和 Jekyll 成功，但长页原生点击被固定层拦截，Chrome 门禁失败。两次均未标作通过；最终门禁改为跟随同一真实普通 href 的 DOM click，不绕过 URL/目标检查。
- 精确验证：[Actions run 37656781396](https://github.com/AplusNeutrino/My_Blog/actions/runs/37656781396) 对应 final head `cf916da6c46f7d1b5962da92af9f96001b6b6fab`，completed/success；build job `112913743570` 的 92 项回归、production Jekyll、390px Chrome、Ravenis 与 artifact upload 全部成功；deploy job `112914304585` 成功。
- 部署证据：artifact `11499200919`，digest `sha256:32e97d3b8bbdc58c129ccbbbbdf5681570f5283e16ee71e665eff50321bce311`。
- 保护：T01 基线继续校验五条 Fragment 的 text/date/type/topic/tags；文章、文件名、slug/permalink、旧路由、hidden/noindex 与外部项目均未改。THINK 仍为 39 篇公开文章 + 5 条 Fragment，筛选直达 5 条。
- 结论：T15 done；T16 ready。用户问题：无。

## Run 2026-10-08 00:04 — T14 Series 目录、筛选与相邻导航

- Task：T14；status = done；依赖 T13 done。
- Base / branch：`4b0be3f61f68acd29217d8598eb3a5a87ad576f1` / main；该 head 的 [Actions run 37642127400](https://github.com/AplusNeutrino/My_Blog/actions/runs/37642127400) build/deploy completed/success，无 validation-pending。
- 范围 / 实现 / 门禁修复：`f390d2223894d12282cd0e38556f518dcbc46659` / `10f4ecf71a815252cce7adb3098d97db4e78c690` / `ac7ca06a20196efcf36156916da91a6d5a372d19`；均以 expected head 非强推更新 main。
- 实际交付：taxonomy 集中定义 database-systems / computer-architecture / computer-networks 三个稳定 ID、标签与说明；新增 Series 目录并以现有公开写作集合即时计数；写作状态新增 `series` 参数、下拉框、目录当前态、刷新/后退与非法值回退；文章系列面板根链接回到对应筛选，并按时间序生成边界正确的上一篇/下一篇。
- 数量：Database Systems 10、Computer Architecture 8、Computer Networks 10，共 28 篇；仅来自显式公开 Series metadata，不从 categories 回退，不复制内容列表。
- 渐进增强：无 JS 时三个目录入口仍是普通 `/think/?series=<id>` 链接，完整 44 项服务端清单不丢；脚本启用后 Database Systems 显示 10 篇，URL、刷新、后退及当前态正确。
- 文章导航：门禁从构建后的 `/think/` 读取真实受保护文章 href；首篇显示 1/10 且仅 next，中间篇 5/10 且 prev/next 指向相邻文章，末篇 10/10 且仅 prev；系列清单保持升序。
- 失败记录：[run 37649992497](https://github.com/AplusNeutrino/My_Blog/actions/runs/37649992497) 的回归与 Jekyll 成功，但 Chrome 门禁把文章路径假定为小写候选 URL，进入非真实页面后失败；未将其记作通过。修复只让门禁跟随构建产物的真实链接，不改文章 URL。
- 精确验证：[Actions run 37650721617](https://github.com/AplusNeutrino/My_Blog/actions/runs/37650721617) 对应 final head `ac7ca06a20196efcf36156916da91a6d5a372d19`，completed/success；build job `112893031112` 的回归、production Jekyll、390px Chrome、Ravenis 与 artifact upload 均 success；deploy job `112893560452` success。
- 部署证据：artifact `11495159334`，digest `sha256:36c5d70c8f16165429b09a8a8c22d0a036826b027c1029372335eb5d73122aa0`。
- 保护：未改旧学习笔记或其他文章/Fragment 的正文、标题、front matter、文件名、日期、slug/permalink、旧 URL、hidden 可见性或外部项目；T15 未提前实现。
- 结论：T14 done；T15 ready。用户问题：无。

## Run 2026-10-07 22:55 — T13 Topic 浏览面与四主题入口

- Task：T13；status = done；依赖 T12 done。
- Base / branch：`c72353c6fa234a8ec5f93b15cdb2dc9b632a8997` / main；该 head 的 [Actions run 37633826334](https://github.com/AplusNeutrino/My_Blog/actions/runs/37633826334) build/deploy completed/success，无 validation-pending。
- 本次最小交付：在 `/think/` 增加 Computation / Humanity / Otaku / Arts 四个 Topic 浏览入口；标签、说明及顺序来自 taxonomy 数据，数量从 T11/T12 的同一公开写作集合即时筛选，不硬编码第二套统计或复制内容列表。
- 范围 / 实现 / 门禁修复：`d2be796a7ef1b617df50227cca31e0868f0c2a0a` / `a4b7874c367e082f34a39653f7ab425f961a242b` / `693c5c3535e55bb21e8149d202e1d6dd4c31cb1c`、`56ee549945d3b61e57b8dd86d67c7b6bab61b82c`；均以 expected head 非强推更新 main。
- 实际交付：新增 `_includes/neutriverse-topic-browser.html`；`content_taxonomy.topic_order` 提供唯一顺序，标签/说明继续来自既有 Topic 数据；组件从传入的 `nv_writing_items` 按 Topic 即时计数。四链接为 `/think/?topic=<id>`，脚本增强后激活筛选并同步 `aria-current`；无 JS 时链接与完整 44 项服务端清单仍存在。
- 数量：Computation 34、Humanity 6、Otaku 3、Arts 1，总和 44，与 39 篇公开文章 + 5 条 Fragment 的同一来源一致。
- 交互验收：Topic 入口激活 Humanity 后显示 6 项并写入 URL；刷新保持条件，浏览器后退回到 All；既有 Type/Topic 组合、排序、分页、空结果及非法参数门禁继续通过。
- 失败记录：[run 37641150181](https://github.com/AplusNeutrino/My_Blog/actions/runs/37641150181) 与 [run 37641420057](https://github.com/AplusNeutrino/My_Blog/actions/runs/37641420057) 均在回归/Jekyll 成功后因 Selenium 对长页下方链接的原生点击被固定界面层拦截而失败；未把它们记作通过。最终门禁对同一真实链接使用 DOM click，普通 href 与 no-JS 兜底另由构建/静态回归校验。
- 精确验证：[Actions run 37641634348](https://github.com/AplusNeutrino/My_Blog/actions/runs/37641634348) 对应 final head `56ee549945d3b61e57b8dd86d67c7b6bab61b82c`，completed/success；build job `112861822320` 的回归、production Jekyll、390px Chrome、Ravenis 与 artifact upload 均 success；deploy job `112862459369` success。
- 部署证据：artifact `11491912924`，digest `sha256:c6c408891eaba643ab1d4bc9b8f4ec0ff4ee01152561bb1c17d9bbabfd61ab70`。
- 保护：未新增 Topic；未改文章/Fragment 内容、front matter、文件名、日期、slug/permalink、旧 URL、hidden 可见性或外部项目；T14 Series 未提前实现。
- 结论：T13 done；T14 ready。用户问题：无。

## Run 2026-10-07 18:58 — T12 组合筛选、排序与分页

- Task：T12；status = done；依赖 T11 done。
- Base / branch：`0ff7e3bb0217f9ee71cc1fd22c0b022be2a3f02f` / main；上一文档 head 的 Actions run `37606136510` build/deploy success，无 validation-pending。
- 本次最小交付：在 T11 服务端完整清单上渐进增强 Type/Topic 组合筛选、newest/oldest 排序、每页 12 项分页和可分享查询参数；刷新、前进/后退保持合法状态，筛选变化回第 1 页，非法参数回退默认。
- 文件范围：`_includes/neutriverse-writing-list.html`、新增 `assets/js/neutriverse-writing-filters.js`、`_layouts/neutriverse-section.html`、`assets/css/neutriverse-sections.css`、`tests/test_think_writing_list.py`、`tools/check_mobile_sidebar.py`、主计划/日志。
- 范围记录 / 实现：`a8b0d0461e5a4faf8129cc5ce92932b27672bfa3` / `e8e70c636ca2456874e0aa25ecc4a341ac78de2d`；均以 expected head 非强推更新 main。
- 实际结果：服务端仍输出 44 项及原始可达链接；JavaScript 启用后默认显示 12/44、4 页，支持 Type = note/essay/fragment、Topic = computation/humanity/otaku/arts、newest/oldest、组合筛选、明确空结果与重置。URL 使用 `type`/`topic`/`sort`/`page`，刷新和浏览器历史恢复合法状态，筛选变化回第 1 页，非法参数回退并规范化。
- 渐进增强：无 JavaScript 时筛选表单保持隐藏且完整 44 项可读可达；分页链接含真实 href；没有把客户端控制伪装成无 JS 可用。
- 390px Chrome：默认 12/44 与 4 页；fragment+humanity = 4；oldest 首项 2024-09-12；刷新保持组合条件，浏览器后退恢复；essay+arts 显示空结果；page 2 可刷新；非法参数回到默认；随后既有 Light/Night、侧栏、焦点和横向溢出门禁继续通过。
- 精确验证：[Actions run 37611360209](https://github.com/AplusNeutrino/My_Blog/actions/runs/37611360209) 对应 head `e8e70c636ca2456874e0aa25ecc4a341ac78de2d`，completed/success；build job `112759102707` 的回归、production Jekyll、Chrome、Ravenis 与 artifact upload 均 success；deploy job `112759519223` success。
- 部署证据：artifact `11477777654`，digest `sha256:668c992fc4263720558f1699ccb61a87905d759266f68ed44744d4534f55afa9`。
- 保护：未改文章/Fragment 内容源、正文、front matter、文件名、日期、slug/permalink、旧 URL、hidden 可见性或外部项目；T13 Topic 浏览面未提前实现。
- 结论：T12 done；T13 ready。用户问题：无。

## Run 2026-10-07 18:02 — T11 写作时间线范围

- Task：T11；status = done；依赖 T03、T05、T10 done。
- Base / branch：`b7fb7920df070d33070206d4f39fcd53b45c2c4f` / main；读取最新主计划、AGENTS、domain docs、taxonomy audit/report、T01 baseline、现有 THINK/Thoughts/layout/CSS/tests。
- 本次最小交付：从现有单一来源合并 39 篇非 hidden 文章与 5 条 Fragment，在 `/think/` 输出 44 项日期倒序列表；明确 Type/Topic，文章保持原 URL，Fragment 返回 Thoughts 稳定锚点；提供无内容空状态。
- 文件范围：`_layouts/neutriverse-section.html`、新增 writing-list include、`_layouts/thoughts.html`、`assets/css/neutriverse-sections.css`、相关测试与 390px Chrome 门禁、主计划/日志。不改 `_posts/`、Fragment 数据、taxonomy metadata、旧路由或外部项目。
- 验收：静态回归 + production Jekyll；构建页面恰有 44 条、35 Note / 4 Essay / 5 Fragment，Topic 为 computation 34 / humanity 6 / otaku 3 / arts 1；首项为 2026-08-17，hidden 条目不输出；390px/双主题无横向滚动且入口可达；精确实现 SHA build/deploy 成功。
- 边界：T12 才实现组合筛选、排序切换、分页和可分享 URL 状态；T11 不提前扩范围。
- 实现提交：`d28ac191c41f316919348b8878977f7b53cb64be`（父提交为范围记录 `3d056912ff09e45bc5caa50dbb834a8e3ddadaee`）；以 expected head 非强推更新 main。
- 实际结果：`/think/` 生成 44 项倒序清单；35 Note / 4 Essay / 5 Fragment，Topic 为 computation 34 / humanity 6 / otaku 3 / arts 1；首项日期 2026-08-17；hidden 标题未出现；文章原链接与 Thoughts 稳定锚点可达；真实空状态存在。
- 精确验证：Actions run `37605371371` 对应 head `d28ac191c41f316919348b8878977f7b53cb64be`；build job `112739422247` 的回归、production Jekyll、390px Chrome 均 success；deploy job `112739815749` success。
- 部署证据：Pages artifact `11474821554`，digest `sha256:288ccb2ac908394dca5dd7b34574682bbdb83159586570d71350005117100550`。
- 保护：未改 `_posts/`、Fragment 原文/数据、文件名、date、slug/permalink、旧路由、hidden 可见性或外部项目；T12 能力未提前实现。
- 结论：T11 done；T12 ready。用户问题：无。
- 后续门禁核验：文档 head `2898a46811aa8170ade88d105a67b41ab0e8a390` 的 run `37605673482` 在回归与 Jekyll 成功后，Chrome 于抽屉已开但 `requestAnimationFrame` 尚未转移焦点时过早断言而失败；这不是站点行为或清单数据失败，仍按真实失败记录。
- 稳定化提交：`b1554ce9d3bbfe9f4e56a2f434b3bbf16d572b5a` 令门禁等待“抽屉打开且焦点进入侧栏”，并将隐藏标题诊断缩减为命中项，避免整份写作清单污染日志。
- 稳定化验证：精确 run `37605887655` success；build `112741125853`（回归、production Jekyll、390px Chrome）与 deploy `112741535916` 均 success；artifact `11475450372`，digest `sha256:6820ea6e1a328cb58e54613937c38918756cc1b92df7c6b6287b190a78ae7dde`。T11 继续为 done，下一项 T12。

## Run 2026-10-07 17:03 — T10.b 手机菜单与窄屏验收范围

- Task / parent：T10.b / T10；status = in-progress；依赖 T10.a done。
- Base / branch：`2a46980d5160e47e5d7e37410dcb6a41cc472f45` / main；最新 main 无并发变化。
- 本次最小交付：在不替换 Chirpy 原生 mobile sidebar toggle 的前提下，同步 trigger 的 controls/expanded，打开后将焦点进入菜单，Escape/mask/导航关闭后恢复 trigger，跨 850px 断点清理移动状态；补足 390px 两主题实际布局与 overflow/触控/入口验收。
- 文件：`assets/js/neutriverse-navigation.js`、`assets/css/neutriverse-sections.css`、相关测试、主计划/日志。不改旧正文、路由、特殊应用或桌面 T10.a contract。
- 验收：自动回归 + T01 基线；精确实现 SHA Pages；浏览器实际 innerWidth 约 390px 时四主入口/三个辅助入口/关闭路径可操作，关键 trigger ≥44px、无 body overflow，Night/Light 一致。无法获得窄屏时不可标父 T10 done。
- 用户问题：无。


### T10.b 交付与验收（最终 done）

- 范围记录 `c7b89d9e71903d3791facc960c4eb20e51980879`；实现链：`63123d19ab5f0cbd05ad8e95b849f03ef32913bb`（mobile controller/CSS/静态回归）、`c1781394d8b04fa667e80b37b1fba40dd53703cf`（在 Pages 构建后加入真实 Chrome 验收）、`fad2f2c6c59c3c1bdd2824d0b2fc1181abb57094` / `796403d9237979f54c05f35c108fbe2332ddb875` / `0ce092bb8844a61a6adbeda101ac35766e535c01` / `d51bf71108fec14b7494c161e8b66f34d2e7d3f5`（校正测试对 HOME、标题节点和侧栏滚动的读取），最终 `337132987101fcb170db718a9713619013fe12d7` 修复真实移动抽屉横向滚动。均 non-force + expected head 保存 main。
- 功能：保留 Chirpy 原生 trigger/mask；同步 `aria-controls=sidebar`、expanded 与打开/关闭标签；打开焦点进入 sidebar，Tab 在打开菜单内循环；Escape/遮罩关闭后回 trigger；跨 850px 清理移动状态。移动 trigger 为 46×44px，sidebar 可纵向滚动，根页面在移动断点锁住横向滚动。
- 第一次功能 head [run 37598635773](https://github.com/AplusNeutrino/My_Blog/actions/runs/37598635773) 已通过 77 tests/Jekyll/部署。新增真浏览器门禁后，失败 runs `37599003282`、`37599228209`、`37599434408` 是断言读取 HOME/编号结构的测试口径校正；`37599637266` 证明已越过入口/焦点检查、定位底部主题按钮需滚动；`37599878310` 首次暴露 Night 打开抽屉时原生位移产生横向滚动，未把失败冒充通过。
- 最终 [run 37600119191](https://github.com/AplusNeutrino/My_Blog/actions/runs/37600119191) 精确 head `337132987101fcb170db718a9713619013fe12d7`：build `112722158257`、deploy `112722471895` success；77 tests、production Jekyll、390px Chrome 门禁、artifact 和 Pages 全通过。artifact `11471544488`，digest `sha256:ebf2eab52a17774d669d1a34deb1d77efa7487881ea4f3808ba1e0c8847bf2a7`。
- Chrome 证据：实际 `innerWidth=390` / `innerHeight=701`；HOME + THINK/BUILD/OBSERVE/ABOUT 与三个辅助入口均可见；trigger 46×44；Light 打开后焦点在 sidebar，Escape/遮罩关闭后焦点回 trigger；Night 主题切换后入口仍完整且横向滚动锁定；导航后菜单关闭。关闭态 body scroll/client width 均为 379（Light）或 375（Night）。
- 保护：实现链仅改导航 JS/共享 CSS/测试与 workflow；未改 `_posts/`、`_thoughts/`、文件名、date/slug/permalink、正文、旧 URL、隐藏可见性或外部项目仓库。T10.a + T10.b 均 done，父 T10 done。
- 调度：只保留“推进 Neutriverse 重构”启用并每小时运行；旧 “Neutriverse Taxonomy Migration” 继续 paused，没有创建重复任务。
- 用户问题：无。下一项 T11 `/think/` 时间序写作列表；T21 也已解锁但按主计划顺序暂后置。

## Run 2026-10-07 16:45 — T10.a 范围锁定（最终 done）

- Task / parent：T10.a / T10；status = in-progress；依赖 T09 done。
- Base / branch：`b7fd898660d9bbabd6d0a8bdd0396069ef014aeb` / main，最新 head 无额外用户差异。
- 本次最小交付：桌面侧栏折叠时不可见控件退出 Tab 顺序；动作标签/expanded 状态与实际一致；Escape 收起、焦点转移与重新展开恢复；保留既有首页展开/文章收起、storage 和 logo 动效规则。
- 拟改：`_includes/metadata-hook.html`、`assets/css/neutriverse-sections.css`、键盘侧栏回归测试、主计划/日志。不改文章、移动菜单本体、外部项目或隐藏入口。
- 验收：全回归/基线保护/精确 SHA Pages；桌面实际浏览器收起→Tab→展开→Escape 与 storage 状态核对。手机菜单与 390px 留 T10.b，父项未全部通过不标 done。
- 调度处理：用户要求保留每小时一次、暂停重复项。peek 只发现一个完整重构任务，原处 paused；已恢复 `6ac11b88fe048191ae937f499e28ed30` enabled/hourly，旧 Taxonomy Migration 保持 paused；没有新建或改其他项目任务。
- 用户问题：无。

### T10.a 交付与验收

- 范围记录 `23108f19456f86ef76911eb520be0f1a01b7037f`；实现 `0968f1da56201a55d3c340dd8c323f6dc7c8c141`，non-force + expected head 保存 main。
- 文件：`_includes/metadata-hook.html`、`assets/css/neutriverse-sections.css`、`tests/test_sidebar_keyboard.py`。桌面折叠令 sidebar inert/aria-hidden，recall 的 hidden/expanded/controls 和 avatar 的动作角色同步；Space/Enter/Escape 与打开/关闭焦点返回；进入手机断点时取消桌面 inert/动作角色；原 native 手机菜单未重写。
- 本地：75 tests OK，其中 Node 运行实际 inline controller，验证折叠/展开/焦点/属性/断点恢复，测试模拟 DOM 不冒充渲染验收；`git diff --check` 通过；T01 baseline protection passed，44 posts/5 Fragments 正文/date/slug/permalink/旧 URL 未改。本地没有 Ruby，构建由精确 CI 验证。
- CI：[run 37596416095](https://github.com/AplusNeutrino/My_Blog/actions/runs/37596416095) head `0968f1da56201a55d3c340dd8c323f6dc7c8c141`；build job `112710055792`、deploy job `112710337878` 全部 success，regression/Jekyll/artifact/Pages 成功。
- artifact 上传证据：`11470288774`，digest `sha256:3752fd415df231da04ee6428e9c193734686febb642076eee7265d0fcbaa20a5`；未声称本次解包验证。
- 实际浏览器：部署后 reload，1363px Night 空格收起→侧栏 inert/aria-hidden、焦点 recall；Shift+Tab 去页脚，不进入隐藏菜单；展开→avatar；HOME Escape→recall；Light Enter 收起/展开→焦点返回正确，recall 焦点环 rgb(25,127,147) solid 2px，Night 为 rgb(95,133,255) solid 2px。role/expanded 状态与可访问树一致。
- 验收限制：可用浏览器 API 未提供 viewport resize；没有进行 390px 真渲染或 native 手机折叠专项。T10.a done，父 T10 in-progress；T10.b ready，下一轮应优先补手机菜单行为及获得可核验的窄视口渲染，不能跳过父依赖推进 T11/T21。
- 调度：恢复同一完整重构任务 enabled/hourly；旧迁移保持 paused，无新增重复任务。无新待答问题。

## Run 2026-10-07 — T09.a 续接与缺陷范围（最终 done）

- Task / parent：T09.a / T09；status = in-progress；依赖 T08 done。
- Base SHA / branch：`15438e1a30715062087f1c05fbfd4c96f103f392` / main；保留其间 PGL 同步与用户首页推荐修改。
- 上次实现：`145d4b9aba56d049a3814140b07def3eff1a513c` 已部署；[run 37164121165](https://github.com/AplusNeutrino/My_Blog/actions/runs/37164121165) build/deploy 成功。上次浏览器验收未完成，不能仅据 CI 标 done。
- 实际浏览器发现：1363px 的 `/think/`，THINK `aria-current` 正确，Search 唤起并聚焦；Tags/Archive 的 li computed display 为 none，旧 Night CSS 的 `:has(.nav-link[href$=...])` 隐藏规则仍覆盖新 utility 菜单。
- 本次边界：删除已失去适用对象的旧隐藏规则，确保次级入口显示；必要的小字可读性修正；增加针对遗留隐藏规则的回归；不改变隐藏工具/索引/应用数据，不实现 T10 手机折叠专项。
- 文件范围：`assets/css/NormaiNight.css`、`assets/css/neutriverse-sections.css`、`tests/test_neutriverse_sidebar.py`、主计划、执行日志。
- 验收：辅助入口可见且链接工作，明暗主题一致，首页/四入口 active/搜索可用；全部测试、T01 正文/URL baseline、精确修复 SHA Pages workflow；父项未满足不得标 done。
- 用户问题：无。

### T09.a 实现与最终验收

- 范围记录：`6f6fa62dbc97cfe2ee863b73f92fa11c4b8fff76`。
- 实现链：`1d809bdf1ba05224f064f9941fec003d40497af5` 删除旧 tab 隐藏规则/文字最小尺寸/回归；`ba33bcbbfdd243b265eb50eeb4f5543dd8eb59ea` 固定辅助按钮宽度与 nowrap；`c50938297d9b9388aceff5df84e60c051973dac9` 清除 Chirpy 的每格 24px 内边距。每次均 non-force + expected head，保留用户变更。
- 第一轮浏览器复验发现搜索文字折行；第二轮 computed geometry 定位 utility li 的左右各 24px 旧内边距，按钮被压至 33px。未把中间修复 CI 成功当最终通过，最后修复后重新检查。
- 最终本地：`PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q`，73 tests OK；`git diff --check` 通过；T01 baseline checker passed（44 posts / 5 Fragments，原文/date/slug/permalink/URL 无变化）。本地无 Ruby，不声称本地 Jekyll。
- CI：最终 [run 37594247954](https://github.com/AplusNeutrino/My_Blog/actions/runs/37594247954) 对应 head `c50938297d9b9388aceff5df84e60c051973dac9`；build job `112702848217` 与 deploy job `112703133929` completed/success，回归/Jekyll/上传/Pages 部署成功。
- artifact：`11469916226` / `github-pages`，digest `sha256:be289d881b1e8f7ac29de1a3f1727b81e7937f2c91443d5cc6b9e99b0e7b9fc8`；仅记录上传证据，未把未经解包的新 artifact 说成逐页检查过。
- 浏览器：实际 1363px，THINK/BUILD/OBSERVE/ABOUT 与 HOME 跳转和 aria-current 正确；Tags/Archive 旧 URL 工作且归属 THINK；搜索 Akasha 返回现有文章，取消恢复；Night/Prospero Light 使用同一菜单。最终部署后 reload 检查辅助三项 display 为 list-item、宽约 81px、li padding 0，标签清晰可见；两主题无 body-level 横向溢出；Tab 焦点到 THINK，2px outline / 3px offset。
- 保护：不修改旧正文、Thought 文本、路由、隐藏配置、社交账号或外部项目；保留用户近期首页推荐和 PGL 同步。没有新增待答问题。
- 结论：T09.a 及父 T09 done；T10 ready。390px 手机导航/折叠/焦点恢复仍属 T10，768/1024/1366 等系统性专项仍按 T31；未提前声称通过。

## Run 2026-10-04 08:02 — T09 范围锁定

- Task / parent：T09；status = in-progress；依赖 T08 done。
- Base SHA / branch：`2c7df63d3a510131cc8563ed9b620c71dd3df2e3` / main。
- 前置核对：从最新 main 新鲜克隆，工作树无本地差异；base 的 Build and Deploy [run 37160986658](https://github.com/AplusNeutrino/My_Blog/actions/runs/37160986658) completed/success。该结果不替代 T09 的精确实现验证。
- 本次范围：用四入口数据替换 Chirpy 旧一级 sidebar tabs；保留清晰的首页返回入口；桌面导航为每项显示英文主标签和中文说明，并按当前 section/路由提供文本与 `aria-current` active 状态；将 Search、Tags、Archive、RSS 及现有公开社交链接作为次级 utilities 保持可达。
- 边界：不删除 `/categories/`、`/thoughts/`、`/library/`、`/links/` 等旧页面；不把 Gate/NAVI/MMXProj 加入公共菜单；不改文章/Thought 正文或 metadata；不在 T09 实现 T10 的手机折叠菜单/专项响应式行为，不改特殊应用本体。
- 拟改文件：sidebar override、桌面导航共享样式、最小 search utility 接线、T09 回归测试、主计划和执行日志；只有必要时才调整既有主题接线。
- 验收：四入口及中文说明来自单一数据源；home/section active 状态正确；首页、搜索、Tags、Archive、RSS、Twitter/GitHub 与既有 BGM 可达；公共菜单无 Gate/NAVI/MMXProj；两主题同一 DOM；全套测试、T01 baseline、构建产物桌面检查及对应实现 SHA 的 Pages workflow 通过。
- 用户问题：无；使用既定 IA、现有站内配置和已公开社交链接。

## Run 2026-10-04 07:00 — T08 完成

- Task / parent：T08；status = done；依赖 T07 done。
- Base SHA / branch：`12d0d70139bcdfa7192820c6f228d9be54bbfbe1` / main。
- 前置核对：从 base 新鲜克隆，工作树无本地差异；base 的 Build and Deploy [run 37157775095](https://github.com/AplusNeutrino/My_Blog/actions/runs/37157775095) completed/success。该结果不替代本次 T08 验证。
- 本次范围：建立 THINK/BUILD/OBSERVE/ABOUT 单一数据源；新增 `/think/`、`/build/`、`/observe/` canonical 页面；ABOUT 保留原页面并接入同一可复用四入口导航；提供各入口基于当前站内事实、可实际到达的链接。OBSERVE 只列 Ravenis/Occult Atlas；BUILD 不公开 Gate/NAVI 工具入口，也不伪造未完成项目详情。
- 拟改文件：四入口数据、共享 section layout/导航/链接 includes、三个新页面、ABOUT 入口接线、共享样式及主题 token 映射、metadata stylesheet 接线、相关测试、主计划、执行日志。
- 验收：四个入口英文名/中文说明/canonical/真实摘要来自单一数据源；三个新 URL 构建存在，ABOUT 旧 URL 不变；全部链接指向已有源或既定 canonical；没有 disabled/coming-soon 假功能；旧 tabs/应用路径不删除；Gate/NAVI/MMXProj 不进入公共数据；Night/Prospero Light 使用同一 DOM 与共享语义 token；全套测试、T01 baseline 与对应实现 SHA 的 Pages workflow 通过。
- 用户问题：无；本项使用已确认的信息架构与站内公开事实。
- 范围记录 / 实现 / 修复提交：`ae9de7696125609b22e3caa1e7a4fda0168e8f6b` / `e5b256505c1ad7e4c8593d49d7c9a5d76336bb6a` / `3818729a1a17e36128d876d5ea06961c7752ab40`。
- 实际交付：`_data/neutriverse_sections.yml` 统一定义四入口；共享 layout、主导航和 section links includes 由该数据渲染；新增 `/think/`、`/build/`、`/observe/`，原 `/about/` 不改路由并接入共享组件；新增主题无关结构 CSS，并在 Night/Prospero Light 中映射 `--nv-*` 语义 token。
- 初次失败：初始实现 head 的 [run 37160568512](https://github.com/AplusNeutrino/My_Blog/actions/runs/37160568512) completed/failure；回归步骤捕获 `test_night_theme_owns_bootstrap_and_related_post_surfaces` 失败。核对 blob 后确认提交接口将大型 `NormaiNight.css` 与 `ProsperoLight.css` 静默截断。未将失败标作 done。
- 修复：通过完整 Git blob（Night `b43d6a7051d7b5a920ffafbabf2598e63225e081`、Light `507a12fb30620ef30316619fae5fafcc73c8b2cd`）恢复主题文件并保留新增 token；修复 head `3818729a...`。
- 本地验收：全套 62 tests OK；T01 baseline protection passed（44 posts / 5 Fragments，Type essay/note/fragment = 5/39/5，正文/文件名/date/slug/permalink/保护 URL 不变）；`git diff --check` 通过。
- 精确 CI：[run 37160746998](https://github.com/AplusNeutrino/My_Blog/actions/runs/37160746998) 的 head 为 `3818729a1a17e36128d876d5ea06961c7752ab40`，build/deploy 均 completed/success；regression tests、Jekyll build、artifact upload、Pages deploy 全部成功。
- 产物验收：artifact `11286954602` / digest `sha256:4d70e6e18f517a598f8f2c7963dc3906e73357edf6928135f8a01d9204060ef8`；`think/build/observe/about/index.html` 和共享 CSS 存在；每页公共主导航只有 `/think/`、`/build/`、`/observe/`、`/about/`；中文说明和 section links 正确；OBSERVE 含 Ravenis/Occult Atlas；公共 section links 不含 Gate/NAVI/MMXProj；两份主题 CSS 大小 148589/70176 bytes。
- 内容/路由/可见性：未改文章或 Thought 正文及 front matter；未删除旧 tabs/路由；Ravenis/Occult Atlas 应用页索引边界未在本项更改；ABOUT 仅复用站内已有资料。
- 结论 / 下一步：T08 done；T09 ready（桌面四入口主导航、返回首页及辅助检索/社交入口）。

## Run 2026-10-04 06:04 — T07 完成

- Task / parent：T07；status = done；依赖 T06 done。
- Base SHA / branch：`df9d33f5e2c845dec388710601f08a780d9a5f5f` / main。
- 前置核对：base 的 Build and Deploy [run 37154464812](https://github.com/AplusNeutrino/My_Blog/actions/runs/37154464812) completed/success；从该 head 新鲜克隆，工作树无本地差异。
- 本次范围：将 `DESIGN.md` 从 Prospero Light 单主题说明升级为 Night / Prospero Light 共享设计契约；消除“保持旧信息架构”和“Ravenis unlisted”等与主计划/Q3 冲突的规则；定义主题角色、文字、8px 间距、组件状态、焦点、动效、移动端与特殊应用边界。只修改规范与契约测试，不在 T07 改 CSS、模板、页面路由或正文。
- 交付文件：`DESIGN.md`、`tests/test_design_contract.py`、主计划、执行日志。
- 验收：四入口与 T06 路由契约优先级明确；Night/Prospero Light 语义等价；字体/阅读宽度/间距/焦点/44px 触控/390–1366px/reduced-motion/无横向页面溢出有机械可查规则；共享组件及 Gate/Ravenis/Occult Atlas 例外边界清楚；旧冲突措辞不存在；全套测试、T01 基线与对应实现 SHA 的 Pages workflow 通过。
- 用户问题：无；本项落实已有视觉与信息架构决定，不新增个人资料或产品范围。
- 范围记录 / 实现提交：`bf3bf1d01becf609c0f8cc1185afc849960e7464` / `6f3ee6e7bc6b4664af34afb9c977394e807a6d1c`。
- 冲突收敛：旧“保持当前信息架构”改为保留 Chirpy shell 能力、用四入口替换旧一级 tab；Ravenis 不再是 unlisted，而是从 `/observe/` 公开发现并继续 `noindex,nofollow`。没有改变实际导航或索引行为，实施仍归后续任务。
- 设计契约：双主题内容/动作/状态等价；复用 `data-mode` / `data-bs-theme` 与既有 storage key；定义 11 个 `--nv-*` 共享角色、四类字体、17px/1.75–1.9/700–740px 阅读规则、8px 主节奏+4px 微步长、九类组件状态和链接/按钮语义。
- 交互/响应式：focus 为 2px + 3px offset；移动目标 44×44px；390/768/1024/1366px 验证；禁止页面级横向滚动和 `transition: all`；reduced-motion 保留功能反馈。特殊应用可保留本地性格，但必须遵守可读标签、键盘、焦点、移动 containment 与隐私/可见性边界。
- 本地验证：新增 8 项契约测试，全套 54 tests OK；`git diff --check` 通过；T01 baseline check passed，44 posts / 5 Fragments、页面源和保护 URL 未变。本地无 Ruby，未声称本地 Jekyll build。
- CI：[run 37157623519](https://github.com/AplusNeutrino/My_Blog/actions/runs/37157623519) 精确对应实现 head，completed/success；测试、Jekyll build、artifact upload 与 deploy 成功。
- 结论 / 下一步：T07 done；T08 ready（创建四入口数据/页面骨架和可复用导航）。

## Run 2026-10-04 05:04 — T06 完成

- Task / parent：T06；status = done；依赖 T01 done。
- Base SHA / branch：`02a1e0c4ac709ac36b4303acc6b02957b876db68` / main。
- 前置核对：base 的 Build and Deploy run 37150692268 completed/success；从该 head 新鲜克隆，工作树无本地或并发差异。
- 本次范围：盘点当前页面源、生成路由、公开入口、索引/robots 语义及特殊模块；建立后续 T07–T33 使用的权威页面归属、路由与可见性映射。只写文档和可重复核对，不在 T06 改线上导航、页面内容、应用或可见性。
- 交付文件：`docs/neutriverse-route-visibility-map.md`、`tests/test_route_visibility_map.py`、主计划、执行日志。
- 验收：覆盖 T01 的 14 个页面源及动态文章/Category/Tag 路由；覆盖首页、THINK 检索面、BUILD/OBSERVE/ABOUT、Library、友链、旅行地球、Gate、NAVI、Ravenis、Occult Atlas、Project Fitzgerald、标签兼容入口；逐项记录当前/目标归属、canonical/兼容策略、公开发现性、noindex、sitemap 与保护边界；Q3/Q4 无遗漏；全文/URL 基线不变；测试与对应 SHA 的 Pages 工作流成功。
- 用户问题：无；Q3/Q4 已 resolved，本项不新增产品决定。
- 范围记录 / 实现提交：`c6c20a8ab14ea585d67560d906ee47990a67c6b4` / `5a01abb2988f4a77e8c4fbc0f2d33931a105b8ee`。范围提交后 PGL 同步 bot 快进了 `5b394610033ba311e7f0368afd14751f91fa5fe2`；实现提交基于 bot head 重建，保留同步数据且未强推。
- 映射结果：14/14 T01 页面源均有当前 URL、当前可见性、目标归属和保护策略；动态文章/Category/Tag、Feed/Search/Sitemap/robots、两个标签兼容路径与新四入口均有契约。特殊模块覆盖旅行地球、友链、PGL、Probe、Gate、NAVI、Ravenis、Occult Atlas、Project Fitzgerald、主题、评论/点赞/RSS/社交/搜索。
- Q3/Q4：Ravenis 与 Occult Atlas 进入公开 OBSERVE 目录但应用页保持 noindex；Library/友链/旅行归 ABOUT；Gate/NAVI 保持 URL 和隐蔽发现，不进入公共主导航/索引。文档另记录 Ravenis robots Disallow 与 noindex、NAVI 缺显式 noindex、Gate 缺 sitemap 排除的当前差异，交 T33 按既定边界收敛。
- BUILD：七个已授权项目完整列入；MMXProj 明确排除；详情与实际应用 URL 分开，未知事实不补写。
- 本地验证：新增 7 项契约测试，全套 46 tests OK；`git diff --check` 通过；T01 baseline protection passed，44 posts / 5 Fragments、14 页面源及保护 URL 均未变化。本地无 Ruby，未声称本地 Jekyll build。
- CI：[run 37154308445](https://github.com/AplusNeutrino/My_Blog/actions/runs/37154308445) 精确对应实现 head，completed/success；workflow 内测试、Jekyll build、artifact upload 与 deploy 成功。
- 结论 / 下一步：T06 done；T07 ready（明暗主题基础规范与共享组件契约）。

## Run 2026-10-04 04:01 — T05 完成

- Task / parent：T05；status = done；依赖 T04 done。
- Base SHA / branch：185236ff7b73934815df6f3c506edd0d40252446 / main。
- 前置核对：base 的 Build and Deploy run 37146695323 completed/success；从该 head 新鲜克隆，未发现并发差异。
- 本次范围：只执行 `Bus` → `System Bus` 与 `Changelog` retire；同步 audit/report；保留两个旧标签 URL；为公开 tag index/detail/trending 增加 hidden 过滤。
- 验收：实际 metadata、权威审计和报告一致；正文/Fragment/受保护 URL metadata 通过 T01 baseline；旧标签 URL noindex 且指向既定目标；全套测试和对应 Pages workflow 成功。
- 用户问题：无。
- 范围记录 / 实现提交：05c34dcd87f73d4638b3074d435c899b779df0a6 / c2cf7da1e969502d34655ad69db3eb8795bb9b5e。
- Metadata / 审计：仅将 `Bus` 改为 `System Bus`、删除 `Changelog`；迁移审计和 final report 同步。当前 149 个文章 Tags、155 个全部写作 Tags、164 次关联，`System Bus` 2 次。
- 兼容 / 可见性：保留 `/tags/bus/`→`/tags/system-bus/`、`/tags/changelog/`→`/tags/neutriverse/` noindex + sitemap false 入口；tag index/detail/trending 统一排除 hidden posts，hidden-only 名称不进入公开索引。
- 本地验证：T04 快照生成物 `--check` 通过；全套 39 tests OK；`git diff --check` 通过；T01 baseline protection passed，44 posts / 5 Fragments 正文、文本及保护 URL metadata 无变化。
- CI：[run 37150481141](https://github.com/AplusNeutrino/My_Blog/actions/runs/37150481141) 对应实现 head，completed/success；回归、Jekyll build、artifact upload、deploy 全部成功。
- 构建产物核对：artifact 11283507681 / digest `sha256:177108483abe5ee333c9328801a2355d1522871535bc6d3fbdd6b5a5d0a0e3ab`。`tags/index.html`、两个旧路径和两个目标路径均存在；公开索引未含 Changelog/Bus/Nhalmasque/RMSPE/Site Styling；redirect noindex/目标正确；抽查 3 个 hidden-only 标签详情均为 0 post links。
- 结论 / 下一步：T05 done；T06 ready。

## Run 2026-10-04 02:55 — T04 完成

- Task / parent：T04；status = done；依赖 T02 done。
- Base SHA / branch：b2a2a15321efb0c443b57f001368227105b1cdce / main。
- 前置核对：base 的 Build and Deploy run 37142886517 completed/success；工作树从该 head 新鲜克隆，无并发差异。
- 本次范围：统计 49 个写作项的当前 Tags；覆盖全部 157 个独立标签，逐项给出 keep/merge/retire 与理由；仅设计 T05 的有限修改和旧 URL 兼容，不在本项改 metadata。
- 拟改：`tools/content_tag_review.py`、`docs/content-taxonomy-tag-review.md`、相关测试、主计划、执行日志。
- 验收：来源/频率/可见性可重复计算；不凭一次使用删除具体作品/实体标签；建议集有限且每项有理由；旧正文、Fragment 文本、文件名、date/slug/permalink 不变。
- 用户问题：无。
- 范围记录 / 实现提交：792176c47f2eeef15f5cc7a2819cc7159109f2e3 / dbdeb5a77cee9f88e106aa861d0523da89716879。
- 交付：`docs/content-taxonomy-tag-review.md`、`tools/content_tag_review.py`、`tests/test_content_tag_review.py`。157 个独立标签、165 次关联均逐项记录 Uses/Public/Hidden/Decision/Target/Reason/来源。
- 频率：150 个标签使用一次、6 个两次、1 个三次；17 个 hidden-only。低频未被当作删除规则，作品/实体和 Fragment 原语言标签保留。
- 决策：155 KEEP；`Bus` MERGE→`System Bus`；`Changelog` RETIRE。T05 应保留 `/tags/bus/`→`/tags/system-bus/`、`/tags/changelog/`→`/tags/neutriverse/` 的 noindex 兼容路径。
- 验证：生成物 `--check` 通过；全套 34 tests OK；`git diff --check` 通过；T01 baseline protection passed，44 posts / 5 Fragments 内容及保护 URL metadata 无变化。
- CI：[run 37146556058](https://github.com/AplusNeutrino/My_Blog/actions/runs/37146556058) 精确对应实现 head，completed/success；build/deploy 均成功。
- 结论 / 下一步：T04 done；T05/T06 ready。T05 可按有限变更集实施，T06 可独立推进。

### T02 验证收敛

- 实现 head `e595599...` 的 run 37139226666 因后续 push 被 Pages concurrency 取消，并非测试失败。
- 直接后续状态提交 `1b9bf7b38c9c0ea79419de55205e9615be39f76e` 包含完整 T02 实现树；run 37139271289 completed/success。T02 done，T03/T04/T06 ready。

## Run 2026-10-04 01:58 — T03 完成

- Task / parent：T03；status = done。
- Base SHA / branch：1b9bf7b38c9c0ea79419de55205e9615be39f76e / main。
- 本次范围：移除无显式 series 的旧 categories 回退；显式 Series 列表排除 hidden 文章；增加回归测试。
- 范围记录提交：378a677efe2f497f4ca108edca68014184585d61。
- 实现提交：338a9c97e1dd615f099ab88ebe011649ca7fcd1a（`fix: require explicit visible series metadata`）。
- 实际实现：无 `page.series` 或当前页 `hidden: true` 时不渲染 Series 面板；有显式 series 时仅按日期列出同 series 且非 hidden 的文章；删除旧 categories/JavaScript 回退。
- 本地验证：`git diff --check` 通过；`PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v` 共 31 项通过。
- CI：[run 37142745038](https://github.com/AplusNeutrino/My_Blog/actions/runs/37142745038) 由实现 head 精确触发，completed/success；包含回归测试、Jekyll build 与 Pages 部署流程，未借用其他提交的结果。
- 保护：不改文章正文、front matter、categories、series 值或 URL；只收紧 Series 展示逻辑。
- 验收：无 series 不渲染；有 series 只列非 hidden 同系列文章并保持日期序；全回归及对应 CI。
- 用户问题：无。
- 结论 / 下一步：T03 done；T04/T06 ready，下轮从中选择最小可交付项。


## Run 2026-10-04 00:01 — T01 基线交付

- Task / parent：T01；status = validation-pending（交付与本地核对通过，CI 未结束）。
- Base SHA / branch：97281227aaafe176870b28bc8a352a0e536e29d6 / main。
- 范围记录：2878fbb0c8d4af0eea7e902a4a8faf4701abf910。
- 实现/交付提交：e1c7f29defce1e2821e81fdd87e4bdbf71597c63。
- 输出：tools/content_restructure_baseline.py、docs/neutriverse-restructure-baseline.json、docs/neutriverse-restructure-baseline.md。
- 覆盖：44 篇文章、5 条 Fragment、14 页面来源、99 集成/布局/配置哈希；全部原文只存保护哈希，不复制新增个人信息。
- 实际统计：44 文章中 5 hidden；全写作 Topic computation/humanity/otaku/arts = 38/6/4/1，Type note/essay/fragment = 39/5/5；157 独立写作 Tags。
- 实际检查：脚本生成/保护核对通过；44 原 Git blobs 逐个匹配 SHA-256；44 源候选 URL 唯一；git diff --quiet 原快照保护源通过；python -m unittest discover -s tests -v 共 27 项通过。
- 已有基线 CI：37132489511，head 97281227... completed/success。
- 新交付 CI：https://github.com/AplusNeutrino/My_Blog/actions/runs/37135823458，head e1c7f29...；最后检查 in_progress。下轮核对该实现提交，不用日志提交的构建代替。
- 环境限制：无 Ruby，未运行本地 Jekyll；线上 sitemap HTTP 403。源 URL 候选未作为已构建链接宣称通过；后续 T33/T38 核查生成路径/robots/线上体验。
- 发现并归入后续任务：显式 Series 无隐藏过滤、旧分类回退（T03）；Tags 目录未过滤 hidden-only 标签（T05/T17）；NAVI robots/Gate sitemap 源层不完整，主题默认 feed/sitemap 行为尚需生成产物验证（T32/T33）。
- 保存方式：CLI clone 可读、直接 push 缺凭据；已用已连接 GitHub 插件 create_tree/create_commit/non-force update_ref 成功保存，未覆盖并发内容。这不是仓库写权限阻断。
- 保护：本次没有修改任何网站功能/旧正文/日期/路径/应用配置。
- 后续：检查 CI 后将 T01 done，解锁 T02 和 T06，优先修正统计报告。
- 用户问题：没有新增需用户决定的事项。


### T01 验证收敛
最终重新读取 run 37135823458：head e1c7f29defce1e2821e81fdd87e4bdbf71597c63，completed/success。T01 改为 done；T02/T06 ready。此前 in_progress 是历史检查记录，不是当前状态。上一条交接记录提交 bab93e7a56161965d26bf8f20e49b5d5677a4e85。


## Run 2026-10-04 01:00 — T02 分类一致性修正

- Task / parent：T02；status = validation-pending。
- Base SHA / branch：c6d8ef5ce1a1a22d635d2f2a9e461509d47852a3 / main。
- 范围记录提交：f5842399e9cedb93569e0f2ecc78f1b9458862d5。
- 实现提交：e595599463b3eee38b4dc38ce6baecbdda7b05a6。
- 输出：修正 docs/content-taxonomy-final-report.md；新增 tests/test_content_taxonomy_consistency.py。
- 结论：44/44 文章 audit 行与当前 type/topic/series/tags 完全一致；5/5 Fragment 的日期/type/topic/tags 一致。Series 为 Database Systems 10、Computer Architecture 8、Computer Networks 10。审计 old/new tags 重新解析为 93/157；当前文章 tags 151、含 Fragments 157。
- 修正：旧报告把 2026-05-02 的 Arts Fragment 计入 Humanity；只改聚合数 humanity 7→6、arts 0→1，总数仍为 49。没有修改内容或 authoritative audit。
- 检查：新一致性测试单独通过；全套 28 tests OK；git diff --check 通过。测试只用 Python 标准库，不新增 CI 依赖。
- CI：https://github.com/AplusNeutrino/My_Blog/actions/runs/37139226666，head e595599...，最后检查 in_progress；下次先核对对应 head。
- 保护：0 篇文章/Fragment/front matter/文件名/日期/slug/permalink 改动。
- 下一步：CI 成功后 T02 done、T03/T04 ready；T06 已 ready，可在 CI 等待或 T02 阻塞时独立推进。
- 用户问题：没有新增需用户决定的事项。
