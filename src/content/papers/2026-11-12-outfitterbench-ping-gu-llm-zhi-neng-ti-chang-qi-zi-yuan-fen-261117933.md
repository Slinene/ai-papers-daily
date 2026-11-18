---
title: 'OutfitterBench: Evaluating LLM Agents on Long-Horizon Resource Allocation
  and Commitment Coordination'
title_zh: OutfitterBench：评估 LLM 智能体长期资源分配与承诺协调
authors:
- Jie Huang
- Yuecheng Hong
- Yao Chen
- Shengding Jiao
- Xudong Liu
- Qiang Ye
affiliations:
- Harbin Institute of Technology
- Peking University
- University of Science and Technology of China
arxiv_id: '2611.17933'
url: https://arxiv.org/abs/2611.17933
pdf_url: https://arxiv.org/pdf/2611.17933
published: '2026-11-12'
collected: '2026-11-18'
category: Eval
direction: LLM Agent 长程规划与资源分配评估
tags:
- LLM Agent
- Long-Horizon
- Resource Allocation
- Benchmark
- Commitment Coordination
- Planning
one_liner: 提出 OutfitterBench 基准，多数 LLM 代理在 200 天租赁业务中不及规则基线，仅领先代理稳定超越
practical_value: '- 在业务 Agent 中显式建模承诺可行性：维护资源可用性日历与承诺列表，每次决策前验证新承诺与现有义务无冲突，避免 LLM
  不一致。

  - 关键场景采用规则基线兜底：LLM 负责排序/建议，规则执行硬约束（库存、预算上限），可提升长期规划稳定性。

  - 引入机会成本评估：要求 LLM 在分配资源时输出放弃的替代收益，防止低回报承诺或延迟再分配。

  - 轨迹分析提示：外部约束验证器和记忆模块可纠正 LLM 常见失误，如不一致约束应用和决策冲突。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：长期运行 Agent 的决策会创造未来约束——承诺有限资源形成义务并排除后续机会。现有基准多关注持续运营，但未充分评估 Agent 如何保持承诺可行并随机会变化重新评估资源价值。

**方法关键点**：OutfitterBench 模拟户外装备租赁业务 200 天，包含 46 个产品、约 1100 个预订请求，固定资本上限下预订与 walk-in 需求竞争可重用设备。Agent 需采购、接受/拒绝预订、管理设备可用性，同时维持承诺可行并优化收益。设置规则基线对照。

**关键结果**：测试 7 个前沿 LLM，多个代理表现低于简单规则基线，仅领先代理稳定超越。轨迹分析显示：部分代理不一致应用已知约束，做出与既有承诺冲突的决策；履行更可靠的代理仍可能从承诺中获得低回报或延迟资源再分配；领先代理更好连接准备与经济选择，但也错过更有利可图的资产使用机会。代码已公开。
