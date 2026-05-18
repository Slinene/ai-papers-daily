---
title: 'PhyMotion: Structured 3D Motion Reward for Physics-Grounded Human Video Generation'
title_zh: 基于物理的3D人体运动奖励用于视频生成
authors:
- Yidong Huang
- Zun Wang
- Han Lin
- Dong-Ki Kim
- Shayegan Omidshafiei
- Jaehong Yoon
- Jaemin Cho
- Yue Zhang
- Mohit Bansal
affiliations:
- UNC Chapel Hill
- FieldAI
- NTU Singapore
- AI2
- Johns Hopkins University
arxiv_id: '2605.14269'
url: https://arxiv.org/abs/2605.14269
pdf_url: https://arxiv.org/pdf/2605.14269
published: '2026-05-13'
collected: '2026-05-18'
category: Multimodal
direction: 物理引导的人体运动视频生成
tags:
- Video Generation
- Motion Reward
- Physics Simulation
- RL Post-training
- Human Motion
one_liner: 提出结构化3D运动奖励PhyMotion，通过物理仿真多维度评估运动真实感，显著提升视频生成中的人体运动质量
practical_value: '- 奖励信号设计：将难以直接评估的运动真实感分解为运动学、接触/平衡、动力学三个可量化维度，每个维度提供连续可解释信号，该分解思路可借鉴用于电商场景（如商品图文一致性、合规性）的多维奖励设计。

  - RL后训练方法：在视频生成模型上用RL优化精心设计的奖励，仅带来适中的训练开销，且不影响整体视频质量，这种低侵入性微调可参考用于可控文本生成或推荐模型的特定属性优化。

  - 多维度互补监督：消融实验证实三个轴信号互补，单独使用效果次优，提示在设计评估或奖励体系时需覆盖多个独立方面以避免盲点。

  - 外部仿真器验证：引入MuJoCo物理仿真器作为奖励的一部分，可缓解模型“奖励黑客”问题，类似思想可迁移到生成式推荐或对话Agent中，用规则引擎或知识图谱做校验，提升生成结果的逻辑一致性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：当前视频生成模型在纹理、光影等方面效果出色，但人体运动仍常出现悬浮、违反物理规律等问题，主要瓶颈在于现有奖励信号仅依赖2D感知，缺乏对3D身体姿态、接触及动力学的建模，导致对物理不合理运动的评分虚高。

**方法**：提出PhyMotion，从生成视频中恢复SMPL人体网格，将其重定向至MuJoCo物理引擎中的人形模型，然后沿三个维度评估运动质量：1）运动学合理性（关节角度、加速度是否符合人体常态）；2）接触与平衡一致性（足部与地面接触状态是否合理，身体是否稳定）；3）动力学可行性（运动是否符合牛顿力学）。每个维度输出连续且可解释的分数，组合成结构化奖励。该奖励被用于基于强化学习的后训练，优化自回归和双向视频生成器。

**结果**：PhyMotion与人类评估的相关性显著高于现有奖励指标。在RL后训练中，优化PhyMotion带来的运动真实感提升比优化现有奖励更大且更稳定，盲评中Elo分提升+68。消融实验表明三个维度提供互补监督，且奖励计算仅带来适度训练开销，未损害整体视频质量。
