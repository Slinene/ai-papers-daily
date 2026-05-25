---
title: 'OnePred: Next-Query Prediction via Recursive Intent Memory in Multi-Turn Conversations'
title_zh: OnePred：基于递归意图记忆的多轮对话下一查询预测
authors:
- Jiangwang Chen
- Bowen Zhang
- Zixin Song
- Jiazheng Kang
- Xiao Yang
- Da Zhu
- Guanjun Jiang
affiliations:
- Tsinghua University
- Alibaba Qwen Applications Business Group
arxiv_id: '2605.23668'
url: https://arxiv.org/abs/2605.23668
pdf_url: https://arxiv.org/pdf/2605.23668
published: '2026-05-22'
collected: '2026-05-25'
category: RecSys
direction: 多轮对话下一查询预测 · 递归意图记忆
tags:
- Next-Query Prediction
- Recursive Memory
- Reinforcement Learning
- Intent Tracking
- Multi-Turn Dialogue
- LLM
one_liner: 提出递归记忆与两阶段RL，用恒定上下文长度预测下一查询，token消耗最高降低22倍，质量优于全历史基线
practical_value: '- **对话式电商的主动查询预测**：可直接借鉴递归记忆架构，用小型模型（8B）在每次交互后实时预测用户下一商品咨询或搜索意图，触发预取和缓存，降低感知延迟。

  - **记忆压缩的RL训练范式**：两阶段RL（先学预测再学压缩）解决了端到端记忆无监督问题，对构建主动对话Agent、推荐对话系统中的状态追踪具有通用性。

  - **低成本长对话上下文管理**：利用文本形式的记忆替代KV-cache全量历史，使每轮推理token消耗恒定，适合高并发、长会话的线上场景；500 token预算已足够保留意图轨迹。

  - **预测评估的量规设计**：5点Likert意图评分量表（从完全命中到无关）可迁移至推荐对话的生成质量评估，优于传统n-gram匹配。'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：当前LLM对话系统仍是被动响应，无法预判用户需求，导致检索延迟累积和体验下降。下一查询预测（next-query prediction）可驱动预取、缓存和主动建议，但面临两大瓶颈：全历史拼接导致token成本随对话长度线性增长，且原始历史中大量噪声掩盖预测信号。核心假设是预测只需追踪用户意图演化轨迹，而非重读全部原始历史。

**方法关键点**：
- **递归意图记忆**：维护一个文本记忆状态$m_t$，仅用上一轮记忆$m_{t-1}$和当前交互$(q_t, r_t)$更新，长度上限$k$（500 tokens），形成硬信息瓶颈。记忆经RL优化后专注保存预测相关信号（话题链、未解决问题、兴趣转移）。
- **两阶段强化学习**：Stage 1用完整历史训练模型直接预测下一查询（Full-History RL），掌握“预测什么”；Stage 2切换到记忆接口，模型只能通过自己维护的记忆进行预测，强制学习“压缩什么”。两者皆用GRPO优化，Stage 2将最终预测奖励广播至所有中间记忆更新步，解决无监督记忆的信用分配。
- **奖励设计**：用三模型集成投票的5点意图对齐评分代替文本匹配，避免形式偏差。
- **基准NQP-Bench**：涵盖私域、WildChat、ShareChat三个子集，经多轮过滤保证可预测性，并标注意图转移范式与难度。

**关键结果**：
在三种模型配置（闭源Gemini-3.1-Pro、未训练Qwen3-8B、RL训练Qwen3-8B）下，OnePred均超过Current-turn和Full-history基线。在NQP-Wild上，RL训练的OnePred比Full-history高出1.6分（Judge评分），且在长对话（≥10轮）中优势扩大至+3.7分，保留97%的短对话性能。推理效率方面，平均每轮消耗约650 tokens保持不变，而全历史方法在14轮时达14k tokens，节省最高22倍。消融证实两阶段训练互补：仅Stage 1得43.82分，仅Stage 2得42.96分，完整管线达到46.00。模型规模从1.7B到8B均可受益，8B下RL提升+6.4分。

**一句话**：通过递归记忆把对话历史压缩为预测导向的意图链，用两阶段RL训练，实现恒定成本的下一查询预测，效果反超完整历史输入.
