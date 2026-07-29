---
title: Localized Adaptation Reveals Distinct Learning Signatures in Transformers
title_zh: 局部适调揭示 Transformer 中不同学习目标的分层偏好
authors:
- Rebecca Ramnauth
- Brian Scassellati
affiliations:
- Yale University
arxiv_id: '2607.25663'
url: https://arxiv.org/abs/2607.25663
pdf_url: https://arxiv.org/pdf/2607.25663
published: '2026-07-28'
collected: '2026-07-29'
category: Training
direction: LoRA 层位置与学习特征适配
tags:
- LoRA
- layer localization
- transfer learning
- model adaptation
- transformer learning
one_liner: 不同层应用 LoRA 会形成各异的学习特征：词法绑定重早期层，事实关联偏后期层，行为策略学后期动作、中期门控
practical_value: '- **任务驱动的 LoRA 层选择**：若需让模型快速绑定新商品名、品牌词等（词法绑定），优先在早期层（1–6层）插入 LoRA，获取速度快且对无关上下文扰动小；若需更新商品属性、事实知识，则应在后期层（约20+层）适配，避免覆盖早期通用表示。

  - **对话/Agent 策略微调解耦**：行为策略学习（如导购话术、推词决策）中，行为的具体生成（action）适合在后期层适配，而策略控制（何时执行）适合在中间层适配，可分层挂载不同
  LoRA 模块，减少策略遗忘与干扰。

  - **因果与流程推理任务适配位置**：类似推理“用户搜索→点击→转化”的因果链或售后流程，在模型中、后期或全层适配效果更好，不建议只在单侧浅层或深层微调。

  - **避免灾难性迁移的基础原则**：当希望模型在新任务上泛化且不破坏原有能力时，可参考论文学到的“适应几何”：获取、迁移、边界性三者往往不可兼得，需按业务目标选择关键层位，如追求高迁移性能需考虑中层或全栈适配。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：Transformer 微调通常更新全层，但窄目标（如学一个新事实）可能波及无关能力。论文探究适应位置（层）如何影响模型学什么、迁移多好、保持多精确。

**方法**：构造涵盖五个目标（词法绑定、事实关联、行为策略学习、因果映射、流程推理）的受控基准，每个目标在早期、中期、后期层及全层分别施加 LoRA，测量获取（acquisition）、迁移（transfer）和边界性（boundedness），定义“适应几何”。在5个模型家族上重复实验，并控制参数量。

**关键结果**：不同目标表现出显著分层偏好：词法绑定在早期层获取快且边界清晰，但迁移需更广更新；事实关联在后期层适配效果最佳；行为学习呈现双阶段结构——后期层负责动作获取，中间层主司策略门控；因果与流程推理任务在中间层或全层适配下迁移最优。这些模式在参数匹配控制下稳健，且大部分方向性对比跨模型复现。
