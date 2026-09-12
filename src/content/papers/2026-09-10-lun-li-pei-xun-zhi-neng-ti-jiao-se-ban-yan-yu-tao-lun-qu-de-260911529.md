---
title: 'Ethics Training Agents: Facilitating Group-Based Ethics Education with Role-Playing
  and Discussion for Ethical Reflection and Exploration'
title_zh: 伦理培训智能体：角色扮演与讨论驱动的群体伦理教育系统
authors:
- Youngseok Seo
- Sueun Jang
- Hyesoo Park
- Renz Samuel Gutierrez
- Joseph Seering
- Uichin Lee
affiliations:
- KAIST
- Georgia Institute of Technology
arxiv_id: '2609.11529'
url: https://arxiv.org/abs/2609.11529
pdf_url: https://arxiv.org/pdf/2609.11529
published: '2026-09-10'
collected: '2026-09-12'
category: MultiAgent
direction: 多智能体协作 · 伦理教育
tags:
- MultiAgent System
- Human-AI Collaboration
- Ethics Education
- Role-Playing
- Group Discussion
- LLM Agents
one_liner: 用多 LLM 智能体扮演不同伦理立场并配主持人，构建结构化人机群体讨论，提升伦理敏感度
practical_value: '- 多智能体角色化设计：在电商/推荐场景可模拟买家、卖家、平台、监管等多方利益相关者，把产品策略或算法伦理评审变成多智能体讨论，提前暴露风险；给每个
  agent 明确价值取向和发言约束，比单一 LLM 自问自答更容易产生对抗性视角。

  - 引入 moderator agent 做结构化协调：负责话题推进、发言顺序、冲突收敛和纪要，这对多 agent 讨论质量很关键，可直接复用到 RAG/Agent
  工作流中的多步规划与 orchestration。

  - 人机混合群体讨论的评估方法：借鉴其用户研究设计，对落地 Agent 产品做过程性指标（参与感、视角采择、协调效率）和结果性指标（决策质量/敏感度）分开测量，而不要只看最终推荐效果。

  - 局限：研究为伦理教育场景、用户规模 45 人，业务可借鉴点主要在 agent 编排与 human-in-the-loop 讨论设计，不直接涉及生成式推荐或
  query 策略。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：STEM 伦理教育资源消耗大，角色扮演、小组讨论等常用活动式教学依赖人工组织，缺乏在线支持。

**方法**：构建 Ethics Training Agents，引入多个 LLM 参与者，各自持有不同伦理取向，另设一个 moderator agent 负责结构化推进；人类学生与多个 AI agent 组成小组讨论，进行协作反思。

**结果**：在 45 名 STEM 本科生用户研究中，系统提升了参与感、讨论协调和观点采择，并对伦理敏感性有正向影响；论文还总结了多 LLM agent 融入多人类小组的设计策略。
