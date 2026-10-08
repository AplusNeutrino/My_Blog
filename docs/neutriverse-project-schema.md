# Neutriverse Project Catalog Schema

T21 建立项目实体的单一来源：`_data/neutriverse_projects.yml`。该文件名虽为 `.yml`，内容使用 JSON 语法；JSON 是 YAML 1.2 的子集，Jekyll 与回归测试可读取同一份数据，不再维护第二份项目清单。

## 字段

| 字段 | 必填 | 含义 |
|---|---:|---|
| `id` | 是 | 发布后稳定、全站唯一的小写 kebab-case 项目标识 |
| `name` | 是 | 公开项目名 |
| `detail_url` | 否 | 只有真实详情页已生成时填写；BUILD 卡片优先进入该页 |
| `summary` | 是 | 仅由已记录来源支持的简述 |
| `contexts` | 是 | 项目出现的概念入口；本轮仅 `build`，或已批准的 `build + observe` |
| `visibility` | 是 | `listed`、`listed_noindex` 或 `unlisted_noindex` |
| `status` | 否 | 只有来源明确、措辞精确时才填写；未知即省略 |
| `links.application/repository/documentation` | 否 | 只有真实可达且适合公开的入口才填写 |
| `related_posts` | 否 | 现有文章与项目的次级 Project Log 关系，不改变文章 Type |
| `releases` | 否 | 只有可核实 Release 数据时才出现；项目不因缺少 Release 而不合法 |
| `sources` | 是 | 支持公开事实的站内路径或公开外部 URL；不是展示文案的第二份副本 |

`_layouts/neutriverse-project.html` 只通过 `page.project_id` 查找 catalog。status、links、related_posts 和 releases 都按真实数据渲染；未知状态明确说明“未记录”，而不是推断 active/complete/paused。T23 已为 FitzSight、Akasha Notes、Toyosatomimi's Headphone 建立 `detail_url`；T24 又为 Ravenis、Occult Atlas、Gate、OfficeSpire 建立同类入口，因此七个 catalog 实体现在都由唯一 `/build/<stable-id>/` 事实页承接。

## 固定项目与来源

| Stable ID | 项目 | 依据 | 可见性说明 |
|---|---|---|---|
| `fitzsight` | FitzSight | `docs/PROJFITZGERALD_PROGRESS.md`、`projfitzgerald/index.html` | BUILD listed |
| `akasha-notes` | Akasha Notes | `_posts/2026-06-30-阿卡夏便笺akashanotes.md` | BUILD listed；文章仍是 Note + Project Log 关系 |
| `toyosatomimis-headphone` | Toyosatomimi's Headphone | `_posts/2026-07-09-丰聪耳机toyosatomimisheadphone.md` | BUILD listed；文章仍是 Note + Project Log 关系 |
| `ravenis` | Ravenis | `ravenis/index.html` | BUILD + OBSERVE listed；应用继续 noindex,nofollow |
| `occult-atlas` | Occult Atlas | `_hidden_pages/occult-atlas.md` | BUILD + OBSERVE listed；应用继续 noindex |
| `gate` | Gate | `README_GATE.md`、`gate/index.md`、`GATE_ROADMAP.md` | catalog 可建实体，但工具入口仍 unlisted/noindex，catalog 不公开链接它 |
| `officespire` | OfficeSpire | [公开仓库 README](https://github.com/AplusNeutrino/OfficeSpire/blob/main/README.md) | BUILD listed；状态严格记录为 `implemented_unverified` |

MMXProj 不在本轮 catalog。T21 没有添加任何 `releases` 字段；现有发布文章或仓库链接不被重新包装为未经核实的项目 Release。关联项目仓库均未修改。

## T24 余下详情与可见性

- Ravenis 与 Occult Atlas 的项目事实页分别链接既有 `/ravenis/`、`/occult-atlas/` 应用；事实页和应用页都继续 noindex，旧应用 URL 不变。
- Gate 的事实页可从 BUILD 了解项目，但 catalog 仍不提供 `/gate/` 动作；详情页 noindex，不公开 NAVI 或浏览器本地配置。
- OfficeSpire 详情仅链接公开仓库与 README，保留来源明确的 `implemented_unverified`。README 明示 M9 不是已发布 Release，因此 catalog 仍不添加 `releases`。
- 四项当前都没有站内 Project Log 记录；模板显示自然空状态，不借用聊天记忆或把开发文档伪装成文章。
