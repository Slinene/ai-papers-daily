---
title: Orthogonally Mixed Sign Coding with Progressive Residual Refinement for Transformer
  Weight Compression
title_zh: 正交混合符号编码与渐进残差细化用于 Transformer 权重压缩
authors:
- Anindya Roy Chowdhury
- Atanu Barai
- Nandakishore Santhi
affiliations:
- Los Alamos National Laboratory
arxiv_id: '2611.31089'
url: https://arxiv.org/abs/2611.31089
pdf_url: https://arxiv.org/pdf/2611.31089
published: '2026-11-23'
collected: '2026-11-24'
category: LLM
direction: LLM 权重压缩 · 正交混合残差符号量化
tags:
- LLM quantization
- PTQ
- orthogonal mixing
- residual coding
- weight compression
one_liner: 训练无关的正交混合残差符号量化，在 GPT-2 与 Llama-3 上以低比特保持接近全精度的困惑度
practical_value: '- 在需要部署 LLM 做特征抽取、reranker 或 Agent 推理时，可尝试该训练无关、无需校准集的量化方案，避免线上业务数据收集和校准流程；其渐进残差结构允许按存储预算灵活选择阶段数，直接控制精度-存储
  trade-off。

  - 正交混合（随机旋转）促进权重残差分布高斯化这一 trick 可迁移到其他 PTQ 方法：对 Transformer 权重先做随机正交变换再量化，能改善符号编码或标量量化的有效性，尤其适合注意力层和
  MLP 投影中的 outlier 分布。

  - 若业务模型对某些层的激活分布敏感，可参考其 activation-aware scaling 思路，在量化时引入少量校准统计提升输出保真度；工程上需权衡额外统计开销与精度收益，尤其在线推荐模型更新频繁时。

  - 方法无需学习码本或 CDF 估计，实现简单，适合快速接入现有推理框架；但论文仅在 GPT-2 和 Llama-3 上验证，迁移到推荐系统常用的小型 Transformer
  或混合架构前需自行验证效果。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 量化可降低存储和推理内存，但低比特下预测保真度下降明显，现有 PTQ 方法常依赖校准集、经验 CDF 或复杂优化，部署成本高。

**方法关键点**：提出训练无关、CDF-free 的渐进残差符号量化框架。核心利用随机正交混合（randomized orthogonal mixing）将 Transformer 权重残差变换为近似高斯分布，从而提升基于符号重建的精度；每阶段独立归一化残差并解析校准重建，逐步恢复量化误差。无需学习码本、经验 CDF 或 trellis 优化，支持灵活存储-保真度权衡。

**关键结果**：在 GPT-2 Large 和 Llama-3-8B 上评估注意力与 MLP 投影，五残差阶段联合量化后，困惑度分别为 32.16 和 12.73，对比全精度 29.89 和 11.07，接近基线。消融显示正交混合相比 identity-based sign coding 显著改善重建，activation-aware scaling 提升输出保真度，降低统计精度可减少存储开销且困惑度退化可忽略。与传统量化器比较验证了渐进保真度恢复和存储-质量/运行时间权衡。
