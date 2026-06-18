---
title: 'SAGE: Stochastic Prompt Optimization via Agent-Guided Exploration'
title_zh: SAGE：通过智能体引导探索的随机提示优化
authors:
- Ziyi Zhu
- Luka Smyth
- Saki Shinoda
- Jinghong Chen
affiliations:
- Slingshot AI
- University of Cambridge
arxiv_id: '2606.18902'
url: https://arxiv.org/abs/2606.18902
pdf_url: https://arxiv.org/pdf/2606.18902
published: '2026-06-17'
collected: '2026-06-18'
category: MultiAgent
direction: 提示优化 · 多智能体协作
tags:
- Prompt Optimization
- Multi-Agent
- Stochastic Search
- A-B Testing
- LLM
one_liner: 提出多智能体诊断执行框架 SAGE，通过随机搜索与连续 A/B 测试将提示优化累积为统计显著的次日留存提升
practical_value: '- 面向对话式推荐或客服机器人，可用 Agent 自动诊断 Bad Case 并生成修复提示，替代人工迭代

  - 借鉴连续 A/B 测试范式，将单次噪声大的实验累积为长期关键指标（如留存、转化）的可靠增益

  - 错误信息驱动的随机搜索策略成本低，可用于推荐系统召回/排序模块的 prompt 候选生成

  - 多智能体协同中加入代码执行（如数据统计、校验），能提升诊断深度，可用于商品推荐理由生成的自动化调试'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有自动提示优化（APO）方法缺乏理论视角，基于文本梯度的优化被证明并非真实梯度，本质是黑盒搜索；且多数方法采用逐样本贪婪更新，易陷入局部最优，分析仅限 LLM 推理，缺乏结构化的诊断与修复能力。

**方法**：提出 SPO（随机提示优化）框架，将提示搜索视为带噪声的昂贵黑盒优化。比较三种策略：1）基于错误信息的随机搜索，利用错误案例引导随机突变；2）带进化算子的遗传算法；3）SAGE（智能体引导探索），引入多智能体流水线——一个智能体分析错误样本并生成诊断代码，执行代码获得统计信息，另一个智能体基于诊断生成候选提示，并通过贝叶斯优化选择下一轮评估点。

**结果**：在三个文本基准上，没有单一策略全面占优，搜索效果取决于错误类型与景观结构。在心理健康聊天机器人上，SAGE 部署为连续优化范式，通过 8 轮每轮噪声较大的 A/B 测试，累积得到次日留存率的统计显著提升（p<0.05），证明定性诊断与定量验证的结合使智能体优化在开放域任务导向对话中有效。
