---
title: 'DiffusionOPD: A Unified Perspective of On-Policy Distillation in Diffusion
  Models'
title_zh: 扩散模型多任务训练的在线策略蒸馏视角统一
authors:
- Quanhao Li
- Junqiu Yu
- Kaixun Jiang
- Yujie Wei
- Zhen Xing
- Pandeng Li
- Ruihang Chu
- Shiwei Zhang
- Yu Liu
- Zuxuan Wu
arxiv_id: '2605.15055'
url: https://arxiv.org/abs/2605.15055
pdf_url: https://arxiv.org/pdf/2605.15055
published: '2026-05-13'
collected: '2026-05-17'
category: Training
direction: 多任务扩散模型训练 · 在线策略蒸馏
tags:
- Diffusion Models
- Multi-task RL
- Policy Distillation
- Online Distillation
- Mean-Matching
one_liner: 提出 DiffusionOPD，通过在线策略蒸馏将多个任务教师知识融入统一学生，实现多任务扩散模型高效训练
practical_value: '- 多任务扩散模型训练中，独立训练专家教师再通过在线蒸馏合并到一个学生，可避免联合训练的任务干扰与灾难性遗忘，适合电商多目标生成场景（如多风格
  banner 生成或多场景推荐解释生成）。

  - 使用学生自身 rollout 轨迹进行蒸馏（而非教师轨迹），能更好地对齐学生当前分布，提升蒸馏效率，这一技巧可直接迁移到生成式推荐的扩散模型微调。

  - 导出的闭式 per-step KL 目标提供低方差梯度，能稳定 RL 训练，可应用于基于扩散模型的用户行为序列生成或交互式多臂老虎机推荐。

  - 确定性 ODE 与随机 SDE 的统一 mean-matching 公式，为实际部署中采样器选择提供依据，减少推理代价，对需要实时响应的推荐系统有益。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：当前扩散模型的强化学习微调多局限于单任务，扩展到多任务时联合优化存在任务间干扰和不平衡，级联 RL 又面临灾难性遗忘和流程繁琐。需要一种高效、稳定的多任务训练范式。

**方法**：提出 DiffusionOPD，基于在线策略蒸馏（OPD）。先独立训练各任务教师模型，然后在学生自身 rollout 轨迹上蒸馏教师能力，实现解耦的单任务探索与多任务集成。理论上，将 OPD 从离散 token 扩展到连续状态马尔可夫过程，推导出闭式 per-step KL 目标，通过 mean-matching 统一了随机 SDE 和确定性 ODE 的精炼。该解析梯度相比 PPO 式策略梯度，方差更低、泛化性更强。

**结果**：大量实验表明，DiffusionOPD 在训练效率和最终性能上均优于多奖励 RL 和级联 RL 基线，并在所有评估基准上取得最优结果。
