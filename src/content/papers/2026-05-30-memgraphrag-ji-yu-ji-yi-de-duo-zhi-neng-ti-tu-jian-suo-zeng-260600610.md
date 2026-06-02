---
title: 'MemGraphRAG: Memory-based Multi-Agent System for Graph Retrieval-Augmented
  Generation'
title_zh: MemGraphRAG：基于记忆的多智能体图检索增强生成
authors:
- Chuanjie Wu
- Zhishang Xiang
- Yunbo Tang
- Zerui Chen
- Qinggang Zhang
- Jinsong Su
affiliations:
- Xiamen University
- Jilin University
arxiv_id: '2606.00610'
url: https://arxiv.org/abs/2606.00610
pdf_url: https://arxiv.org/pdf/2606.00610
published: '2026-05-30'
collected: '2026-06-02'
category: MultiAgent
direction: 多智能体协同 · 图检索增强生成
tags:
- GraphRAG
- Multi-Agent
- Knowledge Graph
- Memory
- Retrieval-Augmented Generation
one_liner: 用三层全局记忆与多智能体协同消除知识图谱构建中的局部噪声与冲突，实现高精度低延迟的图检索增强生成。
practical_value: '- **知识图谱自动化清洗与一致化**：电商商品知识图谱常因多渠道爬取导致属性冲突（如价格、规格矛盾），可借鉴记忆层冲突检测‑证据比对‑裁决的多
  Agent 闭环，自动合并冗余、修正错误三元组。

  - **全局主题过滤防止无关抽取**：在构建推荐或问答用知识图谱时，设定 Schema 频率阈值过滤低频噪音，避免局部抽取引入偏离主商品类目的 off‑topic
  事实，提升图谱信噪比。

  - **结构感知的检索初始化**：处理包含海量类目节点的商品图谱时，对高连通度的“类目”节点使用 log‑degree 惩罚初始化，防止 PPR 传播时重要性被泛化节点稀释，确保多跳推理聚焦于具体商品实体。

  - **分层记忆检索范式**：在生成式推荐或对话中，可按本体 → 事实 → 文本段落逐层召回、过滤，先匹配类目与属性范式再定位具体商品与评论文本，兼顾粗粒度的语义约束与细粒度的证据支撑。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有 GraphRAG 系统多基于孤立 chunk 局部抽取构建知识图谱，缺乏对全量语料的全局视野，导致三大缺陷：主题无关（大量 off‑topic 三元组）、逻辑冲突（同一实体出现矛盾事实）、结构碎片化（关键实体分散在不同子图）。这三类噪声严重损害检索上下文的相关性与推理连贯性，使得图增强生成在实际多跳问答中常不如朴素 RAG。

**方法关键点**：
- 提出 **MemGraphRAG**，引入三层全局记忆架构（本体层、事实层、段落层）与多智能体协作（提取、冲突检测、冲突解决 Agent），在抽取过程中持续维护全局一致性。
- **全局记忆驱动的图谱构建**：通过 Schema 频率过滤剔除主题无关三元组；冲突检测 Agent 异步扫描新激活事实，冲突解决 Agent 利用证据追溯进行证据驱动的裁决；记忆引导桥接消除实体碎片化。
- **分层索引图**：构建本体图（类型关系）、事实图（实体‑关系）、证据图（事实‑原文）三层异构结构，支持从抽象语义到具体证据的遍历。
- **记忆感知层次化检索**：并行从三层记忆中召回候选，经语义相似度过滤后作为 PPR 初始种子；种子初始化引入结构先验——类型节点用 log‑degree 惩罚抑制高度中心节点的扩散，段落节点用 IDF 加权的信息密度项强化罕见实体的证据；最后在异构图上执行 PPR 传播，选取 Top‑K 段落与实体供 LLM 生成。

**关键结果**：
- 在 HotpotQA、2WikiMultiHopQA、MuSiQue、G‑Medical、G‑Novel 五个基准上，MemGraphRAG 平均 LLM‑Acc 达 59.25%，超越最强基线 LinearRAG 2.10 个百分点。
- 检索延迟仅 0.061 秒，比 LightRAG 快 180 倍，同时 Recall 与 Relevance 在复杂推理任务上双高（Recall 90.42、Relevance 82.64）。
- 图构建质量验证：将 MemGraphRAG 构建的图谱替换到其他 GraphRAG 检索器中，所有基线性能均有提升，证明其可作为通用高质量图构造函数。
- 消融表明：移除 Schema 过滤、冲突解决、Hub 抑制或信息密度项均导致性能下降，验证各模块不可或缺。

**值得记住的一句话**：把局部信息抽取升级为全局记忆协同的多智能体进化过程，才是解决 GraphRAG "高召回低相关"困境的有效路径。
