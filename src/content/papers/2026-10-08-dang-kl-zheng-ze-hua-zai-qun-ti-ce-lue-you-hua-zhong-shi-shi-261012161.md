---
title: When KL Regularization Misfires in Group Policy Optimization
title_zh: 当 KL 正则化在群体策略优化中失灵时
authors:
- Fei Ding
affiliations:
- Alibaba Group
arxiv_id: '2610.12161'
url: https://arxiv.org/abs/2610.12161
pdf_url: https://arxiv.org/pdf/2610.12161
published: '2026-10-08'
collected: '2026-10-10'
category: Training
direction: RLHF/GRPO 训练稳定性优化
tags:
- GRPO
- KL Regularization
- RLHF
- Policy Optimization
- Training Stability
- ZCPO
one_liner: 系统分析 GRPO 中参考 KL 与奖励交互的七种失效模式，提出条件 KL 标定组内奖励系数的 ZCPO
practical_value: '- 在电商/广告/Agent 场景用 GRPO 类方法做 LLM 策略优化时，若显式 reference KL 导致奖励收敛慢或指标波动，可尝试去掉
  KL 项或改用条件 KL 只用在校准组内奖励系数，而非独立正则项。

  - 对于文案生成、搜索词推荐等变长输出任务，注意 KL 会随 response length 增长且可能集中在少数 token，造成长度偏置；可考虑 per-token
  或条件归一化，避免长文本被过度惩罚。

  - 当组内样本 reward 相同或梯度取消时，独立 KL 梯度不会完全抵消，仍会推动策略漂移；可在组内 reward 方差接近 0 时关闭 KL 更新，或采用
  ZCPO 式相对漂移标定。

  - 将 KL 估计直接加入 reward 会引入采样噪声，建议分离 KL 估计与 reward 计算，并使用更稳健的组内相对校准系数。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：为什么移除 reference-policy KL 正则有时能提升 GRPO 系列方法？已有实验显示 PAPO 移除参考 KL 后 Qwen2.5-VL-3B/7B 的多模态推理 avg@8 分别从 47.92% 提高到 50.18%、从 58.78% 提高到 61.30%；Open-Reasoner-Zero 的文本推理消融也表明 PPO 无 KL 优于加 KL 的变体。

**方法关键点**：论文系统梳理了 KL 与奖励交互的七种失效模式：reward clipping 后残留 KL 更新、梯度取消后残留、组内 reward 相同时 KL 仍更新、KL 随 response length 增长、KL 相对贡献不平衡、KL 集中于少数 token、以及将 k1 纳入 reward 时引入采样噪声。在此基础上提出 ZCPO：用条件 KL 测量相对漂移，标定组内奖励系数，并集成到基础 surrogate 中，使参考策略信息只通过组内相对校准起作用，而非作为独立正则项。

**关键结果**：数学推理实验和消融验证了 ZCPO 设计的有效性；在受控设置下，去 KL 或采用条件 KL 校准相比传统 GRPO 变体更稳定，避免 KL 与奖励梯度的冲突。
