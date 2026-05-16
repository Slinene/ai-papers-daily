---
title: Is Grep All You Need? How Agent Harnesses Reshape Agentic Search
title_zh: Grep 是否就已足够？代理框架如何重塑代理式搜索
authors:
- Sahil Sen
- Akhil Kasturi
- Elias Lumer
- Anmol Gulati
- Vamse Kumar Subbiah
affiliations:
- PricewaterhouseCoopers
arxiv_id: '2605.15184'
url: https://arxiv.org/abs/2605.15184
pdf_url: https://arxiv.org/pdf/2605.15184
published: '2026-05-14'
collected: '2026-05-16'
category: Agent
tags:
- Agentic Search
- Grep
- Vector Search
- LLM Agent
- Context Engineering
- Evaluation
one_liner: 系统实验揭示：检索策略（grep vs 向量）的效果依赖于代理框架与工具输出方式，内联 grep 在对话记忆任务中整体更强
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机** 现有研究多将检索策略作为独立流水线进行评估，忽略了代理式工作中模型自主调用工具、迭代搜索的真实情境。如何将检索结果呈现给模型（内联或文件），以及自定义代理框架与供应商 CLI 框架的差异如何影响端到端性能，一直缺乏系统比较。这篇论文通过两项实验填补这一空白。

**方法关键点**
- 在 LongMemEval 基准的 116 个长对话问答上测试，覆盖知识更新、多会话聚合、时间推理等六类任务。
- 使用 Chronos 预处理流水线从对话中提取结构化时间事件，作为检索语料。
- 实现两种检索工具：基于正则的 grep 精确匹配，以及基于嵌入的近似最近邻向量搜索。
- 对比四种代理框架：自定义框架 Chronos（动态提示）与三个供应商 CLI 代理（Claude Code、Codex、Gemini CLI）。
- 对比两种工具结果传递方式：标准内联（直接注入上下文）和程序性文件（写入文件后要求代理读取或二次搜索）。
- 测试多个模型（Claude Opus 4.6、Claude Haiku 4.5、GPT-5.4、Gemini 3.1 Pro/Flash-Lite），用 GPT-4o 统一打分。

**关键实验与结果**
实验1 比较同一检索/传递方式下的全量 haystack 准确率。
- 内联 grep 在所有框架–模型组合上均优于内联向量搜索；Chronos + Claude Opus 4.6 内联 grep 达 93.1%，向量 83.6%；最低的 inline grep 也是 55.2%（Claude Code + Haiku），对应向量 44.0%。
- 同一模型换用不同框架，性能变化可达与更换检索器相当的幅度（例如 Claude Opus 在 Chronos 下 93.1%，Claude Code 下 76.7%）。
- 文件式传递改变排名：程序性向量在 5/10 的配置中反超 grep，但 Codex + GPT-5.4 的程序性 grep 暴跌至 55.2%，揭示文件工作流可能引入新的失败模式。

实验2 在逐步加入无关对话会话（s5→full）的条件下比较 grep-only 和 vector-only。
- grep 与向量的优劣不再是全局单调，而依赖于框架和模型：Chronos 下出现了多次交叉，而 Gemini CLI 上 Gemini 3.1 Pro 全程向量占优，Claude Code 上 Opus/Haiku 则 grep 始终胜出。这一结果表明，检索噪声下的行为受供应商工具设计（如提示、输出截断）的强烈影响。

**一句话结论**：在代理式搜索中，检索策略被代理框架和结果传递方式大幅重塑——“只能用 grep”的假设在某些堆栈下成立，在另一些下则被反转，提示评估必须将检索、编排和上下文工程作为一个联合系统来衡量。
