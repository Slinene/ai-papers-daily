---
title: 'ConSA: Controllable Sparsity in Hybrid Attention via Learnable Allocation'
title_zh: 可控稀疏的混合注意力：通过可学习分配优化FA/SWA组合
authors:
- Yao Chen
- Yinqi Yang
- Junyuan Shang
- Xiangzhao Hao
- Simeng Zhang
- Yilong Chen
- Tingwen Liu
- Shuohuan Wang
- Dianhai Yu
affiliations:
- Institute of Information Engineering, Chinese Academy of Sciences
- School of Cyber Security, University of Chinese Academy of Sciences
- Baidu Inc.
arxiv_id: '2606.18056'
url: https://arxiv.org/abs/2606.18056
pdf_url: https://arxiv.org/pdf/2606.18056
published: '2026-06-16'
collected: '2026-06-17'
category: LLM
direction: 高效LLM推理 · 混合注意力稀疏分配
tags:
- Hybrid Attention
- Sparse Attention
- L0 Regularization
- Lagrangian Optimization
- Efficient Inference
- KV Cache
one_liner: 用L0正则化与增广拉格朗日约束学习全局/局部注意力的最优分配，实现可控稀疏并揭示底层局部、中层全局的一致结构
practical_value: '- 部署长上下文LLM（如query理解、会话摘要）时，可用ConSA动态决定哪些层/头用全局注意力、哪些用滑动窗口，在几乎不降性能的同时减少KV
  cache和推理计算。

  - 借鉴可控稀疏思想，在推荐系统的Transformer中为不同用户行为序列（短期 vs. 长期）分配不同的注意力范围，用类似L0-拉格朗日方法学习分配。

  - 增广拉格朗日约束可精确满足目标稀疏率，适合在业务中需要严格控制资源预算的场景（例如单机GPU限制）。

  - 手工设计混合注意力时可参考已发现的规律：底层放局部注意力、中层放全局注意力，避免均匀交错模式。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：LLM推理中全注意力（FA）的平方复杂度成为部署瓶颈，而滑动窗口注意力（SWA）虽高效但丢失长程依赖。现有混合架构（如Mistral、Gemma2）依靠手工规则交替FA/SWA，未考虑层与头间的异构行为，且不能灵活控制稀疏程度。

**方法**：
- 将FA/SWA分配形式化为稀疏约束优化问题，引入可学习二进制掩码z，通过hard concrete分布连续松弛，用L0正则化学习稀疏性。
- 采用增广拉格朗日乘子法精确满足用户指定的目标稀疏率ρ（SWA比例），支持**层粒度**或**KV头粒度**分配。
- 两阶段训练：Stage 1（1B token）联合优化模型参数θ、掩码参数α和拉格朗日乘子，使期望稀疏率E[ˆρ(z)]趋于ρ；Stage 2（100B token）二值化掩码（z = 𝟙[α>0]），固定分配继续预训练。

**关键结果**：
- 在1.7B模型、ρ=0.50下，**头粒度ConSA**比规则头粒度分配平均准确率高3.7%（46.45→49.06），甚至略超密集全注意力（47.83→49.06）。
- 消融实验证明L0-拉格朗日优于直接学习标量门再排序的校准方法，且拉格朗日约束在所有稀疏度下均能收敛。
- 学习到的结构一致：**底层偏好SWA，FA集中在中间连续层**；头级分配下，中间层SWA头比例最低，底层和顶层偏高，形成W形趋势。这与各层关注范围的多样性（从均匀分布到局部密集再到全局稀疏）高度吻合。

**核心启示**：受控的稀疏学习能自动发现优于手工设计的混合注意力格局，且底层放局部、中层放全局的规律在不同模型规模和稀疏度下保持稳定。
