---
title: 'CiteGuard-RAG: A Validation-Centered AI System for Evidence-Grounded Question
  Answering'
title_zh: CiteGuard-RAG：以验证为中心的证据支撑问答系统
authors:
- Sumit Barua
- Guan Hong
- Halil Dursunoglu
- Charles Rodgers
- Alvis Fong
affiliations:
- Department of Computer Science, Western Michigan University
arxiv_id: '2609.15830'
url: https://arxiv.org/abs/2609.15830
pdf_url: https://arxiv.org/pdf/2609.15830
published: '2026-09-14'
collected: '2026-09-15'
category: RAG
direction: 验证中心RAG架构
tags:
- RAG
- Hallucination Mitigation
- Citation Validation
- Evidence-Grounded QA
- Hybrid Retrieval
- Abstention
one_liner: 集成混合检索、引用约束生成、句级grounding验证与单次重生成，在最终交付前决定接受、拒绝或重生成答案
practical_value: '- 在电商客服/商品问答中，可将验证作为独立运行时组件放在检索和最终回答之间，对生成答案做句级引用校验，避免给出无依据的售后政策或参数。

  - 混合语义-词汇检索（受控数据集检索准确率99.1%）值得借鉴：商品知识库/店铺政策QA可结合BM25和向量检索，提升证据命中率。

  - 单次重生成机制：验证失败时先尝试基于检索证据重新生成，若仍不合格则拒绝回答；适合价格、退换货规则等高合规风险场景，防止误导用户。

  - 引用约束生成要求逐句标注来源，便于线上审核和用户信任；可用于广告文案合规检查，确保每句声称都有依据。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：RAG 虽然改善信息获取，但单独检索不能保证答案 grounded、引用有效或恰当地拒绝回答，在法律等高风险场景中幻觉和弱来源可追溯性会导致误导。  
**方法**：CiteGuard-RAG 以验证为核心，集成混合语义-词汇检索、引用约束生成、句级 grounding 验证和单次重生成。运行时验证决定候选答案应接受、拒绝还是重生成，确保最终交付前经过显式校验。  
**结果**：在受控住房法数据集 400 个问题上，检索准确率 99.1%，grounded-answer 准确率 98.3%，引用有效率 98.3%，且无验证检测到的幻觉；消融显示去除验证后准确率大幅下降，即使检索准确率不变。外部数据集（PrivacyQA、CUAD）上引用有效性仍强，但证据利用、span 对齐和拒绝校准在域迁移下变难。
