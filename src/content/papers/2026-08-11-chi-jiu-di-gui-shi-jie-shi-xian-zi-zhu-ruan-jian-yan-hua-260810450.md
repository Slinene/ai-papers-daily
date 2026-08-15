---
title: Persistent Recursive Worlds Enable Autonomous Software Evolution
title_zh: 持久递归世界实现自主软件演化
authors:
- Beichen Huang
- Zhenyu Liang
- Bowen Zheng
- Ran Cheng
affiliations:
- The Hong Kong Polytechnic University
arxiv_id: '2608.10450'
url: https://arxiv.org/abs/2608.10450
pdf_url: https://arxiv.org/pdf/2608.10450
published: '2026-08-11'
collected: '2026-08-15'
category: MultiAgent
direction: 持久递归世界 · 多智能体协作
tags:
- Multi-Agent
- Long-Horizon
- Software Evolution
- Recursive Delegation
- LLM
- Autonomous Coding
one_liner: 提出以持久化项目而非持久化 Agent 为核心的递归多智能体框架，实现长程软件自动开发与演进
practical_value: '- 把长期任务的“记忆”外置到项目版本/制品，而不是塞进单个 Agent 的上下文：电商选品、活动策划、自动调参等长时间运行 Agent
  可让 worker 只持有局部上下文，验收后写回版本库，避免上下文膨胀与错误累积。

  - 递归委派 + 按路径拆分：搜索词/文案/商品策略可按类目或子域递归拆解，子 Agent 只做局部变更，上层合并验收，便于并行和回滚。

  - 验收驱动的版本推进：推荐/广告策略改动只允许通过离线评测或小流量验证的“后果”合入版本历史，形成可审计、可复现的实验资产。

  - 成本敏感的长程任务可用廉价快速 LLM 跑大量 episode：本工作 120 小时/1000+ episodes 仅 44 美元，适合批量生成候选 query、商品卖点、广告文案等。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：复杂软件系统比任何单个 coding agent 寿命更长，当前多数 agent 系统依靠持久会话、记忆或共享上下文保持连续性，但长期上下文与 agent 更替仍难维护。Genesis 采取相反设计：让软件项目持久，而局部 agent 有限生命。

**方法**：将软件表示为 persistent recursive world；每个 local world 由 accepted version 与 repository path 定位。有限生命 agent 提出局部变更，递归委派跨越路径分发工作；只有验收通过的后果才推进持久版本历史。评测覆盖 formation、continuation、redevelopment。

**结果**：从空编译器仓库出发，用 DeepSeek V4 Flash 构建 Rust 版 C 编译器约 250k 行，持续 120 小时以上，归档 1000+ agent episodes，模型 token 费仅 44 美元；通过完整 c-testsuite 及大部分 LLVM/Csmith 测试。GLM 5.2 生成的另一编译器世界在多次替换 agent 后仍保持全量测试性能。重写 13 个 MESA 模块（100k+ Fortran 行）为近 90k Rust 行，6 个数值负载中位加速 1.55–6.87 倍。
