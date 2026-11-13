---
title: 'KuaiRecV2: Benchmarking Large-Scale Continual Learning for Diversified and
  Multi-task Recommendation'
title_zh: KuaiRecV2：面向多样化多任务推荐的大规模持续学习基准评测
authors:
- Chenxu Li
- Shuchang Liu
- Hantao Shu
- Wei Yuan
- Zhe Xu
- Guoqing Hu
- Yan Wang
- Biao Yang
- Xiang Li
- Cheng Ling
affiliations:
- University of Science and Technology of China
- Kuaishou Technology
arxiv_id: '2611.16795'
url: https://arxiv.org/abs/2611.16795
pdf_url: https://arxiv.org/pdf/2611.16795
published: '2026-11-12'
collected: '2026-11-13'
category: GenRec
direction: 生成式推荐 · 持续学习评测基准
tags:
- Generative Recommendation
- Continual Learning
- Semantic ID
- Multi-task
- Diversity
- Benchmark
one_liner: 构建含 24M 物品、484M 交互的 30 天动态候选池基准，系统评估生成式推荐的持续学习、多样性及多任务表现
practical_value: '- 动态候选池与持续学习评估：借鉴 7 天滑动窗口和跨日历史拼接，在电商商品池中模拟每日上新/下架；用 Replay buffer（5%
  旧样本）缓解灾难性遗忘，比 EWC LoRA 更实用。

  - 生成式推荐的 token 级多样性：SID 后几层 token 高度偏差，需在 beam search 中加入 token 级别多样化约束（如熵正则或 DPP），而非只做
  item 级融合；可直接用于电商语义 ID 生成。

  - 多任务 RL 与 SFT 交替：RL-only 对分布漂移脆弱，业务中应先用 SFT 在新数据上微调再做 RL 对齐；多行为 reward 加权需谨慎，先验证任务相关性（related
  behaviors 指标相近）。

  - 统一评估门槛：要求新方法同时提升准确率、多样性、多任务所有指标才算有效，避免单一 NDCG 过拟合；可迁移到推荐系统离线评测标准。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
离线评测与线上效果不一致是推荐系统的长期痛点，在 LLM-style generative recommenders 兴起后更加突出。现有 benchmark 多为静态物品池、单任务、忽略持续学习动态，难以反映真实生产环境。需要一个大规模、多模态、多任务、动态候选池的评测基准。

**方法关键点**
- 数据集 KuaiRecV2-FullMonth：124,055 用户、24,898,648 物品、484,045,145 交互，跨度 30 天；另有 Small 子集（前 2 天）。
- 为每个物品提供 64 维多模态 embedding、8 级 RQ-VAE Semantic ID、MLLM 推断 tag。
- 长期推荐 pipeline：每日训练，7 天滑动窗口候选池，跨日历史拼接避免序列断裂。
- 评估体系：检索准确性（NDCG, HR）；多级多样性（item 级 Gini、Coverage，token 级路径多样性、唯一 token 数、熵）；多任务行为（click, long view, like, follow, forward, comment, search, profile enter, hate）。
- 实现 baseline：SASRec, GRURec, LLaDA-Rec, TIGER, MiniOneRec；支持 SFT 与 RL 训练策略。

**关键结果数字**
- 生成式模型显著优于传统：MiniOneRec NDCG@50 19.22×10⁻³ vs SASRec 1.92×10⁻³；HR@50 62.63×10⁻³ vs 6.61×10⁻³。
- 模型容量重要：MiniOneRec (0.5B) > TIGER-Small (30M) > TIGER-Tiny (4.9M)，且最小生成式模型仍优于传统模型。
- 持续学习灾难性遗忘严重：MiniOneRec Day1 HR@50 39.09，Day7 降至 0.19；加入 Replay 5% 可保留至 3.20，EWC LoRA 改善有限。
- RL-only 在动态候选池下不稳定：Day21 性能骤降，需与 SFT 交替训练才能稳定。
- 多样性差：Gini 系数 >0.86，coverage 极低；token 级后几层几乎无多样性，Top1 层 diversity 始终为 1。

**最值得记住的一句话**
动态候选池下的持续学习、token 级多样性控制和多任务平衡，是生成式推荐从离线刷榜走向线上落地的三个关键瓶颈，且 RL-only 必须与 SFT 协同才能应对分布漂移。
