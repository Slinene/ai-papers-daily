---
title: 'Chronicle: Cut-Point Replay for Regression Testing of LLM Agents'
title_zh: Chronicle：LLM Agent 回归测试的切点回放
authors:
- Tisha Chawla
- Susheem Koul
affiliations:
- Microsoft
arxiv_id: '2609.20625'
url: https://arxiv.org/abs/2609.20625
pdf_url: https://arxiv.org/pdf/2609.20625
published: '2026-09-17'
collected: '2026-09-19'
category: Eval
direction: LLM Agent 回归测试与录制回放
tags:
- record-replay
- regression-testing
- non-determinism
- LLM agents
- CI-CD
one_liner: 通过切点回放把 LLM agent 失败运行转成 CI 回归测试，兼顾录制的可复现与新代码实跑
practical_value: '- 把 LLM agent 运行中的模型调用、工具读取外部状态等非确定性边界作为 cut-point 录制，之后可部分回放、部分实跑新代码，快速把线上事故变成
  CI 回归测试。

  - 录制开销很低（23μs/边界），可在电商/广告 agent 的关键工作流中在线开启录制，积累回归 case，不影响性能。

  - 对高风险工具（退款、出价、商品发布等）做 guard/安全断言时，cut-point replay 比全 stub 更能捕获真正的不安全变更，避免测试假阴性。

  - 业务中可先离线模拟模型边界，用 replay 验证修复，再逐步接入 CI，减少对 LLM 调用的依赖和成本。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM agent 的非确定性导致失败难以复现：模型推理不可按位复现，工具读取的外部状态会变化，多步 trajectory 也很难重复。现有 record-and-replay 工具只用于追踪或评分，无法把录制事件变成针对代码变更的回归测试。

**方法关键点**：Chronicle 在 agent 运行的非确定性边界处录制 immutable envelopes，支持按边界回放。核心操作 cut-point replay 选择一部分边界从录制中回放，互补部分用新代码实跑，从而把历史失败事件转化为可在 CI 运行的回归测试。

**关键结果**：在 6 个录制失败基准上，录制每跨边界仅增加 23 μs（占假设 300 ms 模型调用的 0.008%）；全回放零模型调用，20 次重复 bit-stable；cut-point 测试在 faulty code 上全部失败，在 guarded 和 benign changes 上通过；在 guarded tools 的 mutation study 中，cut-point tests 捕获所有让不安全 action 通过的 mutant，而全 stub baseline 捕获 0 个。
