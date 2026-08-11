---
title: 'Efficient Knowledge Distillation for LLMs: Offline Top-K Logits and a Fused
  Chunked KL Loss'
title_zh: 面向 LLM 的高效知识蒸馏：离线 Top-K logit 缓存与融合分块 KL 损失
authors:
- Bakbergen Ryskulov
- Iker García-Ferrero
- David Montero
- David Jansen
- Ali Hashemi
- Jezabel R. Garcia
- Antonio Tiene
- Román Orús
affiliations:
- Multiverse Computing
arxiv_id: '2608.03796'
url: https://arxiv.org/abs/2608.03796
pdf_url: https://arxiv.org/pdf/2608.03796
published: '2026-08-03'
collected: '2026-08-11'
category: Training
direction: 训练效率 · 知识蒸馏 · 长上下文
tags:
- Knowledge Distillation
- LLM
- Memory Efficiency
- Long Context
- Offline Distillation
- Fused Loss
one_liner: 通过缓存教师 Top-K logits 和融合分块 KL 损失，实现单 GPU 上长上下文蒸馏训练，匹配在线质量且内存线性增长。
practical_value: '- **离线蒸馏策略**：预教师 Top-K logit 一次缓存后重复用于多轮消融实验，大幅降低资源占用，适合需频繁蒸馏的推荐模型迭代。

  - **长上下文训练解锁**：融合分块 KL 损失让峰值内存与序列长度成线性关系，可在单卡 H200 上训练 32K 上下文，用于处理电商搜索中长用户行为序列的场景。

  - **损失设计经验**：logit KL 损失是知识迁移的必需品，追加隐藏状态特征损失（MSE 或余弦）可稳定提升约 1% MMLU。

  - **打包训练简化**：蒸馏时用朴素的全 1 注意力掩码做序列打包，仅牺牲约 1 个 MMLU 点，工程实现简单且效率高。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：紧凑 LLM 部署受内存和延迟限制，知识蒸馏是质量恢复的关键步骤，但训练时教师模型常驻内存、长上下文下 logit 张量导致显存爆炸，使得规模化实验和长上下文修复成本极高。该工作针对这两大瓶颈提出系统性工程方案。

**方法关键点**
- **离线蒸馏**：预先计算教师 top-K（K=100）logit 并缓存，训练时仅读取缓存，教师不出现在循环中，内存和计算量锐减，同时避免重归一化，完整保留截断质量。
- **融合分块 KL 损失**：将输出投影融合进损失，分块处理序列，不实例化完整的词汇维度 logit 张量；前向分块计算 logZ 与稀疏项，反向利用闭式梯度 `∂L/∂z_v = M·q_v - p_v` 重新计算，内存从 O(SBV) 降至 O(SBd)。
- **多实现对比**：全密集 KL、前分块 KL、全分块 KL 保证数学等价性；全分块是唯一使内存随序列长度线性增长的方案。

**关键实验**
- 在 Llama 3.1 8B → 3.2B 学生上，离线蒸馏在线损失完全一致，内存从 103GB 降至 78GB，单步迭代快 29%，吞吐量提升 41%。
- 在 32K 上下文下，密集 KL 需约 250GB（超过 H200 容量），全分块 KL 仅需 128GB，使长上下文训练可行。
- 玩具基准测试：词汇 131K，隐藏维度 4096，序列 256K 时全分块 KL 仅占 11.6GB，比前分块低 11.6 倍，且迭代速度更快。
- 损失消融：仅用中间层特征损失学生崩溃，logit KL 为必要条件；附加隐藏状态损失（MSE）可将 MMLU 从 59.9% 提升至 60.6%。
- 打包序列：全 1 注意力掩码在蒸馏时仅损失约 1 个 MMLU 点，可作为高效默认配置。

**核心结论**：离线 Top-K 缓存与融合分块 KL 的组合使得在单 GPU 上高效训练长上下文紧凑 LLM 成为可能，且不牺牲蒸馏质量。
