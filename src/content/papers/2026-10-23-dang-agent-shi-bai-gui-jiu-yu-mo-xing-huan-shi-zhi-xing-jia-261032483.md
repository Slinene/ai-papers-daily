---
title: 'When Agents Fail: Model or Harness--Who''s to Blame?'
title_zh: 当 Agent 失败：归咎于模型还是执行框架？
authors:
- Shao Zhang
- Hangfan Zhang
- Yuanyuan Shi
- Hao Li
- Min-Le Su
- Kangcong Li
- Jingping Wang
- Chunjiang Mu
- Chen Zhang
- Yang Chen
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2610.32483'
url: https://arxiv.org/abs/2610.32483
pdf_url: https://arxiv.org/pdf/2610.32483
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: Agent 执行框架评估与匹配
tags:
- LLM Agents
- Harness Evaluation
- Model-Harness Fit
- Token Efficiency
- Benchmarking
one_liner: 提出模型-执行框架匹配度评估框架，发现无单一最佳组合，OpenCode 跨模型最稳
practical_value: '- 选型 Agent 执行框架时，不要只看最终任务分数，建议同时监控 VCR（有效完成率）和 Token Load，避免高分数掩盖高失败率或高
  token 浪费。

  - 不同模型适配不同 harness：内部构建 Agent 平台时，可以为每个主力模型分别评测 harness 的 Model-Harness Fit，而不是统一采用一个“最佳”框架。

  - 在电商搜索/推荐 Agent 场景中，大量交互式工具调用和长上下文任务会放大模型-框架不匹配问题，可引入 Interaction Residuals 定位具体哪个组合在哪些步骤频繁失败。

  - Token Load 包含失败尝试，适合作为成本控制指标：当框架重试机制激进时，即使任务最终成功，也可能消耗数倍 token，影响线上性价比。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM Agent 性能是底层模型与执行框架（harness）共同作用的结果，但现有基准通常只给最终任务得分，无法区分失败来自模型能力不足还是框架设计缺陷。

**方法关键点**：提出五维评估框架：① VCR（Valid Completion Rate），衡量 Agent 能否正常结束并产出可评估结果，不关心任务正确性；② Model-Harness Fit，衡量特定模型在某框架下通过有效完成支持任务达成的程度；③ Cross-Model Fit，框架跨模型的整体适用性；④ Interaction Residuals，捕捉配对特有的执行强弱项；⑤ Token Load，包括失败尝试在内的 token 总开销。在 6 个基准（覆盖上下文管理、工具使用、长程规划、多模态、artifact 交接）、4 个通用框架（OpenCode、Codex CLI、Pi CLI、DeepAgents）+ 2 个 native 组合上，共 111 个评估设置、52,168 条轨迹。

**关键结果**：框架排名随模型和基准变化；任务性能与有效完成率可能偏好不同配对；相似任务分数背后执行画像差异显著。OpenCode 在跨模型性能上排第一；DeepSeek V4 Flash Preview 在共享四基准上平均 VCR 最高。
