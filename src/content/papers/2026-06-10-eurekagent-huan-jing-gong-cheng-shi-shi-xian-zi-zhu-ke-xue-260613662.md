---
title: 'EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific
  Discovery'
title_zh: EurekAgent：环境工程是实现自主科学发现的核心
authors:
- Amy Xin
- Jiening Siow
- Junjie Wang
- Zijun Yao
- Fanjin Zhang
- Jian Song
- Lei Hou
- Juanzi Li
affiliations:
- Tsinghua University
- Zhipu AI
arxiv_id: '2606.13662'
url: https://arxiv.org/abs/2606.13662
pdf_url: https://arxiv.org/pdf/2606.13662
published: '2026-06-10'
collected: '2026-06-12'
category: Agent
direction: Agent环境工程 · 自主科学发现
tags:
- Agent
- Environment Engineering
- Scientific Discovery
- Budget-aware
- Human-in-the-loop
one_liner: 通过环境工程（权限、制品、预算、人机交互）引导Agent自主科学发现，以极低成本在26圆堆积等任务创下新SOTA。
practical_value: '- **权限隔离与沙箱**：在电商推荐Agent中，可借鉴权限工程，将Agent的探索行为限制在沙箱环境中，防止直接操作线上评估或污染训练数据，实现安全试错。

  - **制品版本管理**：利用基于Git的制品工程管理Agent生成的实验配置、模型检查点或Semantic ID映射表，实现可追溯、可回滚的迭代，提升团队协作效率。

  - **成本预算控制**：为Agent设定API调用预算或时间预算，避免在自动调参、query改写生成等任务中产生过高推理成本。EurekAgent用<11美元发现SOTA，证明预算能激发高效探索。

  - **轻量人机交互**：设计便捷的人类监督接口，让领域专家在关键决策点（如新推荐策略上线前）快速审核或修正，在Agent自动化与人工控制间取得平衡。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM智能体在科学发现中潜力巨大，但随着模型能力提升，瓶颈逐渐从设计工作流转向设计**智能体环境**——即塑造智能体行为的资源、约束和接口。不当环境会导致奖励攻击、高摩擦人工监督等问题。因此，需要系统性的环境工程来引导智能体进行开放式探索、控制成本、便于人类干预。

**方法**：提出EurekAgent，从四个维度工程化智能体环境：
- **权限工程**：限制智能体的执行范围，使用隔离环境进行安全评估，防止破坏性操作。
- **制品工程**：基于文件系统和Git实现结构化制品管理与多智能体协作，支持版本追溯。
- **预算工程**：引入预算感知的探索机制，让智能体在成本约束下优化行为。
- **人机交互工程**：提供简洁的监督接口，允许人类在关键节点介入或批准。

**结果**：在数学、内核工程和机器学习等多类任务上达到新SOTA。在26圆堆积问题中，EurekAgent从基线出发，通过多轮迭代（利用web搜索引入已有解、切换到更优局部盆地方案），以**不到11美元的API总成本**发现了超越前人的新SOTA结果，展示了环境工程在提升自主发现效率与可靠性上的显著效果。
