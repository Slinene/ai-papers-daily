---
title: 'REVES: REvision and VErification--Augmented Training for Test-Time Scaling'
title_zh: REVES：面向测试时扩展的修订与验证增强训练
authors:
- Yuanxin Liu
- Ruida Zhou
- Xinyan Zhao
- Amr Sharaf
- Hongzhou Lin
- Arijit Biswas
- Mohammad Ghavamzadeh
- Zhaoran Wang
- Mingyi Hong
affiliations:
- Northwestern University
- Amazon AGI
- Qualcomm AI Research
- University of Minnesota
arxiv_id: '2606.18910'
url: https://arxiv.org/abs/2606.18910
pdf_url: https://arxiv.org/pdf/2606.18910
published: '2026-06-16'
collected: '2026-06-19'
category: Reasoning
direction: 测试时扩展训练 · 多步推理修订与验证
tags:
- test-time scaling
- sequential revision
- multi-turn RL
- off-policy data
- verification
- reasoning
one_liner: 从成功修正轨迹中抽取“接近正确”的中间步骤，构造修订与验证提示进行两阶段交替训练，显著提升多步推理测试时性能
practical_value: '- **多步修正与验证分离**：将中间错误转化为独立的修订和验证提示，可借鉴到 Agent 自我修正流程中，将生成改进与错误检测解耦，提升多轮交互的可靠性。

  - **高效数据利用**：利用成功修正轨迹中的 near-miss 样本生成 off-policy 训练数据，适用于推荐 Agent 的在线学习，减少昂贵的长链采样开销。

  - **两阶段交替训练**：在线数据增广与策略优化交替的框架，可迁移到需要策略迭代的推荐系统（如动态创意优化、查询改写），平衡探索与利用。

  - **约束泛化能力**：在约束满足任务上的泛化表现提示，该方法能增强模型对结构化规则的遵循能力，可用于推荐系统中的合规性校验或商品描述约束生成。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：标准后训练优化单次输出，与测试时多步序列修订的动态存在根本性错配；现有方法直接优化多步轨迹，未充分利用中间步骤中高质量的错误（near-miss），从而错失从纠正过程中学习的机会。

**方法**：提出 REVES，一种两阶段迭代框架，交替进行（1）在线数据/提示增广和（2）策略优化。核心是从成功修正轨迹中提取“接近正确”的中间答案，将其解耦为修订提示和验证提示，分别训练模型进行有效的答案转换和错误识别。这种设计实现了高效的 off-policy 数据生成，大幅降低长链采样的计算负担。

**结果**：在 LiveCodeBench 上，REVES 比 RL 基线高 +6.5 分，比标准多轮训练高 +4.0 分；在 circle packing 任务中使用 4B 最小模型和极少量 rollout 即达先前 SOTA；数学 ground-truth 验证下纠正能力显著提升；方法还泛化到 n_queens、mini_sudoku 等约束满足谜题。
