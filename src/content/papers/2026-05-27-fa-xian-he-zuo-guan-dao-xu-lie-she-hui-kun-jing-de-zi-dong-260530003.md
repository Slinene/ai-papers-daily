---
title: 'Discovering Cooperative Pipelines: Autoresearch for Sequential Social Dilemmas'
title_zh: 发现合作管道：序列社会困境的自动研究
authors:
- Víctor Gallego
affiliations:
- Komorebi AI Technologies
arxiv_id: '2605.30003'
url: https://arxiv.org/abs/2605.30003
pdf_url: https://arxiv.org/pdf/2605.30003
published: '2026-05-27'
collected: '2026-05-30'
category: MultiAgent
direction: 多智能体合作 · 自动管道发现
tags:
- Autoresearch
- MultiAgent
- Sequential Social Dilemmas
- LLM-as-Policy
- Cooperation
- Fairness
one_liner: 外层AI代理自主重新设计内层LLM策略合成管道，在多智能体社会困境中超越手工基线并目标自适应注入公平机制
practical_value: '- 可借鉴**自动管道搜索范式**：用外层智能体（如Coding Agent）动态编辑内层智能体系统的提示、反馈函数、迭代逻辑，自主发现更优协作策略，减少手工调参。

  - 在电商多智能体场景（如多个推荐Agent竞价、协商）中，可**目标自适应机制注入**：当业务目标从效率转向公平（如GMV vs. 中小商家曝光）时，系统能自动引入公平约束，无需人工重设计。

  - 通过**信息设计（Information Design）** 视角优化Agent行为：控制向有限理性Agent透露的信息（如修改反馈信号或辅助库），间接引导其决策，该方法可用于推荐系统中的多目标权衡。

  - 工程上，可将**外层研究Agent与内层合成管道解耦**，实现持续自动实验：定期让R探索新管道，利用评估指标选择最优配置，降低人工维护成本并稳定方差。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：多智能体序列社会困境（如公地悲剧）中，个体理性导致集体次优，传统MARL困难。近期LLM策略合成方法虽有效，但依赖手工设计管道。本文研究如何自动发现更优的协作管道。

**方法**：提出两级自动研究框架，外层研究者Agent R（编码Agent）读取内层LLM策略合成系统的源码，自主编辑系统提示、反馈函数、辅助库和迭代逻辑，运行评估，并决定保留与否。内层合成器在自对弈中迭代生成Python策略。实验覆盖Cleanup和Gathering两个游戏、两种合成器LLM、功利效率与罗尔斯最小最大化两种福利目标。

**关键结果**：自动发现的管道在所有配置下均超越手工设计基线，显著降低运行间方差，优于纯提示优化。尤其在最小最大化目标下，R自发注入显式公平机制（如约束资源分配），而效率目标下无此行为，表明管道发现是目标依赖的。这支持信息设计解读：R根据福利目标选择向有限理性合成器透露何种信息。
