---
title: 'StateM: Reaching 95.3% Raw Accuracy, or a \$15 Frontier Run, on Terminal-Bench
  2.1 via Harness Scaling'
title_zh: StateM：用 Harness Scaling 在 Terminal-Bench 2.1 达 95.3% / $15 前沿运行
authors:
- Ziheng Qin
- Yaxin Lu
- Zhangyang Atlas Wang
- Kai Wang
arxiv_id: '2608.15089'
url: https://arxiv.org/abs/2608.15089
pdf_url: https://arxiv.org/pdf/2608.15089
published: '2026-08-14'
collected: '2026-08-19'
category: Agent
direction: Agent harness 扩展与状态机执行控制
tags:
- Harness Scaling
- State Machine
- Agent Runtime
- Long-horizon Agent
- Procedural Memory
- Terminal-Bench
one_liner: StateM 用状态机 runbook 外部化执行控制，不改权重，Terminal-Bench 2.1 达 95.28%，DeepSeek $15
  达 88.8%
practical_value: '- 将长流程 Agent（如生成式推荐、商品投放、数据分析 pipeline）编码为 YAML 状态机 runbook，每个阶段设
  exit checks（离线评估分、数据完整性检查、配置校验），可显著减少 agent 提前退出或跳过必要步骤。

  - 采用“状态即上下文与契约边界”设计：进入新阶段时刷新 phase-local 指令与进度摘要，避免长轨迹导致控制信号稀释；离开阶段必须通过可执行 command/predicate
  校验，而不是 agent 自述完成。适合生成-验证-修复-发布这类闭环。

  - 建立失败驱动的 harness 迭代流程：把每次失败归类为缺失上下文、无效转换、弱检查、提前交接、恢复失败等，将通用修复固化为 runbook 版本，不改模型权重。这能把重复踩过的坑沉淀为可执行约束，并保持模型不变。

  - 跨模型迁移时，同一模型家族可冻结 runbook 直接复用；跨 provider 需按新模型适配 practices，但可保留 runbook 结构与开发原则。可以尝试用便宜模型
  + 定制 harness 逼近昂贵模型，降低推理成本。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：长程 agent 的失败往往不是模型不会每一步，而是执行系统丢失可变状态、不激活历史教训、跳过必要检查或提前停止。与其继续升级模型，本文研究 harness scaling：不改模型权重，改进外部控制层，把已有模型能力转化为可靠完成的执行结果。

**方法关键点**：
- StateM 是 agent 原生状态机运行时，用 YAML runbook 定义状态、合法转换、hooks、检查与恢复规则。
- 状态作为 context-and-contract boundary：进入状态刷新阶段指令和持久化进度，离开状态必须通过 exit checks；检查有 command/predicate、manual、checklist、llm_review 等不同证据强度。
- 三类 gap 对应三类控制：epistemic gap -> state-local context；procedural-memory gap -> versioned practices；procedural-compliance gap -> checked transitions。
- 失败驱动 harness 优化：把失败分类（缺上下文、无效转换、弱检查、提前交接等），通过超代理提出 runbook 修改，审慎验证后版本化；程序性知识沉淀在外部控制层，模型权重不变。
- 共享控制面：agent 通过 CLI 操作 runbook，用户可审计、编辑、版本化；runbook 与 per-run 状态分离，支持恢复。

**关键结果**：
- Terminal-Bench 2.1：GPT-5.5 xhigh + StateM 92.1% vs 基础 83.1%，提升 9 个百分点，约等于一代模型升级。
- 冻结该 runbook 用于 GPT-5.6 Sol xhigh 达 95.28% raw（424/445），全部 89 任务至少成功一次；GPT-5.6 Luna 从 76.7% 提升到 85.4%，超过 Sol xhigh 基础 84.9%。
- 跨 provider：直接冻结 GPT profile 到 DeepSeek-V4 Flash 从 82.7% 降至 82.0%，但低成本适配后达 88.09%（standard timeout），扩展 timeout 后描述性 88.76% 与 GPT-5.6 Sol max 的 88.8% 持平；DeepSeek 最终评估成本约 $15，总适配+评估 $52.22，对比参考 $574.68。
- BusinessBench：frozen held-out macro +0.55、micro +1.34；两个机制匹配家庭提升 10.04；RefactorBench 与 WooCommerce 先出现负迁移，纠正控制边界后恢复。

**最值得记住的一句话**：模型能力与执行可靠性对系统性能分别贡献；在这些场景中，模型不是主要瓶颈。
