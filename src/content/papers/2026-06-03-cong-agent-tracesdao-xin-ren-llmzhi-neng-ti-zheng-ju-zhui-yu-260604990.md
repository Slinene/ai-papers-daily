---
title: 'From Agent Traces to Trust: Evidence Tracing and Execution Provenance in LLM
  Agents'
title_zh: 从Agent Traces到信任：LLM智能体证据追踪与执行溯源综述
authors:
- Yiqi Wang
- Jiaqi Zhang
- Taotao Cai
- Zirui Liu
- Qingqiang Sun
- Zequn Sun
- Zhangkai Wu
- Mingkai Zhang
- Yanming Zhu
affiliations:
- Griffith University
- Jiangsu University
- University of Southern Queensland
- Peking University
- Great Bay University
arxiv_id: '2606.04990'
url: https://arxiv.org/abs/2606.04990
pdf_url: https://arxiv.org/pdf/2606.04990
published: '2026-06-03'
collected: '2026-06-04'
category: Agent
direction: LLM 智能体证据追踪与执行溯源
tags:
- Evidence Tracing
- Execution Provenance
- LLM Agents
- Trustworthy AI
- Agent Observability
- Survey
one_liner: 提出LLM智能体证据追踪与执行溯源统一分类框架，连接检索、工具、记忆与通信，支撑调试、安全与审计。
practical_value: '- 在构建电商智能体（如客服、推荐Agent）时，应记录完整的执行轨迹（检索、工具调用、记忆操作）并构建溯源图，用于调试和审计。

  - 采用证据支持关系（SUPPORT, CONTRADICT）来验证生成的推荐理由是否基于实际检索证据，减少幻觉。

  - 实施运行时防护：对工具调用参数进行来源追踪，防止注入攻击或不安全操作。

  - 利用记忆溯源（memory provenance）确保个性化推荐不会因过时或偏差的记忆而输出不一致内容。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM智能体通过检索、工具调用、记忆、环境交互与多智能体协作完成复杂任务，其行为越来越难以验证、调试和审计。仅凭最终答案的准确性无法解释产出依赖的证据链、工具调用是否正当、记忆是否过时、失败根因在哪。这形成了“过程级问责缺口”，因此需要系统化的证据追踪与执行溯源机制，将异构执行产物（检索文档、工具输出、记忆条目、环境观测、中间声明、智能体消息）连接为可解释的信任层。

### 方法关键点
本文提出一个五维分类法统一LLM智能体的溯源问题：
- **追踪源**：推理、检索、工具使用、记忆、环境、多智能体通信。
- **证据与执行单元**：语义证据（文档、声明、观测）与过程步骤（工具调用、参数、行动）。
- **溯源关系**：定义七种关系类型（SUPPORT, DERIVE, DEPEND-ON, CONTRADICT, INVALIDATE, TRIGGER, UPDATE），将原始轨迹转化为结构化溯源图。
- **追踪粒度和时机**：从运行级到声明/参数级；可用于预执行检查、运行时拦截、事后分析或持续追踪。
- **信任功能**：支撑验证、归因、调试、安全实施、审计和恢复。

### 关键结果
本文是综述，无新实验；但系统梳理了现有基准与评估方法（如ALCE、FActScore、RAGAS、ToolEmu、AgentDojo、τ-bench等），指出当前评估多停留在最终答案正确性，需向**过程级问责**迁移，例如检查声明级别的证据支持度、工具调用安全性、记忆污染链路等。

> 最值得记住的一句话：LLM智能体的信任不应仅来自最终答案的正确，更应来自可追溯、可验证、可审计的执行过程——证据链比答案本身更重要。
