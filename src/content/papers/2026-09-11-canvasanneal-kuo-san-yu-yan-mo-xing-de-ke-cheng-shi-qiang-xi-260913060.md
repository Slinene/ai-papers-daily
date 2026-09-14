---
title: 'CanvasAnneal: Curriculum Reinforcement Learning for Diffusion Language Models'
title_zh: CanvasAnneal：扩散语言模型的课程式强化学习框架
authors:
- Blake Olson
- Yuhang Song
- Emmett McQuinn
- Yuan Shangguan
affiliations:
- Google DeepMind
arxiv_id: '2609.13060'
url: https://arxiv.org/abs/2609.13060
pdf_url: https://arxiv.org/pdf/2609.13060
published: '2026-09-11'
collected: '2026-09-14'
category: Training
direction: 扩散语言模型 · 课程强化学习
tags:
- Diffusion Language Models
- Curriculum RL
- Exploration Bottleneck
- GRPO
- Reasoning
- Tool-use
one_liner: 通过向扩散 RL 训练初期注入教师推理轨迹并逐步退火，缓解探索瓶颈，提升数学推理与工具调用性能
practical_value: '- 在生成式推荐模型的 RL 训练中（如推荐理由、query 改写、对话式 Agent），早期探索难可用教师模型生成的高质量轨迹初始化
  action/context，再逐步减少依赖，能显著加快收敛。

  - 若业务采用 diffusion/非自回归生成（如并行生成候选序列、文案），可将教师轨迹作为初始 canvas 的 masked/部分可见条件，做课程退火，缓解探索瓶颈。

  - 设计可退火的先验注入而非固定 prompt，监控 reward 提升曲线；该方法对多步推理、工具调用等困难任务更有效，简单任务收益有限，需评估任务难度。

  - 工程上保存 teacher 轨迹作为额外输入，注意训练/推理解耦：推理时不再提供教师轨迹，避免分布不一致。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：扩散语言模型（DLMs）具备并行生成优势，但在复杂推理和工具调用上落后于自回归模型；标准 RL 训练存在探索瓶颈。

**方法关键点**：提出 CanvasAnneal，一种课程式扩散 RL 框架。训练初期把强教师模型生成的推理轨迹注入初始扩散画布，作为 warm-start 引导探索；随着训练推进，逐步移除引导，让模型自主生成更多推理序列。核心是课程退火策略，将外部先验逐步过渡到模型自身策略。

**结果**：在 MATH500、Countdown、Tau2 等数学推理和工具调用基准上，CanvasAnneal 相比标准 diffu-GRPO 取得提升，并在多个任务上显著加速 reward 提升，但增益具有任务依赖性。实验表明结构化训练时引导能缓解扩散 RL 的探索瓶颈，加快困难任务的收敛。
