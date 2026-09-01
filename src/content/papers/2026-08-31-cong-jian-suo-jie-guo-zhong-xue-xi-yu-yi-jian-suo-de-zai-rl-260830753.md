---
title: 'Learning from What You Retrieve: Online RL Fine-Tuning for Semantic Retrieval'
title_zh: 从检索结果中学习：语义检索的在线 RL 微调
authors:
- Shaowei Wei
- Chong Huang
- Songtao Fang
- Jin Zhang
- Zhuojun Wang
- Chengfu Huo
affiliations:
- Alibaba Group
arxiv_id: '2608.30753'
url: https://arxiv.org/abs/2608.30753
pdf_url: https://arxiv.org/pdf/2608.30753
published: '2026-08-31'
collected: '2026-09-01'
category: RecSys
direction: 语义检索 · 在线 RL 微调
tags:
- Semantic Retrieval
- Reinforcement Learning
- Dual Encoder
- Frozen Index
- E-commerce Search
- Query Encoder
one_liner: 提出 PAO，在冻结文档索引下只对正 advantage 样本做 RL 更新，避免 embedding 几何塌缩并提升检索效果
practical_value: '- 工业双塔召回中文档索引冻结是常态，PAO 的 RL 更新只作用于 query encoder，无需重建索引；可直接改造现有
  REINFORCE：对 advantage 加 I(A>0) mask，并加入 KL 到预训练 reference policy，工程落地成本低。

  - 如果业务上用 reranker 或点击信号作为 reward 做在线 RL，不要无差别惩罚低 reward 样本。标准 policy gradient 的负向
  push 会破坏预训练语义流形；优先只利用正 reward 的 pull 信号，能更稳定地做 retriever-reranker 对齐。

  - 与直接蒸馏 reranker soft distribution 相比，positive-only policy gradient 在冻结索引下更稳，尤其深层召回
  Recall@50 提升更明显；当目标是对齐精排偏好时，可优先考虑 PAO 而非全局 KL 蒸馏。

  - 使用标准化 advantage 降低方差；β=0.1~0.3、τ≈1.0 是较稳健的超参区间。注意 reward model 的偏差会传导到召回，若 reranker
  偏好标题党，需要多目标或额外约束。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
电商大规模检索通常采用双塔召回 + 下游精排的两段式架构，但双塔的对比相似度目标与精排的细粒度相关性目标不一致。工业界文档索引因成本原因通常冻结，只能在线更新 query encoder。直接用 RL 用 reranker reward 微调 query encoder 时，标准 policy gradient 对负样本的 push 操作会破坏预训练 embedding 流形，导致严重的 geometry collapse，召回指标大幅下降。

## 方法关键点
- 把 query encoder 作为 policy，检索 top-K 列表作为 macro-action，检索概率由 softmax 内积得分定义；reward 来自下游 reranker。
- 标准 REINFORCE 对所有候选按 advantage 加权更新，负 advantage 会把 query embedding 推向语义空洞。
- 提出 PAO：只对 positive advantage 的 retrieved items 做梯度更新，mask 掉负样本；同时加入 KL 散度约束到预训练 reference policy，防止整体漂移。
- 实际只更新 query encoder，文档索引保持冻结，避免重建索引。

## 关键实验
- 工业电商搜索日志：1M 训练查询 / 50k 测试查询，GTE-Base 初始化，BGE-Reranker 做 reward，top-100 检索。
- 对比 Baseline（InfoNCE）、RL-All（标准 PG）、RL-Pos（PAO）。
- 工业数据上，PAO 相比 Baseline 达到 NDCG@5 +9.0pt、Recall@5 +6.9pt；而 RL-All 出现 -13.6pt NDCG@5 的灾难性退化。
- LLM judge（Qwen3-235b）：Hits@20 +2.1pt，Matchment +1.4pt。
- MS MARCO：PAO 相比 Baseline NDCG@5 +2.03pt、Recall@50 +4.23pt，且优于 KL 蒸馏。
- 消融：β=0.3、τ=1.0 最优。

## 最值得记住的一句话
在冻结文档索引下，只做正 advantage 的 pull 更新、屏蔽负样本 push，是实现 retriever-reranker 对齐同时保持 embedding 几何稳定的关键。
