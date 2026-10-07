---
title: Learning to Retrieve via Reinforcement Learning in Embedding Space
title_zh: 嵌入空间强化学习检索训练
authors:
- Qi Liu
- Fengming Liang
- Yiqun Chen
- Erhan Zhang
- Jiaxin Mao
affiliations:
- Renmin University of China
arxiv_id: '2610.07731'
url: https://arxiv.org/abs/2610.07731
pdf_url: https://arxiv.org/pdf/2610.07731
published: '2026-10-06'
collected: '2026-10-07'
category: RecSys
direction: RL 后训练 dense retriever
tags:
- Reinforcement Learning
- Dense Retrieval
- Embedding Space
- vMF
- CMP
- RAG
one_liner: RELER 将 embedding 视为动作，以 vMF 采样探索，用 RL 直接优化检索/下游奖励，结合 CMP 降方差，后训练提升检索与
  RAG
practical_value: '- 在电商/广告检索中，可只对 query encoder 做 RL 微调、冻结文档/商品向量库与 ANN 索引，直接把 nDCG@K、Recall@K、点击率或
  GMV 等不可微业务指标作为 reward，无需重建索引即可适配新目标。

  - 用 vMF 分布对归一化 query/document embedding 做采样探索，再配合 RLOO 策略梯度，可以把已有双塔模型从对比学习后训练成直接优化业务排序指标，线上推理保持确定性单向量检索，无额外成本。

  - Product rollouts 将同一批 query 与 document embeddings 两两配对计算 reward，不增加 encoder 前向，却让每个采样获得更多反馈，适合候选集有限、前向成本敏感的场景。

  - CMP 把采样嵌入投影到由策略均值和候选向量张成的低维子空间再算梯度，能在不改变期望梯度的前提下显著降噪；当候选集维度远小于 embedding 维度时尤其值得采用，例如电商候选池通常有限。

  - 奖励设计上，分档 nDCG@10 + pairwise 准确率（λ=0.5）优于 binary nDCG/MRR；业务中可类比使用分档排序指标与 pairwise
  反馈混合，但 pairwise 权重不宜过大。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
对比学习训练 dense retrieval 只优化表示质量，与最终检索指标（nDCG、Recall@K）或下游任务（RAG 答案质量）存在目标不一致，类似 LLM 对齐中 next-token prediction 与人类偏好的差距。现有 RL 检索方法多采样文本或文档选择，而 query/document 向量本身并未作为动作被探索。

### 方法关键点
- 将 embedding 视为可学习的检索动作：在单位球上用 von Mises–Fisher (vMF) 分布围绕 encoder 输出采样 query 和 document embedding，探索嵌入方向。
- Product rollouts：同一 rollout group 内 G 个 query 动作与 G 个 document bundles 两两配对，得到 G² 个 reward，不增加 encoder 前向，每个动作获得多个反馈。
- 使用 REINFORCE leave-one-out (RLOO) 对 query 与 document 两侧分别计算 advantage，更新共享 encoder。
- 提出 conditional-mean projection (CMP)：将采样嵌入投影到由策略均值和候选向量张成的低维子空间，去除 reward 不可见的梯度噪声，同时保持每个候选分数与期望梯度不变；在 BRIGHT 上梯度方差降低 291–590 倍。
- 固定索引 query-only 适应：冻结文档向量库和 generator，只更新 query encoder，并加 anchor 限制漂移，适合线上 ANN 索引不可重建场景。
- 奖励设计：BRIGHT 检索用分档 nDCG@10 + pairwise 准确率（λ=0.5）；RAG 用 0.5 nDCG@10 + 0.5 answer F1 混合。

### 关键结果数字
- BRIGHT 上，RELER 在 BGE-M3、Qwen3-Embedding-0.6B/4B 三个 backbone 和原始/GPT-4 推理 query 两种设置下，平均 nDCG@10 均超过 InfoNCE、LambdaLoss 和 pretrained。原始 query 下 BGE-M3 从 10.66 提升到 14.49，Qwen3-0.6B 从 15.10 到 23.38，Qwen3-4B 从 18.70 到 30.46。
- 固定索引 RAG 在七个 QA 数据集上，混合奖励使平均 EM 从 pretrained 32.30 提升到 32.96，F1 从 40.76 到 41.10，Hit@10 从 55.87 到 56.38，均超过 InfoNCE。
- CMP 和 product rollouts 是关键增益来源：CMP 使平均 nDCG@10 从 21.91 增加到 23.38；product rollouts 相比一对一配对提升 2.14 点。

> 最值得记住的一句话：把 embedding 本身当作动作，在低维有效子空间内用 RL 直接优化不可微排序/业务目标，可以在不改变线上推理的前提下显著提升检索与下游效果。
