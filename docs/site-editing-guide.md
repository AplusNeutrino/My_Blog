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
| 左下角 RSS 图标 | `_data/contact.yml` |
| 文章分享按钮 | `_data/share.yml` |
| 头像 / 社交预览图 | `NeutriverseTitle.png` |
| 浏览器标签页图标 | `favicon.ico`、`_includes/favicons.html` 和 `assets/img/favicons/` |
| 自定义域名 | `CNAME` 和 `_config.yml` |
| 首页右侧状态模块 | `_includes/neutriverse-status.html` |
| 标签页列表 | `_layouts/tags.html` |
| 当前自定义配色方案 | `assets/css/ChirpyDefault.css` |
| 阅读时间文案 | `_includes/read-time.html` |
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

### 2.4 左侧导航栏

截图位置：左侧中部导航菜单。

来源：

| 导航文字 | 文件 | 作用 |
| --- | --- | --- |
| 中间层首页 | `index.html` | 首页入口，使用 `layout: home` |
| 中间文章索引 | `_tabs/categories.md` | 分类页 |
| 中间文章标签集 | `_tabs/tags.md` | 标签页 |
| 中间思维片段 | `_tabs/thoughts.md` | 即时短句页 |
| 中间层时间线 | `_tabs/archives.md` | 归档页 |
| 中间层漫游指南 | `_tabs/about.md` | 关于页 |

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
| `title` | 页面标题、导航文字和页面顶端显示名 |
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

### 2.5 左下角订阅图标

截图位置：左下角圆形图标。

来源：

```yaml
# _data/contact.yml
- type: rss
  icon: "fas fa-rss"
  noblank: true
```

当前只保留 RSS 订阅图标。GitHub、X、邮箱等图标已从 `_data/contact.yml` 中移除，因此不会在左下角显示。

常见修改：

| 目标 | 修改位置 |
| --- | --- |
| 隐藏 RSS 图标 | 删除或注释 `_data/contact.yml` 中的 `rss` 条目 |
| 恢复 GitHub/X/邮箱等图标 | 按 `_data/contact.yml` 下方注释模板重新添加对应条目，并确认 `_config.yml` 中有对应用户名或链接 |
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

### 2.11 右侧栏：中间记忆

截图位置：右侧原 `热门标签` 区块，现在标题为 `中间记忆`。

来源：

```text
_data/middle_memory.yml
_includes/trending-tags.html
```

`_data/middle_memory.yml` 中每一条 `sentences` 都是一句候选短句：

```yaml
sentences:
  - "第一句短句"
  - "第二句短句"
```

页面会按本地日期每天 24 点自动切换到当天对应的一句。如果 `sentences` 为空，或全部是空白内容，则显示：

```text
正在加载中...
```

如果以后想恢复 Chirpy 默认热门标签，需要删除仓库里的 `_includes/trending-tags.html` 覆盖文件，主题就会重新使用 gem 内置版本。

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

这组配置同时用于文章页底部的授权说明。正文页会显示：

```text
本文由作者按照 CC BY-NC 4.0. 进行授权
```

页脚在宽屏时显示为一行，顺序为版权、框架与主题来源、站点运行信息。三块内容会自动分散占满一行：版权靠左，框架与主题来源居中，站点运行信息靠右。

```text
©2026 Neutrino. CC BY-NC 4.0.           Powered by Jekyll · Theme by Chirpy.           本站已运行 304 天 · 总浏览 8,771 次
```

窄屏时自动拆成三行并居中显示。

这些内容来自：

```text
_includes/footer.html
```

其中 `Jekyll` 链接到 `https://jekyllrb.com/`，`Chirpy` 链接到 `https://github.com/cotes2020/jekyll-theme-chirpy`，与关于页中的来源链接保持一致。

### 2.13 页脚网站运行天数

截图位置：页脚中的 `本站已运行 ... 天 · 总浏览 ... 次`。

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

### 2.14 中间思维片段

页面文件：

```text
_tabs/thoughts.md
```

这个文件同时负责页面入口和短句数据。以后只需要在 front matter 的 `fragments` 列表里继续追加：

```yaml
fragments:
  - text: "短句正文"
    date: 2026-04-30
    tags: [标签一, 标签二]
```

字段含义：

| 字段 | 作用 |
| --- | --- |
| `text` | 短句正文，会显示在方块主体里 |
| `date` | 方块底部显示的日期 |
| `tags` | 方块底部显示的标签，可写多个；没有标签时写 `tags: []` |

页面样式来自：

```text
_layouts/thoughts.html
assets/css/ChirpyDefault.css
```

这个页面不是 `_posts` 文章，因此不会计入首页状态模块的文章数量和总字数。

### 2.15 浏览器标签页图标 favicon

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
title: 中间层漫游指南
icon: fas fa-info-circle
order: 5
---
```

下面才是正文，可以自由改：

```markdown
这里是 Neutrino 的个人文字站。

这里面有笔记、读后感和记忆碎片。

欢迎所有的你。
```

关于页中的十五年倒计时也在这个文件里。正文和倒计时之间保留了 20 行 `<br>` 空行。倒计时起点是 `2024-09-15 20:00:00 +08:00`，目标时间是十五年后的 `2039-09-15 20:00:00 +08:00`，页面会每秒刷新显示：

```text
倒计时：剩余xx年xx月xx日xx时xx分xx秒
```

## 6. 如何修改颜色、字体、卡片样式

当前仓库使用 Chirpy 主题包提供基础布局，再通过自定义 CSS 覆盖 Neutriverse 的浅色/深色配色。

### 6.1 白天/黑夜模式切换按钮

```yaml
# _config.yml
theme_mode: dark
```

当前站点临时固定为黑夜模式，左下角模式切换按钮会隐藏。

如果以后想恢复点击切换，可以把它改回空值：

```yaml
theme_mode:
```

恢复为空后，Chirpy 会重新显示左下角模式切换按钮。

### 6.2 白天/黑夜颜色接口

颜色接口文件：

```text
assets/css/ChirpyDefault.css
```

当前 `ChirpyDefault.css` 用于恢复 Chirpy 默认配色，同时保留 Neutriverse 新增模块的布局样式。

它不重新定义 Chirpy 的全局颜色变量，只使用主题已有变量：

| 字段 | 作用 |
| --- | --- |
| `--main-bg` | Chirpy 默认页面背景 |
| `--card-bg` | Chirpy 默认卡片背景 |
| `--main-border-color` | Chirpy 默认边框颜色 |
| `--text-color` | Chirpy 默认正文颜色 |
| `--text-muted-color` | Chirpy 默认次级文字颜色 |
| `--heading-color` | Chirpy 默认标题颜色 |

例如：

```css
.neutriverse-status {
  background: var(--card-bg);
  border: 1px solid var(--main-border-color);
}
```

注意：`_data/neutriverse.yml` 现在不再保存配色。当前默认观感主要由 Chirpy 主题自己控制；`ChirpyDefault.css` 只维护新增模块的布局和少量尺寸样式。

旧的高饱和测试配色保留在 `assets/css/neutriverse.css`，完整留档见：

```text
docs/april-fools-color-scheme.md
```

## 7. 如何修改图标

站内图标主要来自 Font Awesome。

常见位置：

| 位置 | 文件 |
| --- | --- |
| 左侧导航图标 | `_tabs/*.md` 的 `icon` 字段 |
| 左下角订阅图标 | `_data/contact.yml` |
| 文章分享图标 | `_data/share.yml` |
| 文章点赞图标 | `_includes/post-like.html` |
| 中间思维片段图标 | `_tabs/thoughts.md` 的 `icon` 字段 |
| 文章卡片日期/分类图标 | Chirpy 主题内置 |

修改示例：

```yaml
# _data/contact.yml
- type: rss
  icon: "fas fa-rss"
  noblank: true
```

```markdown
---
icon: fas fa-book
---
```

如果换了图标但页面没显示，通常是类名写错，或当前主题版本没有加载对应 Font Awesome 图标。

### 7.1 文章底部点赞

文章底部分享按钮左侧的点赞功能来自：

```text
_includes/post-like.html
```

点赞接口配置在：

```yaml
# _data/neutriverse.yml
likes:
  endpoint: "https://neutriverse-stats.feiyuzou-me.workers.dev"
  count_path: "/likes"
  hit_path: "/like"
```

前端期望接口格式为：

```text
GET  {endpoint}{count_path}?path=/posts/example/ -> {"likes": 0}
POST {endpoint}{hit_path} with {"path": "/posts/example/"} -> {"likes": 1}
```

如果接口暂时不可用，页面会退回到浏览器本地计数，避免按钮空白或报错。

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
| 标签页列表 | `_layouts/tags.html` |
| 当前默认配色兼容样式 | `assets/css/ChirpyDefault.css` |
| 加载自定义 CSS | `_includes/metadata-hook.html` |
| 覆盖主题 favicon | `_includes/favicons.html` 和 `assets/img/favicons/` |
| 文章封面图 | 文章 front matter 的 `image` |

### 首页右侧状态模块

状态模块显示运行天数、文章数量、标签数量、总字数、最近更新和总访问。模块位置由 `_layouts/default.html` 控制，只在首页右侧栏顶部显示。

### 标签页列表

标签页文件：

```text
_layouts/tags.html
```

当前标签页已移除上方星图，只保留下方 tag 表。每个标签仍然链接到原来的标签归档页。

### 自定义白天/黑夜配色

文件：

```text
assets/css/ChirpyDefault.css
```

这里不覆盖 Chirpy 的默认配色，只保留状态模块、中间记忆、点赞按钮、文章封面等新增模块的结构样式。

### 文章封面图

首页卡片支持文章 front matter 的 `image` 字段。当前第一篇文章 `Zodiac` 已移除封面图；如果以后想给文章添加封面，可以写：

```yaml
image:
  path: /assets/img/covers/my-cover.png
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

### 文章阅读时间

文章页标题下方的阅读时间文案由这个文件控制：

```text
_includes/read-time.html
```

当前格式为：

```text
全文阅读预计需要 xx 分钟
```

## 9. 如何修改评论系统

文件：

```text
_config.yml
```

当前评论已启用 Utterances：

```yaml
comments:
  provider: utterances

utterances:
  repo: AplusNeutrino/My_Blog
  issue_term: pathname
```

Utterances 使用 GitHub Issues 保存评论，每篇文章会按页面路径匹配一个 issue。仓库目前是公开仓库并已启用 Issues。

如果以后想改用 Giscus，可以改成：

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
- 给 `assets/css/ChirpyDefault.css` 增加构建版本参数。
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
_data/middle_memory.yml
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
| 中间思维片段 | `_tabs/thoughts.md` 的 `fragments` |
| 文章公开发布时间 | 文章 front matter 的 `display_date` |
| 文章公开更新时间 | 文章 front matter 的 `display_updated_at` |
| 分类 | 文章 front matter 的 `categories` |
| 标签 | 文章 front matter 的 `tags` |
| 关于页 | `_tabs/about.md` |
| 导航图标 | `_tabs/*.md` 的 `icon` |
| 导航顺序 | `_tabs/*.md` 的 `order` |
| 左下角 RSS 图标 | `_data/contact.yml` |
| GitHub/X/邮箱基础信息 | `_config.yml` |
| 分享按钮 | `_data/share.yml` |
| 点赞按钮 | `_includes/post-like.html` 和 `_data/neutriverse.yml` 的 `likes` |
| 评论系统 | `_config.yml` 的 `comments`，当前为 Utterances |
| 阅读时间文案 | `_includes/read-time.html` |
| 深色/浅色切换按钮 | `_config.yml` 的 `theme_mode`，当前固定为 `dark` |
| 白天/黑夜颜色 | 当前由 Chirpy 默认主题控制，新增模块样式在 `assets/css/ChirpyDefault.css` |
| 首页状态模块 | `_includes/neutriverse-status.html` |
| 右侧中间记忆短句 | `_data/middle_memory.yml` |
| 标签页列表 | `_layouts/tags.html` |
| 导航文字统一替换 | `_includes/neutriverse-labels.html` |
| 白天/黑夜仪表盘配色 | 当前由 Chirpy 默认主题控制，新增模块样式在 `assets/css/ChirpyDefault.css` |
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

如果只是想调整页面上显示的发布日期或更新时间，但不想改变文章排序、归档逻辑或真实 Git 修改时间，可以在文章 front matter 里添加：

```yaml
display_date: 2026-04-30
display_updated_at: 2026-05-01
```

示例：

```yaml
---
title: "Zodiac"
date: 2025-07-01
display_date: 2026-04-30
display_updated_at: 2026-05-01
categories: [Blog]
tags: [FirstPost]
---
```

效果：

| 字段 | 作用 |
| --- | --- |
| `date` | Jekyll/Chirpy 的真实发布日期，用于排序、归档、URL 等主题逻辑 |
| `display_date` | 首页文章卡片和文章详情页公开显示的发布日期 |
| `last_modified_at` | Chirpy/Git 识别到的真实更新时间 |
| `display_updated_at` | 文章详情页公开显示的更新时间 |

如果删除 `display_date`，页面会自动恢复显示 `date`。如果删除 `display_updated_at`，页面会自动恢复显示默认的 `last_modified_at`。
