# Neutriverse 作者操作指南

本指南是新增写作项和维护项目目录的操作入口。内容模型以 `_data/content_taxonomy.yml`、`docs/neutriverse-project-schema.md` 与 `docs/adr/0001-retain-jekyll-and-legacy-categories.md` 为准；本指南不授权重写旧文章、公开隐藏内容或添加未经来源支持的项目事实。

## 1. 开始前

1. 从最新 `main` 创建工作分支或干净工作树。
2. 选择唯一内容类型：长短文章写入 `_posts/`，短句 Fragment 写入 `_tabs/thoughts.md`，项目事实写入 `_data/neutriverse_projects.yml`。
3. 复制 `docs/templates/` 中对应模板，替换所有尖括号占位符；不要把模板本身移入公开内容目录。
4. 只记录准备公开且有来源的事实。个人信息、项目状态、链接或 Release 不确定时省略，不用猜测值占位。
5. 提交前运行 `python tools/check_authoring.py` 和完整回归。

模板：

- Post：`docs/templates/neutriverse-post.md`
- Fragment：`docs/templates/neutriverse-fragment.yml`
- Project catalog entry：`docs/templates/neutriverse-project.json`

## 2. Post：Note 或 Essay

### 2.1 文件与正文

- 文件放在 `_posts/`，名称必须是 `YYYY-MM-DD-slug.md`；日期部分与 front matter 的 `date` 完全一致。
- 发布后不要为了分类整理改文件名、`date`、`slug` 或 `permalink`。这四项会影响旧 URL。
- `type: note` 用于问题、记录、学习或实现笔记；`type: essay` 用于完成度较高、论证或叙事更完整的长文。
- Fragment 不建成 Post，也不使用第四种 Type。
- 正文保持作者原文。taxonomy 或布局维护不构成重写旧正文的授权。

### 2.2 必填字段

| 字段 | 规则 |
|---|---|
| `title` | 公开标题，非空字符串 |
| `date` | `YYYY-MM-DD`，与文件名日期一致 |
| `type` | 只能是 `note` 或 `essay` |
| `topic` | 只能是 `computation`、`humanity`、`otaku`、`arts` |
| `tags` | YAML 列表；每一项在解析后必须是字符串，可为空列表 |

Topic 的边界：

- `computation`：计算、AI、数据、编程、数据库、网络、算法和机器学习。
- `humanity`：社会、哲学、个人反思、互联网文化、价值、身份与人的经验。
- `otaku`：游戏、动画、漫画、视觉小说、JRPG 及相关亚文化。
- `arts`：电影、书籍、文学与相邻传统文化作品。

跨领域内容选择文章的主问题所属 Topic，不为单篇文章新增 Topic。若边界无法由现有定义判断，应先记录决定，不用 categories 代替 Topic。

### 2.3 Tags 必须保持字符串

推荐给每个 tag 加引号，尤其是纯数字、日期、布尔形单词或 YAML 特殊值：

```yaml
tags: ["8086", "Addressing Modes", "Assembly Language"]
```

以下写法会让 `8086` 被 YAML 当作数字，校验会失败：

```yaml
tags: [8086, Addressing Modes]
```

Tags 使用可检索的具体概念或作品名。不要恢复已退役的 `Bus`、`Changelog`，也不要仅因单次使用就删除有意义的实体标签。当前映射与理由见 `docs/content-taxonomy-tag-review.md`。

### 2.4 可选字段

| 字段 | 规则 |
|---|---|
| `series` | 仅使用 `_data/content_taxonomy.yml` 已定义的 label；不要从 categories 推断 |
| `description` | 公开摘要；必须由文章本身支持 |
| `hidden` | 仅为布尔值 `true`/`false`；hidden、noindex 与访问控制不是同义词 |
| `categories` | 旧 URL 兼容字段，可省略；默认不新增 category 名称 |
| `media_subpath`、`image` 等 | 只有文章实际使用对应资源时添加 |

当前 Series label 是 `Database Systems`、`Computer Architecture`、`Computer Networks`。新增 Series 需要先在 taxonomy 中定义稳定 ID、label 和说明，再添加文章；不能只在单篇 front matter 中发明名称。

`categories` 是 ADR 0001 定义的只读兼容层。新文章不强制填写；确需挂入既有旧分类时才显式使用。它不能覆盖 Type/Topic/Series/Tags，也不能用来创造第二套权威分类。

## 3. Fragment

Fragment 的唯一来源是 `_tabs/thoughts.md` front matter 中的 `fragments` 列表。把 Fragment 模板中的单个列表项粘贴到该列表，不建立第二份数据文件。

| 字段 | 规则 |
|---|---|
| `text` | 原始短句正文，非空字符串 |
| `id` | `fragment-YYYY-MM-DD`；同日多条追加简短 kebab-case 后缀；发布后不改 |
| `date` | `YYYY-MM-DD`，必须与 ID 中日期相同 |
| `type` | 固定为 `fragment` |
| `topic` | 四个 Topic 之一 |
| `tags` | 字符串列表；无标签时写 `[]` |

Fragment 链接使用 `/thoughts/#<id>`。排序变化不应改变 ID；THINK、Search 和 Atom feed 都复用这一来源与稳定锚点。

## 4. Project catalog 与详情页

当前 BUILD catalog 是 `_data/neutriverse_projects.yml`，文件扩展名虽为 `.yml`，内容必须保持有效 JSON。当前七个项目是已批准范围；新增第八个项目或公开新的隐藏入口，需要先取得范围与可见性决定，不能因为有模板就自行扩大目录。

### 4.1 新增或更新记录

1. 找到能够支持公开名称、摘要、状态和链接的站内文件或公开外部 URL。
2. 复制 Project 模板中的单个对象，替换占位符后加入 `projects` 数组。
3. `id` 使用小写 kebab-case，发布后稳定；`detail_url` 固定为 `/build/<id>/`。
4. 同一提交创建 `build/<id>/index.md`：

```yaml
---
layout: neutriverse-project
title: "<same public project name>"
description: "<same source-supported summary>"
permalink: /build/<stable-kebab-id>/
project_id: <stable-kebab-id>
---
```

5. 根据已批准的可见性决定是否在详情页添加 `robots: noindex,nofollow` 与 `sitemap: false`。不要根据“公开列在 BUILD/OBSERVE”自动推断应用页可以索引。

### 4.2 字段和不造假规则

- `id`、`name`、`summary`、`contexts`、`visibility`、`sources`、`detail_url` 必填。
- `contexts` 必须包含 `build`，只有已批准的观察项目才增加 `observe`。
- `visibility` 只能是 `listed`、`listed_noindex`、`unlisted_noindex`。
- `sources` 至少一项。`site` source 的 `path` 必须真实存在；`external` source 必须是公开 HTTPS URL。
- `status` 未被来源明确支持时整个字段省略；不要写 `unknown`、`active`、`complete` 或 `paused` 作为猜测。
- `links`、`related_posts`、`releases` 没有真实数据时整个字段省略，不创建空对象或假入口。
- Release 至少要有可核实的名称或版本；版本文章、可访问页面或仓库存在本身不等于已经发布 Release。
- Project Log 是文章与项目的次级关系，不是第四种 Type；关联文章仍保留自己的 Note/Essay 与 Topic。
- Gate/NAVI 的工具入口、私人配置和本地数据不得因 catalog 更新公开。MMXProj 不在本轮 catalog；关联项目仓库只读，不由本站提交修改。

字段完整说明见 `docs/neutriverse-project-schema.md`。

## 5. 校验和发布

### 5.1 本地命令

PowerShell：

```powershell
python tools/check_authoring.py
python -m unittest discover -s tests -v
bundle exec jekyll build -d _site
python tools/check_search_feed.py _site
python tools/check_seo_routes.py _site
```

`check_authoring.py` 只读检查当前 checkout，成功时输出 Post、Fragment、Project 数量的 JSON；失败时逐项输出文件与原因并返回非零状态。它不改写正文、自动补字段或生成新内容。

### 5.2 提交前清单

- [ ] 模板中的全部尖括号占位符已替换。
- [ ] Type/Topic/Series 来自现有 taxonomy；所有 Tags 解析后都是字符串。
- [ ] Fragment ID 唯一且日期一致；Project ID 与详情页接线一致。
- [ ] status、links、releases、个人事实和可见性都有来源或明确决定；未知项已省略。
- [ ] 新增内容未改变任何旧文件名、date、slug、permalink、正文或旧 URL。
- [ ] `python tools/check_authoring.py`、全回归与 Jekyll build 通过。
- [ ] 提交后核对该精确 head 的 Build and Deploy；不能用其他提交的成功结果替代。

production workflow 会在 Jekyll build 前运行 authoring 校验，并继续执行 Search/feed、SEO/旧路由、资源边界、移动端与无障碍门禁。失败时先修复该 head，不强推或绕过门禁。

## 6. 修改既有内容

本指南主要用于新增内容。对本轮重构前已经存在的文章与 Fragment，正文、文件名、date、slug、permalink 和旧 URL 仍受 T01 基线保护。维护 taxonomy、模板或显示层时，不批量重写旧学习笔记，也不把格式统一当作内容编辑授权。
