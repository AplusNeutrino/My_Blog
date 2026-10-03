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

## Run 2026-10-04 07:00 — T08 范围锁定

- Task / parent：T08；status = in-progress；依赖 T07 done。
- Base SHA / branch：`12d0d70139bcdfa7192820c6f228d9be54bbfbe1` / main。
- 前置核对：从 base 新鲜克隆，工作树无本地差异；base 的 Build and Deploy [run 37157775095](https://github.com/AplusNeutrino/My_Blog/actions/runs/37157775095) completed/success。该结果不替代本次 T08 验证。
- 本次范围：建立 THINK/BUILD/OBSERVE/ABOUT 单一数据源；新增 `/think/`、`/build/`、`/observe/` canonical 页面；ABOUT 保留原页面并接入同一可复用四入口导航；提供各入口基于当前站内事实、可实际到达的链接。OBSERVE 只列 Ravenis/Occult Atlas；BUILD 不公开 Gate/NAVI 工具入口，也不伪造未完成项目详情。
- 拟改文件：四入口数据、共享 section layout/导航/链接 includes、三个新页面、ABOUT 入口接线、共享样式及主题 token 映射、metadata stylesheet 接线、相关测试、主计划、执行日志。
- 验收：四个入口英文名/中文说明/canonical/真实摘要来自单一数据源；三个新 URL 构建存在，ABOUT 旧 URL 不变；全部链接指向已有源或既定 canonical；没有 disabled/coming-soon 假功能；旧 tabs/应用路径不删除；Gate/NAVI/MMXProj 不进入公共数据；Night/Prospero Light 使用同一 DOM 与共享语义 token；全套测试、T01 baseline 与对应实现 SHA 的 Pages workflow 通过。
- 用户问题：无；本项使用已确认的信息架构与站内公开事实。

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
