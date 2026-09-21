---
title: 'CodeMidas: Scaling Agentic Coding RL Environments from Code Itself'
title_zh: CodeMidas：从代码本身规模化构建智能编程强化学习环境
authors:
- Bowen Ye
- Lei Li
- Shicheng Li
- Zihao Yue
- Linghao Zhang
- Hanglong Lv
- Yuanxin Liu
- Wenhan Ma
- Hao Tian
- Rang Li
affiliations:
- Xiaomi
- Peking University
- University of Hong Kong
- Renmin University of China
arxiv_id: '2609.22068'
url: https://arxiv.org/abs/2609.22068
pdf_url: https://arxiv.org/pdf/2609.22068
published: '2026-09-17'
collected: '2026-09-21'
category: Training
direction: Agentic RL 环境构建与编码智能体训练
tags:
- RL environments
- coding agents
- source code
- GRPO
- MiMo
one_liner: 用 agentic 流水线仅从源码自动构建可执行 RL 环境，训练 MiMo-V2.5 在多项编程基准全面提升
practical_value: '- **自动构造可验证任务库**：借鉴 CodeMidas 思路，从业务已有的代码库（数据管道、特征工程、推荐策略实现）中自动提取「行为规范
  + 执行测试」对，形成用于训练内部 agent 的 RL 环境，降低人工造题成本。

  - **用执行校验与多次 rollout 过滤低质量样本**：在推荐/搜索 agent 的训练数据构建中，可用类似机制：让 agent 生成多个轨迹，通过可执行校验（如
  SQL 运行、API 返回、线上小流量指标）筛选高质量样本再用于 GRPO 等 RL 训练，提升数据纯度。

  - **RL 训练催生更优探索与自验证行为**：该工作发现 RL 后 agent 会主动增加代码库探索并采用更多样自验证策略，这提示在电商商品文案生成、搜索 query
  改写等长 horizon agent 任务中，引入 RL 能改善策略的长期规划与自我纠错能力。

  - **高质量任务数量是性能瓶颈**：消融显示增加高质量训练任务数量单调提升性能，而非只调模型或算法；业务中应优先构建可扩展的「任务生成流水线」持续产出多样训练任务。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 coding agent RL 训练依赖 issues 和 commits 等开发产物，任务提取范围受限；开源代码库本身蕴含大量已实现功能，但缺少直接可用的 RL 环境。

**方法关键点**：提出 CodeMidas，一个只用 source code 作为任务特定输入的 agentic 流水线。它把 agentic compute 分配到环境构建的每个阶段：先让 agent 探索代码库中已实现的功能并制定行为规范，再基于原代码的真实执行构造测试，最后通过执行检查和多次 solution rollouts 验证过滤候选任务。由此得到 5,545 个训练任务，覆盖 3,185 个开源代码库、23 种编程语言和 15 个技术领域。

**关键结果**：用这些任务对 MiMo-V2.5 进行 GRPO 训练，在五个不同基准上全部提升：DeepSWE +11.7%，ProgramBench +17%，Terminal-Bench v2.1 +8.5%。消融实验表明，增加高质量任务数量能持续提升性能；轨迹分析显示 RL 训练后的 agent 展现出更多的代码库探索和更多样的自验证行为。
