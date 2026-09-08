---
title: A Verifier-Guided Explainable Reasoning Framework with Gold-Anchored QLoRA,
  Task-Aware Mixture-of-Experts, and Group-Relative RLVR
title_zh: 验证器引导的可解释推理框架：金答案锚定QLoRA与组相对RLVR
authors:
- Thi Kim Trang Vo
- Nam Tien Le
- Thi Kim Nguyet Vo
- Minh Khang Tran
- Duy Phuong Tran
affiliations:
- University of Information Technology (UIT), Ho Chi Minh City, Vietnam
- Ho Chi Minh City University of Technology (HCMUT), Vietnam
- Vietnam National University, Ho Chi Minh City, Vietnam
- University of Economics Ho Chi Minh City (UEH), Vietnam
- Viet Nam – The Netherlands Programme (VNP), Vietnam
arxiv_id: '2609.05221'
url: https://arxiv.org/abs/2609.05221
pdf_url: https://arxiv.org/pdf/2609.05221
published: '2026-09-04'
collected: '2026-09-08'
category: Reasoning
direction: 神经符号推理 · RLVR 可解释性
tags:
- RLVR
- QLoRA
- Mixture-of-Experts
- Neuro-Symbolic Reasoning
- Explainable AI
- Self-Consistency
one_liner: 结合金答案锚定QLoRA、任务感知符号路由和组相对RLVR，在保持答案正确率的同时大幅提升推理可解释性
practical_value: '- 可借鉴「符号验证器 + 模型自一致性」的双层校验：在电商 Agent 中，对价格计算、优惠规则等可形式化任务部署轻量符号求解器，对
  LLM 候选输出做系统级修正，可在不改变模型参数的情况下提升可靠性。

  - RLVR 中的多维奖励设计可迁移：将奖励分为答案正确性、证据一致性、推理深度/可解释性三类，能单独优化推理结构而不牺牲准确率；在推荐解释生成、Agent 决策理由生成等场景可借鉴。

  - 任务感知路由：用轻量路由器将问题分发给不同专家（符号求解器 vs 神经模型），减少不必要计算并提高针对性；在电商多任务 Agent 中可按意图分流到不同工具或验证模块。

  - QLoRA 微调时锚定权威答案（gold-anchored）可减少幻觉；在构建商品知识问答或客服 Agent 时，用结构化知识库答案做监督信号，提升生成内容的可靠性。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 推理能力强但解释常不一致、缺乏验证，尤其在教育问答中需要可追溯的推理。

**方法**：提出验证器引导框架，包含三部分：
1. 用 gold-anchored QLoRA 在 Qwen2.5-3B-Instruct 上做领域适配，并引入 field-weighted 监督；
2. 轻量路由器将逻辑题分给 FOL/Z3 验证器，物理题分给公式与单位感知的符号求解器；
3. 基于验证器反馈构建 group-relative RLVR，从 P1（答案正确）、P2（证据/单位一致）、P3（推理深度与可解释性）三个维度评估候选，用于自修订和奖励构造。

推理时用 gold-free 自一致性聚合多个候选，可选问题级物理验证器做保守修正。

**结果**：在 438 个 held-out 样本上，RLVR 将 P3 从 50.68% 提升到 72.20%，而混合 P1 稳定在 55.94%；自一致性将纯模型 P1 从 48.86% 提升到 50.23%，符号验证补足剩余增益，说明 RLVR 主要强化推理结构，符号验证在系统层提升答案可靠性。
