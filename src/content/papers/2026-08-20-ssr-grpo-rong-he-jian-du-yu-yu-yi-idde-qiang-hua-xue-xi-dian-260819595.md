---
title: 'SSR-GRPO: Integrating Supervision and Semantic IDs into Reinforcement Learning
  for Dense Retrieval in E-commerce'
title_zh: SSR-GRPO：融合监督与语义ID的强化学习电商稠密检索
authors:
- Guangxin Song
- Xing Fang
- Mingmin Jin
- Jing Wang
- Bokang Wang
- Zhentao Song
- Junjie Bai
- Jianbo Zhu
affiliations:
- Alibaba Group
arxiv_id: '2608.19595'
url: https://arxiv.org/abs/2608.19595
pdf_url: https://arxiv.org/pdf/2608.19595
published: '2026-08-20'
collected: '2026-08-21'
category: RecSys
direction: 电商稠密检索 · Semantic ID + RL
tags:
- Dense Retrieval
- GRPO
- Semantic ID
- Hard Negative Mining
- E-commerce Search
- Reward Modeling
one_liner: 用层级语义ID替代大模型裁判并构造难负样本，提升电商稠密检索的RL训练稳定性
practical_value: '- 用 RQ-VAE 学层级 Semantic ID 作为稀疏 relevance 信号：item 量化成 3 层 SID，query
  用 LLM 生成 SID，按前缀匹配深度打分（0/0.25/0.5/1.0），与 dense embedding 融合后替代 Judge LLM。SID-only
  效果已接近 42B MoE 判官，训练成本低且减少裁判偏置，适合电商召回模型 RL 落地。

  - 难负样本构造可复用：Type II 共享前两层 SID、只差第三层的负样本能逼迫模型学细粒度语义边界；Type I 用进入粗排但被精排低分过滤的样本，作为“语义相关但商业弱”的负样本，适合电商
  CTR/CVR 目标。

  - Masking 机制：GRPO 中 top-K 候选里 reward 低于 hard negative 的样本直接 mask 掉，可过滤 batch 内噪声
  easy negatives，缓解 Reward Hacking；类似 DeepSeek V3.2 的 off-policy sequence masking。

  - 多目标联合优化：RL 梯度方差大，用 R-DPO（无 reference policy 的 pairwise margin loss）提供稳定监督梯度，配合
  uncertainty-based dynamic weighting 避免手动调权；同时 SFT 初始化不可省略，RL-only 效果很差。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：R-GRPO 等 RL 稠密检索框架虽有收益，但从 batch 内 top-K 检索的候选噪声大，且用 TaoSR1 42B MoE LLM 算 relevance reward 既昂贵又与训练策略同源，裁判有偏。需要低成本、无偏的 relevance 信号和更稳定的优化。

**方法关键点**
- 用 RQ-VAE 对 item 学 3 层 Semantic ID，query 侧由 LLM 以 next-token-prediction 生成 top-K SID；relevance reward 融合 SID 前缀匹配深度（0/0.25/0.5/1.0）和 dense embedding 内积，α=0.8。
- 利用 SID 层级构造难负样本：商业表现差但语义相关、以及共享前两层 SID 但第三层不同的细粒度难负；基于难负样本设计 masking，过滤 top-K 中 reward 低于难负的 trivial negatives。
- 增加 R-DPO 损失：对(点击正样本, SID难负)最大化 margin，不用 reference policy；与 SID-R-GRPO 用 uncertainty-based dynamic weights 联合优化；GRPO 中用 InfoNCE 代替 KL 作为语义正则。

**关键实验**：基于 0.3B+ Tmall 点击/购买日志，SFT 3 个月 + SSR-GRPO 15 天。Tbstars-3B SFT + SSR-GRPO 在 General/Long-tail 上 HR@4k 达 0.8218/0.5943，GR@100 达 0.9372/0.7195，全面超过 R-GRPO；Long-tail HR@4k 高 0.86%。消融显示去掉 R-DPO 掉 0.49% HR@4k，去掉 dual-perspective reward 掉 0.17% HR@4k、0.25% GR@100。仅用 Sparse SID reward 与 42B TaoSR1 判官 HR@4k 持平（0.8154 vs 0.8152）。线上 A/B：UCTCVR +0.99%，GMV +1.40%，Goodrate +0.61%。

**最值得记住**：用 RQ-VAE 的 SID 层级同时做 relevance reward 和难负样本，可替代大模型裁判并显著提升 RL 检索稳定性。
