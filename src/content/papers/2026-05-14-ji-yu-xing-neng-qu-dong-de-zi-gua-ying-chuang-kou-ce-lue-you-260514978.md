---
title: Performance-Driven Policy Optimization for Speculative Decoding with Adaptive
  Windowing
title_zh: 基于性能驱动的自适应窗口策略优化用于投机解码
authors:
- Jie Jiang
- Xing Sun
arxiv_id: '2605.14978'
url: https://arxiv.org/abs/2605.14978
pdf_url: https://arxiv.org/pdf/2605.14978
published: '2026-05-14'
collected: '2026-05-15'
category: Training
tags:
- Speculative Decoding
- Reinforcement Learning
- LLM Inference
- Window-Level Optimization
- Drafter Training
one_liner: 提出PPOW框架，将草稿模型训练转为窗口级强化学习，结合性能奖励与自适应窗口采样提升投机解码效率
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：投机解码通过小模型提议候选窗口再由大模型并行验证来加速 LLM 推理，但实际加速往往受制于“难草稿”位置——早期 token 不匹配会导致整个窗口作废。现有草稿模型大多仅用 token 级监督训练，与窗口级、前缀敏感的投机效用存在错位。PPOW 正是为了解决这一错位，直接将草稿模型的优化目标对齐到推理时的窗口级接受行为。

**方法关键点**
- **窗口级强化学习**：将投机解码的训练建模为在投机窗口上的策略优化，对同一前缀采样 G 个窗口构成 rollout 组，计算组相对优势，使用 PPO 风格的剪切目标与 KL 惩罚（以目标模型而非初始化策略为锚）进行更新。
- **性能驱动奖励**：主奖励为 Cost-Aware Speedup Reward `k / (kγ + 1)`（k 为接受长度，γ 为草稿模型相对成本），直接鼓励长接受前缀的同时考虑成本权衡；辅助奖励 Distribution-Based Proximity Reward 在验证截断（k=0）时仍对与目标模型偏好窗口足够接近的草稿窗口给予部分信用。
- **自适应发散感知窗口采样（ADAW）**：计算每个位置的置信度加权 KL 散度 `v_t = C(P_t) ⋅ D_KL(P_t‖Q_t)`，聚合为窗口级关键性分数，优先选择那些高发散、高置信度的训练窗口，使优化聚焦于接受瓶颈位置。

**关键结果**
- 在 LLaMA-3‑8B/70B、Qwen3‑8B/32B 上，温度 0.0 时 PPOW 的平均接受长度达 6.29–6.52，加速比 3.39–4.36×，均优于 EAGLE‑3、GRIFFIN。
- 相比同样步数的继续监督训练，PPOW 接受长度持续提升（6.50 vs. 5.47），且监督训练后期出现退化。
- 消融实验：移除 Distribution-Based Proximity 奖励和 ADAW 均导致明显性能下降；完整方法在较小的推理候选组大小下即可获得高接受长度，表明更高效的候选预算利用。
