---
title: 'GUI-HARVEST: Self-Improving GUI Agents through Evidence-Driven Harness Evolution'
title_zh: GUI-HARVEST：证据驱动的 GUI Agent Harness 自改进
authors:
- Geyi Yang
- Zikun Qu
- Xiang Li
- Zhiyong Wang
- Min Zhang
- Shipei Zeng
- Zhongxiang Dai
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Tianjin University
- Harbin Institute of Technology (Shenzhen)
- East China Normal University
- Shenzhen Research Institute of Big Data
arxiv_id: '2610.00948'
url: https://arxiv.org/abs/2610.00948
pdf_url: https://arxiv.org/pdf/2610.00948
published: '2026-09-30'
collected: '2026-10-07'
category: Agent
direction: GUI Agent 自适应 Harness 优化
tags:
- GUI Agent
- Harness Optimization
- Self-Improvement
- Evidence-Driven
- OSWorld
- WindowsAgentArena
one_liner: 用证据驱动 harness 自动进化，让冻结 backbone GUI agent 自改进并跨任务/模型泛化
practical_value: '- 在电商/搜索推荐 Agent 管线中，可借鉴「证据驱动诊断」：记录模型意图、实际执行动作及前后环境状态（如搜索结果页、购物车状态变化），定位具体状态转移，而非只看最终
  reward，从而找出 harness 该改哪里（如终止条件、重试策略、query 改写触发点）。

  - 同任务重复运行作为联合证据，比较成功/失败轨迹差异，能排除执行随机性影响，提取 outcome-relevant 的行为差异（例如成功轨迹多了一次二次验证），再把这些差异固化为
  runtime 规则，比单次失败更可靠。

  - harness 优化建议限制在 bounded source-code edits（观测组装、动作执行、验证/恢复、终止控制），并在评估前记录预测行为效果；这样能验证行为与任务性能双重提升，降低过拟合到特定任务的风险，便于在
  unseen tasks 上复用。

  - 冻结 backbone 下优化 harness，再跨模型/跨环境迁移，可减少对每个新模型做 fine-tune 或 prompt 工程；电商场景中可先在成本较低模型上优化
  harness，再迁移到更强闭源模型或不同产品域。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：GUI agent 的可执行 harness 决定观测组装、动作执行、验证/恢复/终止，但自动优化 harness 需同时解决三个耦合挑战：模型意图与视觉结果对齐、执行波动下诊断失败、跨任务复用失败模式。非 GUI harness 优化无法直接迁移。

**方法关键点**：
- 证据驱动诊断：对齐模型输出、已执行动作与前后截图，把发现绑定到具体界面 transition；
- 执行波动建模：将同任务重复运行视为联合证据，通过组内对比定位与结果相关的行为差异；
- 跨任务复用：把验证后的发现聚合成 recurrent failure patterns，映射为 bounded source-code edits；评估前记录预测的行为效果，重复执行验证行为与任务性能。

**结果**：在 OSWorld-Verified 上，六个 backbone（通用开源、GUI 专用开源、闭源）held-out 一致提升；Qwen3-VL-32B-Instruct 全量 +12.33 pts；frozen-harness 迁移到 WindowsAgentArena，GPT-5 在 50 steps 提升 13.87 pp；同 backbone 下优于 Self-Harness 和 Meta-Harness。
