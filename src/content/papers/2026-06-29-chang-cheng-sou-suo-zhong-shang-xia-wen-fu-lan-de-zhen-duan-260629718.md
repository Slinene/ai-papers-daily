---
title: Diagnosing and Mitigating Context Rot in Long-horizon Search
title_zh: 长程搜索中上下文腐烂的诊断与缓解
authors:
- Shijie Xia
- Yikun Wang
- Zhen Huang
- Pengfei Liu
affiliations:
- Shanghai Jiao Tong University
- Fudan University
- SII
- GAIR
arxiv_id: '2606.29718'
url: https://arxiv.org/abs/2606.29718
pdf_url: https://arxiv.org/pdf/2606.29718
published: '2026-06-29'
collected: '2026-06-30'
category: Agent
direction: 上下文腐烂诊断与缓解策略
tags:
- Context Rot
- Long-horizon Search
- LLM Agents
- Context Management
- Rejection Sampling
one_liner: 揭示长上下文导致LLM放弃回答的现象，提出上下文管理与拒绝采样两种缓解策略
practical_value: '- 长程搜索Agent（如电商多步查询）可采用滑动窗口、摘要等上下文管理方法防止性能衰减，论文给出的七种方法对比可作为选型参考

  - 后验拒绝采样策略：对Agent输出进行一致性过滤或置信度校准，过滤掉因上下文过长而冒出的放弃性答案，提升回答可靠性

  - 诊断思路复用：可在线评估并监控模型在长上下文下的“放弃率”，一旦发现显著上升，自动触发上下文压缩或截断

  - 工程实现上，将上下文管理与拒绝采样组合部署，可在不增加过多成本的情况下获得稳定收益'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM在长程搜索中累积大量上下文后，性能会下降，出现“上下文腐烂”——模型直接放弃回答或过早给出不确定答案，该现象在深层搜索Agent中尤为突出，但缺乏系统研究和缓解手段。

**方法**：
1. **诊断**：在多个开源模型和基准上评估长上下文下的行为退化，通过剪枝实验揭示累积上下文与腐烂现象的关联。
2. **上下文管理**：系统对比三类共七种上下文管理方法（如滑动窗口、摘要、关键词提取），从性能、成本和腐烂缓解效果三个维度给出选择指南。
3. **后验拒绝采样**：设计rot感知过滤策略，在输出端对同一问题的多次回答进行一致性聚合，剔除低质量回答；该策略在三种聚合方法上均有效。
4. **组合方案**：两种策略结合可进一步带来性能增益。

**关键结果**：
- 四个主流开源模型在三个基准上均出现上下文腐烂，且随上下文增长而加重。
- 上下文管理方法能有效缓解腐烂，但不同方法在成本与效果间存在权衡。
- rot感知拒绝采样显著提升了长程搜索的准确率，与上下文管理联合使用效果更优。
