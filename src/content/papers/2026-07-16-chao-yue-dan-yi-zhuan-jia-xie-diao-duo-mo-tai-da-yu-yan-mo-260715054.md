---
title: 'Beyond Single Expert: Harmonizing Diverse Visual Priors in MLLMs for Spatial
  Understanding'
title_zh: 超越单一专家：协调多模态大语言模型中的多样化视觉先验以增强空间理解
authors:
- Xiao Lin
- Xiaohu Huang
- Kai Han
affiliations:
- The University of Hong Kong
arxiv_id: '2607.15054'
url: https://arxiv.org/abs/2607.15054
pdf_url: https://arxiv.org/pdf/2607.15054
published: '2026-07-16'
collected: '2026-07-19'
category: Other
direction: 多模态空间理解 · 多先验融合
tags:
- Multimodal LLM
- Spatial Reasoning
- Prior Fusion
- Efficient Proxy
- Dynamic Fusion
one_liner: 提出ViPS框架，通过高效代理和动态融合将多个视觉模型的互补先验集成到MLLM中，显著提升空间推理性能
practical_value: '- 可借鉴多先验融合思想：在电商多模态商品理解中，同时接入多个视觉模型（如CLIP、DINOv2、SAM）提取互补特征，通过动态门控加权融合，提升商品属性识别和空间关系理解。

  - 高效代理设计可降低线上成本：使用轻量级学生模型离线预生成多种先验特征，避免每次推理都调用重模型，适合推荐系统的大规模商品库特征提取。

  - 动态融合机制适用于推荐多信号源：将用户行为序列、商品图像、文本描述等视为不同模态先验，通过上下文感知的融合模块（如注意力加权）注入推荐模型，增强冷启动物品表征。

  - 多专家先验协调思路可迁移到Agent决策：在搜索推荐Agent中，不同模型（如召回、排序、过滤）给出各自的候选，利用动态融合策略综合多路信号，提升最终决策质量。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有MLLMs通常仅依赖一个外部编码器（如VGGT）注入空间先验，但不同视觉基础模型（如Geometric Encoder、CLIP等）提供互补的信息，单一模型无法覆盖各类空间任务的需求。该工作首先揭示当集成多个基础模型时，不同先验对不同任务各有助益，因此需要一种机制来高效融合多源先验。

**方法**：提出ViPS框架，包含两个核心组件：1）**高效先验代理**（Efficient Prior Proxy），通过轻量级代理模型在不显著增加推理开销的前提下生成多个基础模型的视觉先验特征；2）**动态先验融合**（Dynamic Prior Fusion），设计一个上下文感知的融合模块，根据输入图像和任务自适应地加权、整合来自不同代理的先验信息，并将其注入MLLM的中间层。

**结果**：在多个复杂空间推理和3D空间理解基准（如SpatialBench、3D-QA等）上，ViPS全面超越以往单一专家方法，取得了新的SOTA性能，验证了多先验协调的有效性。
