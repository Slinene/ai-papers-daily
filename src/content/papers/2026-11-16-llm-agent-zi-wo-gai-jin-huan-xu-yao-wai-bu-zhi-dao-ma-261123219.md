---
title: Do LLM Agents Still Need to Be Told How to Self-Improve?
title_zh: LLM Agent 自我改进还需要外部指导吗？
authors:
- Shobhita Sundaram
- Cansu Sancaktar
- Phillip Isola
affiliations:
- MIT CSAIL
- University of Tübingen
arxiv_id: '2611.23219'
url: https://arxiv.org/abs/2611.23219
pdf_url: https://arxiv.org/pdf/2611.23219
published: '2026-11-16'
collected: '2026-11-18'
category: Agent
direction: LLM Agent 自组织自我改进
tags:
- Self-Improvement
- LLM Agents
- Context Optimization
- Curriculum Learning
- Generalization
one_liner: 给定基础工具与预算、不指定循环，足够强的 LLM 能自主构造自学习流程并实现跨环境泛化。
practical_value: '- 在搜索/推荐系统中，可用 LLM 作为 teacher 自主优化 prompt 或 skill files（文本上下文）而非权重，配合沙箱与模拟器，设置
  update/gameplay 预算，让它自动生成候选任务、运行 A/B 对比、沉淀经验，降低人工调 prompt 成本。

  - 借鉴论文中的 A/B 测试策略：teacher 对同一批 query/请求分别应用新旧文本工件直接测量收益，而不是凭主观判断；可工程化到 prompt 或策略迭代流程中。

  - 学习论文中的可学习性任务筛选：agent 重点 replay 胜率 20-60% 的中等难度样本，与 UED/Zone of Proximal Development
  思路一致；在电商数据中可优先挑选模型表现中等的样本做针对性优化，避免简单/太难样本浪费预算。

  - 注意信息过拟合：提供过多线上评测细节（如特定 token/turn 预算、窄分布描述）会提升域内指标但损害泛化；在生成式推荐或 prompt 自动调优时，需平衡环境信息丰富度与跨场景迁移能力。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM agent 自我改进通常依赖人类预设的优化循环：如何生成数据、如何更新、使用什么反馈。随着模型越来越强，一个问题浮现：是否仍需要人类指定“如何自我改进”？本文在 gameplay 环境测试：给 frozen LLM 教师 agent 基础工具（Read/Write/Bash/Gameplay）、资源预算和总体目标，但不提供真实游戏、不指定任何学习循环，观察它能否自主构造学习算法，并在 held-out 任务上提升玩家表现。

## 方法关键点
- 教师-玩家同源：同一 frozen LLM 实例分别作为 teacher 和 player；teacher 修改 player 上下文（prompt + skill files），player 在 turn-based 游戏（PuzzleScript 或 Python）中行动。
- 工具集：Read/Write/Bash/Gameplay；teacher 可自由生成游戏、运行 player、观察 transcript/score，并编辑文本工件。更新预算 20，gameplay 预算 150。
- 上下文优化而非权重优化：文本更新可读、可解释、可迁移，且适用于闭源模型。
- 评估：held-out benchmarks 包括 PuzzleScript-t20/t30、ARC-AGI-3 L1、MazeBench；度量 J(c_final)-J(c0) 是否为正。

## 关键结果
- Claude Opus-5 在 PuzzleScript-t20 上胜率 +20%，GPT-6 Astra +10%，GLM 5.3 +6%；上一代模型几乎无提升。
- 自组织学习在相同 rollout 预算下达到与 prescribed 优化算法 GEPA 相当的性能。
- 学到的文本工件跨环境迁移：PuzzleScript-t30 +9%，ARC-AGI-L1 +21%，MazeBench SPL +0.15。
- 有效自学者显示类似 Zimmerman 自我调节学习的行为：A/B 测试、难度过滤、生成对抗性游戏、验证回归；并集中精力在胜率 20-60% 的中等难度任务（inverted-U learnability）。
- 提供更多评测环境信息可提升域内性能但可能导致过拟合（t30 下降）。
- 跨模型迁移：GPT-6 Astra 的优化上下文使 Claude Opus-5 从 25.4% 提升至 47.5%，Opus-5 的上下文使 GPT-6 Astra 从 67.1% 提升至 72.1%。

最值得记住的一句话：**给定基础工具与预算，足够强的模型能够自主构建有效的自学习流程，并产生跨环境可迁移的文本工件。**
