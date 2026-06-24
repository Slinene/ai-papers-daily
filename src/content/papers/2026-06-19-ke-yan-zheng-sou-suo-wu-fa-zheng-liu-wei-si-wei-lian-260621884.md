---
title: A Verifiable Search Is Not a Learnable Chain-of-Thought
title_zh: 可验证搜索无法蒸馏为思维链
authors:
- Harsh Patel
affiliations:
- Independent Researcher
arxiv_id: '2606.21884'
url: https://arxiv.org/abs/2606.21884
pdf_url: https://arxiv.org/pdf/2606.21884
published: '2026-06-19'
collected: '2026-06-24'
category: Reasoning
direction: 思维链蒸馏的局限性
tags:
- chain-of-thought
- search
- distillation
- LoRA
- reasoning
- backtracking
one_liner: 对需回溯搜索的任务，直接蒸馏思维链会失败，模型仅学到表面模板而非搜索能力
practical_value: '- 当推荐/Agent任务包含需搜索（如回溯、试错）的子过程时，避免直接蒸馏为端到端思维链，因为模型会退化为输出模板而非执行搜索。

  - 可将搜索的核心组合空间预计算为显式目录（类似推荐系统中的索引或候选池），让模型做检索与验证，从而将任务从搜索变为记忆+比较。

  - 在RL训练中使用可验证奖励时，若任务需要搜索，应确保奖励能指导前向决策，否则稀疏奖励可能导致模型学会“猜测”模板而不探索。

  - 对于生成式推荐中需多步推理的输出（如解释生成），应验证是否包含隐藏的搜索步骤，考虑将其拆分为搜索阶段和生成阶段。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：常用假设——任何可用短程序解决的任务都能通过写出步骤微调让模型学会——对一类需要回溯搜索的过程不成立。本文在9个由确定性生成器产生的推理任务上验证。  
**方法**：将生成器逆向为Python求解器，渲染为思维链，通过rank-≤32的LoRA蒸馏到30B（3.5B active）的Nemotron模型。任务分为前向可计算型（查找/算术、8-bit布尔规则）和需回溯搜索的cryptarithm任务。还尝试了RL、自训练等11种思维链设计。  
**关键结果**：前向任务迁移良好（≥0.99和0.68），但cryptarithm准确率仅0.01–0.07，尽管搜索求解器正确率71%。模型在算术行上表现优异（97–100%），且71%情况下将正确密码排入top-8，却无法从左到右进行搜索推导。微调学到的是“verdict-as-token”模板，判决正确率仅16–57%。该天花板在3B至671B多种模型和微调/提示下复现。控制实验揭示：若给定密码密钥使推导变为前向，同一批样例准确率从0.03跃升至0.57。当程序唯一的解是搜索无信息结构时，不存在可模仿的前向思维链。通过预计算组合核心为目录，将思维链简化为回忆+验证，任务变得可学习，第一名方案达到Private LB 0.92。结论：蒸馏学到的是记忆与验证，而非搜索。
