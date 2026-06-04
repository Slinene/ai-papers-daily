---
title: 'ANN Search: Recall What Matters'
title_zh: 近似最近邻搜索：召回并非一切，距离比才是关键
authors:
- Dimitris Dimitropoulos
- Nikos Mamoulis
affiliations:
- University of Ioannina & Archimedes, Athena RC
arxiv_id: '2606.04522'
url: https://arxiv.org/abs/2606.04522
pdf_url: https://arxiv.org/pdf/2606.04522
published: '2026-06-03'
collected: '2026-06-04'
category: Eval
direction: ANN 检索质量评估：从重叠度到距离比
tags:
- ANN
- Recall@k
- 1-Ratio@k
- evaluation metric
- RAG
- vector search
one_liner: 提出用逆近似比 1/Ratio@k 替代 Recall@k 评估 ANN 质量，更真实反映下游效用且节省计算
practical_value: '- 在生产 ANN 召回评估中，用 **1/Ratio@k** 代替 Recall@k 调优索引参数，可在下游分类或 RAG 效果不降的前提下大幅提升
  QPS 或降低计算成本。

  - 推荐系统和 Agent 检索链路中，当业务指标对检索噪声不敏感时，可主动降低对 Recall@k 的要求，转而监控距离比，以换取更高吞吐和更低延迟。

  - 离线基准测试或 CI/CD 流程中，**1/Ratio@k 无需人工标注、仅依赖查询向量和距离**，易于工程化实现，可作为自动化质量关卡。

  - 选型 ANN 算法时，关注不同索引在相同 **1/Ratio@k** 下的吞吐差异，能更直接地预测线上真实性价比，避免为虚高的 Recall 浪费资源。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：ANN 搜索是信息检索、推荐、RAG 的核心组件，社区普遍用 Recall@k（检索到的真近邻比例）衡量质量，但重叠率不代表结果的真实效用，追求高 Recall 常导致不必要的计算开销。本文质疑这一惯例，提出更贴近下游任务的度量。

**方法**：引入 **1/Ratio@k**，即真实 kNN 距离之和与检索到的 k 个邻居距离之和的比值（逆近似比）。该指标直接刻画检索结果与真实最近邻在距离空间上的接近程度，无需判定、无超参数，仅依赖标准基准数据即可计算。

**结果**：在多种数据集（覆盖宽范围内在维度）和主流 ANN 算法（HNSW、DiskANN 等）上实验表明：优化至相同 1/Ratio@k 阈值的计算成本远低于优化 Recall@k 的成本。在下游分类（标签精度）和 RAG（语义相似度、BERTScore、LLM 评分）任务中，即使 Recall@k 大幅下降，任务指标仍高度稳定；而 1/Ratio@k 与任务表现高度一致，比 Recall@k 更准确地跟踪真实效用。结论：1/Ratio@k 更精确、更部署友好，召回率虚高了近似代价，该指标可有效指导实际系统设计。
