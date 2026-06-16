---
title: 'Agent trajectories as programs: fingerprinting and programming coding-agent
  behavior'
title_zh: 将智能体轨迹视为程序：编码智能体行为的指纹识别与编程
authors:
- Hamidah Oderinwale
arxiv_id: '2606.16988'
url: https://arxiv.org/abs/2606.16988
pdf_url: https://arxiv.org/pdf/2606.16988
published: '2026-06-15'
collected: '2026-06-16'
category: Agent
direction: Agent行为指纹识别与过程审计
tags:
- agent trajectories
- fingerprinting
- coding agents
- procedural representation
- ProcGrep
- SWE-bench
one_liner: 通过过程表征压缩轨迹，以85.7%准确率识别编码智能体指纹，并构建过程审计库ProcGrep
practical_value: '- 在多Agent系统中，利用行为指纹进行任务感知的模型路由，将特定请求分发给最适配的Agent，优化系统效率与效果

  - 在推荐/搜索Agent中，使用ProcGrep审计Agent解决问题时的内部轨迹，监控其行为是否符合预期模式，及时发现异常或退化的步骤

  - 借鉴过程表征压缩方法，对Agent交互历史进行结构化搜索，替代昂贵的LLM回溯，提升Agent记忆检索的确定性和速度

  - 比较不同模型或不同提示策略产生的轨迹指纹，量化差异，指导模型选型与微调，尤其当蒸馏模型的行为趋向教师时可提前评估风险'
score: 7
source: arxiv-cs.LG
depth: abstract
---

## 动机
基准分数只衡量智能体完成任务的结果，无法揭示其底层的问题解决策略。随着编码智能体日益普及，理解“如何做”变得与“做对了什么”同等重要，尤其在模型饱和基准时。为此，需要一种过程视角来比较不同智能体在多样任务下的行为模式。

## 方法
提出一种将智能体轨迹重构为紧凑程序化表征的技术，通过自适应词汇归纳对原始事件序列进行压缩，剔除表面细节同时保留各模型的独特行为习惯（即指纹）。该表征既具有表达力，又能最大限度降低表面变异。使用这些表征对10个编码智能体的轨迹（来自SWE-Bench）进行相似度分析，并通过探查任务验证指纹的可辨识性。同时发布ProcGrep库，以声明式语法对轨迹进行过程级审计和搜索。

## 结果
指纹探查准确率达85.7%，表明智能体确实具备可区分的程序性行为习惯。相似度分析显示，同时期发布的模型以及蒸馏对（教师-学生）的行为最为接近，蒸馏对之间的JS散度仅0.25，约为其他模型对间距的一半。ProcGrep在搜索历史事件时，效率与准确率均优于LLM方法，为确定性、可编程的轨迹审计提供了工程化工具。
