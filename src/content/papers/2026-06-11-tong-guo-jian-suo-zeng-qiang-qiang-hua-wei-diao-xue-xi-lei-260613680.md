---
title: Learning to Reason by Analogy via Retrieval-Augmented Reinforcement Fine-Tuning
title_zh: 通过检索增强强化微调学习类比推理
authors:
- Zilin Xiao
- Qi Ma
- Chun-cheng Jason Chen
- Xintao Chen
- Avinash Atreya
- Hanjie Chen
- Vicente Ordonez
affiliations:
- Meta Superintelligence Labs
- Rice University
arxiv_id: '2606.13680'
url: https://arxiv.org/abs/2606.13680
pdf_url: https://arxiv.org/pdf/2606.13680
published: '2026-06-11'
collected: '2026-06-13'
category: Training
direction: 检索增强的强化微调与推理效用学习
tags:
- RAG
- Reinforcement Fine-Tuning
- Analogy Reasoning
- Mathematical Reasoning
- RLVR
- Contrastive Learning
one_liner: 提出 RA-RFT，用推理效用蒸馏检索器，并在强化微调中注入类比演示，大幅提升数学推理性能
practical_value: '- **检索应面向任务效用而非表面相似**：在电商推荐中，传统的语义相似召回可能带不来转化或点击，可用 judge 模型离线蒸馏“转化效用”标签，训练检索器优先召回能提升下游任务（如购买）的
  item，而不只是语义相关。

  - **强化学习训练时可注入类比案例**：在对话 Agent、多智体协作等 RL 训练中，可将历史成功轨迹作为演示（类比），以少量上下文形式注入，提高奖励信号密度，加速策略学习，方法可套用
  RA-RFT 的"检索-蒸馏-注入"流程。

  - **多向量检索更适合结构级匹配**：使用 ColBERT 等 late-interaction 模型捕捉推理结构或交互模式，适用于需要挖掘行为序列相似性的场景，如推荐中的
  session 匹配、用户轨迹类比。

  - **训练目标决定检索增益**：仅做 SFT 时检索增益微弱，须配合让模型主动探索并选择性利用外部信息的训练范式（如 RLVR），这提示在将 RAG 融入推荐
  agent 训练时，要用生成式奖励而非固定目标的监督学习。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：现有 RLVR 方法完全依赖参数化知识，面对陌生推理模式时探索失败、奖励稀疏。传统 RAG 的语义相似度检索与推理效用脱节，表面相似的题目可能需要不同解法，结构类似的题目表面却不同。人类解决复杂问题时依靠类比推理——回忆已解决的、底层推理结构可迁移的问题。该工作希望让语言模型在 RL 微调中也能获得类比演示，形成推理支架。

**方法关键点**
- **黄金相关性蒸馏**：用 GPT-4o 作为 judge，对每对 query-candidate trace 判断是否共享可迁移的推理模式（如同一定理、证明技术），产生二元标签，避免完全依靠语义相似度。
- **推理感知检索器训练**：基于蒸馏的标签，用对比 InfoNCE 损失微调 ColBERT 风格的多向量检索器，使其按推理效用排序。
- **检索增强的 RL 微调**：训练时用该检索器为每个问题取 top-1 推理 trace 作为上下文，模型在 trace 条件下采样 rollout，通过 GRPO 等策略优化，仅根据答案正确性给奖励，模型学会利用类比线索。

**关键实验结果**
- 在 AIME 2024/2025、HMMT 2025、BrUMO 2025 四个竞赛数学基准上，RA-RFT 一致优于标准 GRPO 和 OPSD 等强基线。Qwen3-1.7B 上 AIME 2025 平均@32准确率提升 7.1 点，Qwen3-4B 提升 2.8 点。
- 消融显示：最终微调的检索器相比未微调版本性能大幅提升（Reason-ModernColBERT 从 40.7 → 47.4），多向量检索优于单向量；SFT 加检索增益微弱（39.7 vs 40.5），但 RL 下增益显著，说明模型需通过探索学习使用外部信息；不同检索上下文对同一问题的准确率差异很大，表明类比多样性提供了不同解题支架。

**核心洞见**：有效的推理检索必须扎根于推理效用而非表面相似；将类比演示融入 RL 训练循环，让模型在结果奖励下学会利用外部类比，而不是死记硬背。
