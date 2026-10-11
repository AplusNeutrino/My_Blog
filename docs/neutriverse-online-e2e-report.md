# Neutriverse T38 线上端到端验收报告

> 状态：T38 已完成；精确 head CI、Pages 部署与部署后复核均通过。
> 验收日期：2026-10-11（Asia/Shanghai）
> 线上站点：https://neutriverse.uk/
> T38 scope base：`8d098915034234cd2f5d622237e5022cbaf2a42a`
> scope commit：`ae95601613192789b6eea59a9190b60419a91f24`
> final implementation head：`8bdff68e54fd14bdaad559da790b62289864d3f3`

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

线上逐页读取浏览器标题时发现：ABOUT、Library、Thoughts、Categories、Tags、Archives、Links 的可见 H1 正确，但浏览器标题均退化为 `| 中间层`。根因是 Chirpy 7.6 的 `_includes/head.html` 对 tabs 只执行 locale lookup，没有页面正文模板已有的 `default: page.title` 回退。

首版 locale alias 与标识符尝试均被新增的 production SEO 门禁真实拦截，没有通过放宽检查掩盖缺陷。最终修复在仓库内覆盖同版本 head，只为该 lookup 加上 `| default: page.title`；七个 tab 原有中文标题与可见 H1 保持不变。标准库契约测试固定 fallback，`tools/check_seo_routes.py` 则直接读取 production 构建 HTML，任何必需 tab 的 title 为空或以 `|` 开头都会失败。

## 4. 移动端、可访问性与 source/build 证据边界

本次云浏览器固定为 1363 × 936，不能把截窄截图冒充 390px 布局。因此 390px 侧栏打开/关闭、焦点、触控目标、横向溢出，以及 768/1024/1366px、双主题、reduced-motion 的机械证据由同一精确实现 head 的 production CI 浏览器矩阵承担；部署后线上复核负责真实路由、交互状态与最终标题。

## 5. 内容与权限边界

本次没有改动任何 `_posts/`、Fragment、Project Log、项目 catalog、正文、front matter、文件名、date/slug/permalink、旧 URL、hidden/published/noindex 或外部项目仓库。修复只触及现有 tab 的本地化标题解析、构建门禁、契约测试与本报告。


## 6. 精确 head CI、部署与部署后复核

- 失败证据保留：run 38127191223 暴露测试正则转义错误；run 38127286837 在 197 tests 与 Jekyll 成功后由 SEO 门禁拦截空标题；run 38127446476 证明只调整 locale/front matter 仍不足。三次失败均未部署。
- 最终通过：[Actions run 38127605436](https://github.com/AplusNeutrino/My_Blog/actions/runs/38127605436)，head `8bdff68e54fd14bdaad559da790b62289864d3f3`，completed/success。
- build job `114435118603` 与 deploy job `114435385689` 均 success；197 tests、T01 protected baseline、authoring、production Jekyll、Search/Atom、SEO/旧路由、资源/集成、390px Chrome、40 项响应式/无障碍矩阵、Ravenis 与 artifact upload 全部通过。
- artifact：`11696999318`；digest：`sha256:f7357e0222b87c0002c375df5c909c231c02215f03b4660540a30a556a5c9941`。
- 部署后真实浏览器逐页结果：`/about/` = `中间层漫游指南 | 中间层`；`/archives/` = `中间层时间线 | 中间层`；`/categories/` = `中间文段索引 | 中间层`；`/library/` = `中间层大图书馆 | 中间层`；`/links/` = `中间层友情链接 | 中间层`；`/tags/` = `中间文段标签 | 中间层`；`/thoughts/` = `中间思维片段 | 中间层`。
