---
title: 'Covering the Unseen: Information Demand Coverage Optimization for Retrieval-Augmented
  Generation'
title_zh: 覆盖未见信息：面向RAG的信息需求覆盖优化
authors:
- Bingxue Zhang
- Jianying Jia
- Feida Zhu
affiliations:
- University of Shanghai for Science and Technology
- Singapore Management University
arxiv_id: '2606.29328'
url: https://arxiv.org/abs/2606.29328
pdf_url: https://arxiv.org/pdf/2606.29328
published: '2026-06-28'
collected: '2026-06-30'
category: RAG
direction: RAG 上下文选择覆盖优化
tags:
- RAG
- Context Selection
- Submodular Optimization
- Sinkhorn-Wasserstein
- Information Coverage
- Diverse Sub-queries
one_liner: 将RAG上下文选择建模为信息需求覆盖优化，通过子查询和Sinkhorn-Wasserstein实现多维需求平衡覆盖
practical_value: '- **复杂查询的多维覆盖**：对于电商搜索中的多意图查询（如“高性价比户外便携蓝牙音箱”），可借鉴生成多样化的子查询（“防水”、“长续航”、“轻便”、“音质好”），并加权，以确保召回的商品列表覆盖所有关键属性，避免
  top-k 相似度排序导致的单一维度过拟合。

  - **即插即用的上下文选择层**：方法无监督、无需训练，且与检索器无关，可直接嵌入现有的 RAG pipeline（如客服问答、推荐理由生成），在检索后增加一个覆盖优化步骤，用次模函数选择互补的文档组，提升答案的全面性。

  - **利用次模函数平衡覆盖**：采用需求加权的设施选址目标，借助贪心算法（1-1/e 近似）选择上下文，工程实现可参考 Sinkhorn-Wasserstein
  距离作为边际增益的快速近似，计算开销可控，适合在线服务。

  - **结构性限制的揭示**：证明单点查询邻近性评分器无法覆盖多模态需求，这提醒从业者在复杂查询场景下（如 Agent 的多步推理、多面商品推荐），不应仅依赖向量相似度排序，而需引入覆盖多样性的选择机制。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：传统 RAG 将用户查询压缩为单一向量，导致复杂查询（多跳、模糊意图）的 top-k 上下文选择只偏重某个语义维度，忽略关键子问题。

**方法**：GeoRAG 把上下文选择重新定义为信息需求覆盖优化。首先生成多样化的子查询，并通过反向验证为每个子查询分配质量权重，构建多维需求分布。然后选择文档集，最小化该需求分布与所选文档覆盖之间的 Sinkhorn-Wasserstein 距离。目标函数是需求加权的设施选址函数，满足单调次模性，可用贪心算法获得 1-1/e 近似。实际实现使用基于 Sinkhorn 的边际增益替代，避免精确计算。方法完全不需训练，与底层检索器解耦。

**结果**：在六个开放域 QA 基准上，精确匹配（EM）比 top-k 截断提升 +6.5 至 +7.5 分，在 HotpotQA 和 ASQA 上达到 +9.7，显著优于 MMR、DPP、BGE-Reranker、SMART-RAG 和 AdaGReS 等强基线。性能增益在不同上下文预算和子查询生成器下保持稳定，证实了覆盖建模的有效性。
