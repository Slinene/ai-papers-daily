---
title: 'Look Before You Leap: Distilling Tree Search into Action Evaluation for Frozen
  VLA Models'
title_zh: 三思而后行：将树搜索蒸馏为冻结VLA模型的动作评估
authors:
- Xinyi Xie
- Zican Hu
- Zhanyu Liu
- Yicheng Dong
- Wenhao Wu
- Zhenhong Sun
- Haoran Li
- Chunlin Chen
- Zhi Wang
- Pichao Wang
affiliations:
- Nanjing University
- Australian National University
- Institute of Automation, Chinese Academy of Sciences
- Nvidia
arxiv_id: '2607.03751'
url: https://arxiv.org/abs/2607.03751
pdf_url: https://arxiv.org/pdf/2607.03751
published: '2026-07-03'
collected: '2026-07-08'
category: Agent
direction: Agent 动作评估与测试时缩放
tags:
- VLA
- Action Evaluation
- Monte-Carlo Tree Search
- Test-Time Scaling
- Q-value Distillation
one_liner: 通过MCTS树搜索采集轨迹并蒸馏为轻量Q值模型，解耦动作提案与后果评估，在不微调VLA下显著提升泛化与效率
practical_value: '- **Agent 动作解耦范式**：将动作生成（VLA）与长期后果评估（Q模型）分离，保持通用模型冻结，仅训练轻量评估器，避免微调带来的泛化能力损失，适用于电商推荐Agent中对话/多步决策的在线动作选择。

  - **仿真树搜索蒸馏**：利用离线仿真环境或历史日志构建奖励信号，通过MCTS充分探索候选动作空间并收集带回报的轨迹，蒸馏为Q值预测器。在搜索推荐Agent中，可对候选query/文案/策略进行前瞻性评估后再执行。

  - **测试时缩放替代模型缩放**：通过增加候选动作采样数（如pass@k）和评估器计算来提升性能，比直接扩大模型更具性价比。例如在低延迟要求下，用小模型生成多候选+评估器挑选，超过大模型效果。

  - **不确定性正则化Q值**：在选择动作时结合不确定性惩罚，平衡探索与利用，可借鉴到多臂老虎机或在线探索推荐场景，用于候选物品/文案的最终择优。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：VLA模型虽经大规模预训练，但泛化仍脆弱，常用微调或RL会损害其通用能力。诊断发现，冻结VLA的 pass@1 成功率仅 33%，而 pass@32 可达 92%，表明模型分布中已包含正确动作，但缺乏对长期后果的准确评估。

**方法**：提出 SVA（Search, Value, and Act）框架。首先，在仿真环境中对冻结VLA进行 Monte-Carlo 树搜索（MCTS），充分探索其输出分布并收集带经验回报的多样化轨迹。然后，将这些轨迹知识蒸馏到一个轻量级 Q-value 模型中，该模型能预测候选动作的期望后果。部署时，冻结VLA生成多个候选动作，评估器选择不确定性正则化 Q 值最高的动作，无需仿真器。

**结果**：在多个具身基准上，SVA 始终提升未知任务的泛化成功率，并展现良好的测试时缩放行为。尤为突出的是，9B VLA 搭配 SVA 以 27% 更低的推理延迟超越 27B VLA 达 7 个百分点，证明缩放测试时评估比缩放模型规模更划算。
