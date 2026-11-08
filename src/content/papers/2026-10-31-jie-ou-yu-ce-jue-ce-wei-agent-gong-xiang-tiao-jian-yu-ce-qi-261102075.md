---
title: 'Decoupled Predictive Decision Making: A Shared Conditional Predictor for Agents'
title_zh: 解耦预测决策：为 Agent 共享条件预测器
authors:
- Lang Mo
- Xingxuan Zhang
- Qi Wang
- Mingchao Hao
- Hao Yuan
- Chunjing Gan
- Wang Lu
- Peng Cui
affiliations:
- Stable AI
- Tsinghua University
arxiv_id: '2611.02075'
url: https://arxiv.org/abs/2611.02075
pdf_url: https://arxiv.org/pdf/2611.02075
published: '2026-10-31'
collected: '2026-11-08'
category: Agent
direction: Agent 决策统一为条件预测
tags:
- Agent
- Conditional Prediction
- Decision Making
- Tool Use
- Structured Pretraining
one_liner: 将 agent 决策解耦为语义编码+条件预测，共享冻结预测器，50 基准平均准确率提升 6.12 个百分点
practical_value: '- 把 agent 中的工具选择、候选偏好、推理步骤评估统一为“证据+查询→目标预测”的接口，用一个条件预测器替代多个任务专用小模型，降低多任务维护成本；电商/广告
  agent 可先落地在工具调用质量评估和候选排序。

  - 语义编码与经验推断解耦：LLM 只负责把当前与历史记录编码成表示，条件预测器基于结构化数据预训练并冻结使用。线上可通过追加历史样本提升准确率而不更新任何大模型参数，适合推荐/广告场景里“策略不动、样本驱动改善”的工程约束。

  - 对 imbalanced history 的平衡准确率提升显著（14.51 个点），可借鉴到点击/转化稀疏的任务：把历史正负样本作为 evidence 输入条件预测器，而不是只做
  few-shot prompting，能显著改善少样本和类不平衡下的决策。

  - ToolPRMBench 上工具判断绝对提升 34.26/28.87 个点，说明在 agent 工具选择/拒绝场景中，显式建模历史成功失败经验比靠 prompt
  推理更可靠；可复用到电商导购 agent 的工具路由、API 选择与风控 reject。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：Agent 决策依赖部署后观察到的经验关系，任务描述不足以提供；需要将历史证据转化为预测的机制。现有 few-shot prompting 受限于 LLM 语义推理，缺乏从结构化历史中学习经验的能力。

方法：DPDM 将异构 agent 决策形式化为条件预测。LLM 作为语义编码器，把当前与历史记录表示为 evidence；共享的通用条件预测器（LimiX-2，结构化数据预训练）根据 evidence 和 query 预测任务定义的目标；决策规则将预测映射为选择。训练后两个模型均冻结，部署时通过历史证据实例化具体任务，不更新神经网络参数。工具判断、候选偏好、推理评估共用同一 evidence-query 接口。

结果：以 Qwen3.5-27B 为语义编码器，DPDM 在 50 个 benchmark 上的平均准确率从 few-shot 的 78.80% 提升到 84.92%（各自评估历史预算），相同历史与 query 下为 82.33%。ToolPRMBench 的 BFCL 和 ToolSandbox 任务绝对准确率分别提升 34.26% 和 28.87%。准确率随 history 增长而提升；在 imbalanced history 下，五个推理步骤评估任务的平均 balanced accuracy 绝对提升 14.51%。
