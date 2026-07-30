---
title: 'Think Short, Defer Smart, Act, and Repeat: Calibrated Reasoning and Uncertainty-Aware
  Deferral for Edge LLM Agents'
title_zh: 边缘 LLM 智能体的校准推理与不确定性推迟框架
authors:
- Amirmohammad Farzaneh
- Osvaldo Simeone
affiliations:
- Northeastern University London
arxiv_id: '2607.26865'
url: https://arxiv.org/abs/2607.26865
pdf_url: https://arxiv.org/pdf/2607.26865
published: '2026-07-29'
collected: '2026-07-30'
category: Agent
direction: 边缘 LLM Agent 推理预算与智能推迟
tags:
- Edge LLM Agents
- ReAct
- Calibrated Deferral
- Uncertainty-Aware
- Lightweight Convergence Probe
- LTT
one_liner: 提出 TSDS，集成轻量收敛探针与困惑度推迟规则，通过 LTT 联合校准，在边缘 ReAct 智能体上显著减少思考计算量并保证性能
practical_value: '- 在构建基于 ReAct 的推荐或客服 agent 时，借鉴轻量收敛探针，监测多步推理中动作的稳定性，当连续几步预测的动作一致时提前终止推理，节省推理成本，适用于商品属性搜索、对话式推荐等需要多步交互的场景。

  - 设计基于困惑度的推迟规则，对 agent 生成的最终动作序列计算困惑度，若低于阈值则本地执行，否则转交云端大模型，有效控制云端调用成本，并可设定可接受的调用率上限。

  - 利用 LTT 方法在历史交互日志上联合校准推理停止阈值和推迟阈值，使系统在满足云端调用率约束的同时最大化成功奖励，提供统计保证，可在推荐系统的多步决策流程中应用。

  - 对于需要权衡延迟和精度的推荐场景（如实时推荐解释生成），TSDS 的动态推理深度和推迟策略可迁移，实现自适应的资源调度。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：边缘部署的 LLM 智能体遵循 ReAct 范式，思考步骤消耗大量计算，但资源受限设备需在可靠性与延迟间权衡。现有方法缺乏对推理预算和云推迟机制的联合优化，当本地不确定性高时应推迟至更强模型。

**方法**：TSDS 框架集成两个机制：(1) 轻量收敛探针，在每步推理中监控连续思考所预测的动作，一旦动作序列稳定即提前终止思考，缩减无效推理；(2) 基于困惑度的推迟规则，对完整动作序列计算困惑度，超过校准阈值则将整个 episode 推迟到云端执行。两者通过多目标 Learn-Then-Test (LTT) 过程在端到端轨迹上联合校准，提供对期望 episode 奖励和云调用率的同时有限样本保证。

**结果**：在 GSM8K、HotpotQA、MBPP 和家用机器人四个 ReAct 基准上，TSDS 在 HotpotQA、MBPP 和机器人任务上将每 episode 思考计算量降低 43%–73%，同时保持认证的奖励与云调用率保证，验证了其在边缘智能体推理管理中的有效性。
