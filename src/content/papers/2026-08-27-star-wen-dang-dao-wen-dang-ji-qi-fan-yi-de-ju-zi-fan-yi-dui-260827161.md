---
title: 'STAR : Sentence Translation Alignment Rate for Document-to-Document Machine
  Translation'
title_zh: STAR：文档到文档机器翻译的句子翻译对齐率与偏好优化
authors:
- Yichen Dong
- Hao Wang
- Junhui Li
- Linlong Xu
- Longyue Wang
- Weihua Luo
affiliations:
- Soochow University, Suzhou, China
- Alibaba Group, Hangzhou, China
arxiv_id: '2608.27161'
url: https://arxiv.org/abs/2608.27161
pdf_url: https://arxiv.org/pdf/2608.27161
published: '2026-08-27'
collected: '2026-08-29'
category: Training
direction: LLM 文档级翻译的结构对齐评估与偏好优化
tags:
- Doc2Doc MT
- LLM
- Preference Optimization
- Alignment
- Evaluation Metric
one_liner: 提出 STAR 结构对齐指标与 StarPO 偏好优化，使紧凑模型在 Doc2Doc 翻译中超过 GPT-4o 且更省 token
practical_value: '- 将 STAR 的句子级结构对齐思想迁移到生成式推荐/广告文案：对输入商品属性、卖点与输出文案做句子或字段级对齐检查，量化漏生成、幻觉、错位比例，作为离线评估或
  reward 信号，避免 LLM 漏掉关键卖点或编造属性。

  - StarPO 的动态掩码偏好优化可用于训练可控生成：先按结构对齐分数排序候选，构造偏好对时只对错位片段计算 loss / 梯度，减少无关 token 干扰，提升对业务约束（如必须包含关键词、数据字段）的遵守率。

  - 紧凑模型 + 结构化偏好优化在特定任务可超过 GPT-4o 且 token 效率更高；在低延迟、高吞吐的电商生成场景中，可优先用小模型配合针对性的对齐训练，不必盲目依赖大模型
  API。

  - 对 RAG / Agent 多步生成也可借鉴：在检索结果摘要、reasoning 步骤输出中增加源-目标结构保真度检查，防止 Agent 遗漏关键检索信息或幻想额外事实。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 推动文档到文档（Doc2Doc）机器翻译，单遍生成常出现句子遗漏或幻觉，导致源文-译文结构错位，违反对应性要求。

**方法**：提出句子翻译对齐率（STAR），显式量化句子级结构保真度，区分 1-to-1 理想对齐、1-to-0 漏译、0-to-1 幻觉及其他偏差。基于此提出 StarPO 框架：对文档级假设按结构质量排序，构建偏好对，并用动态对齐掩码将优化聚焦在错位片段上，减少无关 token 干扰。

**结果**：在新闻和文学领域，StarPO 显著提升翻译质量和结构完整性。基于 Qwen2.5-7B 的紧凑模型 1-to-1 对齐达 98.43%，漏译 0.68%，幻觉 0.00%，优于 GPT-4o 的 92.91% / 2.25% / 2.89%，同时 token 效率更高。
