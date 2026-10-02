---
title: 'Mem++: Non-Destructive Memory for Long-Term Organizational LLM Agents'
title_zh: Mem++：面向组织 LLM Agent 的非破坏性长期记忆
authors:
- Ahmad Yehia
- Aly O. Abdelkareem
- Islam Ahmed
- Hesham Omran
- Khaled Alashmouny
- Christian Claudel
- Abduallah Mohamed
affiliations:
- The University of Texas at Austin
- AIDAChip Inc.
arxiv_id: '2610.02002'
url: https://arxiv.org/abs/2610.02002
pdf_url: https://arxiv.org/pdf/2610.02002
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: LLM Agent 长期组织记忆 · 读时检索
tags:
- LLM Memory
- Non-Destructive
- Retrieval Fusion
- Temporal Reasoning
- Organizational Agents
- RAG
one_liner: Mem++ 用整文档存储与读时时间过滤+多路检索融合，替代写时蒸馏，在组织记忆基准上大幅领先
practical_value: '- 在电商/广告规则、商品属性、政策文档等需要追溯“某时间点有效版本”的场景，不要写时蒸馏成事实或图谱，保留原始文档并按日期/作者索引，读时按
  as-of 时间过滤检索。这样能回答“当时规则是什么”“谁改的”“从哪个版本改成哪个版本”等问题，避免旧版本被覆盖后无法回答。

  - 多路检索融合策略可直接复用：lexical（精确 ID/术语）+ semantic（嵌入相似）+ tag（作者/店铺/品类）加权 RRF 融合，并保留 top
  k-3 融合结果 + 3 个最新日期匹配记录（recency reserve）。在商品搜索、客服知识库、推荐理由生成中能兼顾精确匹配与语义泛化，同时保证时效性。

  - 写时零 LLM 调用，只做 embedding 和索引，读时才做选择。对海量商品/文档更新场景，可大幅降低写入延迟和费用；消融显示实体图谱、事实抽取、consolidation
  在多个基准上增益有限甚至为负，可优先采用更简单的纯检索方案。

  - 多作者冲突版本不删除、由答案模型读时判断，适合多客服、多团队知识库，避免一个模型在写入时错误地覆盖或合并关键信息，保持溯源能力。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
组织记忆与单人会话记忆不同：多位作者独立撰写文档，决策变更以新文档形式出现，旧文档不被删除。现有记忆系统通常在写时压缩为事实、笔记或图谱，导致可回答的问题在提问前就被固定。RAG 保留原始文本但切块丢失版本关系，无法分辨“哪个版本当时有效”。因此需要一种非破坏性记忆，将选择推迟到读时。

**方法关键点**  
- **整文档存储**：每篇文档作为一个 row，保存全文 x、作者 a、事件日期 t、嵌入 e、状态 σ；只增不改不删，旧版本保留可检索。  
- **写时无生成模型**：仅做 embedding 和索引，文档超过编码器长度只截断嵌入，原文全文保留。  
- **三路索引**：lexical 全文匹配、tag 作者标签、vector 语义相似；读时先用可选 as-of 日期 θ 过滤 Sθ = {active 且 t_r ≤ θ}，保证只检索当时有效的记录。  
- **加权 RRF 融合**：三条路径按排名融合，权重 w_lex=1, w_tag=1, w_vec=4（或 2）；前 k-3 个按融合分数，后 3 个留给最新日期的匹配记录（recency reserve），兼顾准确与时新。  
- **可选扩展**：consolidation 用 LLM 分组近重复文档并标记 superseded；Memg++ 增加实体图谱；主实验均关闭，消融证明这些额外成本收益有限。  

**关键实验与结果**  
- **OrgMemBench**（组织记忆基准，443 篇文档，73 题）：使用 gpt-4.1-mini 时 Mem++ 总分 57.6，超过最强基线 RAG 2.6 分、超过最佳记忆系统 A-Mem 13.1 分；使用 gpt-4o-mini 时总分 44.2，超过 Zep 8.0 分。在 Supersession 和 Audit Replay 类别大幅领先。  
- **LoCoMo**：平均 LLM-judge 得分最高，gpt-4.1-mini 下 81.5，超 Nemori 2.1 分。  
- **LongMemEval S**：排名第二（72.2/74.7），仅次于 Memg++ 的 72.4/75.3，但 Memg++ 额外成本高。  
- **消融**：去掉 vector 路径在 OrgMemBench 掉 35.7 分、LongMemEval S 掉 76.0 分；去掉 lexical 几乎无影响；consolidation、fact index、entity graph 增益不稳定甚至为负。  

**最值得记住的一句话**：保留原始文档、读时按时间过滤与多路融合检索，比写时蒸馏或图谱构建更简单且有效，是组织记忆的强基线。
