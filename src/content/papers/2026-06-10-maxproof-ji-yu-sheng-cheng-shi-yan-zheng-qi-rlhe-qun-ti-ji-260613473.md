---
title: 'MaxProof: Scaling Mathematical Proof with Generative-Verifier RL and Population-Level
  Test-Time Scaling'
title_zh: MaxProof：基于生成式验证器RL和群体级测试时扩展的数学证明规模化
authors:
- Jiacheng Chen
- Xinyu Zhang
- Shunkai Zhang
- Yanmohan Wang
- Lin Li
- Tiancheng Qin
- Qin Wang
- Zhengmao Zhu
- Tianle Li
- Jingyang Li
affiliations:
- MiniMax
- The Chinese University of Hong Kong
- Fudan University
- Peking University
- Tsinghua University
arxiv_id: '2606.13473'
url: https://arxiv.org/abs/2606.13473
pdf_url: https://arxiv.org/pdf/2606.13473
published: '2026-06-10'
collected: '2026-06-12'
category: Reasoning
direction: 数学证明 · 生成式验证器 · 测试时扩展
tags:
- Math Reasoning
- Test-Time Scaling
- Generative Verifier
- RL
- Proof Generation
- Multi-Agent
one_liner: 通过生成-验证-修复一体化训练与锦标赛搜索，在IMO 2025和USAMO 2026上超越人类金牌线
practical_value: '- 防御式多层验证器（defense-in-depth verifier）降低误判的思路可迁移至电商推荐中的内容审核、虚假评论检测等高风险场景，通过生成式模型直接判断并给出理由提升解释性。

  - 群体级测试时扩展（population-level test-time scaling）的锦标赛搜索框架可启发多智能体推荐系统，将生成、验证、排序等角色分配给同一模型的不同调用，在推理阶段提升最终推荐质量。

  - 将验证器训练与生成器对齐，通过“错误发现”任务强化模型对瑕疵的感知，这一范式可用于商品描述生成或广告文案的自我修正，减少人工审核成本。

  - RF过程中的数据领域和技巧平衡策略（domain and trick balance）对电商冷启动或长尾商品建模有借鉴意义，通过构造均衡训练集避免模型偏向高频模式。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：当前数学证明大模型受限于单一生成模式，验证器误判率高，且测试时计算未被有效利用。本文旨在通过生成-验证器联合强化学习和群体级搜索，实现竞赛级数学证明的规模化突破。

**方法**：提出MaxProof框架。首先训练M3模型同时具备证明生成、验证和带批评的修复三种能力。采用“防御式深度验证器”降低假阳性，并用CISPO算法结合标准差阈值过滤进行RL训练，精心平衡数据领域和数学技巧。测试时，将模型自身作为生成器、验证器、精炼器和排序器，对候选证明群体执行锦标赛选择，输出最优证明。

**结果**：在IMO 2025上取得35/42分，USAMO 2026上取得36/42分，均超过人类金牌线。消融实验证明群体搜索和防御式验证器是关键增益，且M3模型在小规模下已展现强证明能力。
