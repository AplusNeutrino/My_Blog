# Neutriverse T38 线上端到端验收报告

> 状态：实现已提交，等待精确 head CI、Pages 部署与部署后复核。
> 验收日期：2026-10-11（Asia/Shanghai）
> 线上站点：https://neutriverse.uk/
> T38 scope base：`8d098915034234cd2f5d622237e5022cbaf2a42a`
> scope commit：`ae95601613192789b6eea59a9190b60419a91f24`

本报告只记录真实可复核证据。标记为“线上浏览”的项目来自已部署站点；标记为“构建门禁”的项目来自本次精确实现 head 的 CI，二者不互相冒充。

## 1. 线上桌面浏览矩阵

浏览器固定视口为 1363 × 936、DPR 1。入口起点均为首页，并实际打开目标、代表详情，再使用浏览器返回或入口导航回到上层。

| 场景 | 线上结果 |
|---|---|
| 首页 | H1 为 NEUTRIVERSE；四个英文入口均有中文说明；Current Signal 为“Neutriverse 网站重构”；公开状态为 44 条表达、39 + 5 写作来源、7 个项目。 |
| THINK | 44 条公开记录；Fragment 筛选得到 5 条且刷新后保持；Fragment + Humanity 得到 4 条，后退/前进正确恢复；Computer Networks Series 得到 10 条；代表文章 `/posts/计网-10/` 可打开，正文、taxonomy 与 10/10 系列导航可读，返回后筛选状态仍为 10 条。 |
| Search | 从 THINK 的 Search 动作打开后焦点进入 `#search-input`；检索“哥德尔”返回唯一正确文章；取消后搜索层关闭。 |
| BUILD | 唯一项目 ID 恰为 FitzSight、Akasha Notes、Toyosatomimi's Headphone、Ravenis、Occult Atlas、Gate、OfficeSpire，共 7 项；页面无 MMXProj。Gate 详情只显示 BUILD 事实页与“当前没有适合公开的应用、仓库或文档入口”，没有隐藏工具链接。 |
| OBSERVE | 目录只列 Ravenis 与 Occult Atlas。Ravenis 实际进入公开日报，日期/时段/搜索/筛选/日报周报控件可见，robots 为 `noindex,nofollow`；应用导航可进入 Occult Atlas。Occult Atlas 星盘控制、刷新、查询与回到此刻控件可见，robots 为 `noindex, nofollow`。 |
| ABOUT | Currently 明确是网站维护状态；Library、友链均为公开普通链接；旅行显示“能力保留 · 当前未公开”，没有地点或隐藏工具入口。Library 实际打开并可返回 ABOUT。 |
| 双主题 | Prospero Light → Night 后 `data-mode=dark`，按钮提示切回昼；刷新保持。Night → Prospero Light 后 `data-mode=light`，按钮提示切回夜；刷新保持。 |

## 2. 旧路由与兼容层线上结果

| 请求 | 实际结果 |
|---|---|
| `/thoughts/` | 原地 5 条 Fragment；canonical 正确。 |
| `/categories/` | 原地 39 篇旧分类兼容目录；canonical 正确。 |
| `/tags/` | 原地标签目录；canonical 正确。 |
| `/archives/` | 原地 39 篇写作时间线；canonical 正确。 |
| `/tags/bus/` | 跳转到 `/tags/system-bus/`，2 篇公开记录，canonical 指向新路由。 |
| `/tags/changelog/` | 跳转到 `/tags/neutriverse/`，页面明确显示暂无公开记录，canonical 指向新路由。 |
| `/occult-atlas-app/` | 跳转到 `/occult-atlas/`；canonical 指向应用路由，继续 noindex。 |

## 3. 线上发现并修复的缺陷

在线上逐页读取浏览器标题时发现：ABOUT、Library、Thoughts、Categories、Tags、Archives 以及 Links 的 front matter 使用中文显示标题，而 Chirpy 7.6 的共享 head 对 tabs 先执行 `page.title | downcase`，再查 `site.data.locales[lang].tabs[tab_key]`，且没有回退。现网因此输出 `<title>| 中间层</title>`，虽然可见 H1 正确。

最小修复是在现有 `_data/locales/zh-CN.yml` 中为七个已存在的自定义 tab 标题增加同值 alias，不复制页面内容、不覆盖主题 head。新增契约测试逐一核对 front matter 与 alias；production `tools/check_seo_routes.py` 同时读取构建 HTML，任何必需 tab 的 title 为空或以 `|` 开头都会失败。部署后复核结果将在本文件与主计划补写。

## 4. 移动端、可访问性与 source/build 证据边界

本次云浏览器固定为 1363 × 936，不能把截窄截图冒充 390px 布局。因此 390px 侧栏打开/关闭、焦点、触控目标、横向溢出，以及 768/1024/1366px、双主题、reduced-motion 的机械证据由同一精确实现 head 的 production CI 浏览器矩阵承担；部署后线上复核负责真实路由、交互状态与最终标题。CI run、job、artifact、digest 和最终部署 head 在完成后写回。

## 5. 内容与权限边界

本次没有改动任何 `_posts/`、Fragment、Project Log、项目 catalog、正文、front matter、文件名、date/slug/permalink、旧 URL、hidden/published/noindex 或外部项目仓库。修复只触及现有 tab 的本地化标题解析、构建门禁、契约测试与本报告。
