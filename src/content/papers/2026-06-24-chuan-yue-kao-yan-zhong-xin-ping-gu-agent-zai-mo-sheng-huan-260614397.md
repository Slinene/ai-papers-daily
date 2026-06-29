---
title: 'Running the Gauntlet: Re-evaluating the Capabilities of Agents Beyond Familiar
  Environments'
title_zh: 穿越考验：重新评估 Agent 在陌生环境中的泛化能力
authors:
- Mykola Vysotskyi
- Runqi Lin
- Grzegorz Biziel
- Michal Zakrzewski
- Sebastian Montagna
- Damian Rynczak
- Shreyansh Padarha
- Kumail Alhamoud
- Zihao Fu
- William Lugoloobi
affiliations:
- University of Oxford
- SoftServe
- Massachusetts Institute of Technology
- The Chinese University of Hong Kong
- UK AI Security Institute
arxiv_id: '2606.14397'
url: https://arxiv.org/abs/2606.14397
pdf_url: https://arxiv.org/pdf/2606.14397
published: '2026-06-24'
collected: '2026-06-29'
category: Eval
direction: Agent 评估基准 · 泛化能力探针
tags:
- Agent Evaluation
- Benchmark
- Generalization
- Temporal Perception
- Graphical Understanding
- 3D Reasoning
one_liner: 提出 GauntletBench 基准，揭示当前最佳 Agent 在时间感知/图形理解/3D 推理任务上仅 19.1% 成功率，远低于人类 80%+。
practical_value: '- **评估泛化缺口**：当前推荐/电商 Agent 的评测也易陷入熟悉任务饱和，可借鉴 GauntletBench 设计新维度（如时间感知、图形理解）的任务集，揭示模型在真实业务场景的短板。

  - **多模态能力补强**：电商 Agent 常需理解 UI、处理含时间序列的数据（如库存变化、促销时段）或分析商品 3D 模型，该基准揭示的视觉推理缺陷提醒我们在构建
  Agent 时需重点强化这些能力。

  - **模块化评测框架**：论文提供的 web 环境、任务套件与自动评测流水线可复用到电商 Agent 测试中，构建可重复、可对比的评测基准，降低人工评估成本。

  - **人类基线锚定**：用非专家人类表现（>80%）作为参照，量化 Agent 成熟度，帮助业务团队设定合理的自动化预期与优化目标。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 Agent 基准多基于简单流行应用，能力维度狭窄，导致现代 Agent 性能饱和，无法暴露真实局限性。亟需一个挑战性基准来评估 Agent 在陌生环境与未充分探索能力上的泛化表现。

**方法**：构建 GauntletBench——一个 web-based 基准，聚焦三大被忽视的能力（时间感知、图形理解、3D 推理），覆盖五个专业应用（视频编辑器、工作流构建器、3D 建模器、飞行分析器、电路设计器），每应用 20 个视觉密集型任务，共计 100 个。提供模块化流水线：兼容开闭源 Agent 框架的环境、受控 web 应用、结构化任务套件及多种指标的自动评估引擎。

**关键结果**：前沿 Agent 表现远未及人类：最先进的 Agent 成功率仅 19.1%（最佳单模型），而人类非专家标注者达 80%+。这暴露了 Agent 在时间推理、图形解读与 3D 空间理解上的严重缺陷，以及跨专业领域泛化的巨大差距。
