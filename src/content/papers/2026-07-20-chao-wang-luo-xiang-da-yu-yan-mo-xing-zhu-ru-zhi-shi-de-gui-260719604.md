---
title: Scaling Laws for Hypernetwork-Based Knowledge Injection in Large Language Models
title_zh: 超网络向大语言模型注入知识的规模法则
authors:
- Nischay Dhankhar
- Dos Baha
- Abulhair Saparov
affiliations:
- Nace AI
- Purdue University
arxiv_id: '2607.19604'
url: https://arxiv.org/abs/2607.19604
pdf_url: https://arxiv.org/pdf/2607.19604
published: '2026-07-20'
collected: '2026-07-25'
category: Training
direction: 超网络训练时知识注入 · 规模法则
tags:
- Hypernetwork
- LoRA
- Knowledge Injection
- Scaling Laws
- OOD Generalization
- Multi-hop QA
one_liner: 发现超网络生成 LoRA 适配器进行知识注入的损失、准确率和 OOD 泛化遵循幂律缩放规律
practical_value: '- **超网络生成个性化适配器**：在推荐系统中，可为不同用户群或内容品类训练超网络，动态生成轻量 LoRA 适配器，实现高效、可扩展的定向知识更新，无需重新全量微调。

  - **解耦设计便于工程拆分**：将知识注入容量与主模型能力解耦，允许单独扩展超网络（深度/宽度）而不影响线上推理成本，适合频繁更新的电商知识库（如商品属性、活动规则）。

  - **利用规模法则指导资源分配**：论文给出的预测性规模曲线可作为经验指南，在算力有限时权衡超网络深度、宽度和目标模型大小，快速找到性价比最优的配置。

  - **OOD 泛化优势用于冷启动**：超网络注入在 OOD 场景（未见实体/关系）的缩放指数更陡，可迁移到新品推荐或冷门 category 的知识覆盖，比直接
  LoRA 微调更可靠。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：向 LLM 大规模注入事实知识仍困难，超网络是一种有前景的方法，但其自身的缩放行为尚未被系统研究。本文旨在探究超网络在进行训练时知识注入时，其深度、宽度及目标模型大小如何影响损失、推理准确率和 OOD 泛化。

**方法关键点**：
- 设计解耦架构：超网络仅负责生成一个固定的 LoRA 适配器，该适配器插入冻结的目标模型后使模型能回答特定事实，从而隔离注入容量与模型通用能力。
- 构建 MegaWikiQA 数据集，包含 39 个领域的数千万多跳 QA 对，源自 Wikidata5M，确保大规模可扩展评测。
- 沿超网络深度、宽度和目标模型大小三个轴，系统测量测试损失、多跳推理准确率（严格匹配）及 OOD 泛化，拟合幂律缩放关系。

**关键结果**：
- 所有维度均呈现可预测的幂律缩放规律，损失随参数量增加平滑下降。
- OOD 设置下，超网络方法的缩放指数显著优于 LoRA 微调和全微调，尤其在未见实体和关系上，表明其泛化优势随规模扩大而增强。
- 在最大规模配置下，OOD 准确率提升达 20% 以上，确立了超网络作为可扩展知识注入基石的实证基础。
