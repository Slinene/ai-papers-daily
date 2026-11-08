---
title: 'MedGraph: Maintaining Patient State with Graph Memory for Long-Term Medical
  Dialogue'
title_zh: MedGraph：用图记忆维护长程医疗对话中的患者状态
authors:
- Donghua Zhang
- Zizheng Wang
- Ze Dong
- Yiding Feng
- Siyu Qian
affiliations:
- University of Michigan
- Georgetown University
- Johns Hopkins University
- Harvard University
arxiv_id: '2611.08433'
url: https://arxiv.org/abs/2611.08433
pdf_url: https://arxiv.org/pdf/2611.08433
published: '2026-11-05'
collected: '2026-11-08'
category: Agent
direction: 长期对话记忆与状态追踪
tags:
- LLM Memory
- Graph Memory
- Long-term Dialogue
- State Tracking
- Fact Attribution
- Temporal Retrieval
one_liner: 构建带日期、归属与链式关系的图记忆，解决长程医疗对话中过期、混淆、缺安全事实三类错误，准确率提升10+点
practical_value: '- **时效状态管理**：电商导购/客服 Agent 可借鉴“带日期事实 + 链式更新”结构，对用户订单、优惠资格、偏好兴趣做多版本存储，提问时按时间点读取正确状态，避免过期推荐。

  - **事实归属区分**：多成员家庭账号或共享设备场景，构建记忆时显式标注事实所属用户，可防止 A 用户的行为被误检索给 B 用户，改善个性化推荐与对话安全性。

  - **检索单元升级**：以“用户实体的一组关联记录链”作为检索单位，比逐条相似度召回更连贯，适合需要完整历史上下文的客服问答、售后纠纷等长对话场景。

  - **安全事实常驻**：将用户的安全/风控相关属性（如过敏、黑名单、券禁用规则）独立成档案，每次生成回复前强制带出，降低营销推荐中的合规风险。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 医疗助手需要跨多次就诊维护患者状态，现有通用记忆系统（RAG、GraphRAG、Mem0 等）在长程医疗对话中常出错。论文分析五类基线，归纳出三类关键错误：检索证据包含过期状态、混入他人健康事实、遗漏回答所需的安全事实。

**方法关键点**：MedGraph 构建阶段从每轮会话中抽取带日期的事实，并显式归属到事实所描述的人；将药物、诊断、测量记录链接成链，保留早期状态演变。检索阶段以患者的整条链为排序单位，定位问题询问的时间点读取状态，同时补充原始对话文本；另设患者档案，每次提问时列出所有已记录的安全事实。

**关键结果**：在 MedMemoryBench 上，MedGraph 在 GPT 和 Qwen 两种骨干下整体准确率均为最高，分别比最强基线高 10.5 和 10.4 个百分点，且在 GPT 设置下记忆构建与回答效率可控。
