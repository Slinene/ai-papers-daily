---
title: Empowering Compact LLMs with Fusion of Layer-wise Exits for Recommendation
title_zh: 层退出融合增强紧凑 LLM 的判别式序列推荐
authors:
- Xurong Liang
- Tong Chen
- Quoc Viet Hung Nguyen
- Jianxin Li
- Xiangliang Zhang
- Hongzhi Yin
affiliations:
- The University of Queensland
- Griffith University
- Edith Cowan University
- University of Notre Dame
arxiv_id: '2608.17316'
url: https://arxiv.org/abs/2608.17316
pdf_url: https://arxiv.org/pdf/2608.17316
published: '2026-08-18'
collected: '2026-08-19'
category: RecSys
direction: 判别式 LLM 推荐 · 层退出动态融合
tags:
- Layer-wise Exits
- Compact LLM
- Sequential Recommendation
- Mixture-of-Experts
- Discriminative LLM-RS
- Adaptive Routing
one_liner: 在判别式 LLM 推荐中引入多层预测出口与连续路由器，以紧凑模型实现全库排序并逼近大模型精度
practical_value: '- 判别式 LLM 排序范式可直接用于召回/粗排全库打分：用预训练 SASRec ID embedding 投影进 LLM，取
  response token 表示做 softmax，避免自回归解码，单用户推理 6-9ms，适合线上候选集大但算力受限的场景。

  - 多层 exit 融合是补偿小模型的有效 trick：在 compact LLM 每层后接预测头，融合不同深度分数，实验在 Toys/Beauty/Yelp
  上以 1.7B/3B 模型超过部分 4B/8B E4SRec，说明深度集成可替代盲目上大模型。

  - 连续 ReLU 路由 + target-k hinge loss 可按用户序列复杂度动态选择 1~k 个 exit，避免固定 top-k 对简单序列浪费、复杂序列不足；该路由仅需训练一个投影矩阵，无额外参数，便于线上轻量自适应推理。

  - 三阶段冻结训练允许共享同一 backbone 训练多个不同 target-k 的路由器，用于不同设备算力预算（GPU/CPU/边缘），对电商多端部署有直接参考价值；Z-loss
  和 load balancing 可保证混合精度训练稳定。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

LLM-RS 虽强但大模型在线计算不可持续；紧凑 LLM 容量有限，生成式或推理/蒸馏方案加剧延迟。判别式 LLM-RS 能全库排序，但小模型 embedding 质量低，且所有用户都走固定深度管线，缺乏对偏好复杂度的自适应。

**方法关键点**

- 基于 E4SRec 判别式架构：将 SASRec 预训练 item ID embedding 线性投影到 LLM 语义空间，拼接 instruction、item、response token，经 L 层 Transformer；在每一层后插入 prediction head 形成 L 个 exit，各自产生 softmax 分数 \(O_l\)。
- AC-Router：取第一层 response token 表示映射为 L 维 logits，经 ReLU 和条件 shift 保证至少一个 exit 激活，归一化得到 \(g_l\)；融合分数 \(O_{fused}=\sum_{l\in A} g_l O_l\)，只前向到最深 active exit，后续层跳过，实现动态 depth pruning。
- 三阶段训练：Stage1 只训练 ID 投影、LoRA、final exit；Stage2 冻结主干和 final exit，训练所有中间 exits；Stage3 冻结全部 backbone 与 exits，仅训练 router 的 \(W_z\)。
- 损失设计：target-k hinge loss 用 sigmoid 估计 active exit 数量 C，惩罚 C>k 和 C<1，使每个序列选择 1~k 个 exits；load balancing loss 用 Softmax proxy 防止路由塌缩；Z-loss 约束 raw logits，保证混合精度训练稳定。

**关键结果**

在 Toys、Beauty、Yelp 三个真实数据集上，使用 Qwen 3 1.7B 和 Llama 3.2 3B 作为 backbone。FLEXRec 在多数 N@10/N@20 指标上超过同 backbone E4SRec，并在 Beauty 两个 backbone 和 Yelp-Qwen 上超过 4B/8B Skyline E4SRec：例如 Beauty-Qwen N@10 0.0451 vs Skyline 0.0435，Yelp-Qwen N@10 0.0207 vs Skyline 0.0199。推理延迟相比 E4SRec 增加不到 1ms。

**最值得记住的一句话**

用连续路由融合 LLM 各层“出口”的推荐分数，能在不依赖大模型或自回归解码的情况下，以紧凑模型逼近甚至超过大模型判别式推荐效果。
