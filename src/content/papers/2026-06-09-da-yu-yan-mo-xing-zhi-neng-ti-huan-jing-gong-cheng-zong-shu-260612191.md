---
title: 'Agentic Environment Engineering for Large Language Models: A Survey of Environment
  Modeling, Synthesis, Evaluation, and Application'
title_zh: 大语言模型智能体环境工程综述：建模、合成、评估与应用
authors:
- Jiachun Li
- Zhuoran Jin
- Tianyi Men
- Yupu Hao
- Kejian Zhu
- Lingshuai Wang
- Dongqi Huang
- Longxiang Wang
- Shengjia Hua
- Lu Wang
arxiv_id: '2606.12191'
url: https://arxiv.org/abs/2606.12191
pdf_url: https://arxiv.org/pdf/2606.12191
published: '2026-06-09'
collected: '2026-06-11'
category: Agent
direction: Agent 环境工程与共同进化综述
tags:
- Agentic Environment Engineering
- LLM Agents
- Environment Synthesis
- Agent Evolution
- Survey
one_liner: 从环境工程生命周期视角系统梳理智能体环境建模、合成、评估及与环境共同进化的研究
practical_value: '- **自动化环境合成**：可借鉴符号合成与神经合成两种范式，为电商推荐智能体自动生成训练场景（如模拟多轮对话、用户行为轨迹），降低人工设计成本。

  - **难度驱动进化**：借鉴难度驱动的环境进化策略，在推荐Agent训练中根据其在线表现动态调整环境复杂性，提升泛化能力。

  - **四类智能体进化路径**：记忆、工作流、轨迹、探索四种进化方向可直接映射到多智能体电商系统中的经验回放、流程优化、离线轨迹学习与在线探索。

  - **多智能体环境即服务**：未来多Agent环境可打包为可复用的沙箱服务，用于测试和优化协同推荐、竞价策略等复杂决策逻辑。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：环境是驱动LLM智能体能力进化的关键因素，但现有工作缺乏对环境设计、合成与进化过程的系统梳理，本文旨在填补这一空白，提供环境工程全生命周期的统一视图。

**方法**：
- 从**8项属性**（目标、约束、动态性等）和**8个领域**（游戏、科学等）梳理代表性环境，分析其发展路径。
- 提出**环境自动合成**的两类范式：符号合成（基于规则生成）与神经合成（利用生成模型构造环境），并对比各自的环境评估方法。
- 从**智能体-环境共同进化**角度，归纳出智能体进化的四种路径：记忆中心的经验进化、编排中心的工作流进化、轨迹中心的离线进化和探索中心的在线进化；以及环境进化的三种范式：神经驱动、难度驱动和规模驱动。

**关键结果**：分类框架总结了数十种环境实例，揭示出环境设计模式；合成范式对比了符号与神经方案的适用边界；共同进化分析展示了四种路径在真实任务中的增益，并指出未来方向（环境即服务、多智能体环境、神经符号环境）。
