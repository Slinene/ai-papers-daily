---
title: 'AGORA: An Archive-Grounded Benchmark for Agentic Workplace Document Reasoning'
title_zh: 面向智能体工作文档推理的档案基准 AGORA
authors:
- Honglin Guo
- Qi Zhang
- Yu Zhang
- Weijie Li
- Rui Zheng
- Zhikai Lei
- Qiyuan Peng
- Zhiheng Xi
- Tao Gui
- Qi Zhang
affiliations:
- Fudan University
- Zhejiang University
- Shanghai Qiji Zhifeng Co., Ltd.
arxiv_id: '2606.24526'
url: https://arxiv.org/abs/2606.24526
pdf_url: https://arxiv.org/pdf/2606.24526
published: '2026-06-22'
collected: '2026-06-25'
category: Eval
direction: Agent 文档探索推理评测
tags:
- Agent
- Document Reasoning
- Benchmark
- LLM
- Retrieval
- Workplace AI
one_liner: 构建跨域大规模真实档案基准，要求智能体在超长上下文中主动探索检索证据，最强模型仅达59.4%准确率
practical_value: '- **多步探索范式**：在电商商品库、政策库等超大规模非结构化文档上构建问答任务时，借鉴其 agent 多轮检索、证据定位与交叉验证的流水线设计，而非依赖一次性长上下文扫描。

  - **防泄漏基准构建**：采用跨文档任务合成、实体混淆与难度过滤构造评测集，可迁移到内部 agent 离线评估，防止模型记忆导致分数虚高。

  - **跨域鲁棒性检验**：覆盖农业、金融、法律等 8 个域，提示推荐/搜索系统若接入 agent 需在多个业务域分别评测，避免单域过拟合。

  - **上下文窗口超限场景**：当文档总量远超模型窗口时，强制 agent 主动探索与选择性检索，为电商导购、客服 agent 在长尾商品/长文档下的策略设计提供参考。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 越来越多被部署为 agent 处理企业内部文档，但现有基准未能同时强调档案通达性（archive-groundedness）、智能体探索行为（agentic exploration）和跨域覆盖，导致难以评估真实工作场景中的长文档推理能力。

**方法关键点**：
- 提出 AGORA 基准，包含 8 个领域（农业、建筑、商业、教育、金融、医疗、法律、科技）的 9,664 份真实文档，总计 372M tokens，远超任何模型的上下文窗口，迫使 agent 通过多轮检索逐步定位证据。
- 采用 agentic 流水线构造任务：跨文档问题合成保证信息分散在多份文件中；实体与数字混淆防止数据泄漏；难度过滤筛出需深度推理的题目。
- 评估 8 个主流 LLM，覆盖闭源与开源模型，要求 agent 在给定文档集合中自行探索并回答事实性问题。

**关键结果**：
- 整体准确率最高仅为 59.39%（Gemini-3.1-Pro），且不同领域差异显著（金融 31% vs 医疗 11% 等），表明任务远未解决。
- 较小模型（如 Qwen3.5-9B）准确率低至 3.04%，显示单纯缩放参数无法弥补主动探索能力的不足。
- 泄漏防护有效：经混淆后模型无法通过记忆回答，真实反映检索与推理能力。
