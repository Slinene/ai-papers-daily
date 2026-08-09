---
title: 'Domain-Grounded Candidate Selection for Agentic Image Editing: A Shadow Removal
  Case'
title_zh: 面向Agent图像编辑的领域约束候选选择：阴影去除案例
authors:
- Shilin Hu
- Jingyi Xu
- Dimitris Samaras
- Hieu Le
affiliations:
- Stony Brook University
- UNC Charlotte
arxiv_id: '2608.06075'
url: https://arxiv.org/abs/2608.06075
pdf_url: https://arxiv.org/pdf/2608.06075
published: '2026-08-06'
collected: '2026-08-09'
category: Agent
direction: Agent驱动的约束式生成编辑
tags:
- Agentic Pipeline
- Image Editing
- Shadow Removal
- Physics-Informed
- Candidate Selection
- Vision-Language Model
one_liner: 将阴影物理先验注入Agent候选生成-评估-筛选流程，显著减少幻觉并提升编辑可靠性
practical_value: '- 借鉴 Agent 多轮候选生成-评估-筛选流程，用于自动生成商品图文描述或广告文案：先让 LLM 生成若干候选，再用领域评估器（基于规则或轻量分类器）过滤并选择最佳，提升内容质量。

  - 将业务先验（如商品属性准确性、合规性）固化为提示与评估准则，约束生成模型，减少幻觉，类似论文中用物理先验界定“阴影是光照效果”的做法。

  - 引入重试机制与快速失败检测：评估器发现明显违规（如描述与图片不符）时立即重新生成，避免低质输出流入下游。

  - 评估器可采用轻量级方案（如关键词匹配、属性校验）替代复杂模型，在候选筛选阶段快速剔除明显错误，降低整体审核成本。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：商用视觉语言模型具备强大的图像编辑能力，但在阴影去除任务中，直接使用会引发新问题——模型可能篡改场景内容、误将阴影视为材质或物体，产生逼真但物理上错误的编辑。研究旨在探索经典物理先验能否约束生成、减少此类幻觉。

**方法**：提出一个 Agent 候选选择流程。编辑生成器首先依据物理提示（阴影是光照遮挡效应，非结构/材质）生成引导探针；评估器快速检测严重失败并触发重试；随后采样多个候选结果，经过评估器过滤后，选出在阴影去除与场景保留之间取得最佳平衡的结果。整个过程以阴影形成物理知识为提示，使生成和评估更可靠。

**结果**：在 ShadowRemovalRefine 基准上，该方法达到 0.0075 的 CDD（颜色差异度），相比最强现有方法降低至少 47%。结果表明，物理先验并未被大模型取代，仍能有效约束和引导生成式编辑。
