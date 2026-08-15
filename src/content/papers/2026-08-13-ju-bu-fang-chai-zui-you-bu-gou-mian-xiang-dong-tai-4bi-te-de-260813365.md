---
title: 'When Local Variance Optimality Is Not Enough: RoPE-Aligned Q/K Rotations for
  Dynamic 4-Bit Quantisation'
title_zh: 局部方差最优不够：面向动态4比特量化的RoPE对齐Q/K旋转
authors:
- Shuhan Wang
- Yilin Luo
- Nan Xu
- Chi Wang Cheung
affiliations:
- University College London
arxiv_id: '2608.13365'
url: https://arxiv.org/abs/2608.13365
pdf_url: https://arxiv.org/pdf/2608.13365
published: '2026-08-13'
collected: '2026-08-15'
category: LLM
direction: RoPE对齐量化变换
tags:
- quantisation
- RoPE
- Hadamard
- LLM
- PTQ
one_liner: 发现RoPE对齐的成对旋转在动态W4A4KV4量化中未提升且增加困惑度，揭示代理目标与量化统计不匹配。
practical_value: '- 部署 LLM 做生成式推荐/Query 改写/Agent 决策时，若采用动态 4-bit 量化（W4A4KV4），优先保留标准全头
  Hadamard 旋转（QuaRot 风格）；实验显示用 RoPE 对齐成对旋转替换反而在多个 checkpoint、短/长上下文均增加 PPL。

  - 若业务必须引入 RoPE 结构变换，可采用成对旋转与 Hadamard 组合，并仅用 K 的校准数据估计共享角度；该方案能满足 ±0.05-PPL 偏差阈值，但无额外收益，可作为兼容性方案而非优化方案。

  - 工程实现注意：量化器步长通常由 tokenwise group range 决定，而代理目标基于位置平均协方差；两者统计错位会导致理论最优不转化为实际量化误差降低。评估量化方案时直接观察动态量化后的
  K range、相对量化误差和下游指标（如 PPL 或线上效果），不要依赖孤立代理指标。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：旋转式后训练量化通常对整头应用正交变换来抑制异常值误差，而 RoPE 将头划分为二维频率对。问题：尊重该分解的变换能否优于全头混合？

**方法关键点**：对 head-shared 参数化，作者推导在池化协方差、位置平均代理下最小化较大通道方差的旋转角，并实现到解析最优。在动态 W4A4KV4 设置下，将该成对旋转与全头 Hadamard 对比；也测试成对旋转与 Hadamard 组合、仅用 K 估计共享角度等变体；还通过从双通道到全头混合的受控插值观察支持度的影响。

**关键结果**：四个 checkpoint 上，用成对旋转替换全头 Hadamard 在短、长上下文长度均使困惑度上升；与 Hadamard 组合可满足 ±0.05-PPL 区间准则；仅从 K 估计角度能改善 pairwise-only 但未能缩小与全头混合的差距。插值实验显示 K range、相对量化误差和 PPL 退化随混合支持度增加而单调下降。核心原因是代理目标控制位置平均二阶矩，而动态量化器步长由 tokenwise group range 决定，且成对变换只有双通道支持；代理与混合支持与量化器统计错位时，结构化最优不转化为量化误差降低。
