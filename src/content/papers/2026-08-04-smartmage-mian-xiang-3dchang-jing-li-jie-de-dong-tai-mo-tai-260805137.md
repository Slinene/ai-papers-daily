---
title: 'SmartMage: Dynamic Modality Orchestration for 3D Scene Understanding'
title_zh: SmartMage：面向3D场景理解的动态模态编排
authors:
- Yue Zhang
- Yingzhao Jian
- Yunqiu Xu
- Xiaoxiao Sun
- Hehe Fan
affiliations:
- Zhejiang University
- Stanford University
arxiv_id: '2608.05137'
url: https://arxiv.org/abs/2608.05137
pdf_url: https://arxiv.org/pdf/2608.05137
published: '2026-08-04'
collected: '2026-08-09'
category: Multimodal
direction: 动态模态路由与专家混合 · 多模态推理
tags:
- Modality Routing
- Mixture of Experts
- 3D Scene Understanding
- Semantic-Aware
- Multimodal Fusion
- Embodied AI
one_liner: 提出动态模态路由与模态感知专家混合，让MLLM按查询语义自适应选择模态，在3D场景理解中大幅超越固定模态组合
practical_value: '- 电商推荐中不同query依赖不同模态（颜色→图像，尺寸→文本），可借鉴SMART模块动态选择模态特征，降低冗余计算与噪声，提升推理效率。

  - 多模态推荐模型常固定拼接所有模态，改用基于查询语义的自适应模态选择，可避免无关模态干扰，类似特征门控机制。

  - 为购物助手等Agent设计多模态感知时，可引入语义‑模态对齐路由，根据用户意图选择性启用传感器数据，节省资源。

  - MAGE的模态先验引导专家专业化，可迁移到多模态推荐MoE架构中，为不同模态组合分配专家，实现分布式高效推理。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：3D场景问答中，问题类型（颜色、位置、形状等）对模态的需求不同（如RGB vs. 点云），但现有MLLM固定融合所有模态，引入无关模态噪声并浪费计算。需一种能按语义动态选择模态的机制。

**方法**：提出SmartMage，包含两个核心模块：
1. **SMART**（语义引导模态自适应路由）：结合查询语义先验、文本‑模态对齐度与模态质量分数，动态决定每个样本激活哪些模态。
2. **MAGE**（模态感知门控专家）：利用模态先验信息指导专家激活，使不同专家专注于不同模态组合的推理，实现自适应专业化。

整体架构在保持统一多模态大模型的前提下，实现端到端的动态模态编排。

**关键结果**：
- 在5个3D场景理解基准上达到SOTA，包括ScanQA、SQA3D等。
- 在仅RGB视频理解任务上也具备竞争力，证明方法的泛化性。
- 诊断基准ScanFacet按语义类别细粒度分析，展现出清晰的模态‑语义偏好模式，验证了动态路由的有效性。
