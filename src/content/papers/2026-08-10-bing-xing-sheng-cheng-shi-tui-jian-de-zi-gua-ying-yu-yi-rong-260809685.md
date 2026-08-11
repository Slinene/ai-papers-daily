---
title: Adaptive Semantic Capacity Allocation for Parallel Generative Recommendation
title_zh: 并行生成式推荐的自适应语义容量分配
authors:
- Chenxi Li
- Yuchen Lu
- Xu Yang
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- University of the Chinese Academy of Sciences
arxiv_id: '2608.09685'
url: https://arxiv.org/abs/2608.09685
pdf_url: https://arxiv.org/pdf/2608.09685
published: '2026-08-10'
collected: '2026-08-11'
category: GenRec
direction: 生成式推荐 · 自适应语义ID
tags:
- Semantic ID
- Parallel Generation
- Adaptive Capacity Allocation
- Generative Recommendation
- Product Quantization
- Recommendation Efficiency
one_liner: 提出自适应分配语义槽的码本比特，动态决定ID长度与码本大小，提升并行生成式推荐准确性
practical_value: '- 构建商品语义ID时避免固定每个槽的码本大小，利用信息分布差异，将更多比特分配给区分度更高的维度（如重要品类），去除无信息槽，节省计算并提升效果。

  - 贪心分配比特的方法简单有效，只需维护重建损失表，在一次离线过程中即可完成自适应分配，适合工程化。

  - 自适应ID长度使模型在线推理仍保持并行一步预测，无需束搜索，延迟可控，适合高吞吐的电商搜索推荐场景。

  - 思路可迁移到其他多目标/多模态特征编码：对用户行为序列的多维量化、多模态特征融合的码本设计均可用容量分配避免冗余。'
score: 10
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
现有基于语义ID的生成式推荐普遍手动固定语义槽数量和各槽码本大小，假设所有子空间需要相等表示容量。但实验发现，简单增加均匀分配的语义槽并不能单调提升推荐效果，且投影后子空间的信息分布（能量）高度不均衡。这促使我们重新审视语义ID构建：应将ID结构视为一个容量分配问题，而非固定超参数。

## 方法
提出 **InforID**，一个轻量、可插拔的自适应语义目标构建框架：
1. **候选语义槽**：从物品内容（如文本）得到连续表示，投影并均分成 𝑀 个子空间作为候选槽。
2. **自适应容量分配**：给定总比特预算 𝐵，贪心地每次分配 1 bit 到使子空间重建损失降低最多的槽上，最终得到各槽的非负比特数 𝑏𝑗 及对应码本大小 𝐾𝑗 = 2^𝑏𝑗。
3. **ID确定与预测**：𝑏𝑗=0 的槽被移除，剩余槽构成有效语义ID；每个保留槽使用一个槽特定的预测头（输出维度 𝐾𝑗），所有槽并行预测，解码仍为一步并行。
4. **训练与检索**：多令牌预测损失优化槽条件概率，检索时用对数概率和打分。

## 关键实验
在四个亚马逊公开评测集（Sports、Beauty、Toys、CDs）上进行评估，对比SASRec、VQ-Rec、TIGER、RPG等基线。使用相同物品嵌入和并行预测骨架下，仅替换ID构建方式：
- **总体性能**：InforID 在 Recall/NDCG@5,10 上全面优于或持平 RPG（并行基线），例如 Sports 上 N@10 从 0.0263 提升至 0.0279，Toys 上 N@10 从 0.0490 提升至 0.0506。
- **消融分析**：统一比特预算下，InforID 的重建损失最低（相对PQ损失：Sports 0.583 vs OPQ 0.775），NDCG@10 同时最优，验证了自适应分配的有效性。
- **预算敏感性**：比特预算增加带来饱和收益，表明容量存在边际效用递减。

## 核心结论
语义ID的结构不应是手动固定的均匀配置，而应根据数据动态确定：自适应分配码本容量能更高效地利用预测能力，在相同计算约束下大幅提升推荐质量。
