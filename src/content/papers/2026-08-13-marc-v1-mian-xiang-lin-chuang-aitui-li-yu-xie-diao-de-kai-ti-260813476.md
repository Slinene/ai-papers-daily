---
title: 'MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and
  Coordination'
title_zh: MARC v1：面向临床AI推理与协调的开源多智能体框架
authors:
- Saisha Shetty
- Satvik Tripathi
- Austin Lin
- Colin Zhao
- Theodore Kim
- Don Enwerem
- Jacinta Arnold
- Shahriar Faghani
- Tessa S Cook
affiliations:
- College of Engineering, University of California, Davis
- Perelman School of Medicine, University of Pennsylvania
- School of Engineering and Applied Science, University of Pennsylvania
- College of Computing and Informatics, Drexel University
- UC Davis Graduate School of Management, Davis, CA
arxiv_id: '2608.13476'
url: https://arxiv.org/abs/2608.13476
pdf_url: https://arxiv.org/pdf/2608.13476
published: '2026-08-13'
collected: '2026-08-15'
category: MultiAgent
direction: 多智能体协作推理与自动提示生成
tags:
- MultiAgent
- Clinical AI
- Orchestration
- Decomposer
- Open-source
- LLM reasoning
one_liner: 开源多智能体框架MARC，用确定性角色编排替代单体LLM提示，实现可追踪的临床推理与自动提示生成
practical_value: '- 角色化多智能体流水线：将复杂推理任务拆解为提取、推理、生成、评估四个阶段，每个阶段独立Agent，便于错误定位和迭代。电商搜索/推荐中的query解析、意图理解、商品属性抽取、客服文案生成等长链路任务可直接套用这种确定性编排。

  - Decomposer模块：用自然语言任务描述自动生成各Agent的prompt，大幅降低prompt工程成本，适合业务快速扩展新场景或调整流程。

  - YAML配置+模型无关+本地CPU部署：架构上将流程与模型解耦，支持灵活切换底层LLM（API或本地模型），减少代码改动，便于算法团队快速实验和部署。

  - 显式上下文传递与可追踪中间输出：多步骤生成任务（如推荐理由、广告创意）中，中间输出可审计、可归因，有利于线上效果分析和调试。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：单体LLM提示在临床推理中存在可解释性差、失败难归因的问题，尤其在多步骤临床问答场景中，需要更结构化的协作推理框架。

**方法关键点**：
MARC（Multi-Agent Reasoning and Coordination）框架用确定性多智能体编排取代单体LLM提示。系统协调四类角色专业化Agent：extraction、reasoning、answer generation、evaluation，Agent间通过显式上下文传递和可追踪中间输出衔接，支持阶段级失败归因。
引入Decomposer模块，从一段自然语言任务描述自动生成各Agent的专用prompt，消除手动prompt engineering。
框架完全通过YAML配置，无需代码修改，支持API和本地CPU兼容部署，模型无关且可解释，面向非编程背景的临床领域专家。

**关键结果数字**：论文摘要未报告具体基准测试分数，主要贡献为开源框架本身，代码公开于GitHub。
