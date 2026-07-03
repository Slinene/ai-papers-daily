---
title: 'DecompRL: Solving Harder Problems by Learning Modular Code Generation'
title_zh: DecompRL：通过模块化代码生成解决更难问题
authors:
- Juliette Decugis
- Fabian Gloeckle
- Francis Bach
- Taco Cohen
- Gabriel Synnaeve
affiliations:
- FAIR at Meta
- Inria
- École Normale Supérieure
- CERMICS
- École des Ponts ParisTech
arxiv_id: '2607.02390'
url: https://arxiv.org/abs/2607.02390
pdf_url: https://arxiv.org/pdf/2607.02390
published: '2026-07-02'
collected: '2026-07-03'
category: LLM
direction: 分解式问题求解 · 模块化代码生成
tags:
- modular generation
- hierarchical RL
- test-time scaling
- code generation
- decomposition
- compositional generalization
one_liner: 将难题分解为独立子函数，训出可组合的模块化代码，用 CPU 组合爆炸替代 GPU 重采样
practical_value: '- 复杂推荐 / Agent 任务可借鉴“分解—独立实现—组合”范式：将长流程或组合动作拆成原子模块，分别用 LLM 生成候选实现，再通过组合搜索提高成功率，同时减少高成本
  LLM 调用。

  - 生成式推荐中，将完整的 item semantic ID 或推荐文案拆成多个独立子部分生成，再灵活组合，可获得指数级候选多样性，且大部分组合验证可在 CPU
  上完成。

  - 训练 Agent 规划能力时，用 DecompRL 类似的 RL 目标鼓励模型自动学习“何时以及如何分解子目标”，可提升长远任务成功率。

  - 线上重采样（pass@k）成本高昂时，可将一次性生成转换为“少量模块候选 + CPU 组合评估”模式，显著压缩 GPU token 消耗（论文中 ~50×），适合高流量推荐系统降本。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 在竞赛编程等任务中，遇到正确解概率极低的难题时，传统重复采样与 RL 均因搜索空间过大而失效。
**方法**：提出 DecompRL，一种让模型显式学习问题分解与模块化实现的 RL 算法。训练两个策略：分解策略将问题拆成多个独立子函数；实现策略为每个子函数并行生成代码。推理时，从每个子函数的 k 个候选中选择组合，理论候选方案数达 k^n，将瓶颈从 GPU 生成转移到 CPU 评估。
**结果**：在 LiveCodeBench 与 CodeContests 上，基于 Qwen2.5 7B 和 Code World Model 32B，DecompRL 在单问题超 10^5 token 预算下超越标准 RL 和多样性优化 RL，解决此前无法攻克的难题（硬子集 pass@k 提升至 35%），且 GPU token 成本降低约 50 倍。
