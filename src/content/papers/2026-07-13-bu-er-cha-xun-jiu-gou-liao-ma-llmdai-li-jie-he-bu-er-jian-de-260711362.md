---
title: Boolean queries are all you need?
title_zh: 布尔查询就够了吗？LLM代理结合布尔检索的探索
authors:
- Charles L. A. Clarke
- Mark D. Smucker
affiliations:
- University of Waterloo
arxiv_id: '2607.11362'
url: https://arxiv.org/abs/2607.11362
pdf_url: https://arxiv.org/pdf/2607.11362
published: '2026-07-13'
collected: '2026-07-15'
category: RAG
direction: LLM Agent 自动布尔查询生成与检索
tags:
- Boolean Retrieval
- LLM Agent
- RAG
- Pattern Matching
- Unsupervised Ranking
one_liner: LLM搜索代理自动生成布尔查询，基于子串匹配密度无监督排序，NDCG@10=0.6863超越主流稠密/稀疏检索器
practical_value: '- **无监督检索替代方案**：电商搜索或广告匹配中，可使用LLM将用户query改写为多条件布尔查询，结合商品属性词库进行精确匹配，无需训练稠密或稀疏模型，适合冷启动或快节奏场景。

  - **多轮交互式检索**：在Agent框架内，用少量模型调用（≤100次/主题）迭代优化布尔查询，可低成本实现高精度检索，可借鉴到对话式导购系统。

  - **匹配密度评分**：仅基于匹配子串的数量和长度计算相关度，实现简单，可解释性强，适合要求透明排序的业务（如合规广告召回）。

  - **数据泄露警惕**：由于测试集可能包含在LLM训练数据中，实际迁移时应避免直接使用公开基准，需在业务特有数据集上验证效果。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：传统布尔检索精确但依赖人工构造复杂查询，难以普及；现代稠密/稀疏检索依赖监督学习或全局统计。探究LLM代理自动生成布尔查询能否重现甚至超越这些检索器。

方法：将LLM搜索代理接入布尔检索引擎，代理基于用户自然语言描述，通过特定提示（如要求返回精确匹配的片段、限定领域词汇）迭代生成布尔查询（正则语言子集），文档评分仅基于匹配子串的密度（匹配次数与长度），不利用语料全局统计、term权重或任何训练。在TREC 2024 RAG track的MS MARCO V2.1去重段集合（约138M段）上，测试86个主题，每主题模型调用预算100次，最终排序取前10。

结果：NDCG@10达到0.6863，超过了BM25、DPR等众多一阶检索器。实验表明，虽然仅在单一公开测试集上（存在数据泄露可能），但简单的模式匹配结合LLM的查询生成能力，在agentic搜索中可能已足够有效。
