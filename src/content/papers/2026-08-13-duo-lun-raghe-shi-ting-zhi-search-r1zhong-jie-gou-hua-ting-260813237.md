---
title: When Should Multi-Round RAG Stop? Structured Stopping Judgments and Retrieval
  Reduction in Search-R1
title_zh: 多轮RAG何时停止？Search-R1中结构化停止判断与检索削减
authors:
- Weimeng Luo
affiliations:
- Unaffiliated
arxiv_id: '2608.13237'
url: https://arxiv.org/abs/2608.13237
pdf_url: https://arxiv.org/pdf/2608.13237
published: '2026-08-13'
collected: '2026-08-16'
category: RAG
direction: 多轮RAG自适应停止策略
tags:
- RAG
- stopping policy
- Search-R1
- structured judge
- retrieval reduction
one_liner: 在冻结的Search-R1框架上训练S2G风格结构化judge，用第一STOP决策减少3.7%检索调用，EM仅降0.625个百分点
practical_value: '- **冻结主流程、只训停止judge**：在电商搜索/Agent的多轮RAG场景，可以保持线上reasoner、retriever、prompt不动，只在小模型judge上做结构化停止判断，降低切换风险。

  - **用“充分性+缺口”双标签替代二分类**：让judge同时预测当前证据是否足够、缺失信息是什么，能提供更可解释的停止信号，后续可直接用缺口引导下一轮query改写或检索。

  - **把序列决策当成first STOP选择问题**：部署时轨迹由第一个STOP决定，因此评估时应按整条轨迹的最终效果而非单状态分类准确率来选阈值，建议用grouped
  validation避免同题多状态之间的泄漏。

  - **注意成本口径**：论文明确即使检索次数减少，judge推理也可能增加总耗时；业务上要单独核算端到端latency/cost，不能只报检索调用下降。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：多轮RAG需要在证据累积中决定何时停止，过度检索会增加延迟和上下文噪声，过早停止则导致答案无依据。现有停止策略多将单状态视为独立分类，忽略部署时由第一个STOP决定整条轨迹的序列选择特性。

**方法关键点**：作者在冻结的Search-R1流水线上适配S2G-RAG的结构化“充分性-缺口”判断，训练一个Qwen3.5-2B judge。训练数据来自900个不重叠HotpotQA问题的3,009个状态，Search-R1的reasoner、retriever、corpus、prompt和检索预算均不变。judge checkpoint和停止阈值在grouped validation上选择，之后冻结进行确认性评估。

**关键结果数字**：在确认测试集上，该策略相对原生Search-R1减少77次检索调用（3.70%），Official Exact Match仅下降0.625个百分点，说明结构化judge能在基本保持答案准确率的同时降低检索量。作者同时指出，这并不意味着准确率不变或提升、安全停止，也不代表总推理成本降低。
