---
title: 'FiRE: Enhancing MLLMs with Fine-Grained Context Learning for Complex Image
  Retrieval'
title_zh: FiRE：细粒度上下文学习增强多模态大模型复杂图像检索
authors:
- Bohan Hou
- Haoqiang Lin
- Xuemeng Song
- Haokun Wen
- Meng Liu
- Yupeng Hu
- Xiangyu Zhao
affiliations:
- Shandong University
- City University of Hong Kong
- Harbin Institute of Technology (Shenzhen)
- Shandong Jianzhu University
arxiv_id: '2607.27959'
url: https://arxiv.org/abs/2607.27959
pdf_url: https://arxiv.org/pdf/2607.27959
published: '2026-07-30'
collected: '2026-08-02'
category: Multimodal
direction: 细粒度上下文学习 · 图像检索
tags:
- Fine-Grained
- MLLM
- Image Retrieval
- CIR
- Two-Stage Finetuning
- Dataset Pipeline
one_liner: 提出自动化细粒度五元组数据集构建与两阶段解耦微调，显著提升MLLM零样本复杂图像检索性能
practical_value: '- **自动化细粒度比对数据构建**：通过流水线生成包含图像、细粒度描述、修改文本的五元组，可复用于电商搜索中构建“参考图 +
  修改指令 → 目标商品”的训练数据，改善组合查询效果。

  - **两阶段解耦微调思路**：先让模型学习细粒度上下文推理（理解修改意图），再对齐查询与目标表示，这一策略可迁移到多模态搜索、对话式推荐等任务，先理解用户意图再优化匹配。

  - **轻量级MLLM也能实现强检索**：文中用小型骨干即超越大模型，说明在业务中可通过精细的数据与微调设计，避免依赖超大模型，降低推理成本。

  - **零样本能力直接用于检索重排**：训练后的模型可直接计算查询与候选图像相似度，适用于搜索结果重排序，尤其在长尾查询或组合查询场景下提升相关性。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：多模态大模型（MLLM）在通用图像检索上展现潜力，但在长文本到图像、视觉对话及组合图像检索（CIR）等复杂任务中，现有工作忽略了细粒度上下文建模与解耦微调目标的重要性，限制了检索精度。

**方法**：提出FiRE，包含两个核心贡献：
1. **自动化细粒度五元组数据集构建**：设计流水线，利用现有图像对生成包含（源图像、细粒度描述、目标图像、细粒度描述、修改文本）的五元组，提供丰富上下文信息。
2. **两阶段解耦微调**：第一阶段“细粒度上下文推理微调”让模型学习从源图像、描述与修改文本推断目标图像描述；第二阶段“细粒度检索微调”通过对比学习直接优化查询与目标图像的匹配。两阶段逐步增强上下文理解与查询-目标对齐能力。

**结果**：在5个数据集（涵盖长文本检索、视觉对话检索、CIR等）上，零样本设定下，FiRE大幅超越现有方法，甚至在使用更轻量MLLM（如7B参数）时仍表现出色，验证了细粒度上下文学习与解耦微调的有效性。
