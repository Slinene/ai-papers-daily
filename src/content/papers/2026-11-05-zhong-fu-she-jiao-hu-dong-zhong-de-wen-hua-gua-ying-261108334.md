---
title: Cultural Adaptation within Repeated Social Interactions
title_zh: 重复社交互动中的文化适应
authors:
- Chen Cecilia Liu
- Roi Reichart
- Anna Korhonen
affiliations:
- Language Technology Lab - University of Cambridge
- Technion - Israel Institute of Technology
arxiv_id: '2611.08334'
url: https://arxiv.org/abs/2611.08334
pdf_url: https://arxiv.org/pdf/2611.08334
published: '2026-11-05'
collected: '2026-11-08'
category: Agent
direction: Agent 交互式文化适应与记忆机制
tags:
- Cultural Adaptation
- LLM Agents
- Memory Mechanism
- Norm Assimilation
- Multilingual
one_liner: 将文化适应重构为通过社交互动持续同化规范，用记忆机制使LLM在重复交互中学习并迁移规范
practical_value: '- 把推荐/客服Agent的用户偏好当作“隐性文化规范”，设计跨会话记忆使模型通过用户反馈持续调整行为，替代每轮从零开始的静态画像。

  - 在沙盒中模拟多轮交互测试Agent的长期适应能力，重点检查是否能将学到的用户规范迁移到新品类或新用户群。

  - 多语言场景下利用跨语言规范同化，通过共享用户规范表示改善低资源语言个性化冷启动。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：人类文化多为隐性，通过具体社会互动习得；现有NLP文化评估多为静态知识问答，把LLM当作固定知识库，难以衡量交互代理在实际社区中的文化适应能力。

**方法关键点**：将文化适应重新定义为通过社会互动持续同化规范的过程；构建沙盒环境，让LLM在重复交互中接收社会反馈并逐步调整行为；重点考察记忆机制，包括跨时间纵向学习、不同社会情境之间的迁移、以及跨五种语言的规范同化。

**关键结果**：记忆机制使LLM能够在重复交互中持续学习文化规范，保持行为适应，并可迁移到新的社会情境；规范同化能力可跨五种语言泛化。
