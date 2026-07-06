---
title: 'The Mirage of Optimizing Training Policies: Monotonic Inference Policies as
  the Real Objective for LLM Reinforcement Learning'
title_zh: LLM 强化学习的真实目标：面向推理策略的单调改进
authors:
- Jing Liang
- Hongyao Tang
- Yi Ma
- Yancheng He
- Weixun Wang
- Xiaoyang Li
- Ju Huang
- Wenbo Su
- Jinyi Liu
- Yan Zheng
affiliations:
- Tianjin University
- Alibaba
arxiv_id: '2606.29526'
url: https://arxiv.org/abs/2606.29526
pdf_url: https://arxiv.org/pdf/2606.29526
published: '2026-06-27'
collected: '2026-07-06'
category: Training
direction: LLM RL 训练-推理对齐
tags:
- LLM RL
- Training-Inference Mismatch
- Policy Optimization
- GRPO
- FP8 Quantization
one_liner: 提出 MIPI 原则与两步框架 MIPU，在训练-推理不匹配下直接优化推理策略，实现稳定高效 RL 训练
practical_value: '- 在电商/搜索推荐系统的 LLM 后训练中，训练引擎与推理引擎不一致（如量化部署）会导致训练策略改善 ≠ 推理策略改善，MIPU
  的两步机制（采样器参考更新 + 推理间隙验收）可直接嵌入 GRPO 流程，提升稳定性

  - Step 1 的 TIS 式截断重要性权重可替代标准 GRPO 裁剪，分离历史不匹配与当前更新，降低梯度方差，适用于任何基于采样优势的 RL 微调场景

  - Step 2 使用验证集上的后更新间隙代理 bTpost 作为接受/回滚信号，可在线上 AB 测试前筛选有害的同步模型，避免部署退化模型，尤其适合 Agent
  系统中的多步决策或量化推理

  - 动态接受阈值策略（起步宽、逐渐收紧）平衡早期探索与后期保护，在推荐模型持续学习时值得借鉴，防止过早收敛或训练宕机'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM RL 后训练（如 GRPO）通常由推理引擎采样、训练引擎更新，即使参数一致，浮点精度等实现差异也会导致训练策略 π 和推理策略 µ 对同一轨迹的概率不同。现有方法（MIS、LR 衰减等）试图在训练侧抑制这种不匹配，但忽略了根本问题：训练策略的改进并不保证推理策略的改进，即目标错位。在 FP8 量化推理等高不匹配设置下，训练常出现性能飙升后崩溃。

**方法关键点**：
- 提出 **MIPI 原则**：RL 更新应直接追求推理策略的单调改进 ΔJ(µ) > 0，而非仅看训练侧 ΔJ(π)。
- 将 J(µ_{k+1}) - J(µ_k) 分解为三项：后更新推理间隙 ( J(µ_{k+1})−J(π_{k+1}) ) + 训练侧更新 ( J(π_{k+1})−J(π_k) ) + 预更新推理间隙 ( J(π_k)−J(µ_k) )。
- 两步框架 **MIPU**：
  - **Step 1 采样器参考更新**：使用截断重要性权重（TIS）以 µ_k 为参考做 PPO 式裁剪，避免历史不匹配干扰当前更新，构造候选训练策略 π_{k+1}。
  - **Step 2 推理间隙感知验收**：同步得到 µ_{k+1} 后，用验证集估计后更新间隙代理 bTpost，若 bTpost < -c 则拒绝更新并回滚，否则接受。
- 容忍度 c 采用动态退火：初期较大以允许探索，逐渐收紧。

**关键实验**：
- 设置：Qwen3-1.7B 和 Qwen3-4B，FP8 量化推理制造强不匹配；训练数据 DAPO-Math-17k 和 DeepMath-103K；评估于 MATH、AIME、AMC23 等 5 个数学推理基准。
- 主要对比：GRPO 基线、MIS（掩码过滤）、LR 衰减。
- 结果：MIPU 在 Qwen3-4B 上平均 pass@1 达 66.71%（基线 64.42%），在量化下训练曲线稳定，无崩溃；消融显示 Step 1 与 Step 2 互补，Step 2 的条件拒绝比随机拒绝更有效。

**论文最值得记住的一句话**：“在训练-推理不匹配下，我们不应只优化训练策略，而应将对推理策略的单调改进作为真正的策略优化目标。”
