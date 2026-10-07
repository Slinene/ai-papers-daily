---
title: 'MiniCorp: The Last Mile of the AI Agent Firm'
title_zh: MiniCorp：AI Agent 公司模拟器与纵向反事实数据生成
authors:
- Jingying Zeng
- Zhenwei Dai
- Jinning Li
- Changho Shin
- Dylan Zhang
- Yuxuan Lu
- Qi He
- Dakuo Wang
- Kai-Wei Chang
affiliations:
- Microsoft
- University of Illinois Urbana-Champaign
- Princeton University
- Northeastern University
- UCLA
arxiv_id: '2610.05912'
url: https://arxiv.org/abs/2610.05912
pdf_url: https://arxiv.org/pdf/2610.05912
published: '2026-10-04'
collected: '2026-10-07'
category: MultiAgent
direction: 多智能体企业模拟与数据生成
tags:
- Multi-Agent
- Simulation
- Enterprise AI
- Counterfactual Data
- E-commerce
- LLM Agents
one_liner: 构建电商公司多智能体模拟器，生成纵向反事实企业数据，用于训练和评估能自主运营的 Agent
practical_value: '- 构建“模拟器+真实业务反馈”沙盒：在电商场景中，可建立市场模拟器生成反事实数据，用于训练决策 Agent，避免直接在生产环境试错。

  - 使用 checkpointing 机制回放同一情境的不同决策，对比长期效果（如广告预算、定价策略），弥补历史日志无对照组的缺陷。

  - 显式注入长期战略目标（如持续探索弱回报广告）可以防止 Agent 短期优化，对电商中需要平衡探索与变现的场景（如新品冷启动）有直接借鉴意义。

  - 按角色划分多 Agent 并记录通信过程：内部世界按市场、财务等角色分工，记录讨论内容，便于审计和策略优化，也可作为 prompt 设计参考。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：企业级 AGI 的最后一公里是能自我运营的公司，但训练和适配此类 Agent 需要纵向企业数据，而这类数据稀缺、昂贵且受隐私限制；历史档案不完整，只有实际发生的结果，缺乏反事实比较。

**方法关键点**：MiniCorp 是一个办公室模拟器，以电商公司为演示，连接两个交互世界：外部世界模拟顾客、动态竞争对手和市场机制；内部世界由多个 Agent 组成，观察事件、讨论方案并做出战略决策，决策持续影响市场，反馈指导后续决策。系统持续记录 Agent 的通信和决策，保留当时可用信息和后续业务结果。Checkpointing 支持同一情境在不同决策下重放，提供静态档案无法提供的比较。保真度评估对照真实市场实证研究模式，确保反馈真实，减少 Agent 利用模拟器缺陷的风险。

**关键结果**：实验表明 Agent 能跨角色协调并适应市场反馈；在有明确长期战略指导时，即使早期广告回报弱，也保持探索。MiniCorp 为研究 AI 运营公司提供了环境，并可作为训练和评估 Agent 的纵向反事实企业数据来源。
