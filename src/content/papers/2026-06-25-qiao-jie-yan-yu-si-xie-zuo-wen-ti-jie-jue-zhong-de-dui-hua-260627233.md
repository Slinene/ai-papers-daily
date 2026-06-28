---
title: 'Bridging Talk and Thought: Understanding Dialogue Dynamics Across Collaborative
  Problem-Solving Contexts'
title_zh: 桥接言与思：协作问题解决中的对话动态分析框架
authors:
- Zhengyuan Liu
- Stella Xin Yin
- Min-Yen Kan
- Nancy F. Chen
affiliations:
- Nanyang Technological University
- Agency for Science, Technology and Research (A*STAR)
- National University of Singapore
arxiv_id: '2606.27233'
url: https://arxiv.org/abs/2606.27233
pdf_url: https://arxiv.org/pdf/2606.27233
published: '2026-06-25'
collected: '2026-06-28'
category: MultiAgent
direction: 多智体协作·对话分析
tags:
- Dialogue Analysis
- Collaborative Problem-Solving
- Metacognitive Regulation
- Multi-Agent Systems
- Human-AI Collaboration
one_liner: 提出双层对话编码框架，整合认知与非认知维度及元认知调节，揭示元认知是深层协作的关键区分器
practical_value: '- 评估推荐对话或多轮客服质量时，可引入元认知调节指标（如计划、监控、反思类话语）作为高阶评判维度，单纯任务完成率不够。

  - 设计多 Agent 协作系统（如协商推荐）时，显式建模 Agent 的元认知交互（例如生成“是否需调整策略”类话语），可能提升协作深度与用户信任。

  - 对话标注可借鉴双层方案，同时标注用户或 Agent 的认知行为与元认知调节，辅助构建更细粒度的对话理解模型。

  - 研究结论提示，元认知模式可用于诊断人机协作瓶颈——当对话缺乏监控与调节时，协作易浮于表面，该信号可作为触发干预的规则。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：协作问题解决的对话分析常偏重任务完成度，忽略了参与者如何协调思维、监控进度等元认知过程。随着人机协作与多智能体系统普及，亟需一个能同时捕捉认知、非认知行为及元认知调节的分析框架。

**方法**：提出了层次化双层对话编码方案。第一层将对话语句分为认知与非认知问题解决行为；第二层细粒度标注元认知调节机制，包括计划、监控、评估、反思等子类。该方案在涵盖教育、办公等九个数据集上验证，既有人-人对话，也有人-AI与多智能体协作数据。

**关键结果**：框架在不同领域均表现出高标注一致性，并有效揭示协作深度差异。尤其发现，元认知调节类话语（如“我们是否需要重新思考方案”）是区分表面协作与深度协作的最显著指标，其出现频率与协作质量强相关。该结论为未来设计更具协作性的对话智能体提供了明确优化方向。
