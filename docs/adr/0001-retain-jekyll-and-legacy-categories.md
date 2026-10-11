# ADR 0001: 保留 Jekyll/GitHub Pages 与旧 categories 兼容层

- Status: Accepted
- Date: 2026-10-11
- Decision owner: Neutriverse site
- Scope: `AplusNeutrino/My_Blog`
- Related plan task: T35

## Context

Neutriverse 本轮重构已经在现有 Jekyll/Chirpy 与 GitHub Pages 架构上完成四入口、THINK 检索、项目目录与详情、OBSERVE、ABOUT、双主题、Search/Atom、SEO、响应式及性能门禁。Q8 已明确本轮保持 Jekyll/GitHub Pages，并保护现有路由。

当前实现证据如下：

- `Gemfile` 使用 `jekyll-theme-chirpy ~> 7.6`；站点由 `.github/workflows/pages-deploy.yml` 执行 production Jekyll build 并发布到 GitHub Pages。
- T34 的实现 head `fd9395f12e356728602a017d483a5f7fa4d38e83` 已在 Actions run `38107144418` 通过 183 项回归、production Jekyll、Search/Atom、SEO/旧路由、资源/集成、真实浏览器响应式/无障碍矩阵和 Pages deploy。
- T01 基线记录 44 篇文章与 5 条 Fragment；目前不存在需要服务端渲染、用户账户、私有个性化状态或写入型应用后端的本轮页面需求。
- Library、Ravenis、Occult Atlas 等交互模块通过独立脚本、数据端点和渐进增强运行，不要求替换站点生成器。
- 44 篇旧文章全部仍有 `categories` front matter，共 15 个 category 名称、87 次关联。`jekyll-archives` 生成 `/categories/:name/`；`/categories/` 与文章详情继续提供旧分类链接。
- 新权威内容语义是 `type`、`topic`、可选 `series` 与 canonical `tags`。THINK、Series、Search 和 feed 不依赖旧 category；T03 已移除用 category 推断 Series 的回退。

因此需要回答两个长期问题：何时平台迁移才有充分理由，以及旧 categories 在新 taxonomy 生效后如何维护。

## Decision

### 1. 继续使用当前平台

Neutriverse 继续使用 Jekyll/Chirpy、GitHub Actions 与 GitHub Pages。此次决定不安排平台迁移、框架重写、CMS 或第二套并行站点。

理由：

1. 当前平台已满足公开静态内容、稳定旧 URL、双主题、渐进增强应用和自动部署需求。
2. 现有 production workflow 已覆盖内容回归、Jekyll 构建、Search/feed、SEO/断链、资源边界、移动端和无障碍；迁移会重新引入这些已解决风险。
3. 当前交互需求可以作为受作用域约束的客户端模块存在，尚未形成必须由应用框架统一管理的共享运行时。
4. GitHub Pages 的静态发布模型与本轮“不增加登录、CMS、私人数据和新后端”的边界一致。

### 2. 平台迁移只能由能力缺口触发

以下任一情况持续出现，且无法用小范围改动安全解决时，才进入新一轮架构评估：

| 触发器 | 必须提供的证据 |
|---|---|
| 需要服务端或用户级状态 | 已批准的产品需求确实需要登录、私有数据、服务端授权或写入型工作流，而非仅为技术偏好 |
| 构建/发布不可接受 | 连续构建数据表明 Jekyll 构建时间、失败率或 Pages 限制阻碍正常发布，并已尝试缓存或增量优化 |
| 客户端模块无法再隔离 | 多个应用必须共享类型化路由、状态和打包边界，现有渐进增强方式产生可复现的维护或性能问题 |
| 内容模型无法可靠校验 | Type/Topic/Series/Tags、项目或关系数据的验证需求超出当前数据文件与测试可维护范围，并有具体失败案例 |
| 平台能力阻止已批准功能 | GitHub Pages 或 Jekyll 的明确限制直接阻塞已批准的必交付功能，且没有等价的静态实现 |

主题流行度、框架新旧、想统一技术栈、单次 CI 波动、纯视觉改版、继续增加静态文章或单个独立应用，都不是迁移触发器。

触发器成立后也不能原地大爆炸式替换。必须另建 ADR 和独立验证分支，至少完成：

1. 盘点 T01 保护 URL、canonical、noindex/sitemap、Search/feed 与特殊应用入口。
2. 以代表性文章、Fragment、四入口、项目页和一个特殊应用制作可丢弃的 proof of concept。
3. 同时构建旧版与候选版，比较生成 URL、正文哈希、metadata、内部链接、双主题、移动端与性能门禁。
4. 为每个无法原地保留的 URL 提供显式兼容映射；没有“默认应该能重定向”的假设。
5. 只有完整回归和真实部署证据通过后，才另行决定切换与回滚办法。

### 3. categories 是只读兼容层，不是新 taxonomy

旧 `categories` 按以下规则维护：

| 对象 | 规则 |
|---|---|
| 现有文章 front matter | 保持原值；不为整理结构而批量删除、改名或重排 |
| `/categories/` | 保留为可直达的旧分类兼容目录，不提升为四入口或 THINK 主浏览 |
| `/categories/:name/` | 继续由 `jekyll-archives` 生成并只列公开文章；保护现有旧链接 |
| 文章详情 category 链接 | 在兼容层存在期间保留，明确位于 canonical taxonomy 之后 |
| Type / Topic / Series / Tags | 唯一权威语义；禁止从 category 推断、回填或覆盖这些字段 |
| 新文章 | 不强制填写 `categories`；只按作者指南填写权威字段。确需兼容某个既有旧分类时可显式添加，但不能创造第二套分类规范 |
| 新 category 名称 | 默认不新增；只有明确的旧链接兼容需求才允许，并记录理由 |
| 统计、筛选、Search、feed | 以权威字段和公开性规则为准，不把 category 数量当新信息架构指标 |

“只读兼容层”不是冻结 Jekyll 本身；必要的安全、hidden 过滤或构建兼容修复仍可修改 category 模板，但不能改变旧文章语义或路由。

### 4. categories 退役没有预定日期

本轮不删除 category front matter、`/categories/`、`jekyll-archives` category 输出或文章详情链接。低使用量、视觉简化或新 taxonomy 已上线，都不足以证明旧分类“无必要”。

未来若提出退役，必须作为独立任务同时满足：

1. 有一段有代表性的真实使用/引用证据，能区分站内点击、外部链接、搜索入口与无人访问，且不公开个人分析数据。
2. 枚举当前 15 个名称及所有实际生成的 `/categories/:name/` 路由，而不是按猜测批量 slugify。
3. 对每个旧路由选择原地保留、永久重定向到最接近的 THINK/Topic/Series/Tag 页面，或说明为什么不能安全映射；禁止把所有 category 机械重定向到一个首页。
4. 先删除站内引用，再处理归档生成；文章正文、文件名、date、slug、permalink 与权威 taxonomy 不得随之改写。
5. T01 全量保护、SEO/断链门禁、Search/feed、sitemap、文章页和真实部署全部通过；提供明确回滚提交。
6. 另写 superseding ADR。没有该 ADR 时，本文件继续有效。

## Consequences

### Positive

- 避免为已满足的需求引入大规模迁移风险。
- 保留已验证的构建、路由、主题、SEO 和应用边界。
- 新内容只维护一套权威语义，同时不破坏历史链接。
- 将“何时迁移”和“何时删旧分类”变为可验证条件，而非主观时间表。

### Trade-offs

- 仓库暂时同时存在 canonical taxonomy 与 legacy categories，作者和维护者需要理解两者职责不同。
- `/categories/` 及文章详情仍会显示历史词汇；它们不是新信息架构的推荐入口。
- 保留 `jekyll-archives` category 输出会增加少量生成页面和维护面。
- 当前平台继续承担 Ruby/Jekyll 依赖升级与 GitHub Actions 维护成本。

### Operational rules

- T36 作者指南必须把 `categories` 标为可选兼容字段，并优先说明 Type/Topic/Series/Tags。
- 后续测试不得重新引入 category → Series/Topic/Type 的推断。
- 任何 category 改名或删除都视为 URL 兼容变更，必须走与旧 tag/route 相同的映射、SEO 和构建验证。
- 架构复审只在上述触发器有证据时进行；常规依赖升级不需要推翻本 ADR。

## Rejected alternatives

### 立即迁移到应用框架

拒绝。当前没有已批准的服务端/账户/CMS 需求，也没有持续构建或客户端架构证据证明迁移收益大于已验证系统的替换风险。

### 立即删除全部 categories

拒绝。旧 category 路由仍由站点生成并在文章详情中引用；直接删除会改变既有 URL 和发现路径，且没有逐路由兼容映射或真实使用证据。

### 让 categories 继续作为新内容的必填分类

拒绝。这会维持两套权威分类，并可能再次出现 category 推断 Series/Topic 的歧义。新内容以 Type/Topic/Series/Tags 为准。

## Verification references

- `NEUTRIVERSE_CONTENT_RESTRUCTURE_PLAN.md` sections 18–23 and Q8
- `docs/neutriverse-route-visibility-map.md`
- `docs/neutriverse-restructure-baseline.json`
- `docs/content-taxonomy-migration.md`
- `docs/content-taxonomy-final-report.md`
- `_config.yml` (`jekyll-archives` category permalink)
- `_layouts/categories.html`, `_layouts/category.html`, `_layouts/post.html`
- `.github/workflows/pages-deploy.yml`

This ADR may only be replaced by a later ADR that cites the triggering evidence, compatibility plan and validation results.
