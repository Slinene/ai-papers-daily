---
title: 'Lean4Agent: Formal Modeling and Verification for Agent Workflow and Trajectory'
title_zh: Lean4Agent：用依赖类型形式化建模与验证 Agent 工作流及轨迹
authors:
- Ruida Wang
- Jerry Huang
- Pengcheng Wang
- Xuanqing Liu
- Luyang Kong
- Tong Zhang
affiliations:
- University of Illinois Urbana-Champaign
- Independent researcher
arxiv_id: '2606.06523'
url: https://arxiv.org/abs/2606.06523
pdf_url: https://arxiv.org/pdf/2606.06523
published: '2026-06-01'
collected: '2026-06-09'
category: Agent
direction: Agent 工作流的形式化验证与自动优化
tags:
- Formal Verification
- Lean4
- Agent Workflow
- Trajectory Verification
- Dependent Types
- Auto-Evolution
one_liner: 首个用依赖类型语言 Lean4 形式化验证 Agent 工作流语义一致性并自动改进的框架
practical_value: '- 多步 Agent 工作流（如电商客服自动处理、推荐系统规划）可引入形式化验证，用类型系统约束步骤间的语义一致性，避免执行时逻辑矛盾导致线上故障。

  - 轨迹级别的失败定位思想可直接用于业务 Agent 的调试：记录每步动作与状态，通过预定义的规格自动检测偏差，快速找到出错的子任务。

  - LeanEvolve 的“验证反馈→修订工作流”闭环可参考，对 Agent 流程做 A/B 测试时，自动利用失败案例生成修正版本，减少人工调优成本。

  - 形式化库 FormalAgentLib 的设计模式（显式假设、可扩展验证规则）可迁移到业务编排框架中，实现可复用、可证明的 Agent 动作规约。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：当前 LLM Agent 系统缺乏形式化方法对多步工作流与执行轨迹进行规约、验证和调试，如同数学中自然语言的歧义性问题。为此，论文提出用依赖类型形式语言 Lean4 来建模和验证 Agent 行为。

**方法**：构建 Lean4Agent 框架，包含两个核心部分：
1. **FormalAgentLib**：基于 Lean4 的可扩展库，在显式假设下形式化建模 Agent 工作流并验证语义一致性，同时支持从轨迹中定位执行期失败。
2. **LeanEvolve**：利用 FormalAgentLib 的验证结果自动修订工作流，提升其能力。

**实验结果**：在 SWE-Bench-Verified 困难子集和 ELAIP-Bench 子集上，使用 5 款主流 LLM 测试，验证通过的工作流比未通过的平均高出 **11.94%** 性能；LeanEvolve 进一步将 SWE 任务性能平均提升 **7.47%**，证明形式化验证与自动改进的可观收益。
