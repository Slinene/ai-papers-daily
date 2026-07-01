---
title: 'One Forward Beats Two: InnerZoom for Accurate and Efficient GUI Grounding'
title_zh: 一次前向胜过两次前向：InnerZoom实现准确高效的GUI定位
authors:
- Chen Liu
- Ling Chen
- Hanzhang Zhou
- Liangyu Chen
- Chenglin Cai
- Xin Yu
- Steven Hoi
- Yue Wang
affiliations:
- Tongyi - MAI
arxiv_id: '2606.30084'
url: https://arxiv.org/abs/2606.30084
pdf_url: https://arxiv.org/pdf/2606.30084
published: '2026-06-28'
collected: '2026-07-01'
category: Agent
direction: 单次前向内部缩放引导解码提升GUI定位
tags:
- GUI Grounding
- InnerZoom
- MLLM
- Cross-layer Evidence
- Decoding Efficiency
one_liner: 单次前向内部缩放桥接跨层证据，超越需两次前向的ZoomIn，同时降延迟降计算量
practical_value: '- 构建电商自动操作Agent时，可直接用InnerZoom替代ZoomIn，只需一次前向即可获得高精度UI元素定位，端到端延迟降低30%+，适合在线或低资源环境。

  - 该方法的核心思想“跨层证据桥接”可迁移到推荐系统的生成式推荐中：将中间层强语义特征显式保留并注入后续解码步骤，提升生成式ID或序列的准确率。

  - 实现上，InnerZoom无需修改基础MLLM架构，仅需设计轻量证据提取与精炼模块，训练成本低，可在现有视觉-语言模型上微调即用，适合需要快速落地GUI自动化场景。

  - 对于多模态商品图片理解任务，若需定位商品区域或关键属性位置，可借鉴内部缩放思路，将区域感知特征跨层传递，增强定位或属性预测的精度。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：MLLM用于GUI定位时，自回归生成坐标的过程会丢失中间解码层已涌现的目标区域意识。现有ZoomIn方法通过外部裁剪重跑前向改善定位，但带来加倍的计算与延迟。希望保留二次缩放的精度，同时避免额外开销。

**方法关键点**：提出InnerZoom，在单一前向过程中实现内部缩放。核心是跨层证据桥接：首先在原始前向的中间层提取与目标区域相关的线索，压缩为紧凑的跨层证据状态；随后在深层解码时，持续保留、精炼该状态并重新注入解码过程，引导坐标的预测。具体结构包括证据提取（基于注意力或隐藏状态）、证据精炼（轻量Transformer或交叉注意力）和证据注入（加性或门控融合）。这样，相当于以极低的内部状态传递替代了外部裁剪与二次前向。

**关键结果**：InnerZoom-4B在六个GUI grounding基准上达到SOTA：OSWorld-G 64.7、UI-Vision 40.2、OSWorld-GR 73.1，分别较此前最佳提升4.1、3.2、2.9点。在可控4B设置下，比SFT+RL基线平均高5.3点，比两阶段ZoomIn高出1.3点；同时端到端延迟最多降低31.8%，TFLOPs减少约29%。
