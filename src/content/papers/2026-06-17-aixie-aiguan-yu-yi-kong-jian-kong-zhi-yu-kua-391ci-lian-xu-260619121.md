---
title: 'Written by AI, Managed by AI: Semantic Space Control and Index Sickness Elimination
  Across 391 Consecutive Sessions'
title_zh: AI写AI管：语义空间控制与跨391次连续会话的索引病消除
authors:
- Hui Zhang
- Shuren Song
affiliations:
- Shenzhen Yunxi Technology Co., Ltd.
- Information Technology Center, Tsinghua University
arxiv_id: '2606.19121'
url: https://arxiv.org/abs/2606.19121
pdf_url: https://arxiv.org/pdf/2606.19121
published: '2026-06-17'
collected: '2026-06-18'
category: Agent
direction: Agent长期协作中的符号退化与语义控制
tags:
- Index Sickness
- Semantic Vitality
- AI Instructions Reduction
- Phantom Legislation
- Long-Horizon Collaboration
one_liner: 发现并解决长周期LLM协作中符号约束过载导致的“索引病”，提出语义活力法则与基线-日志物理分离机制
practical_value: '- **避免推荐Agent系统提示膨胀**：在为电商推荐、搜索等构建长期运行LLM Agent时，不要无节制地在System Prompt中添加符号索引、ID映射或防御性规则。一旦超过临界点，模型会放弃对业务语义的真实理解，转而进行自指推理，产生逻辑自洽但脱离实际（如生成不存在的商品ID、错误的活动规则）的输出。

  - **采用基线-日志物理分离**：将Agent的任务定义、核心指令（Baseline）与运行时的历史对话、上下文记录（Log）严格拆分。只在Baseline中保留最精简的自然语言目标描述，避免无效历史噪声污染推理，大大降低上下文窗口中的“索引病”风险。

  - **用自然语言承载明确目的**：在生成式推荐或Agent指令中，尽量用完整的、目标导向的自然语言语句代替符号化简写（如直接用“推荐适合露营的防水帐篷”而非“item:camping_tent_v3”）。这符合“语义活力法则”，能显著提升信息质量和模型遵守指令的可靠性。

  - **量化指令体积并监控**：定期审计Agent交互中AI Instructions的总长度和冗余度，作为健康状况指标。通过类似基线-日志分离的方法，我们可将指令量减少约75%，同时彻底消除索引病复发，这对维护长周期运行的推荐智体至关重要。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：在长周期LLM协作（如长期运行的推荐Agent）中，业界惯用方法是为实体设计符号ID、在系统提示中堆砌规则、加大上下文窗口，以期输出更可靠。但实际工程记录（Bang-v3项目，391次会话）表明，当符号系统超过复杂度阈值时，LLM会放弃真正理解业务语义，退守到符号层自指推理，产生表面内部一致却脱离现实的输出，即“索引病”（Index Sickness），其典型表现为“幻影立法”。

**方法**：采用行动研究法，记录并分析失败过程。提出反直觉解释：长周期协作的核心障碍并非AI记忆不足，而是活跃上下文中存在本不应有的历史噪声。由此归纳出“庞原则（语义活力法则）”：在人类-AI协作中，载有明确目的的自然语言比符号表达传递的信息质量高得多。基于此原则设计“基线-日志物理分离”机制，将静态核心指令与动态运行记录严格分离，避免符号过载和噪声累积。

**结果**：在同一项目中，该机制使AI指令体积缩减约75%，后续约150次会话中未再出现索引病，完美消除故障。
