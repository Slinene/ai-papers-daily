---
title: Where Should Optimizer State Live? Tiered State Allocation for Memory-Efficient
  Mixture-of-Experts Training
title_zh: MoE 训练中优化器状态该放在哪里？分层状态分配实现内存高效训练
authors:
- Nuemaan Malik
affiliations:
- Independent Researcher
arxiv_id: '2607.19058'
url: https://arxiv.org/abs/2607.19058
pdf_url: https://arxiv.org/pdf/2607.19058
published: '2026-07-20'
collected: '2026-07-24'
category: Training
direction: MoE 训练内存优化
tags:
- MoE
- optimizer state
- memory-efficient training
- SkewAdam
- tiered allocation
one_liner: 针对 MoE 三种参数群体，差异化分配优化器状态，使内存降至原来的 2.6%，且困惑度更优
practical_value: '- **大规模 MoE 推荐模型训练**：在训练广告/内容推荐的 MoE 模型时，专家层参数通常占 95% 以上，可仅用 factored
  second moment（无 momentum），骨干网络保留动量，大幅降低显存，使单卡训练更大 batch 或更多专家成为可能。

  - **骨干与专家差异化优化**：业务中可借鉴“骨干保留动量、专家不保留动量”的思路，骨干提取通用特征需要稳定收敛，而大量专家可通过轻量状态快速适应不同领域/任务。

  - **路由器仅需精确二阶矩**：推荐 MoE 中路由器通常极小，保持完整 Adam 状态几乎无开销，且对负载均衡有利（论文中负载均衡接近均匀下限）。

  - **从显存到精度无 trade-off**：实验表明分层状态分配不损害精度，甚至更好，可直接迁移到现有 MoE 训练流程，无需担心性能回退。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：MoE 训练中，AdamW 优化器状态（一阶+二阶矩）占内存极大，例如 6.78B 参数模型需 50.6 GB 状态，而权重仅 12.6 GB。且 MoE 三类参数（骨干网络、专家、路由器）量级和梯度特性差异显著，一刀切的优化器状态分配造成浪费。

**方法关键点**：提出 **SkewAdam**，对三类参数使用不同状态：
- 骨干网络（约 5% 参数）：保留 float32 momentum 与 factored 二阶矩，维持稳定学习；
- 专家层（约 95% 参数）：仅用 factored 二阶矩，无 momentum，大幅降低内存；
- 路由器（<0.01% 参数）：保留精确二阶矩，确保路由收敛与负载均衡。
整体优化器状态仅 1.29 GB，为 AdamW 的 2.6%。

**关键结果**：在相同初始化、训练 82M tokens 后，SkewAdam 验证困惑度 108.4，优于 AdamW 的 126.8、Muon 的 120.2、Lion 的 393.7。峰值训练内存从 81.4 GB 降至 31.3 GB，适配 40 GB 单卡。消融表明：分层状态本身即可节省 20× 内存；精度优势来自保留 momentum，但只有与分层结合才无需付出内存代价。
