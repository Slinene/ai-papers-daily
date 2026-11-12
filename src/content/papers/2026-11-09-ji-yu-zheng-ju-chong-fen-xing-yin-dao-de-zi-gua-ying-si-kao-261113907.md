---
title: 'EVAThink: Evidence Sufficiency-Guided Training for Adaptive Thinking in Video
  Understanding'
title_zh: 基于证据充分性引导的自适应思考视频理解训练
authors:
- Changti Wu
- Ruizhe Fan
- Bin Wang
- Lei Zhang
- Yuxiang Zhang
affiliations:
- East China Normal University
- Zhongguancun Academy
- Huawei Technologies Co., Ltd
arxiv_id: '2611.13907'
url: https://arxiv.org/abs/2611.13907
pdf_url: https://arxiv.org/pdf/2611.13907
published: '2026-11-09'
collected: '2026-11-12'
category: Multimodal
direction: 多模态视频理解 · 自适应推理训练
tags:
- Video Understanding
- Reinforcement Learning
- Adaptive Thinking
- VLM
- Evidence Sufficiency
- Mode Collapse
one_liner: 用证据充分性挖掘稀疏/密集视频视图配对，并通过两阶段RL训练VLM在直接回答与显式推理间自适应切换
practical_value: '- 在商品视频/直播切片理解中，可先估计当前采样帧的证据充分性，决定走“直接输出标题/卖点”还是“多跳推理补全属性”，降低低价值推理调用延迟；类似
  EVAThink 的 sparse/dense 配对数据可自动构造：同一商品视频，密集帧 vs 稀疏帧，保留“稀疏直接回答变差但推理能救回”的样本作为模式选择监督。

  - RL 两阶段可迁移到生成式推荐/query 改写：先让 reward 偏好 evidence-based mode，再引入 token 成本或响应效率惩罚，使模型在“直接生成推荐理由/搜索词”与“先推理用户意图再生成”之间自适应，控制平均输出长度和
  latency。

  - first-token advantage regularization 可用于 LLM4Rec 的 RL 训练，防止 reward hacking/mode
  collapse，尤其做生成式 Semantic ID 或推荐理由时，避免模型只学一种模板。

  - 仅 6.7K 精选样本即可稳定提升，说明在业务标注预算有限时，优先构造高质量 contrastive evidence pairs 比堆量更有效。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：固定帧预算下，视频问答质量取决于采样帧是否覆盖足够证据；证据充分时直接回答即可，证据不足时显式推理能连接可用线索，但模型通常不会自适应切换。

**方法关键点**：Recoverable Evidence Gap Mining 构造同一问答下的 evidence-dense / evidence-sparse 两种视频视图，保留“sparse 视图直接回答变差、但显式推理可恢复”的样本，作为 response-mode 选择监督。Evidence-Guided Two-Stage RL 先按证据充分性训练模式偏好，再优化输出效率；first-token advantage regularization 用于防止模式坍缩。

**关键结果**：仅用 6.7K 精选样本，在 32/64 帧预算下多个视频理解 benchmark 稳定超过 base model，平均优于强 baseline。
