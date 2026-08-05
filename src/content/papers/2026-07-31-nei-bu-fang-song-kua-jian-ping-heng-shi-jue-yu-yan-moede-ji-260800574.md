---
title: 'Relax Within, Balance Across: Geometry-Guided Load Balancing for Vision-Language
  Mixture-of-Experts'
title_zh: 内部放松，跨间平衡：视觉语言MoE的几何引导负载均衡
authors:
- Ziang Wu
- Peng Jin
- Qishen Yin
- Munan Ning
- Hao Li
- Peizhen Zhang
- Li Yuan
affiliations:
- Peking University
- Peng Cheng Laboratory
- Qwen Team
- Sun Yat-sen University
arxiv_id: '2608.00574'
url: https://arxiv.org/abs/2608.00574
pdf_url: https://arxiv.org/pdf/2608.00574
published: '2026-07-31'
collected: '2026-08-05'
category: Training
direction: 多模态MoE负载均衡优化
tags:
- Multi-modal MoE
- Load Balancing
- ReBA
- Vision-Language
- Auxiliary Loss
one_liner: 提出ReBA，通过模态分离与图像内放松路由，解决视觉语言MoE在不同token混合下的负载失衡
practical_value: '- 多模态推荐模型中，图像/文本token数量随请求动态变化时，可借鉴ReBA对图像和文本分别计算负载均衡损失，避免跨模态误差抵消。

  - 对于图像特征，按源图像分组，每个图像内均匀路由（Relax Within），能有效抑制分辨率变化导致的负载波动，适合电商商品图片处理。

  - 利用“固定负载曲线”离线分析模型在不同token混合比例下的负载表现，提前预估推理瓶颈，指导工程部署资源分配。

  - 实现轻量：只需在路由器添加模态标识和图像分组，不改变主干结构，易于在现有MoE推荐模型上试验。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：视觉语言MoE推理时，批次中图像分辨率、数量和文本长度变化导致token混合比例动态变化。传统token级Switch辅助损失（Std-Aux）仅在特定混合下平衡，不同混合下图像与文本负载误差可互相抵消，造成实际推理中负载失衡可达5倍以上。

**方法**：首先固定图像与文本负载分布，推导出负载随token混合比例变化的精确曲线，发现图像-文本负载差距控制混合敏感性。进一步分析路由器输入结构，观察到图像与文本token占据不同区域，且同一图像内visual token强聚集。据此设计ReBA：1) 模态分离，对图像和文本分别施加负载均衡项，避免误差抵消；2) 图像内放松路由，对每个源图像的所有token采用等权重路由（Relax Within），跨图像则均匀分配（Balance Across）。

**结果**：在四个分割主干上，ReBA在所有benchmark输入上降低了负载，平均任务准确率与Std-Aux持平。在分辨率与tiling变化范围下，ReBA显著降低最差物理负载与平均负载，提升推理稳健性。
