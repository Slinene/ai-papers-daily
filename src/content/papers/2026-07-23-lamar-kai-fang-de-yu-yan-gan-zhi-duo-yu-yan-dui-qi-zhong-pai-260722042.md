---
title: 'LAMAR: An Open Language-Aware Multilingual Alignment Reranker'
title_zh: LAMAR：开放的语言感知多语言对齐重排序器
authors:
- Seongtae Hong
- Youngjoon Jang
- Jungseob Lee
- Seungyoon Lee
- Heuiseok Lim
affiliations:
- Korea University
arxiv_id: '2607.22042'
url: https://arxiv.org/abs/2607.22042
pdf_url: https://arxiv.org/pdf/2607.22042
published: '2026-07-23'
collected: '2026-07-27'
category: RAG
direction: 多语言RAG重排序 · 语言感知对齐
tags:
- Multilingual Reranker
- Cross-encoder
- Language Coherence
- Preference Alignment
- RAG
one_liner: 提出语言感知多语言重排序器LAMAR，通过英语锚定蒸馏和偏好对齐，同时优化语义相关性和语言一致性。
practical_value: '- 在电商搜索重排序中引入语言偏好特征，优先展示与查询语言一致的商品描述，可提升多语言用户体验和转化率。

  - 使用英语作为锚定语言进行跨语言相关性蒸馏，统一多语言语义评分，可直接复用至多语言召回/排序的 teacher 模型构建。

  - 偏好对齐（如 DPO）可显式控制排序中的语言一致性，结合点击/转化等业务信号微调，比规则加权更精细。

  - 多语言 RAG 场景下，重排序考虑语言一致性可减少下游生成的语言混淆，对多语言客服 Agent 或知识库问答有直接帮助。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：多语言 RAG 中，重排序器通常忽略文档语言，即使存在语义等价的不同语言文档，也不优先将与查询语言相同的文档排在前面，而文档语言会影响答案生成质量。现有模型缺乏语言一致性考量。

**方法**：LAMAR 分两阶段训练。第一阶段：英语锚定的相关性蒸馏——用英语教师模型对多语言正负例打分，训练学生 cross-encoder，统一跨语言语义相关性评分，避免语言偏见。第二阶段：语言一致性偏好对齐——构造偏好对（查询语言与文档语言相同 > 不同，但语义等价），使用 DPO 损失，既保持语义相关性，又鼓励将同语言文档排得更靠前。

**结果**：在受控的语言一致性实验中，LAMAR 在所有受测语言上均取得最佳 F1；在标准多语言重排序基准（如 mMARCO、Mr.TYDI）上保持有竞争力的性能；在实际检索后重排序设置中，所有评估指标均最优，证实其兼顾语言一致性与通用重排序能力。
