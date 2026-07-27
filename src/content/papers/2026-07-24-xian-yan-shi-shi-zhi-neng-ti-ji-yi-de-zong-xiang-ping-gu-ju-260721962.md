---
title: 'Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory,
  and the Tenure Crossover in Memory-Architecture Rankings'
title_zh: 先验事实：智能体记忆的纵向评估工具与架构排名逆转
authors:
- Quentin Spencer
affiliations:
- Independent Researcher
arxiv_id: '2607.21962'
url: https://arxiv.org/abs/2607.21962
pdf_url: https://arxiv.org/pdf/2607.21962
published: '2026-07-24'
collected: '2026-07-27'
category: Agent
direction: Agent 记忆评估基准与架构反转
tags:
- Agent Memory
- Benchmark
- Longitudinal Evaluation
- Architecture Crossover
- LLM-as-Judge
- Veracium
one_liner: 提出反转生成流水线的评测基准，揭示记忆架构排名随对话历史长度反转，开源分层记忆库Veracium
practical_value: '- 长期Agent场景（如客服、推荐对话）中，记忆架构需要按信息时效与来源分层，可借鉴「分层图记忆」（provenance-typed
  graph）设计，区分事实有效期和发送/接收信任度，避免简单 LRU 淘汰。

  - 构建记忆评测时，采用“先事实后对话”的生成流水线，机械式出题可杜绝标签泄漏，并且植入时间衰减、注入干扰等特性，更真实模拟业务中持续更新的用户画像。

  - 写入质量直接决定下游问答准确率（弱写事实失败率24% vs. 干净写2%），在记录用户交互（如购物偏好、咨询历史）时，务必保证写入端的清晰度与完整性。

  - 短历史评测会误导架构选择，需结合长期（如数周）对话累积进行压测；全量历史回读虽然短期有效，但成本高且不持久，工程上可优先采用分层记忆实现高性价比。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：现有 LLM-agent 记忆评测存在标签污染、只测短上下文，缺少对事实时效性、来源可信度等真实特性的覆盖，导致架构选择偏差。

方法：提出**反转生成流水线**——先用脚本生成带有效区间、易变性类别、来源渠道的可控事实，再驱动 LLM 渲染聊天与邮件，经忠实度验证后机械式生成问答对，形成 380 题、15 类的**虚构语料**。评测囊括五种记忆架构（如 curated-map、provenance-typed graph 等）与无记忆控制，使用固定回答者、版本化 LLM 评判，在 3 周和 9 周两个时间跨度下做三重随机重复。

关键结果：
- **架构排名逆转**：3 周时领先的 curated-map 在 9 周时召回从 96% 跌至 72%，而 provenance-typed graph 升至 90%；全量历史重读在短期与最佳系统持平或更好，但长期无显著独立优势且读成本高。
- **分层架构最优**：结合两种记忆优势的 layered 系统在短期达 96.8%，长期保持竞争力，已开源为 Veracium 库。
- **写入质量强相关**：弱写事实导致 24% 的问答失败，干净写入仅 2%。
- **注入抵抗**：来源于来源边界是否保留。
