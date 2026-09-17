---
title: 'Agora: Git as Shared Memory for Collective AutoResearch'
title_zh: Agora：以 Git 作为集体自动研究的共享记忆
authors:
- Yifan Zhang
- Yunheng Zou
- Shaokun Zhang
- Jian Hu
- Hao Zhang
- Binfeng Xu
- Jan Kautz
- Yi Dong
affiliations:
- NVIDIA
arxiv_id: '2609.18094'
url: https://arxiv.org/abs/2609.18094
pdf_url: https://arxiv.org/pdf/2609.18094
published: '2026-09-15'
collected: '2026-09-17'
category: MultiAgent
direction: Git共享记忆多智能体协作
tags:
- multi-agent
- shared-memory
- Git
- autonomous-research
- diversity-aware-selection
- reproducibility
one_liner: 用 Git 的 append-only DAG 为多智能体研究提供共享记忆，实现去中心化协作探索
practical_value: '- **用 Git 管理 Agent 实验/策略迭代**：把每个实验、假设、验证结果作为不可变 commit，parent 边显式记录依赖关系，业务侧可以低成本获得可追溯、可复现的离线实验记录，尤其适合推荐模型调参、特征
  ablations 和策略 A/B 测试。

  - **派生索引暴露“前沿+被忽略分支”**：维护一个由 commit 图计算的派生索引，让 Agent 或人工可以快速看到当前最优版本、验证状态和未被探索的分支，避免多个
  Agent 重复搜索同一方向。

  - **多样性感知选择规则防单一收敛**：在多智能体并行探索超参数、召回策略或生成式推荐 Semantic ID 时，引入类似多样性奖励，防止所有 worker
  都扑向当前领先方案，强制探索 neglected branches，提升整体发现效率。

  - **去中心化协作无需中央规划**：13 个 LLM worker 仅通过共享 Git 状态自主分工，适合构建离线自动化 Agent 团队做模型初始化、权重迁移或
  embedding 压缩等可验证任务，每个 agent 只需 checkout 任意 commit 继续工作。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：单个自动研究 Agent 能独立改进训练配置，但多个 Agent 并行运行时各自从零开始，导致重复搜索多于新发现，缺少共享研究状态。

**方法关键点**：Agora 将研究过程建模为 Git 中的 append-only DAG。每个结果、洞察、假设、验证和报告都是不可变 commit，其 parent 边表示“构建于什么之上”；派生索引实时暴露研究前沿、被忽略分支和各 claim 的验证状态；多样性感知选择规则防止群体收敛到单一 leader。无中央规划，Agent 可自由 checkout 任意 commit 继续探索。

**关键结果**：近 12 天运行中，13 个语言模型 worker 在无任务分配、无中心调度下解决权重转移问题：给定 141 个预训练 donor 模型和维度不匹配的 frozen 119.6M 参数 attention-SSM hybrid 目标，需在无训练数据、无梯度更新条件下初始化目标。社区发布 1,703 个贡献，评估指标从 3.39 降至 1.899 bits per byte，缩小了与训练后 GPT-2 124M 差距的 62%。获胜配方将 donor 的 next-token 统计压缩进目标 embedding 和 output head，再对 attention、feed-forward 和 state-space 块做稀疏编辑引入短程上下文信号。该配方 145 个 commit 祖先跨 15 个账户，165 次独立复现全部成功。一次中期人类干预打破了单一文化，作者也讨论了可控对比实验的必要性。
