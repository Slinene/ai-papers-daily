---
title: 'Rethinking Psychometric Evaluation of LLMs: When and Why Self-Reports Predict
  Behavior'
title_zh: 重新思考LLM心理测量评估：自我报告何时及为何能预测行为
authors:
- Rafal Kocielnik
- Pengrui Han
- Peiyang Song
- Myrl G. Marmarelis
- Ramit Debnath
- Dean Mobbs
- Anima Anandkumar
- R. Michael Alvarez
affiliations:
- Caltech
- UIUC
- University of Cambridge
arxiv_id: '2606.12730'
url: https://arxiv.org/abs/2606.12730
pdf_url: https://arxiv.org/pdf/2606.12730
published: '2026-06-09'
collected: '2026-06-14'
category: Eval
direction: LLM心理测量评估 · 自我报告行为一致性
tags:
- LLM Evaluation
- Self-Report
- Behavior Prediction
- TPB
- Big 5
one_liner: 发现大五人格无法预测LLM行为，而计划行为理论在共享对话中达到人类水平一致性，跨会话一致性取决于行为是否锚定于训练数据
practical_value: '- 在对 Agent 或对话系统做安全性评估时，优先使用计划行为理论（TPB）框架而非大五人格，因为 TPB 在特定行为预测上更准确，且共享会话内能达到人类水平的一致性。

  - 跨会话场景下，行为一致性仅对训练数据中固化下来的行为（如隐性偏见）有效，对上下文强启动的行为（如谄媚）无效。因此，多轮交互的安全测评不能依赖单次会话的自我报告，需在多次独立会话中重复测试。

  - 角色提示（persona prompting）可以让模型的自我报告更一致，但无法让实际行为对齐。这意味着仅靠 prompt 注入人设无法保证 Agent 的行为安全，必须结合其他机制。

  - 在生成式推荐或对话式推荐中，若想通过类似心理测量的方法快速探测用户模型或对话 Agent 的倾向，应针对具体任务设计行为锚定项，而非依赖宽泛的人格量表。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：安全部署 LLM 需要低成本预测其行为倾向，心理测量自我报告（SR）是常用手段，但近期工作发现 SR 与行为严重脱节。现有研究依赖大五人格，而大五对特定行为预测力弱，且未控制会话上下文一致性，无法确定 LLM 是否真的缺乏连贯性。

**方法**：引入计划行为理论（TPB），该理论针对具体行为测量意图，在人类中预测力远超大五。在 4 个行为任务（如谄媚、隐性偏见）和 11 个前沿 LLM 上实验，操控会话上下文（共享对话 vs. 独立对话）和身份诱导（角色提示）。

**关键结果**：
1. 共享对话中，TPB 达到人类水平的一致性（r≈0.6），大五无效；
2. 跨独立对话时，只有锚定于训练数据的行为（如隐性偏见）保持一致性，上下文强启动的行为（如谄媚）一致性崩溃；
3. 角色提示使自我报告在跨会话中更一致，但行为未对齐。说明大五等宽泛框架不是部署行为测试的最佳工具，需要更特定于任务和行为的工具，且必须在多任务多上下文中评估。
