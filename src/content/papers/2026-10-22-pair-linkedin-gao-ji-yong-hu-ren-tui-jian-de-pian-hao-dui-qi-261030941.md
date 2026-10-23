---
title: 'PAIR: Preference-Aligned Intent Retrieval for Premium People Recommendation
  at LinkedIn'
title_zh: PAIR：LinkedIn 高级用户人推荐的偏好对齐意图检索
authors:
- Zhongkai Shangguan
- Yanbin Kang
- Yihan Cao
- Ruijie Jiang
- Qiannan Yin
- Chang Yue
- Zijian Zhou
- Girish Kathalagiri
- Changshuai Wei
- Zhengming Xing
affiliations:
- LinkedIn
arxiv_id: '2610.30941'
url: https://arxiv.org/abs/2610.30941
pdf_url: https://arxiv.org/pdf/2610.30941
published: '2026-10-22'
collected: '2026-10-23'
category: RecSys
direction: 偏好对齐检索 · LLM Embedding
tags:
- embedding retrieval
- preference learning
- LLM
- history modeling
- Matryoshka
- people recommendation
one_liner: 用曝光条件偏好对比学习与可增量更新的历史注意力，将 LinkedIn Premium 人推荐检索 MAR@100 提升 56%，线上 CTR
  +7.5%
practical_value: '- **用「曝光未点击」当负样本，而不是随机负样本**：把生产日志里同批次曝光但未点击的候选作为难负例，随机样本作为易负例，可以让召回模型直接对齐线上检索策略的曝光分布，比
  ANN 硬负挖掘更贴合真实曝光偏差。电商/广告召回可以直接复用这个负样本构造思路，尤其是多路召回混合的场景。

  - **静态画像与动态意图分离，行为更新只在 embedding 空间做**：Profile tower 和 Document tower 离线预计算，用户历史用最近
  K 个点击 item 的预计算 embedding + positional attention 聚合成意图向量，更新复杂度 O(Kd)，不需要在线重过 LLM。适合大规模实时个性化，对需要频繁更新用户表示的推荐系统尤其有价值。

  - **Matryoshka 训练让一个模型同时服务多种维度预算**：在训练时同时对 200/256/512/1024 维前缀计算 loss，线上可按 latency/storage
  截断，不需要为不同业务线训练多个模型。电商多场景召回/粗排可以合并训练，降低模型维护成本。

  - **工程细节可直接抄**：bf16 而非 fp16 防止 DeepSpeed 梯度溢出；温度设 0.02；离线指标优先看 MAR@k，ACC 在小候选集容易饱和，MAR@k
  更能反映排序召回质量。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：专业社交网络中的用户交互往往是非对称、目标驱动的，比如求职者更常点击招聘者而不是背景相似的工程师。但 LinkedIn 生产通用用户 embedding（Holistic-171）和通用 LLM embedding 都偏向 profile 相似性，导致 Premium Browsemaps 人推荐召回质量不足，线上 MAR@100 分别只有 0.288 和 0.192。问题本质是：召回需要学习曝光条件下的偏好，而不是语义相似。

**方法关键点**：
- **曝光条件偏好学习**：把生产日志中的「点击」作为正样本，「同会话曝光但未点击」作为难负样本，「随机采样」作为易负样本，用多负对比学习的目标训练，不引入显式 reference model，也避开了 DPO 的 token 级优化。
- **Triple-tower 架构**：Query profile tower 和 document tower 共享编码器，history tower 用最近 K=10 个点击用户的预计算 embedding 做位置注意力聚合，再与归一化后的 profile embedding 做可学习加权的 normalized additive fusion。
- **增量更新**：历史更新只需要 O(Kd) 向量操作，不需要在线 LLM re-inference，适合每日/近实时刷新。
- **Matryoshka 训练**：在 {200,256,512,1024} 四个前缀维度上同时优化，一个模型支持多档 dim 截断。

**关键结果**：PAIR 从 0.6B Qwen embedding 基座微调后，P-ATT history 版本在 Premium 检索基准上 MAR@100 达 0.450，比生产 Holistic-171 提升 56%，是 off-the-shelf 0.6B embedding 的 2.3 倍；即使无 history 的 two-tower 也达到 0.436。线上 A/B 测试 CTR +7.5%，Premium retention +2.1%，latency 与 coverage 无显著退化。

最值得记住的一句话：在推荐召回中，把目标从「语义相似」改成「曝光条件下的偏好对齐」，往往比换更大的模型更有效。
