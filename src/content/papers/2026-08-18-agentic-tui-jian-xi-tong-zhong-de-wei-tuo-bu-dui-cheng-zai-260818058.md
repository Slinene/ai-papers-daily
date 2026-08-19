---
title: 'Delegation Asymmetry in Agentic Recommender Systems: Measuring Two-Sided Receptivity
  in Online Dating'
title_zh: Agentic 推荐系统中的委托不对称：在线约会双向接受度测量
authors:
- Daria Leshchikova
- Valentina V. Kuskova
- Dmitry Zaytsev
- Valerii Klimov
affiliations:
- Fleamily, Inc.
- Lucy Family Institute for Data & Society, University of Notre Dame
arxiv_id: '2608.18058'
url: https://arxiv.org/abs/2608.18058
pdf_url: https://arxiv.org/pdf/2608.18058
published: '2026-08-18'
collected: '2026-08-19'
category: Agent
direction: Agentic 推荐系统 · 双向接受度建模
tags:
- LLM agents
- agentic recommender systems
- two-sided receptivity
- delegation asymmetry
- graded response model
- online dating
one_liner: 用双语言大规模调查与潜变量模型证明发送和接收 Agent 对话的接受度是两个不同构念，并量化部署-接收不对称及路由增益
practical_value: '- 在构建 Agent 对话/推荐系统时，把“用户是否愿意让 Agent 代表自己对外发消息”和“是否愿意收到对方 Agent
  消息”分开测量与建模，两者相关但可分（ρ=0.92，ΔBIC=52），合并成一个接受度指标会高估用户接受度。

  - 路由策略可借鉴：按“接收方接受 Agent 消息的概率”优先路由 agent-initiated 消息，论文显示每次接触互动率提升约 3 倍，OOS AUC=0.88；对应电商导购、社交推荐中的
  receptivity-aware matchmaking，即用接收方接受度分数做排序或过滤。

  - 产品设计需提供分层 opt-in 和披露机制：部署自己 Agent 的阈值（θ=-0.38）远低于与对方 Agent 互动（θ=+0.32, 全互动 +1.39），发送与接收意愿对称性差，不能只问一句“是否允许
  Agent”。建议分别设置同意开关，降低用户防御。

  - 互惠要求/双向同意会显著压缩可用池：要求双方都接受 Agent 通信会排除近三分之二潜在部署者，交互量减半以上；在冷启动或规模优先场景下应谨慎使用强制双向
  opt-in，可改为单侧路由 + 接收端优先策略。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM Agent 代用户对话成为匹配平台的新设计范式，但其可行性依赖于一个很少被检验的条件：用户不仅要愿意把自己的对话委托给 Agent，还要愿意接受对方由 Agent 中介的沟通。论文聚焦这一双向接受度。

**方法关键点**：在两个大规模调查中（生成式个人资料特征 N=2,894；自动对话 Agent N=2,617，双语言），用 graded response model 加 latent regression 建立潜变量测量模型。模型比较显示，发送 Agent 消息的意愿与接收 Agent 消息的意愿是两个不同构念：高度相关（ρ=0.92）但可分（ΔBIC=52），且具有跨语言部分测量不变性。模型量化了系统性委托不对称：部署自己 Agent 所需的接受度阈值（θ=-0.38）远低于与对方 Agent 互动的阈值（θ=+0.32；全互动 +1.39），平均部署倾向约为互动倾向的三倍。

**关键结果**：基于陈述接受度的随机配对反事实中，仅 4–13% 的有向二元组同时满足部署 Agent 与接收端互动，性别方向不平衡明显。设计反事实显示：互惠要求会排除近三分之二潜在部署者，交互量减半以上；而按接收接受度路由 agent 消息可使每次接触互动率提升约 3 倍，经 leave-item-out 验证 AUC=0.88，respondent-level CV 下四分位提升 3.1×。论文据此讨论披露、opt-in 机制和接受度感知匹配设计。
