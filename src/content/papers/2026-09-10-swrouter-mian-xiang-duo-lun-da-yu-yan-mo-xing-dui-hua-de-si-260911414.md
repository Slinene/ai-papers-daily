---
title: 'SWRouter: Similarity-Contractive Window Routing for Multi-Turn Large Language
  Model Conversations'
title_zh: SWRouter：面向多轮大语言模型对话的相似度收缩窗口路由
authors:
- Yu Wang
- Yuchen Li
- Rui Kong
- Xinran Chen
- Jiamin Chen
- Hengyi Cai
- Shuaiqiang Wang
- Jiashu Zhao
- Yulun Zhang
- Zhonghao Lyu
affiliations:
- Shanghai Jiao Tong University
- Baidu Inc.
- Wilfrid Laurier University
- The Hang Seng University of Hong Kong
- York University
arxiv_id: '2609.11414'
url: https://arxiv.org/abs/2609.11414
pdf_url: https://arxiv.org/pdf/2609.11414
published: '2026-09-10'
collected: '2026-09-12'
category: LLM
direction: 多轮LLM路由与上下文构建
tags:
- LLM routing
- multi-turn dialogue
- context segmentation
- evaluation framework
- similarity-contractive window
one_liner: 提出相似度收缩窗口的上下文分段与双指标评估，多轮路由准确率较最佳单模型提升16.26%
practical_value: '- 多轮对话/客服Agent中的模型路由不能简单沿用单轮特征；需要显式设计历史上下文的切割与保留。文中相似度收缩窗口的思路可直接用于对话状态上下文管理：按语义相似度而非固定轮数滑动窗口，降低历史信息混淆与冗余。

  - 评估路由策略时，建议将上下文构建质量与路由决策解耦，采用双指标评测；否则上下文构建差会掩盖路由器的真实能力，这在线上A/B测试中容易误判。

  - 对电商导购/搜索多轮Agent，可在多模型池（大模型、小模型、领域模型）上实现基于上下文分段的路由，降低长会话长尾token成本和延迟，同时保持回复质量。

  - 工程实现上，相似度分割可以通过现成embedding+阈值/聚类实现，轻量，适合在线服务；无须训练路由器，可先行试点。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有LLM路由器在单轮场景有效，但直接迁移到多轮对话时性能大幅下降。核心瓶颈在于历史上下文如何被切分、保留并融入当前prompt，容易出现信息丢失或信息混淆；同时现有评估难以区分上下文构建质量与路由决策质量。

**方法关键点**：SWRouter提出相似度收缩窗口机制，基于语义相似度对历史轮次进行分段并压缩，保留关键信息的同时抑制冗余与干扰；同时设计双指标评估框架，将上下文构建准确度与路由性能解耦，分别衡量“是否选对上下文”和“是否选对模型”。

**关键结果**：在多轮对话基准上，SWRouter较最佳单一LLM评估准确率提升16.26%，较Conv-ID上下文基线再提升8.22%。实验表明多轮路由必须联合设计上下文构建与评估，而非单轮方法的简单扩展。
