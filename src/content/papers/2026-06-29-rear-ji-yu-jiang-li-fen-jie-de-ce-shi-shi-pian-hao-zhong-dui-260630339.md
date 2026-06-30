---
title: 'REAR: Test-time Preference Realignment through Reward Decomposition'
title_zh: REAR：基于奖励分解的测试时偏好重对齐
authors:
- Fuxiang Zhang
- Pengcheng Wang
- Chenran Li
- Yi-Chen Li
- Yuxin Chen
- Lang Feng
- Chenfeng Xu
- Masayoshi Tomizuka
- Bo An
affiliations:
- Nanyang Technological University
- University of California, Berkeley
- Nanjing University
arxiv_id: '2606.30339'
url: https://arxiv.org/abs/2606.30339
pdf_url: https://arxiv.org/pdf/2606.30339
published: '2026-06-29'
collected: '2026-06-30'
category: LLM
direction: 测试时偏好对齐 · 奖励分解
tags:
- Test-time Alignment
- Reward Decomposition
- LLM
- Preference Realignment
- Best-of-N
- Tree Search
one_liner: 提出奖励分解方法 REAR，在测试时无需训练即可重对齐 LLM 至多样化用户偏好。
practical_value: '- 测试时偏好干预：无需额外训练，适合广告文案生成、商品描述等需要快速适配不同风格偏好的场景。

  - 奖励分解视角：将生成奖励分解为任务相关和偏好相关项，通过调整权重可细粒度控制输出属性（如多样性、长度、倾向）。

  - 与解码策略集成：可无缝接入 Best-of-N、树搜索等测试时优化框架，实现高效可扩展的偏好引导。

  - Agent 动态偏好适应：在对话或推荐 Agent 中，用户偏好变化时可通过调整 REAR 权重实时重对齐，无需重训模型。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 后训练对齐成本高，测试时缩放（TTS）虽训练自由但主要用于数学、编码等可验证任务，难以处理主观偏好。为此，将偏好对齐重新定义为测试时重对齐问题，旨在无需训练即可让模型快速适配不同用户偏好。

**方法**：核心洞察是将奖励函数分解为两部分：与问题相关的奖励（如正确性）和与偏好信息相关的奖励（如风格）。通过选择性缩放这两部分的比例，推导出重对齐奖励 REAR。REAR 可进一步表示为 token 级策略对数概率的线性组合，计算高效且易于集成到 Best-of-N 采样、树搜索等现有 TTS 算法中。

**结果**：实验表明，REAR 在多种偏好对齐任务上优于传统测试时基线，实现了可扩展的实时重对齐，并在数学和视觉任务上通过适当偏好设置展现了泛化能力。
