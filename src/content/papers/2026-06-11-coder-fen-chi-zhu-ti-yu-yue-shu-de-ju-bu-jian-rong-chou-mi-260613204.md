---
title: 'CoDeR: Local Constraint-Compatible Retrieval Beyond Semantic Similarity'
title_zh: CoDeR：分离主题与约束的局部兼容稠密检索
authors:
- Xingkun Yin
- Xuebin Tang
- Hongyang Du
affiliations:
- University of Hong Kong
- University of Science and Technology Beijing
arxiv_id: '2606.13204'
url: https://arxiv.org/abs/2606.13204
pdf_url: https://arxiv.org/pdf/2606.13204
published: '2026-06-11'
collected: '2026-06-13'
category: RAG
direction: 约束兼容信息检索，分离主题与约束
tags:
- dense retrieval
- constraint compatibility
- negative constraints
- bi-encoder
- lexical-polarity supervision
- antonymy-negation-exclusion
one_liner: 提出将主题相关性与约束兼容性解耦的双编码器检索方法，专门减少违反负约束的文档暴露
practical_value: '- 电商搜索中处理否定约束（如“不含酒精”、“非转基因”）：可独立训练兼容性评估器，对召回的商品根据约束兼容性重排或过滤，避免返回违反要求的商品。

  - 在构建Agent的检索组件时，对于用户带有硬约束的查询（如“不要推荐含糖饮料”），可直接采用CoDeR的双编码器架构，无需调用LLM，推理成本低。

  - 可用对比学习和词汇极性信号（如反义词对）监督训练兼容性模型，方法简单有效，可迁移至各类产品属性约束。

  - 重排和单独检索兼容性候选两种模式灵活，适用于不同时延要求：重排适合在线快速筛选，单独检索适合离线生成高质量候选集。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有检索系统以语义相似度作为相关性代理，但遇到约束敏感查询（如“安静且不吵闹的酒店”）时，语义相近但内容违反约束（如“酒店夜生活热闹”）的文档会被错误地排在前面，导致风险。此类约束违反证据暴露在RAG或直接面向用户的场景下尤其有害。

**方法关键点**：CoDeR将检索拆分为主题编码器和约束兼容性评分器。主题编码器保持原有稠密检索能力，确保候选覆盖；兼容性评分器采用双编码器，通过在正例（满足约束）与负例（违反约束）上作对比学习，并以词汇极性（如反义词、否定词）作为监督信号进行训练。推理时兼容性分数可用来重排主题模型返回的候选列表，或直接检索一个独立的兼容候选集，整个过程无需调用外部LLM。

**关键结果**：在反义词、否定、排除三类诊断测试上，CoDeR将V@2（前2个结果中出现违反约束文档的比例）相对最强基线分别降低20.59、23.53和5.77个百分点，同时显著推迟第一个违反约束文档出现的位置，大幅减少约束违反曝光。
