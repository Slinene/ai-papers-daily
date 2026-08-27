---
title: On-policy Distillation with Verifiable Reward
title_zh: 基于可验证奖励的在线策略蒸馏
authors:
- Wenze Lin
- Jiale Zhao
- Xitai Jiang
- Songde Rao
- Yining Li
- Shenzhi Wang
- Bingxiang He
- Gao Huang
affiliations:
- LeapLab, Tsinghua University
- Beihang University
- SMS, Peking University
- NLPLab, Tsinghua University
arxiv_id: '2608.24696'
url: https://arxiv.org/abs/2608.24696
pdf_url: https://arxiv.org/pdf/2608.24696
published: '2026-08-24'
collected: '2026-08-27'
category: Training
direction: RLVR+OPD 无缝结合训练推理模型
tags:
- RLVR
- On-policy Distillation
- GRPO
- Reasoning
- Policy Optimization
- Distillation
one_liner: 对采样 token OPD 的 log-ratio 奖励做 ReLU 门控，使教师信号与轨迹正确性对齐，零超参结合 OPD 与 RLVR
practical_value: '- **可直接复用的训练 trick**：若业务中已有可验证奖励（点击、转化、GMV 等）和教师模型或旧版模型，可在 on-policy
  蒸馏损失中只加一行 ReLU 门控——正确轨迹上 `max(0, log(πT/πθ))`，错误轨迹上 `-max(0, log(πθ/πT))`，无需额外超参或
  loss 权重，即能避免教师信号与业务奖励方向冲突。

  - **GRPD 替换二元 reward**：用 GRPO 的 group-relative advantage 替换二元正确性 sign，再做同样的 ReLU
  gate，可平滑引入相对优势信息；适合推荐/广告中 reward 噪声大、需要组内归一化的场景。

  - **训练健康度监控指标**：论文观察到 zero-gated token ratio 稳定在 40-50%，可作为训练健康的实时监控；如果该比例过高或过低，说明教师信号与业务奖励大量冲突或几乎无冲突，需要检查教师模型质量或
  reward verifier。

  - **架构兼容性**：该方法可无缝接入现有 PPO/GRPO/DAPO 训练框架，不改变采样流程；在已有的 RL 训练脚本中实现成本低，适合快速验证。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**

RLVR 提供稀疏但可靠的任务级正确性信号，OPD 提供密集但忽略轨迹正确性的 token 级教师分布引导。两者互补，但现有结合方式往往引入额外超参数或启发式切换。

**方法关键点**

- 从 RLVR 视角重新解读 sampled-token OPD：其隐式 token 奖励为 `log(πT/πθ)`，但符号完全由师生概率比决定，与轨迹正确性无关，导致正确轨迹上学生自信更高时被惩罚、错误轨迹上教师自信更高时被奖励。
- 提出 OPDVR：对采样 token 的 log-ratio 施加 ReLU 门控。正确轨迹（R=+1）奖励为 `max(0, log(πT/πθ))`，错误轨迹（R=-1）惩罚为 `-max(0, log(πθ/πT))`。该门控保证所有 token 更新方向与 verifier 梯度一致，同时保留教师分布的大小信息。
- 理论分析：OPDVR 更新方向与纯 verifier 梯度永不夹角为负；等价于从标准 OPD 梯度中精确移除与 verifier 对抗的冲突项。
- 扩展 GRPD：用 GRPO 的 group-relative advantage `Â` 替代二元 reward，用 `sign(Â)` 控制方向，得到更稳定的 group-relative 蒸馏。

**关键结果数字**

- 同架构蒸馏（Qwen3-4B←Qwen3-4B-RL），六个推理基准平均：OPDVR 49.1，sampled-token OPD 47.8，top-64 OPD 47.4，teacher 50.4。
- 跨架构蒸馏（Qwen3-1.7B-Base←Qwen3-4B-Base-RL）：OPDVR 22.8，sampled-token OPD 20.9，top-64 OPD 21.7。
- GRPD 在 DAPO-Math-17K 上平均 49.4，超过 GRPO 44.8 和 OPD 48.4；AIME25 上 GRPD 31.7 vs GRPO 20.8。
- 逆门控消融：平均 44.6，远低于 OPD 47.8，证明门控方向正确。
- 训练动态：zero-gated token ratio 稳定在约 50%，即有近一半 token 的蒸馏信号被门控移除，且不随训练退化。

**最值得记住的一句话**：ReLU 门控让 on-policy 蒸馏的 token 级教师信号与可验证业务奖励方向对齐，几乎零成本地将 OPD 变成有效 RLVR，还能与任何 policy gradient 算法组合。
