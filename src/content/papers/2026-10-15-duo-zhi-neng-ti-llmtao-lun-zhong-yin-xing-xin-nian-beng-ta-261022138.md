---
title: 'Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM
  Discussions'
title_zh: 多智能体LLM讨论中隐性信念崩塌的测量：相信却不说
authors:
- Liangjie Huang
- Henry Peng Zou
- Wei-Chieh Huang
- Wooseong Yang
- Yuwei Han
- Philip S. Yu
affiliations:
- University of Illinois Chicago
arxiv_id: '2610.22138'
url: https://arxiv.org/abs/2610.22138
pdf_url: https://arxiv.org/pdf/2610.22138
published: '2026-10-15'
collected: '2026-10-18'
category: MultiAgent
direction: 多智能体讨论中的对抗性错误传播与隐性信念崩塌
tags:
- Multi-Agent
- Belief Collapse
- Adversarial Attack
- Conformity
- Factual QA
- LLM
one_liner: 少数对抗智能体反复陈述看似合理的假答案，即可让多数良性智能体私下采信但公开不表态，揭示隐性信念崩塌
practical_value: '- 多 Agent 协同的搜索/推荐/审核系统中，公开发言不一定反映各 Agent 真实判断；建议在关键决策节点增加独立于共享上下文的私密
  probe（如隐藏答案抽取、置信度打分），持续监测隐性漂移，而非只依赖公开投票或共识。

  - 少量对抗性或污染信息（如异常检索结果、有偏商品知识、腐败工具输出）可能在多 Agent 讨论中快速传播；可在架构中加入来源可信度加权、异常 Agent 检测与隔离、关键事实外部校验机制。

  - 对事实性要求高的业务场景（商品卖点、价格政策、售后规则等）不宜完全依赖多 Agent 公开辩论作为唯一护栏；可增加单 Agent 私密事实核查或强 RAG
  约束，减少隐性错误被内化。

  - 评估多 Agent 决策质量时需区分公开立场与私有信念，因为公开支持率可能严重低估真实影响——本实验中三对抗者场景下私有假答案率 51.6% vs 公开支持率仅
  19.7%。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 多智能体系统依赖群体讨论、相互批判与检查，默认同伴能发现个体错误。但共享通信信道本身也是攻击面：被攻陷的工具 Agent、污染检索源或不信任参与者都可反复注入假信息。

**方法**：在 10 个 Agent 的事实讨论中，设置 1 或 3 个对抗 Agent 反复断言一个看似合理的假答案。每轮后通过独立调用（对同伴隐藏）探测每个良性 Agent 的私有答案，同时标记其公开立场。覆盖 6 个模型、3 个事实 QA 数据集，并设置无攻击者基线。

**结果**：无攻击者时群体稳定，仅 0.6% 良性 Agent 最终持有假答案；1 个对抗者使该比例升至 44.8%，3 个对抗者升至 60.5%。与传统从众研究中“公开服从但私下不变”相反，本实验发现反向模式：3 个对抗者存在时，良性 Agent 在暴露轮中 51.6% 持有假答案，但仅 19.7% 公开支持。影响在讨论中大量不可见，且假答案在被单独询问时依然存在。能保留真答案的 Agent 往往不能有效捍卫，假答案会在良性 Agent 间传播，基线知识不能预测稳健性。
