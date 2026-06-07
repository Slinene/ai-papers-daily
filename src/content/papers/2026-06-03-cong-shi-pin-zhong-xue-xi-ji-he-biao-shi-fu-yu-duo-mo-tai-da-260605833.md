---
title: Learning Geometric Representations from Videos for Spatial Intelligent Multimodal
  Large Language Models
title_zh: 从视频中学习几何表示赋予多模态大模型空间智能
authors:
- Haibo Wang
- Lifu Huang
affiliations:
- University of California, Davis
arxiv_id: '2606.05833'
url: https://arxiv.org/abs/2606.05833
pdf_url: https://arxiv.org/pdf/2606.05833
published: '2026-06-03'
collected: '2026-06-07'
category: Multimodal
direction: 多模态大模型空间推理 · 视频几何表示
tags:
- MLLM
- 3D Geometry
- Video Representation
- Spatial Intelligence
- Knowledge Distillation
one_liner: GeoVR框架通过2D视频蒸馏3D几何知识，重塑MLLM内部表示以增强空间感知
practical_value: '- **利用预训练3D模型蒸馏，无需3D数据**：对于电商中的3D商品展示、虚拟试穿等场景，可借鉴GeoVR的蒸馏范式，通过现有3D模型（如DUSt3R）从商品视频中提取几何知识，注入2D视觉模型，避免昂贵3D标注。

  - **多目标几何约束增强空间一致性**：四个互补目标（相机位姿、深度图、公制尺度、多尺度特征对齐）可迁移到物品视频理解任务，例如从商品旋转视频中联合优化，提升尺寸估算、空间关系推理的可靠性。

  - **解耦微调策略，低成本提升现有模型**：GeoVR仅微调视觉编码器，冻结LLM，这种做法可复用到推荐系统的视频理解组件中，在不大幅增加训练成本的前提下增强物品的空间表示。

  - **为虚实融合场景提供基础**：在AR购物、虚拟空间布局推荐等Agent任务中，空间智能是核心瓶颈，GeoVR的表示重组思路启发我们如何从大量2D交互视频中学习稳定的几何先验。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：多模态大模型（MLLM）虽强于2D语义，但缺乏内禀的3D感知，导致视频帧间几何与空间一致性缺失。现有方法或依赖稀缺的3D标注数据，或仅表面特征混合，无法真正重塑模型的表示空间。  
**方法**：提出GeoVR，一种纯2D视频序列驱动的几何表示学习框架。它从预训练3D基础模型蒸馏几何知识，通过四个互补目标重塑MLLM内部潜在空间：(1) 估计帧间相机位姿，捕捉视角动态；(2) 回归密集深度图，锚定物理距离；(3) 预测公制尺度因子，实现真实世界校准；(4) 蒸馏多尺度3D特征，对齐中间特征空间。训练时冻结LLM部分，仅微调视频编码器。  
**结果**：在BLINK、MMVP、GeneC-Spatial等多个空间推理基准上取得SOTA，证明了该范式能有效赋予基础模型空间智能。
