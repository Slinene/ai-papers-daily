---
title: 'Longtail-SWE: High-Quality SWE Tasks for Underrepresented Languages'
title_zh: Longtail-SWE：面向长尾编程语言的软件工程任务基准
authors:
- Vladimir Dobrovolskii
- Ibragim Badertdinov
- Alexander Golubev
affiliations:
- Nebius
arxiv_id: '2611.10304'
url: https://arxiv.org/abs/2611.10304
pdf_url: https://arxiv.org/pdf/2611.10304
published: '2026-11-06'
collected: '2026-11-11'
category: Eval
direction: 多语言 SWE 基准与评测修复
tags:
- SWE-bench
- Code Agents
- Benchmark
- Multilingual
- Test Repair
- Longtail Languages
one_liner: 构建跨13种长尾语言的202个SWE任务，用solver-judge-repairer修正测试与描述并开放全套评估资源
practical_value: '- 构建离线评估集时，可复用 solver-judge-repairer 思路：不只凭单次 pass/fail 过滤任务，而把模型执行轨迹和测试结果交给
  judge 联合审阅，自动修正误判合法方案或误接受错误方案的测试，能显著提升评测集信噪比。

  - 对长尾/多场景 Agent 评估，应分层报告一致性与资源消耗，而不是只看单一成功率；电商搜索推荐里的多类目、小流量场景同样需要这种稳定性视角。

  - 发布完整环境、轨迹和 easier 子集的做法值得借鉴：内部建设 agent 评测集时保留难度分层，便于低成本迭代小模型和快速回归。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有仓库级代码基准主要集中在 Python 等主流语言，许多长尾语言生态缺乏可执行、可靠评估的 issue 解决任务；且从历史 issue/PR 构建任务时，候选任务常因描述歧义或测试缺陷被丢弃，限制了代码 Agent 在不同工具链和开发实践下的能力证据。

**方法关键点**：提出 Longtail-SWE，包含 202 个 issue 解决任务，覆盖 Clojure、Dart、Elixir、Erlang、F#、Haskell、Julia、Kotlin、Lua、OCaml、R、Scala、Swift 共 13 种语言。构建流程采用 solver–judge–repairer 管线：先让 solver 尝试候选任务；再由 judge 结合 solver 的执行轨迹与测试结果进行审查，指导修正测试和任务描述。修正目标是消除两类错误：拒绝合法替代实现的测试，以及接受错误解决方案的测试，同时保留任务挑战性和原始需求。

**关键结果数字**：评估 9 种模型配置（含前沿模型），分析任务解决表现、重复尝试一致性与资源消耗；除基准实例和可执行环境外，还发布完整构建/评估工具、agent 轨迹，以及额外的一组更简单任务，用于支持较小模型的评估。
