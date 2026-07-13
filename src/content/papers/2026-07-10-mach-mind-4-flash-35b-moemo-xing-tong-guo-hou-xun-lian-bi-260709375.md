---
title: Mach-Mind-4-Flash Technical Report
title_zh: Mach-Mind-4-Flash：35B MoE模型通过后训练比肩百B级性能
authors:
- Foundation Model Team
affiliations:
- Li Auto Inc.
arxiv_id: '2607.09375'
url: https://arxiv.org/abs/2607.09375
pdf_url: https://arxiv.org/pdf/2607.09375
published: '2026-07-10'
collected: '2026-07-13'
category: Agent
direction: Agent后训练与强化学习优化
tags:
- MoE
- Reinforcement Learning
- Knowledge Distillation
- Token Efficiency
- Post-training
- Agent
one_liner: 35B MoE仅3B激活参数，通过多专家RL与MOPD蒸馏融合，在Agent基准上超越10-30倍激活参数的大模型
practical_value: '- **多专家在线蒸馏（MOPD）**：为电商搜索推荐中的多目标（如点击率、转化率、多样性）独立训练RL专家，再通过MOPD路由融合到单个轻量模型，避免多目标奖励混合导致的指标跷跷板效应，且新增目标只需注册新教师，零代码侵入。

  - **奖励课程设计**：在稀疏奖励场景（如长周期转化）借鉴两阶段课程，先用过程奖励（中间行为反馈）冷启动，再切换到最终结果奖励，解决强化学习冷启动困难。

  - **Token效率优化（HMPO）**：对于推荐系统对话Agent或生成式推荐中的过长推理链，可引入基于自适应长度预算的强化学习压缩，在保证推荐质量前提下降低推理成本，实现19-46%的文本压缩且精度损失≤0.7%。

  - **环境扩展（EnvScaling）**：为Agent训练构建可执行验证的环境池（如文件系统、状态模拟等），可迁移至电商场景，用于模拟用户端到端的操作路径，生成高难度、可验证的决策轨迹，驱动深度搜索或购物Agent的强化学习优化。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：大模型推理成本高昂，万亿参数模型难以在延迟敏感场景落地；而单纯扩展预训练计算已非唯一路径。后训练优化可将小模型推至前沿性能，本文探索在仅3B激活参数的35B MoE模型上，通过大规模强化学习、专家集成与推理效率优化，达到或超越100B级以上模型在数学、代码、指令遵循、安全与自主Agent任务上的表现。

**方法关键点**
- **三阶段流水线**：SFT奠定基础 → 并行训练推理、通用、Agent三大轨道的多个RL专家 → 通过Multi-Teacher On-Policy Distillation (MOPD) 将专家融合为统一模型 → 使用Hybrid Median-length Policy Optimization (HMPO) 压缩生成长度。
- **MOPD**：为每个专家训练一个冻结教师，每个训练样本按路由键分发给对应教师，学生在其自身rollout上最小化token级反向KL散度，替代混合奖励RL，消除能力跷跷板。专家参数与学生匹配，教师自身见过的提示进一步提升迁移效果。
- **领域特定RL设计**：推理与代码采用两阶段奖励课程（过程奖励→结果奖励），数学以确定性验证为基础；工具使用RL扩展了可执行环境（EnvScaling），覆盖文件系统、可编程状态与模拟器三类环境，采用组相对策略优化与动作token掩码；安全RL同时涵盖内容安全与行为安全；代码智能体使用容器化执行环境与XML工具模板，SFT数据经错误掩码处理。
- **HMPO**：单阶段RL，动态从正确rollout的中位数长度计算自适应预算，结合正确性优先的乘法奖励（错误答案奖励强制归零），防止奖励黑客，实现推理链压缩。
- **基础设施**：统一RL/OPD训练框架，动态多教师弹性调度；SonicMoE算子加速与共享专家分段融合，训练端到端提速17%。

**关键实验**
- 在AIME'26数学竞赛（92.70）、LiveCodeBench-V6（80.91）、IFEval（94.64）、IFBench（82.82）、BFCL-v4（75.80）、BrowseComp-zh（72.31）、ClawBench（84.20）等基准上，Mach-Mind-4-Flash领先或持平于激活参数为3-30倍的模型（如Qwen3.5-122B-A10B、Kimi-K2.5-1T-A32B等）。
- 消融显示MOPD融合后各能力普遍保留且个别超越独立专家；HMPO将生成长度压缩19-46%，且数学、代码、科学推理任务准确率损失不超过0.7个百分点。

**一句话要点**：通过专业化RL训练再蒸馏集成，配合Token效率优化，3B激活参数的MoE模型可在Agent综合能力上媲美百B级大模型。
