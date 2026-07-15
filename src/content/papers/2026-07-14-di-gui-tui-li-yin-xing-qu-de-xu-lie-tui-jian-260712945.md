---
title: 'RecRec: Latent Interests Recursive Reasoning for Sequential Recommendation'
title_zh: 递归推理隐兴趣的序列推荐
authors:
- Wenhao Deng
- Junchen Fu
- Hanwen Du
- Alexandros Karatzoglou
- Ioannis Arapakis
- Hangjun Guo
- Kaiwen Zheng
- Yongxin Ni
- Joemon M. Jose
arxiv_id: '2607.12945'
url: https://arxiv.org/abs/2607.12945
pdf_url: https://arxiv.org/pdf/2607.12945
published: '2026-07-14'
collected: '2026-07-15'
category: RecSys
direction: 序列推荐 · 隐兴趣递归推理
tags:
- Sequential Recommendation
- Latent Reasoning
- Recursive Reasoning
- Interest Decomposition
- Deep Supervision
- Inference-Time Computation
one_liner: 解耦推理与预测，用兴趣压缩和递归推理模块在隐空间逐步精炼，深度可调且无需RL
practical_value: '- Context Compressor 将用户序列压缩为多个隐兴趣向量，配合 Interest Diversity Regularizer
  迫使各兴趣捕获不同行为侧面，可直接作为电商多兴趣召回或用户理解模块

  - Recursive Reasoner 在独立的隐空间对兴趣进行递归式精炼，这种“逐步思考”的范式可用于带货直播、购物车序列等长序列场景，捕捉演化意图

  - 推理深度可动态调节：线上可根据 latency 预算自由选择递归步数，浅层做低延迟预测，深层提升准确率，无需重新训练模型

  - 框架完全监督化，无 RL 训练负担，工程实现简单；解耦的设计让 Backbone、Compressor、Reasoner 可单独替换或蒸馏，便于在已有推荐系统上增量叠加推理能力'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机** 序列推荐通常在推理时仅做一次前向计算，近期工作尝试引入中间推理步骤，但普遍将推理状态和预测耦合在固定的 d 维向量中，限制了推理深度且依赖强化学习训练，实用性受限。  
**方法** RecRec 解耦为两个模块：Context Compressor 把 Backbone 输出的隐状态压缩为一小组隐兴趣向量，并用 Interest Diversity Regularizer 迫使每个兴趣捕捉用户行为的不同方面；Recursive Reasoner 在独立的隐空间对这些兴趣进行递归推理，每一步输出精炼的兴趣，并通过 Deep Supervision 保证中间步骤也具备预测能力，使得推理深度在测试时可任意调节。整个框架仅需两阶段监督训练，无需 RL。  
**结果** 在四个真实数据集上，RecRec 全面超越现有推理增强方法，且在三个数据集上，推理深度超过训练深度时仍能持续提升，表明解耦的多向量设计成功释放了隐推理的潜力。
