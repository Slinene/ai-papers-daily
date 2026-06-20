---
title: 'SSD: Spatially Speculative Decoding Accelerates Autoregressive Image Generation'
title_zh: SSD：空间推测解码加速自回归图像生成
authors:
- Shilong Xiang
- Zirui Zhang
- Lijun Yu
- Chengzhi Mao
affiliations:
- Rutgers University
arxiv_id: '2606.20543'
url: https://arxiv.org/abs/2606.20543
pdf_url: https://arxiv.org/pdf/2606.20543
published: '2026-06-18'
collected: '2026-06-20'
category: Multimodal
direction: 自回归视觉生成中的并行推测解码
tags:
- Spatially Speculative Decoding
- Autoregressive Image Generation
- Inference Acceleration
- 2D Spatial Locality
- Visual Token Prediction
one_liner: 利用2D空间局部性并行预测相邻token，将自回归图像生成加速13.3倍且质量无损
practical_value: '对于电商/推荐/Agent从业者，该方法可直接迁移到任何自回归生成任务（如生成式推荐中的Semantic ID序列、商品描述、多模态内容生成）：

  - 利用 item 间共现或相似性图谱构建空间/结构化的并行预测分支，将逐 token 生成改为多 token 并发预测，减少解码步数，提升推荐结果生成速度。

  - 工程上可实现类似树形推测解码的验证机制，用大模型一次产出多个候选 token，再由小模型并行验证，保持输出分布一致。

  - 适合对延迟敏感的在线推荐场景，尤其在高分辨率、多模态内容生成（如商品图生成、广告素材合成）中应用，可大幅降低 RTF。

  - 需要预先定义 token 之间的依赖关系（如商品 ID 序列的常见转移模式），可结合 Graph Embedding 或 co-occurrence 矩阵来设计并行预测目标。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：自回归图像生成将2D图像压平为1D token 序列，忽略了视觉信号的局部空间相关性，导致推理时计算瓶颈严重（内存墙）。传统语言模型加速方法（如推测解码、雅可比迭代）未充分利用图像的空间先验。
**方法**：提出**空间推测解码（SSD）**，颠覆逐 token 顺序预测，让模型同时预测当前 token 的右方水平邻居和下方垂直邻居，形成2D网格上的并行预测。通过训练时添加辅助预测头，在推理时生成多分支候选 token，再用验证模型并行校验，保证输出分布不变。
**结果**：在 DPG-Bench 和 GenEval 上，SSD 实现最高 **13.3×** 推理加速，同时生成质量与原始自回归模型相当，证明了尊重视觉几何结构可极大提升计算效率。
