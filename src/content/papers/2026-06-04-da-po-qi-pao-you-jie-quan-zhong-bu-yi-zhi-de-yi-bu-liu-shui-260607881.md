---
title: 'Breaking the Bubble: Asynchronous Pipeline Parallel Training with Bounded
  Weight Inconsistency'
title_zh: 打破气泡：有界权重不一致的异步流水线并行训练
authors:
- Itay Elam
- Eliron Rahimi
- Avi Mendelson
- Chaim Baskin
affiliations:
- Technion - Israel Institute of Technology
- Ben-Gurion University of the Negev
arxiv_id: '2606.07881'
url: https://arxiv.org/abs/2606.07881
pdf_url: https://arxiv.org/pdf/2606.07881
published: '2026-06-04'
collected: '2026-06-12'
category: Training
direction: 分布式训练 · 流水线并行优化
tags:
- Pipeline Parallelism
- Asynchronous Training
- Weight Staleness
- Gradient Accumulation
- Distributed Training
one_liner: 通过局部梯度积累作为版本控制，零气泡异步流水线以有界权重漂移换取训练加速
practical_value: '- 梯度累积被重新用作一种轻量级版本控制机制：通过增大累积步数减缓参数版本演化，使异步流水线中微批次跨越的优化器更新次数有界，从而控制权重不一致，这个思路可直接用于训练推荐大模型或
  Agent 的 LLM 骨干网，无需额外校正模块。

  - PACI 无需权重暂存、预测或全局同步，内存峰值与同步 1F1B 持平，对 GPU 显存敏感的电商推荐模型训练（如多模态大模型）很有吸引力，可以在不增加显存成本的前提下消除流水线气泡。

  - 实现零气泡流水线调度：所有设备持续利用，在 GPT 预训练中获得 1.69× 的时间到精度加速。对于需要快速迭代训练的大规模 Agent 或生成式推荐模型，可考虑采用类似有界异步流水线策略来压缩实验周期。

  - 该方法揭示一个原则：前向/后向的权重不一致不必完全消除，显式控制其边界即可安全地换取效率。在设计其他分布式训练策略（如异步数据并行或混合并行）时，可借鉴这一思路，通过参数版本漂移的定量控制来简化系统设计。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：流水线并行训练中，同步调度（如 1F1B）保证前向/后向的权重一致性，但引入计算气泡，浪费硬件性能；异步调度消除气泡，却导致微批次在不同权重版本下执行，传统方法需要权重暂存、预测或校正，增加内存和实现复杂度。

**方法关键**：提出 PACI，一种无气泡的异步流水线方法。核心创新在于利用局部梯度累积作为版本控制机制：通过累积 K 个微批次的梯度后再更新参数，使参数版本演化速度相对流水线延迟显著减慢，从而将任何一个微批次在前向和后向传播中跨越的优化器更新次数限制在有界范围内。PACI 无需权重暂存、不需预测、不增加参数副本、不要全局同步，保持了与同步 1F1B-flush 相同的峰值内存占用。

**关键结果**：在 GPT 风格的 LM 预训练中，PACI 达到与同步 1F1B-flush 相同的训练稳定性和最终困惑度，实现完全流水线利用率（零气泡），且训练时间到精度最高比最快的 flush 基线加速 1.69 倍。验证了前向/后向不一致不必消除，只需显式有界即可换取显著效率提升。
