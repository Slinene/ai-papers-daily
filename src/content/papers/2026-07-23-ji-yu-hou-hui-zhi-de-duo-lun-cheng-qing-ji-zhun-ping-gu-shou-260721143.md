---
title: 'One More Turn, Less Regret: A Regret-Based Multi-Turn Benchmark for LLMs''
  Clarification Policies'
title_zh: 基于后悔值的多轮澄清基准：评估LLM助手的澄清策略
authors:
- Minh Ngoc Ta
- My Anh Tran Nguyen
- Duong D. Nguyen
- Yuxia Wang
- Preslav Nakov
affiliations:
- MBZUAI
- BKAI Research Center, Hanoi University of Science and Technology
- INSAIT, Sofia University "St. Kliment Ohridski"
arxiv_id: '2607.21143'
url: https://arxiv.org/abs/2607.21143
pdf_url: https://arxiv.org/pdf/2607.21143
published: '2026-07-23'
collected: '2026-07-24'
category: Agent
direction: 对话Agent澄清策略的后悔值评估基准
tags:
- Clarification
- Multi-turn
- Regret
- Benchmark
- LLM agent
- Product recommendation
one_liner: 提出基于后悔值的多轮澄清基准RegretBench，衡量LLM助手澄清策略的效率与效用，避免仅看最终成功。
practical_value: '- **对话推荐中的澄清策略评估**：在电商对话推荐中，用户需求往往模糊，可借鉴RegretBench的后悔值度量，评估系统是否在正确时机提问、何时停止，避免无效追问或过早错误回答，优化用户交互体验和转化效率。

  - **优化Agent的停止决策**：后悔值框架量化了“多问一轮”的机会成本，可直接用于强化学习稀疏奖励设计，训练Agent在信息增益低于阈值时果断停止，减少对话轮次和用户流失。

  - **隐藏意图数据构建**：RegretBench的隐藏意图设定可用于生成大量用户意图不确定的模拟训练数据，提升推荐Agent对模糊查询的处理能力，特别适合冷启动或用户画像缺失的场景。

  - **多指标评估体系**：该工作提醒不要仅看最终准确率，而应同时关注交互成本、无效澄清率，对应搜索推荐中的“结果页翻页深度”或“对话轮次”，可迁移到消息推送频率、主动推荐时机的决策中。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有评估多聚焦最终回答正确与否，忽略澄清过程的效率和时机。模糊用户查询需要LLM助手做出多轮序贯决策——是否问、问什么、何时停、何时答，仅看最终成功无法区分模型的澄清策略优劣。

**方法**：引入RegretBench基准，采用**隐藏意图**形式化用户模糊性，通过**语义状态跟踪**衡量意图解析进度。核心定义**后悔值**——模型实际表现与参考最优澄清策略之间的价值损失，从意图识别精度、交互轮次成本、无效澄清占比和最终后悔值四个维度联合评估，而非仅比较单一问答质量。

**结果**：在开放域QA和产品推荐两个场景实验发现，**最终准确率相似的模型在效率、鲁棒性和停止决策上差异显著**。有效澄清需要模型在正确时机问正确问题，并及时停止；仅追求提问质量而忽视决策时机，会导致交互冗余或过早误解。
