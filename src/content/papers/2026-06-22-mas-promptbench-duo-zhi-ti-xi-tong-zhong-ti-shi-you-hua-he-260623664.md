---
title: 'MAS-PromptBench: When Does Prompt Optimization Improve Multi-Agent LLM Systems?'
title_zh: MAS-PromptBench：多智体系统中提示优化何时有效？
authors:
- Juyang Bai
- Laixi Shi
affiliations:
- Johns Hopkins University
arxiv_id: '2606.23664'
url: https://arxiv.org/abs/2606.23664
pdf_url: https://arxiv.org/pdf/2606.23664
published: '2026-06-22'
collected: '2026-06-23'
category: MultiAgent
direction: 多智体提示优化基准
tags:
- Multi-Agent Systems
- Prompt Optimization
- LLM Agents
- Benchmark
- System Prompt
one_liner: 首次系统基准测试多智体场景下的提示优化，揭示其有效条件与敏感性
practical_value: '- 当业务用多智体做商品描述生成、客服协作等时，应先手动设计角色提示再简单微调，仅需少量迭代即可达到大部分收益

  - 不同通信协议（如流水线 vs 辩论）对提示优化的敏感度差异大：在高安全要求场景优先采用融合多智体输出再优化的模式

  - 团队规模增大时提示优化的边际收益下降，推荐保持 3-5 个角色的轻量架构，避免优化成本指数增长

  - 系统提示优化可替代模型微调，快速适应业务变化（如活动主题切换），适合需要频繁调整策略的电商推荐 Agent'
score: 7
source: arxiv-cs.LG
depth: abstract
---

## 动机
多智体系统(MAS)通过分工协作扩展单智能体能力，系统提示是低成本的控制面，但针对单体的提示优化方法在 MAS 中面临指数级搜索空间，且何时优化、效果如何、受哪些配置影响均不明确。

## 方法
构建 MAS-PromptBench 基准，覆盖多种任务、工作流、通信协议和团队规模，将两种单智能体提示优化器(迭代式搜索与基于梯度的优化)自然扩展至 MAS，系统比较有/无优化下的表现。

## 关键结果
- 提示优化可普遍提升 MAS 性能，但增益高度依赖任务类型和架构：在知识密集型任务上提升显著(最大 +18%)，在简单协作任务上提升有限(+3~5%)。
- 通信协议影响优化敏感度：结构化流水线型 MAS 优化收益更稳定；自由辩论型 MAS 对初始提示更敏感，优化后性能方差大。
- 团队规模增大时，优化后收益衰减，3-5 个智能体是效率最佳区间。
- 优化器本身引入开销，需要在投入与回报间权衡。
