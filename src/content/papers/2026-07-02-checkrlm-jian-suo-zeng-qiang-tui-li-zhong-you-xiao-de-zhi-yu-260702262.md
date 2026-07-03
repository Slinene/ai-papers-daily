---
title: 'CheckRLM: Effective Knowledge-Thought Coherence Checking in Retrieval-Augmented
  Reasoning'
title_zh: CheckRLM：检索增强推理中有效的知识与思维一致性检查
authors:
- Dingling Xu
- Ruobing Wang
- Qingfei Zhao
- Yukun Yan
- Zhichun Wang
- Daren Zha
- Shi Yu
- Zhenghao Liu
- Shuo Wang
- Xu Han
affiliations:
- Beijing Normal University
- Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Tsinghua University
- Northeastern University
arxiv_id: '2607.02262'
url: https://arxiv.org/abs/2607.02262
pdf_url: https://arxiv.org/pdf/2607.02262
published: '2026-07-02'
collected: '2026-07-03'
category: Reasoning
direction: 检索增强推理 · 知识一致性检查
tags:
- Retrieval-Augmented Reasoning
- Factual Error Correction
- Reasoning Language Models
- Knowledge Coherence
- RAG
- Error Accumulation
one_liner: 提出 CheckRLM 框架，在推理过程中实时提取事实声明并利用外部知识进行错误检测与最小代价修正，显著缓解长链条推理的错误累积。
practical_value: '- 在电商/Agent 的多步推理链（如推荐解释、对话决策）中，可借鉴事实声明提取与外部知识校验机制，实时拦截幻觉，提升最终推荐可信度。

  - 最小代价修正策略（仅针对错误事实局部改写）能降低 token 开销，适合在线高并发场景的推理成本控制。

  - 知识-思维一致性检查模块可作为独立插件嵌入现有 LLM 推理流程，无需重新训练模型，便于业务快速实验与迭代。

  - 长推荐会话或用户意图推理中易出现错误累积，该方法提供的及时纠错可防止下游决策偏离，增强整体链路的鲁棒性。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：推理语言模型（RLMs）通过延长推理链提升复杂任务表现，但长链条中易引入事实错误，尤其知识密集型场景。现有方法难以在推理过程中低成本、精准地定位并修正这些细微知识不一致，导致错误累积，影响最终答案可靠性。

**方法关键点**：CheckRLM 在 RLMs 推理过程中插入检查-修正机制。首先从每一步推理中提取**事实声明（factual claims）**，对每个声明进行原子化分割并利用检索增强（RAG）获取外部知识进行一致性校验；当检测到错误时，仅在错误事实处进行**最小代价的精准修正**，避免重写整个推理链，从而保持知识与思维间的连贯性。该框架可灵活适配不同基础 RLM，无需额外训练。

**关键结果**：在多个知识密集型推理基准上，CheckRLM 显著超越现有基线方法，特别是在长链条任务中有效抑制错误累积，且推理成本更低（修正环节不引入过多额外 token 消耗）。
