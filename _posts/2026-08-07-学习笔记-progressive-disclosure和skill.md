---
title: "学习笔记：Progressive Disclosure和SKILL"
date: 2026-08-07
categories: [学习笔记, LLM笔记]
tags: [Progressive Disclosure, SKILL]
description: "总结了渐进式披露的原理和SKILL的一些设计思路。注意文章中很多部分的思路是直接照搬的参考文献，比起原创文章我更愿意称其为摘抄笔记。"
---

## 从 SKILL.md 开始的 Pandamonia


公司最近在调整和审查 Skills，遂针对性地学习了一点点内容。我发现在很多部门创建 Skill 时，为了满足各种繁杂的业务需求，或是在没有繁杂业务需求的时候受限于 AI 的各种防御性编程习惯，做出来的 Skill 争奇斗艳。试图通过穷尽一切可能性来覆盖所有复杂业务场景，往往是一种代价高昂且难以奏效的设计方式。

+ 从信息论的视角，输入与期望输出之间的互信息决定了模型表现的上限。为了让模型准确理解“是什么，为什么，怎么做”我们必须提供相当充足的上下文。但这种穷举所有可能性分支的方式只能导致任务决策树和指令集发生指数级膨胀，大部分上下文成为无效的噪声。有效信息被淹没，互信息被严重稀释。幻觉率与目标偏离率也随之飙升。
+ 从工程实践的视角，无限膨胀的上下文也将增加输入 Token、预填充（prefill）阶段的计算与延迟；频繁变化的提示前缀还可能降低 Prompt Cache 的复用率。消耗高昂算力成本。

知识约束（Skill）同时解决了两个经常被混为一谈的问题：如何复用一套工作方法，以及尽可能减少这套方法在不需要时占用的上下文长度。其中一个关键机制就是渐进式披露（Progressive Disclosure）：不在一开始把所有知识都交给模型，而是先提供目录或索引，让 Agent 在需要时主动检索和加载。这极大减少了无关说明长期占据上下文的机会。

Anthropic 在 2025 年 10 月公开推出 Agent Skills，并在同年 12 月宣布将其发布为开放标准。OpenAI 当前也采用 Agent Skills 标准，并将 Skill 定位为 ChatGPT 和 Codex 中可复用工作流的编写格式。本文将 Skill 理解为一个可被 Agent 发现并按需加载的结构化上下文包，其中包含完成一类任务所需的工作流程、判断标准以及相关资源。

其特征主要有以下三点：

+ 结构化上下文包：至少包含 `SKILL.md`，还可以包含脚本、参考资料和模板。
+ 可复用工作流：可重复执行、结果稳定、可以不断迭代，类似团队的 SOP。
+ 按需加载的能力扩展：设计上强调渐进式披露，先提供 Skill 的元信息，任务需要时再加载完整说明，并按需读取、使用或执行脚本与其他资源。

从上面可以看出，Skill 在产品体验上与 System Prompt 或 Slash Command 都有“保存常用指令”的相似之处，但在上下文进入方式上存在重要差异。System Prompt 通常承载跨任务适用的全局行为和长期约束，并长期驻留在上下文中；本文所说的 Slash Command 则是由用户显式触发、用于展开一段预设指令的命令或提示词模板。Skill 既可以由用户显式指定，也可以由 Agent 根据 `description` 隐式触发，并在执行过程中逐层加载。与无差别常驻相比，这种方式有助于节省 Token，并减少无关指令对当前任务的干扰。

OpenAI 当前文档明确区分了显式调用和隐式调用：用户可以主动选择 Skill，Agent 也可以根据 `description` 判断任务是否匹配。

## Skill 的三层上下文结构

Progressive Disclosure 原本是人机交互（HCI，Human-Computer Interaction）和交互设计领域的一种设计模式：先呈现当前任务必需的信息，再在用户或系统需要时揭示更多细节与复杂度。映射到 Skill 设计中，被“逐步揭示”的对象从界面功能变成了模型上下文。

基于该概念，我们将 Skill 的工程设计架构分成三层上下文结构：

+ 发现层，包括 `name`、`description`，主要在 Agent 启动时被加载入上下文。负责向大模型揭示 Skill 的作用以及何时应该加载；
+ 指导层，主要是 `SKILL.md` 正文，这部分会在 Skill 被触发时再加载。主要用于向大模型提供 Skill 的详细执行流程；
+ 资源层，主要是 `references/`、`scripts/`、`assets/`。这些资源会在 Agent 执行到具体分支时再被读取、使用或执行，用于补充当前步骤的细节，或提供更具确定性的处理能力。

在 Anthropic 发布的Agent Skills 开放规范中，给出了几个关键数据的建议尺度：

+ 元信息约 100 tokens；
+ `SKILL.md` 正文建议小于 5000 tokens；
+ 主文件建议不超过 500 行；
+ 其他资源按需读取；
+ 文件引用最好只深入一层。

而在 OpenAI 的 Skills 文档中也有类似的记载。Codex 为初始 Skills 列表设置了最多占上下文 2%，或在未知窗口大小时最多 8000 字符的预算；Skill 太多时，它会先缩短描述，甚至省略部分 Skill。

## 从 Progressive Disclosure 的视角看 Skill Design

基于以上分析，我们得出了一个好的 Skill 看起来应该是什么样子：

### 1. 精简 `description`，但保留路由接口特征

`description` 位于 Skill 的发现层，是最可能进入初始上下文、也可能因 Skill 数量过多而被缩短的内容，因此确实需要精简。但是很多人的精简都容易陷入误区，让`description`变成了字面意义上的 SKILL 描述。比如下面的这个版本，其虽然概括了 Skill 的用途，却不足以支持稳定的路由判断。

```plain
description: Helps with code review.
```

不妨将这个 skill 的功能范围，调用条件，隐式调用时可能出现的关键词，skill 边界等全部加入`description`。这样虽然轻度增加了上下文消耗，但是可以显著性增加 skill 的调度稳定性。

```plain
description: >
  Review a Git diff or pull request for correctness, regressions,
  security risks, and missing tests. Use when the user asks to
  review changes, inspect a PR, or assess a concrete patch.
```

此外，OpenAI 的官方 Skills 文档有提到，建议将核心用例和触发词放在 `description` 的前部，因为很多时候 Skill 的 `description` 有可能会被缩短。

### 2. 详尽`SKILL.md`，但不包含通识

 `SKILL.md` 正文主要应包含输入要求、任务执行顺序、关键判断标准、输出格式和验证方式，而不应大篇幅重复模型已经掌握的通识。Anthropic 的 Skill 编写指南将上下文窗口视为一种共享资源：Skill 被触发后，正文中的每个 Token 都会与系统提示、对话历史、用户请求和其他上下文竞争。

### 3. 基于条件分支的参考资料拆分方式

在如下的示例目录中：

```plain
code-review/
├── SKILL.md
├── references/
│   ├── python.md
│   └── typescript.md
└── scripts/
    └── collect-diff.ps1
```

在 `SKILL.md` 中，可以只保留工作流主干，以及指向各类详细资料的条件化读取说明：

```markdown
When reviewing Python changes, read references/python.md.
When reviewing TypeScript changes, read references/typescript.md.
Do not load both unless the patch contains both languages.
```

但值得注意的是，文件拆分并不直接等同于 Progressive Disclosure。只有当文件拆分正确对应了真实的任务分支，并且主文件清楚告诉 Agent 何时需要读取哪个文件的时候，才能形成有效的 Disclosure。开放规范中建议应当保持一层引用，Anthropic Skill 文档也支持了这一观点，明确反对了深层嵌套。 2026 年 7 月发布的一篇文章比较了原始文档导航、单层 Skill 披露和更深的层级式披露：在强 Agent 已能有效搜索的单个文档上，PD 的收益可能很小；文档集合扩大时，单层披露的优势会更明显；增加第二层路由则没有带来稳定收益，部分设置下反而降低了准确率。

### 4. 由任务脆弱程度决定的指令自由度

指令自由度的一个明显体现，是文本指令与确定性脚本之间的比例。

在 Skill 中使用文本指令还是调用脚本，需要根据任务的实际情况决定。对于规则明确、可程序化、要求结果稳定的步骤，可以调用脚本以获得更确定的输出：模型负责判断何时运行、如何提供参数以及怎样处理结果，脚本负责具体的确定性操作。对于需要结合上下文、允许多种正确做法的任务，例如代码审查，就只能主要依赖文本指令来提供目标、原则和判断标准。

而在实际的 Skill 任务解决过程中，往往需要同时使用这两者。例如：

```plain
文本指令：判断当前迁移属于哪种类型，并检查风险
    ↓
脚本：生成迁移、备份数据或执行格式校验
    ↓
文本指令：审查脚本结果并决定是否继续
    ↓
脚本：执行迁移和验证
```

所以“指令自由度”描述的实际上是还有多少决策空间留给模型临场完成。

+ 高指令自由度：文本给出目标、原则和判断标准。
+ 中指令自由度：文本给出流程，脚本或模板处理部分步骤。
+ 低指令自由度：要求模型严格执行指定脚本和固定顺序。

### 5. 对执行失败的评估思路

一个 Skill 通常可能出现两种不同的失败方式：

1. 路由失败：即本该触发的时候没有触发，或者在无关任务中误触发；
2. 执行失败：即 Skill 成功触发，但在工作流中依然遗漏步骤或者产生错误结果。

因此，在对失败情况的评估处理中，我们至少应该包括应当触发的任务、不应触发的邻近任务和触发后需要正确完成的代表性任务三者。Anthropic Skill 编写指南中建议先观察没有 Skill 时模型在哪里失败，再写最少量的说明解决这些失败，并通过任务的迭代来优化说明。

## 在 Skills 与 Tools 中的 Progressive Disclosure

Anthropic 在介绍 Advanced Tool Use 时给出了一个包含 58 个 Tools 的示例配置，其定义在会话开始前约占 55K tokens；Anthropic 还称其内部曾见过优化前达到 134K tokens 的工具定义开销。其 Tool Search 方案通过常驻一个搜索工具，再动态展开命中的完整 schema 来解决发现问题；在 Anthropic 披露的内部测试设置中，该方案将上下文使用量减少了约 85%。

Skills 的说明和 Tools 的接口定义都可能显著占用上下文，因此都存在按需加载的需求，但二者面临的问题并不相同。

Skills 的内容以说明、流程和参考资料为主，渐进式披露的核心是如何合理分层：哪些元信息应该常驻，哪些操作说明在触发后加载，哪些细节留到执行过程中再读取。

Tools 则必须向模型暴露足够准确的接口信息，模型才能发起有效调用。如果完整 schema 尚未进入上下文，系统仍需提供足够的工具索引、描述或路由机制，让模型知道应该搜索什么；否则，模型很难可靠地发现目标工具。因此，Tools 的渐进式披露不仅是内容组织问题，还包含工具发现与接口可调用性之间的依赖问题。

针对这一问题，已有在 Provider 和 Agent Runtime 引入 Tool Search、Dynamic Tool Routing 等机制，为工具按需加载增加一个发现层，这涉及的内容姑且不表。相比之下，Skill 可以较直接地利用名称、描述和文件引用形成披露路径。这也解释了为什么 Progressive Disclosure 不是 Skills 的附加优化，而是其最核心的结构特征之一。

## 参考资料

1. 时歌的博客：《关于渐进式披露工具上下文的几点讨论》：https://www.lapis.cafe/posts/ai-and-deep-learning/agi/progressive-disclosure-of-tool-context/

2. 时歌的博客：《上下文是稀缺资源｜RAG、Memory、Skills 的设计哲学刍议》：https://www.lapis.cafe/posts/ai-and-deep-learning/agi/context-scarcity-rag-memory-skills/

3. Anthropic, “Equipping agents for the real world with Agent Skills”：https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

4. OpenAI, “Build skills”：https://developers.openai.com/codex/skills

5. Agent Skills, “Specification”：https://agentskills.io/specification

6. Anthropic, “Skill authoring best practices”：https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices

7. IBM, “Progressive Disclosure”：https://www.ibm.com/docs/en/technical-content?topic=practices-progressive-disclosure

8. Yifeng He, Yinzhe Zhao, Jicheng Wang, Hao Chen, “Is Progressive Disclosure All You Need for Long-Context Agents?”：https://arxiv.org/abs/2607.17598

9. Anthropic, “Introducing advanced tool use on the Claude Developer Platform”：https://www.anthropic.com/engineering/advanced-tool-use

10. Anthropic, “Effective context engineering for AI agents”：https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

11. Ashish Vaswani et al., “Attention Is All You Need”：https://papers.neurips.cc/paper/7181-attention-isall-you-need.pdf

12. Nelson F. Liu et al., “Lost in the Middle: How Language Models Use Long Contexts”：https://aclanthology.org/2024.tacl-1.9.pdf
