# Neutriverse 博客使用与修改说明

本文档对应仓库 `AplusNeutrino/My_Blog`，说明当前 GitHub Pages 博客中各个设计要素、图标和文字信息分别来自哪里，以及如何修改。

线上网站地址：

```text
https://neutriverse.uk/
```

本地仓库路径：

```text
C:\Users\ZFY\Documents\Codex\2026-04-29\github-blog\repo
```

## 1. 这个网站是什么结构

当前网站不是普通单页 HTML，而是一个 Jekyll 博客，使用 `jekyll-theme-chirpy` 主题。

核心文件：

| 用途 | 文件 |
| --- | --- |
| 站点总配置 | `_config.yml` |
| 首页入口 | `index.html` |
| 文章目录 | `_posts/` |
| 左侧导航页签 | `_tabs/` |
| 左下角社交图标 | `_data/contact.yml` |
| 文章分享按钮 | `_data/share.yml` |
| 头像 / 社交预览图 | `NeutriverseTitle.png` |
| 浏览器标签页图标 | `favicon.ico`、`_includes/favicons.html` 和 `assets/img/favicons/` |
| 自定义域名 | `CNAME` 和 `_config.yml` |
| 首页右侧状态模块 | `_includes/neutriverse-status.html` |
| 标签星图页 | `_layouts/tags.html` |
| 自定义白天/黑夜配色 | `_data/neutriverse.yml` 和 `assets/css/neutriverse.css` |
| 自动部署流程 | `.github/workflows/pages-deploy.yml` |
| 主题依赖 | `Gemfile` |

大部分布局、卡片样式、搜索框、右侧栏、移动端适配都由 Chirpy 主题提供。你的仓库主要通过配置文件和 Markdown 内容来控制它们。

## 2. 截图中的元素对应哪里

### 2.1 左侧圆形头像

截图位置：左上角圆形图案。

来源：

```yaml
# _config.yml
avatar: "/NeutriverseTitle.png"
```

图片文件：

```text
NeutriverseTitle.png
```

修改方式：

1. 准备一张新的图片，例如 `avatar.png`。
2. 放到仓库根目录，或放入 `assets/img/`。
3. 修改 `_config.yml`：

```yaml
avatar: "/avatar.png"
```

如果图片放在 `assets/img/avatar.png`，则写：

```yaml
avatar: "/assets/img/avatar.png"
```

注意：当前网站使用自定义域名 `neutriverse.uk`，站点部署在域名根路径，所以 `_config.yml` 里的 `baseurl` 应保持为空字符串。

### 2.2 左侧站点名称 Neutriverse

截图位置：头像下面的大字 `Neutriverse`。

来源：

```yaml
# _config.yml
title: Neutriverse
```

修改方式：

```yaml
title: 你的新博客名
```

这个标题也会影响浏览器标题、SEO 信息、RSS 等位置。

### 2.3 左侧副标题 Quantum Pandemonia

截图位置：站点名称下面的斜体小字。

来源：

```yaml
# _config.yml
tagline: Quantum Pandemonia
```

修改方式：

```yaml
tagline: 你的副标题
```

### 2.4 左侧导航栏：主页、分类、标签、归档、关于

截图位置：左侧中部导航菜单。

来源：

| 导航文字 | 文件 | 作用 |
| --- | --- | --- |
| 首页 | `index.html` | 首页入口，使用 `layout: home` |
| 分类 | `_tabs/categories.md` | 分类页 |
| 标签 | `_tabs/tags.md` | 标签页 |
| 归档 | `_tabs/archives.md` | 归档页 |
| 关于 | `_tabs/about.md` | 关于页 |

这些文件开头都有 front matter，例如：

```markdown
---
layout: categories
icon: fas fa-stream
order: 1
---
```

字段含义：

| 字段 | 含义 |
| --- | --- |
| `layout` | 使用主题里的哪种页面布局 |
| `icon` | 导航图标，来自 Font Awesome |
| `order` | 在导航栏中的排序，数字越小越靠上 |

修改图标：

```markdown
icon: fas fa-tags
```

图标类名来自 Font Awesome。比如：

| 想要的图标 | 可用类名示例 |
| --- | --- |
| 首页 | `fas fa-home` |
| 分类 | `fas fa-stream` |
| 标签 | `fas fa-tags` |
| 归档 | `fas fa-archive` |
| 关于 | `fas fa-info-circle` |
| 书本 | `fas fa-book` |
| 笔 | `fas fa-pen` |

修改顺序：

```markdown
order: 2
```

如果想临时隐藏某个导航页，可以把对应文件移出 `_tabs/`，或改名为不被 Jekyll 识别的文件名，例如 `about.md.bak`。

### 2.5 左下角社交图标

截图位置：左下角 GitHub、X、邮件、RSS 等圆形图标。

来源：

```yaml
# _data/contact.yml
- type: github
  icon: "fab fa-github"

- type: twitter
  icon: "fa-brands fa-x-twitter"

- type: email
  icon: "fas fa-envelope"
  noblank: true

- type: rss
  icon: "fas fa-rss"
  noblank: true
```

具体用户名来自 `_config.yml`：

```yaml
github:
  username: AplusNeutrino

twitter:
  username: Neutrino_X

social:
  name: Neutrino
  email: Latencyvladimir@gmail.com
  links:
    - https://twitter.com/Neutrino_X
    - https://github.com/AplusNeutrino
```

常见修改：

| 目标 | 修改位置 |
| --- | --- |
| 改 GitHub 链接 | `_config.yml` 的 `github.username` |
| 改 X/Twitter 链接 | `_config.yml` 的 `twitter.username` 和 `social.links` |
| 改邮箱 | `_config.yml` 的 `social.email` |
| 隐藏某个图标 | 在 `_data/contact.yml` 中删除或注释对应条目 |
| 增加 LinkedIn 等 | 参考 `_data/contact.yml` 下方注释模板 |

### 2.6 顶部面包屑“首页”

截图位置：页面内容区域顶部的 `首页`。

来源：Chirpy 主题根据当前页面自动生成。

普通情况下不需要改。如果想改导航语言，优先检查：

```yaml
# _config.yml
lang: zh-CN
```

### 2.7 右上角搜索框

截图位置：右上角 `搜索...`。

来源：Chirpy 主题内置搜索功能。

搜索索引来自文章、页面标题和正文内容。通常不需要手动维护。新增文章后，GitHub Actions 重新构建，搜索内容会自动更新。

如果想完全移除或大幅修改搜索框，需要覆盖 Chirpy 主题模板，不建议作为早期修改项。

### 2.8 首页文章卡片

截图位置：中间的 `Zodiac`、`Python复健笔记01` 两张卡片。

来源：`_posts/` 目录中的 Markdown 文章。

当前文章：

```text
_posts/2025-07-01-TestInfo.md
_posts/2025-07-01-PythonIntro.md
```

文章卡片中的信息来源：

| 卡片内容 | 来源 |
| --- | --- |
| 标题 | 文章 front matter 的 `title` |
| 日期 | 文章 front matter 的 `date` |
| 分类 | 文章 front matter 的 `categories` |
| 标签 | 文章 front matter 的 `tags` |
| 摘要 | 文章正文开头自动截取 |

示例：

```markdown
---
title: "Zodiac"
date: 2025-07-01
categories: [Blog]
tags: [FirstPost]
---

# Super Large title

正文内容写在这里。
```

修改文章标题：

```markdown
title: "新的标题"
```

修改首页摘要：

Chirpy 默认会从正文开头自动生成摘要。想控制摘要，可以在 front matter 中加入：

```markdown
description: "这是一段会显示在首页卡片中的摘要。"
```

### 2.9 文章卡片底部图标：日历、文件夹

截图位置：文章卡片底部日期前的小日历、分类前的小文件夹。

来源：Chirpy 主题模板内置 Font Awesome 图标。

你通常只需要改文章的 `date` 和 `categories`，图标本身会自动显示。

### 2.10 右侧栏：最近更新

截图位置：右侧 `最近更新` 区块。

来源：Chirpy 主题根据文章自动生成。

排序主要依据文章日期和最后修改时间。相关逻辑包含：

```text
_plugins/posts-lastmod-hook.rb
```

普通修改方式：

| 目标 | 做法 |
| --- | --- |
| 让文章出现在最近更新 | 修改或新增文章后推送 |
| 改文章显示名 | 修改文章 front matter 的 `title` |
| 改文章日期 | 修改文章 front matter 的 `date` |

### 2.11 右侧栏：热门标签

截图位置：右侧 `热门标签` 区块。

来源：所有文章 front matter 的 `tags` 汇总。

示例：

```markdown
tags: [Python, Note]
```

如果希望标签更规整，建议统一使用英文或统一使用中文，不要混用多个含义接近的标签，例如 `Python`、`python`、`Py`。

### 2.12 页脚版权文字

截图位置：底部 `©2026 Neutrino. CC BY-NC 4.0.`

来源：

```text
_data/neutriverse.yml
```

当前配置：

```yaml
copyright:
  year: 2026
  owner: Neutrino
  label: "CC BY-NC 4.0."
  tooltip: "This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License."
  link: "https://creativecommons.org/licenses/by-nc/4.0/"
```

字段含义：

| 字段 | 作用 |
| --- | --- |
| `year` | 页脚版权年份 |
| `owner` | 页脚版权姓名 |
| `label` | 显示在姓名后面的协议文字 |
| `tooltip` | 鼠标移动到协议文字上时显示的说明 |
| `link` | 协议文字点击后打开的链接 |

如果以后想换成其他协议或自定义说明，只改这几个字段即可。`link` 留空时，协议文字会变成不可点击文本，但仍保留鼠标悬停说明。

### 2.13 页脚网站运行天数

截图位置：底部右侧，原来显示 `本站采用 Jekyll 主题 Chirpy` 的地方。

来源：

```text
_includes/footer.html
```

开始日期来源：

```yaml
# _config.yml
site_start_date: "2026-04-29"
```

页脚会在浏览器中根据这个日期自动计算：

```text
本站已运行 123 天 · 总浏览 1,024 次
```

总浏览量来自 Cloudflare Worker：

```text
https://neutriverse-stats.feiyuzou-me.workers.dev
```

页脚脚本每天每个浏览器只向 `/hit` 发送一次 `POST`，避免刷新页面时重复增加太多浏览量。当天再次打开页面会改为读取 `/stats`。

原来的主题署名已经移动到关于页：

```text
_tabs/about.md
```

### 2.14 浏览器标签页图标 favicon

来源：

```text
favicon.ico
_includes/favicons.html
assets/img/favicons/
```

Chirpy 主题默认会通过 `_includes/favicons.html` 声明一组图标路径，例如：

```text
assets/img/favicons/favicon-16x16.png
assets/img/favicons/favicon-32x32.png
assets/img/favicons/favicon.ico
```

如果仓库里不覆盖这个 include 和这些资源，浏览器可能会加载到主题包自带的默认图标。当前仓库已经新增本地覆盖文件：

```text
_includes/favicons.html
```

所有 favicon 声明都集中在这个文件中，并且带有构建版本参数：

```html
<link rel="icon" type="image/png" sizes="32x32" href="{{ favicon_path }}/favicon-32x32.png?v={{ favicon_version }}">
```

这样无论以后使用自定义域名还是 GitHub Pages 项目路径，图标路径都更可靠，也能降低浏览器继续显示旧图标的概率。

## 3. 如何新增一篇文章

在 `_posts/` 目录新建文件，命名格式必须是：

```text
YYYY-MM-DD-title.md
```

例如：

```text
_posts/2026-04-29-first-note.md
```

基础模板：

```markdown
---
title: "第一篇正式笔记"
date: 2026-04-29
categories: [Blog]
tags: [Note]
description: "这是一篇测试首页摘要的文章。"
---

这里开始写正文。

## 二级标题

正文支持 Markdown。
```

写作建议：

- `title` 用来显示在首页卡片、文章页标题和最近更新里。
- `date` 会影响首页排序和归档。
- `categories` 建议 1 到 2 个，例如 `[学习笔记]`、`[Blog]`。
- `tags` 可以多个，例如 `[Python, Jekyll, Note]`。
- `description` 可选，但建议写，方便控制首页摘要。

## 4. 如何修改已有文章

打开 `_posts/` 下对应文件即可。

例如要修改 `Zodiac`：

```text
_posts/2025-07-01-TestInfo.md
```

要修改 `Python复健笔记01`：

```text
_posts/2025-07-01-PythonIntro.md
```

修改标题、分类、标签、日期时，只改文件开头的 front matter。修改正文时，只改 front matter 下方的 Markdown 内容。

## 5. 如何修改“关于”页面

文件：

```text
_tabs/about.md
```

文件开头这段不要随便删：

```markdown
---
# the default layout is 'page'
icon: fas fa-info-circle
order: 4
---
```

下面才是正文，可以自由改：

```markdown
## 关于 Neutriverse

这里写你的介绍。
```

## 6. 如何修改颜色、字体、卡片样式

当前仓库使用 Chirpy 主题包提供基础布局，再通过自定义 CSS 覆盖 Neutriverse 的浅色/深色配色。

### 6.1 白天/黑夜模式切换按钮

```yaml
# _config.yml
theme_mode:
```

`theme_mode` 留空时，Chirpy 会显示左下角模式切换按钮。这个按钮位于左下角社交按钮组最左端，可以在白天模式和黑夜模式之间点击切换。

如果以后想强制固定某一种模式，可以改成：

```yaml
theme_mode: light
theme_mode: dark
```

但固定后切换按钮会隐藏。当前为了保留点击切换按钮，应该继续保持为空。

### 6.2 白天/黑夜颜色接口

颜色接口文件：

```text
_data/neutriverse.yml
```

当前默认配色：

```yaml
theme_colors:
  note: "Alea iacta est (vladimirlenin@qq.com), 2026-04-29"
  light:
    background: "#F8FAFC"
    primary: "#2563EB"
    accent: "#FACC15"
    text: "#111827"
  dark:
    background: "#020617"
    primary: "#10B981"
    accent: "#94A3B8"
    text: "#E5E7EB"
```

实际配置里还有更多可调字段：

| 字段 | 作用 |
| --- | --- |
| `background` | 页面整体背景 |
| `surface` | 搜索框、顶部栏、普通面板底色 |
| `surface_alt` | 辅助面板或悬停底色 |
| `card` | 文章卡片、状态模块、标签块底色 |
| `border` | 边框、分隔线 |
| `primary` | 主色，链接、激活态、重点按钮 |
| `accent` | 强调色，头像边框、分隔点等 |
| `text` | 正文文字 |
| `muted` | 次级文字 |
| `heading` | 标题文字 |
| `sidebar_bg` | 左侧栏背景 |
| `sidebar_text` | 左侧栏主文字 |
| `sidebar_muted` | 左侧栏副文字 |
| `sidebar_button_bg` | 左下角按钮背景 |
| `sidebar_button_text` | 左下角按钮图标颜色 |
| `sidebar_hover_bg` | 左侧导航和按钮悬停背景 |
| `topbar_bg` | 顶部栏背景 |
| `link` | 链接颜色 |
| `link_hover` | 链接悬停颜色 |
| `code_bg` | 行内代码和代码块背景 |
| `shadow` | 卡片悬停阴影 |

白天和黑夜各有一套字段：

```yaml
theme_colors:
  light:
    background: "#F8FAFC"
  dark:
    background: "#020617"
```

CSS 入口：

```text
assets/css/neutriverse.css
```

这个文件会读取 `_data/neutriverse.yml` 里的颜色配置，并生成对应的 CSS 变量：

```css
html[data-mode='light'] { ... }
html[data-mode='dark'] { ... }
```

注意：修改 `_data/neutriverse.yml` 后需要重新提交并部署，线上颜色才会更新。

当前白天模式使用的是一套高饱和测试配色，方便辨识每个颜色字段对应的页面元素。完整留档见：

```text
docs/april-fools-color-scheme.md
```

## 7. 如何修改图标

站内图标主要来自 Font Awesome。

常见位置：

| 位置 | 文件 |
| --- | --- |
| 左侧导航图标 | `_tabs/*.md` 的 `icon` 字段 |
| 左下角社交图标 | `_data/contact.yml` |
| 文章分享图标 | `_data/share.yml` |
| 文章卡片日期/分类图标 | Chirpy 主题内置 |

修改示例：

```yaml
# _data/contact.yml
- type: github
  icon: "fab fa-github"
```

```markdown
---
icon: fas fa-book
---
```

如果换了图标但页面没显示，通常是类名写错，或当前主题版本没有加载对应 Font Awesome 图标。

## 8. 如何修改分享按钮

文件：

```text
_data/share.yml
```

当前启用：

```yaml
platforms:
  - type: Twitter
  - type: Facebook
  - type: Telegram
```

如果不想显示某个平台，可以删除或注释对应条目。

如果想启用 Weibo、LinkedIn、Reddit 等，文件里已经有注释模板，取消注释即可。

## 8.1 如何修改 Neutriverse 视觉模块

当前站点新增了几处自定义视觉：

| 功能 | 文件 |
| --- | --- |
| 首页右侧 `Neutriverse Status` | `_includes/neutriverse-status.html` |
| 标签星图页 | `_layouts/tags.html` |
| 白天/黑夜仪表盘配色 | `_data/neutriverse.yml` 和 `assets/css/neutriverse.css` |
| 加载自定义 CSS | `_includes/metadata-hook.html` |
| 覆盖主题 favicon | `_includes/favicons.html` 和 `assets/img/favicons/` |
| 文章封面图 | 文章 front matter 的 `image` |

### 首页右侧状态模块

状态模块显示运行天数、文章数量、标签数量、总字数、最近更新和总访问。模块位置由 `_layouts/default.html` 控制，只在首页右侧栏顶部显示。

### 标签星图页

标签页文件：

```text
_layouts/tags.html
```

每个标签会生成一个可点击节点，链接仍然指向原来的标签归档页。节点位置主要由 `assets/css/neutriverse.css` 中的 `.node-*` 类控制。

### 自定义白天/黑夜配色

文件：

```text
assets/css/neutriverse.css
```

这里覆盖了 Chirpy 默认暗色主题的一些变量和组件样式，包括背景、侧边栏、卡片、状态模块、标签星图。

### 文章封面图

首页卡片支持文章 front matter 的 `image` 字段。当前 `Zodiac` 已添加：

```yaml
image:
  path: /NeutriverseTitle.png
  alt: Neutriverse cover image
```

给其他文章添加封面时，把图片放到仓库中，例如：

```text
assets/img/covers/my-cover.png
```

然后在文章开头写：

```yaml
image:
  path: /assets/img/covers/my-cover.png
  alt: Cover image description
```

## 9. 如何修改评论系统

文件：

```text
_config.yml
```

当前评论关闭：

```yaml
comments:
  provider:
```

可以选择：

```yaml
comments:
  provider: giscus
```

然后补齐：

```yaml
giscus:
  repo:
  repo_id:
  category:
  category_id:
```

建议以后确定要评论区时再配置，因为 Giscus 需要 GitHub Discussions 和对应 ID。

## 9.1 Cloudflare Web Analytics 与总浏览量

Chirpy 已经支持 Cloudflare Web Analytics 的前端统计脚本。配置位置：

```yaml
# _config.yml
analytics:
  cloudflare:
    id:
```

Cloudflare 后台创建 Web Analytics site 后，会给出一段类似这样的代码：

```html
<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{"token": "这里是TOKEN"}'></script>
```

把 `token` 的值填到 `_config.yml`：

```yaml
analytics:
  cloudflare:
    id: "这里是TOKEN"
```

注意：Cloudflare Web Analytics 的 beacon 脚本只负责采集访问数据，它不会在网页前端公开提供“总浏览量数字”。如果要在网页上直接显示总浏览量，需要额外做一层安全读取：

| 方案 | 说明 |
| --- | --- |
| Cloudflare Worker | 当前采用此方案，Worker + KV 保存公开浏览量数字 |
| GitHub Actions 定时更新 JSON | Action 用 API token 拉取数据，生成静态 `assets/data/stats.json` |
| 第三方公开计数器 | 例如 GoatCounter 或不蒜子，接入更简单，但不是 Cloudflare Web Analytics |

不要把 Cloudflare API token 直接写进网页 JavaScript。那会把 token 暴露给所有访问者。

当前 Worker 地址写在：

```text
_includes/footer.html
```

如果以后 Worker 地址变化，修改：

```js
const statsEndpoint = 'https://neutriverse-stats.feiyuzou-me.workers.dev';
```

## 10. 如何把 Cloudflare 域名连接到博客

你购买的域名是：

```text
neutriverse.uk
```

目标博客仓库是：

```text
AplusNeutrino/My_Blog
```

最终访问地址建议使用裸域：

```text
https://neutriverse.uk/
```

`www.neutriverse.uk` 可以作为自动跳转的备用域名。

### 10.1 仓库侧已经需要的文件

仓库根目录需要有：

```text
CNAME
```

内容为：

```text
neutriverse.uk
```

`_config.yml` 里需要是：

```yaml
url: "https://neutriverse.uk"
baseurl: ""
```

含义：

| 配置 | 含义 |
| --- | --- |
| `url` | 站点正式域名 |
| `baseurl` | 自定义域名根路径部署时应为空 |

### 10.2 GitHub Pages 设置

在 GitHub 网页上操作：

1. 打开仓库 `AplusNeutrino/My_Blog`。
2. 进入 `Settings`。
3. 左侧进入 `Pages`。
4. 确认 `Build and deployment` 的 source 是 `GitHub Actions`。
5. 在 `Custom domain` 输入：

```text
neutriverse.uk
```

6. 点击 `Save`。
7. 等 DNS 生效后，回到这个页面勾选 `Enforce HTTPS`。

注意：GitHub 官方说明里提到，使用自定义 GitHub Actions 发布时，GitHub 不一定会自动创建 `CNAME` 文件；所以我们手动在仓库中保留 `CNAME`，同时仍然需要在 Pages 设置里保存 custom domain。

### 10.3 Cloudflare DNS 设置

登录 Cloudflare 后：

1. 选择域名 `neutriverse.uk`。
2. 进入左侧 `DNS`。
3. 进入 `Records`。
4. 删除或停用和 `@`、`www` 冲突的旧记录。尤其留意默认停车页、旧 A 记录、旧 CNAME。
5. 添加下面这些记录。

裸域 `neutriverse.uk`：

| Type | Name | Content | Proxy status | TTL |
| --- | --- | --- | --- | --- |
| `A` | `@` | `185.199.108.153` | `DNS only` | `Auto` |
| `A` | `@` | `185.199.109.153` | `DNS only` | `Auto` |
| `A` | `@` | `185.199.110.153` | `DNS only` | `Auto` |
| `A` | `@` | `185.199.111.153` | `DNS only` | `Auto` |

`www` 子域：

| Type | Name | Content | Proxy status | TTL |
| --- | --- | --- | --- | --- |
| `CNAME` | `www` | `AplusNeutrino.github.io` | `DNS only` | `Auto` |

可选 IPv6 记录：

| Type | Name | Content | Proxy status | TTL |
| --- | --- | --- | --- | --- |
| `AAAA` | `@` | `2606:50c0:8000::153` | `DNS only` | `Auto` |
| `AAAA` | `@` | `2606:50c0:8001::153` | `DNS only` | `Auto` |
| `AAAA` | `@` | `2606:50c0:8002::153` | `DNS only` | `Auto` |
| `AAAA` | `@` | `2606:50c0:8003::153` | `DNS only` | `Auto` |

建议先只用 `DNS only`，也就是灰色云朵。这样 GitHub Pages 更容易正确验证域名和签发 HTTPS 证书。等 GitHub Pages 页面显示 HTTPS 可用、网站稳定后，再考虑是否开启 Cloudflare 代理。

不要添加通配符记录，例如：

```text
*.neutriverse.uk
```

通配符 DNS 可能带来子域名被错误接管的风险。

### 10.4 Cloudflare SSL/TLS 建议

在 Cloudflare 的 `SSL/TLS` 页面：

1. 模式建议使用 `Full`。
2. 不建议使用 `Flexible`，因为它可能导致 HTTPS 重定向循环或源站连接不一致。
3. 在 GitHub Pages 的 `Enforce HTTPS` 可勾选后，优先使用 GitHub Pages 自己的 HTTPS。

如果你一直保持 `DNS only`，Cloudflare 的代理层 SSL 设置不会真正介入访问链路，但保持 `Full` 是比较稳的默认选择。

### 10.5 如何检查 DNS 是否生效

在 Windows PowerShell 中可以运行：

```powershell
Resolve-DnsName neutriverse.uk -Type A
Resolve-DnsName www.neutriverse.uk -Type CNAME
```

预期：

- `neutriverse.uk` 能看到 GitHub Pages 的 `185.199.xxx.153` 地址。
- `www.neutriverse.uk` 指向 `AplusNeutrino.github.io`。

也可以在浏览器访问：

```text
https://neutriverse.uk/
https://www.neutriverse.uk/
```

DNS 传播可能需要几分钟到 24 小时。GitHub Pages 的 HTTPS 证书签发也可能需要等待一段时间。

### 10.6 常见问题

| 现象 | 可能原因 | 处理 |
| --- | --- | --- |
| GitHub Pages 显示 DNS check failed | DNS 还没生效，或 Cloudflare 记录填错 | 等待传播，核对 A/CNAME 记录 |
| 打开 `neutriverse.uk` 是 Cloudflare 停车页 | 有旧记录或注册商默认页面 | 删除冲突记录，只保留 GitHub Pages 记录 |
| `www` 打不开 | 缺少 `www` CNAME | 添加 `CNAME www -> AplusNeutrino.github.io` |
| HTTPS 不可勾选 | GitHub 还没签发证书 | 等待，确认 DNS only |
| 页面资源路径不对 | `baseurl` 仍是 `/My_Blog` | 改成 `baseurl: ""` 并重新部署 |

## 11. 如何发布修改

修改文件后，提交并推送到 `main` 分支即可触发部署。

常用命令：

```powershell
git status
git add 修改过的文件
git commit -m "Update blog content"
git push origin main
```

部署流程文件：

```text
.github/workflows/pages-deploy.yml
```

GitHub Actions 成功后，网站会更新到：

```text
https://neutriverse.uk/
```

## 12. 当前仓库中需要留意的点

### 12.1 旧文章可能存在编码显示问题

你截图里 `Python复健笔记01` 可以显示，但本地 PowerShell 读取时会出现乱码。这通常与终端输出编码有关，也可能与历史编辑器保存编码有关。

建议以后统一使用 UTF-8 保存 Markdown 文件。用 VS Code 时可以在右下角确认编码是 `UTF-8`。

### 12.2 页面缓存与刷新

为了减少浏览器看到旧页面的概率，当前仓库做了这些处理：

```yaml
# _config.yml
pwa:
  enabled: false
  cache:
    enabled: false
```

并在 `_includes/metadata-hook.html` 中：

- 添加了 no-cache meta。
- 给 `assets/css/neutriverse.css` 增加构建版本参数。
- 注销旧的 Service Worker。
- 清理旧的 Cache Storage。

如果未来重新启用 PWA，浏览器可能再次缓存页面和资源，部署后看到旧内容的概率会变高。

### 12.3 自定义域名配置

当前自定义域名文件：

```text
CNAME
```

内容：

```text
neutriverse.uk
```

相关站点配置：

```yaml
url: "https://neutriverse.uk"
baseurl: ""
```

DNS 需要在 Cloudflare 后台设置。裸域 `neutriverse.uk` 指向 GitHub Pages 的 A/AAAA 记录，`www.neutriverse.uk` 可以 CNAME 到 `AplusNeutrino.github.io`。

### 12.4 不建议直接改主题源码

Chirpy 的大部分模板来自 Ruby gem，不在仓库中。早期建议优先改：

```text
_config.yml
_posts/
_tabs/
_data/contact.yml
_data/share.yml
_includes/head/custom-head.html
```

如果未来要深度自定义布局，再把主题模板复制到仓库中覆盖。

## 13. 最常用修改速查表

| 我想改 | 去哪里改 |
| --- | --- |
| 网站名 `Neutriverse` | `_config.yml` 的 `title` |
| 副标题 `Quantum Pandemonia` | `_config.yml` 的 `tagline` |
| 网站运行天数起始日 | `_config.yml` 的 `site_start_date` |
| 页脚运行天数显示 | `_includes/footer.html` |
| 头像 | `NeutriverseTitle.png` 和 `_config.yml` 的 `avatar` |
| 浏览器标签页图标 | `_includes/favicons.html` 和 `assets/img/favicons/` |
| 首页文章 | `_posts/` 下的 Markdown 文件 |
| 文章标题 | 文章 front matter 的 `title` |
| 文章摘要 | 文章 front matter 的 `description` |
| 分类 | 文章 front matter 的 `categories` |
| 标签 | 文章 front matter 的 `tags` |
| 关于页 | `_tabs/about.md` |
| 导航图标 | `_tabs/*.md` 的 `icon` |
| 导航顺序 | `_tabs/*.md` 的 `order` |
| 左下角社交图标 | `_data/contact.yml` |
| GitHub/X/邮箱 | `_config.yml` |
| 分享按钮 | `_data/share.yml` |
| 深色/浅色切换按钮 | `_config.yml` 的 `theme_mode`，保持为空 |
| 白天/黑夜颜色 | `_data/neutriverse.yml` 的 `theme_colors` |
| 首页状态模块 | `_includes/neutriverse-status.html` |
| 标签星图 | `_layouts/tags.html` 和 `assets/css/neutriverse.css` |
| 白天/黑夜仪表盘配色 | `_data/neutriverse.yml` 和 `assets/css/neutriverse.css` |
| 文章封面 | 文章 front matter 的 `image` |
| 部署流程 | `.github/workflows/pages-deploy.yml` |

## 14. 自定义显示数据接口

### 14.1 自定义总浏览量显示偏移

文件：

```text
_data/neutriverse.yml
```

配置：

```yaml
stats:
  display_offset: 0
```

这个值不会替代 Cloudflare Worker 里的真实浏览量，而是在真实浏览量基础上做显示层加减：

| 想要效果 | 写法 |
| --- | --- |
| 显示真实浏览量 | `display_offset: 0` |
| 显示真实浏览量 + 100 | `display_offset: 100` |
| 显示真实浏览量 - 100 | `display_offset: -100` |

页面显示逻辑：

```text
页面显示浏览量 = Worker 返回的真实 totalViews + display_offset
```

如果相减后小于 0，页面会显示为 0，避免出现负浏览量。

Worker 地址也放在同一个文件里：

```yaml
stats:
  endpoint: "https://neutriverse-stats.feiyuzou-me.workers.dev"
```

一般不需要修改，除非以后更换 Cloudflare Worker。

### 14.2 自定义文章发布日期显示

默认情况下，文章发布日期来自文章 front matter 的 `date`：

```yaml
date: 2025-07-01
```

如果只是想调整页面上显示的发布日期，但不想改变文章排序、归档逻辑或原始发布日期，可以在文章 front matter 里添加：

```yaml
display_date: 2026-04-30
```

示例：

```yaml
---
title: "Zodiac"
date: 2025-07-01
display_date: 2026-04-30
categories: [Blog]
tags: [FirstPost]
---
```

效果：

| 字段 | 作用 |
| --- | --- |
| `date` | Jekyll/Chirpy 的真实发布日期，用于排序、归档、URL 等主题逻辑 |
| `display_date` | 首页文章卡片和文章详情页公开显示的发布日期 |

如果删除 `display_date`，页面会自动恢复显示 `date`。
