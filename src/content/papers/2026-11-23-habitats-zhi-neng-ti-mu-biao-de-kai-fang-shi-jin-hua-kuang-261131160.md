---
title: 'Habitats: A Framework for Open-Ended Evolution of Agent Objectives'
title_zh: Habitats：智能体目标的开放式进化框架
authors:
- Nicolas Bolouri
- Gaya Mehenni
- Daniel Toyama
affiliations:
- Google DeepMind
arxiv_id: '2611.31160'
url: https://arxiv.org/abs/2611.31160
pdf_url: https://arxiv.org/pdf/2611.31160
published: '2026-11-23'
collected: '2026-11-24'
category: Agent
direction: Agent 目标开放式进化 · LLM 进化算子
tags:
- Open-ended evolution
- LLM-guided search
- Reward design
- Population-based training
- Quality diversity
one_liner: 分离种群级规划与奖励合成，用交叉适应度矩阵引导多样、可复用行为库的进化
practical_value: '- **Planner-Mutator 分离**：在电商/广告等 Agent 场景中，可让一个 LLM 根据策略种群的整体健康指标（如转化率集中度、行为多样性）决定探索方向，另一个
  LLM 只负责生成具体策略/文案，避免单一模型同时决定“探索什么”和“怎么实现”导致收敛到狭窄方案。

  - **用 cross-fitness matrix 度量行为多样性**：不要用策略文本/代码的差异衡量多样性，而用每个策略在他人目标上的表现剖面计算 cosine
  distance；可直接用于推荐策略库或 Agent 题库的质量-多样性管理，筛选真正功能不同的候选。

  - **离线进化策略库 + 在线 meta-routing**：先通过开放目标进化得到一个多样、冻结的策略库，再训练一个轻量 meta-policy 路由，可在少量在线样本内快速适应新目标；对应电商冷启动或新用户场景，可以离线生成多样推荐策略，在线快速选路。

  - **grounding 检查**：每个生成的 reward/策略必须可执行且超过随机策略基线，过滤不可学习或无效候选；在 LLM 生成推荐策略/文案时，可用随机或无策略基线做廉价过滤，提高输出可靠性。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
设计智能体该优化什么，往往和优化智能体本身一样困难。现有基于 LLM 的奖励生成方法通常为预定义任务精调目标，且把“选择探索什么”和“如何实现”耦合在同一个模型中，导致行为库变窄。当未来任务未知时，需要开放式目标发现，产生多样、可复用的行为集合。

**方法关键点**  
- Habitats 维护一个 reward-policy 对的种群，每代评估每个策略在所有种群 reward 上的表现，形成 cross-fitness matrix；列归一化后计算 Specialist Quality (SQ) 和 Behavioral Diversity (BD)。  
- 个体幸存需满足：策略在自身 reward 上优于所有其他策略，且超过随机策略基线，保证 reward 可学习且不琐碎。  
- 两阶段进化：Planner 依据种群健康指标（SQ、BD）决定后代数、选择父本、写出自然语言 mutation directive；Mutator 把 directive 和父本代码翻译成新的可执行 reward 程序，并通过语法检查和沙箱验证。  
- 只有 reward 参与进化，策略架构和优化过程固定；surviving policies 不再重训，只有新 reward 配新策略训练。

**关键实验与结果**  
在 Card Sandbox（离散、tabular Q-learning）和三个 MuJoCo 连续控制环境（CartPole、Hopper、Cheetah）上，对比 Independent Generation（无父本条件、无 Planner）和 Direct Mutation（有父本条件但无 Planner）。Habitats 最终 Behavioral Diversity 达到 0.3825，是 Direct Mutation 的 1.8 倍、Independent Generation 的 2.5 倍；在多数环境取得最高 Grounded Behavioral Profile Coverage，同时保持有竞争力的 Specialist Quality。下游测试中，10 个进化期间未见过的任务，使用 15 个冻结 Habitats 策略库和 meta-policy 路由，在 10,000 adaptation episodes 时 paired win rate 达 0.617，超过 size-matched baselines，并超过训练 20,000 episodes 的 task-specific Scratch 策略。此外，更强的 LLM backbone（gemini-4-argon）可进一步提升多样性而不牺牲质量。

**最值得记住的一句话**  
分离种群级规划与奖励合成，用 cross-fitness 定义行为多样性而非代码多样性，让 LLM 根据种群健康引导探索，能产生多样且可复用的行为库。
