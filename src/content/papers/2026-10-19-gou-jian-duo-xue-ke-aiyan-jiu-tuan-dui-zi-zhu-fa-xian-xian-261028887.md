---
title: Building AI Research Teams for Autonomous Discovery of Linear Attention Architectures
title_zh: 构建多学科AI研究团队自主发现线性注意力架构
authors:
- Yujian Liu
- Li An
- Zelin He
- Jacob Helwig
- Jiabao Ji
- Rohit Jain
- Siyu Zhu
- Shiyu Chang
affiliations:
- UC Santa Barbara
- Pennsylvania State University
- LinkedIn
arxiv_id: '2610.28887'
url: https://arxiv.org/abs/2610.28887
pdf_url: https://arxiv.org/pdf/2610.28887
published: '2026-10-19'
collected: '2026-10-22'
category: MultiAgent
direction: 多智能体协作自主架构搜索
tags:
- MultiAgent
- Autonomous Discovery
- Linear Attention
- Architecture Search
- LLM
- Agent
one_liner: 通过不同学科背景、私有历史与自适应分配组织多智能体团队，自主搜索出优于GDN2的线性注意力架构
practical_value: '- 在推荐/广告模型结构搜索中，可借鉴“多学科背景Agent团队”设计，让不同Agent从召回、排序、多任务、效率等视角提出正交的架构修改，避免群体思维陷入局部最优。

  - “私有研究历史”机制可迁移到A/B实验知识管理：每个实验Owner保留独立的假设与失败记录，仅共享实验结果，防止过早收敛到主流方案。

  - 自适应分配研究机会（而非均匀轮询）适合实验预算有限的场景：根据近期收益动态调整各Agent的探索资源，把更多算力给有潜力的方向。

  - 对于线性注意力等新型高效模块，业务侧可以低成本在小规模（如150M参数）用该团队框架快速筛选候选，再扩展到线上模型，节省大规模训练开销。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：AI agent 已能独立提出想法、改代码、跑实验，但单一agent容易陷入设计空间的局部最优。受多学科团队协作启发，提出用不同学科背景的AI研究员组成团队，通过正交探索突破瓶颈，同时解决有限实验预算下的探索-利用平衡问题。

**方法关键点**：构建一组持续存在的AI研究员，每个agent被赋予不同学科基础（如数学、物理、生物启发等）；每个agent维护私有研究历史，只共享实验证据（避免重复尝试已知失败方向）；通过自适应分配机制（而非均匀轮询）选择哪个agent获得下一轮实验机会，动态权衡深耕与探索。团队在150M参数下搜索线性注意力架构，然后将最强发现扩展到1.3B参数。

**关键结果**：在1.3B规模下，发现的架构在语言建模、常识推理、合成与真实检索任务上均优于基线GDN2。消融实验表明：移除学科背景导致搜索早期停滞；移除私有历史，即便共享相同证据，agent进展更差；均匀选择在相同预算下不如自适应分配。追踪发现过程可见各agent运用本领域原理互相改进想法，证明组织要素对持续自主发现至关重要。
