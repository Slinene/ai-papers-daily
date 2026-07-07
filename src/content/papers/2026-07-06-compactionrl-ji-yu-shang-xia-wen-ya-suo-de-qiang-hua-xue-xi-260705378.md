---
title: 'CompactionRL: Reinforcement Learning with Context Compaction for Long-Horizon
  Agents'
title_zh: CompactionRL：基于上下文压缩的强化学习训练长程智能体
authors:
- Yujiang Li
- Zhenyu Hou
- Yi Jing
- Jie Tang
- Yuxiao Dong
affiliations:
- Tsinghua University
arxiv_id: '2607.05378'
url: https://arxiv.org/abs/2607.05378
pdf_url: https://arxiv.org/pdf/2607.05378
published: '2026-07-06'
collected: '2026-07-07'
category: Agent
direction: 长程Agent强化学习与上下文压缩
tags:
- Reinforcement Learning
- Context Compaction
- LLM Agents
- Long-Horizon
- SWE-bench
- Token-level Loss
one_liner: 提出CompactionRL，联合优化任务执行与上下文压缩，使LLM智能体从压缩长轨迹中学习，显著提升长程编码任务性能
practical_value: '- **多轮对话推荐/搜索Agent的上下文压缩训练**：可借鉴CompactionRL思路，让推荐Agent在交互中自主生成紧凑的对话历史摘要，代替人工设计的截断或固定压缩模板，通过强化学习优化压缩质量和任务完成度的平衡，提升长对话下的推荐准确率和用户满意度。

  - **联合损失的Token级归一化设计**：在处理多目标强化学习（如推荐准确性与解释性文本生成）时，可采用token级别的损失加权，根据序列长度动态调整不同损失项的权重，避免长文本损失主导训练，适用于训练同时生成推荐理由和结果的Agent。

  - **跨轨迹广义优势估计（GAE）**：当训练数据包含多个不同推荐会话（轨迹）时，可借鉴跨轨迹GAE的技巧，更稳定地估计优势值并分配信用，改善大规模离线RL训练的效果。

  - **推理阶段的上下文压缩部署**：训练得到的自主压缩能力可简化在线推理，使推荐/搜索Agent在有限上下文窗口内支持更长的用户交互历史，降低抛弃历史带来的信息损失，同时节约上下文计算成本。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：长程LLM智能体在交互中积累的轨迹很容易超出上下文窗口限制，导致任务失败或性能下降；现有长上下文模型成本高且序列利用率衰减，而将上下文压缩与强化学习结合的训练方法尚未探索。

**方法关键点**：CompactionRL在RL训练中联合优化任务执行和上下文压缩。智能体在每步交互中可选择生成一个压缩摘要（compaction），以压缩后的上下文继续后续推理。训练通过token-level loss normalization平衡任务损失与压缩损失，并使用cross-trajectory generalized advantage estimation（跨轨迹广义优势估计）处理多条轨迹的奖励信号，使智能体学会从压缩后的长轨迹中有效学习。

**关键结果**：在两个编码智能体基准上，CompactionRL带来显著提升。基于GLM-4.5-Air (106B-A30B)，SWE-bench Verified Pass@1提高7.0个百分点至66.8%，Terminal-Bench 2.0提高3.1个百分点至24.5%；基于GLM-4.7-Flash (30B-A3B)，两项分数分别提升5.5个百分点至56.0%和6.8个百分点至20.2%。该方法已部署在GLM-5.2 (750B-A40B) 的RL训练管道中。
