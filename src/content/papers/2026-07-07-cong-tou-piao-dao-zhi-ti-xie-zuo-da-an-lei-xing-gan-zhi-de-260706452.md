---
title: 'From Voting to Agent Collaboration: Answer-Type-Aware LLM Pipelines for BioASQ
  14b'
title_zh: 从投票到智体协作：答案类型感知的LLM流水线
authors:
- Taeyun Roh
- Eunha Lee
- Wonjune Jang
- Sohyun Chung
- Junha Jung
- Jaewoo Kang
affiliations:
- Korea University
- Myongji University
- AIGEN Sciences
arxiv_id: '2607.06452'
url: https://arxiv.org/abs/2607.06452
pdf_url: https://arxiv.org/pdf/2607.06452
published: '2026-07-07'
collected: '2026-07-08'
category: Agent
direction: 多Agent协作与问题类型路由
tags:
- LLM
- Multi-Agent
- Biomedical QA
- Prompt Engineering
- Ensemble
- Chain-of-Thought
one_liner: 针对生物医学问答中不同答案类型设计LLM推理策略，结合多智体协作验证取得最佳结果
practical_value: '- **问题类型路由**：在推荐/搜索中，可对查询意图分类后路由到不同LLM推理策略，例如事实型查询用CoT，主观型查询用多Agent辩论，减少单一模板的偏差。

  - **多Agent验证与集成**：对于需要多源证据的推荐解释或复杂决策，可采用类似“提取-生成-验证-聚合”的协作链，提高答案可靠性和可解释性，尤其适合客服Agent或商品选品解释。

  - **自反思与顺序扰动**：yes/no问题中对证据片段进行洗牌和自反思，可降低模型对输入顺序的敏感性，增强预测稳定性；在广告创意排序或商品评论摘要中可借鉴，避免位置偏差。

  - **集成预测与类型定制**：将多个模型/模板的预测通过投票结合，并根据问题类型定制集成方式，这种方法可直接用于搜索广告Bidding中的多信号融合，提升出价策略的鲁棒性。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：生物医学问答需从多篇文献中抽取并整合证据，不同答案类型（yes/no、事实、列表）对推理和评估的要求差异显著，单一LLM策略难以兼顾。

**方法关键点**：
- 构建**答案类型感知的LLM流水线**，对三类问题分别设计推理流程：
  - yes/no：对证据片段随机洗牌，结合多次自反思和多数投票，降低对输入顺序的敏感度。
  - factoid：将完整证据输入，通过链式思考（CoT）结合上下文学习，精准抽取生物医学实体。
  - list：引入**多Agent协作架构**，依次执行证据提取、候选生成、答案验证与最终聚合，确保列表答案的完整与准确。
- 在BioASQ 13b数据集上进行初步实验，确定各类型的最优策略组合，再应用于BioASQ 14b Task B。

**关键结果**：
- 在BioASQ 14b官方评测中，整体表现具竞争力，多个批次成绩突出。
- factoid子任务在Batch 4取得**第一名**，证明问题类型特化与多Agent验证能有效提升生物医学QA的准确性与证据可靠性。
