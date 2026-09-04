---
title: 'Knowing When Not to Reuse: Conditional Experience Transfer in Autonomous LLM
  Post-Training'
title_zh: 知何时不复用：自主 LLM 后训练中的条件经验迁移
authors:
- Tingyun Li
- Wenfeng Feng
- Weiqing Li
- Abudukelimu Wuerkaixi
- Guohua Liu
- Yuewei Zhang
affiliations:
- Alibaba Cloud Computing
arxiv_id: '2608.26730'
url: https://arxiv.org/abs/2608.26730
pdf_url: https://arxiv.org/pdf/2608.26730
published: '2026-08-26'
collected: '2026-09-04'
category: Training
direction: 自主 LLM 后训练经验迁移控制
tags:
- Autonomous Post-Training
- Experience Transfer
- LLM Adaptation
- Training Efficiency
- Continual Learning
one_liner: 提出 BCIT 方法，在自主 LLM 后训练中只授权可迁移的历史更新，减少有害复用并提升同预算下最终模型质量
practical_value: '- 持续训练或自动更新线上模型时，不要将历史训练更新（数据配比、超参、LoRA 模块）视为无条件成功经验；应记录父模型版本、数据分布、训练阶段，并将每次效果与其来源上下文绑定。

  - 在正式改变权重或晋升模型前，先做有界小规模训练试验，验证候选更新在当前父模型状态下是否仍然有效，避免错误更新进入线上后污染后续训练轨迹。

  - 对已知硬冲突（如数据源、工具 schema、任务定义变化）建立命名规则，在候选生成阶段直接否决，节省算力并降低风险；所有候选共享统一采纳门槛，只有真实观察事件才进入经验记忆。

  - 对 Agent 自动迭代工具调用、prompt 更新或模型微调的场景，可借鉴“条件经验复用”思路：经验不是越多越好，关键是在当前上下文中可行动。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 需要反复后训练适应新领域、工具和需求，自主系统自动提议、训练、评估更新并积累历史证据。但历史更新是否仍适用于当前父模型存在不确定性：更新效果依赖父模型、数据配比和训练阶段。无上下文地复用过去成功会浪费算力，若错误晋升子模型，还可能降低后续训练轨迹质量。

**方法关键点**：将问题形式化为条件经验迁移（conditional experience transfer），提出 BCIT。BCIT 将观察效果绑定到源上下文，检查适用条件，对命名硬冲突直接否决，必要时通过有界训练试验获取当前状态证据。完全训练的候选仍遵循统一采纳规则，仅观察到的事件扩展记忆。

**关键结果**：在 4B 模型跨金融推理、text-to-SQL、function calling 的自适应中，候选更新在目标效果与保留效果上表现异质。在匹配候选、证据和算力约束下，BCIT 授权更少有害更新，并取得更高的等预算最终模型质量，支持将经验授权作为自主后训练中的独立问题。
