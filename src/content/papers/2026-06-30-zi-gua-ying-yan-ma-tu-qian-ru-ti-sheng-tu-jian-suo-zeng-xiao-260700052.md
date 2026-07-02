---
title: 'AGE: Adaptive-masking for Graph Embedding in Graph Retrieval-Augmented Generation'
title_zh: 自适应掩码图嵌入提升图检索增强生成效果
authors:
- Bao Long Nguyen Huu
- Atsushi Hashimoto
affiliations:
- OMRON Corporation
- OMRON SINIC X Corporation
arxiv_id: '2607.00052'
url: https://arxiv.org/abs/2607.00052
pdf_url: https://arxiv.org/pdf/2607.00052
published: '2026-06-30'
collected: '2026-07-02'
category: RAG
direction: 图检索增强生成对齐 · 自适应掩码预训练
tags:
- GraphRAG
- Self-Supervised Learning
- Graph Embedding
- Adaptive Masking
- Knowledge Graph QA
one_liner: 提出自适应掩码图嵌入AGE，通过可学习节点采样器避开关键节点对齐图与文本特征，显著提升GraphRAG问答准确率。
practical_value: '- 在电商知识图谱问答或商品搜索中，可借鉴AGE的图嵌入对齐方法：用类似文本编码器的Transformer预训练图节点嵌入，与LLM文本空间对齐，提升GraphRAG检索召回。

  - 可学习节点采样器识关键节点：对推荐场景中如品牌、类目等关键实体，自适应避免掩码它们，提高嵌入学习的鲁棒性，适合大规模商品图谱。

  - 非参数搜索组件与冻结LLM结合，无需微调，降低部署成本，适合电商快速迭代和A/B实验。

  - 图数据预处理阶段加入自适应掩码预训练，可作为召回或特征生成步骤，融入现有RAG流程，改善商品关联和语义理解。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：GraphRAG利用图结构化知识增强LLM，但图嵌入与LLM文本特征空间不对齐，尤其对冻结的LLM。现有基于掩码的自监督图预训练方法不加区分地掩码节点，忽略了图中存在关键节点——它们携带主导上下文信息，难以从邻域预测，导致学习低效。

**方法**：提出AGE（Adaptive-masking for Graph Embedding）。采用与文本编码器架构一致的Transformer作为图编码器，在掩码自监督预训练阶段对齐图与文本特征。设计了一个可学习的节点采样器，自动识别关键节点并避免掩码它们，仅对非关键节点进行掩码预测，迫使模型关注更有信息量的重构任务。

**结果**：在四个特性各异的GraphQA基准数据集上，AGE显著提升了基于非参数搜索的GraphRAG方法准确率，证明了其对齐效果和预训练策略的有效性。
