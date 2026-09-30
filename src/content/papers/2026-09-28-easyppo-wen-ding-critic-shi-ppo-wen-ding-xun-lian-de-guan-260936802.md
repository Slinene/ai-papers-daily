---
title: 'EasyPPO: Stabilizing the Critic Is Key'
title_zh: EasyPPO：稳定 Critic 是 PPO 稳定训练的关键
authors:
- Xuanyi Zhou
- Qiuyang Mang
- Huanzhi Mao
- Dacheng Li
- Wenhao Chai
- Mayank Mishra
- Yichuan Wang
- Karthik Narasimhan
- Alvin Cheung
- Joseph E. Gonzalez
affiliations:
- University of California, Berkeley
- Princeton University
arxiv_id: '2609.36802'
url: https://arxiv.org/abs/2609.36802
pdf_url: https://arxiv.org/pdf/2609.36802
published: '2026-09-28'
collected: '2026-09-30'
category: Training
direction: RLVR / PPO 训练稳定性优化
tags:
- PPO
- RLVR
- Critic Stability
- Variance Weighting
- LLM Post-training
- Overlong Filtering
one_liner: 通过 actor-only 截断过滤、按回报方差加权 critic 损失和较小 critic mini-batch，稳定 PPO 训练并全面优于现有方法
practical_value: '- 若在搜索/推荐 Agent 或生成式排序中用 PPO/RLVR 训练 LLM，不要同时对 actor 和 critic 过滤超长
  rollout：截断样本保留给 critic 学习，能避免策略偏向“早点截断也能拿到的条件奖励”，同时 actor 侧只过滤截断样本仍可降低噪声。

  - 当不同 query / 用户组 / 问题上的 reward 方差差异很大（如连续奖励：转化金额、延迟、GPU kernel 加速比等），对 critic loss
  使用 prompt 组内回报标准差的倒数加权，可以在现有分组采样 rollout 的框架下低成本实现，防止少数高方差 prompt 主导 critic 更新。

  - 工程上 critic mini-batch 不必等于整个 rollout batch；默认切成 4 个 mini-batch 并做 gradient clipping，能限制
  outlier 影响范围。若改变 mini-batch 数，记得按 η ∝ 1/√K 调整 critic 学习率。

  - 训练监控可以看 critic 的 explained variance 和 clip 前 gradient norm；持续大幅波动或 EV 突然下降通常是
  critic 失效的前兆，可作为在线崩溃预警。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
PPO 在 LLM 的 RLVR 后训练中常用，因为 critic 提供 token 级回报估计，能降低策略梯度方差。但作者发现 critic 本身是不稳定的重要来源，并识别出两种 failure mode：
1. 截断 rollout 如果同时从 actor 和 critic 中过滤，critic 学会的是“已完成响应中的平均回报” E[R|s, not truncated]，策略目标退化为只优化条件奖励，可能让截断率升高、整体奖励变差。
2. 不同 prompt 的回报噪声差异很大，高方差 prompt 在有限 batch 中会通过梯度二阶矩主导 critic 更新，尤其在连续奖励任务中更明显。

## 方法关键点
EasyPPO 只改 critic 侧，保留标准 PPO actor 更新：
- **Actor-only overlong filtering**：截断 rollout 不参与 actor loss，但保留给 critic 训练，使 critic 目标恢复为 E[R|s]，保留完成概率信号。
- **Noise-normalized critic regression**：对每个 prompt 按组内回报标准差的倒数加权 critic loss，权重归一化到 batch 均值；离散 reward 用 ε=Δ/(2√n) 做方差 floor。
- **Moderately smaller critic mini-batches + gradient clipping**：默认把 rollout batch 切成 4 个 critic mini-batch，每个 mini-batch 单独 clip gradient norm 后更新，限制 outlier 对更新方向的影响。

## 关键实验
在三个任务上对比 vanilla PPO、PPO+actor-only filtering、HL-Gauss PPO、VAPO：
- FrontierCS 连续奖励 coding
- AIME24 二值奖励数学推理
- Search-R1 多轮搜索

EasyPPO 在整段 200–300 步训练中保持稳定，而所有 baseline 至少在一个任务上出现后期 collapse。最佳验证分数相对 PPO 分别提升 **14.89%、2.28%、9.47%**，且是唯一三个任务都稳定的方法。消融显示噪声归一化在不同 critic mini-batch 配置下都能提高稳定性，K=4 是早期 outlier 控制与后期噪声平均之间的较优点。

最值得记住的一句话：**稳定 PPO 训练的关键在于稳定 critic——不要从 critic 里丢掉截断样本，按回报方差归一化 critic 损失，并用较小 mini-batch 配梯度裁剪控制 outlier。**
