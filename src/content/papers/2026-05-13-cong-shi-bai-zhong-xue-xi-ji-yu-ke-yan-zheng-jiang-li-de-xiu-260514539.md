---
title: 'Learning from Failures: Correction-Oriented Policy Optimization with Verifiable
  Rewards'
title_zh: 从失败中学习：基于可验证奖励的修正导向策略优化
authors:
- Mengjie Ren
- Jie Lou
- Boxi Cao
- Xueru Wen
- Hongyu Lin
- Xianpei Han
- Le Sun
- Xing Yu
- Yaojie Lu
affiliations:
- Chinese Information Processing Laboratory, Institute of Software, Chinese Academy
  of Sciences
- University of Chinese Academy of Sciences
- Xiaohongshu Inc.
arxiv_id: '2605.14539'
url: https://arxiv.org/abs/2605.14539
pdf_url: https://arxiv.org/pdf/2605.14539
published: '2026-05-13'
collected: '2026-05-18'
category: Training
direction: 利用失败轨迹的修正训练增强 RLVR
tags:
- RLVR
- GRPO
- Error Correction
- Self-Refinement
- Reasoning
- Code Generation
one_liner: 将 RLVR 中的失败轨迹转化为修正监督，无需额外信号，显著提升推理与自我纠错能力
practical_value: '- 在构建对话推荐 Agent 时，可利用用户交互中的失败轨迹（如不满意回复）构造修正对，通过 RL 训练提升 Agent 自我纠错能力，而非简单抑制。

  - 生成式推荐或代码生成 Agent 可借鉴难度感知偏好采样（Section 3.3），优先重放中等通过率的样本，避免在过难或过易问题上浪费计算。

  - 自适应重放比率与风险厌恶奖励塑形（Section 3.2）可迁移到推荐策略 RL 训练中，动态平衡正确与错误轨迹，防止遗忘已学知识并抑制能力退化。

  - 在线修正机制无需外部标注或奖励模型，适合电商 Agent 在无人工反馈的条件下持续优化多步规划与纠错能力。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：标准 RLVR（如 GRPO）使用二元稀疏奖励，失败轨迹被统一惩罚，忽略了其中部分正确的推理步骤和错误模式的多样性，导致优化信号模糊、探索低效。已有的过程监督方法依赖外部奖励模型或标注，成本高且可能引入偏差。本文提出 CIPO，将 on-policy 失败轨迹转化为修正导向的监督信号，无需外部信息，提供更强的方向性学习信号。

**方法关键点**：
- **修正流构建**：对每条原始 prompt，用模型自身的错误输出作为条件，重新采样生成修正解，形成“失败→修正”轨迹对，联合优化标准 GRPO 目标与修正目标。
- **自适应重放比率**：根据模型在历史正确轨迹上的保持表现，动态调整成功与失败轨迹的混合比例，防止过度修正导致性能退化。
- **风险厌恶奖励塑形**：对“正确→错误”的修正施加额外惩罚，抑制能力倒退。
- **难度感知轨迹偏好**：优先选择中等通过率的 prompt 进行修正重放，避免简单/困难样本浪费计算。

**关键实验**：在 Qwen3-4B（数学）和 Seed-Coder-8B（代码）上训练 500 步。数学 6 个基准（AIME24/25、AMC23、MATH500、Minerva、Olympiad）平均准确率从初始 46.82% 提升至 64.38%，比 GRPO 高 4.55%；AIME24 上达 47.50%（GRPO 42.08%）。代码生成 LiveCodeBench 达 30.33%（GRPO 29.45%）。纠错能力：CriticBench 数学修正率 +7.74%，DebugBench 提升 4.20%，超越 Qwen2.5-72B 并与 Claude-4-sonnet 相当。pass@K 显著提升（AIME24 pass@32 86.67% vs GRPO 76.67%），表明模型内在推理能力增强，而非单纯概率重分配。

**核心 insight**：通过将失败轨迹转化为修正样本，CIPO 天然区分错误模式——接近正确的方案在修正采样时更易成功，从而提供细粒度学习信号，同时显式训练模型的自我纠错能力。
