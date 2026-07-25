---
title: 'FVAttn: Adaptive Sparse Attention with Runtime Load Balancing for Video Generation'
title_zh: FVAttn：视频生成的自适应稀疏注意力与运行时负载均衡
authors:
- Hao Liu
- Chenghuan Huang
- Ye Huang
- Zhiying Wen
- Hao Liu
- Mohan Zhang
- Chen Li
- Ziyang Ma
- Jing Lyu
- Jiangsu Du
affiliations:
- 中山大学
- Tencent Inc. (WeChat HPC)
- Tencent Inc. (WeChat Vision)
- 北京大学
arxiv_id: '2607.16190'
url: https://arxiv.org/abs/2607.16190
pdf_url: https://arxiv.org/pdf/2607.16190
published: '2026-07-16'
collected: '2026-07-25'
category: Other
direction: 分布式推理·稀疏注意力负载均衡
tags:
- sparse attention
- load balancing
- sequence parallelism
- video DiT
- inference optimization
one_liner: 提出训练无关的自适应稀疏注意力系统，通过运行时头迁移与空闲填充解决多GPU序列并行的负载不均，推理加速超2倍
practical_value: '- 自适应稀疏中的 `Top-p + Top-k 地板` 组合策略：确保每个注意力头至少保留 k 个高相关 token，避免完全稀疏导致的训练/推理不稳定，在
  LLM 长上下文推荐对话或 Agent 记忆检索时可借鉴此安全机制。

  - 运行时负载均衡通过 P2P 迁移少量“重头”到轻载 GPU，这对多 GPU 部署推荐模型（如生成式推荐、多模态理解）时的序列并行头负载不均问题有直接参考价值，可降低栅极延迟。

  - `Slack-Aware Sparse Augmentation` 利用非关键路径 GPU 的空闲时间计算额外高价值块，这种“空闲填充”思路可迁移到分布式
  Agent 流水线调度，在等待 I/O 或其他 Agent 结果时执行预取或候选评分。

  - 将稀疏计算与负载均衡、通信重叠结合的整体系统设计，展示了在工业级推理服务中如何兼顾精度与吞吐，推荐系统从业者可将类似思想用于大规模模型的多路召回或多专家（MoE）推理的负载均衡。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：视频扩散 Transformer（DiT）的推理瓶颈在于长时空序列的自注意力计算（占推理时间 74.1%）。训练无关的自适应稀疏注意力（如 Top-p 路由）可降低成本，但在多 GPU 序列并行下，不同注意力头的负载严重不均，形成拖慢整体的“栅极问题”。

**方法**：提出了 FVAttn，一种训练无关的分布式稀疏注意力系统。前端采用 Top-p 路由结合 Top-k 安全地板，并组织时空块，生成稀疏掩码后在运行时修复；核心创新是 *运行时负载均衡*，通过 P2P 通信将少数重头迁移到轻载 GPU，缩短关键路径；利用 *Slack-Aware 稀疏增强*，在非关键 GPU 的空闲时段填充高价值计算块；同时用重叠隐藏调度与迁移开销。

**结果**：在步蒸馏 Wan2.2 I2V 模型上，负载不均衡系数从 1.34 降至 1.08；注意力计算相比 FlashAttention 加速 4.41 倍；DiT 整体推理加速 2.02–2.11 倍，且视频质量无明显下降。
