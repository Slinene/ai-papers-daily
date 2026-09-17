---
title: 'Beyond Truncation: Rethinking LLM Decoding as Ensemble Pruning'
title_zh: 超越截断：将 LLM 解码重新定义为集成剪枝
authors:
- Dunyao Xue
- Chengshuo Du
- Zhengbo Wang
- Wenlin Dai
- Cheng Meng
affiliations:
- Institute of Statistics and Big Data, Renmin University of China
- Big Data and Responsible Artificial Intelligence for National Governance, Renmin
  University of China
- Center for Applied Statistics, Renmin University of China
arxiv_id: '2609.18723'
url: https://arxiv.org/abs/2609.18723
pdf_url: https://arxiv.org/pdf/2609.18723
published: '2026-09-16'
collected: '2026-09-17'
category: LLM
direction: LLM 解码 · 集成剪枝
tags:
- LLM Decoding
- Ensemble Pruning
- Mahalanobis Distance
- Token Diversity
- Plug-and-Play
one_liner: 提出 Mahalanobis-Ensemble Decoding，基于 token 嵌入相似度做集成剪枝，提升解码多样性且近乎零开销
practical_value: '- 在电商/广告文案、搜索 query 推荐等文本生成场景，可直接作为解码端插件，用 token 语义相似度矩阵做候选剪枝，减少重复
  token 和语义冗余，无需重新训练模型。

  - 若业务中已有 LLM 生成候选商品描述、推送文案或 Agent 规划路径，可把 ME-Decoding 的 adaptive-bandwidth kernel
  思路迁移到自有 token/item embedding 上，构造 Mahalanobis 距离驱动的多样性目标，提升候选集召回质量。

  - 该方法强调 near-linear 复杂度和 early stopping，适合线上推理延迟敏感场景；在 beam search 或采样前对候选 token
  做一次轻量剪枝，可作为低成本的多样性增强层。

  - 对生成式推荐中的 Semantic ID 或多 token 生成路径，可用相似度矩阵动态 discount 冗余路径，缓解生成结果坍缩到高频 ID 或重复
  token 的问题。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：主流 LLM 解码策略主要依赖标量概率选择 token，忽略 token 之间的几何语义关系，容易产生候选冗余；现有几何感知方法要么需要复杂优化，要么直接重加权原始概率，带来额外计算开销或推理不稳定。

**方法关键点**：提出 Mahalanobis-Ensemble Decoding (ME-Decoding)，将候选 token 选择形式化为集成剪枝问题。通过 token embedding 上 adaptive-bandwidth kernel 构造 token 相似度矩阵，利用 Mahalanobis 距离驱动目标，在保留高概率 token 的同时增强语义多样性；动态 discount 冗余生成路径。配套设计贪心选择算法，在 early stopping 下达到近似线性复杂度，并提供理论近似保证，可作为 plug-and-play 模块。

**关键结果**：在多种推理和生成任务上实验，方法一致取得强性能，且推理开销可忽略。
