---
title: Toward a Compositional Knowledge Architecture for a Shared Organizational Cortex
title_zh: 迈向共享组织皮层的组合式知识架构
authors:
- Andrew Miracle
- Phyl Georgiou
- Christine Okoth
- Ese Monday
affiliations:
- Robin Inc.
- Nosen
arxiv_id: '2611.05753'
url: https://arxiv.org/abs/2611.05753
pdf_url: https://arxiv.org/pdf/2611.05753
published: '2026-11-03'
collected: '2026-11-05'
category: RAG
direction: 组织级共享知识架构与可修订判断存储
tags:
- Knowledge Architecture
- Truth Maintenance
- Organizational Memory
- Retrieval
- Agent Memory
one_liner: 提出四层知识架构与真值维护网络，让解释性判断随证据修订并提升检索效果
practical_value: '- 电商搜索/推荐团队可将原始行为日志（Signals）与解释性判断（Claims）分层存储：例如把“价格敏感”“偏好风格”等用户画像做成带依据和置信度的
  Claim，避免每次从点击序列重新推断。

  - 在 Agent 或客服知识系统中引入 truth-maintenance：当商品属性、库存、政策等证据变化时，自动降级或撤销相关 Claim，保持知识一致性，减少过期信息影响决策。

  - 用版本化 Dimensions 管理维度标签（如“性价比”“时尚度”），支持按时间回溯和对比，用于模型可解释性、实验归因。

  - 多 Agent 协作可建立共享 Claim 层，每个 Claim 必须携带 justification 和 standing，缓解“结论传播但丢失证据”的不确定性吸收问题。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：组织积累大量证据（对话、文档、决策），但实际依靠的是解释性判断——这些判断由多个观察组装、基于假设、随环境修订。现有检索、知识图谱和 Agent 记忆只留存记录，丢失了解释及其依据和状态，导致后续请求必须重新推断甚至误判。

方法：提出四层架构 Signals（原始信号）→ Domains（领域）→ Claims（断言/解释，附论证）→ Dimensions（版本化维度轴，定位判断）。Truth-maintenance network 根据证据变化自动修订 Claim 的 standing；Dimensions 经校验和版本化，使组织形成“共享皮层”，保存可持久、可修订的判断基础。

关键结果：注册检索实验中，Dimension term 带来 nDCG@10 +0.028 (p=0.002)；系统级对比中，完整检索配置比 Signals-only 高 0.081，比 graph-augmented Signals-only 高 0.053（p<0.001），验证该架构对检索效果有显著提升。
