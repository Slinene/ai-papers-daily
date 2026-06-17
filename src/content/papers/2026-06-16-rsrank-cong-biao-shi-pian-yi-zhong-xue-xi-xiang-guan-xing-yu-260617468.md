---
title: 'RSRank: Learning Relevance from Representational Shifts'
title_zh: RSRank：从表示偏移中学习相关性用于重排序
authors:
- Archit Gupta
- Sai Sundaresan
- Debabrata Mahapatra
affiliations:
- Adobe Research
arxiv_id: '2606.17468'
url: https://arxiv.org/abs/2606.17468
pdf_url: https://arxiv.org/pdf/2606.17468
published: '2026-06-16'
collected: '2026-06-17'
category: RAG
direction: 重排序 · 表示偏移 · 零阈值过滤
tags:
- Reranker
- Representational Shift
- Relevance Scoring
- RAG
- Lightweight Training
one_liner: 利用查询在文档条件下的表示偏移作为相关性信号，零阈值过滤，克服启发式阈值依赖
practical_value: '- **将 RS 信号用于电商搜索重排序**：在精排阶段，用用户查询在商品描述条件下的 hidden state 变化量作为特征，代替传统
  logit 或人工特征，可能捕捉更细腻的相关性，尤其适合语义模糊的长尾 query。

  - **零阈值过滤简化工程阈值**：RS 信号经投影后，不相关文档得分天然接近 0，可省去离线调阈值的麻烦，线上直接截断即可；在推荐系统召回后过滤粗糙结果时，能减少人工维护阈值的工作量。

  - **轻量训练框架便于部署**：只需在预训练 LLM 顶层加一个投影头，训练成本低，适合在已有 RAG 或搜索管道中快速实验；电商 Agent 生成推荐理由时，可用此方法对候选知识片段做即插即用的相关性过滤。

  - **对齐 Oracle 文档集的思路可迁移**：如果业务中存在高相关“理想文档”集合（如人工标注的金牌结果），可以计算候选文档与 Oracle 文档集产生的
  RS 相似度作为弱监督信号，用于训练推荐排序模型。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：企业级 RAG 系统中，重排序是分离相关与干扰文档的最后过滤步骤，但现有方法通常依赖启发式阈值调优，且常用 LLM 的 logit 信号，其设计目标是下一 token 预测而非相关性评估，缺乏原则性信号。

**方法**：作者发现查询在文档条件作用下的**表示偏移（Representational Shift, RS）**能稳健指示相关性。具体计算为：将查询与文档拼接输入 LLM，取查询部分最后一层 hidden state 的均值，与仅查询本身的均值之差，作为该文档的 RS 向量。进一步观察到，候选文档的 RS 向量与 Oracle 文档集（所有正相关文档）的 RS 向量之间的余弦相似度，是强相关性指标。基于此，提出一个轻量级训练框架：学习一个投影矩阵，将查询-文档对的 RS 矩阵映射为标量相关性分数，训练目标使正样本得分靠近 1，负样本靠近 0，自然在 0 处形成分界，消除人工阈值依赖。

**关键结果**：在多个检索数据集（如 MS MARCO、Natural Questions）上，RSRank 相比 Cohere、BGE 等 SOTA 重排序器，Mean Reciprocal Rank 和 Normalized DCG 均有显著提升，同时训练和推理开销极小。
