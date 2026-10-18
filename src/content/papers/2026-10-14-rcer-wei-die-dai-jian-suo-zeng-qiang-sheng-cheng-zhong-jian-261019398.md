---
title: 'RCER: Reconstructing Cross-Evidence Relations for Iterative Retrieval-Augmented
  Generation'
title_zh: RCER：为迭代检索增强生成重建跨证据关系
authors:
- Linyao Zheng
- Xuhang Shi
- Zhifang Mao
- Xiuquan Hou
- Sai Zhou
affiliations:
- Xi'an Jiaotong University
- Beijing University of Posts and Telecommunications
arxiv_id: '2610.19398'
url: https://arxiv.org/abs/2610.19398
pdf_url: https://arxiv.org/pdf/2610.19398
published: '2026-10-14'
collected: '2026-10-18'
category: RAG
direction: 迭代 RAG · 跨证据关系重建
tags:
- RAG
- Iterative Retrieval
- Multi-hop QA
- Cross-evidence Relations
- Knowledge-state Updating
one_liner: 在迭代 RAG 中重建跨证据实体对应与推理依赖，多跳 QA 平均 EM/F1 提升 2.83/3.06
practical_value: '- 在商品/店铺/活动规则等复杂问答或客服 Agent 中，可把多轮检索到的片段抽象成实体对应关系和推理依赖图，每次新证据加入时增量重建关系，驱动下一轮
  query 分解，避免仅靠向量相似度重复召回。

  - 把「证据获取」和「推理上下文构建」解耦：先做互补证据联合选择，再基于跨证据推理补齐隐式链条，最后组合关系回答；适合电商场景中跨文档信息拼接，如满减规则+商品类目+用户历史生成答案。

  - 工程实现上，RCER 直接利用累积的 source passages，不依赖外部知识图谱或额外训练，可以低成本接入现有 RAG pipeline；在多跳、叙事型、隐式推理问题上收益更明显。

  - 若业务问题偏短平快，收益有限；更值得用于导购对比、合规规则问答、售后政策推理等需要链路推理的场景。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：迭代 RAG 在回答复杂多跳问题时，随着新证据加入，往往难以恢复跨段落实体对应关系和推理依赖，导致证据利用不充分。

**方法关键点**：RCER 直接从累积的源段落中重建跨证据关系，分三阶段：
1. **Inter-round relational evidence acquisition**：识别实体对应和关系依赖，驱动动态问题分解与后续检索；
2. **Reasoning context reconstruction**：联合选择互补段落，并推导跨证据推断，构建连贯推理上下文；
3. **Cross-evidence compositional reasoning**：利用推断结果建立实体对应并组合关系，完成答案推导。

**关键结果**：在三个 multi-hop QA 基准上，平均 EM 和 F1 分别比最佳基线高 2.83 和 3.06 分；在叙事型与隐式推理任务上表现更优。
