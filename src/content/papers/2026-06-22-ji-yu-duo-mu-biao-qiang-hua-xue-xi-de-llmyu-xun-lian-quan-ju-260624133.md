---
title: Holistic Data Scheduler for LLM Pre-training via Multi-Objective Reinforcement
  Learning
title_zh: 基于多目标强化学习的LLM预训练全局数据调度器
authors:
- Chenhao Dang
- Jing Ma
- Mingjie Liao
affiliations:
- China Electronics Technology Group Corporation 15th Research Institute
- Renmin University of China
- BRAIN
- Alibaba Group
arxiv_id: '2606.24133'
url: https://arxiv.org/abs/2606.24133
pdf_url: https://arxiv.org/pdf/2606.24133
published: '2026-06-22'
collected: '2026-06-25'
category: Training
direction: LLM预训练在线数据混合
tags:
- Online Data Mixing
- Multi-Objective RL
- SAC
- LLM Pre-training
- Data Scheduling
one_liner: 用多目标强化学习动态混合训练数据，兼顾数据质量、域间影响和模型自身信号
practical_value: '- 训练电商/搜索/推荐场景的多域统一模型（如用户行为序列模型）时，可借鉴其**多目标奖励设计**：同时考虑各域数据质量指标、域间损失信号交互（如搜索域的
  loss 变化对推荐域的预测影响），以及模型参数范数等内在反馈，用 RL 动态调整各域采样比例，替代固定混合策略。

  - 工程实现上，采用 **Soft Actor-Critic (SAC)** 算法在连续空间中输出各域采样权重，比离散调度更平滑，且通过离线回放池减少在线交互成本；该框架可直接复用到多数据源的
  Embedding 训练或生成式推荐模型的 token 混合训练。

  - 实验显示 HDS 可节省 44% 训练步数达到同等困惑度，且下游任务（MMLU）提升 7.2%，表明**更高效的数据利用**——在业务资源有限时，用该方法加速大模型训练收敛，避免昂贵的全量等比例训练。

  - 注意该方法需要实时监控多域验证损失，业务落地时须搭建配套的评估流与 RL 控制回路，初期可先在离线训练中模拟不同混合策略的效果，再切换到在线调度。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 预训练的数据混合策略至关重要，现有在线数据混合（ODM）方法只从单一视角（如仅看数据质量或损失）优化，忽略了预训练需要多维度动态权衡。

**方法**：提出 Holistic Data Scheduler (HDS)，将数据调度建模为连续控制空间中的强化学习问题，使用 SAC 算法稳定探索高维策略空间。核心是**多目标 holistic reward**：
- 数据驱动奖励：基于数据源质量指标（如困惑度、毒性得分）；
- 损失驱动奖励：捕捉域间影响，通过监控各域验证损失的耦合变化；
- 模型驱动奖励：利用模型权重范数反映训练状态。
训练过程中，RL 智能体根据上述奖励实时输出各数据源的采样概率。

**关键结果**：在 The Pile 上训练 Pythia-1B，HDS 比次优方法用**少 44% 的迭代步数**达到相同验证集困惑度；下游 MMLU 0-shot 准确率**提升 7.2%**，并在其他基准上一致改善，验证了训练效率与模型能力的双重提升。
