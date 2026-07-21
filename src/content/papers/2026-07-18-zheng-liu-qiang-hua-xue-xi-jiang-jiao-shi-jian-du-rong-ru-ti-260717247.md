---
title: Distilled Reinforcement Learning for LLM Post-training
title_zh: 蒸馏强化学习：将教师监督融入LLM后训练梯度
authors:
- Chen Wang
- Zhaochun Li
- Jionghao Bai
- Yining Zhang
- Hexuan Deng
- Ge Lan
- Yue Wang
affiliations:
- Nankai University
- Zhongguancun Academy
- Beijing Institute of Technology
- Zhejiang University
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2607.17247'
url: https://arxiv.org/abs/2607.17247
pdf_url: https://arxiv.org/pdf/2607.17247
published: '2026-07-18'
collected: '2026-07-21'
category: Training
direction: 强化学习 · 知识蒸馏融合
tags:
- Distilled RL
- On-Policy Distillation
- GRPO
- Token-Level Reweighting
- Cross-Family Distillation
- RLHF
one_liner: 通过逆向重要性采样将教师知识注入RL梯度，实现选择性token级信用重分配
practical_value: '- **RL训练的教师信号注入**：在推荐模型或Agent的RL训练中，可以用一个更强的教师模型对学生生成的序列进行token级重加权（教师/学生概率比），取代传统的KL散度模仿，避免无条件模仿导致的局部最优和模型坍塌。

  - **负样本重置技巧**：只在优势为正的样本上应用教师权重，负优势样本权重重置为1。在电商推荐场景中，可确保只从“好”的推荐路径中学习教师知识，避免在失败路径上模仿教师而遭受更大惩罚。

  - **序列几何归一化**：当学生和教师分布差异大时，教师对学生生成token的概率往往偏低，会导致乘积权重骤减，该方法除以序列内几何均值，仅保留相对偏好，稳定训练。尤其适用于跨模型结构（如不同推荐模型家族）的知识迁移。

  - **跨模型家族鲁棒性**：在师生模型结构差异大(如DeepSeek到Qwen)的蒸馏中，传统OPD容易失效，而Distilled RL仍能稳定提升效果，对需要混合异构模型推荐的场景有参考价值。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM后训练主要分为强化学习（RL）和在线策略蒸馏（OPD）。RL使用粗粒度的序列结果奖励，难以实现token级信用分配且无法引入新知识；OPD通过KL散度无条件模仿教师分布，当师生相似时知识增量有限，差异大时模仿信号不可靠，容易过早收敛。因此需要一种既能传递教师知识又能保持RL探索优势的统一框架。

### 方法关键点
- **核心思想**：Distilled RL将教师监督直接融入RL策略梯度，教师不是模仿目标，而是作为信用重分配的指导者。
- **逆向重要性采样**：计算教师与学生旧策略在每个token上的概率比ρ，并裁剪到[1/ϵ, ϵ]（ϵ=3），衡量教师对该token的相对偏好。
- **负样本重置**：仅对优势A>0的正样本应用教师权重w=ρ；对A≤0的负样本将w置为1，避免在错误路径上模仿教师而导致更大惩罚。
- **序列几何归一化**：对每个响应内的裁剪权重除以几何均值，使权重乘积为1，消除学生策略采样导致的全局尺度差异，仅保留教师token级相对偏好。
- **整体目标**：最终策略更新为min(ri·wi·Ai, clip(ri)·wi·Ai)，其中ri是当前与旧策略的概率比。

### 关键实验
- **实验配置**：教师Qwen3-8B-GRPO，学生DSQW-1.5B（跨家族）和Qwen3-4B（同家族），训练集DAPO-17K，评测覆盖10个数学推理基准。
- **主要结果**：DSQW-1.5B上Distilled RL平均Pass@1达40.00，比OPD高4.73点，比RL高3.14点；Qwen3-4B上平均58.96，比OPD高2.99点。跨家族场景优势更显著。
- **消融实验**：去除负样本重置导致DSQW-1.5B下降6.39点，Qwen3-4B下降8.81点；去除几何归一化分别下降1.24和1.47点。
- **知识迁移案例**：通过温度控制教师熵特性，验证Distilled RL能引导学生策略熵向教师分布靠拢，证明其能传递原始奖励信号之外的新知识。

### 最值得记住的一句话
教师分布不应作为无条件模仿的目标，而应作为RL梯度中token级信用的重新分配器。
