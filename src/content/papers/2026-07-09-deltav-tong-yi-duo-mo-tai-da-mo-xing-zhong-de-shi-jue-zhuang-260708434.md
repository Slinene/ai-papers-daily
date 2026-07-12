---
title: 'DeltaV: Thinking with Visual State Updates in Unified Large Multimodal Models'
title_zh: DeltaV：统一多模态大模型中的视觉状态更新推理
authors:
- Pengjie Wang
- Linger Deng
- Zujia Zhang
- Shaojie Zhang
- Zhenbo Luo
- Pei Fu
- Jian Luan
- Xiang Bai
- Yuliang Liu
affiliations:
- Huazhong University of Science and Technology
- MiLM Plus, Xiaomi Inc.
arxiv_id: '2607.08434'
url: https://arxiv.org/abs/2607.08434
pdf_url: https://arxiv.org/pdf/2607.08434
published: '2026-07-09'
collected: '2026-07-12'
category: Multimodal
direction: 视觉更新驱动高效多模态推理
tags:
- Visual Updates
- Token Compression
- Multimodal Reasoning
- TSIM Router
- StructCoT
- ULMM
one_liner: 提出视觉更新范式，增量预测变化令牌替代全图生成，减少55.6%视觉令牌并提升多模态推理3.3%
practical_value: '- 当推荐/Agent系统需序列输出视觉状态（如商品搭配演化、试穿效果步骤），采用增量更新可大幅减少生成token的冗余，直接降低推理延迟与成本。

  - 借鉴TSIM Router思想，在推荐场景的自适应计算中，根据边际增益动态分配视觉生成token预算：复杂变化场景多分配，简单场景早停，提升整体效率。

  - StructCoT数据集构建思路可迁移至电商多模态推理数据准备，通过链式思维引导模型进行多步视觉决策（如商品对比、需求分析），增强推荐可解释性。

  - 55.6%的token减少且性能不降，表明视觉差分编码是移动端或资源受限场景下一种高性价比压缩方案，适合部署轻量级多模态推荐助手。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：统一多模态大模型在推理时通常生成整张图像作为中间视觉状态，导致大量视觉token冗余，且关键状态变化的监督信号被淹没。**方法**：DeltaV提出视觉更新范式，不再生成全图，而是基于历史视觉状态增量预测紧凑的更新令牌，仅捕捉推理步骤间的视觉变化。通过时间相似度路由器（TSIM Router）对齐每步的token预算与变化幅度：当边际重建增益低于阈值时停止分配token，实现自适应压缩。同时构建了StructCoT大规模多模态推理数据集（1.05M样本，44个任务域），提升模型的推理泛化性。**结果**：视觉更新范式平均减少55.6%新生成视觉token，重建保真度不降，多模态推理性能提升3.3%。DeltaV-2B在域内推理评估上超越更大的开源模型8.4%，在外部基准上超越同规模的Qwen3-VL-2B 5.9%。
