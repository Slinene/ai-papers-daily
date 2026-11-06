---
title: 'Persistent Retrieval for Conversational Agents: A Study of Retrieval Efficiency'
title_zh: 面向会话代理的持久化检索：检索效率研究
authors:
- Karthik Ravula
- Sathwik Kowtha
- Rishabh Verma
- Kala Mehak Jain
- Gunjit Mittal
affiliations:
- ServiceNow
arxiv_id: '2611.07899'
url: https://arxiv.org/abs/2611.07899
pdf_url: https://arxiv.org/pdf/2611.07899
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: Agent 持久化检索子代理设计
tags:
- Persistent Retrieval
- Subagent
- Multi-turn
- Token Efficiency
- Conversational Agent
one_liner: 提出持久化检索子代理架构，跨轮维护检索历史并直接返回证据，较技能检索节省43.3% token和45.0%成本，延迟降9.1%
practical_value: '- 在对话式电商助手或客服 Agent 中，将检索状态（已召回商品集、用户偏好槽位）独立到有状态子代理或专用检索服务，避免主 LLM
  上下文被历史工具结果撑大；可节省主代理 token，缓解长对话上下文溢出。

  - 让检索子代理返回原始证据（商品/知识条目）而非生成推荐文案，由主 LLM 排序和解释，避免中间压缩丢失细节；主代理可继续向同一子代理发送修正指令（如“价格低于500”、“换品牌”），在现有结果上增量更新，减少重检索延迟。

  - 权衡 tokens 与延迟：若业务强延迟敏感（如实时导购、广告文案生成），优先持久化检索；若成本敏感且可容忍重复检索，非持久化子代理已足够。论文量化差值：延迟
  -15.6s/问，但 token +65.1%，API 成本 +29.1%，便于架构选型。

  - 多轮 query 重写或搜索建议可借鉴：保持跨轮 query 状态，将证据原样传给生成器，减少 repeated context 和重复召回。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：对话代理中检索设计影响历史维护、上下文大小和多轮后续问题的重复检索。企业场景中，技能检索在主代理内执行，历史工具结果不断累积到上下文，导致 token 与成本上升；非持久化检索子代理虽然隔离上下文，但每轮重新检索，延迟高。

**方法关键点**：提出持久化检索子代理：跨轮维护检索历史，将检索证据直接返回给主代理，而非生成综合答案；主代理可向同一子代理请求修正。这种设计将检索状态从主代理上下文剥离，子代理负责维护状态并提供可被主代理直接评估的证据。

**关键结果**：在五个多轮设置中，相比技能检索，持久化检索子代理节省 43.3% 的代理模型 token，降低 45.0% 估计 API 成本，响应时间减少 9.1%；相比非持久化检索，每问题响应时间降低 15.6 秒，但 token 增加 65.1%，API 成本高 29.1%。核心权衡：延迟敏感场景优选持久化，成本敏感场景可选非持久化。
