---
title: '1% of Tokens Can Be Enough: On Gradient Estimation in On-Policy Distillation'
title_zh: 1% 的 Token 已足够：在线策略蒸馏中的梯度估计
authors:
- Huanxin Sheng
- Zhiling Ye
- Haonan Wang
- Jian Wang
- Jinjie Gu
- Jian Kang
affiliations:
- MBZUAI
- Ant Group
arxiv_id: '2609.24432'
url: https://arxiv.org/abs/2609.24432
pdf_url: https://arxiv.org/pdf/2609.24432
published: '2026-09-20'
collected: '2026-09-22'
category: Training
direction: LLM 稀疏在线蒸馏 token 选择
tags:
- On-Policy Distillation
- Token Selection
- Gradient Estimation
- Information Geometry
- Sparse Distillation
- LLM
one_liner: 提出信息效率比 IER，将有用性与梯度估计可靠性结合做稀疏在线蒸馏 token 选择，0.1%-1% 预算匹配全量 OPD
practical_value: '- 做 LLM 在线蒸馏或生成式推荐模型压缩时，不必全量 token 蒸馏；用 IER 结合 usefulness 做稀疏 token
  监督，0.1%–1% 预算可接近/超过 full OPD，大幅降低 teacher 调用与训练成本。

  - 不要只用 loss 或 uncertainty 选 token；高 useful 的 token 可能梯度估计噪声大，实际更新不稳。可借鉴 IER 的 signal-to-noise
  思路，对 token/样本做梯度可靠性二次筛选。

  - 候选集近似是工程可落地的关键：不必对全 vocab 精确计算梯度方差，用较小候选集估计 IER，能直接嵌入现有 sampled reverse-KL 训练流程，适合工业级
  RLHF/GRPO/蒸馏 pipeline。

  - 若是 Agent/电商文案生成等多步 trajectory 蒸馏，可把 IER 扩展到 step/token 级预算分配，优先在梯度可靠且 teacher
  有信息量的位置蒸馏，节省长轨迹的训练成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**
稀疏在线策略蒸馏（OPD）只在 student 生成的轨迹中选少量 token 接受 teacher 监督，但有用的 teacher 指导可能因从采样 next token 估计梯度而带来高噪声更新。仅按 useful 分数选 token 未必可靠。

**方法关键点**
- 在固定 prefix 下用信息几何分析梯度估计，提出信息效率比 IER，基于 signal-to-noise 分解，刻画最优标量 baseline 下的相对梯度估计误差。
- 用候选集近似估计 IER，可与已有 usefulness 分数结合做 token 选择，训练目标仍是 sampled reverse-KL。
- 保留在线 rollouts 与 token 级稀疏监督，实现极低预算。

**关键结果**
- 在数学和医学推理任务上，加入 IER 提升多种现有 selector。
- 0.1%–1% token 预算下，稀疏配置匹配或超过无 token 选择的 full OPD；证明需同时考虑有用性与梯度估计可靠性。
