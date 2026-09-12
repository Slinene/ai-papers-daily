---
title: 'Explainability Assistant: A Conversational XAI Interface for Interpreting
  Energy Consumption Models'
title_zh: 可解释性助手：用于解读能耗模型的对话式XAI接口
authors:
- Rodion Krjutškov
- Eduard Barbu
- Nikos Sakkas
- Sofia Yfanti
affiliations:
- Nupp Software
- Institute of Computer Science, University of Tartu
- Apintech Ltd, POLIS-21 Group
- Department of Mechanical Engineering, Hellenic Mediterranean University
arxiv_id: '2609.11860'
url: https://arxiv.org/abs/2609.11860
pdf_url: https://arxiv.org/pdf/2609.11860
published: '2026-09-10'
collected: '2026-09-12'
category: Agent
direction: 对话式XAI · LLM Function Calling
tags:
- XAI
- LLM Function Calling
- Conversational AI
- Energy Forecasting
- Intent Parsing
one_liner: 用LLM function calling替代自定义语法，实现94%意图解析准确率的对话式可解释AI系统
practical_value: '- 用 LLM function calling 替代 custom grammar / 意图分类器做 NLU，意图解析准确率从
  76.8% 提到 94%；在做推荐系统诊断、模型解释、运维助手的对话式 Agent 时可直接复用，避免为每个意图维护固定语法。

  - 把 LIME、SHAP、反事实等解释能力封装成 function schema，让 LLM 在对话中动态选择工具，适合嵌入内部调试或面向业务人员的模型解释界面，减少对技术背景的依赖。

  - 评估方法可借鉴：邀请领域专家对比传统 dashboard 和对话式界面，既测任务完成一致性也测主观偏好；业务上线前用少量专家做可用性评估，比单纯离线指标更有说服力。

  - 该工作面向能源预测，推荐算法本身无直接迁移价值，主要贡献在对话式 XAI 的工具编排与交互层。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：复杂 ML 模型（如基于遗传编程的符号回归器）在能耗预测中难以解释，传统 XAI dashboard 技术门槛高且不支持动态、上下文相关的追问。此前对话式 XAI 如 TalkToModel 受限于自定义语法，意图解析准确率仅 76.8%。

**方法关键点**：Explainability Assistant 是开源对话式 XAI 系统，利用现代 LLM 的 function calling 能力，将解释功能（如 LIME、SHAP、反事实解释）封装为可调用函数，通过 schema 让 LLM 解析用户意图并动态调用工具，无需针对特定任务微调，可适应不同 ML 问题类型。

**关键结果数字**：意图解析准确率达到 94%，支持灵活自然语言交互；与能源领域专家对比传统 XAI dashboard 的评估显示，对话式界面在可用性上更优，任务完成准确性一致，所有专家均偏好对话式界面用于实际工作。
