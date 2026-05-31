---
title: How's it going? Reinforcement learning in language models recruits a functional
  welfare axis
title_zh: 语言模型中强化学习招募功能福利轴
authors:
- Andy Q Han
- David J. Chalmers
- Pavel Izmailov
affiliations:
- New York University
arxiv_id: '2605.30232'
url: https://arxiv.org/abs/2605.30232
pdf_url: https://arxiv.org/pdf/2605.30232
published: '2026-05-28'
collected: '2026-05-31'
category: Training
direction: 强化学习表征工程与模型对齐
tags:
- reinforcement learning
- representation analysis
- concept vector
- alignment
- interpretability
one_liner: 强化学习通过招募预训练模型已有的“功能福利”表征轴广泛影响行为，而非从零创建。
practical_value: '- 在电商推荐对话Agent中，可借鉴提取“福利轴”向量的方法，作为模型内部状态的监控器，用于检测拒绝、不确定或消极倾向，及时干预。

  - 通过操纵该轴（正向或负向），可以控制推荐语气：正向偏置生成更乐观积极的推荐话术，负向偏置可用来模拟谨慎或风险提示场景。

  - 该轴在RL前后都存在，表明可以用它作为预训练模型的zero-shot行为调节器，无需额外训练即可影响Agent的决策风格。

  - 这一发现提示在奖励设计中，即使目标仅限定在特定任务，RL也会放大模型原有的广泛偏好表征，因此设计奖励时需考虑可能泛化的行为后果。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：探究强化学习（RL）如何改变语言模型内部表征。已有研究表明后训练往往放大预训练已有能力，但具体机制不明。
**方法**：在语义中立的迷宫环境中训练多个LLM，提取奖励与惩罚轨迹的“概念向量”。利用这些向量在迷宫外场景进行干预评估，包括促进失败/不可能令牌、对齐情绪概念、追踪目标完成度、引导自报等。控制变量包括奖励映射、模型规模、指令微调、RL算法、模型家族及LoRA vs 全微调。
**关键发现**：
- 惩罚向量表现为稳定的负福利表征（激发失败、负情绪、拒绝、回溯等），奖励向量呈镜面对称，二者近乎反平行。
- 效果在迷宫训练前就已存在，仅预训练模型亦能观察到相似效应，表明该“功能福利轴”原生于预训练模型，RL仅将其招募并增强。
- 使用SFT替代RL仍可产生类似效果，但RL更显著。
- 该轴可解释为系统对目标达成情况的内部评估器，影响输出范围远超训练任务。
