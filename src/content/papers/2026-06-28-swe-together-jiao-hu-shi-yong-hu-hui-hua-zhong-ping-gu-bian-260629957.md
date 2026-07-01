---
title: 'SWE-Together: Evaluating Coding Agents in Interactive User Sessions'
title_zh: SWE-Together：交互式用户会话中评估编码智能体
authors:
- Yifan Wu
- Zhuokai Zhao
- Songlin Li
- Ho Hin Lee
- Jiacheng Zhu
- Shirley Wu
- Tianhe Yu
- Serena Li
- Lizhu Zhang
- Xiangjun Fan
affiliations:
- Meta
arxiv_id: '2606.29957'
url: https://arxiv.org/abs/2606.29957
pdf_url: https://arxiv.org/pdf/2606.29957
published: '2026-06-28'
collected: '2026-07-01'
category: Agent
direction: 编程Agent交互式协作评估
tags:
- coding agent
- multi-turn
- user simulator
- benchmark
- collaborative evaluation
one_liner: 从真实用户会话构建多轮编程基准，用反应式模拟器重放交互，同时衡量代码正确性和所需干预次数。
practical_value: '- **交互式Agent评估范式**：可直接迁移到电商推荐Agent的评估中，构建多轮用户模拟器，根据用户偏好和反馈调整推荐，同时衡量推荐成功率与用户修改轮数，评估协作效率。

  - **真实会话驱动的基准构建**：借鉴其从海量真实交互记录中筛选可重放会话的方法，在电商场景中收集用户与推荐系统的多轮对话，构建可复现的评估集，避免人工设计偏差。

  - **反应式用户模拟器设计**：利用LLM模拟用户意图保持和条件反馈，用于离线测试推荐Agent的意图理解与纠错能力，降低人工评测成本。

  - **效率与效果联合指标**：不仅关注最终推荐准确率，也追踪达到满意结果所需的交互轮数，更全面反映用户体验，适合用于优化多轮推荐策略。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有编程Agent基准（如SWE-Bench）采用静态评测：一次性给出任务描述，只评估最终代码。实际编程协助是交互式的，用户多轮澄清、添加约束、纠正错误，现有基准无法反映这种协作过程。

**方法**：从11,260条真实用户与编码Agent的会话中，筛选出109个仓库级任务，要求仓库状态可恢复、用户目标清晰、结果可观测，构建多轮基准SWE-Together。为在不同Agent间重放交互，设计了一个反应式LLM用户模拟器，它保留原始用户意图，并在Agent进展需要时提供反馈。评估维度包括最终仓库正确性，以及交互过程中所需的纠正反馈轮数。

**关键结果**：在多个前沿编码Agent上的实验表明，更强的Agent通常达到更高的最终成功率（如Claude 3.5 Sonnet达38.5%），同时平均仅需2.1轮纠正反馈，而较弱Agent需要4.8轮且成功率低。这说明更强的Agent能更好地理解用户意图，减少交互摩擦，提升用户体验。
