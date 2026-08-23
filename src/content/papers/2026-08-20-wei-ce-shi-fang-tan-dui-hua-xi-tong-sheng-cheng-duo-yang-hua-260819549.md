---
title: Generating Diverse Personas for User Simulators to Test Interview Dialogue
  Systems
title_zh: 为测试访谈对话系统生成多样化用户模拟器画像
authors:
- Mikio Nakano
- Kazunori Komatani
- Hironori Takeuchi
affiliations:
- C4A Research Institute, Inc.
- SANKEN, University of Osaka
- Musashi University
arxiv_id: '2608.19549'
url: https://arxiv.org/abs/2608.19549
pdf_url: https://arxiv.org/pdf/2608.19549
published: '2026-08-20'
collected: '2026-08-23'
category: LLM
direction: 用户模拟器 persona 多样性生成
tags:
- Persona Generation
- User Simulator
- LLM
- Dialogue Systems
- Diversity
one_liner: 用 LLM 自动生成带沟通风格人格特质的用户画像，提升访谈对话系统测试中用户模拟器的行为多样性
practical_value: '- 在构建 Agent 用户模拟器做评测或数据合成时，可复用「LLM 生成 persona + 显式注入沟通风格人格特质」的方法，低成本扩大用户行为覆盖面，避免人工构造
  personas 的瓶颈。

  - 对于需要模拟多样化用户场景（如访谈、客服、搜索会话）的评测，可先定义人格特质维度（如沟通风格），再让 LLM 根据特质生成 personas，从而控制多样性。

  - 如果要为推荐/搜索 Agent 做模拟评测，可以用类似思路生成不同背景、偏好、表达习惯的用户，帮助发现 Agent 对长尾用户行为的鲁棒性。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**  
访谈对话系统测试依赖大量真人用户，成本高、效率低。用户模拟器虽能降低测试负担，但现有模拟器主要面向任务型对话训练，对模拟用户的 persona 关注不足；手动创建覆盖多样行为的 persona 又很耗时。

**方法关键点**  
提出用 LLM 自动生成用户模拟器所需的 personas。关键设计是：生成时显式分配与沟通风格相关的人格特质（如直接/委婉、主动/被动），以提升沟通风格的多样性。生成的 personas 被送入用户模拟器，控制其对话中的语言风格与行为模式。

**关键结果**  
实验表明，该方法能让用户模拟器生成的话语（utterances）具有更大的变化幅度，即多样性显著提升。
