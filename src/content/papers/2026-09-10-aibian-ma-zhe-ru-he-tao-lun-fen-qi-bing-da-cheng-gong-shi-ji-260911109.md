---
title: 'How AI Coders Discuss, Disagree, and Reach Consensus: Challenges and Opportunities
  for LLM-Based Qualitative Coding'
title_zh: AI编码者如何讨论、分歧并达成共识：基于LLM的定性编码挑战与机遇
authors:
- Jeongyeon Kim
- John Mitchell
affiliations:
- Stanford University
arxiv_id: '2609.11109'
url: https://arxiv.org/abs/2609.11109
pdf_url: https://arxiv.org/pdf/2609.11109
published: '2026-09-10'
collected: '2026-09-12'
category: MultiAgent
direction: 多智能体LLM协作定性编码机制
tags:
- Multi-agent LLM
- Qualitative Coding
- Agent Debate
- Consensus
- Codebook
- Thematic Analysis
one_liner: 多智能体LLM定性编码中，独立编码、辩论与协调流程的有效性受编码簿长度、数据相似性和代理分歧影响
practical_value: '- 多智能体辩论机制可迁移至电商场景中的商品属性标注、用户评论意图分类、广告标签体系构建等定性判断任务：采用“独立编码→辩论→协调分歧”流程，且不必强制要求达成一致，未解决的激烈辩论往往意味着更高质量的分析结果。

  - 设计Agent协作时需显式建模上下文状态：论文发现LLM缺乏对讨论上下文的适应性响应，因此在多轮Agent交互中应引入记忆模块或动态调节策略，避免固定轮次和静态提示词。

  - 编码簿长度（相当于Prompt/标签体系复杂度）显著影响准确率，建议在业务落地时先对标签粒度做消融实验，找到准确率与标注成本之间的平衡点。

  - 论文开源了AI讨论数据集和评估框架，可直接用于评测自家多Agent系统在标注、审核、分类等任务上的可靠性，省去从头搭建评估环境的工作。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：定性编码费时费力，多智能体LLM被认为有自动化潜力，但缺乏在不同上下文中的可靠性实证。本研究旨在量化多智能体LLM编码的有效性，并揭示影响编码结果的关键因素。

**方法关键点**：
- 构建基于文献的基线pipeline：多个AI代理独立编码→相互辩论→协调分歧。
- 跨多个定性数据集进行评估，系统分析编码簿长度、定性数据相似性、代理间分歧程度等中介变量。
- 分析代理讨论行为与人类讨论行为的异同。

**关键结果**：
- 编码准确率显著依赖于编码簿长度、数据相似性和代理分歧程度。
- 意外发现：激烈且未解决的代理辩论反而与更高准确率相关，说明深度讨论可能挖掘出更丰富的语义。
- LLM能模拟许多人类讨论行为（如表达异议、引用证据），但缺乏对讨论上下文的适应性响应，例如不能根据前文动态调整策略。
- 提出面向自动化编码系统的设计建议，并开源AI讨论数据集及方法框架。
