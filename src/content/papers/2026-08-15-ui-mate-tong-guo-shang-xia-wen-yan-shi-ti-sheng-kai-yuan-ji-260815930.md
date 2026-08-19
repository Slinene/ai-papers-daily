---
title: 'UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations'
title_zh: UI-Mate：通过上下文演示提升开源权重基础 GUI 智能体
authors:
- Zihan Ding
- Longxu Dou
- Qi Gao
- Xiangwu Guo
- Shengchao Hu
- Zilong Huang
- Zihang Jiang
- Lei Ke
- Mengcheng Lan
- Weixian Lei
affiliations:
- Tencent Hy Frontier Team
arxiv_id: '2608.15930'
url: https://arxiv.org/abs/2608.15930
pdf_url: https://arxiv.org/pdf/2608.15930
published: '2026-08-15'
collected: '2026-08-19'
category: Agent
direction: GUI Agent 训练与上下文演示
tags:
- GUI Agent
- In-Context Learning
- RL
- Benchmark
- Open-Weight
- Computer Use
one_liner: UI-Mate 结合环境驱动训练栈与上下文演示学习，在 OSWorld 等基准刷新开源 GUI 智能体 SOTA
practical_value: '- **任务验证器与闭环数据引擎**：可复用到电商 RPA、客服助手等 GUI 操作场景，用统一的 task–verifier
  bundles 自动化生成、过滤和平衡训练数据，减少人工标注。

  - **演示学习的方式**：将多模态演示转成 subtask-level workflow 而非刚性轨迹回放，同时允许从实时界面重新规划——适合电商中用户特定工具、隐性规则（如改地址需二次确认）的场景。

  - **区分 self-demo 与 variant-demo**：在构建演示数据库时，应分离同任务成功轨迹与相似但非同一任务的人类录制，有助于评估和提升模型对未见变体的泛化能力。

  - **评测指标**：除了 strict success，还引入 progress 指标，对长流程电商操作（如比价、下单、售后）更细粒度地反映中间进展，适合作为内部迭代指标。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：基础 GUI 智能体部署受限于训练数据稀缺与分布偏差，以及提示歧义和执行不可靠。日常工作流依赖用户特定工具和隐性惯例，未明示指令会导致执行结果逐次波动。

**方法关键点**：UI-Mate 提出三项贡献：
1) **环境驱动的可扩展训练栈**：闭环数据引擎自动化任务生成、环境构建、rollout、过滤、能力平衡，并通过统一 task–verifier bundles 在大量并行环境中进行 SFT 与在线 RL。
2) **上下文演示学习**：将多模态演示转化为灵活的 subtask 级工作流，而非僵硬回放轨迹；在关键步骤遵循演示，同时基于实时界面自主重新规划。
3) **OSWorkerBench 基准**：包含 100 个长程办公任务、跨 41 个应用，支持纯指令与演示引导两种评估；33 个 self-demo 任务使用同目标成功轨迹，45 个 variant-demo 任务使用相关但非同一任务的人类录制。

**关键结果**：UI-Mate-27B 在 OSWorld-Verified 得 77.0%、WindowsAgentArena 得 66.2%，均为开源权重新 SOTA。在 OSWorkerBench 上达到 41.0% strict success 和 76.9% progress，较 Qwen3.6-27B 基座分别提升 17.7 和 24.5 个百分点。在 33 个 self-demo 子集上，一条演示将 strict success 从 17.2% 提升到 35.4%，progress 从 67.9% 提升到 81.1%，显著改善长程可靠性。
