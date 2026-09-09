---
title: 'FlowBalance: Verifier-Grounded Self-Improvement from On-Policy Reasoning Experience'
title_zh: FlowBalance：验证器校准的轨迹平衡自改进
authors:
- Zixun Huang
- Kishan Panaganti
- Haitao Mi
- Leowei Liang
affiliations:
- Tencent HY LLM Frontier
- University of Pennsylvania
arxiv_id: '2609.03241'
url: https://arxiv.org/abs/2609.03241
pdf_url: https://arxiv.org/pdf/2609.03241
published: '2026-09-02'
collected: '2026-09-09'
category: Training
direction: LLM 自改进训练 · 轨迹平衡
tags:
- self-improvement
- trajectory balance
- verifier
- reasoning
- RL
- flow matching
one_liner: 用 verifier 校准 on-policy 自引导分数，并通过轨迹平衡训练稳定的推理自改进
practical_value: '- 在生成式推荐/QueryRec 的 LLM 后训练中，若已有 outcome verifier（如点击、转化、相关性），可借鉴
  group advantage 校准 self-guidance 符号：正优势保留密集信号、负优势反转、无偏好时禁用，避免 dense same-model 信号强化伪自信。

  - 轨迹平衡替代逐 token 模仿 loss，对长文本生成（推荐理由、搜索词扩展、商品文案）训练更稳定，能缓解长度坍塌和模式集中，适合带 terminal reward
  的离线增强场景。

  - 冻结策略视图产生自引导分数的方法，可在 RLHF/DPO 管线上低成本复用，减少额外 critic 或 token 级标注需求；若业务能定义可靠 verifier，可让
  LLM 在搜索推荐 Agent 的推理链路上保持策略多样性。

  - 无明确 outcome verifier 或奖励稀疏的业务场景，方法借鉴价值有限，主要适用于可自动判定的任务（如数学、代码、结构化查询生成）。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：推理模型从自身 on-policy 经验改进时，terminal verifier 可靠但稀疏，dense same-model guidance 可能强化错误信心或使学习过度集中到某个窄解模式。

**方法**：FlowBalance 学习完整响应上的归一化分布。对每个 on-policy 轨迹，用同一个策略的冻结视图，在特权上下文中计算 token 级对数概率增益，聚合成轨迹级自引导分数。然后用 verifier 派生的 group advantage 校准该分数：正优势轨迹保留自引导，负优势轨迹反转自引导，rollout 组无偏好时禁用。所得能量指数重加权参考策略，profiled trajectory balance 用每个 rollout 组一个 log-partition 估计拟合归一化目标，不引入单独的 token 级模仿 loss。

**理论分析**：证明组内对比保持、最小变化 reverse-KL 特性、目标奖励对 verifier 的单调控制，以及在被拒响应上对假阳性自引导的精确校正。

**结果**：在 Qwen3-4B 和 Qwen3-8B 数学推理上，平均性能超过 FlowRL，训练速度与稳定性提升，避免直接 OPSD 导致的响应长度崩塌，AIME24 诊断中正确策略多样性更高。
