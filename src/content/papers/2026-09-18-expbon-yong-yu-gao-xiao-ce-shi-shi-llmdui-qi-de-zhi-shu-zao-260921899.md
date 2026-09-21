---
title: 'ExpBoN: Exponential-Noise Best-of-$n$ for Efficient Test-Time LLM Alignment'
title_zh: ExpBoN：用于高效测试时LLM对齐的指数噪声Best-of-n
authors:
- Yanxiao Liu
- Sicheng Wan
- Deniz Gündüz
affiliations:
- Imperial College London
- University of Washington
arxiv_id: '2609.21899'
url: https://arxiv.org/abs/2609.21899
pdf_url: https://arxiv.org/pdf/2609.21899
published: '2026-09-18'
collected: '2026-09-21'
category: LLM
direction: 推理时对齐 · 指数噪声BoN
tags:
- Best-of-n
- Inference-time Alignment
- Speculative Inference
- Exponential Noise
- LLM
one_liner: 提出指数噪声Soft Best-of-n，有限样本下指数收敛，结合GSI可减少推理计算39%-45%
practical_value: '- 在需从候选集按 reward 加权采样的场景（如生成式推荐、query/文案选择），可用 exponential-noise
  report-noisy-max 替代 softmax/Gumbel，有限样本下收敛更快，且期望奖励不低于 SBoN；其精确分解还可用于分布保持的 early
  exit。

  - 借鉴 GSI 的 draft-target 架构：用轻量 draft 模型生成候选、大模型验证和选择，结合 clipped reward（对 log-likelihood
  ratio 设上限）可避免无界重要性权重；clipping level 用历史数据 95 分位数校准，跨任务固定。

  - 工程实现中，利用 exponential noise 的 memorylessness：通过阈值截断和随机顺序扫描实现早停，命中时直接返回，可大幅降低实际计算量；在设计
  speculative decoding 或 Agent 多步推理时，可借鉴此早停策略。

  - 注意：指数噪声对 proxy reward 的过优化可能更激进，业务中需搭配 reward hacking 缓解、或对 reward 模型做校准。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：Best-of-n 是常用的推理时对齐方法，但 hard max 控制粗糙，soft BoN 虽然平滑但收敛慢（O(1/n)）。需要更高效、理论更优的变体。

**方法关键点**：
- ExpBoN：采样 n 个候选，计算 reward，加 Exp(1) 噪声，选 arg max(r_i/λ + E_i)，等价于 permute-and-flip。
- 具有精确有限 n 分解：输出分布 = (1-ρ^n) P* + ρ^n Q，其中 P* 是最优 tilted 分布，ρ 是未命中概率。因此 TV 距离 O(ρ^n)，KL 距离 O(ρ^{2n})，均为指数收敛，优于 SBoN 的多项式速率。
- 期望奖励不低于 SBoN（utility dominance），且 proxy-reward 下的 regret 有覆盖度依赖的指数级有限样本项。
- 结合 GSI：用 draft 模型生成候选、target 模型验证，奖励为 βr + min{d, C}，clip 处理无界似然比；利用指数噪声 memoryless 实现分布保持的 early stop（先小批量扫描，命中阈值直接返回，否则全扫描）。

**关键结果**：在 MATH500、MMLU-STEM、Minerva Math 上，用 Qwen2.5-Math（draft 1.5B / target 7B）和 Qwen3（1.7B / 14B）。ExpGSI 相比 GSI 节省计算：Qwen2.5-Math 从 n=2 到 16 节省 14%-39%，Qwen3 n=16 节省 45%；准确率与 GSI 相当（≤0.8 点），且优于 RSD 和 draft-only S-BoN。

**最值得记住的一句话**：用 exponential noise 替代 Gumbel noise 的 soft BoN，可获得精确的指数收敛分解，并在 speculative inference 中实现分布保持的 early exit，实现无损加速。
