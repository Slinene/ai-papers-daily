---
title: 'EXIMO: VLM Guided Exploration of VLA Policies'
title_zh: 'EXIMO: VLM 引导的 VLA 策略探索'
authors:
- Bhavya Sukhija
- Oliver Groth
- Mohit Shridhar
- Tim Hertweck
- Michael Bloesch
- Markus Wulfmeier
- Abbas Abdolmaleki
- Martin Riedmiller
affiliations:
- Google DeepMind
arxiv_id: '2608.19891'
url: https://arxiv.org/abs/2608.19891
pdf_url: https://arxiv.org/pdf/2608.19891
published: '2026-08-19'
collected: '2026-08-24'
category: Training
direction: 机器人 VLA 微调 · 探索-模仿-优化
tags:
- VLA
- VLM planning
- RL fine-tuning
- sample efficiency
- imitation learning
one_liner: 提出三阶段（探索-模仿-优化）VLA 微调算法，用 VLM 规划分解任务并配合 residual off-policy RL，显著提升样本效率
practical_value: '- 可借鉴 VLM 作为规划器分解长程任务：在搜索/推荐 Agent 中，用 LLM 将用户复杂意图拆解为多个可执行子 query
  或子步骤，降低单次决策难度。

  - “探索-模仿-优化”三阶段训练模式：先通过规划引导收集高质量数据（探索），再做监督微调（模仿），最后用离线 RL 优化策略，比直接在线 RL 或纯 BC 更高效，适合
  Agent 策略迭代。

  - Residual off-policy RL 思路：在已有大模型策略上训练残差模块进行 RL 微调，避免全参数 RL 的不稳定，可迁移到 LLM 推荐策略的轻量级在线优化。

  - 用 VLM 生成 intermediate subgoals 指导策略探索，类似在推荐中生成有序的候选集或子任务序列，提升长链路任务的完成率。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 VLA 机器人策略基于大规模遥操数据的行为克隆，但为新任务微调仍面临数据采集昂贵、RL 样本效率低且对 VLA 架构不友好的问题。

**方法关键点**：
- 提出 EXIMO 算法，分探索、模仿、优化三个阶段。
- 探索阶段：装备 VLA 一个 VLM 作为规划器，VLM 将长程任务分解为多个短程子任务，引导 VLA 收集编排数据集。
- 模仿阶段：用编排数据对 VLA 进行监督微调。
- 优化阶段：使用 residual off-policy RL 进一步微调策略，残差设计降低 RL 对超大模型的影响。

**关键结果**：三阶段消融实验表明，EXIMO 在样本效率和最终性能上显著超过已有方法，尤其对长程操作任务提升明显。
