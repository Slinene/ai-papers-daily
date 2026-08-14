---
title: Test-Time Optimization of Query Embeddings with Ranking Aware Reward Maximization
title_zh: 基于排序奖励最大化的查询向量测试时优化
authors:
- Tianyu Chen
- Jiaxing Wu
affiliations:
- The University of Texas at Austin
- Google DeepMind
arxiv_id: '2608.12569'
url: https://arxiv.org/abs/2608.12569
pdf_url: https://arxiv.org/pdf/2608.12569
published: '2026-08-12'
collected: '2026-08-14'
category: RecSys
direction: 测试时查询向量优化 · 排序奖励蒸馏
tags:
- test-time optimization
- dense retrieval
- embedding adaptation
- ranking reward distillation
- reranker
- MTEB
one_liner: 把 reranker/LLM 排序分数蒸馏成可复用查询向量残差，冻结权重与索引，MTEB 最高 +8.36 nDCG@10
practical_value: '- 在闭源 embedding API 或已有 ANN 索引不能改时，可只学一个查询侧残差向量 v_g：部署时用 unit(x_q
  + α v_g) 重新检索，索引、doc embedding、相似度函数都不动，适合线上低成本接入 reranker 蒸馏增益。

  - scope 选择可作为固定 reward 预算下的复用策略：预算极少先 global 共享；预算中等按业务类目/任务建 task-wise；预算充足再 query-wise。对应从冷启动全局复用
  → 类目/场景共享 → 个性化 query 专用。

  - 免调参的置信度缩放 α_g = n_g/(n_g+1) 值得直接迁移：共享状态按覆盖 query 数自动控制应用强度，小样本不过冲，省掉按预算手动调 magnitude。

  - reward 预算分配上，小预算优先 depth，大预算优先 breadth：即在线先给少量 query 多评几个候选，预算变大后扩 query 覆盖比继续加深候选更划算。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

Dense retriever 用 frozen encoder 和预计算文档索引排序，reranker 或 LLM judge 的强相关性信号通常只服务当前 query 后即被丢弃。更新 retriever 权重能让奖励跨 query 复用，但闭源 API 拿不到权重，大模型 embedding 更新也过重。问题变成：在固定测试时 reward 预算下，如何不碰模型权重和索引，把排序奖励作为可复用状态共享给未见 query。

**方法关键点**

- TTT-Embed 在 frozen embedding 输出空间学习一个轻量残差向量 v_g，query 检索向量变为 unit(x_q + α_g v_g)。只有 v_g 是可学习状态，doc embedding、ANN 索引、相似度函数全部不动。
- 对选中 query 的 top-K 候选，reranker 打分 r；用 softmax(r/τ_T) 构造 teacher 分布，用修正 query 与 doc 内积的 softmax 构造 student 分布，优化 KL + ridge，属于 listwise soft-label 蒸馏。
- 三个 sharing scope：global-wise 跨任务共用一个 v_g；task-wise 单任务一个；query-wise 每 query 私有。实现同一学习规则，只有分组不同。
- 部署幅度采用无调参的 evidence-adaptive 缩放 α_g = n_g/(n_g+1)，其中 n_g 是学习该状态用的 reward query 数，带 Bayesian shrinkage 解释。

**关键实验**

在 15 个 MTEB retrieval 任务、12,263 query、1,661,208 doc 上，覆盖 5 个 embedding 模型，包括两个闭源 Gemini Embedding API。Reward model 默认 Qwen3-Reranker-4B 的 Yes/No logits；与同预算 direct reranking 比较。

- b=10 时，task-wise TTT-Embed 平均 +6.36 nDCG@10，比 direct reranking 的 +3.21 高 3.15。
- b=100 时，query-wise 达到 +8.36 nDCG@10，仍高于 direct reranking。
- 最优 scope 随预算动态转移：极低预算 global 最优，中预算 task 最优，高预算 query 最优。
- 泛化：80% query 提供 reward 时，task-wise 在完全未标注的 20% query 上平均 +5.57；leave-one-task-out 跨任务 +3.09。
- 灾难遗忘恢复：SKILLRET 领域微调后 MTEB 下降 4.49，TTT-Embed 在冻结权重下 +8.00，超过原始基座。

**最值得记住的一句话**

排序奖励不只是当次 rerank 信号，而是可以被压缩进 embedding 空间、按预算选择 global/task/query 复用粒度的测试时状态。
