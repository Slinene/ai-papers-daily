---
title: 'Batch-wise Adaptive Pruning: Periodic Neuron Activation-Aware Weight Pruning
  for Language Reasoning Model'
title_zh: 批量自适应剪枝：面向语言推理模型的周期性神经元激活感知权重剪枝
authors:
- Yongmin Kim
- Shota Takashiro
- Yusuke Iwasawa
- Takeshi Kojima
- Yutaka Matsuo
affiliations:
- The University of Tokyo
arxiv_id: '2608.14003'
url: https://arxiv.org/abs/2608.14003
pdf_url: https://arxiv.org/pdf/2608.14003
published: '2026-08-14'
collected: '2026-08-17'
category: LLM
direction: LLM 推理优化 · 自适应剪枝
tags:
- adaptive pruning
- batch inference
- reasoning model
- activation memory
- training-free
- LLM
one_liner: 针对批量推理下训练无关自适应剪枝失效问题，提出周期 top-k 选择与激活记忆，实现推理加速同时保持精度
practical_value: '- 在批量推理服务（如推荐系统中的 LLM 重排、解释生成、Agent 规划）中，如果采用训练无关自适应剪枝，优先用 **top-k
  选择替代阈值剪枝**：批量共享 mask 时阈值受激活聚合分布偏移影响大，top-k 对分布偏移鲁棒，稀疏率更可控。

  - 对长文本生成/推理链场景，可借鉴 **activation memory 累积跨更新周期的神经元重要性**，保留周期性重激活的关键神经元；这类似于对“反复出现的
  pattern”做缓存，减少剪枝对长程推理的破坏。

  - 工程上可设置 **update period 周期性更新 mask**，而不是每个 token 都重新选择，降低剪枝本身的开销；在 batch size>1、高吞吐优先的部署中，这是保持加速比的关键。

  - 评估推理优化方法时应显式测试 **batched inference**，因为离线单样本精度无法反映线上批量服务下的漂移问题；尤其对于生成式推荐中的 LLM
  打分/文案生成，batch 内样本分布差异可能导致 mask 失效。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：大型推理模型（LRMs）通过长链思维生成提升复杂任务表现，但推理计算成本高。生产环境中批量推理对高吞吐至关重要，然而现有训练无关自适应剪枝方法在批量推理下严重退化：batch 必须共享一个剪枝 mask，聚合激活分布发生偏移，离线校准的阈值不再匹配，导致实际稀疏率漂移、推理任务精度崩溃。

**方法关键点**：提出 **Batch-wise Adaptive Pruning**，包含两个组件：
1. **周期 top-k 选择**：替换阈值法，对聚合后的重要性分数做 top-k 选取，不受激活分布聚合偏移影响；且每更新周期执行一次，而非每个 token 都选，保持加速效果。
2. **激活记忆**：观察到重要神经元在长推理生成中周期性重新激活，维护跨更新阶段的累积重要性，保留反复出现的神经元，避免周期性关键神经元被误剪。

**关键结果**：在 DeepSeek-R1-Distill-Qwen-7B 上，batch size 4、50% 目标稀疏度下，平均准确率超越先前 SOTA 自适应剪枝方法 **39.7 个百分点**；50% 实际稀疏度时相对稠密推理达到 **1.40× 加速**。
