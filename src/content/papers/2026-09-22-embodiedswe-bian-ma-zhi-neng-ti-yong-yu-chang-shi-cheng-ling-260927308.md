---
title: 'EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics'
title_zh: EmbodiedSWE：编码智能体用于长时程灵巧机器人及策略监督
authors:
- Haoxiang You
- Zeyu Shen
- Yilang Liu
- Zhicheng Zheng
- Lihan Zha
- Kashu Yamazaki
- Mingtong Zhang
- Suning Huang
- Jiankai Sun
- Qianzhong Chen
affiliations:
- ByteDance Seed
- Yale University
- Princeton University
- Carnegie Mellon University
- Stanford University
arxiv_id: '2609.27308'
url: https://arxiv.org/abs/2609.27308
pdf_url: https://arxiv.org/pdf/2609.27308
published: '2026-09-22'
collected: '2026-09-24'
category: Agent
direction: 编码智能体与机器人策略数据生成
tags:
- Coding Agents
- VLA
- Robotics
- Simulation Benchmark
- Data Generation
- Embodied AI
one_liner: 提出 EmbodiedSWE 基准与 EmbodiedSWE-Gen 流水线，用编码智能体解决机器人任务并生成大规模训练数据以提升 VLA 策略
practical_value: '- 借鉴 EmbodiedSWE-Gen 的思路：让 LLM coding agent 在仿真/沙盒中生成任务解决方案（如推荐策略、用户模拟器或
  query 改写规则），再通过参数扰动、初始状态随机化、对象属性变化等方式扩充为大规模多样化交互轨迹，用于训练排序/策略模型，降低人工标注成本并提升长尾场景泛化。

  - 为 coding agent 封装可验证的工具 API 与奖励函数（例如模拟用户反馈、转化率仿真器、线上策略回放），使 agent 能迭代 refine 策略；业务上可将验证通过的
  agent 方案蒸馏进轻量模型部署，避免线上实时调用的高延迟。

  - 利用“单方案/单轨迹→多样轨迹”的扩增方法：在推荐系统中，将一条成功用户轨迹或一个高质量策略通过环境扰动、反事实操作、行为模拟生成大量多样训练样本，缓解数据稀疏和冷启动问题。

  - 注意 agent 生成方案需要大量迭代交互且易任务特化，落地时优先离线用于高价值场景（如大促机制设计、自动化营销策略生成），并设置验证门槛以减少无效探索。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：长程、灵巧机器人任务数据采集与策略学习困难，现有手工示范成本高；探索 coding agents 能否解决复杂任务并作为可扩展的监督信号。

**方法**：构建 EmbodiedSWE-Bench 仿真基准，覆盖接触丰富操作、可变形物体和最长 30 分钟连续交互的长时程任务。为 coding agents 设计支持工具，使其迭代求解并可跨任务/embodiment 迁移方案。针对单一解决方案特化问题，提出 EmbodiedSWE-Gen：将单个已验证的 coding agent 方案扩展为大规模多样轨迹，用于训练 VLA 模型，并引入 agent-aided 多样化提升泛化。

**结果**：前沿 coding agents 能解决复杂长时程任务，但需要大量迭代交互且方案通常特化于单个任务实例。通过 EmbodiedSWE-Gen 扩展数据后，VLA 性能随生成示范数量提升，agent-aided 多样化改善对 held-out 任务变体的泛化；仅用仿真生成的示范微调 VLA，即可在真实机器人上完成长时程任务。
