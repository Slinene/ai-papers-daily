---
title: 'GeoPair: Geometry-Preserving Cross-Layer Factorization for Training-Free Transformer
  Compression'
title_zh: GeoPair：保持几何的跨层分解实现无训练 Transformer 压缩
authors:
- Baher Mohammad
- Ammar Ali
- Stamatios Lefkimmiatis
affiliations:
- MWS AI
- ITMO University
arxiv_id: '2609.25963'
url: https://arxiv.org/abs/2609.25963
pdf_url: https://arxiv.org/pdf/2609.25963
published: '2026-09-21'
collected: '2026-09-25'
category: Other
direction: Transformer 压缩 · 跨层矩阵分解
tags:
- Transformer Compression
- Matrix Factorization
- Cross-Layer Redundancy
- Post-Training
- Structured Sparsity
- Training-Free
one_liner: 提出训练无关的跨层共享字典分解框架 GeoPair，通过优化跨层配对保持各层激活几何，实现高效 Transformer 压缩
practical_value: '- 可直接用于电商/广告场景中 Transformer 塔（如用户行为序列建模、多模态编码器）的后训练压缩：用校准数据离线优化跨层权重配对，无需微调，适合快速上线低延迟推理。

  - 跨层共享字典分解能显著降低大模型部署内存，尤其适合多任务或多模态推荐模型中共用 backbone 的场景；比起逐层独立分解，它利用层间冗余，参数效率更高。

  - 结构化稀疏与共享字典联合优化，能同时减少参数量和计算量，对移动端或边缘推理有直接工程价值。

  - 方法论上可迁移：不要简单按相邻层或启发式层级合并，而是用优化目标显式保持每层激活几何，等价于用校准数据做结构搜索，在压缩与精度之间取得更好平衡。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：Transformer 深层网络存在跨层冗余，但现有后训练压缩通常逐层独立处理权重矩阵，或采用启发式分组策略，忽略不同层激活分布的几何差异，导致精度损失或压缩率受限。

**方法关键点**：论文提出 GeoPair，一个训练无关的压缩框架。它串行优化两个环节：跨层权重配对与共享字典分解。首先基于校准数据，识别结构兼容的投影层并配对，而不是强制相邻层共享基；然后在共享字典上学习各层专属系数，从而保持每层独特的激活几何。该方法与结构化稀疏结合，形成高效的权重分解表示，全程无需反向传播或微调，通过可收敛的优化过程替代人工工程策略。

**关键结果**：在多种架构、规模和模态（语言、视觉、生成任务）上取得 SOTA 效果，一致优于独立的逐层结构化分解以及基于启发式分组的成对权重分解方法，证明优化驱动的跨层共享字典能显著降低存储与计算开销，同时保持功能保真度。
