---
title: Evidence-Aligned Entity Verification for Hallucination Detection in Retrieval-Augmented
  Generation
title_zh: 检索增强生成中用于幻觉检测的证据对齐实体验证
authors:
- Runsong Jia
- Zhen Fang
- Mengjia Wu
- Jie Lu
- Yi Zhang
affiliations:
- University of Technology Sydney
arxiv_id: '2609.08267'
url: https://arxiv.org/abs/2609.08267
pdf_url: https://arxiv.org/pdf/2609.08267
published: '2026-09-08'
collected: '2026-09-09'
category: RAG
direction: RAG幻觉检测·实体证据对齐
tags:
- hallucination detection
- RAG
- entity verification
- counterfactual stability
- LLM
one_liner: 提出 EAEV，在实体层面用 RAG 对齐生成与检索证据，结合三维对齐评估和反事实稳定性分析，一致提升 RAG 幻觉检测性能
practical_value: '- 在电商商品文案/搜索结果生成中，可借鉴实体级幻觉检测：将商品属性（品牌、型号、参数）作为实体，逐项验证生成文本与商品知识库/活动规则的证据对齐，比整体一致性打分更细粒度、可定位错误属性。

  - 采用多维度对齐信号：可设计“实体是否在证据中出现”“实体上下文是否一致”“实体关系是否冲突”等互补指标，结合轻量规则或分类器进行 RAG 输出校验，适合低延迟的线上
  Agent 回复。

  - 反事实稳定性分析可迁移为回归测试：对检索到的证据文本做小扰动（替换同义词、增减片段），要求生成关键实体保持稳定，若翻转则标记高风险幻觉，提升对检索噪声的鲁棒性。

  - 用 RAG 做幻觉检测而非仅生成，可解决模型参数知识过时的问题，特别适合电商频繁更新的价格、库存、促销等时效性知识。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 幻觉检测目前主要依赖模型内部信号（不确定度、自一致性），但预训练知识存在过期和覆盖不足，尤其是专业/实时信息。RAG 能引入外部证据，但需要判断生成内容是否与检索证据一致，即 RAG-based hallucination detection (RHD) 问题。

**方法关键点**：EAEV 在实体层面检测幻觉，不判断整个句子，而是对齐生成实体与检索证据上下文。通过三个互补维度评估实体-证据对齐（例如实体是否出现、上下文匹配度、关系一致性），并引入反事实稳定性分析：对证据施加扰动，观察对齐结果是否稳定，以排除偶然对齐，提升鲁棒性。

**结果**：在多个 RAG 基准上，EAEV 相比现有方法取得一致改进，并展现强泛化能力。
