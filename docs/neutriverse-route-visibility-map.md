# Neutriverse 页面归属、路由与可见性映射

> 状态：T06 authoritative implementation contract  
> 基线：`02a1e0c4ac709ac36b4303acc6b02957b876db68`  
> 依据：`NEUTRIVERSE_CONTENT_RESTRUCTURE_PLAN.md` 第 18–24 节、`docs/neutriverse-restructure-baseline.json`、Q3/Q4/Q5/Q8 已确认决定  
> 边界：本文件记录当前事实与目标契约；T06 不改变线上路由、导航、索引或页面内容。

## 1. 如何读取可见性

以下维度必须分别判断，不能互相替代：

| 维度 | 含义 | 不代表 |
|---|---|---|
| 可直达 | 知道 URL 时可以打开 | 有公开入口、可被搜索引擎收录或需要身份验证 |
| 公开发现 | 首页、主导航、四入口目录或明确的公开关联中有链接 | 允许搜索引擎收录 |
| 隐蔽发现 | 只经 Gate、Probe、彩蛋或已有深层链接到达 | 私密或受访问控制 |
| `noindex` | 页面向支持该指令的爬虫请求不进入索引 | 隐藏、鉴权或 URL 不可传播 |
| `sitemap: false` | Jekyll sitemap 不主动列出页面 | `noindex` 或禁止爬取 |
| `robots.txt Disallow` | 请求爬虫不要抓取路径 | `noindex`；被禁止抓取时爬虫可能无法读取页面内的 `noindex` |
| `hidden: true` / `hidden_pages` | 站内聚合或集合层面的内容规则 | 自动生成 `noindex` |

公开目录中的 `noindex` 页面是允许的：Q3 明确要求 Ravenis 与 Occult Atlas 在 OBSERVE 可发现，同时保留 `noindex`。所有私人配置仍不得进入生成 HTML、公开数据或仓库新增文件；本文件没有授予公开隐藏内容的权限。

## 2. 顶层信息架构与导航契约

| 入口 | 中文说明 | canonical | 公开发现 | 收录目标 | 内容边界 |
|---|---|---|---|---|---|
| THINK | 我如何思考与表达 | `/think/`（新增） | 主导航、首页 | index | 文章、Fragments、Type/Topic/Series/Tags 入口；Archive 仍只统计写作 |
| BUILD | 我正在制作什么 | `/build/`（新增） | 主导航、首页 | index | 仅 Q5 名单；项目详情与实际应用入口分开 |
| OBSERVE | 我持续观察什么 | `/observe/`（新增） | 主导航、首页 | index | 公开列出 Ravenis、Occult Atlas；两者的应用页仍 `noindex` |
| ABOUT | 我是谁以及这个站如何生长 | `/about/`（保留） | 主导航、首页 | index | 作者/网站资料、Currently、时间线；关联 Library、友链、旅行地球 |

主导航第一层只使用这四个英文入口，并带中文说明。Search、Tags、Archive、RSS、社交链接和主题切换是辅助入口，不与四入口争夺同一层级。Night 与 Prospero Light 使用同一套信息架构。

## 3. 当前页面源全量映射

本表覆盖 T01 基线中的 14 个页面源。`当前发现性` 描述 base SHA 的真实实现；`目标契约` 是后续任务的唯一默认方向。

| 页面源 | 当前 URL | 当前归属 / 发现性 / 索引 | 目标契约 | 路由与保护措施 |
|---|---|---|---|---|
| `index.html` | `/` | 首页；公开；可索引 | 首页继续作为四入口、近期表达与 Current Signal 的汇合点 | URL 原地保留；不得推荐 hidden 内容 |
| `_tabs/about.md` | `/about/` | 公开 tab；可索引；内嵌旅行地球 | ABOUT canonical | URL 原地保留；ABOUT 文案只使用站内事实；旅行数据不扩写 |
| `_tabs/archives.md` | `/archives/` | 输出为 tab，但 Night CSS 隐藏该侧栏项；可直达、可索引 | THINK 的辅助写作时间线 | URL 原地保留；只纳入文章/Fragments 的策略在 T17 固化，不混入项目时间线 |
| `_tabs/categories.md` | `/categories/` | 输出为 tab但侧栏隐藏；可直达、可索引 | 旧分类兼容目录 | URL 和 category 详情原地保留；不作为新 Topic 主导航 |
| `_tabs/tags.md` | `/tags/` | 输出为 tab但侧栏隐藏；可直达、可索引 | THINK 辅助检索 | URL 原地保留；公开列表/详情不得泄露 hidden 条目 |
| `_tabs/thoughts.md` | `/thoughts/` | 输出为 tab但侧栏隐藏；可直达、可索引；五条 Fragment 唯一来源 | THINK / Fragments canonical 内容源 | URL 原地保留并由 `/think/` 链接；不复制文本；后续增加稳定锚点 |
| `_tabs/library.md` | `/library/` | 公开 tab；可索引；PGL 数据/同步/隐私逻辑 | ABOUT 关联的独立 Library 页面 | URL 原地保留；只调整入口层级，不改 PGL 同步、隐私过滤、关联或数据源 |
| `_tabs/links.md` | `/links/` | 公开 tab；可索引 | ABOUT 关联的友情链接页面 | URL 和友链关系原地保留；后续从 ABOUT 提供清晰入口 |
| `gate/index.md` | `/gate/` | 可直达并从部分工具互链；非 tab；layout 输出 `noindex,nofollow`；当前未显式 `sitemap: false` | BUILD 中可介绍 Gate 项目，但实际 Gate 入口维持隐蔽 | 应用 URL 原地保留；不得加入主导航/首页公共工具入口；补齐 sitemap 排除交 T33 |
| `_hidden_pages/navi.md` | `/navi/` | hidden collection；Probe 可发现；`sitemap: false`；当前没有显式 `noindex` | 私人工具，维持隐蔽发现 | URL 原地保留；不得进入四入口/公开搜索/feed；补齐 `noindex` 交 T33；不公开 `_data/private_navigation.yml` 之外的任何配置 |
| `_hidden_pages/occult-atlas.md` | `/occult-atlas/` | hidden collection；全局底栏星图入口、Gate、Probe 可达；layout `noindex,nofollow`；`sitemap: false` | OBSERVE 公开目录项，同时是 BUILD 项目关联的实际使用入口 | URL、状态与主题原地保留；公开描述不等于允许索引 |
| `occult-atlas-app/index.html` | `/occult-atlas-app/` | noindex 兼容跳转到 `/occult-atlas/`；配置默认 `sitemap: false` | 仅兼容旧入口 | 永久保留可用跳转；canonical 指向 `/occult-atlas/`；不作为目录卡片目标 |
| `ravenis/index.html` | `/ravenis/` | 非 tab；Gate/Probe 可达；`noindex,nofollow`、`sitemap: false`；`robots.txt` 当前 Disallow | OBSERVE 公开目录项，同时是 BUILD 项目关联的实际使用入口 | URL 和数据流程原地保留；仍 `noindex`；T33 应消除 Disallow 与页面 noindex 的语义冲突但不得改为 index |
| `projfitzgerald/index.html` | `/projfitzgerald/` | 独立进度工具；可直达；无显式 noindex/sitemap 排除 | FitzSight BUILD 项目的实际进度/工具入口 | URL、`docs/PROJFITZGERALD_PROGRESS.md` 数据契约和功能原地保留；项目详情使用独立 stable ID |

## 4. 动态、生成与兼容路由

| 路由族 | 当前来源 | 目标归属 | 契约 |
|---|---|---|---|
| `/posts/:title/` | 44 篇 `_posts`，Jekyll permalink | THINK 详情 | 全部旧 URL、文件名、date/slug/permalink、正文和附件链接受保护 |
| `/categories/:name/` | `jekyll-archives` | THINK 旧分类兼容 | 保留；只列公开文章；不自动映射成 Topic |
| `/tags/:name/` | `jekyll-archives` | THINK Tags | 保留；公开详情过滤 hidden；新标签改名必须另有兼容策略 |
| `/tags/bus/` | T05 兼容页 | 兼容 | `noindex` + `sitemap: false` → `/tags/system-bus/` |
| `/tags/changelog/` | T05 兼容页 | 兼容 | `noindex` + `sitemap: false` → `/tags/neutriverse/` |
| `/feed.xml` | Chirpy/Jekyll feed | THINK 订阅 | 保留；T32 明确 Fragment 与 hidden 输出策略 |
| `/assets/js/data/search.json` 与主题搜索面 | Chirpy search | THINK 辅助检索 | 保留；T17/T32 排除 hidden，四入口页面是否入站内搜索由 T32 统一决定 |
| `/sitemap.xml` | Jekyll sitemap | 技术设施 | 保留；遵守每页 sitemap 契约；T33 核对实际产物 |
| `/robots.txt` | `assets/robots.txt` | 技术设施 | 保留；T33 对齐 Ravenis/noindex，不把 robots 当访问控制 |
| 新 `/think/`、`/build/`、`/observe/` | T08 起新增 | 四入口 | 新 canonical；无旧路由替换关系，不重定向旧 tabs/应用路径 |
| 新 `/build/<stable-id>/` | T21 起新增 | BUILD 详情 | 项目事实页；与应用/工具 URL 并存，卡片明确区分“了解项目”和“打开工具” |

## 5. 特殊模块与非独立路由

| 模块 / 来源 | 所在位置 | 归属 | 发现性与保护契约 |
|---|---|---|---|
| 旅行地球：`_tabs/about.md` + `_data/travel_regions.yml` | `/about/` 内嵌 | ABOUT | 保留现有能力、来源标注与移动降级；不新增地点或个人轨迹 |
| 友链：`_includes/friend-nodes.html` + `_data/friends.yml` | `/links/` | ABOUT | 保留原关系与 URL；ABOUT 只建立关联，不复制数据 |
| Prospero Great Library | `/library/` 与文章关联卡 | ABOUT | 保留独立页面、懒加载、同步、隐私和文章关联；不并入写作 Archive |
| Probe Tracking Module | 默认 layout 的隐藏交互 | 隐蔽设施 | 保留彩蛋触发与 hidden 聚合边界；不得变成公开菜单或将 hidden 项送入公开 Search/feed |
| Gate | `/gate/` 独立 layout / data / JS | 隐蔽工具 + BUILD 项目关联 | BUILD 可介绍项目，但不得把工具入口提升到主导航或首页公共入口 |
| NAVI | `/navi/` + `_data/private_navigation.yml` | 隐蔽工具 | 维持原 URL 和隐蔽发现；数据文件只允许公开、无凭证的链接 |
| Ravenis 数据界面 | `/ravenis/` + `assets/js/ravenis.js` | OBSERVE 使用入口 + BUILD 关联 | OBSERVE 公开卡片可直接到达；页面仍 noindex；发布数据流程受保护 |
| Occult Atlas 工作台 | `/occult-atlas/` + app assets/API config | OBSERVE 使用入口 + BUILD 关联 | OBSERVE 公开卡片可直接到达；页面仍 noindex；旧 app 跳转、浏览器状态、主题受保护 |
| Project Fitzgerald / FinSight tracker | `/projfitzgerald/` | FitzSight BUILD 关联工具 | 继续读取站内 progress 文档；不改关联项目仓库 |
| Night / Prospero Light、主题切换 | 全站共享 | 横切能力 | 四入口、旧页与特殊模块均保持两主题可用；不建立主题专属路由 |
| 评论、点赞、RSS、社交与站内搜索 | 文章/全站辅助层 | 横切能力 | 保留端点和回退；不提升为顶层信息架构，不泄露 hidden 内容 |

## 6. BUILD 项目实体和实际入口

Q5 名单只定义 BUILD 第一版实体；不存在的事实不得补写。Ravenis 与 Occult Atlas 同时出现在 BUILD 和 OBSERVE 是有意的：BUILD 解释“制作了什么”，OBSERVE 提供“进入观察界面”。

| stable ID（T21 最终固化） | 展示名 | 已有站内依据 / 实际入口 | BUILD 契约 |
|---|---|---|---|
| `fitzsight` | FitzSight | `/projfitzgerald/`、站内进度文档 | 新详情关联现有 tracker，不替换旧 URL |
| `akasha-notes` | Akasha Notes | 现有相关文章 | 新详情引用文章；未知仓库/Release 不编造 |
| `toyosatomimis-headphone` | Toyosatomimi's Headphone | 现有相关文章 | 新详情引用文章；未知仓库/Release 不编造 |
| `ravenis` | Ravenis | `/ravenis/` | BUILD 详情关联 noindex 使用入口；同时列于 OBSERVE |
| `occult-atlas` | Occult Atlas | `/occult-atlas/`、`/occult-atlas-app/` | BUILD 详情关联 canonical 使用入口；同时列于 OBSERVE |
| `gate` | Gate | `/gate/`、站内 roadmap | 可有公开项目介绍，实际工具入口仍隐蔽 |
| `officespire` | OfficeSpire | 待 T21–T24 只读核对公开/站内来源 | 只写可追溯事实；不修改关联仓库 |

`MMXProj` 明确排除，不生成项目实体、卡片、详情页或间接推荐。

## 7. 聚合边界

| 聚合面 | 可以进入 | 必须排除 |
|---|---|---|
| 首页近期表达 / THINK | 非 hidden 文章；按 T15 决定接入的五条 Fragment | hidden posts、NAVI、Gate 私人工具数据、观察应用内部数据 |
| Tags / Categories / Series / Archive | 非 hidden 写作内容 | hidden posts；BUILD/OBSERVE/ABOUT 事件不得混入写作 Archive |
| BUILD | Q5 七个实体和经核实的关联文章 | MMXProj、未知 Release/状态、聊天记忆推断 |
| OBSERVE | Ravenis、Occult Atlas | 其他 hidden pages、NAVI、Gate；除非用户另行授权 |
| ABOUT | 站内已有作者/网站事实及 Currently；Library、友链、旅行关系 | 私人信息、未确认实时状态、新增地点、账号凭证 |
| Search / feed / sitemap | 各任务明确允许的公开内容 | hidden 内容、NAVI、noindex 应用页和兼容 stub（按各自契约） |

## 8. 实施顺序与验收归属

- T07 定义共享主题/组件契约，不改变本路由表。
- T08–T10 建立四入口及主/辅导航；旧 URL 同时保持可达。
- T11–T17 实现 THINK 聚合，并统一检查 hidden 过滤。
- T21–T26 使用 stable project ID 实现 BUILD/OBSERVE；OBSERVE 公开发现不取消应用 noindex。
- T27–T29 重组 ABOUT，仅移动入口关系，不复制 Library/友链/旅行数据源。
- T32 统一 Search/feed 输出；T33 核对 canonical、sitemap、noindex、robots 和全部旧链接。
- T37 以 T01 基线验证正文、Fragment 文本、页面源和旧 URL；T38 在线端到端验证实际发现路径。

任何后续实现若要删除、改名或重定向本文件标为“原地保留”的 URL，必须先回写主计划并说明兼容依据。`noindex`、sitemap 排除或隐蔽发现的放宽属于产品边界变更，不能从“页面可直达”自行推导。
