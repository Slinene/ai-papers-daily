---
title: 'QUASAR: Lowering the Loss Floor of Quantization-Aware Training with Loss-Aware
  Reconstruction'
title_zh: QUASAR：通过损失感知重建降低量化感知训练的损失下界
authors:
- Vincent Counathe
- Ben Athiwaratkun
- Christopher De Sa
- Tianyi Zhang
affiliations:
- Cornell University
- Together AI
arxiv_id: '2608.13966'
url: https://arxiv.org/abs/2608.13966
pdf_url: https://arxiv.org/pdf/2608.13966
published: '2026-08-14'
collected: '2026-08-17'
category: Training
direction: 量化感知训练 · 损失感知重建
tags:
- QAT
- Quantization
- Loss-aware Reconstruction
- LLM
- NVFP4
- Low-bit Inference
one_liner: 将损失感知重建引入 QAT 训练循环，用 Adam 二阶矩做 saliency 进行尺度搜索和加权最小二乘拟合，压低低比特模型 loss floor
practical_value: '- 低比特部署 LLM 时，若线上沿用 PTQ 掉点明显，可切换到 QUASAR 式 QAT：保持 weight-only 量化，不增加推理
  overhead，训练开销仅 +1.4%。对需要长期稳定低延迟的推荐/Agent 推理服务有直接落地价值。

  - 可直接复用两个 trick：用 AdamW 的 second moment \(v_t\) 作为权重的 saliency 估计，无需额外 Hessian 计算/存储；每步在
  [0.3,1.0] 范围内搜索裁剪因子，并对反量化 scale/zero-point 做 saliency 加权最小二乘闭式求解，插入现有训练循环成本极低。

  - 在 2-bit 这类极端低精度下，QAT 对数学推理和长链 Agent 任务质量影响显著；QUASAR 直接低比特 SFT 平均数学基准比最强 baseline
  高 10.9 点，且是唯一在 HMMT''25 上非零的方法，说明保住长生成能力很关键。

  - 该方法兼容 NVFP4 等生产格式，可把同样思路迁移到 MXFP4 或自定义 block-scaled 格式；迁移时只需调整候选 scale 与网格约束，核心目标不变。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
随着 LLM 推理向 FP4/INT4 等低精度格式迁移，PTQ 在推理/Agent 模型长上下文下累积量化误差，越来越脆弱。QAT 虽能保留质量，但前向使用量化重建权重 r，优化器更新潜在全精度权重 w，STE 梯度不最优，导致训练收敛到较高 loss floor。第二阶 PTQ 用 loss-aware 重构误差弥补这种 mismatch，但一次性求解耗时太长，无法在训练中重复。

**方法关键点**  
- 将 loss-aware 重构误差近似为 S_t = Σ h_i (r_i - w_i)^2，其中 saliency h 直接复用 AdamW 的 second moment，无额外开销。  
- 每一训练步分解为两个阶段优化：码本分配阶段在 [0.30,1.00] 范围内搜索裁剪因子 f，生成不同整数码 q_f；反量化阶段对每个 q_f 用 saliency 加权最小二乘闭式解拟合 scale/zero-point，选择 S_t 最小的候选。  
- 理论收敛界分解为初始化、minibatch noise、loss-aware 重构误差三项，只有重构误差依赖重建映射，正是 QUASAR 每步优化的目标；在 PL 条件下控制最终量化模型损失。  
- 只改训练过程，不改推理，兼容 INT4/3/2 和 NVFP4。

**关键实验结果**  
- Qwen3-4B-Thinking / Llama-3.1-8B-Instruct INT4/3/2 量化感知蒸馏：QUASAR 在所有 bit 下达到最低 held-out KL；INT3/4 降低至少 10%，INT2 降低至少 29%。INT2 平均下游准确率提升 3.5–4.3 点，GSM8K 从最佳 baseline 的 49.0/53.1 提升到 68.8/66.4。  
- Qwen3-4B-Base 低比特 SFT 学数学：INT2 平均五基准 29.6 分，比最强 QAT 高 10.9 分；所有 FT-then-PTQ 基线 MATH/GSM8K 不超过 2.1/1.2。  
- NVFP4：Qwen3-8B / Qwen3.5-9B KL 降低约 30%，下游平均精度 +0.5–2.0 点。  
- 训练开销 +1.4%，无推理 overhead。

**最值得记住的一句话**  
低比特 QAT 不该只学 step size 或软化 rounding，而应每步用 saliency 加权最小二乘和尺度搜索直接最小化 loss-aware 重构误差，才能显著压低 loss floor。
