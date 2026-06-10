---
title: Rethinking the Divergence Regularization in LLM RL
title_zh: 重新思考LLM强化学习中的散度正则化
authors:
- Jiarui Yao
- Xiangxin Zhou
- Penghui Qi
- Wee Sun Lee
- Liefeng Bo
- Tianyu Pang
affiliations:
- Tencent Hunyuan
- UIUC
- NUS
arxiv_id: '2606.09821'
url: https://arxiv.org/abs/2606.09821
pdf_url: https://arxiv.org/pdf/2606.09821
published: '2026-06-07'
collected: '2026-06-10'
category: Training
direction: LLM 强化学习训练·信任域正则化
tags:
- LLM RL
- trust region
- divergence regularization
- DRPO
- off-policy RL
- PPO
one_liner: 提出DRPO，用连续二次正则化替代硬掩码，实现基于Binary-TV散度的平滑信任域，提升LLM RL训练的稳定性与效率
practical_value: '- **信任域设计应从比例转向绝对概率偏移**：在长尾词表的LLM策略优化中，重要性比率 (ratio) 不能准确反映分布变化。DRPO
  通过 Binary-TV 散度（|π-μ|）定义信任域，对高频token更严格、对低频token更宽松，避免 PPO 对稀有token的过度惩罚，适合电商推荐中大量长尾item的生成式建模。

  - **用平滑正则代替硬掩码，提供连续纠正信号**：DPPO 的硬掩码在边界处梯度突变且无纠正。DRPO 的二次正则项产生有界、连续的梯度权重，边界内逐步衰减更新，边界外反向修正。这种设计可迁移到多智体训练、推荐模型RL微调等需要稳定策略更新的场景。

  - **正则项必须与优势绝对值 (|A|) 挂钩**：DRPO 通过 |A| 加权正则项，使信任域边界独立于奖励尺度，避免小优势token过纠、大优势token欠纠。在多轮对话Agent或推荐系统中，奖励信号常带噪声，该设计能增强训练鲁棒性。

  - **低精度 (如FP8) 训练场景下更稳健**：由于训练-推理数值不匹配加剧off-policy程度，DRPO 的 bounded gradient 在 FP8
  E2E 设置下仍保持稳定，而 ratio-based 方法（GRPO/SPO）易崩溃。对于需要降低成本的大规模工业训练（如电商LLM部署）具备直接工程价值。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现代 LLM RL 训练普遍采用 PPO/GRPO 等比率裁剪方法，但重要性比率在长尾词表上是分布偏移的糟糕代理——小概率token产生大比率但贡献微小概率质量，而高概率token即使比率变化不大也可能造成显著策略漂移。DPPO 改用基于散度的硬掩码，一旦token超出信任域便丢弃梯度，缺乏纠正信号且边界处梯度突变。因此需要一种既对齐真实分布几何、又提供连续平滑更新的信任域机制。

**方法关键点**：
- 从 DPPO 的 Binary-TV 视角度量绝对概率偏移 \(|π(y_t|s_t) - μ(y_t|s_t)|\)，构建 token 自适应的比率约束。
- 借鉴 SPO 的凹二次正则化思想，将硬掩码替换为优势加权二次项 \(|\hat{A}_t|\mu(y_t|s_t)(r_t-1)^2/(2\delta)\)，隐式惩罚 ℓ₂ 距离而非 χ² 距离。
- 梯度权重 \(w_t = 1 - \text{sign}(\hat{A}_t(r_t-1)) \cdot D_t^{\text{Bin-TV}}/\delta\) 连续有界：发散方向衰减至零再反转（纠正），收敛方向放大。信任域边界恰好位于 DPPO 的阈 \(\delta\) 处。
- 优势绝对值加权确保信任域边界不随奖励尺度变化，比纯 KL 或 TV 散度更稳定。

**关键实验**：
- 模型与数据：Qwen3-4B/30B-A3B/35B-A3B 基座、DeepSeek-R1-Distill-1.5B；数学推理任务 DAPO 数据集（13K 题），评测 AIME 2024/2025 average score。
- 对比方法：无信任域代理、GRPO (clip-higher)、SPO、DPPO。
- 主要结果：DRPO 在全部六种设置（含 FP8 推理/端到端低精度、MoE 架构）下均达到或超越最佳准确率，尤其在低精度场景下 GRPO/SPO 不稳定甚至崩溃，DRPO 依然稳健；相对于 DPPO 收敛更快且最终精度更高。
- 消融实验显示去除 \(|\hat{A}_t|\) 或改用 KL/TV 正则化均会导致性能下降和不稳定，证实了 DRPO 设计的必要性。

**核心洞见**："正则化的梯度形式比目标表面上的散度名称更重要；一个稳定的信任域需要基于绝对概率偏移的有界、连续梯度权重。"
