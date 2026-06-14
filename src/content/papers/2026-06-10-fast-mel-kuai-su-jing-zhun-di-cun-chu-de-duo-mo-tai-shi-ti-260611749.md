---
title: 'FAST-MEL: A Fast, Accurate, and Storage Efficient Solution for Multimodal
  Entity Linking'
title_zh: FAST-MEL：快速、精准、低存储的多模态实体链接方案
authors:
- Derrien Thomas
- Laurent Amsaleg
- Pascale Sébillot
affiliations:
- Univ. Rennes
- INSA Rennes
- CNRS
- Inria
- IRISA
arxiv_id: '2606.11749'
url: https://arxiv.org/abs/2606.11749
pdf_url: https://arxiv.org/pdf/2606.11749
published: '2026-06-10'
collected: '2026-06-14'
category: Multimodal
direction: 多模态实体链接 · 高效向量索引
tags:
- Multimodal Entity Linking
- Vector Representation
- Efficiency
- Knowledge Base
- Dense Retrieval
one_liner: 提出紧凑固定向量表示，在维持SOTA准确率的同时实现千倍加速与储空间缩减。
practical_value: '- **紧凑的统一表示**：为每个实体生成固定尺寸的多模态向量（文本+视觉），可直接用于电商知识图谱构建，将商品标题、图片与实体快速对齐，无需维护异构特征。

  - **极速检索**：通过向量化索引实现近似最近邻搜索，实体链接速度提升三个数量级，适合大规模商品库的实时实体消歧、搜索词到商品的映射。

  - **存储优化**：存储需求降至最快系统的1/10，适合部署在资源受限的终端或边缘节点，例如移动端商品识别或本地缓存Agent知识。

  - **多模态融合思路**：轻量编码器架构可借鉴至生成式推荐中的Semantic ID生成，将图文特征压缩为固定向量，平衡语义保真度与推理效率。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：现有多模态实体链接（MEL）系统无法同时满足高准确度、计算效率和存储效率——要么准确但慢，要么快但存储开销极大。

方法：FAST-MEL采用轻量编码器，为每个实体或提及生成一个固定尺寸的紧凑向量，统一融合文本与视觉信息。该向量可直接用于高效的近似最近邻检索，无需复杂的跨模态交互。

结果：在两个基准数据集上，链接准确率与当前最佳系统持平；推理速度提升三个数量级（千倍），知识库索引存储需求降低一个数量级（十分之一）。
