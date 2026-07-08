---
title: 'CurateEvo: Data-Curation Evolving for Agentic Post-Training'
title_zh: CurateEvo：面向Agent后训练的失败驱动数据策展进化框架
authors:
- Dingzirui Wang
- Xuanliang Zhang
- Keyan Xu
- Qingfu Zhu
- Wanxiang Che
affiliations:
- Harbin Institute of Technology
arxiv_id: '2607.06140'
url: https://arxiv.org/abs/2607.06140
pdf_url: https://arxiv.org/pdf/2607.06140
published: '2026-07-07'
collected: '2026-07-08'
category: Training
direction: Agent后训练 · 失败驱动的数据策展进化
tags:
- Data Curation
- Agentic Post-Training
- Failure-Driven Evolution
- Reinforcement Learning
- Memory Bank
- Pruning
one_liner: 用失败轨迹动态重写可执行策展代码，统一生成SFT/RL/记忆数据并裁剪冗余
practical_value: '- 构建 Agent 训练数据闭环：将线上 Agent 的失败轨迹作为反馈，自动诊断反复出现的失败模式，驱动数据策展策略迭代，持续补充或过滤训练数据，适合电商搜索/推荐
  Agent 的长期优化。

  - 将数据策展表示为可执行代码，交由 LLM 自动重写进化，降低人工维护成本。可用类似思路实现“Agent 训练数据自动管线”，在每次迭代中根据新失败 case
  调整数据加工逻辑。

  - 统一输出 SFT、RL 与推理时记忆库数据，保证训练一致性；在电商多轮 Agent 场景下，可同时产出监督微调数据和用于强化学习的环境交互样本，减少重复开发。

  - 成本感知的冗余剪枝：在策展代码中加入效率目标，自动剔除低效用训练轮次，降低训练计算开销，适合工业级海量数据的 Agent 训练场景。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有 Agent 后训练将数据策展视为固定预处理步骤，主要做数据增广，忽略根据下游失败模式进行过滤、精炼和自适应调整，导致训练数据无法针对 Agent 实际弱点进化。

**方法**：提出 CurateEvo，一个失败驱动的动态进化框架。它将数据策展策略表示为可执行代码，并利用开发集上 Agent 的失败轨迹，让 LLM 自动诊断反复出现的失败模式，据此迭代重写策展代码。每轮进化后的策略将固定原始语料转化为三类数据：监督微调数据、强化学习数据以及推理时使用的记忆库。进化分两步：先提升效果——通过诊断失败模式进行定向增强、过滤或精炼；再提升效率——在成本感知目标下剪枝冗余或低效用训练轮次。

**结果**：在 ACEBench-Agent、BFCL-V4 和 τ²-Bench 三个基准上，CurateEvo 在标注数据和自由数据设置下均优于现有策展方法，平均得分分别提高 3.2 和 2.7 点。同时兼容不同后训练配方，并大幅减少策展计算开销。
