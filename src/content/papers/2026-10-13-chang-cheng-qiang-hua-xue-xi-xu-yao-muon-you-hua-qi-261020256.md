---
title: Long-Horizon RL Needs Muon
title_zh: 长程强化学习需要 Muon 优化器
authors:
- Kai Ruan
- Jinghao Lin
- Tao Chen
- Ziqi Zhou
- Qianshan Wei
- Zihe Huang
affiliations:
- Renmin University of China
- Duke University
- Institute of Automation, Chinese Academy of Sciences
- Institute of Computing Technology, Chinese Academy of Sciences
arxiv_id: '2610.20256'
url: https://arxiv.org/abs/2610.20256
pdf_url: https://arxiv.org/pdf/2610.20256
published: '2026-10-13'
collected: '2026-10-15'
category: Training
direction: Agent RL 优化器与训练 recipe
tags:
- Muon
- RL
- Agent
- Asynchronous
- Importance Sampling
- Reward Shaping
one_liner: 在仓库级 issue 修复的异步 RL 中，Muon 配合单 rollout、TIS 与奖励塑形显著提升训练成功率
practical_value: '- 训练多轮交互 Agent（对话式推荐、商品搜索助手）时，可尝试隐藏权重矩阵换用 Muon，其余 embedding/output
  head/norm/vector 保持 AdamW；稀疏奖励长轨迹任务中 Muon 的谱范数约束可能带来更稳更新，但需监控 collapse，Adam 与 Muon
  差距会受 recipe 影响。

  - 线上已有旧策略产生的轨迹时，可复用单 rollout 异步训练 + 截断重要性采样：按 token 计算 π_train_old / π_rollout 比值并截断到
  [0,2]，再加权 PPO loss；不必等待同 issue 多条轨迹，适合电商 Agent 环境异步执行时策略滞后场景。

  - 对过长回复、无效工具调用加负奖励，但建议将单独或组合 penalty clip 到 [−0.25,0.25] 再加到 advantage 并标准化，避免惩罚过重破坏策略；长度惩罚在最终回合可省略。

  - Ablation 显示 length penalty 影响大、tool-error penalty 影响相对较小且不一定稳定；不要盲目堆 penalty，先做单组件实验。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
仓库级 issue 修复要求 agent 进行多步推理、工具调用与环境反馈，属于典型长程任务。稀疏二进制奖励下训练难点在于：不同长度轨迹的加权方式、异步 rollout 与 learner 策略之间的滞后、以及优化器在非平稳数据上的稳定性。现有单 rollout 异步 RL 方法多默认使用 Adam，本文对比 Muon 并研究其与不同 recipe 组件的组合效果。

## 方法关键点
- 基于 SPO / SPO++ 的单 rollout 异步策略优化，不等待同一 issue 多条轨迹即可更新。
- 优化器：隐藏权重矩阵用 Muon（谱范数约束、Newton–Schulz 近似正交化），embedding、output head、norm 与向量参数用 AdamW。
- 损失聚合：token-level 平均，排除环境观测 token；PPO clip 采用 DAPO Clip-Higher（低 0.2、高 0.28）。
- 截断重要性采样 TIS：对每个 token 计算 π_train_old / π_rollout 权重并截断到 2，直接加权 masked PPO loss，不进行 batch 归一化。
- 奖励塑形：二元 outcome 之外，引入长度惩罚（超过 2048 token 至 -0.5）和工具错误惩罚（-0.5）；二者组合后 clip 到 [-0.25,0.25]，再加到 token advantage 并标准化。

## 关键实验
在 R2E-Gym 仓库级 issue 任务上训练 MiniCPM5-2B 与 Qwen3.5-4B，对比 SPO+Adam、SPO+Muon、SPO++ + Muon full recipe 及多个 ablation。Full recipe（SPO++ + Muon + penalties + TIS + token mean）训练成功率：MiniCPM5-2B 约 74.1%，Qwen3.5-4B 约 66.9%；而 SPO+Adam 分别为 26.8% / 18.0%，SPO+Muon 为 45.2% / 18.2%。去掉 length penalty 后成功率明显下降，若干 Adam 配置在训练中出现 collapse。

## 最值得记住的一句话
长程 agent RL 中，优化器选择不是孤立的；Muon 需要与 token 级损失、截断重要性采样和轻量奖励惩罚组合，才能稳定获得收益。
