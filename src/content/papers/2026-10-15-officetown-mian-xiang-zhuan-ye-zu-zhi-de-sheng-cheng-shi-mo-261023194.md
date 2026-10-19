---
title: 'OfficeTown: Generative Organizations for Evolving Agent Intelligence'
title_zh: OfficeTown：面向专业组织的生成式模拟与智能体演进框架
authors:
- Hongchen Wei
- Daohong Ying
- Zhi Hong
- Aidan Wu
- Bei Liu
- Ruichun Ma
- Yifan Yang
- Qi Dai
- Kai Qiu
- Rui Xu
affiliations:
- Wuhan University
- University of California San Diego
- South China University of Technology
- Cornell University
- Microsoft Research Asia
arxiv_id: '2610.23194'
url: https://arxiv.org/abs/2610.23194
pdf_url: https://arxiv.org/pdf/2610.23194
published: '2026-10-15'
collected: '2026-10-19'
category: MultiAgent
direction: 生成式组织模拟 · 多智能体协作评估与训练
tags:
- Multi-Agent
- Agent Benchmark
- Simulation
- SFT
- On-policy Distillation
- Professional Work
one_liner: 用生成式组织模拟持续产生专业任务、上下文与反馈，构建 406 任务基准并训练提升 Qwen3.5-9B
practical_value: '- 用自然语言组织描述自动生成任务流、工件、权限和反馈，可迁移到电商运营/广告投放/客服等场景，低成本构建多智能体训练与评估环境。

  - Principal–assistant 架构值得借鉴：主 Agent 拆解需求、委派边界子任务并审查交付物，子 Agent 只可见权限内上下文，适合搜索推荐链路中把意图理解、召回、排序、文案生成拆给不同子
  Agent。

  - 持久化 artifacts、decisions、unresolved matters 相当于跨任务长期记忆，可提升多轮推荐/搜索 Agent 对用户历史、活动状态和未决问题的利用效率。

  - 模拟数据 + SFT/on-policy distillation 能有效提升外部专业工作基准，业务上可批量生成带评审反馈的搜索推荐 Agent 轨迹，蒸馏到中小模型，降低线上成本。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有专业工作基准通常把任务当孤立实例，忽视组织内跨任务积累的材料、决策和反馈，也不建模职责与权限。

方法关键点：OfficeTown 从自然语言组织描述出发，初始化一个由成员、职责、权限构成的组织；成员协调工作，将边界性子任务委派给助理 Agent，并审查交付物。工件、决策和未决问题持久化并进入后续任务上下文。基于该框架构建 OfficeTown Bench，覆盖 23 个模拟组织、8 个专业领域、406 项任务、4,836 条评估标准，评审反馈融入领域专家意见。用该数据做 SFT 和 on-policy distillation 训练 Qwen3.5-9B，并在外部专业工作基准 GDPval 上评估；同时比较 principal–assistant harness 与单 Agent/多 Agent 基线。

关键结果：前沿模型在 OfficeTown Bench 上仍有明显提升空间；OfficeTown 数据训练后，Qwen3.5-9B 在外部专业工作基准上显著提升，包括 GDPval；principal–assistant harness 得分高于单智能体和多智能体基线。
