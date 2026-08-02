---
title: 'LEDGERMIND: Provenance-Constrained Multimodal Agentic Reasoning with a Structured
  Evidence Ledger'
title_zh: LEDGERMIND：基于结构化证据账本的溯源约束多模态智能推理
authors:
- Enjun Du
- Hange Zhou
- Chenxu Du
- Siyi Liu
- Zirong Chen
- Ziyu Zheng
- Yongqi Zhang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- The University of Hong Kong
- Tsinghua University
- University of Sussex
arxiv_id: '2607.28374'
url: https://arxiv.org/abs/2607.28374
pdf_url: https://arxiv.org/pdf/2607.28374
published: '2026-07-29'
collected: '2026-08-02'
category: Agent
direction: 溯源约束的多模态Agent推理框架
tags:
- Multimodal Agent
- Provenance
- Structured Evidence Ledger
- Grounding
- Verification-and-Repair
- Visual Question Answering
one_liner: 将多模态Agent轨迹构建为溯源约束状态机，用结构化证据账本限制推理，提升准确性与轨迹忠实度
practical_value: '- 在电商商品问答或推荐解释等场景中，可借鉴**结构化证据账本**约束Agent的推理链：要求每条中间论断必须引用来自工具调用（如商品数据库、图像识别）的确定证据，防止产生“幻象接地”式的错误推荐理由。

  - **自适应双路分发器**根据查询复杂度动态选择推理深度，可迁移至搜索/推荐系统中的多模态查询处理：简单意图走轻量路径，避免过度调用昂贵模型，兼顾效率与准确性。

  - **事件触发验证与修复引擎**可应用于实时纠错：当监测到推理过程中的证据不一致时，仅允许基于已有账本条目的修复操作，杜绝凭空捏造信息，保障推荐理由的事后可审计性。

  - **三层接地协议**（实体级、数值级等校验）可直接用于商品属性抽取与校验，确保生成的商品描述或推荐文案中实体名称、数值参数等与原始多模态信息严格一致，降低事实性错误。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：多模态Agent在视觉问答中依赖多步推理，但现有评估只聚焦最终答案正确性，掩盖了推理过程中的典型故障：无证据支撑的中间推理、引用幻觉实体的“幻象接地”、简单查询过度推理、修复时引入超出原始证据的内容。  
**方法**：提出将Agent轨迹视为溯源约束状态机，核心是**结构化证据账本**。工具输出被归一化存入账本，后续推理只能引用活跃账本条；引入三层接地协议在实体与数值层面校验；修复被定义为受约束的状态转换，禁止引入未经工具产生的内容，具备形式化的非放大保证。整套系统包含自适应双路分发器（根据问题复杂度选择推理深度）和事件触发验证修复引擎。  
**结果**：在多个多模态推理基准和不同规模的多模态大模型上，LedgerMind不仅提升答案准确率，更显著改善轨迹层面的忠实度，有效抑制了四类被最终准确率掩盖的故障模式。
