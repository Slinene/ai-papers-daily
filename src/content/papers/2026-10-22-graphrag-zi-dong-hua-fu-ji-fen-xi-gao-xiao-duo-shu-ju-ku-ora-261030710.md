---
title: 'Automated Enrichment Analysis with GraphRAG: Efficient Multi-Database ORA
  Extraction and Biological Interpretation'
title_zh: GraphRAG 自动化富集分析：高效多数据库 ORA 提取与生物解释
authors:
- Guangcan Li
- Shuyuan Zheng
- Jiayao Liu
- Shigeto Seno
- Makoto Onizuka
affiliations:
- Graduate School of Information Science and Technology, The University of Osaka,
  Japan
- The First Affiliated Hospital of China Medical University, China
arxiv_id: '2610.30710'
url: https://arxiv.org/abs/2610.30710
pdf_url: https://arxiv.org/pdf/2610.30710
published: '2026-10-22'
collected: '2026-10-25'
category: RAG
direction: GraphRAG 加速 ORA 并提升解释忠实度
tags:
- GraphRAG
- Over-representation analysis
- Knowledge Graph
- LLM
- Faithfulness
- Bioinformatics
one_liner: 将多基因集库建成术语-基因知识图谱，用紧凑证据子图驱动 LLM 生成可溯源解释，查询提速 37 倍且忠实度最高 0.90
practical_value: '- 多源标签整合：把商品属性、类目、场景、用户标签建成统一实体关系图，用共享实体连接分散的标签体系，便于跨源召回和解释。

  - 证据子图检索：给 LLM 提供紧凑连通子图而非平铺 top-k 文档，可降低上下文噪音并提升推荐理由/广告文案生成的事实一致性。

  - claim-level 忠实度评估：逐条校验生成声明是否被图谱边路径支撑，可作为 RAG/Agent 输出质量监控指标，适合落在 pipeline 里自动打分。

  - 查询加速：图式预计算+子图检索相比逐库查询显著提速，可用于实时推荐解释或 Agent 工具检索的缓存设计。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**
现有 ORA 结果分散在 GO/KEGG/Reactome 等多个基因集库，呈现为扁平术语列表，丢失基因级共现与跨库关联。

**方法关键点**
- 建图：把异质基因集库统一为术语-基因知识图谱，共享基因连接跨源相关术语。
- 检索：先基于图做 ORA 评分，再取回一个紧凑连通的证据子图（平均 36.8 节点），而非 top-k 孤立术语。
- 生成：用该子图作为上下文驱动 LLM 生成生物解释，并增加 PubMed 文献层补强。
- 评估：提出 claim-level faithfulness，逐声明检查是否有图中的显式证据支持。

**关键结果**
图式 ORA 与传统 ORA 高度一致（Pearson r=0.997），查询时间中位降低 37×（最高 48×）；GBOR-RAG 的 claim 忠实度为 0.90，是对比系统中最高；加入 PubMed 层后，整体解释质量从 4.17 升到 4.75。
