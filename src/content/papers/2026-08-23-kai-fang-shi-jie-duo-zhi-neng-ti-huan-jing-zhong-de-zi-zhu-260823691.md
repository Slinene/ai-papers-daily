---
title: Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment
title_zh: 开放世界多智能体环境中的自主数学发现
authors:
- Stephen Chung
- Wenyu Du
- William J. Wesley
affiliations:
- DualverseAI
- University of Cambridge
- University of Hong Kong
- University of California San Diego
arxiv_id: '2608.23691'
url: https://arxiv.org/abs/2608.23691
pdf_url: https://arxiv.org/pdf/2608.23691
published: '2026-08-23'
collected: '2026-08-27'
category: MultiAgent
direction: 多智能体开放世界协作与知识累积
tags:
- Multi-Agent
- Open-World
- Mathematical Discovery
- Shared Literature
- Autonomous Research
- LLM
one_liner: 在无中心协调的多智能体开放环境中，AI 智能体自主协作完成多项数学发现并产出可解释定理与分析
practical_value: '- **共享文献库机制**：多个 LLM 智能体异步贡献和引用彼此的中间结果，形成可累积的知识库。在电商推荐/广告场景中，可让多个
  Agent 分别探索不同用户群或商品类目的策略，通过共享“发现日志”避免重复试错，加速全局优化。

  - **无中心协调的自组织协作**：不依赖固定流水线或中央调度器，智能体自主选择研究方向。适合动态变化的业务环境（如大促、季节性选品），可部署多个并行探索 Agent，根据实时数据自主调整目标，减少人工编排成本。

  - **可解释性要求**：智能体不仅输出数值结果，还生成定理和分析，使产出可被人类理解。在生成式推荐或 Agent 决策中，强制输出结构化推理过程而非仅最终答案，便于业务方审计、验证和信任模型决策。

  - **完整交互日志与验证代码开放**：透明记录所有智能体对话和决策轨迹，有利于调试和回溯。线上推荐 Agent 系统应记录每一轮多智能体交互、中间产物和最终采纳理由，形成可审计的“决策链”，支撑后续评估与合规。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 AI 数学研究多依赖固定流水线或中央协调，限制了智能体的自主性和创造力。论文探索在完全无中央协调的开放世界多智能体环境中，AI 能否像独立研究者一样自主推进数学发现。

**方法关键点**：构建 Station 环境，来自不同模型家族的智能体共享一个研究目标，可以自主选择研究方向、设计并执行实验、与其他智能体协作，并共同维护一份不断增长的“科学文献”。没有预设脚本或任务分配，智能体通过异步贡献和引用文献形成自组织协作。

**关键结果数字**：在 AlphaEvolve 目录的 12 个构造问题和 2 个额外案例研究中，Station 在 5 个问题上取得了相对先前文献新颖的结果：新的有限域 Kakeya 集合无限族；维度 11 的精确 604 点亲吻配置；离散化 Kakeya 针和符号不确定性问题新纪录；Erdős 最小重叠问题的显著改进下界。此外还发现了 Book Ramsey 数的新无限族。更重要的是，智能体不仅产出数值构造，还生成了定理和分析，使结果可解释、可被数学家进一步利用。论文公开了所有原始智能体对话、证明和验证代码，提供透明的发现过程记录。
