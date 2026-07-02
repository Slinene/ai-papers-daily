---
title: 'The Organizational Behavior of Agentic AI: Collective Intelligence in Human-Agent
  Workflows'
title_zh: 智能体AI的组织行为：人-智能体工作流中的集体智能
authors:
- Canhui Liu
affiliations:
- University College London
- The AI Hub in Generative Models
arxiv_id: '2606.30986'
url: https://arxiv.org/abs/2606.30986
pdf_url: https://arxiv.org/pdf/2606.30986
published: '2026-06-29'
collected: '2026-07-02'
category: MultiAgent
direction: 多智能体组织行为与协作机制
tags:
- MultiAgent
- Organizational Behavior
- Human-Agent Collaboration
- Collective Intelligence
- Contextual Transaction Cost
- Workflow Design
one_liner: 将智能体集体视为部分组织类比，提出上下文交易成本机制，证明共享状态与自适应形式优于模仿人类团队的结构
practical_value: '- 在电商搜索/推荐的多Agent工作流中，优先采用共享记忆或状态架构，避免严格角色隔离和有损消息传递，以保持上下文一致性。

  - 设计自适应协作深度：简单查询由单Agent直接处理，复杂任务再动态调度多Agent协同，减少不必要的通信与相关性审议开销。

  - 引入可检查的上下文快照与校验点，便于调试推荐逻辑链，确保多Agent推荐解释的一致性。

  - 避免多个Agent产生高度相关的推理结果（类似群体思维），可通过注入多样性提示或独立记忆模块打破冗余，提升推荐多样性。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：智能体AI正以集体形式（规划、执行、审查、记忆管理等）进入组织工作流，但其是否真正表现出可分析的组织行为尚不明晰。  
**方法**：将智能体集体与人类组织进行类比，识别相似性（分工、协调、例行程序等）与差异（动机、身份、信任等缺失），提出“上下文交易成本”作为核心机制。通过计算理论、合成任务模拟、真实LLM多智能体轨迹及鲁棒性分析，对比不同组织结构（层级、委员会、市场、共享状态、自适应等）的效能。  
**关键结果**：模仿人类的结构（如层级、委员会）常因有损交接、相关审议和额外验证负担导致性能下降；而共享状态与自适应形式通过使上下文持久化、可检查且任务相关，显著提升集体智能。研究明确了人类与智能体组织行为有效融合的接口条件，为设计高效人-智能体工作流提供了理论基石。
