---
title: 'Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement
  Learning'
title_zh: 教LLM自我进化：用强化学习培养核心元技能
authors:
- Shujin Wu
- Cheng Qian
- Xiusi Chen
- Heng Ji
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2607.21971'
url: https://arxiv.org/abs/2607.21971
pdf_url: https://arxiv.org/pdf/2607.21971
published: '2026-07-24'
collected: '2026-07-27'
category: Training
direction: RL训练自我进化元技能
tags:
- Meta-Skills
- Reinforcement Learning
- Self-Evolution
- Code Generation
- Test-time Scaling
one_liner: 通过合成进化轨迹和进化感知的RL，教会LLM自我反思等元技能，大幅提升跨领域迭代优化能力
practical_value: '- 借鉴进化轨迹合成方法：在搜索/推荐场景中，收集多轮策略调整的历史数据（如出价序列、排序规则迭代），构造包含状态、收益、历史尝试的训练样本，让模型学会基于历史决策反馈进行增量优化。

  - 奖励塑形技巧：利用业务连续指标（CTR、转化率、时长）设计fitness score，替代二元成败，为RL训练提供更细粒度的反馈，引导模型生成更高效的策略。

  - 推理时进化搜索：部署推荐/广告Agent时，可对同一请求执行多轮推理，每轮根据环境模拟反馈（如预测的CTR）微调输出，最后选择最优解，实现test-time自我改进。

  - 域无关元技能迁移：在代码数据上训练获得的自我反思与迭代优化能力，可迁移到推荐文案生成、搜索词优化等开放域任务，减少对标注数据的依赖。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM在测试时通过迭代自我进化（如AlphaEvolve）可大幅提升性能，但传统后训练忽视支撑这一过程的元技能（如基于环境反馈的自我反思）。MetaEvolve旨在显式培养这些域无关的元技能，使模型能自主多轮优化。

**方法**：以代码生成为训练场，利用程序执行提供超越二元对错的连续适应度信号（正确性+效率）。首先合成进化轨迹数据：每条轨迹包含当前程序、适应度得分和先前尝试历史。然后用强化学习训练模型，奖励由单元测试执行给出的可验证指标计算，使模型学会进化感知的生成策略。推理时引入进化搜索，迭代改进解。

**结果**：在7个代码基准上，分布内任务绝对提升10.01%，分布外任务提升24.12%；在完全未见过的开放算法优化问题上，相对提升46.9%。证明显式培养自我进化元技能是一条通往更强自主进化AI的有效路径。
