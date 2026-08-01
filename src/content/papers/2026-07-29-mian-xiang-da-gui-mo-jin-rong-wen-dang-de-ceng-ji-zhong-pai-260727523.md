---
title: Hierarchical Reranking for Scalable Financial RAG System
title_zh: 面向大规模金融文档的层级重排序RAG系统
authors:
- Joohyun Lee
- Sungwoo Hong
affiliations:
- Financial Security Institute
- Hanyang University
arxiv_id: '2607.27523'
url: https://arxiv.org/abs/2607.27523
pdf_url: https://arxiv.org/pdf/2607.27523
published: '2026-07-29'
collected: '2026-08-01'
category: RAG
direction: RAG 层级重排序与长上下文处理
tags:
- RAG
- Hierarchical Reranking
- Long-Context
- Query Optimization
- Financial NLP
one_liner: 通过预检索优化、两阶段层级重排序与自适应长上下文管理，显著提升金融RAG的检索精度与事实一致性
practical_value: '- **预检索优化可复制**：归一化、关键词扩展与表格转换等轻量级预处理，可直接用于电商搜索或推荐系统的查询理解模块，提升召回阶段的命中率，尤其适合含表格的产品描述。

  - **两阶段重排序架构**：先粗排后精排的思路在推荐系统中已成熟，本文的层级重排序强调利用不同粒度证据进行递进式匹配，可将类似思路用于多路召回后的融合排序，比如先用稀疏特征粗排，再用cross-encoder精排，降低精排计算压力。

  - **长上下文的切片与融合机制**：对于需要处理用户长期行为序列或长文档描述的推荐场景，自适应分区和证据融合方法可以避免上下文截断带来的信息丢失，保持长序列推理的连贯性，可迁移至用户长历史建模或多轮对话Agent的记忆管理。

  - **事实一致性校验的启发**：文中强调生成结果的事实一致性，电商生成式推荐（如AI文案、评论总结）同样面临幻觉问题，可借鉴其在RAG管道中加入事实核对步骤，对生成内容与检索证据进行交叉验证。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：金融文档分析（如10-K报表、表格披露）需要专家推理和跨文档交叉引用，现有RAG系统难以处理混合文本-表格结构和大规模长上下文，导致检索不精确、生成事实不一致。

**方法**：提出层级重排序RAG框架，包含三个关键组件：（1）预检索优化：通过归一化、关键词扩展和表格转换提升查询清晰度和检索效率；（2）层级重排序架构：两阶段排序机制，第一阶段利用稀疏检索快速召回，第二阶段用细粒度神经重排序提升精度；（3）长上下文管理：自适应输入分区和证据融合，确保在超长上下文下推理的连贯性和准确性。

**结果**：在FinQA、FinanceBench和ConvFinQA等多个金融基准上，NDCG@20达到0.7918，事实一致性指标显著优于基线；在ACM-ICAIF‘24 FinanceRAG竞赛中获得第二名，验证了系统的鲁棒性和可部署性。
