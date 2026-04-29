# Neutriverse Blog

这是 `AplusNeutrino/My_Blog` 的 GitHub Pages 博客仓库，基于 Jekyll 和 Chirpy 主题。

线上地址：

```text
https://neutriverse.uk/
```

## 写新文章

在 `_posts` 目录中新建 Markdown 文件，文件名格式为：

```text
YYYY-MM-DD-title.md
```

文章开头需要 front matter，例如：

```markdown
---
title: "文章标题"
date: 2026-04-29
categories: [Blog]
tags: [Note]
---
```

正文使用 Markdown 编写。推送到 `main` 分支后，GitHub Actions 会自动构建并部署到 GitHub Pages。

## 常用文件

- `_config.yml`: 站点标题、简介、头像、链接、语言和部署路径。
- `_posts/`: 文章目录。
- `_tabs/about.md`: 关于页。
- `NeutriverseTitle.png`: 侧边栏头像和社交预览图。
- `.github/workflows/pages-deploy.yml`: GitHub Pages 自动部署流程。

## 部署设置

仓库的 Pages source 应设置为 `GitHub Actions`。之后每次推送到 `main` 都会触发部署。

自定义域名：

```text
neutriverse.uk
```

Cloudflare DNS 中建议设置：

- `A` / `@` -> `185.199.108.153`
- `A` / `@` -> `185.199.109.153`
- `A` / `@` -> `185.199.110.153`
- `A` / `@` -> `185.199.111.153`
- `CNAME` / `www` -> `AplusNeutrino.github.io`

Proxy status 建议先设为 `DNS only`，等 GitHub Pages 验证和 HTTPS 证书签发完成后再考虑是否开启代理。
