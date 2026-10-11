# Neutriverse T37 保护基线与完整回归验收

本文件记录 T37 的验收口径和可重复检查，不替代 T01 原始基线，也不授权刷新它。最终实现 SHA、Actions、artifact 与部署证据写回根目录主计划和 `docs/neutriverse-restructure-execution-log.md`。

## 1. 权威输入

- 冻结基线：`docs/neutriverse-restructure-baseline.json`，来源为 T01 的 `97281227aaafe176870b28bc8a352a0e536e29d6`。
- 只读对照器：`tools/content_restructure_baseline.py`。验证时输出到临时路径；不得把当前状态覆盖成新基线。
- 内容结构：`_posts/` 与 `_tabs/thoughts.md`。
- 构建 URL 门禁：`tools/check_seo_routes.py`；它在 production Jekyll 产物中核对 T01 文章与页面来源、canonical、sitemap、兼容跳转和站内链接。
- 新内容门禁：`tools/check_authoring.py`；它不替代历史内容保护。

## 2. 当前全量对照结果

| 项目 | T01 | T37 对照 | 结果 |
|---|---:|---:|---|
| 原文章文件 | 44 | 44 | 全部存在，没有重命名或删除 |
| 原 Fragment | 5 | 5 | 原 text/date 全部存在 |
| hidden 文章 | 5 | 5 | 逐篇布尔值一致 |
| Essay / Note / Fragment | 5 / 39 / 5 | 5 / 39 / 5 | 一致 |
| Computation / Humanity / Otaku / Arts | 38 / 6 / 4 / 1 | 38 / 6 / 4 / 1 | 一致 |

对 44 篇原文章逐篇比较后，以下字段没有差异：

- 正文 LF 归一化 SHA-256 与字节数；
- `date`、`slug`、`permalink`；
- 从源推导的文章 URL 候选；
- `hidden` 与 `published`；
- `title`、Type、Topic、Series、categories、sitemap 与 robots。

5 条原 Fragment 的 text SHA-256、date、Type、Topic、Tags 与 hidden 逐项一致。T01 基线对照器返回 `passed: true`、`errors: []`。

## 3. 唯一有依据的文章源差异

原始文件整体哈希只有两篇变化，且差异仅为 T05 已授权、已审计的 Tags metadata；正文与全部保护字段不变：

| 文件 | T01 Tags | 当前 Tags | 依据 |
|---|---|---|---|
| `_posts/2025-05-07-计组-06.md` | `Bus, I/O, DMA, Interrupts` | `System Bus, I/O, DMA, Interrupts` | T05 `Bus → System Bus` 合并，旧 `/tags/bus/` 保留兼容 |
| `_posts/2026-05-24-neutriverse-site-changelog.md` | `Neutriverse, Changelog, Jekyll` | `Neutriverse, Jekyll` | T05 退役 `Changelog`，旧 `/tags/changelog/` 保留兼容 |

`tests/test_restructure_acceptance.py` 将这两个文件和准确的前后 Tags 固定为唯一例外；出现第三个整体哈希差异、不同字段差异或例外内容漂移都会失败。

## 4. URL 与可见性证据边界

源基线负责证明原文章文件、保护 URL metadata 和候选 URL 未变。T33 的 production-build 门禁负责证明实际生成结果：44 篇基线文章、14 个基线页面来源、公开入口、canonical、sitemap、noindex、兼容跳转和站内链接。这样不会把源路径推导冒充 Jekyll 运行时结果。

T33 对 Gate、NAVI、Ravenis 与 Occult Atlas 做过的 noindex/sitemap/canonical 收敛是有记录的可见性修复，不是公开隐藏内容。T32 Search/feed 与 THINK、Tags、Archive、Series 的回归继续证明 5 篇 hidden 文章不进入公开聚合。

## 5. 永久门禁与完整回归

production workflow 在 Jekyll build 前依次执行：

1. 全部 Python 回归；
2. T01 protected baseline 对照；
3. T36 authoring source 校验；
4. production Jekyll build；
5. Search/Atom、SEO/旧路由、资源/集成、390px 手机导航、四视口×双主题响应式/无障碍检查；
6. Ravenis 验证、artifact 上传与 Pages 部署。

基线步骤显式安装 PyYAML，输出到 `${{ runner.temp }}`，不会修改仓库中的冻结 JSON。后续 T38–T39 若触碰受保护内容，同一 workflow 会在构建前失败。

本验收不声称已经完成线上端到端浏览；首页到四入口、详情、返回、筛选、主题、手机和旧链的线上交互属于 T38。

## 6. 本地复核

```powershell
$check = Join-Path $env:TEMP ("neutriverse-current-" + [guid]::NewGuid() + ".json")
python tools/content_restructure_baseline.py --output $check --check-against docs/neutriverse-restructure-baseline.json
python tools/check_authoring.py
python -m unittest discover -s tests -v
bundle exec jekyll build -d _site
python tools/check_search_feed.py _site
python tools/check_seo_routes.py _site
python tools/check_performance_integrations.py _site
python tools/check_mobile_sidebar.py _site
python tools/check_responsive_accessibility.py _site
```
