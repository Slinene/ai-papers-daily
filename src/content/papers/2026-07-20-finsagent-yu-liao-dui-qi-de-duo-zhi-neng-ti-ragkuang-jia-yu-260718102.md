---
title: 'FinSAgent: Corpus-Aligned Multi-Agent RAG Framework for Evidence-Grounded
  SEC Filing Question Answering'
title_zh: FinSAgent：语料对齐的多智能体RAG框架用于SEC文件问答
authors:
- Jijun Chi
- Zhenghan Tai
- Hanwei Wu
- Tung Sum Thomas Kwok
- Hailin He
- Zixing Liao
- Bohuai Xiao
- Chaolong Jiang
- Jianliang Lei
- Jerry Huang
affiliations:
- SimpleWay.AI
- McGill University
- University of Toronto
- University of California, Los Angeles
- The Chinese University of Hong Kong
arxiv_id: '2607.18102'
url: https://arxiv.org/abs/2607.18102
pdf_url: https://arxiv.org/pdf/2607.18102
published: '2026-07-20'
collected: '2026-07-23'
category: MultiAgent
direction: 多智能体RAG · 语料对齐检索规划
tags:
- Multi-Agent RAG
- Corpus Alignment
- Evidence-Grounded QA
- Feature-Gated Reranker
- SEC Filing
one_liner: 将SEC文件问答重塑为语料对齐检索规划，通过注入语料侧条件解决先验-语料错配，提升证据检索与回答正确性
practical_value: '- **角色专门化Agent**：按文档结构（如商品详情、用户评价、售后政策）分配Agent，降低跨部分混淆，电商客服可借鉴。

  - **数据库感知查询分解**：让Agent在生成子查询时基于语料摘要视图，避免问题驱动的检索错配，提升召回证据的相关性。

  - **特征门控重排序器**：除语义相似度外，引入证据有效性特征（如来源部分、格式模板）过滤虚假相关片段，用于精准匹配条款或政策。

  - **多路径检索机制**：结合稀疏与密集检索，确保覆盖不同证据类型，适用于商品手册、合同等长文档问答。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有RAG和多智能体系统直接从用户问题生成检索查询，并按语义相似度排序片段，导致‘先验-语料错配’——模型先验与目标文件结构、术语和证据标准不匹配。查询生成遗漏语料特定证据，语义重排序则偏好主题相似但证据无效的假阳性片段。

**方法关键点**：FinSAgent将SEC文件问答重构为语料对齐的检索规划，核心是在模型先验可能占主导之处注入语料侧条件化。具体包含三个组件：(1) 角色专门化智能体，锚定于10-K文件强制披露项目结构；(2) 数据库感知查询分解，每个智能体的子查询都依据轻量级本地语料摘要视图生成，而非仅依赖用户问题；(3) 多路径检索搭配学习型特征门控重排序器，分离证据有效性与语义相似度，抑制假阳性。

**关键结果**：在五个离线金融问答基准上，FinSAgent相比强单智能体和多智能体基线，提升了检索覆盖率和答案正确性。在一项涉及1000名匿名用户评分的三臂随机在线实验中，其用户评分也显著高于基线。
