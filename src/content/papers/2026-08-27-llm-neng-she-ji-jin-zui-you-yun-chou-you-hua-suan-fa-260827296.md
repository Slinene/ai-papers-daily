---
title: LLMs Can Design Near-Optimal OR Algorithms
title_zh: LLM 能设计近最优运筹优化算法
authors:
- Jackie Baek
arxiv_id: '2608.27296'
url: https://arxiv.org/abs/2608.27296
pdf_url: https://arxiv.org/pdf/2608.27296
published: '2026-08-27'
collected: '2026-08-29'
category: LLM
direction: LLM 算法设计 · 运筹优化
tags:
- LLM
- algorithm design
- operations research
- code generation
- optimization
- sandbox
one_liner: 未微调的 frontier LLM 在库存、排队网络、品类优化上生成算法，匹配或超过现有专用方法
practical_value: '- 在电商/广告中，品类优化（assortment）、库存分配、预算 pacing、实时请求路由等定义清晰的约束优化问题，可快速用
  frontier LLM + Python sandbox 生成策略算法作为 baseline，再与手写规则或求解器对比；固定 compute budget 可控制线上可行性。

  - 优先采用 Level 2 方式：让 LLM 只根据问题类描述和参数范围输出「参数→决策」的算法函数，而不是逐实例求解；这样得到的策略可直接部署到实时系统，并在未见参数上做离线评估。

  - Prompt 无需复杂调优：简单描述问题、目标、约束和可用工具，LLM 即可写出可执行代码；这对快速原型验证、A/B 测试前的候选策略生成很实用。

  - 注意：该方法适用于目标函数和约束都能明确写出的优化场景；对依赖隐式反馈或需要从数据中学习的推荐排序任务，LLM 生成算法可能只能解决局部优化子问题，仍需与
  ML 模型结合。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：运筹优化问题通常依赖专家设计专用算法，LLM 是否能自动生成近最优算法？

方法：在库存控制、排队网络控制、品类优化三个问题上，测试两种使用层级：Level 1 给定单个实例返回解；Level 2 仅给定问题类描述和参数范围，返回一个从参数到解的算法。使用未调优 prompt，LLM 可调用 Python sandbox 与固定计算预算。

结果：最强模型 gpt-5.6-sol 在几乎所有评估实例上匹配或超过现有最佳方法；Level 2 返回的算法在未见实例上仍保持优势；模型能力在不到 8 个月内快速提升。

结论：对于定义良好的 OR 问题，单次未调优 LLM 查询即可产生与专用方法竞争的算法，frontier LLM 可作为严肃的经验基线。
