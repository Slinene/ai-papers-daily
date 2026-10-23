---
title: 'Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity
  in Test-Time Reasoning'
title_zh: 直接优化 Pass@k 的思维剪枝：平衡测试时推理的质量与多样性
authors:
- Mahdi Salmani
- Adel Javanmard
- Devansh Gupta
- Meisam Razaviyayn
affiliations:
- University of Southern California
arxiv_id: '2610.31667'
url: https://arxiv.org/abs/2610.31667
pdf_url: https://arxiv.org/pdf/2610.31667
published: '2026-10-22'
collected: '2026-10-23'
category: Reasoning
direction: LLM 推理剪枝 · pass@k 优化
tags:
- Test-time scaling
- pass@k
- thought pruning
- reasoning models
- quality-diversity tradeoff
- LLM inference
one_liner: 直接优化所选候选池的 pass@k，让质量与多样性在剪枝中自动平衡，超越现有策略
practical_value: '- 在搜索/推荐/QueryRec 中用 LLM 生成多个候选 query、文案或商品描述时，可将 pass@k 作为筛选目标：只保留能最大化「至少有一个成功」概率的子集，而不是单独按质量分或多样性筛选，减少冗余并提升最终命中率。

  - 工程实现上，对每个生成前缀估计其最终成功的概率（可由模型 logprob 或轻量分类器给出），然后用联合概率选择子集，而非独立 top-k 截断；该思想可嵌入
  beam search 或 MCTS 框架，用于 Agent 多步推理轨迹的早期剪枝。

  - 结论显示保留中等数量候选时收益最明显，提示不要过度剪枝：当 LLM 生成大量候选时，仅保留前 1-2 个可能损害覆盖，适当保留 5-10 个候选再精排更优。

  - 该方法不依赖特定模型，适用于任何可产出候选集的 LLM 场景，可直接用于消息推送选词、搜索 suggestion 的候选生成环节。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：测试时扩展通过生成大量候选解提高正确率，但全部完成计算成本高；在生成短前缀后剪枝可分配计算。现有方法分为质量导向（打分丢弃可能错误）与多样性导向（选择不同推理轨迹），二者存在探索-利用权衡，但缺乏直接优化目标。

**方法关键点**：直接优化所选候选池上的 pass@k——最大化池中至少有一个部分解继续完成时正确的概率。该目标自动奖励高质量部分解并惩罚冗余，因此质量与多样性由目标本身平衡，无需单独 ad-hoc 设计。具体通过选择子集来优化联合成功概率，而非独立打分或多样性采样。

**关键结果**：在八个开放权重推理模型上，该方法优于现有质量和多样性剪枝策略；尤其在保留中等数量部分解继续生成时增益更明显，验证了直接平衡质量与多样性的价值。
