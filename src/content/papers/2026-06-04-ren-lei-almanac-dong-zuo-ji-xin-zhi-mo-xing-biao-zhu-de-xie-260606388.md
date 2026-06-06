---
title: 'Humans'' ALMANAC: A Human Collaboration Dataset of Action-Level Mental Model
  Annotations for Agent Collaboration'
title_zh: 人类ALMANAC：动作级心智模型标注的协作数据集
authors:
- Jiaju Chen
- Yuxuan Lu
- Jiayi Su
- Chaoran Chen
- Songlin Xiao
- Zheng Zhang
- Yun Wang
- Yunyao Li
- Jian Zhao
- Tongshuang Wu
affiliations:
- Northeastern University
- University of Notre Dame
- Adobe
- Microsoft
- University of Waterloo
arxiv_id: '2606.06388'
url: https://arxiv.org/abs/2606.06388
pdf_url: https://arxiv.org/pdf/2606.06388
published: '2026-06-04'
collected: '2026-06-06'
category: Agent
direction: Agent协作心智模型评估数据集
tags:
- mental model
- human-agent collaboration
- dataset
- action annotation
- LLM evaluation
one_liner: 构建ALMANAC数据集，以动作级心智模型标注评估LLM模拟人类协作行为的能力
practical_value: '- 在电商多Agent客服/导购系统中，可借鉴Map Task范式收集协作对话，并显式标注自我意图、感知对方意图、团队目标，用于训练Agent的协作对齐。

  - 动作级的心智模型标注方法可迁移到生成式推荐对话评估，衡量推荐Agent对用户实时意图和长期兴趣的推理能力。

  - 利用ALMANAC或类似数据对LLM进行微调，提升Agent在多轮协作中主动推测伙伴意图、调整策略的能力，避免机械式回复。

  - 工程AB测试可参考该数据集构建评估指标（如心智模型预测准确率），量化Agent的协作智能。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有LLM Agent主要优化任务完成，缺乏协作过程中持续对齐心智模型的能力，社区缺少带动作级心智模型标注的真实人类协作数据，难以引导Agent发展协作智能。
**方法**：基于社会科学经典Map Task（双人路径指引任务），收集了覆盖2987个协作动作的数据集ALMANAC。每个动作均配有心智模型标注，包括参与者的自我推理、对伙伴意图的感知、对团队目标的感知，并提供自由文本解释。
**结果**：在预测人类下一步行为与心智模型的任务上，对6个LLM进行基准测试，证明ALMANAC能有效评估模型模拟人类协作行为及推断潜在心智模型的能力。
