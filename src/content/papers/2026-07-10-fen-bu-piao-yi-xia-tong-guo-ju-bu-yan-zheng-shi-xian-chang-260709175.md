---
title: Scoped Verification for Reliable Long-Horizon Agentic Context Evolution under
  Distribution Shift
title_zh: 分布漂移下通过局部验证实现长程智能体上下文可靠演化
authors:
- Dan C. Hsu
- Luke Lu
affiliations:
- RedMind Research, San Francisco, CA, USA
- National Taiwan University, Taipei, Taiwan
arxiv_id: '2607.09175'
url: https://arxiv.org/abs/2607.09175
pdf_url: https://arxiv.org/pdf/2607.09175
published: '2026-07-10'
collected: '2026-07-13'
category: Agent
direction: Agent 持久指令的结构化可靠演化
tags:
- Agentic Context
- Persistent Instruction
- Typed Semantic Graph
- Local Verification
- Distribution Shift
- GRACE
one_liner: 提出图正则化上下文演化(GRACE)，将指令表示为类型化语义图并局部验证更新，使长程Agent可靠性提升7倍
practical_value: '- 将系统指令/策略用类型化图（节点+关系）维护，取代扁平长文本，便于增量更新和冲突检测；可适用于推荐Agent的规则积累

  - 采用局部邻域验证：修改指令时只检查直接关联节点的约束，避免全局重审，降低校验成本

  - 图更新后自动生成文本指令 checkpoint，保持部署兼容性；工程上可作为指令管理中间层

  - 使用 pass^k 等严格通过率指标评估 Agent 在分布漂移下的可靠性，比简单成功率更能暴露脆弱性'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：部署的LLM-Agent依赖可变的外部“代理上下文”，其中持久系统指令会从运行经验中持续更新。长程演化下，扁平文本指令不断累积、交互，验证其正确性和一致性变得极其困难，导致Agent在分布漂移中可靠性崩溃。

**方法关键点**：提出GRACE——将持久指令维护为**类型化语义图**，节点和边都有明确类型。当产生指令更新时，仅在**修改节点的局部类型邻域内验证**一致性，确保不引入冲突。验证通过的图更新再被**重建为文本指令增量编辑**，生成可部署的检查点。整个过程形成“图验证→文本重建”闭环，使验证局部化、可控。

**关键结果数字**：在电信Agent任务（改编自τ²-bench）受控分布漂移下，用Gemini 2.5 Flash作为基座，严格可靠性指标pass³从零样本的**0.091**提升至最终检查点的**0.673±0.136**（5次独立重复）。对比Gemini 3.1 Pro零样本参考0.242，扁平文本基线仅0.191±0.051。GRACE在提升可靠性的同时，也证明了结构化基板和局部验证对长程上下文演化的必要性。
