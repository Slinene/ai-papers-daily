---
title: 'Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention
  for Video Generation and World Models'
title_zh: 划分支持集并重构残差：面向视频生成与世界模型的训练-free稀疏注意力
authors:
- Pardis Taghavi
- Reza Langari
- Gaurav Pandey
affiliations:
- Texas A&M University
arxiv_id: '2608.18484'
url: https://arxiv.org/abs/2608.18484
pdf_url: https://arxiv.org/pdf/2608.18484
published: '2026-08-18'
collected: '2026-08-25'
category: Other
direction: 训练-free 稀疏注意力加速视频 Transformer
tags:
- Sparse Attention
- Training-Free
- Video Generation
- World Models
- Residual Reconstruction
- Inference Acceleration
one_liner: 训练-free稀疏注意力，通过响应耦合分区与探针拟合残差重构，在视频生成和世界模型中保持质量并加速1.48-2.61倍
practical_value: '- 对长序列用户行为建模的 Transformer 推理，可借鉴训练-free 稀疏注意力：先按 query 与 key 的响应相关性做块划分，再用少量
  probe query 精确计算残差，用仿射校正补偿被跳过的注意力，避免重新训练。

  - 适合已有预训练电商/推荐大模型在线上做低成本加速，不需改权重，直接以更低的 executed-pair density（如 22-26%）换取 1.5-2.6x
  端到端吞吐提升。

  - 探针拟合成本低、效果贡献大，可以在工程实现中作为轻量残差模块嵌入，优先保证 probe 数量和选择策略，而不是复杂的分区方法。

  - 若有多头注意力且头间分布差异明显，可做 head-dependent 稀疏策略，本方法中的响应耦合分区思路可迁移到不同 head 和长序列场景。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：视频生成与世界模型处理长时空 token，二次注意力成为推理瓶颈。预训练视频 DiT 有结构化注意力集中，但行级集中不直接给出可执行的块稀疏算子，且保留注意力质量不代表 softmax 后误差。

方法关键点：
- SparsePR 组合 Response-Coupled Partitioning 与 Probe-Fitted Residual Reconstruction。
- 采样 query-key 响应构成配对 K/V 组，用质心诱导 query-response 坐标实现共享路由，使同路由 query 的支持集更可预测。
- 用小部分精确 query 行在 probe 残差观测到的输出子空间内，对稀疏输出做 call-specific 仿射校正，重构被跳过的交互。

结果：
- 在四个异构视频生成与世界模型上一致降低注意力重建误差。
- 消融：probe fitting 贡献大部分误差降低；response-coupled partitioning 降低 hard-drop 误差，并在有限 probe 预算下改善重建。
- 保持生成质量，实现 22.0-26.0% 的 executed-pair density，端到端加速 1.48x-2.61x。
