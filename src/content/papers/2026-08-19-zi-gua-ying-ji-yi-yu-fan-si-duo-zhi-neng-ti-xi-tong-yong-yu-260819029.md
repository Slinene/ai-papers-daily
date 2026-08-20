---
title: Adaptive Memory and Reflection Multi-Agent System for Medical Question Answering
title_zh: 自适应记忆与反思多智能体系统用于医学问答
authors:
- Pradeep Murugesan
- Luoxiao Yang
- Xueli Chen
- Xinqi Fan
arxiv_id: '2608.19029'
url: https://arxiv.org/abs/2608.19029
pdf_url: https://arxiv.org/pdf/2608.19029
published: '2026-08-19'
collected: '2026-08-20'
category: MultiAgent
direction: 多智能体协作与记忆反思机制
tags:
- Multi-Agent
- Memory
- Reflection
- Medical QA
- Adaptive Routing
- RAG
one_liner: 提出医学问答多智能体框架，通过智能体专属记忆、反思反馈与复杂度路由提升答案质量
practical_value: '- **复杂度评估与工作流路由**：电商/搜索推荐中可参考“复杂度评估器”，根据用户 query 或上下文难度，将任务路由到 solo、collaborative
  或 escalated 工作流——简单查询走轻量单智能体，复杂需求触发多智能体协作或人工升级，平衡效果与成本。

  - **智能体专属记忆与反思**：为不同智能体（如意图识别、商品召回、排序、文案生成）维护独立记忆和反思缓存，记录历史失败案例与反馈，让后续推理更少犯同类错误；这与用户长期偏好记忆类似，但更强调任务级错误纠正。

  - **共识与伦理监督模块**：在生成推荐理由、广告文案或客服回答时，引入多个智能体输出共识和合规审查，能减少事实性错误、品牌风险，尤其适用于医疗、金融等需要强监管的场景；电商大促文案也可以借鉴此类多角度审核。

  - **外部检索与记忆结合**：AMR 将外部 RAG 与历史对话/案例记忆有效结合，对电商问答或生成式推荐有借鉴意义——既要有实时商品知识检索，也要沉淀用户交互记忆与反思，提升生成稳定性和个性化。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：医学问答需要事实知识与复杂推理，现有系统多是单智能体架构或静态检索，缺乏适应性、持久记忆和结构化决策，难以从历史错误中学习并提升复杂病例的推理质量。

**方法关键点**：
- 构建 AMR 多智能体框架，每个专用智能体拥有独立记忆，并通过反思机制生成反馈，检索相关历史案例，改进后续推理。
- 引入复杂度评估模块，将输入问题路由到 solo、collaborative 或 escalated 工作流，按难度动态分配协作强度。
- 设计共识模块和伦理监督模块，对多智能体推理进行整合与输出审核，增强可靠性与合规性。
- 结合外部检索与智能体内部记忆，形成闭环学习。

**关键结果**：在 MedQA 和 MedMCQA 两个医学 QA 基准上，AMR 相比多个基线取得显著性能提升；消融实验表明，同时使用智能体特定记忆、反思和外部检索能带来最强表现，说明结构化记忆与反馈机制对提升可信医学智能体有重要作用。
