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

### T02 验证收敛

- 实现 head `e595599...` 的 run 37139226666 因后续 push 被 Pages concurrency 取消，并非测试失败。
- 直接后续状态提交 `1b9bf7b38c9c0ea79419de55205e9615be39f76e` 包含完整 T02 实现树；run 37139271289 completed/success。T02 done，T03/T04/T06 ready。

## Run 2026-10-04 01:58 — T03 开始

- Task / parent：T03；status = in-progress。
- Base SHA / branch：1b9bf7b38c9c0ea79419de55205e9615be39f76e / main。
- 本次范围：移除无显式 series 的旧 categories 回退；显式 Series 列表排除 hidden 文章；增加回归测试。
- 保护：不改文章正文、front matter、categories、series 值或 URL；只收紧 Series 展示逻辑。
- 验收：无 series 不渲染；有 series 只列非 hidden 同系列文章并保持日期序；全回归及对应 CI。
- 用户问题：无。


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
