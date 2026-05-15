---
title: 'Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution,
  and Self-Evolution in LLM-based Multi-Agent Systems'
title_zh: 超越个体智能：基于LLM的多智能体系统协作、失败归因与自我演化综述
authors:
- Shihao Qi
- Jie Ma
- Rui Xing
- Wei Guo
- Xiao Huang
- Zhitao Gao
- Jianhao Deng
- Jun Liu
- Lingling Zhang
- Bifan Wei
affiliations:
- 西安交通大学
- 联想AI技术中心
- 华中师范大学
- 悉尼大学
arxiv_id: '2605.14892'
url: https://arxiv.org/abs/2605.14892
pdf_url: https://arxiv.org/pdf/2605.14892
published: '2026-05-13'
collected: '2026-05-15'
category: Agent
tags:
- LLM
- Multi-agent
- Collaboration
- Failure Attribution
- Self-Evolution
- Survey
one_liner: 提出LIFE框架将单智能体能力、多智能体协作、失败归因与自我演化统一为因果链环，填补了闭环诊断与自主改进的综述空白
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：基于LLM的智能体虽在推理、规划、工具使用上进展显著，但多智能体协作中错误传播与诊断困难日益突出，现有综述割裂地讨论单智能体能力、协作或自我演化，缺乏从诊断到改进的统一闭环视角。因此，亟需一个整合的框架来连接协作、归因与演化，推动多智能体系统向自主改进的集体智能发展。

**方法关键点**
- 提出LIFE四阶段因果链：①奠定能力基础（Lay foundation）——个体智能体推理、记忆、规划、工具使用；②整合协作（Integrate collaboration）——角色、通信、编排、交互模式；③发现故障（Find faults）——失败分类体系与数据驱动、约束引导、因果推断三类归因方法；④自动演化（Evolve）——智能体级、系统级和元演化三层自改进设计空间。
- 系统梳理各阶段技术：推理的输入增强/过程搜索/输出调控，记忆的形成与维护，规划的分解与搜索，工具使用的获取与泛化；协作的角色分配、通信拓扑、信息流；归因的故障溯源与因果链重建；演化的动态优化策略。
- 强调跨阶段依赖：归因结果可直接驱动协作结构调整，协作模式又塑造了可观测的失败类型，形成闭环回路。

**关键结果数字**
本综述覆盖超过200篇论文，建立了从单智能体到多智能体自我演化的完整技术分类，整理了多个对比表格（如推理增强方法、记忆系统、规划策略），并公开维护了GitHub资源库，提供结构化文献、可视化分类，为未来的跨阶段研究议程提供了概念地图。
