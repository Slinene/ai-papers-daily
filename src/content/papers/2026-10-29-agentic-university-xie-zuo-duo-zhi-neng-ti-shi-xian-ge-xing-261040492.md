---
title: 'Agentic University: Collaborative Agents for Personalized Learning'
title_zh: Agentic University：协作多智能体实现个性化学习
authors:
- Jingru Fan
- Tianle Zhou
- Yunjie Zhou
- Zihao He
- Yixuan Zhou
- Kezhao Wu
- Xinyu Zheng
- Xiyuan Wang
- Yuheng Wang
- Zhi Li
affiliations:
- Shanghai Jiao Tong University
- Nanyang Technological University
- National University of Singapore
arxiv_id: '2610.40492'
url: https://arxiv.org/abs/2610.40492
pdf_url: https://arxiv.org/pdf/2610.40492
published: '2026-10-29'
collected: '2026-11-01'
category: MultiAgent
direction: 多智能体协作个性化学习
tags:
- multi-agent
- personalized learning
- LLM
- human-in-the-loop
- adaptive learning
one_liner: 提出人类参与的多智能体组织方法，让学习者与专门Agent协作维护可修订能力计划，实现连贯自适应学习
practical_value: '- 借鉴“Capability Program”作为用户长期偏好/目标的显式表示，让用户参与目标设定与修订，将行为证据（点击、转化、反馈）作为驱动后续推荐策略的“学习证据”，形成目标-行为-评估闭环。

  - 多智能体组织分工：将推荐链路拆分为目标对齐、候选生成、评估反思等专门 agent，通过组织化协调而非单一大模型调用，提升系统的可解释性和可控性；可参考其“人类参与”机制，让用户作为协作方而非被动对象。

  - 分层评估与反馈闭环：引入分层评估（如短期满意度、长期能力提升）并利用评估结果触发策略修订，对应推荐系统中结合即时指标（CTR）与长期指标（用户留存、LTV）的动态调整。

  - 工程实现上，Agent 间通过共享可修订文档（Capability Program）协调，类似用结构化状态文件协调多智能体，适合电商场景中多 agent 共同维护用户画像或推荐策略。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 在个性化辅导、内容生成和自适应学习路径方面已有应用，但如何将零散的资源与交互组织成随学习者演化的连贯学习过程，关键在于对齐目标、活动与评估，并利用学习证据决定后续步骤。

**方法关键点**：提出 Human-Participatory Multi-Agent Organization，并实例化为 Agentic University（AU）。在 AU 中，学习者作为组织成员参与，与专业化 Agent 协作维护一个可修订的 Capability Program。该计划连接个人目标、跨模态学习活动和分层评估，学习者的反馈与表现引导后续支持。系统通过多智能体协调，使学习过程的各部分形成整体。

**关键结果数字**：与基线相比，用户在 50 分制评估中平均增益 12.19 分（基线 5.61 分），并报告更强的认知支持；在计划组织、评估设计和修订质量方面均表现优势。
