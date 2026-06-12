---
title: Recursive Agent Harnesses
title_zh: 递归智能体框架：以完整工具集为递归单元的长上下文推理
authors:
- Elias Lumer
- Sahil Sen
- Kevin Paul
- Vamse Kumar Subbiah
affiliations:
- PricewaterhouseCoopers, U.S.
arxiv_id: '2606.13643'
url: https://arxiv.org/abs/2606.13643
pdf_url: https://arxiv.org/pdf/2606.13643
published: '2026-06-11'
collected: '2026-06-12'
category: Agent
direction: Agent 架构 · 长上下文推理 · 代码即行动
tags:
- Recursive Agent Harness
- Long-Context Reasoning
- Code-as-Action
- Multi-Agent Systems
- Agent Architecture
one_liner: 将递归单元从裸模型调用升级为完整 agent harness，在长上下文推理上超越 coding agent 和 RLM，代码生成子 agent
  并行处理。
practical_value: '- **用代码脚本生成子 agent 替代工具调用并行限制**：当需要处理大量独立条目（如千级商品描述分析）时，由父 agent
  生成 asyncio 并行脚本，绕过 API 并行调用上限，可应用于电商批量商品属性提取或用户评论汇总。

  - **递归单元配备完整文件系统与执行环境**：每个子 agent 拥有独立的上下文窗口和工具（read_file、grep、execute 等），避免共享状态干扰，适合多文档聚合任务（如合同审查、多源数据抽取），可直接用于客服历史或物流文档分析。

  - **模式可组合：代码路径处理海量条目，工具调用路径处理少量任务**：根据条目数自动选择策略（少于5个用 JSON tool call，否则用代码执行），兼顾效率与灵活性，推荐系统中对候选池做细粒度推理时可借鉴。

  - **递归深度可配置且架构与模型解耦**：沿用 GPT-5 到 Claude Sonnet 均显著提升，表明 harness 设计本身带来增益，从业者可在现有模型基础上仅升级编排逻辑而无须换模型。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：长上下文推理任务（如 Oolong 基准）需要既能够导航大规模文档，又能对成千上万个独立条目进行逐条 LLM 推理。现有方法要么用 coding agent 依赖正则启发式损失精度，要么用递归语言模型（RLM）缺乏工具访问，两者均未同时满足导航与逐条推理。本文提出递归单元不应是裸模型调用，而应是完整的 agent harness（带文件系统、代码执行、规划工具），即递归 agent 框架（RAH）。

**方法关键点**：
- 父 agent 检查任务规模后，通过两种路径生成子 agent：少量条目（1–5）用 JSON tool call；大量条目则由父 agent 编写 Python 脚本（使用 asyncio.gather）并行启动子 harness，突破 API 并发限制。
- 每个子 agent 是完整 harness，具备相同的工具（读/写文件、grep、shell 执行、规划）和递归生成能力（可再生成子 agent），递归深度可配置（默认3层）。
- 子 agent 独立运行，无共享内存，结果写入共享输出文件，父 agent 最后聚合。
- 使用 LangChain 实现，但模式与具体框架无关。

**关键实验**：
- 数据集：Oolong-Synthetic 验证集，199 个样本，覆盖 1K 到 4M tokens 的 13 个上下文长度桶，平均 629K tokens。
- 基线：Full-context baseline（59.22%）、RLM（64.38%）、Codex coding agent（71.75%），均使用 GPT-5 骨干。
- RAH 在相同 GPT-5 下达到 81.36%，绝对提升 9.61 个百分点，且在所有长度桶上均优于 Codex。使用 Claude Sonnet 4.5 骨干进一步升至 89.77%。
- 逐类别分析：语义类型（USER/COMPARISON/LABEL）得分均超 86%，NUMERIC 类型因评分函数惩罚严格为 69.33%，但推理正确性无损。

**一句话结论**：将递归单元从无工具的模型调用替换为完整 agent harness，能在不改动模型的情况下，将长上下文聚合推理准确率提升近 10 个百分点，成本由并行控制。
