---
title: Variable-Width Transformers
title_zh: 可变宽度 Transformer
authors:
- Zhaofeng Wu
- Oliver Sieberling
- Shawn Tan
- Rameswar Panda
- Yury Polyanskiy
- Yoon Kim
affiliations:
- MIT
- MIT-IBM Watson AI Lab
arxiv_id: '2606.18246'
url: https://arxiv.org/abs/2606.18246
pdf_url: https://arxiv.org/pdf/2606.18246
published: '2026-06-15'
collected: '2026-06-17'
category: LLM
direction: Transformer 架构优化 · 宽度缩放
tags:
- Transformer
- Architecture
- Scaling
- Width
- KV Cache
- FLOPs
one_liner: 提出 × 形瓶颈架构，中间层窄、两端宽，同等参数量下性能更优且推理成本更低
practical_value: '- 将瓶颈结构引入大模型，可减少推荐/搜索系统中 LLM 的显存和计算开销，尤其对需保留 KV cache 的在线服务有利

  - 无需额外参数的残差维度映射方法可直接复用到现有 Transformer 推荐模型（如 SASRec），通过非均匀宽度提升效率

  - 对于 Agent 中多次调用 LLM 的场景，可降低单次推理延迟与成本，加速多步决策

  - 提示我们在设计生成式推荐模型时，不必每层等宽，中间层适当缩减可兼顾容量与效率'
score: 7
source: huggingface-daily
depth: abstract
---

动机：传统 Transformer 每层宽度固定，忽略了不同深度的计算角色差异，导致资源分配不够高效。  
方法：提出 ×-former 架构，保持首尾层宽度较大，中间层宽度收窄，形成瓶颈形状；通过无参数的残差重缩放机制（上下采样）保证维度对齐，不额外增加可学习参数。  
实验：在 200M～2B 参数的稠密解码器模型及 3B 参数 MoE 模型上验证，与等参数量的均匀宽度基线相比，语言建模损失持续改善；拟合损失匹配的缩放曲线下，训练 FLOPs 减少 22%，KV cache 内存和 I/O 开销降低 15%；分析表明瓶颈结构产生的残差流表示具有质性差异。  
结论：非均匀宽度分配能实现更资源最优的语言模型缩放。
