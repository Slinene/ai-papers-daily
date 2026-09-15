---
title: Learning to Coach for Experiential Learning
title_zh: Learning to Coach：训练 LLM 教练从轨迹中提取可操作经验
authors:
- Guanheng Chen
- Tianzhu Ye
- Li Dong
- Xun Wu
- Shaohan Huang
- Furu Wei
affiliations:
- Microsoft Research
- Tsinghua University
arxiv_id: '2609.15851'
url: https://arxiv.org/abs/2609.15851
pdf_url: https://arxiv.org/pdf/2609.15851
published: '2026-09-14'
collected: '2026-09-15'
category: MultiAgent
direction: LLM 教练 · 经验学习与多智能体协作
tags:
- LLM-as-a-Coach
- GRPO
- Experiential Learning
- RL
- MultiAgent
one_liner: 训练一个 LLM-as-a-Coach 用 GRPO 从冻结 actor 的轨迹中提取经验，以引导正确性为奖励，显著提升推理与交互游戏表现
practical_value: '- **分离 actor 与 coach，避免主模型微调**：在电商推荐/搜索 Agent 中，可保持主策略或大模型冻结，训练一个轻量
  coach 从用户会话、行为轨迹、失败案例中提取可操作经验（如用户偏好摘要、失败原因、下一步策略），作为上下文注入主模型，既保留主模型通用能力，又降低全量微调成本。

  - **用下游可验证指标直接训练 coach**：将点击、转化、任务完成等可验证业务指标作为 reward，通过 GRPO 训练 coach 生成对特定 actor
  更有用的经验。same-instance reward 用于纠错和保留问题细节，cross-instance reward 鼓励提取跨用户/跨品类/跨场景的通用规则，可借鉴到跨域推荐或策略迁移。

  - **迭代式经验更新，算力用在刀刃上**：让 coach 在多轮交互中不断更新并缩短经验笔记，逐步收敛到更精炼的指导信息，降低后续推理成本。论文证明将额外算力花在迭代
  coach 引导上比单纯扩大 actor 解码预算更有效，这对于生成式推荐或 Agent 多步决策的推理优化有直接参考价值。

  - **OOD 迁移潜力**：在可验证任务上训练的 coach 可迁移到较难推理、交互游戏、指令跟随等未见任务，说明这种“经验提取”能力具有一定通用性，可用于跨任务的知识蒸馏与复用。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
LLM 在推理和交互任务中能从自身历史轨迹获得经验，但原始轨迹往往冗长、嘈杂，包含错误结论。直接 self-refinement 重喂整个轨迹无法区分有用与误导信息；微调 actor 会改变参数且昂贵，可能损害通用能力。因此需要一种解耦方案：冻结执行任务的 actor，训练一个专门的 LLM-as-a-Coach，从轨迹中提取可操作经验。

## 方法关键点
- 冻结 actor π_actor，训练 coach π_θ 从轨迹 (x, y) 生成经验 e。
- 奖励为：将 e 提供给 actor 在目标实例上生成的引导响应，由 verifier 打分是否正确。
- 两种奖励：same-instance 鼓励纠错、保留问题特定中间结果；cross-instance 在不相交 probe 集上评估，鼓励提取跨实例可复用规则。
- 用 GRPO 优化 coach，每个 source 轨迹采样 8 条候选经验，形成 advantage 组。
- 支持迭代：K=10 时 coach 基于上一轮经验和最新轨迹反复更新笔记，逐步精炼。

## 关键实验
- 数据集：DAPO-Math-17K 数学、FrozenLake 与 Sokoban 文本游戏；模型 Qwen3 1.7B/4B/8B。
- 对比基线：Base Model、Self-Refinement、untrained LLM-as-a-Coach。
- 结果：FrozenLake Qwen3-1.7B 从 7.4 提升到 65.4（untrained 23.4）；Sokoban Qwen3-4B 从 3.8 到 23.6；数学 Qwen3-4B 从 67.7 到 78.6。
- cross-instance 奖励训练在文本游戏上产生大幅可迁移提升，说明能学到环境通用规则；数学上 cross-instance 迁移有限。
- K=10 迭代时准确率持续上升，untrained coach 快速 platform；响应和经验长度逐步缩短，推理成本下降。
- 计算扩展：L2C 10 次迭代在数学上可超过 32k 解码预算（Qwen3-1.7B 71.0 vs 67.9），说明算力分配在迭代引导上更高效。
- 训练的 coach 适应特定 actor（NLL 下降），并迁移到 AIME 2026、FrozenLake、IFEval（+1.5~2.9pp）。

**最值得记住的一句话**：把额外算力花在可训练的 LLM-as-a-Coach 的迭代经验提取和引导上，比单纯扩大 actor 解码预算更高效；对于存在隐藏规则、需要从交互中学习的任务收益最大。
