---
title: 'Sequential Beats Joint: On the Interplay between On-Policy Distillation and
  RLVR'
title_zh: 顺序优于联合：On-Policy 蒸馏与 RLVR 的相互作用
authors:
- Boyan Li
- Bingsen Chen
- Chenghao Yang
- Ping Nie
- Chen Zhao
- Xi Ye
affiliations:
- University of Alberta
- New York University
- NYU Shanghai
- University of Chicago
- University of Waterloo
arxiv_id: '2609.04108'
url: https://arxiv.org/abs/2609.04108
pdf_url: https://arxiv.org/pdf/2609.04108
published: '2026-09-03'
collected: '2026-09-04'
category: Training
direction: RLVR 与 On-Policy 蒸馏两阶段后训练
tags:
- RLVR
- On-Policy Distillation
- GRPO
- OPD
- LLM Post-training
- Reasoning
one_liner: 两阶段 OPD-then-RL 在逻辑与数学推理上稳定优于纯 OPD、纯 RLVR 及所有同一步混合的方法
practical_value: '- 若业务中有稠密教师信号（大模型打分/业务规则）与稀疏奖励（点击、转化），不要每步加权融合；先跑 OPD 把模型推到教师支撑边界，再切
  RL 做 reward sharpening，可避免梯度信号打架。

  - 切换时机用 OPD 的离线验证分数：验证分数饱和后再切 RL，否则会过早封顶最终效果；电商/推荐里可对应用离线 AUC/召回，验证不再提升时再上策略梯度。

  - OPD 冷启动优于离线 SFT：推荐/广告中若只有日志式行为克隆，尝试 on-policy rollout + 教师 soft label 蒸馏，可扩大长尾
  query/item 覆盖，再进入 RL 收益更明显。

  - 监控 sign conflict ratio 可发现 RL 是否破坏教师阶段的关键参数方向；对 embedding 或 attention 层可设不同保护等级。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
RLVR 与 on-policy distillation (OPD) 是推理 LLM 后训练两大主流。RLVR 只提供序列级稀疏奖励，OPD 提供稠密 token 级教师信号，但只优化行为代理，不直接最大化任务奖励。已有方法在同一训练步内融合两者，或加权相加，或用教师调制 RL advantage；简单两阶段方案未受重视。

**方法关键点**
- 统一 token 级策略梯度视角，将现有混合方法归为两类：weighted-additive（KDRL、KDRL-mask、SRPO、HDPO）与 teacher-modulated（TRRD、RLSD）。
- 提出 **OPD-then-RL**：先用 OPD 训练学生到教师分布支撑，再硬切换为纯 GRPO。
- 学生用 Qwen3-1.7B-Base / 0.6B，教师用 Qwen3-8B；逻辑任务来自 Reasoning Gym（Knights & Knaves、Zebra、Countdown），数学任务训练 DeepMath-103K，评估 MATH-500、AMC23、AIME24/25。
- 分析 pass@k、学习动力学（KL/熵/交叉熵）与参数更新 sign conflict ratio。

**关键结果**
- OPD-then-RL 逻辑平均 pass@1 达 80.6，数学 31.8，均超过纯 OPD、纯 RL 及所有联合 baseline；逻辑上比联合方法高 11.7–26.7 个点，数学上与最强三方法打平但 pass@32 未被超越。
- pass@k 显示：OPD 扩大学生可解决题目覆盖（大 k 提升），RL 在教师支撑内锐化概率到 pass@1；联合优化使二者相互干扰，同时牺牲覆盖面与锐化。
- 切换点方面，OPD 验证分数是决定后续 RL 效果的关键信号；OPD 冷启动优于同等 teacher 下的 SFT，差距在 RL 后进一步扩大。

**最值得记住的一句话**
把 OPD 和 RLVR 从同一步内的纠缠信号改成前后两阶段，能解耦“能力扩展”与“奖励锐化”，这是简单且稳定的后训练方案。
