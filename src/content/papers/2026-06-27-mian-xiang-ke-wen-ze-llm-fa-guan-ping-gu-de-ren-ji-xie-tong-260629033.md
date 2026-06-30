---
title: Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations
title_zh: 面向可问责 LLM 法官评估的人机协同金块标注
authors:
- Laura Dietz
affiliations:
- University of New Hampshire
arxiv_id: '2606.29033'
url: https://arxiv.org/abs/2606.29033
pdf_url: https://arxiv.org/pdf/2606.29033
published: '2026-06-27'
collected: '2026-06-30'
category: Eval
direction: 人机协同评估 · 锚定偏差消除
tags:
- Nugget Annotation
- LLM-as-a-Judge
- Human-in-the-Loop
- Evaluation
- Accountability
- Anchoring Bias
one_liner: 提出人定义信息金块、LLM 匹配系统输出的分工，消除评估锚定偏差并保持人类监督
practical_value: '- **构建领域信息点库（Nugget Bank）**：在电商搜索、推荐或Agent评估中，先由业务专家定义每条查询/任务应覆盖的关键信息点（如商品属性、政策限制），LLM自动匹配输出是否覆盖这些点，实现低成本可复用的自动评分。

  - **消解锚定偏差的标注流程**：通常人工评估时若先看到机器输出，容易盲目同意（橡皮图章）。借鉴本文，人工先独立标注信息需求（金块），之后再看系统输出或让LLM做匹配，保护人类判断独立性。

  - **高方差任务的人机分工**：推荐解释、Agent决策理由等开放式输出，人类直接打分一致性低。改用“金块”原子化评估维度，让LLM承担细粒度匹配，人类只需定义标准，提升评估稳定性。

  - **自动评分结合人工监督**：金块库经专家审核后，可持久化用于线上评估，结合自动匹配形成半自动评估流水线，兼顾问责与效率。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 评判 LLM 存在循环偏差，人工校验 AI 提案因先看到机器答案而诱发锚定偏差（橡皮图章效应），纯人工测试集则昂贵且标注一致性低。需要一种既保留真正人类监督又降低主观方差和高成本的评估方式。

**方法关键点**：提出三阶段人机协同标注流程。首先，人类标注员独立定义信息“金块”（nuggets）——系统输出理应包含的关键信息片段，形成金块库；其次，LLM 自动将金块与待评估的系统输出做语义匹配，判断每个金块是否被覆盖；最后，基于覆盖度计算自动化评分。关键设计在于：人类只负责定义“什么信息重要”，而 LLM 负责高体积的匹配工作，各展所长，同时消除人类在看到系统输出后才打分时的锚定效应。工具支持金块库导出，可与自动评判器集成。

**结果**：原型标注工具已在 https://trec-auto-ju 上线演示，该流程避免了循环锚定，并提供了可问责的评估基础。未报告量化指标，主要贡献在流程设计和工程实践。
