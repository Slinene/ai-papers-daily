---
title: Semantic Generative Tuning for Unified Multimodal Models
title_zh: 语义生成调优：统一多模态模型的协同训练范式
authors:
- Songsong Yu
- Yuxin Chen
- Ying Shan
- Yanwei Li
affiliations:
- Shanghai Jiao Tong University
- Tencent ARCLab
arxiv_id: '2605.18714'
url: https://arxiv.org/abs/2605.18714
pdf_url: https://arxiv.org/pdf/2605.18714
published: '2026-05-17'
collected: '2026-05-20'
category: Multimodal
direction: 统一多模态模型 · 生成代理任务训练
tags:
- Semantic Generative Tuning
- Unified Multimodal Models
- Image Segmentation
- Generative Proxy
- Multimodal Alignment
one_liner: 以图像分割为生成代理任务，对齐统一多模态模型的理解与生成表征空间
practical_value: '- 电商场景中可借鉴“生成代理任务”思想，例如用商品分割图作为监督信号，同时提升视觉理解（属性识别）与生成（背景替换/风格迁移）质量

  - 对于生成式推荐，可设计语义生成代理（如品类层级结构预测）来统一商品序列理解与生成式版面布局，避免表征割裂

  - 高层语义任务（分割）比低层纹理任务更有效，启示我们在多模态对齐时优先使用结构性强标注（如实体分割），而非像素级重建

  - 机制分析显示SGT能改善特征线性可分性和注意力分配，可在跨模态推荐模型的训练中引入类似辅助任务，强制模型学习更解耦、可解释的特征'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有统一多模态模型（UMM）将视觉理解（稀疏文本信号）与生成（密集像素目标）分开训练，导致表征空间不对齐，二者无法互相增强。本文首次系统研究生成式后训练，意图用层次视觉任务作为生成代理来弥合隔离。

**方法关键点**：通过实证发现，高层语义任务（特别图像分割）优于低层纹理任务，因为分割提供结构语义，能同时增强感知能力和生成布局保真度。基于此提出语义生成调优（SGT），将分割作为生成代理，使模型在对分割掩码的生成中学习到对齐的多模态表征。机制分析证实SGT提升了特征的线性可分性，优化了视觉-文本注意力分配。

**关键结果数字**：在多个主流基准上，SGT一致提升了多模态理解（如VQA准确率）和生成保真度（如FID指标），且分割任务本身的质量也得到改善。
