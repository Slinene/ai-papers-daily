---
title: 'SWIM: Step-Wise Integrated Measure for Session-supervised List Evaluation
  in Generative Re-ranking'
title_zh: SWIM：生成式重排中会话监督列表评估的逐步积分测度
authors:
- Yuanhao Pu
- Chenghao Zhang
- Chao Feng
- Xunyong Yang
- Xiang Li
- Yongqi Liu
- Defu Lian
- Kaiqiao Zhan
- Kun Gai
affiliations:
- University of Science and Technology of China
- Kuaishou Technology
arxiv_id: '2608.25104'
url: https://arxiv.org/abs/2608.25104
pdf_url: https://arxiv.org/pdf/2608.25104
published: '2026-08-25'
collected: '2026-08-27'
category: RecSys
direction: 生成式重排评估 · session 级生存建模
tags:
- Generative Re-ranking
- Listwise Evaluation
- Survival Analysis
- Session-aware
- Generator-Evaluator
- Recommender Systems
one_liner: 将重排 list 评估建模为有限时域生存过程，用因果 Transformer 并行估计 continuation 与 reward
practical_value: '- **用 survival 加权替代 pointwise 加和**：短视/短视频 feed 的 list 价值不应是 item
  reward 直接相加。可以把当前 list 贡献写成 Σ(Π q_t) r_t，其中 q_t 是位置 t 的继续概率，r_t 是到达位置后的条件收益。这套公式能直接迁移到重排
  evaluator，尤其适合 session 连续消费场景。

  - **用 causal-masked Transformer 并行估计 q_t 与 r_t**：在 [prefix token, item_1..item_T]
  上做因果注意力，每个位置输出 continuation probability 和 reward heads，一次 forward 得到整条 list 评估。这样避免自回归
  rollout，满足工业延迟约束；prefix token 编码 session prefix，可同时估计跨 request 的进入概率 q_0。

  - **连续目标做离散 bucket 分类**：play time 等长尾连续反馈不要直接回归，而是离散为有序 bucket 预测 categorical distribution，再取
  bucket 代表值恢复期望；训练更稳定，适合多目标 reward 融合。

  - **训练时只在 reached positions 计算 survival/reward loss**：reward 是到达位置后的条件收益，未到达位置不应参与
  reward 监督；survival BCE 也只在已到达位置有效。这个 masked loss 设计能避免 selection bias，工业日志可直接复用。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

现代工业推荐重排广泛采用 Generator-Evaluator（G-E）框架：generator 生成多个候选列表，evaluator 打分选最优。但现有 evaluator 通常按单次请求做 pointwise 聚合，默认请求之间、列表之间独立。在短视频等连续 feed 中，用户跨请求连续消费，当前 list 会影响用户是否继续 session，因此需要 session 级 list evaluator。

**方法关键点**

SWIM 把当前 list 对 session 的贡献建模为有限时域生存过程，分解为两部分：递归生存分布和到达位置后的条件收益。

- 定义 session-wise list contribution 为 `Σ_{t=1..T} S_t r_t`，其中 `S_t = Π_{i=0}^{t-1} q_i`，`q_i` 是 step-wise continuation probability，`r_t` 是到达位置 t 后的条件 reward。
- 引入 prefix token 放在序列位置 0，编码 session prefix、历史反馈、累积 session 参与度等，用于估计 request-entry probability `q_{k,0}`；在线推理时请求已经触发，因此固定 `q_{k,0}=1`。
- 使用 causal-masked Transformer 一次前向并行估计所有 `q_t` 和 `r_t`，避免自回归 rollout，满足工业延迟。
- 训练损失只有 survival BCE 和 reward loss；survival loss 只在已到达位置计算，reward loss 也只监督 reached positions。连续目标如 play time 离散为有序 bucket 做分类。

**关键实验**

在 RecFlow 和 KuaiRand 两个公开数据集上对比 DNN、Seq2Slate、DLCM、SetRank、PRM、SORT-Gen、NAR4Rec、PIER、MultiG、CAVE。RecFlow 上 SWIM 取得 NDCG@6 0.2031、AUC 0.7185，相比最强 baseline CAVE 分别提升约 +0.0074 NDCG 和 +0.0102 AUC；KuaiRand 上同样领先。消融显示 session prefix、boundary `q_{k,0}`、recursive survival chain 均带来稳定提升。快手真实流量 7 天 A/B 中，SWIM 替换 CAVE 后 App stay time 相对提升 +0.351%，LT7 留存提升 +0.048%。

**最值得记住的一句话**

把 list 价值从 pointwise 加和改成 survival-weighted reward accumulation，并用 causal Transformer 并行估 `q_t` 和 `r_t`，是低延迟获得 session 级收益的关键。
