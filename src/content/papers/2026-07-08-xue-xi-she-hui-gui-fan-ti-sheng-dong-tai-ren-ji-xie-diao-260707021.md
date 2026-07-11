---
title: Learning social norms enhances compatibility in dynamic human-AI coordination
title_zh: 学习社会规范提升动态人机协调兼容性
authors:
- Yi Yang
- Siyuan Liu
- Xin Gao
- Huamu Sun
- Chao Liu
- Qing Zhou
- Bingbing Nie
arxiv_id: '2607.07021'
url: https://arxiv.org/abs/2607.07021
pdf_url: https://arxiv.org/pdf/2607.07021
published: '2026-07-08'
collected: '2026-07-11'
category: Agent
direction: Agent · 社会规范量化与协调优化
tags:
- social norms
- human-AI coordination
- LLM agents
- dynamic interaction
- reward design
one_liner: 量化行人交互中的社会规范三原则（结果可预测、价值对齐、优势意识）使LLM协调得分超基线4倍，超人类43%
practical_value: '- 在电商客服、对话推荐agent中显式定义类“可预测性、价值对齐、优势意识”的规范原则，可通过system prompt或RLHF
  reward塑造行为，提升用户对连贯性与体谅度的体验。

  - 通过小规模人类交互实验提取隐式规范的方法，可迁移到推荐系统：设计轻量级问卷或游戏收集用户动态协作偏好，抽取出“响应时机”“主动推荐程度”等维度，用于微调对话策略。

  - 闭-loop交互评测框架（人机反复博弈）可复用于搜索/推荐系统的多轮效果评估，取代单轮离线和静态用户模型测试，更能捕捉长期协调性与粘性。

  - 优势意识原则（agent意识到自身信息优势时主动引导）可直接用于主动推荐场景：当模型拥有用户历史、库存等全局信息时，应更主动地提供选项并解释理由，而非被动等待查询。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：当前LLM在人机动态交互中常表现机械、不自然，原因是只模仿表面行为而未量化底层共享的社会规范。行人-车辆交互被选为典型场景，此类交互存在隐式协调规则，如谁先走、如何让步。

**方法**：构建简化实验平台收集3456次真实人类动态交互，通过行为分析归纳出三种量化原则：① 结果可预测性——交互结果应稳定且符合期望；② 价值对齐——行为应尊重对方偏好（如时间损失、安全）；③ 优势意识——当一方拥有信息或行动优势时，应主动承担更多协调责任。将这些原则编码为LLM的提示词或奖励信号，指导其决策。

**结果**：在人类参与的闭环交互任务中，社会规范知情LLM的总得分比行为克隆基线高近4倍，甚至比实际人类-人类交互组高43%，互动更加高效、体贴、自然。
