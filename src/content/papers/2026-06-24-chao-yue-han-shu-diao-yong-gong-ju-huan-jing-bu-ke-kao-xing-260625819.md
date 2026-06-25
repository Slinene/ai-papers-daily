---
title: 'Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment
  Unreliability'
title_zh: 超越函数调用：工具环境不可靠性下智能体基准测试
authors:
- Yang Tian
- Zhengpeng Shi
- Bo Zhao
affiliations:
- Shanghai Jiao Tong University
arxiv_id: '2606.25819'
url: https://arxiv.org/abs/2606.25819
pdf_url: https://arxiv.org/pdf/2606.25819
published: '2026-06-24'
collected: '2026-06-25'
category: Agent
direction: Agent 工具使用可靠性评估与恢复分析
tags:
- Tool-Using Agents
- Benchmark
- Reliability
- LLM
- Function Calling
- Failure Recovery
one_liner: 提出ToolBench-X基准，系统注入五种可恢复工具风险，揭示Agent在不可靠环境中可靠性大幅下降，恢复能力不足。
practical_value: '- 构建Agent时需模拟工具不可靠性进行鲁棒性测试：工具描述漂移、调用失败、输出异常等在真实API、数据库查询中常见，应设计恢复路径（重试、回退、交叉验证）。

  - 评估Agent应超越单步函数调用准确率，关注端到端任务完成率，尤其考虑并行与混合工作流的可靠性。

  - 实验表明仅扩大推理预算(test-time scaling)对解决工具不可靠性增益有限，更有效的是增强Agent的故障诊断与恢复逻辑，例如提供恢复提示(hints)能挽救大量失败任务。

  - 在搜索推荐等涉及多工具调用的场景（商品API、用户画像、库存查询），可参考ToolBench-X设计结构化故障注入测试集，验证Agent在部分依赖失效时的降级方案。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：当前LLM工具使用基准假设工具环境洁净可靠，忽略真实世界中常见的规范变更、调用错误、执行失败、输出漂移及跨源冲突等风险。即使Agent能正确调用函数，环境不可靠也会导致任务失败，亟需评估其可靠性与恢复能力。

**方法**：提出ToolBench‑X，包含多领域多步可执行任务，覆盖顺序、并行和混合工作流。在干净工具基础上，注入五种结构化风险：`Specification Drift`（工具描述过时）、`Invocation Error`（调用参数错误）、`Execution Failure`（执行超时/失败）、`Output Drift`（输出格式/内容异常）、`Cross-source Conflict`（多方信息矛盾）。每个注入实例保留至少一条有效恢复路径（重试、回退、验证、交叉校验），并提供确定性答案用于自动评估。

**关键结果**：可靠工具下表现优异的Agent，在注入可恢复风险后成功率大幅下降（如部分Agent从90%+降至不足50%）。失败主因不是调用次数或推理预算，而是危险诊断与恢复能力有限。提供针对性恢复提示可显著挽救失败任务，而单纯增加test-time scaling收益有限。这要求工具使用评估必须从函数调用准确性转向不可靠环境下的任务完成能力。
