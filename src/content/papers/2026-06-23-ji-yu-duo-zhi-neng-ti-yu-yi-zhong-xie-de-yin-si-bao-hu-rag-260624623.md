---
title: 'Privacy-Preserving RAG via Multi-Agent Semantic Rewriting: Achieving Confidentiality
  Without Compromising Contextual Fidelity'
title_zh: 基于多智能体语义重写的隐私保护RAG
authors:
- Yuanhe Zhao
- Tianyu Zhang
- Huafei Xing
- Derek F. Wong
- Jianbin Li
- Tao Fang
affiliations:
- North China Electric Power University
- University of Florida
- University of Macau
- Macau Millennium College
arxiv_id: '2606.24623'
url: https://arxiv.org/abs/2606.24623
pdf_url: https://arxiv.org/pdf/2606.24623
published: '2026-06-23'
collected: '2026-06-24'
category: MultiAgent
direction: 多Agent语义重写实现隐私保护RAG
tags:
- Privacy-Preserving
- Multi-Agent
- Semantic Rewriting
- RAG
- LLM
- Data Sanitization
one_liner: 通过多Agent协作语义重写去除检索内容中的隐私，将LLaMA-3-8B信息泄露从144例降至1例，且离线预处理无在线延迟
practical_value: '- 电商/推荐系统若用RAG检索含用户隐私的文档，可借鉴多Agent语义重写，在构建商品描述或用户画像时去除PII，平衡隐私与语义保真度。

  - 异步预处理模块的设计不影响在线服务延迟，适合集成到数据ETL管道中，对实时推荐系统友好。

  - 隐私提取-语义分析-重构的三Agent协作模式可复用到内容安全审核，多个代理协同检测并改写敏感信息。

  - 对生成式推荐模型，在生成item文案时可用类似方法防止模型泄露训练数据中的隐私信息。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：RAG引入外部知识增强了LLM，但检索内容可能包含敏感信息，恶意提示可导致隐私泄露。现有脱敏方法（如SAGE）难以兼顾隐私保护和语义保真度。
**方法**：提出多Agent框架，包含三个专门代理：隐私提取Agent识别敏感实体（姓名、电话等），语义分析Agent理解上下文含义，重构Agent生成语义等价但无隐私的文本。三个Agent协作进行语义重写，整个流程作为异步预处理模块离线完成，不增加在线推理延迟。
**结果**：在ChatDoctor和Wiki-PII数据集上，对6个LLM评估。面对目标攻击，LLaMA-3-8B的信息泄露实例从144个降至1个，大幅降低隐私风险；语义保真度方面，BLEU-1达到0.122，优于SAGE的0.117；且离线预处理保持零在线延迟。
