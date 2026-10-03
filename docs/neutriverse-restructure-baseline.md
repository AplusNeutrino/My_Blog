# Neutriverse 重构保护基线（T01）

源快照：`97281227aaafe176870b28bc8a352a0e536e29d6`。本文件与 JSON 只用于重构验证，不是公开导航或新增作者资料。

## 交付与覆盖

- `neutriverse-restructure-baseline.json`：44 篇文章的原文件 SHA-256、LF 正文 SHA-256、date/slug/permalink、源推导 URL、Type/Topic/Series/Tags、hidden/published；5 条 Fragment 的原文 SHA-256 和日期；14 个实际页面来源；布局、插件、配置、导航、主题、应用脚本和集成文件哈希。
- `../tools/content_restructure_baseline.py`：只读生成/核对脚本，依赖 Python 3 + PyYAML。输出已存在时拒绝覆盖，防止验证时把原始基线刷新掉。
- 正文哈希仅归一化 BOM/换行；不删除末尾换行或其他空白。Fragments 保存文本哈希而不是复制个人原文。
- 本轮源码盘点已核对所有保护源文件与原始 SHA 一致；文档更新不会改写基线。

## 当前写作统计

| 范围 | 数量 |
|---|---:|
| 全部文章 | 44 |
| `hidden: true` 文章 | 5 |
| 非 hidden 文章 | 39 |
| Fragments | 5 |
| 全写作 | 49 |
| Essay / Note / Fragment | 5 / 39 / 5 |
| Computation / Humanity / Otaku / Arts | 38 / 6 / 4 / 1 |
| 文章独立 Tags / 全写作独立 Tags | 151 / 157 |

这是全源统计，不能直接作为公开目录计数；公开结果必须按 hidden、published 和实际发布日期规则计算。上一轮 final report 的 humanity=7 / arts=0 与当前实际源不一致，交由 T02 修正。

## 页面与可见性

| 源对象 | 源路径契约 | 当前发现性 / 后续保护 |
|---|---|---|
| 根首页 | `/` | 保留；当前 home 模板仍依赖旧 categories |
| About / Library / 友链 | `/about/`、`/library/`、`/links/` | `_tabs` 来源；按确认决定归 ABOUT，不改原数据/友链 |
| 检索页 | `/categories/`、`/tags/`、`/archives/` | 旧入口保留；样式隐藏部分导航不代表页面私有 |
| Thoughts | `/thoughts/` | 唯一源 `_tabs/thoughts.md` 的 5 条对象；保护文本/日期 |
| 文章 | `/posts/:title/` | 源文件 slug/date/permalink 保留；JSON 保存逐篇候选路径 |
| Ravenis | `/ravenis/` | `sitemap:false`、robots 字段及 metadata-hook 的 noindex；未来可由 OBSERVE 发现，继续 noindex |
| Occult Atlas | `/occult-atlas/` | hidden_pages 集合、默认 sitemap:false；专用布局明确 noindex |
| Atlas 原应用入口 | `/occult-atlas-app/` | HTML robots noindex，配置排除 sitemap；不得破坏既有兼容入口 |
| NAVI | `/navi/` | hidden_pages、sitemap:false、未列公开导航；源未发现专用 robots 输出，不把 sitemap 排除当 noindex |
| Gate | `/gate/` | 专用布局 noindex；front matter 未排除 sitemap，留给 T33 一致性核查；不加入主导航 |
| FitzSight 现有界面 | `/projfitzgerald/` | 独立 layout:null 页面；原数据来源和应用功能受保护 |

**路径证据层级：**显式 permalink 为源契约；文章默认路径按配置与文件 slug 推导，JSON 均标记 `runtime_url_verified:false`。未将 Jekyll slugify 生成的 Category/Tag 详情路径当成已运行验证的完整 URL 清单；T05/T33 必须从生成产物核对 slug/编码/兼容链接。这里的源路径不是声称线上逐链通过。

## 已有集成契约

| 集成 | 关键来源 | 保护内容 |
|---|---|---|
| 主题与侧栏 | `_includes/poe-night-mode.html`、`metadata-hook.html`、Night/Prospero CSS | 保存主题、侧栏状态；不要改变存储键导致状态丢失 |
| 评论 / 点赞 / 统计 | `_config.yml`、`_includes/post-like.html`、`footer.html` | Twikoo 配置、统计/点赞 endpoint 契约、失败降级；本次不读密钥或改服务端 |
| 大图书馆 | `_plugins/prospero_great_library.rb`、`_includes/pgl/`、`assets/pgl/`、PGL 工作流 | 隐私过滤、关联、导出、02:17 同步及生成数据；每日更新不是正文变化 |
| Ravenis | `tools/fetch_ravenis_release.py`、Pages workflow、`ravenis/index.html` | 远端验证/最后可用数据、manifest/选中日加载、错误降级 |
| Atlas | 专用 layout、`occult-atlas-app/` | 主题控制器、图表/输入/原跳转；不改业务计算 |
| Gate | `_data/gate.yml`、`assets/js/gate.js`、Gate layout | localStorage/sessionStorage、导入/导出/快照、偏好和书签；不公开个人配置 |
| 旅行地球 | `_tabs/about.md`、travel-globe 脚本与数据 | 地图/tooltip/降级、已有来源；不增添位置或个人事实 |
| FitzSight | `projfitzgerald/`、`docs/PROJFITZGERALD_PROGRESS.md` | 单一进度源及原界面，后续 BUILD 仅关联 |
| 搜索 / 归档 / 标签 / Series | `assets/js/data/search.json`、对应 layouts/includes | hidden 过滤一致性及旧路径 |

## 已发现缺口（记录，不在本次改行为）

1. 显式 Series 分支没有 hidden 过滤；无 series 文章仍回退旧 categories（T03）。
2. Tags 主目录使用全部 `site.tags`，未过滤 hidden-only 标签/数量（T05/T17/T33）。
3. Search JSON 和 Archives 已显式过滤 hidden；不能因此假定主题自带 feed、sitemap 和 tag 详情也过滤（T32/T33）。
4. NAVI robots 未被源明确覆盖，Gate sitemap 未在 front matter 排除；需核对生成 HTML 而非机械套用默认（T33）。
5. 基础主题部分 include 来自 gem，当前源码未覆盖；生成页面/资源行为必须在 CI 产物或可用 Jekyll 环境检查。

## 实际验证

- 原快照 Build and Deploy：run [37132489511](https://github.com/AplusNeutrino/My_Blog/actions/runs/37132489511)，head `97281227aaafe176870b28bc8a352a0e536e29d6`，API 返回 completed/success。这是源基线的历史构建证据，不代表后续实现已构建。
- 本次本地 `python -m unittest discover -s tests -v`：27 项通过（包含 Ravenis 的 fixture/LKG 检查；不等于访问真实 R2 成功）。
- 基线脚本生成/核对：44 篇 + 5 Fragment 覆盖；原正文/URL 元数据/hidden/published 核对无差异；实际源与原 SHA 的 `git diff --quiet` 通过。
- 当前执行环境 `ruby --version` 返回未找到，未跑本地 Jekyll build。
- 线上 sitemap 请求返回 HTTP 403；未完成线上路径抓取，不声称线上 UI/URL/robots 已验证。后续可在 GitHub 构建产物或授权浏览器中继续，当前不影响 T02/T06 的源盘点工作。

## 后续核对命令

从仓库根目录运行；使用新的临时输出路径，不覆盖原基线：

```powershell
python -m pip install PyYAML
python tools/content_restructure_baseline.py --check-against docs/neutriverse-restructure-baseline.json --output "$env:TEMP/neutriverse-check.json"
python -m unittest discover -s tests -v
```

同名临时输出已存在时换新名字。脚本允许新增文章/Fragments，保护原记录；本轮不授权修改原记录的 hidden/published。工具不能替代实际 Jekyll URL、视觉和最终部署验收。集成文件哈希用于解释变化，不要求未来布局文件永久不变。
