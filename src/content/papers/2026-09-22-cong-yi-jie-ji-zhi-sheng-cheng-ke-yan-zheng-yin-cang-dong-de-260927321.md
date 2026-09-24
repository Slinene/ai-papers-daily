---
title: 'Verifiable Hidden Dynamics Play: Generating Agentic RL Environments from Solved
  Mechanisms'
title_zh: 从已解机制生成可验证隐藏动态的智能体RL环境
authors:
- Xinjie Shen
- Wei Fan
- Xudong Guo
- Jianhong Tu
- Yang Su
- Chuqiao Kuang
- Yinger Zhang
- Dayiheng Liu
affiliations:
- Georgia Institute of Technology
- Alibaba Token Foundry, Alibaba Group
arxiv_id: '2609.27321'
url: https://arxiv.org/abs/2609.27321
pdf_url: https://arxiv.org/pdf/2609.27321
published: '2026-09-22'
collected: '2026-09-24'
category: Agent
direction: Agentic RL 环境生成与策略训练
tags:
- Agentic RL
- Environment Generation
- Verifiable Rewards
- Operations Research
- GRPO
- LLM Agents
one_liner: 先求解运筹模型再渲染为有状态工具环境，用同一参考解固定奖励，低成本生成可验证的Agentic RL训练环境
practical_value: '- 借鉴机制优先构建：在电商/供应链场景，可用库存控制、路径规划、调度等运筹模型作为底层机制，用求解器预先算出最优值和默认策略值，生成可执行环境并归一化奖励（r=(u-u0)/(u*-u0)），避免人工标注或
  LLM judge，获得可靠训练信号。

  - 通过语料库 grounding 让同类机制产生多样场景：从商品文案、物流文档、活动规则等真实语料采样，让 LLM setter 生成具体工具、数据库和玩家指令，低成本扩增训练环境（每条约
  $0.01–$0.03）；可迁移到电商长周期店铺运营、库存补货、多仓履约等 Agent 训练。

  - 设计信息不对称接口训练主动信息获取：将需求、库存、价格等关键参数设为隐藏，要求 Agent 通过 probe 工具查询后再决策；论文显示同一模型 written-out
  分数 0.962 但 agentic 仅 0.204，说明有状态交互是主要短板，训练后提升至 0.815；可在对话式导购、动态定价、客服工单处理中应用。

  - 使用 GRPO 对同一环境的多条 rollout 做组内对比，配合 admission 检查（可执行性、默认奖励区间、最优解一致性）保证环境质量；同时实验表明冻结
  35B setter 即可生成有效环境，无需前沿模型，可降低工程门槛。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM agent 在长程、状态演化、延迟结果的任务中表现明显下降，训练需要多样化环境、可靠奖励信号和低扩展成本。但现有生成管线通常先构建环境再定义奖励或标注轨迹，导致 dynamics 与 evaluation 事后对齐，影响训练质量。

**方法关键点**：
- 机制优先（mechanism-first）构建：先采样并求解数学机制 M(θ) 得到最优值 u* 和默认策略值 u0，据此固定奖励规则 Rθ；再将模型实现为可执行 dynamics D(θ) 并包装成有状态环境 E(θ)。
- 语料 grounding：从 28 个主题领域的真实文档采样 seed，冻结 LLM setter 生成场景、关系数据库、≥10 个工具和玩家指令，每条环境成本约 $0.01–$0.03。
- 信息不对称接口：策略只能通过 probe/decision/clock 等工具观察状态，关键参数和参考解不可直接读取；奖励归一化为 clip[0,1]((u(π;θ)-u0)/(u*-u0))。
- 训练使用 GRPO，admission 检查可执行性、默认奖励区间和最优解一致性，最终生成 3,300 个环境，平均 59.7 个助手回合。

**关键实验**：
- 训练 Qwen3.6-35B-A3B 后，五个优化家族平均 agentic score 从 0.204 提升到 0.815；held-out 训练家族 +0.56，near-OOD +0.63，far-OOD 两组分别为 +0.24 和 +0.16。
- 外部基准：E-Commerce Bench 365 天店铺经营中，训练后余额从 54,294 增至 182,844（3.4×），超过 Qwen3.7-Max 的 165,224，且无破产；BFCL V4 交互单元提升 2.84 点；TravelBench plan score 从 0.700 到 0.794。
- 三种形式对比（written-out / informed-agentic / agentic）：base 得分为 0.962 / 0.231 / 0.204，训练后为 0.992 / 0.875 / 0.815，表明 gap 主要来自有状态交互而非数学求解能力。
- Co-scaling：knapsack 从 6×5 到 11×11，base 分数从 0.432 降至 0.085，但训练后升至 0.843 至 0.946，增益随规模增加。

**最值得记住**：机制优先让同一个已解模型同时固定 dynamics 和奖励，把可验证 RL 从答案拓展到轨迹。
