---
title: Small-world Networks of Agents Brainstorm AI Risks to Support Ideation
title_zh: 小世界网络智能体头脑风暴支持 AI 风险构思
authors:
- Ke Zhou
- Edyta Bogucka
- Daniele Quercia
affiliations:
- Nokia Bell Labs, UK
- University of Nottingham, UK
- Politecnico di Torino, Italy
arxiv_id: '2609.24859'
url: https://arxiv.org/abs/2609.24859
pdf_url: https://arxiv.org/pdf/2609.24859
published: '2026-09-21'
collected: '2026-09-22'
category: MultiAgent
direction: 多智能体小世界网络风险构思
tags:
- LLM agents
- small-world network
- network centrality
- risk ideation
- participatory AI
- multi-agent brainstorming
one_liner: 将 LLM 模拟的利益相关者连成小世界网络，以中介中心性优先风险，提升 AI 风险构思新颖性
practical_value: '- 在需要多智能体头脑风暴或创意生成的场景（如广告文案、活动主题、风险 review），可把 LLM personas 组织成小世界网络（高聚集
  + 短路径）而非全连接或单 agent，显著提升 idea novelty，不损失 plausibility。

  - 聚合阶段不用多数投票或平均分，改用节点中介中心性给 idea 打分/排序，更易捞出桥接不同用户簇、跨域的系统性风险或冷门需求；可优先进入人工评审。

  - 动态 stakeholder 发现：从核心用户/品类/场景出发递归扩展相邻角色，能覆盖传统预设列表漏掉的间接相关方；在电商中可用于模拟极端用户、监管、售后、供应商等，做上线前风险或体验盲区排查。

  - 人机协作方式：把工具生成的高质量种子列表交给业务/用户 workshop，可提升后续讨论的总风险数量与系统/交互/环境类风险，适合作为 HITL 冷启动环节嵌入。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：参与式 AI 风险评估的构思阶段常从空白或预设风险清单开始，容易漏掉间接与系统性危害。
方法关键点：提出三阶段工具：1) 动态发现利益相关者，从给定 AI 用例递归向外扩展，捕捉被忽视的间接方；2) 用 LLM 模拟这些利益相关者，连接成指定拓扑（小世界网络）进行风险头脑风暴；3) 用网络中心性对风险排序。小世界网络 + betweenness centrality 效果最佳，能抬升桥接断连群体的利益相关者所提风险。
结果：在 AI 聊天伴侣用例上，相比单 LLM 头脑风暴，新颖性在 5 分归一 Likert 上约提升 1.1 分；相比普通 agentic LLM 头脑风暴提升 0.5 分，且合理性、严重性未下降。在 11 个非西方年轻聊天机器人用户团队参与的 Futures Wheel 人工构思中，以框架生成清单作为起点的 treatment 组识别出更多整体风险，尤其在系统性、人机交互与环境风险方面，而这些类别从业者通常更难发现。
