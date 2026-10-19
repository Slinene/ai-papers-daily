---
title: 'Dream2Discern: Learning from Hard Latent Variants for Runtime Failure Prediction
  in Multi-Agent Systems'
title_zh: Dream2Discern：从困难潜在变体学习多智能体系统运行时失败预测
authors:
- Boxuan Zhang
- jianing Zhu
- Xiaotian Han
- Ruixiang Tang
affiliations:
- Rutgers University
- The University of Texas at Austin
arxiv_id: '2610.16071'
url: https://arxiv.org/abs/2610.16071
pdf_url: https://arxiv.org/pdf/2610.16071
published: '2026-10-11'
collected: '2026-10-19'
category: MultiAgent
direction: 多智能体系统 · 运行时审计
tags:
- Runtime Failure Prediction
- Multi-Agent Systems
- Latent Augmentation
- LLM Auditor
- Representation Perturbation
one_liner: 用自预测损失引导的隐式增广，把有限轨迹语料变成可再生难例源，提升多智能体失败审计
practical_value: '- 在电商/广告的 Agent 流水线（如购物助手、广告投放 Agent、搜索多工具调用）中，可训练轻量运行时审计器，只从执行前缀预测最终失败概率；达到阈值时提前终止或降级为规则/检索/人工确认，减少高风险工具调用和外部系统误操作。

  - 数据受限场景可借鉴 Dream 阶段的隐式增广：不采集新轨迹，而是对审计器表示算子做可学习扰动，构造让当前模型预测损失增大的 latent variants，再按原始标签训练。这种方式类似
  hard negative mining，但发生在隐蔽空间，适合轨迹/会话/行为序列标注昂贵的问题。

  - 注意审计器的 ''表征算子'' 选择与扰动强度需要平衡：过大扰动会引入噪声，过小则难例不足；可参考其按预测损失反馈、随训练迭代重新生成 variants 的做法，把有限样本做成可持续更新的难例池。

  - 评估不要只看最终准确率，应引入 trajectory-level weighted accuracy 和预测及时性指标；对在线系统更有意义，能帮助选择既能早停又不误杀正常任务的审计阈值。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM 驱动的多智能体系统在开放环境中容易产生推理和工具调用错误，部署时需要运行时审计器从已观察的执行前缀预测最终任务失败风险。但可用轨迹及其结果标签数量有限，扩展语料需要额外执行与验证，成本高且没有明确标准选择当前审计器难以分类的前缀。

方法关键点：Dream2Discern 让审计器用自身预测损失引导隐式增广。Dream 阶段，对审计器的表征算子选择扰动，使已有轨迹前缀的预测损失增大，得到 hard latent variants；Discern 阶段，审计器从这些变体中按原始标签学习预测执行结果。变体随审计器学习不断重新生成，因此有限语料变成可再生的困难样本来源，不需要额外轨迹收集或结果验证。

关键结果：在 AFTraj-2K 和 StepShield 上全面优于对比的失败审计器，两个基准的 trajectory-level weighted accuracy 均超过 90%，并且在预测准确性与及时性之间取得平衡。
