---
title: 'Reasoning over Non-Parametric Memory in Multilingual LLMs: A Cognitive-Based
  Analysis of Relational Knowledge'
title_zh: 多语言LLM中非参数记忆上的关系推理：基于认知的分析
authors:
- Zohreh Abbasi Liasi
- Batoul Hammoud
- Anas Madkoor
- Ehsaneddin Asgari
affiliations:
- Qatar Computing Research Institute (QCRI), Hamad Bin Khalifa University
- Universitat Pompeu Fabra
arxiv_id: '2611.06715'
url: https://arxiv.org/abs/2611.06715
pdf_url: https://arxiv.org/pdf/2611.06715
published: '2026-11-04'
collected: '2026-11-05'
category: Eval
direction: RAG推理评估 · 跨语言诊断基准
tags:
- RAG
- relational reasoning
- multilingual
- evaluation
- LLM
- counterfactual
one_liner: 构建多语言关系推理诊断基准，发现模型从Apply到Analyze准确率骤降且Evaluate仍是瓶颈
practical_value: '- 在电商 RAG、商品知识问答或推荐解释生成中，不要默认 LLM 能对 context 中的关系做复杂推理；尤其涉及“分析/评价”层级的任务，可以将
  prompt 拆解为多个“应用”级别子任务，或显式约束推理步骤。

  - 构建内部 LLM 评估集时，可借鉴 Bloom 分层（Remember/Apply/Analyze/Evaluate）监控模型在不同认知层次上的表现，而不是只看总体准确率；这能帮助定位线上知识库问答失败的具体层级。

  - Counterfactual 场景（如“如果把价格翻倍用户会怎样选择”）更难，建议在 prompt 中加入 few-shot 或对输出进行额外校验；去除实体名称/匿名化有时能提升高阶推理，可在涉及商品
  ID 推理或去偏场景中尝试。

  - 跨语言难度排名一致意味着在多语言电商助手中，某语言上发现的困难关系或 item 可能在其他语言同样困难，可以共用 hard case 集进行针对性优化。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：RAG 假设 LLM 能对上下文中提供的关系进行推理，而不是仅依赖预训练记忆。本文在隔离环境中检验这一假设，将事实直接放入 prompt 而非检索。

**方法**：构建 REL-Bloom——多语言诊断基准，包含 450 道多选题，基于 30 个 Wikidata 关系；同一关系在五级 Bloom 层级（Remember、Understand、Apply、Analyze、Evaluate）实例化，并覆盖三种真实性条件（Factual、Counterfactual、Neutralized）。评估 43 个模型、6 种语言、两种多语言设置，共 226,800 个预测。

**关键结果**：① 所有开源模型系列从 Apply 到 Analyze 准确率急剧下降，Large Granite bucket 降幅达 47.2 个百分点，但 Gemini 模型未出现该现象；② Evaluate 仍是瓶颈：Gemini 3.1 Pro 在其他四级平均 99.5%，Evaluate 仅 60.7%；③ 项目与关系级难度排名跨语言一致，说明难度结构部分跨语言共享。此外，Counterfactual 条件通常比 Factual 更难，而去掉实体身份在某些模型机制下能改善高阶表现。结论：模型能力提升并不自动保证对给定关系证据的可靠推理。
