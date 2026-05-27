---
title: Efficient Agentic Reinforcement Learning with On-Policy Intrinsic Knowledge
  Boundary Enhancement
title_zh: 基于在线策略知识边界增强的高效智能体强化学习
authors:
- Dingwei Chen
- Zefang Zong
- Zhipeng Ma
- Leo Luo
- Yang Li
- Chengming Li
- Peng Chen
- Jie Jiang
affiliations:
- Tencent Inc
- The Chinese University of Hong Kong
- Shenzhen MSU-BIT University
arxiv_id: '2605.26952'
url: https://arxiv.org/abs/2605.26952
pdf_url: https://arxiv.org/pdf/2605.26952
published: '2026-05-25'
collected: '2026-05-27'
category: Agent
direction: Agent 工具调用效率优化
tags:
- Agentic RL
- Tool Call Reduction
- Knowledge Boundary
- On-policy
- Dual-path rollouts
- Efficiency
one_liner: 通过在线双路径 rollout 探测知识边界，构建细粒度监督信号，在不牺牲准确率的前提下减少冗余工具调用 18%。
practical_value: '- 在 Agent RL 训练中引入双路径（with-tool / no-tool）rollout 来动态评估模型是否真正需要工具，这一探测机制可直接用于电商对话
  Agent 或推荐 Agent 的工具调用决策，避免因盲目调用搜索、计算等工具而增加延迟和成本。

  - 将问题按知识边界分为四类（Tool‑dependent / Efficiency / Hallucination / Both‑wrong）并差异化构建监督信号，这种细粒度策略可迁移到多智能体协作或生成式推荐场景，用于优化不同情境下的资源调度与动作选择。

  - 该方法作为即插即用模块，与 GRPO / DAPO / GSPO / AEPO 等多种主流 Agentic RL 算法兼容，无需修改奖励函数或优化流程，适合在现有业务
  RL 训练框架上快速叠加实验。

  - 训练过程中轨迹类别的分布变化（如 Efficiency 比例上升）可作为知识内化的可解释指标，帮助监控 Agent 对工具依赖的演化，为线上策略调整提供信号。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
Agentic RL 训练 LLM 使用外部工具时，会逐渐产生大量冗余工具调用（认知卸载），不仅浪费计算资源，还可能引入噪声导致答案质量下降。现有基于奖励塑形的方法（如 OTC‑PO）对工具调用施加全局惩罚，容易诱导智能体不分场合地抑制工具使用，造成奖励破解，且无法适应模型知识边界在训练过程中的动态变化。

**方法关键点**
- **双路径 rollout**：对每个训练问题，同时采样带工具（with‑tool）和无工具（no‑tool）的多条轨迹。
- **知识边界探测**：比较两条路径的正确性，判断问题是否在模型参数知识范围内（即无工具也能答对）。
- **四类信号构建**：根据 with‑tool 和 no‑tool 的正确性组合，将问题分为 Tool‑dependent（需工具，选最少工具调用的正确轨迹）、Efficiency（无需工具，选无工具正确轨迹）、Hallucination（无工具对而有工具错，选无工具轨迹）和 Both‑wrong（跳过），并构造对应的监督目标。
- **联合训练**：在标准 RL 损失（如 GRPO）之上加入选出的目标轨迹的交叉熵损失 L_AKBE，通过系数 λ 平衡，实现在线知识边界的动态跟踪与优化。

**关键实验**
在 HotpotQA、2WikiMultihopQA、MuSiQue、Bamboogle、NQ、TriviaQA、PopQA 共 7 个 QA 基准上，使用 Qwen3‑4B 和 Qwen2.5‑7B 进行实验。与 ReAct、Search‑o1、R1‑Searcher、Search‑R1、OTC‑PO、β‑GRPO、Offline AKBE 等多个基线对比，AKBE 平均准确率提升 +1.85，工具调用减少 18%，工具生产力提升 25%。消融实验表明三类信号缺一不可，其中 Tool‑dependent 信号有效防止了对必要工具调用的过度抑制。此外，AKBE 与多种 RL 算法（DAPO、GSPO、AEPO）组合均能一致提升，训练速度反而比原始 GRPO 快约 15%。

**核心洞见**
通过在线双路径 rollouts 动态捕捉模型的知识边界，并转化为实例级的细粒度监督信号，可以同时实现准确率提升和工具调用精简，避免粗粒度奖励塑造带来的副作用。
